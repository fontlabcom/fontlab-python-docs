# this_file: scripts/source_visibility.py
"""Keep explicit exports and the source-proven bases needed by public classes.

Private implementations are indexed only when a public declaration reaches
them. Unrelated private classes and private members stay outside the reference.
No package code runs; base bindings use the existing source-order resolver.
"""

from bisect import bisect_left
from pathlib import Path
from typing import Any

from .export_aliases import _export_contract, resolved_aliases
from .source_bindings import bind_bases


def private_module(relative: Path) -> bool:
    return any(
        part.startswith("_") and part != "__init__" for part in relative.parts[1:]
    )


def visible(row: dict[str, Any], targets: set[str], ordered: list[str]) -> bool:
    parts = row["id"].split(".")
    if any(".".join(parts[:i]) in targets for i in range(len(parts), 0, -1)):
        return True
    index = bisect_left(ordered, row["id"] + ".")
    return (
        row["kind"] == "class"
        and index < len(ordered)
        and ordered[index].startswith(row["id"] + ".")
    )


def _private_owners_exposed(
    identifier: str, module: str, targets: set[str], ordered: list[str]
) -> bool:
    """A private class needs its own export/base path, not just a public parent."""
    parts = identifier.removeprefix(module + ".").split(".")
    for i, part in enumerate(parts):
        if not part.startswith("_") or part.startswith("__"):
            continue
        owner = module + "." + ".".join(parts[: i + 1])
        index = bisect_left(ordered, owner + ".")
        descendant = index < len(ordered) and ordered[index].startswith(owner + ".")
        if owner not in targets and not descendant:
            return False
    return True


def visible_declaration(
    row: dict[str, Any],
    module: str,
    relative: Path,
    targets: set[str],
    ordered: list[str],
    native_families: set[str],
) -> bool:
    native = module.partition(".")[0] in native_families
    if not native and not _private_owners_exposed(row["id"], module, targets, ordered):
        return False
    private_owner = not native and any(
        part.startswith("_") and not part.startswith("__")
        for part in row["id"].removeprefix(module + ".").split(".")
    )
    return not (private_module(relative) or private_owner) or visible(
        row, targets, ordered
    )


def _base_closure(classes: dict, unresolved: set[str], pending: list[str]) -> set[str]:
    """Keep only statically bound base identities; cycles cannot loop here."""
    bases, seen = set(), set()
    while pending:
        name = pending.pop()
        if name in seen or name in unresolved:
            continue
        seen.add(name)
        for base in classes[name].get("bases", []):
            target = base["target"]
            if target in classes:
                bases.add(target)
                pending.append(target)
    return bases


def exposed_targets(
    records: list, available: dict, aliases: dict, native_families: set[str]
) -> set[str]:
    """Extend public export targets with the bases their class headers prove."""
    resolved = resolved_aliases(aliases, available)
    targets = set(resolved.values())
    for _, module, _, _, _, tree, _ in records:
        exports, _ = _export_contract(tree)
        targets.update(
            module + "." + name
            for name in exports or ()
            if module + "." + name in available
        )
    ordered = sorted(targets)
    classes = {name: row for name, row in available.items() if row["kind"] == "class"}
    unresolved = bind_bases(records, classes, resolved)
    pending = []
    for relative, module, _, _, _, _, declarations in records:
        for row in declarations:
            if (
                row["kind"] == "class"
                and row["id"] in classes
                and visible_declaration(
                    row, module, relative, targets, ordered, native_families
                )
            ):
                pending.append(row["id"])
    return targets | _base_closure(classes, unresolved, pending)
