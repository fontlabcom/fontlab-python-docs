# this_file: scripts/search_identities.py
"""Make captured native identities searchable through MaterialX headings."""

MODULE_BOOST = 1000
CLASS_BOOST = 100


def qualify_titles(data: dict, symbols: dict, aliases: dict | None = None) -> None:
    """Replace short API headings with their exact captured qualified names."""
    by_page = {
        symbol["url"].partition("#")[0]: identifier
        for identifier, symbol in symbols.items()
        if symbol.get("kind") in {"module", "class"} and symbol.get("url")
    }
    by_target = {}
    for alias, target in (aliases or {}).items():
        by_target.setdefault(target, []).append(alias)
    for row in data["docs"]:
        page, marker, identifier = row["location"].partition("#")
        if not marker:
            identifier = by_page.get(page)
        if identifier in symbols:
            row["title"] = identifier
            names = [identifier.rsplit(".", 1)[-1], *by_target.get(identifier, [])]
            row["tags"] = sorted(set(row.get("tags", []) + names))
            kind = symbols[identifier].get("kind")
            if kind in {"module", "class"}:
                # MaterialX expands a query to a prefix wildcard and groups by
                # page. Give namespace roots priority over descendant classes.
                row["boost"] = MODULE_BOOST if kind == "module" else CLASS_BOOST

    # Shared occurrences have span anchors, not indexed headings. Attach their
    # exact names and aliases to the canonical body using the worker's tags field.
    by_location = {row["location"]: row for row in data["docs"]}
    additions = {}
    for identifier, symbol in symbols.items():
        if symbol.get("body_target", identifier) == identifier:
            continue
        location = symbol["body_url"]
        if location not in by_location:
            raise ValueError("Missing searchable canonical body: " + location)
        additions.setdefault(location, set()).update(
            [identifier, *by_target.get(identifier, [])]
        )
    for location, names in additions.items():
        row = by_location[location]
        row["tags"] = sorted(set(row.get("tags", [])) | names)


def verify_search_coverage(data: dict, symbols: dict, aliases: dict) -> None:
    """Require every source identity and alias on its occurrence or body row."""
    locations = {}
    for row in data["docs"]:
        for name in [row["title"], *row.get("tags", [])]:
            locations.setdefault(name, set()).add(row["location"])
    missing = []
    for name, target in {**{key: key for key in symbols}, **aliases}.items():
        symbol = symbols[target]
        allowed = {symbol["url"], symbol["body_url"]}
        if symbol["kind"] in {"module", "class"}:
            allowed.add(symbol["url"].partition("#")[0])
        if not locations.get(name, set()) & allowed:
            missing.append(name)
    if missing:
        raise ValueError(
            f"Missing searchable identities ({len(missing)}): {missing[:10]}"
        )
