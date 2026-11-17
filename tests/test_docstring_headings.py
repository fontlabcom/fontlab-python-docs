# this_file: tests/test_docstring_headings.py
from scripts.docstring_headings import normalize_headings


def test_normalize_headings_when_prose_starts_at_h2_then_shifted_to_h1():
    text = "Lead.\n\n## What\n\n### Sub\n\n## Next\n"
    assert normalize_headings(text) == "Lead.\n\n# What\n\n## Sub\n\n# Next\n"


def test_normalize_headings_when_level_skipped_then_clamped_to_one_deeper():
    assert normalize_headings("### A\n## B\n#### C\n") == "# A\n# B\n## C\n"


def test_normalize_headings_when_code_fence_then_comments_untouched():
    text = "## T\n\n```python\n# ── Step 1\n## not a heading\n```\n"
    assert normalize_headings(text) == "# T\n\n```python\n# ── Step 1\n## not a heading\n```\n"


def test_normalize_headings_when_no_headings_then_unchanged():
    assert normalize_headings("plain #tag text") == "plain #tag text"


def test_normalize_headings_when_fl_banner_then_becomes_h1():
    text = "===============\n  Anchor - class to represent Anchor point\n===============\nBody\n## Methods\n"
    assert normalize_headings(text) == "# Anchor - class to represent Anchor point\nBody\n## Methods\n"


def test_normalize_headings_when_setext_then_converted_to_atx():
    assert normalize_headings("Title\n=====\n\nPart\n----\n\n#### Deep\n") == "# Title\n\n## Part\n\n### Deep\n"


def test_normalize_headings_when_tilde_inside_backtick_fence_then_fence_stays_open():
    text = "## T\n```\n~~~\n## code\n```\n"
    assert normalize_headings(text) == "# T\n```\n~~~\n## code\n```\n"


def test_normalize_headings_when_heading_indented_then_normalized():
    assert normalize_headings("   ### A\n") == "# A\n"


def test_normalize_headings_when_paragraph_dash_line_continues_then_not_heading():
    text = "one\ntwo\n---\n"
    assert normalize_headings(text) == text
