# this_file: tests/test_a11y_navigation.py
"""Primary site navigation must not be replaced by article tag metadata."""

import pytest
from playwright.sync_api import sync_playwright
from scripts.a11y_check import check_page, serve_site


@pytest.fixture
def browser_page():
    """Use the installed browser; launch or dependency failures remain errors."""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        try:
            yield browser.new_page()
        finally:
            browser.close()


@pytest.mark.browser
@pytest.mark.parametrize(
    "mode", ["desktop", "tabs", "mobile", "broken", "missing", "late"]
)
def test_audit_when_article_tags_follow_primary_navigation_then_target_primary(
    browser_page, tmp_path, mode
):
    """Tag metadata cannot replace the primary disclosure or hide its defects."""
    hidden = " hidden" if mode in ("mobile", "broken", "missing") else ""
    activate = (
        "onclick=\"document.getElementById('primary').hidden=false;"
        "this.setAttribute('aria-expanded','true');"
        "document.querySelector('#primary a').focus()\""
        if mode == "mobile"
        else ""
    )
    opener = (
        f'<button id="opener" aria-label="Site navigation" aria-controls="primary" '
        f'aria-expanded="false" {activate}>Navigation</button>'
        if mode in ("mobile", "broken")
        else ""
    )
    links = "".join(f'<a href="#main">Reference {i}</a> ' for i in range(45))
    primary_class = "md-tabs" if mode == "tabs" else "md-nav--primary"
    primary = f'<nav id="primary" class="{primary_class}"{hidden}><a href="#main">Home</a></nav>'
    html = (
        "<!doctype html><html><head><style>body{background:white;color:#111}"
        "a{color:#006}:focus{outline:3px solid #111}</style></head><body>"
        f'<nav aria-label="Header"{hidden}><a href="#main">Utility</a></nav>'
        '<input type="search" aria-label="Search">'
        + opener
        + (links if mode == "late" else "")
        + primary
        + '<main id="main"><article><h1>Browser notices</h1>'
        + (links if mode != "late" else "")
        + '<nav class="md-tags"><a href="#main">Python</a></nav>'
        + "</article></main></body></html>"
    )
    (tmp_path / "page.html").write_text(html)
    with serve_site(tmp_path) as url:
        browser_page.goto(url + "page.html")
        result = check_page(browser_page)
    assert result["reach_budget"] == 40, "Keep the original primary-target budget"
    if mode == "missing":
        assert result["targets"]["nav"] is None, (
            "Tags are not a fallback for missing site navigation"
        )
        assert any(
            f["check"] == "keyboard_reach" and f["target"] == "nav"
            for f in result["failures"]
        )
    elif mode == "broken":
        assert any(
            f["check"] == "keyboard_reach" and f["target"] == "nav_after_open"
            for f in result["failures"]
        ), result
    elif mode == "late":
        assert any(
            f["check"] == "keyboard_reach" and f["target"] == "nav"
            for f in result["failures"]
        ), result
    else:
        assert result["passed"], result["failures"]
        assert result["nav_panel"] == ("#primary" if mode == "mobile" else None)
        if mode in ("desktop", "tabs"):
            assert (
                browser_page.locator(result["targets"]["nav"]).evaluate(
                    "e => e.parentElement.id"
                )
                == "primary"
            ), "Reach the primary navigation, not an earlier utility link"
        # The original full cycle still measures late tag focus, beyond forty Tabs.
        tag = browser_page.locator(".md-tags a").evaluate(
            "e=>e.getBoundingClientRect().width"
        )
        assert tag > 0 and any(
            f["selector"].endswith(
                "article:nth-of-type(1) > nav:nth-of-type(1) > a:nth-of-type(1)"
            )
            for f in result["focus"]
        ), "Tag links remain in the real complete keyboard cycle"
