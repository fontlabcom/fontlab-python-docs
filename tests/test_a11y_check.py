# this_file: tests/test_a11y_check.py
"""Tiny browser fixtures prove each acceptance rule can pass and fail."""

import json
from pathlib import Path
from unittest.mock import Mock

import pytest
from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import sync_playwright

from scripts.a11y_check import SiteServer, check_page, main, open_page, serve_site

FIXTURES = Path(__file__).parent / "fixtures/a11y"


@pytest.fixture
def browser_page():
    with sync_playwright() as playwright:
        if not Path(playwright.chromium.executable_path).exists():
            pytest.skip(
                "Chromium is not installed; run python -m playwright install chromium"
            )
        # Launch errors (including sandbox denial) must remain visible failures.
        browser = playwright.chromium.launch(headless=True)
        try:
            yield browser.new_page()
        finally:
            browser.close()


def test_receipt_when_target_is_late_then_reach_fails_but_later_focus_is_still_checked():
    result = {
        "failures": [],
        "focus": [],
        "targets": {"nav": "a"},
        "tab_budget": 3,
        "reach_budget": 2,
        "needs_manual": [],
    }
    page = Mock()
    page.evaluate.side_effect = [
        result,
        {"selector": "button1", "indicator": True},
        {"selector": "button2", "indicator": True},
        {"selector": "a", "indicator": False},
    ]
    receipt = check_page(page)
    assert len(receipt["focus"]) == 3, (
        "Reach budget must not truncate focus-defect coverage"
    )
    assert {f["check"] for f in receipt["failures"]} == {"focus", "keyboard_reach"}, (
        receipt
    )


@pytest.mark.browser
@pytest.mark.parametrize("scheme", ["light", "dark"])
@pytest.mark.parametrize("width,height", [(1280, 800), (375, 812)])
def test_audit_when_accessible_fixture_then_all_rules_pass(
    browser_page, scheme, width, height
):
    browser_page.emulate_media(color_scheme=scheme)
    browser_page.set_viewport_size({"width": width, "height": height})
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + "pass.html")
        result = check_page(browser_page)
    assert result["passed"], result["failures"]
    assert result["text_elements"] > 0, "Contrast must actually measure fixture text"
    assert len(result["focus"]) >= 5, "Keyboard traversal must exercise the controls"


@pytest.mark.browser
@pytest.mark.parametrize(
    "check",
    [
        "overflow",
        "h1",
        "heading_order",
        "image_alt",
        "accessible_name",
        "contrast",
        "focus",
        "keyboard_reach",
    ],
)
def test_audit_when_rule_is_violated_then_receipt_has_measurement(browser_page, check):
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + check + ".html")
        result = check_page(browser_page)
    matching = [failure for failure in result["failures"] if failure["check"] == check]
    assert matching, f"Expected {check} failure: {result}"
    assert matching[0]["selector"], "Failure must identify its element"
    if check == "contrast":
        assert matching[0]["ratio"] < 4.5, "Do not weaken the AA threshold"


def test_cli_when_site_missing_then_writes_receipt_and_fails(tmp_path, monkeypatch):
    receipt = tmp_path / "receipt.json"
    monkeypatch.setattr(
        "sys.argv",
        ["a11y_check", "--site", str(tmp_path / "missing"), "--out", str(receipt)],
    )
    assert main() == 1, "Missing site must fail acceptance"
    data = json.loads(receipt.read_text())
    assert data["schema_version"] == 1 and not data["passed"], (
        "Receipt must record failure"
    )
    assert data["failures"][0]["check"] == "runtime", "Retain the operational error"


def test_receipt_when_contrast_needs_manual_then_does_not_fail_acceptance():
    result = {
        "failures": [],
        "focus": [],
        "targets": {},
        "tab_budget": 1,
        "needs_manual": [
            {"check": "contrast_unmeasurable", "selector": "p", "reason": "gradient"}
        ],
    }
    page = Mock()
    page.evaluate.side_effect = [result, None]
    receipt = check_page(page)
    assert receipt["passed"] and receipt["needs_manual"], (
        "Manual findings must survive without failing the gate"
    )


