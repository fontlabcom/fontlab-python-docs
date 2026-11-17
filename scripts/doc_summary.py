# this_file: scripts/doc_summary.py
"""Short summaries and cleaned overviews from captured native docstrings.

Used by ``scripts/reference_pages.py`` for module landing tables and member
indexes. Captured Proteus/FontGate docstrings often start with generated
placeholders ("flGlyph representation", "Data wrapper") or structural
blocks ("Constructors:", "Native bases:"); those never become summaries.
"""

from __future__ import annotations

import re
from html import escape

SUMMARY_LIMIT = 200
SIGNATURE_LIMIT = 110

_PLACEHOLDER = re.compile(
    r"^(?:[\w<>,.* ]{0,60}\brepresentation|\S+<[^>]*> doc|\S+ doc|doc|Data wrapper"
    r"|\S+ object|Call an MCP tool by name)\.?$",
    re.IGNORECASE,
)
_STRUCTURAL = ("Constructors:", "Native bases:", "Source:", "#", "```", "|", ">>>", "**")
_SUPPLEMENTAL = "Supplemental documentation:"
_FL_BANNER = re.compile(r"^\s*=+\s*$")
_DASH_LEAD = re.compile(r"^\s*[\w.]+(?:\([^)]*\))?\s+-\s+")
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[A-Z`\"(\[])")
_SIGNATURE_LINE = re.compile(
    r"^(?:\([^)]*\)\s+)?[\w\s<>*&:,\[\]]*?\w+\(.*\)\s*(?:->\s*\S+)?\s*;?\s*$"
)
_LIST_LINE = re.compile(r"^[\w<>,]+: \S")
_FENCE = re.compile(r"^```.*?^```[ \t]*$", re.MULTILINE | re.DOTALL)
_CODE = re.compile(r"`([^`]+)`")


def is_placeholder(text: str) -> bool:
    """True for generated leads that say nothing beyond the symbol name."""
    return bool(_PLACEHOLDER.match(" ".join(text.split())))


def _paragraphs(doc: str) -> list[str]:
    doc = _FENCE.sub("\n\n", doc)
    lines = [line for line in doc.splitlines() if not _FL_BANNER.match(line)]
    return [part.strip() for part in re.split(r"\n\s*\n", "\n".join(lines)) if part.strip()]


def _lead(paragraph: str) -> str:
    """Paragraph text without signature lines; a capitalised next line ends a sentence."""
    lines = [line.strip() for line in paragraph.splitlines()]
    while lines and _SIGNATURE_LINE.match(lines[0]):
        lines.pop(0)
    if not lines:
        return ""
    lines[0] = _DASH_LEAD.sub("", lines[0], count=1)
    if len(lines) > 1 and not lines[0].endswith((".", "!", "?", ",", ";", ":")) and lines[1][:1].isupper():
        lines = [lines[0] + "."]
    return " ".join(" ".join(lines).split())


def summary(doc: str | None) -> str:
    """First informative sentence of ``doc``, or an empty string."""
    for paragraph in _paragraphs(doc or ""):
        if paragraph.startswith(_SUPPLEMENTAL):
            paragraph = paragraph.removeprefix(_SUPPLEMENTAL).strip()
        if not paragraph or paragraph.startswith(_STRUCTURAL) or paragraph.startswith("- "):
            continue
        text = _lead(paragraph)
        if not text or " " not in text or is_placeholder(text) or text.endswith(":"):
            continue
        sentence = _SENTENCE_END.split(text, maxsplit=1)[0]
        if len(sentence) > SUMMARY_LIMIT:
            sentence = sentence[: SUMMARY_LIMIT - 1].rsplit(" ", 1)[0] + "…"
        return sentence[:1].upper() + sentence[1:]
    return ""


def module_list_summaries(doc: str | None) -> dict[str, str]:
    """``Name: summary`` lines of a native module docstring, placeholders removed."""
    found: dict[str, str] = {}
    for line in (doc or "").splitlines():
        if _LIST_LINE.match(line):
            name, _, text = line.partition(": ")
            if not is_placeholder(text):
                found[name] = text.strip()
    return found


def overview(doc: str | None) -> str:
    """Module docstring without its generated class list, headings demoted one level."""
    kept: list[str] = []
    for paragraph in _paragraphs(doc or ""):
        lines = paragraph.splitlines()
        if len(lines) > 1 and all(_LIST_LINE.match(line) for line in lines):
            continue
        if paragraph.startswith(_SUPPLEMENTAL):
            paragraph = paragraph.removeprefix(_SUPPLEMENTAL).strip()
        if paragraph.startswith("#"):
            paragraph = "#" + paragraph
        kept.append(paragraph)
    return "\n\n".join(kept)


def cell(text: str) -> str:
    """Markdown table cell: backtick spans become <code>, pipes cannot split columns."""
    parts = _CODE.split(text)
    html = "".join(
        f"<code>{escape(part)}</code>"
        if index % 2
        else escape(part, quote=False).replace("[", "&#91;").replace("]", "&#93;")
        for index, part in enumerate(parts)
    )
    return html.replace("|", "&#124;")


def signature_cell(signature: str | None) -> str:
    signature = (signature or "").removeprefix(": ")
    if not signature:
        return ""
    if len(signature) > SIGNATURE_LIMIT:
        signature = signature[: SIGNATURE_LIMIT - 1] + "…"
    return "<code>" + escape(signature).replace("|", "&#124;") + "</code>"
