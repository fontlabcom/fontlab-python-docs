# this_file: scripts/docstring_headings.py
"""Keep Markdown headings inside native API docstrings in document order.

mkdocstrings renders a docstring heading of level L at L + heading_level, so a
class page (heading level 2) shows ``##`` as ``<h4>`` directly after the
class ``<h2>``. The Proteus reference prose enriched into Echopy starts at
``##`` and sometimes skips levels, which fails the accessibility heading-order
check. This extension rewrites only the rendered copy: the shallowest heading
becomes ``#`` and no heading goes more than one level below the one before.
Fenced code blocks are left alone. Source bytes and identities are unchanged.
"""

import re
from typing import Any

from griffe import Extension, Object

PREFIX = "fontlab_echopy."
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
HEADING = re.compile(r"^ {0,3}(#{1,6})(\s+\S.*)$")
UNDERLINE = re.compile(r"^ {0,3}(=+|-+)\s*$")
RULER = re.compile(r"^ {0,3}=+\s*$")
BLOCK_MARKER = re.compile(r"^ {0,3}([-*+>]|\d+[.)])(\s|$)")


def _fence_flags(lines: list[str]) -> list[bool]:
    """Mark lines inside or on fenced code blocks; a fence closes on its own kind."""
    flags, opener = [], None
    for line in lines:
        match = FENCE.match(line)
        if opener is None and match:
            opener = match.group(1)
            flags.append(True)
        elif opener is not None:
            if match and match.group(1)[0] == opener[0] and len(match.group(1)) >= len(opener):
                opener = None
            flags.append(True)
        else:
            flags.append(False)
    return flags


def _atx_from_setext(lines: list[str]) -> list[str]:
    """Rewrite setext and ``====``-banner headings as ATX headings."""
    fenced, out, index = _fence_flags(lines), [], 0
    while index < len(lines):
        line = lines[index]
        nxt = lines[index + 1] if index + 1 < len(lines) else ""
        after = lines[index + 2] if index + 2 < len(lines) else ""
        free = not any(fenced[index : index + 3])
        if free and RULER.match(line) and nxt.strip() and RULER.match(after) and (not out or not out[-1].strip()):
            out.append("# " + nxt.strip())
            index += 3
            continue
        starts_block = not out or not out[-1].strip()
        if free and starts_block and line.strip() and not HEADING.match(line) and not BLOCK_MARKER.match(line) and (match := UNDERLINE.match(nxt)):
            out.append(("# " if match.group(1)[0] == "=" else "## ") + line.strip())
            index += 2
            continue
        out.append(line)
        index += 1
    return out


def normalize_headings(text: str) -> str:
    """Return text whose headings start at level 1 and never skip a level."""
    lines = _atx_from_setext(text.split("\n"))
    fenced = _fence_flags(lines)
    levels = [len(m.group(1)) for line, f in zip(lines, fenced) if not f and (m := HEADING.match(line))]
    if not levels:
        return text
    shift, previous = min(levels) - 1, 0
    for index, line in enumerate(lines):
        match = None if fenced[index] else HEADING.match(line)
        if match:
            level = min(len(match.group(1)) - shift, previous + 1)
            lines[index] = "#" * level + match.group(2)
            previous = level
    return "\n".join(lines)


class NativeHeadings(Extension):
    """Normalize headings of every Echopy object docstring before rendering."""

    def on_instance(self, *, obj: Object, **kwargs: Any) -> None:
        if obj.docstring is None or not obj.path.startswith(PREFIX):
            return
        obj.docstring.value = normalize_headings(obj.docstring.value)
