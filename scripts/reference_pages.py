# this_file: scripts/reference_pages.py
"""Render complete, paginated references through mkdocstrings directives."""

from __future__ import annotations

import json
import posixpath
from html import escape
from typing import Any

from scripts.doc_summary import (
    cell,
    module_list_summaries,
    overview,
    signature_cell,
    summary,
)

# Native modules whose landing page replaces the raw captured docstring with
# cleaned overview prose and grouped summary tables.
NATIVE_LANDINGS = {"fontlab", "fontgate", "fontpr", "FL", "PythonQt"}
# Captured module docstrings that only name the module get a written overview.
NATIVE_OVERVIEWS = {
    "PythonQt": (
        "PythonQt is the Qt binding built into FontLab. Scripts use it to build "
        "dialogs, panels and other user interface, and to work with Qt values such "
        "as points, rectangles, colours and fonts that the FontLab API returns. "
        "`PythonQt.QtCore`, `PythonQt.QtGui` and the other modules below expose "
        "the Qt classes that FontLab's build provides; the classes in this module "
        "are PythonQt's own helpers."
    ),
}


def relative_link(page: str, url: str) -> str:
    path, marker, fragment = url.partition("#")
    path = path.removesuffix(".html") + ".md"
    return posixpath.relpath(path, posixpath.dirname(page)) + (
        marker + fragment if marker else ""
    )


# Narrative guide for each documented package root (site-src/packages/).
PACKAGE_GUIDES = {
    "fontlab_echopy": ("Echopy", "echopy"),
    "fly": ("Fly", "fly"),
    "fontlabapp": ("Fontlabapp", "fontlabapp"),
    "fontlab_remopy": ("Remopy", "remopy"),
    "grablab": ("Grablab", "grablab"),
    "pythonqtside": ("Pythonqtside", "pythonqtside"),
    "fontlab_glyport": ("Glyport", "glyport"),
    "fontlab_fontport": ("Fontport", "fontport"),
    "fontlab_pens": ("Pens", "pens"),
    "typerig": ("TypeRig", "typerig"),
    "fontlab_aidus_agentus": ("Aidus Agentus", "aidus-agentus"),
    "fontlab_instamix": ("Instamix", "instamix"),
    "fontlab_plugmix": ("Plugmix", "plugmix"),
}


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
    guides = plan.get("guides", PACKAGE_GUIDES)  # the build passes only existing guides
    if kind == "module" and identifier in guides:
        name, slug = guides[identifier]
        guide = posixpath.relpath(f"packages/{slug}.md", posixpath.dirname(path))
        lines += [f"Overview, install and quick start: [{name} guide]({guide}).", ""]
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
                lines[-1:-1] = [
                    "      heading: " + json.dumps(member_display),
                    "      separate_signature: true",
                    "      show_signature_annotations: true",
                    "      annotations_path: source",
                ]
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
    if kind == "module" and identifier in NATIVE_LANDINGS:
        lines.insert(len(lines) - 1, "      show_docstring_description: false")
        return "\n".join(lines + _native_landing(path, plan, page)) + "\n"
    if kind in {"module", "class"}:
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
    symbol = plan["symbols"][identifier]
    if kind == "class" and symbol.get("bases"):
        lines += ["## Source bases", ""]
        for base in symbol["bases"]:
            target = base.get("target")
            lines += [
                f"- [`{base['expression']}`]({relative_link(path, plan['symbols'][target]['url'])})"
                if target
                else f"- `{base['expression']}` (not resolved from selected source)"
            ]
        lines += [""]
    inherited = symbol.get("inherited_members", {})
    if inherited:
        lines += [
            "## Inherited member index",
            "",
            "Source-proven inherited members; local declarations override these entries.",
            "",
        ]
        for name, target in sorted(inherited.items()):
            row = plan["symbols"][target]
            lines += [
                f"- [`{name}`]({relative_link(path, row['body_url'])}) — defined by `{target}`"
            ]
        lines += [""]
    if page["members"]:
        lines += [
            "## Complete member index",
            "",
            "Every captured member retains its own identity. Identical captured declaration text is linked once; this does not establish native inheritance or interchangeable objects.",
            "",
            "| Member | Kind | Signature | Summary |",
            "| --- | --- | --- | --- |",
        ]
        for member in page["members"]:
            row = plan["symbols"][member]
            text = cell(summary(row.get("docstring")))
            if row["body_target"] != member:
                text = (text + " " if text else "") + "(shared captured text)"
            lines += [
                f"| {_anchored(path, member, row)} | {row['kind']} | {signature_cell(row.get('signature'))} | {text} |"
            ]
    return "\n".join(lines) + "\n"


def _anchored(path: str, member: str, row: dict[str, Any]) -> str:
    link = relative_link(path, row["body_url"])
    return f'<span id="{escape(member, quote=True)}"></span>[`{row["name"]}`]({link})'


def _native_landing(path: str, plan: dict[str, Any], page: dict[str, Any]) -> list[str]:
    """Overview prose plus Functions, Classes and Constants tables for a native module."""
    symbols = plan["symbols"]
    module_doc = symbols[page["id"]].get("docstring")
    listed = module_list_summaries(module_doc)
    lines: list[str] = []
    prose = NATIVE_OVERVIEWS.get(page["id"]) or overview(module_doc)
    if prose:
        lines += ["## Overview", "", prose, ""]
    functions = [m for m in page["members"] if symbols[m]["kind"] == "function"]
    constants = [m for m in page["members"] if symbols[m]["kind"] != "function"]
    if functions:
        lines += ["## Functions", "", "| Function | Signature | Summary |", "| --- | --- | --- |"]
        for member in functions:
            row = symbols[member]
            lines += [
                f"| {_anchored(path, member, row)} | {signature_cell(row.get('signature'))} | {cell(summary(row.get('docstring')))} |"
            ]
        lines += [""]
    if page["modules"]:
        lines += ["## Modules", "", "| Module | Summary |", "| --- | --- |"]
        for name in page["modules"]:
            row = symbols[name]
            lines += [f"| [`{row['name']}`]({relative_link(path, row['url'])}) | {cell(summary(row.get('docstring')))} |"]
        lines += [""]
    if page["classes"]:
        lines += ["## Classes", "", "| Class | Summary |", "| --- | --- |"]
        for name in page["classes"]:
            row = symbols[name]
            text = summary(row.get("docstring")) or listed.get(row["name"], "")
            lines += [f"| [`{row['name']}`]({relative_link(path, row['url'])}) | {cell(text)} |"]
        lines += [""]
    if constants:
        lines += ["## Constants and attributes", "", "| Name | Type | Summary |", "| --- | --- | --- |"]
        for member in constants:
            row = symbols[member]
            kind = (row.get("signature") or "").removeprefix(": ")
            type_cell = signature_cell(kind) if kind else row["kind"]
            lines += [
                f"| {_anchored(path, member, row)} | {type_cell} | {cell(summary(row.get('docstring')))} |"
            ]
        lines += [""]
    return lines
