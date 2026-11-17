# this_file: tests/test_browser_smoke.py
"""Unit tests for the browser smoke driver with a fake Playwright page."""

import json
import sys

import pytest

from scripts import browser_smoke

ASSETS = [f"https://i.fontlab.com/fltheme26/asset-{n}.css" for n in range(4)]


class FakeLocator:
    def __init__(self, page, selector):
        self.page, self.selector = page, selector

    @property
    def first(self):
        return self

    def fill(self, value):
        self.page.actions.append(("fill", value))

    def press(self, key):
        self.page.actions.append(("press", key))

    def click(self):
        self.page.actions.append(("click", self.selector))

    def press_sequentially(self, text, delay=0):
        self.page.actions.append(("type", text))

    def wait_for(self, **kwargs):
        self.page.actions.append(("wait", self.selector))

    def get_attribute(self, name):
        return self.selector.split('"')[1] if '"' in self.selector else None

    def count(self):
        return 1

    def bounding_box(self):
        return {"y": 120.0}


class FakePage:
    def __init__(self, *, overflow=False, asset_status=200, error=None):
        self.actions, self.handlers = [], {}
        self.overflow, self.asset_status, self.error = overflow, asset_status, error

    def on(self, event, handler):
        self.handlers[event] = handler

    def locator(self, selector):
        return FakeLocator(self, selector)

    def set_viewport_size(self, size):
        self.actions.append(("viewport", size["width"]))

    def evaluate(self, script, *args):
        return self.overflow if "scrollWidth" in script else None

    def wait_for_timeout(self, ms):
        pass

    def screenshot(self, path, animations):
        self.actions.append(("screenshot", path))


class FakeResponse:
    def __init__(self, url, status):
        self.url, self.status = url, status


class FakePlaywright:
    def __init__(self, page):
        self.page, self.closed = page, False
        self.chromium = self

    def launch(self, headless):
        return self

    def new_page(self, viewport):
        return self.page

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def fake_open_page(page, url):
    page.actions.append(("open", url))
    for asset in ASSETS:
        page.handlers["response"](FakeResponse(asset, page.asset_status))
    page.handlers["response"](FakeResponse("http://127.0.0.1:8765/other.js", 200))
    if page.error:
        page.handlers["pageerror"](page.error)


def run(monkeypatch, tmp_path, page):
    driver = FakePlaywright(page)
    monkeypatch.setattr(browser_smoke, "sync_playwright", lambda: driver)
    monkeypatch.setattr(browser_smoke, "open_page", fake_open_page)
    monkeypatch.setattr(sys, "argv", ["browser_smoke", "--url", "http://x/", "--output", str(tmp_path)])
    return driver


def test_search_when_target_attached_then_reports_href():
    page = FakePage()
    result = browser_smoke.search(page, "fontpr", "reference/fontpr.html")
    assert result["query"] == "fontpr" and result["url"] == "reference/fontpr.html"
    assert ("fill", "fontpr") in page.actions and ("press", "Backspace") in page.actions
    assert result["seconds"] >= 0


def test_main_when_site_is_clean_then_writes_passing_report(monkeypatch, tmp_path, capsys):
    page = FakePage()
    driver = run(monkeypatch, tmp_path, page)
    browser_smoke.main()
    report = json.loads((tmp_path / "browser-report.json").read_text())
    assert report["passed"] is True and driver.closed
    assert len(report["queries"]) == len(browser_smoke.QUERIES)
    assert [(v["width"], v["scheme"]) for v in report["viewports"]] == [
        (1440, "default"), (1440, "slate"), (390, "default"), (390, "slate")]
    assert len([a for a in page.actions if a[0] == "screenshot"]) == 4
    assert '"passed": true' in capsys.readouterr().out


@pytest.mark.parametrize(
    "page, message",
    [
        (FakePage(overflow=True), "wrap at viewport"),
        (FakePage(asset_status=404), "shared assets must succeed"),
        (FakePage(error="boom"), "browser errors"),
    ],
)
def test_main_when_check_fails_then_raises_and_still_writes_report(monkeypatch, tmp_path, page, message):
    driver = run(monkeypatch, tmp_path, page)
    with pytest.raises(AssertionError, match=message):
        browser_smoke.main()
    report = json.loads((tmp_path / "browser-report.json").read_text())
    assert "passed" not in report and driver.closed
