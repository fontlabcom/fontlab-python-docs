# this_file: scripts/browser_smoke.py
"""Exercise the real local reference UI and retain bounded browser evidence."""

import argparse
import json
import time
from pathlib import Path

from playwright.sync_api import sync_playwright

QUERIES = {
    "flNode": "reference/fontlab/flNode.html",
    "fontgate": "reference/fontgate.html",
    "fontpr": "reference/fontpr.html",
    "fontlabpr": "guide/native.html",
    "PythonQt.QtGui.QWidget.resize": "#PythonQt.QtGui.QWidget.resize",
    "fly.fl": "reference/fontlab.html",
    "GlyphsApp": "guide/glyphs.html",
    "Signal": "reference/PythonQt/QtCore/Signal.html",
    "PythonQt.QtXmlPatterns.QXmlQuery.setQuery": "#PythonQt.QtXmlPatterns.QXmlQuery.setQuery",
}


def search(page, query: str, target: str) -> dict:
    """Measure one search after initial index readiness with real key events."""
    field = page.locator(".md-search__input")
    field.fill(query)
    # MaterialX observes keyboard state as well as the input's value.
    field.press("Space")
    field.press("Backspace")
    started = time.monotonic()
    match = page.locator(f'.md-search-result__link[href*="{target}"]')
    match.first.wait_for(state="attached", timeout=2000)
    return {
        "query": query,
        "target": target,
        "seconds": round(time.monotonic() - started, 3),
        "url": match.first.get_attribute("href"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:8765/")
    parser.add_argument("--output", type=Path, default=Path(".build/browser"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    report = {"queries": [], "viewports": [], "errors": [], "shared_assets": {}}
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1440, "height": 1000})
        page.on("pageerror", lambda error: report["errors"].append(str(error)))
        page.on(
            "response",
            lambda response: (
                report["shared_assets"].update({response.url: response.status})
                if "i.fontlab.com/fltheme26/" in response.url
                else None
            ),
        )
        try:
            page.goto(args.url, wait_until="networkidle")
            assert page.locator(".md-search__input").count() == 1, (
                "one search owner required"
            )
            field = page.locator(".md-search__input")
            field.click()
            field.press_sequentially("flNode", delay=20)
            page.locator(
                '.md-search-result__link[href*="reference/fontlab/flNode.html"]'
            ).first.wait_for(timeout=20000)
            for query, target in QUERIES.items():
                report["queries"].append(search(page, query, target))
            field.press("Escape")
            for width, scheme in [
                (1440, "default"),
                (1440, "slate"),
                (390, "default"),
                (390, "slate"),
            ]:
                page.set_viewport_size({"width": width, "height": 844})
                page.evaluate(
                    "scheme => document.body.setAttribute('data-md-color-scheme', scheme)",
                    scheme,
                )
                page.goto(
                    args.url
                    + "reference/PythonQt/QtGui/QWidget/members-004.html#PythonQt.QtGui.QWidget.resize",
                    wait_until="networkidle",
                )
                page.evaluate(
                    "scheme => document.body.setAttribute('data-md-color-scheme', scheme)",
                    scheme,
                )
                page.wait_for_timeout(700)
                anchor = page.locator('[id="PythonQt.QtGui.QWidget.resize"]')
                assert anchor.count() == 1, "native deep anchor missing"
                overflow = page.evaluate(
                    "document.documentElement.scrollWidth > innerWidth"
                )
                report["viewports"].append(
                    {
                        "width": width,
                        "scheme": scheme,
                        "overflow": overflow,
                        "anchor_y": anchor.bounding_box()["y"],
                    }
                )
                page.screenshot(
                    path=str(args.output / f"reference-{width}-{scheme}.png"),
                    animations="disabled",
                )
                assert not overflow, "reference must wrap at viewport width"
            assert not report["errors"], "browser errors must be resolved"
            assert len(report["shared_assets"]) == 4, (
                "all shared theme assets must load"
            )
            assert all(status == 200 for status in report["shared_assets"].values()), (
                "shared assets must succeed"
            )
            report["passed"] = True
        finally:
            (args.output / "browser-report.json").write_text(
                json.dumps(report, indent=2) + "\n"
            )
            browser.close()
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
