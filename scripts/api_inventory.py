# this_file: scripts/api_inventory.py
"""Inventory source occurrences and plan complete references without imports."""

from __future__ import annotations

import ast
import hashlib
from bisect import bisect_left
from pathlib import Path
from typing import Any

from .export_aliases import exported_aliases, resolved_aliases


NATIVE_FAMILIES = {"fontlab", "fontgate", "fontpr", "fontlabpr", "PythonQt"}


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
    body: list[ast.stmt],
    parent: str,
    source: str,
    decorator_imports: dict[str, str] | None = None,
    *,
    keep_private: bool = False,
) -> list[dict[str, Any]]:
    """Index public declarations; captured native sidecars keep `_x` names too."""
    rows = []
    properties = set()
    decorator_imports = decorator_imports or {}
    for index, node in enumerate(body):
        name = _name(node)
        if (
            name is None
            or (name.startswith("_") and not name.startswith("__") and not keep_private)
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
        labels, accessor = set(), None
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                value = decorator.func if isinstance(decorator, ast.Call) else decorator
                value = ast.unparse(value)
                first, _, suffix = value.partition(".")
                resolved = decorator_imports.get(first, first) + (
                    "." + suffix if suffix else ""
                )
                if resolved in {
                    "property",
                    "functools.cached_property",
                    "cached_property.cached_property",
                }:
                    labels.add("property")
                    if resolved != "property":
                        labels.add("cached")
                    accessor = "getter"
                elif name in properties and value in {
                    name + ".setter",
                    name + ".deleter",
                }:
                    labels.update(
                        {
                            "property",
                            "writable" if value.endswith(".setter") else "deletable",
                        }
                    )
                    accessor = value.rsplit(".", 1)[-1]
            if labels:
                kind = "attribute"
                properties.add(name)
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
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef))
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
        if isinstance(node, ast.ClassDef):
            row["bases"] = [{"expression": ast.unparse(base)} for base in node.bases]
        if labels:
            row["labels"] = sorted(labels)
            row["declarations"] = [
                {
                    "source": source,
                    "line": node.lineno,
                    "kind": "function",
                    "accessor": accessor,
                    "declaration_sha256": fingerprint,
                    "docstring": doc,
                }
            ]
        rows.append(row)
        if isinstance(node, ast.ClassDef):
            rows.extend(
                _declarations(
                    node.body,
                    row["id"],
                    source,
                    decorator_imports,
                    keep_private=keep_private,
                )
            )
    return rows


def _decorator_imports(tree: ast.Module) -> dict[str, str]:
    imports = {}
    for node in tree.body:
        if isinstance(node, ast.Import):
            imports.update({name.asname or name.name: name.name for name in node.names})
        elif isinstance(node, ast.ImportFrom) and not node.level:
            imports.update(
                {
                    name.asname or name.name: (node.module or "") + "." + name.name
                    for name in node.names
                }
            )
    return imports


def _occurrence(row: dict[str, Any]) -> dict[str, Any]:
    return {
        key: row[key]
        for key in ("source", "line", "kind", "declaration_sha256", "docstring")
    }