def test_receipt_when_unrendered_control_actually_receives_tab_focus_then_name_is_required():
    result = {
        "failures": [],
        "focus": [],
        "targets": {},
        "tab_budget": 1,
        "needs_manual": [],
    }
    page = Mock()
    page.evaluate.side_effect = [
        result,
        {
            "selector": "input",
            "indicator": True,
            "rendered": False,
            "accessible_name": "",
        },
    ]
    receipt = check_page(page)
    assert receipt["failures"] == [
        {
            "check": "accessible_name",
            "selector": "input",
            "name": "",
            "keyboard_focusable": True,
        }
    ], receipt
    assert not receipt["passed"], (
        "Observed keyboard focus prevents hidden-control exclusions from masking missing names"
    )


@pytest.mark.browser
@pytest.mark.parametrize(
    "fixture",
    [
        "focus_auto",
        "focus_transition",
        "names_hidden",
        "names_labelled",
        "keyboard_targets",
        "contrast_manual",
    ],
)
def test_audit_when_valid_focus_names_targets_or_manual_contrast_then_passes(
    browser_page, fixture
):
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + fixture + ".html")
        result = check_page(browser_page)
    assert result["passed"], result["failures"]
    if fixture == "contrast_manual":
        assert result["needs_manual"], (
            "Unmeasurable text needs a separate manual record"
        )
        assert all(
            f["check"] == "contrast_unmeasurable" for f in result["needs_manual"]
        ), result
    if fixture == "keyboard_targets":
        assert "skip" not in result["targets"], "A skip link is optional in this gate"
        assert result["focus"][0]["selector"] == result["targets"]["nav"], (
            "Ignore hidden desktop logo"
        )
        assert result["targets"]["search"].endswith("input:nth-of-type(2)"), (
            "Target search field, not mouse-only label"
        )


@pytest.mark.browser
@pytest.mark.parametrize(
    "fixture,check",
    [
        ("names_focusable", "accessible_name"),
        ("keyboard_nav_unreachable", "keyboard_reach"),
        ("focus_offscreen", "focus"),
        ("contrast_manual_unreadable", "contrast"),
    ],
)
def test_audit_when_real_defect_remains_then_fails(browser_page, fixture, check):
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + fixture + ".html")
        result = check_page(browser_page)
    assert any(f["check"] == check for f in result["failures"]), result
    assert not result["passed"], "Checker fixes must retain actual defects"


@pytest.mark.browser
def test_audit_when_nav_is_behind_working_disclosure_then_reach_passes(browser_page):
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + "nav_disclosure.html")
        result = check_page(browser_page)
    assert result["passed"], result["failures"]
    assert result["targets"]["nav"].endswith("button:nth-of-type(1)"), (
        "Closed navigation is reached through its keyboard opener"
    )


@pytest.mark.browser
def test_audit_when_disclosure_does_not_open_nav_then_reach_fails(browser_page):
    with serve_site(FIXTURES) as url:
        browser_page.goto(url + "nav_disclosure_broken.html")
        result = check_page(browser_page)
    assert any(
        f["check"] == "keyboard_reach" and f["target"] == "nav_after_open"
        for f in result["failures"]
    ), result


def test_site_server_when_browser_bursts_connections_then_backlog_holds_them():
    """Backlog 5 reset ~1 in 30 page loads' script requests (issue 104 blocker 4)."""
    assert SiteServer.request_queue_size >= 128


def test_open_page_when_third_party_request_hangs_then_ready_after_scripts_run(tmp_path):
    """networkidle waited on api.github.com; readiness is the page's own JS."""
    import time

    (tmp_path / "page.html").write_text(
        '<html class="no-js"><body><script>fetch("https://api.github.invalid/repo");'
        'setTimeout(() => document.documentElement.className = "js", 200)</script></body></html>'
    )
    (tmp_path / "broken.html").write_text('<html class="no-js"><body></body></html>')
    with sync_playwright() as playwright, serve_site(tmp_path) as url:
        if not Path(playwright.chromium.executable_path).exists():
            pytest.skip("Chromium is not installed")
        browser = playwright.chromium.launch(headless=True)
        try:
            page = browser.new_page()
            page.route("https://api.github.invalid/**", lambda route: None)  # never answers
            started = time.monotonic()
            open_page(page, url + "page.html")
            assert time.monotonic() - started < 5, "readiness waited on the hanging request"
            with pytest.raises(PlaywrightError):
                open_page(page, url + "broken.html", timeout_ms=1000)
        finally:
            browser.close()
