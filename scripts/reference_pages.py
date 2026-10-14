# this_file: scripts/reference_pages.py
"""Render complete, paginated references through mkdocstrings directives."""

from __future__ import annotations

import json
import posixpath
from html import escape
from typing import Any


def relative_link(page: str, url: str) -> str:
    path, marker, fragment = url.partition("#")
    path = path.removesuffix(".html") + ".md"
    return posixpath.relpath(path, posixpath.dirname(page)) + (
        marker + fragment if marker else ""
    )


def render_page(path: str, plan: dict[str, Any]) -> str:
    page = plan["pages"][path]
    identifier = page["id"]
    display = plan["symbols"][identifier].get("display_id", identifier)
    kind = page["kind"]
    title = (
        display
        if kind != "members"
        else display + " · declarations " + path.rsplit("-", 1)[-1].removesuffix(".md")
    )
    lines = [f"---\nthis_file: {path}\n---", f"# {title}", ""]
    if kind == "members":
        lines += [
            f"[Back to `{display}`]({relative_link(path, plan['symbols'][identifier]['url'])})",
            "",
        ]
        for member in page["members"]:
            lines += [
                f"::: {member}",
                "    options:",
                "      show_root_heading: true",
                "      heading_level: 2",
                "      members: false",
                "",
            ]
            member_display = plan["symbols"][member].get("display_id")
            if member_display:
                lines.insert(
                    len(lines) - 1, "      heading: " + json.dumps(member_display)
                )
        return "\n".join(lines)
    lines += [
        f"::: {identifier}",
        "    options:",
        "      members: false",
        "      show_root_heading: true",
        "      heading_level: 2",
        "",
    ]
    if display != identifier:
        lines.insert(len(lines) - 1, "      heading: " + json.dumps(display))
    if kind == "module":
        for label, identifiers in [
            ("Modules", page["modules"]),
            ("Classes", page["classes"]),
        ]:
            rows = [plan["symbols"][name] for name in identifiers]
            if rows:
                lines += ["## " + label, ""]
                lines += [
                    f"- [`{row['name']}`]({relative_link(path, row['url'])})"
                    for row in rows
                ]
                lines += [""]
    if page["members"]:
        lines += [
            "## Complete member index",
            "",
            "Every captured member retains its own identity. Identical captured declaration text is linked once; this does not establish native inheritance or interchangeable objects.",
            "",
            "| Member | Kind | Declaration |",
            "| --- | --- | --- |",
        ]
        for member in page["members"]:
            row = plan["symbols"][member]
            link = relative_link(path, row["body_url"])
            shared = (
                "Shared captured text"
                if row["body_target"] != member
                else "Signature and documentation"
            )
            lines += [
                f'| <span id="{escape(member, quote=True)}"></span>`{row["name"]}` | {row["kind"]} | [{shared}]({link}) |'
            ]
    return "\n".join(lines) + "\n"
