# this_file: scripts/static_inheritance.py
"""Source-proven class relationships; never infer bases from repeated text."""

import ast
from functools import cache
from importlib.util import resolve_name

from griffe import c3linear_merge

from .export_aliases import resolved_aliases


def add_inheritance(symbols: dict, records: list, aliases: dict) -> None:
    """Record bases and canonical inherited members using Griffe C3 ordering."""
    bindings = {}
    for relative, module, _, _, _, tree, _ in records:
        context = module if relative.name == "__init__" else module.rpartition(".")[0]
        names = {}
        for node in tree.body:
            if isinstance(node, ast.Import):
                names.update(
                    {
                        item.asname or item.name.split(".")[0]: item.name
                        if item.asname
                        else item.name.split(".")[0]
                        for item in node.names
                    }
                )
            elif isinstance(node, ast.ImportFrom):
                origin = "." * node.level + (node.module or "")
                origin = resolve_name(origin, context) if node.level else origin
                names.update(
                    {
                        item.asname or item.name: origin + "." + item.name
                        for item in node.names
                        if item.name != "*"
                    }
                )
        bindings[module] = names
    resolved = resolved_aliases(aliases, symbols)
    classes = {name: row for name, row in symbols.items() if row["kind"] == "class"}
    members = {}
    for name, row in symbols.items():
        members.setdefault(row["parent"], {})[row["name"]] = name
    for name, row in classes.items():
        module = name.rpartition(".")[0]
        while module not in bindings and "." in module:
            module = module.rpartition(".")[0]
        for base in row.get("bases", []):
            expression = base["expression"]
            first, _, suffix = expression.partition(".")
            imported = bindings.get(module, {}).get(first)
            candidates = (
                [imported + ("." + suffix if suffix else "")] if imported else []
            )
            parent = row["parent"]
            while parent:
                candidates.append(parent + "." + expression)
                parent = parent.rpartition(".")[0]
            candidates.append(expression)
            target = next(
                (
                    resolved.get(value, value)
                    for value in candidates
                    if resolved.get(value, value) in classes
                ),
                None,
            )
            base["target"] = target

    @cache
    def lineage(name, seen=()):
        if name in seen:
            raise ValueError("Cyclic source inheritance: " + name)
        bases = classes[name].get("bases", [])
        if any(
            base["target"] is None and base["expression"] != "object" for base in bases
        ):
            raise ValueError("Unresolved source base: " + name)
        targets = [base["target"] for base in bases if base["target"]]
        return [
            name,
            *c3linear_merge(
                *[lineage(target, (*seen, name)) for target in targets], targets
            ),
        ]

    for name, row in classes.items():
        inherited = {}
        try:
            ancestors = lineage(name)[1:]
        except ValueError as error:
            row["inheritance_status"] = str(error)
        else:
            for ancestor in ancestors:
                for member, target in members.get(ancestor, {}).items():
                    if member not in members.get(name, {}):
                        inherited.setdefault(member, target)
            row["inheritance_status"] = "source-proven"
        row["inherited_members"] = inherited
        for member, target in inherited.items():
            aliases.setdefault(name + "." + member, target)
