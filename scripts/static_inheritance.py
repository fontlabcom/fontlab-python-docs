# this_file: scripts/static_inheritance.py
"""Source-proven class relationships; never infer bases from repeated text."""

from functools import cache

from griffe import c3linear_merge

from .export_aliases import resolved_aliases
from .source_bindings import bind_bases


def add_inheritance(symbols: dict, records: list, aliases: dict) -> None:
    """Record bases and canonical inherited members using Griffe C3 ordering."""
    resolved = resolved_aliases(aliases, symbols)
    classes = {name: row for name, row in symbols.items() if row["kind"] == "class"}
    unresolved = bind_bases(records, classes, resolved)
    members = {}
    for name, row in symbols.items():
        members.setdefault(row["parent"], {})[row["name"]] = name

    @cache
    def lineage(name, seen=()):
        if name in seen:
            raise ValueError("Cyclic source inheritance: " + name)
        bases = classes[name].get("bases", [])
        if name in unresolved:
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
