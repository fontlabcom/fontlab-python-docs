# this_file: tests/test_search_identities.py
"""Search must index native member names, not only their short headings."""

from scripts.search_identities import qualify_titles


def test_search_when_native_member_anchor_exists_then_title_uses_complete_name():
    row = {
        "location": "reference/widget.html#PythonQt.QtGui.QWidget.resize",
        "title": "resize",
        "text": "Captured documentation.",
    }
    other = {
        "location": "guide.html#installation",
        "title": "Installation",
        "text": "Guide.",
    }
    data = {"docs": [row, other]}
    qualify_titles(data, {"PythonQt.QtGui.QWidget.resize": {}})
    assert row["title"] == "PythonQt.QtGui.QWidget.resize", (
        "native name must be searchable"
    )
    assert row["text"] == "Captured documentation.", "documentation must remain intact"
    assert other["title"] == "Installation", "authored headings must remain intact"
    qualify_titles(data, {"PythonQt.QtGui.QWidget.resize": {}})
    assert row["title"] == "PythonQt.QtGui.QWidget.resize", (
        "reprocessing must be idempotent"
    )


def test_search_when_public_alias_exists_then_alias_reaches_native_target():
    row = {
        "location": "reference/fontlab.html#fontlab",
        "title": "fontlab",
        "text": "Native API.",
    }
    qualify_titles(
        {"docs": [row]}, {"fontlab": {"kind": "module"}}, {"fly.fl": "fontlab"}
    )
    assert row["tags"] == ["fly.fl", "fontlab"], "alias must target the native API"
    assert row["boost"] == 100, (
        "module/class results must precede incidental prefix matches"
    )
