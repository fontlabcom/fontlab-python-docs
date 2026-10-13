# this_file: scripts/api_inventory.py
"""Inventory source occurrences and plan complete references without imports."""

from __future__ import annotations

import ast
import hashlib
from pathlib import Path
from typing import Any

from .export_aliases import exported_aliases


def _name(node: ast.AST) -> str | None:
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        return node.name
    if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
        return node.target.id
    if (
        isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
    ):
        return node.targets[0].id
    return None


def _declarations(
    body: list[ast.stmt], parent: str, source: str
) -> list[dict[str, Any]]:
    rows = []
    for index, node in enumerate(body):
        name = _name(node)
        if (
            name is None
            or (name.startswith("_") and not name.startswith("__"))
            or name == "__all__"
        ):
            continue
        kind = (
            "class"
            if isinstance(node, ast.ClassDef)
            else "function"
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            else "attribute"
        )
        adjacent = body[index + 1] if index + 1 < len(body) else None
        attribute_doc = (
            adjacent.value.value
            if isinstance(adjacent, ast.Expr)
            and isinstance(adjacent.value, ast.Constant)
            and isinstance(adjacent.value.value, str)
            else None
        )
        doc = (
            ast.get_docstring(node, clean=False)
            if kind in {"class", "function"}
            else attribute_doc
        )
        fingerprint = hashlib.sha256(
            (ast.dump(node, include_attributes=False) + (attribute_doc or "")).encode()
        ).hexdigest()
        row = {
            "id": parent + "." + name,
            "name": name,
            "parent": parent,
            "kind": kind,
            "source": source,
            "line": node.lineno,
            "declaration_sha256": fingerprint,
            "docstring": doc,
            "occurrences": 1,
        }
        rows.append(row)
        if isinstance(node, ast.ClassDef):
            rows.extend(_declarations(node.body, row["id"], source))
    return rows


def inventory_sources(sources: list[tuple[Path, str]]) -> dict[str, Any]:
    """Index every public declaration; prefer authoritative adjacent stubs.

    Source roots contain packages. Never import package code during extraction.
    Identical text does not prove native identity or inheritance.
    """
    symbols, modules, inputs, aliases = {}, {}, [], {}
    for source_root, package in sources:
        package_root = source_root / package
        if not package_root.is_dir():
            raise FileNotFoundError(f"Missing source package: {package}")
        paths = {
            path.relative_to(source_root).with_suffix(""): path
            for path in package_root.rglob("*.py")
            if not any(
                part in {"tests", "__pycache__", ".venv"}
                for part in path.relative_to(package_root).parts
            )
        }
        paths.update(
            {
                path.relative_to(source_root).with_suffix(""): path
                for path in package_root.rglob("*.pyi")
            }
        )
        for relative, path in paths.items():
            if relative.name != "__init__":
                continue
            tree = ast.parse(path.read_bytes())
            module = ".".join(relative.parts).removesuffix(".__init__")
            aliases.update(
                exported_aliases(tree, module, package=relative.name == "__init__")
            )
        for relative, path in sorted(paths.items(), key=lambda pair: str(pair[0])):
            tree = ast.parse(path.read_bytes())
            parsed_module = ".".join(relative.parts).removesuffix(".__init__")
            aliases.update(
                exported_aliases(
                    tree, parsed_module, package=relative.name == "__init__"
                )
            )
            private = any(
                part.startswith("_") and part != "__init__"
                for part in relative.parts[1:]
            )
            source_module = ".".join(relative.parts).removesuffix(".__init__")
            targets = [
                target
                for target in aliases.values()
                if target.startswith(source_module + ".")
            ]
            if private and not targets:
                continue
            module = ".".join(relative.parts)
            if module.endswith(".__init__"):
                module = module.removesuffix(".__init__")
            canonical_module = module
            if package == "fontlab_echopy" and path.suffix == ".pyi":
                module = module.removeprefix("fontlab_echopy.")
            data = path.read_bytes()
            source = path.relative_to(source_root).as_posix()
            inputs.append(
                {
                    "source": source,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "bytes": len(data),
                }
            )
            modules[module] = {
                "id": module,
                "source": source,
                "docstring": ast.get_docstring(tree, clean=False),
            }
            symbols[module] = {
                "id": module,
                "kind": "module",
                "parent": None,
                "name": module.rsplit(".", 1)[-1],
                "source": source,
                "line": 1,
                "declaration_sha256": hashlib.sha256(data).hexdigest(),
                "docstring": modules[module]["docstring"],
                "occurrences": 1,
            }
            for row in _declarations(tree.body, module, source):
                if private and not any(
                    row["id"] == target or row["id"].startswith(target + ".")
                    for target in targets
                ):
                    continue
                row["canonical_id"] = canonical_module + row["id"][len(module) :]
                if row["id"] in symbols:
                    old = symbols[row["id"]]
                    if old["kind"] == "module" and row["kind"] == "class":
                        row["facets"] = [{"kind": "module", "source": old["source"]}]
                        row["occurrences"] += old["occurrences"]
                        symbols[row["id"]] = row
                        continue
                    old["occurrences"] += 1
                    old["declaration_sha256"] = hashlib.sha256(
                        (old["declaration_sha256"] + row["declaration_sha256"]).encode()
                    ).hexdigest()
                else:
                    symbols[row["id"]] = row
    return {
        "schema_version": 1,
        "modules": modules,
        "symbols": symbols,
        "inputs": inputs,
        "aliases": aliases,
    }