def inventory_sources(sources: list[tuple[Path, str]]) -> dict[str, Any]:
    """Index every public declaration; prefer authoritative adjacent stubs.

    Source roots contain packages. Never import package code during extraction.
    Identical text does not prove native identity or inheritance.
    """
    symbols, modules, inputs, aliases, records, available = {}, {}, {}, {}, [], {}
    seen_packages = set()
    for source_root, package in sources:
        if (source_root.resolve(), package) in seen_packages:
            continue
        seen_packages.add((source_root.resolve(), package))
        package_root = source_root / package
        if not package_root.is_dir():
            raise FileNotFoundError(f"Missing source package: {package}")
        all_paths = sorted(
            (
                path
                for path in package_root.rglob("*")
                if path.suffix in {".py", ".pyi"}
                and not any(
                    part in {"tests", "__pycache__", ".venv"}
                    for part in path.relative_to(package_root).parts
                )
            ),
            key=lambda path: path.relative_to(source_root).as_posix(),
        )
        paths = {
            path.relative_to(source_root).with_suffix(""): path
            for path in all_paths
            if path.suffix == ".py"
        }
        paths.update(
            {
                path.relative_to(source_root).with_suffix(""): path
                for path in all_paths
                if path.suffix == ".pyi"
            }
        )
        source_bytes = {}
        for path in all_paths:
            data = path.read_bytes()
            source = path.relative_to(source_root).as_posix()
            row = {
                "source": source,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
            }
            if source in inputs and inputs[source] != row:
                raise ValueError("Conflicting API source input: " + source)
            inputs[source] = row
            source_bytes[path] = data
        for relative, path in sorted(paths.items(), key=lambda pair: str(pair[0])):
            data = source_bytes[path]
            tree = ast.parse(data)
            parsed_module = ".".join(relative.parts).removesuffix(".__init__")
            aliases.update(
                exported_aliases(
                    tree, parsed_module, package=relative.name == "__init__"
                )
            )
            module = ".".join(relative.parts)
            if module.endswith(".__init__"):
                module = module.removesuffix(".__init__")
            canonical_module = module
            if package == "fontlab_echopy" and path.suffix == ".pyi":
                module = module.removeprefix("fontlab_echopy.")
            source = path.relative_to(source_root).as_posix()
            # Single-underscore members of captured native classes are native API.
            # Only Echopy's native sidecars lose their package prefix.
            declarations = _declarations(
                tree.body,
                module,
                source,
                _decorator_imports(tree),
                keep_private=module.partition(".")[0] in NATIVE_FAMILIES,
            )
            available[module] = {"kind": "module"}
            available.update({row["id"]: row for row in declarations})
            if module != canonical_module:
                aliases[canonical_module] = module
            records.append(
                (relative, module, canonical_module, source, data, tree, declarations)
            )
    resolved = resolved_aliases(aliases, available)
    targets = set(resolved.values())
    ordered_targets = sorted(targets)
    for relative, module, canonical_module, source, data, tree, declarations in records:
        private = any(
            part.startswith("_") and part != "__init__" for part in relative.parts[1:]
        )
        index = bisect_left(ordered_targets, module + ".")
        has_descendant = index < len(ordered_targets) and ordered_targets[
            index
        ].startswith(module + ".")
        if private and module not in targets and not has_descendant:
            continue
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
        for row in declarations:
            if private and not _visible(row, targets, ordered_targets):
                continue
            row["canonical_id"] = canonical_module + row["id"][len(module) :]
            if row["id"] in symbols:
                old = symbols[row["id"]]
                if old["kind"] == "module" and row["kind"] == "class":
                    row["facets"] = [{"kind": "module", "source": old["source"]}]
                    row["declarations"] = [_occurrence(old), _occurrence(row)]
                    row["occurrences"] += old["occurrences"]
                    symbols[row["id"]] = row
                    continue
                old["occurrences"] += 1
                old.setdefault("declarations", [_occurrence(old)]).extend(
                    row.get("declarations", [_occurrence(row)])
                )
                if "property" in old.get("labels", []):
                    old["labels"] = sorted(
                        set(old["labels"]) | set(row.get("labels", []))
                    )
                old["declaration_sha256"] = hashlib.sha256(
                    (old["declaration_sha256"] + row["declaration_sha256"]).encode()
                ).hexdigest()
            else:
                symbols[row["id"]] = row
    from .static_inheritance import add_inheritance

    add_inheritance(symbols, records, aliases)
    return {
        "schema_version": 1,
        "modules": modules,
        "symbols": symbols,
        "inputs": [inputs[name] for name in sorted(inputs)],
        "aliases": {**aliases, **resolved_aliases(aliases, symbols)},
    }


def _visible(row: dict[str, Any], targets: set[str], ordered: list[str]) -> bool:
    parts = row["id"].split(".")
    if any(".".join(parts[:i]) in targets for i in range(len(parts), 0, -1)):
        return True
    index = bisect_left(ordered, row["id"] + ".")
    return (
        row["kind"] == "class"
        and index < len(ordered)
        and ordered[index].startswith(row["id"] + ".")
    )


def _stem(identifier: str) -> str:
    return "reference/" + identifier.replace(".", "/")


def plan_pages(inventory: dict[str, Any], *, chunk_size: int = 40) -> dict[str, Any]:
    """Keep each identity/anchor while sharing exactly identical member text."""
    if chunk_size < 1:
        raise ValueError("chunk_size must be positive")
    symbols = {
        identifier: dict(row) for identifier, row in inventory["symbols"].items()
    }
    public_names = {}
    for alias, target in inventory["aliases"].items():
        if target not in symbols or any(
            part.startswith("_") for part in alias.split(".")
        ):
            continue
        parent = symbols[target].get("parent")
        if parent in symbols and symbols[parent]["kind"] == "class":
            alias_parent = alias.rpartition(".")[0]
            if inventory["aliases"].get(alias_parent, alias_parent) != parent:
                continue  # Inheritance exposes a member but does not rename its body.
        if alias.partition(".")[0] == target.partition(".")[0]:
            public_names.setdefault(target, []).append(alias)
    for identifier, row in symbols.items():
        if identifier.startswith(
            ("fontlab.", "fontgate.", "fontpr.", "fontlabpr.", "PythonQt.")
        ):
            continue
        if row["kind"] != "module" and any(
            part.startswith("_") for part in identifier.split(".")[:-1]
        ):
            candidates = public_names.get(identifier, [])
            if candidates:
                row["display_id"] = min(
                    candidates, key=lambda name: (name.count("."), len(name), name)
                )
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
