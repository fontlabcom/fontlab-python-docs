# this_file: tests/test_search_backend.py
"""Use the installed MaterialX UI, prefix routes and real worker network failures."""

import json
import subprocess
import sys

from playwright.sync_api import sync_playwright
from search_fixture import browser_corpus, start_server

from scripts.search_shards import ROOT, build_shards


def test_backend_routing_semantics_and_malformed_metadata():
    result = subprocess.run(
        ["node", "--test", str(ROOT / "scripts/search_backend/tests.cjs")],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_installed_template_suggestions_failure_retry_and_stale_queries(tmp_path):
    """One context/tab/stock UI: actual configured suggestion plus startup and row recovery."""
    import yaml

    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "index.md").write_text("# SignalWidget\n\nSearch fixture.\n")
    (docs / "nested.md").write_text("# Nested\n")
    config = {
        "site_name": "Complete search fixture",
        "site_url": "http://localhost/docs/",
        "docs_dir": str(docs),
        "site_dir": str(tmp_path / "site"),
        "theme": {
            "name": "materialx",
            "custom_dir": str(ROOT / "overrides"),
            "search_index_only": True,
            "features": ["search.suggest", "search.highlight", "navigation.instant"],
        },
        "plugins": ["/search"],
    }
    path = tmp_path / "mkdocs.yml"
    path.write_text(yaml.safe_dump(config))
    result = subprocess.run(
        [sys.executable, "-m", "properdocs", "build", "--strict", "-f", str(path)],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    site = tmp_path / "site"
    for relative, prefix in (("index.html", ""), ("nested/index.html", "../")):
        html = (site / relative).read_text()
        assert (
            f'data-worker="{prefix}assets/javascripts/workers/complete-search.js"'
            in html
        )
        assert html.index("complete-search-ui.js") < html.index(
            "assets/javascripts/bundle."
        )
    corpus = browser_corpus()
    index = site / "search/search_index.json"
    index.write_text(json.dumps(corpus))
    build_shards(index, shard_bytes=80)
    manifest = json.loads((site / "search/complete/manifest.json").read_text())
    policy = {"startup": True, "missing": None, "delay": None, "corrupt": False}
    requests = []

    server = start_server(tmp_path, site, policy, requests)
    try:
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            page = browser.new_page()
            errors = []
            page.on("pageerror", lambda error: errors.append(str(error)))
            page.goto(f"http://127.0.0.1:{server.server_port}/docs/")
            settings = page.locator("#__config").text_content()
            assert json.loads(settings)["features"] == config["theme"]["features"]
            assert len(json.loads(settings)["translations"]) == 12
            query = page.locator('[data-md-component="search-query"]')
            query.fill("sig")
            panel = page.locator("[data-complete-search-status]")
            panel.wait_for(state="visible")
            assert "unavailable" in panel.text_content()
            assert not any("rows-" in request for request in requests), (
                "READY cannot hide row prefetch"
            )
            policy["startup"] = False
            panel.locator("button").click()
            page.wait_for_function(
                "document.querySelector('.md-search__output').dataset.completeSearchState === 'ready'"
            )
            query.fill("")
            for key in "sig":
                query.press(key)
            page.wait_for_function(
                "document.querySelector('[data-md-component=search-suggest]').textContent === 'signalwidget'"
            )
            query.press("End")
            page.wait_for_function(
                "document.querySelector('[data-md-component=search-query]').selectionStart === 3"
            )
            query.press("ArrowRight")
            page.wait_for_function(
                "document.querySelector('[data-md-component=search-query]').value === 'signalwidget'"
            )
            assert query.input_value() == "signalwidget", (
                "Configured stock suggestion keyboard action must work"
            )
            policy["missing"] = manifest["shards"][1]["file"]
            query.fill("Beta")
            query.press("Space")
            query.press("Backspace")
            panel.wait_for(state="visible")
            assert page.locator(".md-search-result__list").is_hidden(), (
                "Never show partial/stale matches after failure"
            )
            policy["missing"] = None
            panel.locator("button").click()
            page.wait_for_function(
                "document.querySelector('.md-search__output').dataset.completeSearchState === 'ready'"
            )
            page.locator(
                '.md-search-result__list a[href*="nested/index.html"]'
            ).first.wait_for(state="attached")
            assert (
                page.locator(
                    '.md-search-result__list a[href*="nested/index.html"]'
                ).count()
                > 0
            )
            policy["delay"] = manifest["shards"][2]["file"]
            query.fill("Gamma")
            query.press("Space")
            query.press("Backspace")
            panel.wait_for(state="visible", timeout=4000)
            query.fill("Gamma ")
            query.press("Backspace")
            query.fill("sig")
            query.press("Space")
            query.press("Backspace")
            page.wait_for_function(
                "document.querySelector('.md-search__output').dataset.completeSearchState === 'ready'"
            )
            assert (
                page.locator('.md-search-result__list a[href*="gamma.html"]').count()
                == 0
            )
            query.fill("zzzznomatches")
            query.press("Space")
            query.press("Backspace")
            page.wait_for_function(
                "document.querySelector('.md-search__output').dataset.completeSearchState === 'ready'"
            )
            assert panel.is_hidden(), (
                "Ordinary no matches must differ from unavailable search"
            )
            page.wait_for_function(
                "document.querySelector('.md-search-result > .md-search-result__meta').textContent.includes('No matching documents')"
            )
            assert (
                "No matching documents"
                in page.locator(".md-search-result__meta").last.text_content()
            )
            policy["corrupt"] = True
            page.goto(f"http://127.0.0.1:{server.server_port}/docs/nested/")
            query.fill("Beta")
            panel.wait_for(state="visible")
            assert "unavailable" in panel.text_content(), (
                "Damaged compressed metadata must fail visibly before READY"
            )
            policy["corrupt"] = False
            panel.locator("button").click()
            page.wait_for_function(
                "document.querySelector('.md-search__output').dataset.completeSearchState === 'ready'"
            )
            assert any(request.endswith("postings.bin.gz") for request in requests), (
                "Plain static serving must use explicit gzip files"
            )
            assert not errors, errors
            browser.close()
    finally:
        server.shutdown()
        server.server_close()