def _stem(identifier: str) -> str:
    return "reference/" + identifier.replace(".", "/")


def plan_pages(inventory: dict[str, Any], *, chunk_size: int = 40) -> dict[str, Any]:
    """Keep each identity/anchor while sharing exactly identical member text."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    symbols = {
        identifier: dict(row) for identifier, row in inventory["symbols"].items()
    }
    pages, body_owners, by_parent = {}, {}, {}
    for identifier, row in sorted(symbols.items()):
        if row["kind"] in {"module", "class"}:
            stem = _stem(identifier)
            pages[stem + ".md"] = {
                "kind": row["kind"],
                "id": identifier,
                "members": [],
                "classes": [],
                "modules": [],
            }
            row["url"] = stem + ".html#" + identifier
            row["body_target"] = identifier
        else:
            by_parent.setdefault(row["parent"], []).append(identifier)
    # Prefer native modules over aggregate Qt/private appearances, then stable ID.
    for identifier, row in symbols.items():
        if row["kind"] not in {"module", "class"}:
            continue
        parent = (
            row["parent"] if row["kind"] == "class" else identifier.rpartition(".")[0]
        )
        path = _stem(parent) + ".md"
        if path in pages:
            pages[path]["classes" if row["kind"] == "class" else "modules"].append(
                identifier
            )
    priority = lambda identifier: (
        identifier.startswith(("PythonQt.Qt.", "PythonQt.private.")),
        identifier,
    )
    for identifier in sorted(
        (i for i, row in symbols.items() if row["kind"] not in {"module", "class"}),
        key=priority,
    ):
        row = symbols[identifier]
        key = (row["kind"], row["name"], row["declaration_sha256"])
        row["body_target"] = body_owners.setdefault(key, identifier)
    for parent, identifiers in sorted(by_parent.items()):
        unique = [i for i in identifiers if symbols[i]["body_target"] == i]
        for index in range(0, len(unique), chunk_size):
            stem = _stem(parent) + f"/members-{index // chunk_size + 1:03}"
            members = unique[index : index + chunk_size]
            pages[stem + ".md"] = {"kind": "members", "id": parent, "members": members}
            for identifier in members:
                symbols[identifier]["body_url"] = stem + ".html#" + identifier
        for identifier in identifiers:
            row = symbols[identifier]
            row["url"] = _stem(parent) + ".html#" + identifier
        pages[_stem(parent) + ".md"]["members"] = identifiers
    for row in symbols.values():
        row["body_url"] = symbols[row["body_target"]].get(
            "body_url", symbols[row["body_target"]]["url"]
        )
    return {
        **inventory,
        "symbols": symbols,
        "pages": pages,
        "summary": {
            "modules": len(inventory["modules"]),
            "classes": sum(r["kind"] == "class" for r in symbols.values()),
            "member_identities": sum(
                r["kind"] not in {"module", "class"} for r in symbols.values()
            ),
            "declaration_occurrences": sum(r["occurrences"] for r in symbols.values()),
            "unique_member_bodies": len(body_owners),
            "generated_pages": len(pages),
        },
    }
