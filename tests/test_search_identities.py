# this_file: tests/test_search_identities.py
"""Search must index native member names, not only their short headings."""

import json
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from scripts.browser_smoke import QUERIES
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
    assert row["boost"] > 100, (
        "module results must precede descendant class prefix matches"
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
    assert row["boost"] > 100, (
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


def test_search_when_full_index_uses_materialx_worker_then_module_alias_is_discoverable():
    """Exercise the shipped worker's real ranking/grouping, not field presence."""
    root = Path(__file__).resolve().parents[1]
    index_path = root / ".build/site/search/search_index.json"
    coverage_path = root / ".build/coverage.json"
    if not index_path.exists() or not coverage_path.exists():
        pytest.skip("Full built source inventory and MaterialX index are required")
    data = json.loads(index_path.read_text())
    coverage = json.loads(coverage_path.read_text())
    identities = [
        (row["location"], row["title"], row["text"], tuple(row.get("tags", [])))
        for row in data["docs"]
    ]
    qualify_titles(data, coverage["symbols"], coverage["aliases"])
    assert identities == [
        (row["location"], row["title"], row["text"], tuple(row.get("tags", [])))
        for row in data["docs"]
    ], "Ranking changes must preserve every existing row, native identity and alias tag"
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    worker = next((root / ".build/site/assets/javascripts/workers").glob("search.*.js"))
    worker_source = worker.read_text()
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        context.route(
            "**/worker.js",
            lambda route: route.fulfill(
                body=worker_source, content_type="application/javascript"
            ),
        )
        context.route(
            "**/search_index.json",
            lambda route: route.fulfill(body=payload, content_type="application/json"),
        )
        context.route(
            "http://source-search.test/",
            lambda route: route.fulfill(
                body="<!doctype html><title>Private search fixture</title>",
                content_type="text/html",
            ),
        )
        page = context.new_page()
        page.goto("http://source-search.test/")
        page.evaluate("""async () => {
            const data = await (await fetch('/search_index.json')).json();
            data.options = {suggest: false};
            window.worker = new Worker('/worker.js');
            await new Promise((resolve, reject) => {
                const deadline = setTimeout(() => reject(Error('Worker readiness timeout')), 20000);
                worker.onmessage = ({data}) => {
                    if (data.type === 1) {clearTimeout(deadline); resolve();}
                };
                worker.onerror = reject;
                worker.postMessage({type: 0, data});
            });
        }""")
        queries = {
            **QUERIES,
            "pythonqtside.AppHandle": "reference/pythonqtside/_app/AppHandle.html",
            "pythonqtside.AppHandle.close": "#pythonqtside._app.AppHandle.close",
            "pythonqtside.run_app": "#pythonqtside._app.run_app",
        }
        observations = []
        for query, target in queries.items():
            result = page.evaluate(
                """query => new Promise((resolve, reject) => {
                const started = performance.now();
                const deadline = setTimeout(() => reject(Error('Search query timeout')), 2000);
                worker.onmessage = ({data}) => {
                    if (data.type === 3) {clearTimeout(deadline); resolve({
                        seconds: (performance.now() - started) / 1000,
                        groups: data.data.items.slice(0, 20).map(group =>
                            group.map(item => ({location: item.location, score: item.score})))
                    });}
                };
                worker.postMessage({type: 2, data: query});
            })""",
                query,
            )
            locations = [
                item["location"] for group in result["groups"] for item in group
            ]
            assert any(target in location for location in locations), (
                f"Existing consumer must discover {query} -> {target} in first 20 groups: {result}"
            )
            if query == "fly.fl":
                assert any(
                    item["location"].split("#")[0] == target
                    for item in result["groups"][0]
                ), "Exact module alias must rank its native module group first"
            observations.append(
                {
                    "query": query,
                    "target": target,
                    "seconds": round(result["seconds"], 3),
                }
            )
        browser.close()
    print(
        json.dumps(
            {
                "consumer": worker.name,
                "index_bytes": index_path.stat().st_size,
                "rows": len(data["docs"]),
                "queries": observations,
            },
            sort_keys=True,
        )
    )
