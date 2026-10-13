# this_file: scripts/search_identities.py
"""Make captured native identities searchable through MaterialX headings."""


def qualify_titles(data: dict, symbols: dict, aliases: dict | None = None) -> None:
    """Replace short API headings with their exact captured qualified names."""
    by_target = {}
    for alias, target in (aliases or {}).items():
        by_target.setdefault(target, []).append(alias)
    for row in data["docs"]:
        identifier = row["location"].partition("#")[2]
        if identifier in symbols:
            row["title"] = identifier
            names = [identifier.rsplit(".", 1)[-1], *by_target.get(identifier, [])]
            row["tags"] = sorted(set(row.get("tags", []) + names))
            if symbols[identifier].get("kind") in {"module", "class"}:
                row["boost"] = 100
