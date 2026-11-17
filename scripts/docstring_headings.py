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
FENCE = re.compile(r"^\s*(```|~~~)")
HEADING = re.compile(r"^(#{1,6})(\s+\S.*)$")


def normalize_headings(text: str) -> str:
    """Return text whose headings start at level 1 and never skip a level."""
    lines = text.split("\n")
    fenced, levels = False, []
    for line in lines:
        if FENCE.match(line):
            fenced = not fenced
        elif not fenced and (match := HEADING.match(line)):
            levels.append(len(match.group(1)))
    if not levels:
        return text
    shift, fenced, previous = min(levels) - 1, False, 0
    for index, line in enumerate(lines):
        if FENCE.match(line):
            fenced = not fenced
            continue
        match = None if fenced else HEADING.match(line)
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
