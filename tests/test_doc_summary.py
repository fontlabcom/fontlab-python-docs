# this_file: tests/test_doc_summary.py
"""Native landing tables and member indexes need informative one-line summaries."""

from scripts.doc_summary import (
    cell,
    module_list_summaries,
    overview,
    signature_cell,
    summary,
)


def test_summary_when_placeholder_lead_then_next_informative_sentence():
    doc = "flGlyph representation\n\nA glyph is one character. It has layers."
    assert summary(doc) == "A glyph is one character."


def test_summary_when_only_structural_or_placeholder_then_empty():
    assert summary("Data wrapper\n\nConstructors:\n  Foo()\n\nNative bases: object") == ""
    assert summary(None) == ""


def test_summary_when_supplemental_label_then_label_dropped():
    doc = "fgAnchor representation\n\nSupplemental documentation:\nA font-data anchor. More."
    assert summary(doc) == "A font-data anchor."


def test_summary_when_fl_banner_and_dash_lead_then_description():
    doc = "=====\n  Anchor - class to represent Anchor point\n====="
    assert summary(doc) == "Class to represent Anchor point"


def test_summary_when_signature_line_then_skipped():
    doc = "bool haveObject(uint);\n\nTrue when the node has an object."
    assert summary(doc) == "True when the node has an object."


def test_module_list_summaries_when_placeholders_then_only_real_entries():
    doc = "fgAnchor: Anchor representation\nfgAnchors: list of fgAnchor objects"
    assert module_list_summaries(doc) == {"fgAnchors": "list of fgAnchor objects"}


def test_overview_when_generated_class_list_then_removed_and_headings_demoted():
    doc = "Intro.\n\n## Architecture\n\nflA: flA representation\nflB: flB doc\n\nSupplemental documentation:\nMore."
    text = overview(doc)
    assert "flA:" not in text and "### Architecture" in text and text.endswith("More.")


def test_cell_when_pipes_brackets_and_code_then_table_safe():
    assert cell("a | b [x] `c|d`") == "a &#124; b &#91;x&#93; <code>c&#124;d</code>"


def test_signature_cell_when_attribute_or_long_then_trimmed():
    assert signature_cell(": int") == "<code>int</code>"
    assert signature_cell(None) == ""
    assert signature_cell("(" + "x, " * 80 + ")").endswith("…</code>")


def test_signature_cell_when_star_args_and_dunder_then_no_markdown_emphasis():
    import markdown

    star = signature_cell("(*args, **kwargs) -> Any")
    dunder = cell("Call `__init__` or `_private` first.")
    assert "*" not in star and "_" not in dunder.replace("&#95;", "")
    rendered = markdown.markdown(f"| a | b |\n| --- | --- |\n| {star} | {dunder} |", extensions=["tables"])
    assert "<em>" not in rendered and "<strong>" not in rendered
    assert "(&#42;args, &#42;&#42;kwargs)" in star and "&#95;&#95;init&#95;&#95;" in dunder
