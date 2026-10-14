# this_file: scripts/a11y_check.py
"""R043: measured accessibility acceptance of a locally served built site."""

import argparse
import json
import threading
from collections.abc import Iterator
from contextlib import contextmanager
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, sync_playwright

DEFAULT_PAGES = [
    "index.html",
    "guide/install.html",
    "guide/native.html",
    "guide/pyside.html",
    "reference/fontlab/flNode.html",
    "reference/PythonQt/QtCore/Signal.html",
    "archive/fontlab7/index.html",
]
VIEWPORTS = [{"width": 1280, "height": 800}, {"width": 375, "height": 812}]
AUDIT = Path(__file__).with_name("a11y_checks.js").read_text()


@contextmanager
def serve_site(site: Path) -> Iterator[str]:
    """Own a loopback-only static server and always release its socket/thread."""
    server = ThreadingHTTPServer(
        ("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(site))
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def check_page(page: Page) -> dict:
    """Check a full focus cycle; required targets must appear within 40 Tabs."""
    result = page.evaluate(AUDIT)
    visited = set()
    reached = set()
    reach_budget = result.get("reach_budget", result["tab_budget"])
    for tab in range(1, result["tab_budget"] + 1):
        page.keyboard.press("Tab")
        focused = page.evaluate("window.a11yFocus()")
        if focused is None:
            continue
        if focused["selector"] in visited:
            break
        visited.add(focused["selector"])
        if tab <= reach_budget:
            reached.add(focused["selector"])
        result["focus"].append(focused)
        if not focused["indicator"]:
            result["failures"].append({"check": "focus", **focused})
        if focused.get("accessible_name") == "" and not any(
            f["check"] == "accessible_name" and f["selector"] == focused["selector"]
            for f in result["failures"]
        ):
            result["failures"].append(
                {
                    "check": "accessible_name",
                    "selector": focused["selector"],
                    "name": "",
                    "keyboard_focusable": True,
                }
            )
    for name, selector in result["targets"].items():
        if selector is None or selector not in reached:
            result["failures"].append(
                {
                    "check": "keyboard_reach",
                    "selector": selector,
                    "target": name,
                    "visited": len(reached),
                    "tab_budget": reach_budget,
                }
            )
    opener = result["targets"].get("nav")
    panel = result.get("nav_panel")
    if panel and opener in reached and not opened_nav_is_reachable(page, opener, panel):
        result["failures"].append(
            {
                "check": "keyboard_reach",
                "selector": opener,
                "target": "nav_after_open",
                "panel": panel,
            }
        )
    result["passed"] = not result["failures"]
    return result


def opened_nav_is_reachable(page: Page, opener: str, panel: str, tabs: int = 5) -> bool:
    """Enter on the opener must make a navigation link keyboard-focusable."""
    inside = f"document.activeElement?.closest({json.dumps(panel)}) != null"
    page.focus(opener)
    page.keyboard.press("Enter")
    page.wait_for_timeout(300)
    for _ in range(tabs + 1):
        if page.evaluate(inside):
            page.keyboard.press("Escape")
            return True
        page.keyboard.press("Tab")
    return False


def run(site: Path, pages: list[str]) -> dict:
    """Retain all page failures; browser/server errors are receipt failures too."""
    receipt = {"schema_version": 1, "results": [], "failures": []}
    try:
        if not site.is_dir():
            raise ValueError(f"Built site directory does not exist: {site}")
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            try:
                with serve_site(site) as url:
                    for path in pages:
                        for viewport in VIEWPORTS:
                            for scheme in ("light", "dark"):
                                context = browser.new_context(
                                    viewport=viewport, color_scheme=scheme
                                )
                                page = context.new_page()
                                entry = {
                                    "page": path,
                                    "viewport": viewport,
                                    "scheme": scheme,
                                }
                                try:
                                    response = page.goto(
                                        url + quote(path, safe="/"),
                                        wait_until="networkidle",
                                    )
                                    if response is None or response.status != 200:
                                        raise ValueError(
                                            f"Page HTTP status: {response.status if response else None}"
                                        )
                                    palette = page.locator(
                                        f'input[name="__palette"][data-md-color-media="(prefers-color-scheme: {scheme})"]'
                                    )
                                    if palette.count():
                                        palette.evaluate(
                                            "e => {e.checked = true; e.dispatchEvent(new Event('change', {bubbles:true})); document.body.dataset.mdColorScheme = e.dataset.mdColorScheme;}"
                                        )
                                    page.wait_for_timeout(700)
                                    entry.update(check_page(page))
                                except (PlaywrightError, OSError, ValueError) as error:
                                    entry.update(
                                        passed=False,
                                        failures=[
                                            {
                                                "check": "runtime",
                                                "selector": None,
                                                "error": str(error),
                                            }
                                        ],
                                    )
                                finally:
                                    context.close()
                                receipt["results"].append(entry)
            finally:
                browser.close()
    except (PlaywrightError, OSError, ValueError) as error:
        receipt["failures"].append(
            {"check": "runtime", "selector": None, "error": str(error)}
        )
    receipt["passed"] = (
        bool(receipt["results"])
        and not receipt["failures"]
        and all(r["passed"] for r in receipt["results"])
    )
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--pages", nargs="+", default=DEFAULT_PAGES)
    args = parser.parse_args()
    receipt = run(args.site.resolve(), args.pages)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        f"Accessibility acceptance: {'PASS' if receipt['passed'] else 'FAIL'}; receipt: {args.out}"
    )
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
