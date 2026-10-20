# this_file: scripts/export_aliases.py
"""Read explicit exported import aliases without executing package code."""

import ast
from bisect import bisect_left
from collections import deque
from importlib.util import resolve_name
from typing import Any


def _export_contract(tree: ast.Module) -> tuple[set[str] | None, dict]:
    """Read literal export lists and registries without evaluating source."""
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
    return exports, registries


def exported_aliases(tree: ast.Module, module: str, *, package: bool) -> dict[str, str]:
    """Resolve source-declared public imports and small lazy export registries."""
    exports, registries = _export_contract(tree)
    aliases = {}
    context = module if package else module.rpartition(".")[0]
    for node in tree.body:
        if isinstance(node, ast.Import):
            for name in node.names:
                public = name.asname or name.name.partition(".")[0]
                explicit = (
                    public in exports
                    if exports is not None
                    else name.asname == name.name
                )
                if explicit and (not public.startswith("_") or exports is not None):
                    origin = name.name if name.asname else public
                    aliases[module + "." + public] = origin
            continue
        if not isinstance(node, ast.ImportFrom):
            continue
        origin = "." * node.level + (node.module or "")
        if node.level:
            origin = resolve_name(origin, context)
        for name in node.names:
            public = name.asname or name.name
            if (
                public.startswith("_") and (exports is None or public not in exports)
            ) or public == "*":
                continue
            if (exports is not None and public in exports) or (
                exports is None and (node.level or name.asname == name.name)
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


def resolved_aliases(
    aliases: dict[str, str], symbols: dict[str, dict[str, Any]]
) -> dict[str, str]:
    """Resolve explicit chains and expose only source-proven descendants.

    Targets remain source identities, not shared-body owners. Prefix resolution
    supports imports through aliased modules/classes without native inspection.
    Cycles and missing targets contribute no invented declarations.
    """

    def resolve(target: str) -> str | None:
        seen = set()
        while target not in symbols:
            parts = target.split(".")
            prefix = next(
                (
                    ".".join(parts[:i])
                    for i in range(len(parts), 0, -1)
                    if ".".join(parts[:i]) in aliases or ".".join(parts[:i]) in symbols
                ),
                None,
            )
            # A real replacement declaration also blocks ancestor alias fallback
            # when the requested descendant does not exist on that declaration.
            if prefix is None or prefix in symbols or prefix in seen:
                return None
            seen.add(prefix)
            target = aliases[prefix] + target[len(prefix) :]
        return target

    def overridden(public: str, root: str) -> bool:
        """Respect every explicit prefix below the alias being expanded."""
        prefix = root
        for part in public[len(root) + 1 :].split("."):
            prefix += "." + part
            if prefix in aliases or prefix in symbols:
                return True
        return False

    direct = {}
    for alias, original in sorted(aliases.items()):
        target = resolve(original)
        if target is None or alias == target or alias in symbols:
            continue
        direct[alias] = target
    resolved = dict(direct)
    exposed = {**{identifier: identifier for identifier in symbols}, **direct}
    identifiers = sorted(exposed)
    pending = deque(
        (alias, target, frozenset({target})) for alias, target in direct.items()
    )
    while pending:
        alias, target, seen = pending.popleft()
        if symbols[target]["kind"] not in {"class", "module"}:
            continue
        prefix = target + "."
        index = bisect_left(identifiers, prefix)
        while index < len(identifiers) and identifiers[index].startswith(prefix):
            descendant = identifiers[index]
            public = alias + descendant[len(target) :]
            # A replacement at any intervening prefix owns all its descendants.
            if not overridden(public, alias) and not any(
                part.startswith("_") and not part.startswith("__")
                for part in descendant[len(prefix) :].split(".")
            ):
                destination = exposed[descendant]
                resolved.setdefault(public, destination)
                # Follow source-declared re-exports inside module aliases. Stop
                # recursive module graphs at their repeated source target.
                if descendant in direct and destination not in seen:
                    pending.append((public, destination, seen | {destination}))
            index += 1
    return dict(sorted(resolved.items()))
