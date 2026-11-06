# this_file: tests/test_pages_theme.py
"""The real consumer CSS must preserve result/Retry clicks and the outside overlay."""

from pathlib import Path

import pytest
from playwright.sync_api import Error as PlaywrightError, sync_playwright

ROOT = Path(__file__).resolve().parents[1]


@pytest.mark.browser
@pytest.mark.parametrize("blocked", [False, True])
def test_search_dialog_when_reparented_then_results_retry_and_outside_close_work(blocked):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        try:
            page = browser.new_page(viewport={"width": 1280, "height": 800})
            page.set_default_timeout(500)
            page.set_content('''<!doctype html><title>Reparented search</title>
<style>.fl-local-search{position:fixed;inset:0;z-index:1001}
.md-search__overlay{position:absolute;inset:0;z-index:1}
.md-search__inner{position:relative;margin:100px auto;width:600px;background:white}
a,button,input{display:block;padding:15px}</style>
<button id="open">Open search</button>
<div class="md-search fl-local-search" hidden>
 <label class="md-search__overlay"></label><div class="md-search__inner">
 <input aria-label="Search"><a id="result" href="#result">Native result</a>
 <button id="retry">Retry search</button></div></div>
<script>
const dialog=document.querySelector('.fl-local-search'),opener=document.querySelector('#open');
opener.onclick=()=>{dialog.hidden=false;dialog.querySelector('input').focus()};
const close=()=>{dialog.hidden=true;opener.focus()};
document.querySelector('.md-search__overlay').onclick=close;
document.addEventListener('keydown',e=>{if(e.key==='Escape')close()});
document.querySelector('#result').onclick=()=>{window.resultClicked=true};
document.querySelector('#retry').onclick=()=>{window.retryClicked=true};
</script>''')
            page.add_style_tag(path=str(ROOT / "src_docs/md/assets/reference.css"))
            page.locator("#open").click()
            if blocked:
                page.locator(".md-search__inner").evaluate("e=>e.style.zIndex='0'")
                with pytest.raises(PlaywrightError, match="Timeout"):
                    page.locator("#result").click()
                assert not page.evaluate("!!window.resultClicked")
                return
            page.locator("#result").click()
            page.locator("#retry").click()
            assert page.evaluate("window.resultClicked && window.retryClicked")
            page.locator(".md-search__overlay").click(position={"x": 10, "y": 10})
            assert page.locator(".fl-local-search").is_hidden()
            assert page.locator("#open").evaluate("e=>e===document.activeElement")
            page.locator("#open").click()
            page.keyboard.press("Escape")
            assert page.locator(".fl-local-search").is_hidden()
            assert page.locator("#open").evaluate("e=>e===document.activeElement")
        finally:
            browser.close()
