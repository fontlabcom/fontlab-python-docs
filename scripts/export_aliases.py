# this_file: scripts/export_aliases.py
"""Read explicit exported import aliases without executing package code."""

import ast
from importlib.util import resolve_name


def exported_aliases(tree: ast.Module, module: str, *, package: bool) -> dict[str, str]:
    """Resolve source-declared public imports and small lazy export registries."""
    exports = None
    registries = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name):
            key = node.targets[0].id
            if key not in {"__all__", "_EXPORTS", "ALIASES"}:
                continue
            try:
                value = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                continue
            if key == "__all__":
                exports = set(value)
            elif isinstance(value, dict):
                registries[key] = value
    aliases = {}
    context = module if package else module.rpartition(".")[0]
    for node in tree.body:
        if not isinstance(node, ast.ImportFrom):
            continue
        origin = "." * node.level + (node.module or "")
        if node.level:
            origin = resolve_name(origin, context)
        for name in node.names:
            public = name.asname or name.name
            if public.startswith("_") or public == "*":
                continue
            if (exports is not None and public in exports) or (
                exports is None and node.level
            ):
                aliases[module + "." + public] = origin + "." + name.name
    for name, origin in registries.get("_EXPORTS", {}).items():
        if isinstance(name, str) and isinstance(origin, str):
            aliases[module + "." + name] = module + "." + origin + "." + name
    for name, target in registries.get("ALIASES", {}).items():
        if isinstance(name, str) and isinstance(target, str):
            aliases[module + "." + name] = (
                target.replace("echopy.", "")
                if target.startswith("echopy.")
                else target
            )
    return aliases
