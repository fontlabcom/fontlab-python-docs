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


def test_search_when_native_module_page_has_no_fragment_then_alias_reaches_module():
    row = {"location": "reference/fontlab.html", "title": "FontLab", "text": ""}
    symbols = {
        "fontlab": {"kind": "module", "url": "reference/fontlab.html#fontlab"},
        "fontlab.Node": {
            "kind": "class",
            "url": "reference/fontlab/Node.html#fontlab.Node",
        },
    }
    aliases = {"fly.fl": "fontlab", "fly.fl.Node": "fontlab.Node"}
    data = {"docs": [row]}
    qualify_titles(data, symbols, aliases)
    assert row["title"] == "fontlab", "module page must retain native primary identity"
    assert row["tags"] == ["fly.fl", "fontlab"], (
        "whole module needs its exact public alias"
    )
    assert row["boost"] == 100, (
        "module page must rank ahead of descendant prefix matches"
    )
    assert row["text"] == "", "duplicate page content must stay omitted"
    once = dict(row)
    qualify_titles(data, symbols, aliases)
    assert row == once, "whole-page module qualification must be idempotent"


def test_search_when_class_page_has_no_fragment_then_real_class_aliases_are_qualified():
    row = {
        "location": "reference/PythonQt/QtGui/QWidget.html",
        "title": "QWidget",
        "text": "Class.",
    }
    symbols = {
        "PythonQt.QtGui.QWidget": {
            "kind": "class",
            "url": row["location"] + "#PythonQt.QtGui.QWidget",
        }
    }
    qualify_titles(
        {"docs": [row]}, symbols, {"fly.qt.QtGui.QWidget": "PythonQt.QtGui.QWidget"}
    )
    assert row["title"] == "PythonQt.QtGui.QWidget"
    assert row["tags"] == ["QWidget", "fly.qt.QtGui.QWidget"]
    assert row["text"] == "Class."
    assert row["boost"] == 100


def test_search_when_authored_section_or_member_body_page_then_no_root_alias_is_added():
    section = {
        "location": "reference/fontlab.html#complete-member-index",
        "title": "Complete member index",
        "text": "Index.",
    }
    body = {
        "location": "reference/fontlab/members-001.html",
        "title": "Declarations",
        "text": "Body.",
    }
    guide = {"location": "guide.html", "title": "Guide", "text": "Guide text."}
    rows = [section, body, guide]
    original = [dict(row) for row in rows]
    symbols = {
        "fontlab": {"kind": "module", "url": "reference/fontlab.html#fontlab"},
        "fontlab.value": {
            "kind": "function",
            "url": "reference/fontlab/members-001.html#fontlab.value",
        },
    }
    qualify_titles({"docs": rows}, symbols, {"fly.fl": "fontlab"})
    assert rows == original, (
        "only genuine module/class pages and source fragments are qualified"
    )


def test_search_when_native_member_fragment_then_alias_tags_preserve_member_semantics():
    row = {
        "location": "reference/fontlab/Node.html#fontlab.Node.close",
        "title": "close",
        "text": "Member.",
        "tags": ["existing"],
    }
    symbols = {"fontlab.Node.close": {"kind": "function", "url": row["location"]}}
    qualify_titles(
        {"docs": [row]}, symbols, {"fly.fl.Node.close": "fontlab.Node.close"}
    )
    assert row["title"] == "fontlab.Node.close"
    assert row["tags"] == ["close", "existing", "fly.fl.Node.close"]
    assert "boost" not in row, "members must not receive the module/class priority"
    assert row["text"] == "Member."
