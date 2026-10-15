# this_file: scripts/interaction_check.py
"""R043: interaction receipts for deep links, type links, aliases, late search and keyboard."""

import argparse
import json
import re
import time
import zlib
from collections.abc import Callable
from contextlib import nullcontext
from pathlib import Path
from urllib.parse import urljoin

from playwright.sync_api import Error as PlaywrightError
from playwright.sync_api import Page, sync_playwright

from scripts.a11y_check import opened_nav_is_reachable, serve_site

VIEWPORTS = [{"width": 1280, "height": 800}, {"width": 375, "height": 812}]
SCHEMES = ("light", "dark")
TAB_BUDGET = 40
# Worker shard fetches abort after this (scripts/search_backend/query.js).
SHARD_DEADLINE_MS = 1800
PLAN = {
    "deep_link": {
        "page": "reference/fontlab/flNode.html",
        "anchor": "fontlab.flNode.isExtreme",
    },
    "type_link": {
        "page": "reference/fontlab_remopy/control/FontLab/members-001.html",
        "member": "fontlab_remopy.control.FontLab.run",
        "target": "reference/fontlab_remopy/execution/ExecutionResult.html#fontlab_remopy.execution.ExecutionResult",
    },
    "param_type_link": {
        "case": "param_type_link",
        "page": "reference/fontlab_glyport/receipt/members-001.html",
        "member": "fontlab_glyport.receipt.write_receipt",
        "target": "reference/fontlab_glyport/receipt/Receipt.html#fontlab_glyport.receipt.Receipt",
    },
    "alias": {
        "name": "fly.fg.fgKerning",
        "canonical": "fontgate.fgKerning",
        "search_page": "reference/fontlab/flNode.html",
        "legacy": "fontgate.fgAnchor.html#-fontgate.fgAnchor.copy",
    },
    "search": {
        "page": "reference/fontlab/flNode.html",
        "query": "decode_execution",
        "target": "reference/fontlab_remopy/execution/members-001.html#fontlab_remopy.execution.decode_execution",
        "delay_ms": 1500,
    },
    "keyboard": {"page": "reference/fontlab/flNode.html"},
    # Decision (issue 104): a shard slower than the 1.8 s deadline shows Retry with no
    # partial results; Retry doubles the deadline (3.6 s here), so the slow shard completes.
    "search_slow_shard": {
        "page": "reference/fontlab/flNode.html",
        "query": "decode_execution",
        "target": "reference/fontlab_remopy/execution/members-001.html#fontlab_remopy.execution.decode_execution",
        "delay_ms": 2500,
    },
}
VIEW_JS = """fragment => {
  const el = document.getElementById(fragment) || document.getElementsByName(fragment)[0];
  if (!el) return {found: false};
  const r = el.getBoundingClientRect(), header = document.querySelector('.md-header');
  const x = Math.min(Math.max(r.left + 2, 0), innerWidth - 1), y = r.top + Math.min(r.height / 2, 8);
  const hit = y >= 0 && y < innerHeight ? document.elementFromPoint(x, y) : null;
  let covered = null;
  for (let e = hit; e && !covered; e = e.parentElement)
    if (['fixed', 'sticky'].includes(getComputedStyle(e).position))
      covered = e.tagName.toLowerCase() + (e.classList[0] ? '.' + e.classList[0] : '');
  return {found: true, top: r.top, height: r.height, viewport_height: innerHeight,
    header_bottom: header ? header.getBoundingClientRect().bottom : 0, covered_by: covered,
    in_view: !!hit && !covered && r.top >= -1 && r.top < innerHeight};
}"""
SIGNATURE_JS = """member => {
  // separate_signature puts the full signature in the object's own .doc-signature;
  // the inline layout keeps it in the heading code. Nested members' signatures do not count.
  const heading = document.getElementById(member), object = heading?.closest('.doc-object');
  const own = object && [...object.querySelectorAll('.doc-signature')]
    .find(s => s.closest('.doc-object') === object);
  const code = own || heading?.querySelector('code');
  const links = code ? [...code.querySelectorAll('a[href]')] : [];
  links.forEach((a, i) => { a.dataset.r043Link = String(i); });
  return {signature: code ? code.textContent.trim() : null, layout: own ? 'separate' : 'heading',
    links: links.map(a => a.href),
    page_signature_links: document.querySelectorAll('.doc-signature a[href], .doc-heading code a[href]').length};
}"""
TARGETS_JS = """() => {
  const rendered = e => e.getClientRects().length > 0 && getComputedStyle(e).visibility === 'visible' &&
    !e.closest('[hidden],[inert]');
  const focusable = e => rendered(e) && e.tabIndex >= 0 && !e.disabled;
  const mark = (name, e) => { if (e) e.dataset.r043 = name; return !!e; };
  const skip = document.querySelector('.md-skip,a[href^="#"][class*="skip"]');
  const searches = [...document.querySelectorAll('.md-search__input,input[type="search"],label[for="__search"][tabindex]')];
  const navLinks = [...document.querySelectorAll('nav a[href],[role="navigation"] a[href]')];
  let nav = navLinks.find(focusable), panel = null;
  if (!nav) nav = [...document.querySelectorAll('[aria-controls]')].find(e => {
    const p = document.getElementById(e.getAttribute('aria-controls'));
    if (!focusable(e) || !p || !navLinks.some(a => p.contains(a))) return false;
    panel = '#' + CSS.escape(p.id); return true; });
  const root = document.querySelector('.md-content,main,[role="main"]');
  const start = skip && document.getElementById(decodeURIComponent(skip.hash.slice(1)));
  const content = root && [...root.querySelectorAll('a[href]')].find(a => focusable(a) &&
    (!start || start === a || start.compareDocumentPosition(a) & Node.DOCUMENT_POSITION_FOLLOWING));
  return {skip: mark('skip', skip), search: mark('search', searches.find(focusable)),
    nav: mark('nav', nav), nav_panel: panel, content: mark('content', content)};
}"""
ACTIVE_JS = "() => document.activeElement?.dataset?.r043 || null"
SEARCH_ACTIVE_JS = (
    "() => !!document.activeElement?.matches('.md-search__input,input[type=search]')"
)
FIND_RESULT_JS = """expected => [...document.querySelectorAll('.md-search-result__link')]
  .find(a => a.href === expected) || null"""


def no_shot(page: Page) -> dict:
    return {}


def fail(result: dict, reason: str, **details) -> None:
    result["failures"].append({"check": result["case"], "reason": reason, **details})


def finish(result: dict) -> dict:
    result["passed"] = not result["failures"]
    return result


def goto(page: Page, base: str, route: str) -> None:
    response = page.goto(urljoin(base, route), wait_until="networkidle")
    if response is None or response.status != 200:
        raise ValueError(
            f"HTTP status {response.status if response else None} for {route}"
        )
    page.wait_for_timeout(300)


def landed_in_view(page: Page, result: dict, expected: str, key: str) -> None:
    """The browser must sit at the expected URL with its fragment visible."""
    result[key] = page.url
    if page.url != expected:
        fail(result, f"{key}_wrong_url", expected=expected, actual=page.url)
    view = page.evaluate(VIEW_JS, expected.partition("#")[2])
    result[key + "_target"] = view
    if not view["found"]:
        fail(result, "target_missing", fragment=expected.partition("#")[2])
    elif not view["in_view"]:
        fail(result, "target_not_in_view", **view)


def check_deep_link(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """A member fragment must exist and be scrolled clear of sticky chrome."""
    result = {"case": "deep_link", "failures": []}
    route = spec["page"] + "#" + spec["anchor"]
    goto(page, base, route)
    result["target"] = page.evaluate(VIEW_JS, spec["anchor"])
    if not result["target"]["found"]:
        fail(result, "target_missing", fragment=spec["anchor"])
    elif not result["target"]["in_view"]:
        fail(result, "target_not_in_view", **result["target"])
    result["screen"] = shot(page)
    return finish(result)


def check_type_link(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """Click a signature type cross-reference; it must land on the type's anchor."""
    result = {
        "case": spec.get("case", "type_link"),
        "failures": [],
        "member": spec["member"],
    }
    goto(page, base, spec["page"] + "#" + spec["member"])
    found = page.evaluate(SIGNATURE_JS, spec["member"])
    result.update(found)
    expected = urljoin(base, spec["target"])
    if expected not in found["links"]:
        fail(result, "no_type_link", signature=found["signature"], expected=expected)
        result["screen"] = shot(page)
        return finish(result)
    index = found["links"].index(expected)
    page.locator(f'[data-r043-link="{index}"]').click()
    page.wait_for_url(expected, timeout=10000)
    page.wait_for_timeout(300)
    landed_in_view(page, result, expected, "landed")
    result["screen"] = shot(page)
    return finish(result)


def open_search(page: Page) -> None:
    """Reveal the single search field (mobile hides it behind its label)."""
    field = page.locator(".md-search__input")
    if not field.is_visible():
        page.locator('label[for="__search"]:visible').first.click()
    field.click()
    field.fill("")
    ready = '.md-search__output[data-complete-search-state="ready"]'
    page.wait_for_selector(ready, state="attached", timeout=30000)


def find_result(page: Page, expected: str, timeout_ms: int):
    """Return the rendered result link for one exact URL, or None after the deadline."""
    try:
        return page.wait_for_function(
            FIND_RESULT_JS, arg=expected, timeout=timeout_ms
        ).as_element()
    except PlaywrightError:
        return None


def open_result(page: Page, result: dict, expected: str, timeout_ms: int, shot) -> bool:
    """Click the exact rendered result and require same-tab navigation to it."""
    link = find_result(page, expected, timeout_ms)
    if link is None:
        fail(result, "search_result_missing", expected=expected)
        result["screen"] = shot(page)
        return False
    # MaterialX folds extra same-page hits under "N more on this page"; a user opens it.
    summary = link.evaluate_handle(
        "a => a.closest('details:not([open])')?.querySelector('summary') || null"
    )
    result["expanded_more_on_page"] = summary.as_element() is not None
    if result["expanded_more_on_page"]:
        summary.as_element().click()
    result["screen"] = shot(page)
    pages = len(page.context.pages)
    link.click()
    page.wait_for_url(expected, timeout=10000)
    page.wait_for_timeout(300)
    if len(page.context.pages) != pages:
        fail(result, "opened_new_tab", pages=len(page.context.pages))
    return True


def check_alias(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """Inventory, search and legacy routes for an alias must reach their targets."""
    result = {
        "case": "alias",
        "failures": [],
        "name": spec["name"],
        "inventory": spec["inventory"],
    }
    canonical = spec["inventory"].get(spec["canonical"])
    if canonical is None or spec["inventory"].get(spec["name"]) != canonical:
        fail(result, "inventory_mismatch", inventory=spec["inventory"])
    if canonical:
        goto(page, base, spec["search_page"])
        open_search(page)
        expected = urljoin(base, canonical)
        page.locator(".md-search__input").press_sequentially(spec["name"], delay=20)
        if open_result(page, result, expected, spec.get("timeout_ms", 20000), shot):
            landed_in_view(page, result, expected, "search_landed")
    check_legacy(page, base, spec, result)
    return finish(result)


def check_legacy(page: Page, base: str, spec: dict, result: dict) -> None:
    """Old routes must redirect with their fragment to the recorded target."""
    expected = urljoin(base, spec["legacy_target"])
    try:
        page.goto(urljoin(base, spec["legacy"]))
        page.wait_for_url(expected, timeout=5000)
    except PlaywrightError:
        fail(result, "legacy_not_resolved", expected=expected, actual=page.url)
        return
    page.wait_for_timeout(300)
    result["legacy_landed"] = page.url
    result["legacy_current_route"] = spec.get("legacy_current_route")
    view = page.evaluate(VIEW_JS, expected.partition("#")[2])
    result["legacy_target_view"] = view
    if not view["found"]:
        fail(result, "legacy_target_missing", fragment=expected.partition("#")[2])
    elif not view["in_view"]:
        fail(result, "legacy_target_not_in_view", **view)
    current = spec.get("legacy_current_route") or {}
    if current.get("route"):
        # Archive pages with an exact current identity link to it (fragment first).
        wanted = urljoin(base, current["fragment"] or current["route"])
        link = page.locator("a.fl-archive-current")
        found = link.first.evaluate("a => a.href") if link.count() == 1 else None
        result["legacy_current_link"] = found
        if found != wanted:
            fail(result, "legacy_current_link_mismatch", expected=wanted, actual=found)


def delay_shard(page: Page, spec: dict, seen: list) -> None:
    """Delay one shard without blocking other route handlers (time.sleep would)."""

    def slow(route) -> None:
        seen.append(time.monotonic())
        page.wait_for_timeout(spec["delay_ms"])
        route.continue_()

    page.context.route("**/" + spec["shard"], slow)


def wait_until(page: Page, moment: float) -> None:
    while time.monotonic() < moment:
        page.wait_for_timeout(min(50, max(1, int((moment - time.monotonic()) * 1000))))


def check_search(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """A result held back by a slow shard appears only after the delay, opens, and Back returns."""
    result = {
        "case": "search",
        "failures": [],
        "query": spec["query"],
        "shard": spec["shard"],
        "shard_id": spec.get("shard_id"),
        "delay_ms": spec["delay_ms"],
        "worker_shard_deadline_ms": SHARD_DEADLINE_MS,
    }
    seen: list[float] = []
    delay_shard(page, spec, seen)
    goto(page, base, spec["page"])
    start_url = page.url
    open_search(page)
    expected = urljoin(base, spec["target"])
    page.locator(".md-search__input").press_sequentially(spec["query"], delay=20)
    probe_late_result(page, result, seen, expected, spec)
    result["delayed_requests"] = len(seen)
    if result["failures"]:
        result["screen"] = shot(page)
        return finish(result)
    if open_result(page, result, expected, 1000, shot):
        landed_in_view(page, result, expected, "landed")
        page.go_back(wait_until="networkidle")
        result["back_url"] = page.url
        if page.url != start_url:
            fail(result, "back_did_not_return", expected=start_url, actual=page.url)
    return finish(result)


def probe_late_result(
    page: Page, result: dict, seen: list, expected: str, spec: dict
) -> None:
    """Prove lateness: the delayed shard was requested and its result was absent before the delay."""
    deadline = time.monotonic() + spec.get("timeout_ms", 20000) / 1000
    while not seen and time.monotonic() < deadline:
        page.wait_for_timeout(50)
    if not seen:
        fail(result, "delayed_shard_not_requested", shard=spec["shard"])
        return
    wait_until(page, seen[0] + (spec["delay_ms"] - 200) / 1000)
    result["absent_before_delay"] = page.evaluate(FIND_RESULT_JS, expected) is None
    if not result["absent_before_delay"]:
        fail(result, "result_before_delay", delay_ms=spec["delay_ms"])
    if find_result(page, expected, spec.get("timeout_ms", 20000)) is None:
        fail(result, "search_result_missing", query=spec["query"], expected=expected)
        return
    result["result_after_first_delay_ms"] = round((time.monotonic() - seen[0]) * 1000)


RETRY_JS = """() => {
  const output = document.querySelector('.md-search__output');
  const panel = document.querySelector('[data-complete-search-status]');
  return output?.dataset.completeSearchState === 'error' && panel && !panel.hidden
    ? {state: 'error', text: panel.textContent.trim()} : null;
}"""


def check_search_slow_shard(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """A shard slower than the worker deadline must surface Retry, not hang silently."""
    result = {
        "case": "search_slow_shard",
        "failures": [],
        "query": spec["query"],
        "delay_ms": spec["delay_ms"],
        "worker_shard_deadline_ms": SHARD_DEADLINE_MS,
    }
    seen: list[float] = []
    delay_shard(page, spec, seen)
    goto(page, base, spec["page"])
    open_search(page)
    page.locator(".md-search__input").press_sequentially(spec["query"], delay=20)
    timeout = spec.get("timeout_ms", 20000)
    try:
        result["retry"] = page.wait_for_function(RETRY_JS, timeout=timeout).json_value()
    except PlaywrightError:
        result["retry"] = None
        fail(result, "retry_not_shown", delayed_requests=len(seen))
    expected = urljoin(base, spec["target"])
    result["result_shown"] = page.evaluate(FIND_RESULT_JS, expected) is not None
    if result["result_shown"] and result["retry"]:
        fail(result, "partial_result_with_retry")
    if result["retry"]:
        result["screen"] = shot(page)
        page.locator("[data-complete-search-status] button").click()
        result["retry_recovered"] = find_result(page, expected, timeout) is not None
        if not result["retry_recovered"]:
            fail(result, "retry_did_not_recover", delay_ms=spec["delay_ms"])
    result["delayed_requests"] = len(seen)
    result["screen_after"] = shot(page)
    return finish(result)


def tab_walk(page: Page) -> dict:
    """First Tab index at which each marked target receives focus."""
    reached = {}
    for tab in range(1, TAB_BUDGET + 1):
        page.keyboard.press("Tab")
        name = page.evaluate(ACTIVE_JS)
        if name and name not in reached:
            reached[name] = tab
    return reached


def content_via_skip(page: Page, base: str, route: str) -> bool:
    """Skip link + Enter, then one Tab must land on the first content link."""
    goto(page, base, route)
    page.evaluate(TARGETS_JS)
    page.keyboard.press("Tab")
    if page.evaluate(ACTIVE_JS) != "skip":
        return False
    page.keyboard.press("Enter")
    page.keyboard.press("Tab")
    return page.evaluate(ACTIVE_JS) == "content"


def shortcuts(page: Page, base: str, route: str) -> dict:
    """Record (never fail) whether `/` or `s` focus search from the page body."""
    found = {}
    for key in ("/", "s"):
        goto(page, base, route)
        page.keyboard.press(key)
        found[key] = page.evaluate(SEARCH_ACTIVE_JS)
    return found


def check_keyboard(page: Page, base: str, spec: dict, shot=no_shot) -> dict:
    """Tab from page start reaches skip, search, navigation and the first content link."""
    result = {"case": "keyboard", "failures": [], "tab_budget": TAB_BUDGET}
    goto(page, base, spec["page"])
    result["targets"] = page.evaluate(TARGETS_JS)
    result["reached_at_tab"] = tab_walk(page)
    for name in ("skip", "search", "nav"):
        if name not in result["reached_at_tab"]:
            fail(result, f"{name}_unreachable", present=result["targets"][name])
    panel = result["targets"]["nav_panel"]
    if panel and "nav" in result["reached_at_tab"]:
        result["nav_via_opener"] = opened_nav_is_reachable(
            page, '[data-r043="nav"]', panel
        )
        if not result["nav_via_opener"]:
            fail(result, "nav_unreachable_after_opener", panel=panel)
    skip_path = content_via_skip(page, base, spec["page"])
    result["screen"] = shot(page)
    tab_path = "content" in result["reached_at_tab"]
    result["content_path"] = "skip_link" if skip_path else "tab" if tab_path else None
    if result["content_path"] is None:
        fail(result, "content_unreachable", present=result["targets"]["content"])
    result["shortcuts"] = shortcuts(page, base, spec["page"])
    return finish(result)


CHECKS: dict[str, Callable] = {
    "deep_link": check_deep_link,
    "type_link": check_type_link,
    "param_type_link": check_type_link,
    "alias": check_alias,
    "search": check_search,
    "keyboard": check_keyboard,
    "search_slow_shard": check_search_slow_shard,
}


def read_inventory(path: Path, names: set[str]) -> dict[str, str]:
    """Read selected entries of a Sphinx v2 objects.inv, expanding `$` URIs."""
    data = path.read_bytes()
    body = zlib.decompress(data.split(b"\n", 4)[4]).decode()
    found = {}
    for line in body.splitlines():
        match = re.match(r"(.+?)\s+(\S+:\S+)\s+(-?\d+)\s+(\S+)\s", line)
        if match and match[1] in names:
            found[match[1]] = (
                match[4].replace("$", match[1]) if match[4].endswith("$") else match[4]
            )
    return found


def shard_for(site: Path, location: str) -> dict:
    """The one complete-search shard holding a row, as the worker fetches it (.gz)."""
    directory = site / "search/complete"
    manifest = json.loads((directory / "manifest.json").read_text())
    hits = [
        spec
        for spec in manifest["shards"]
        if any(
            row.get("location") == location
            for row in json.loads((directory / spec["file"]).read_text())
        )
    ]
    if len(hits) != 1:
        raise ValueError(f"Expected {location} in exactly one shard, found {len(hits)}")
    return {"id": hits[0]["id"], "file": f"search/complete/{hits[0]['file']}.gz"}


def resolve_plan(site: Path, plan: dict) -> dict:
    """Bind the site's own records (inventory, legacy routes, shard manifest) to the plan."""
    alias, search = dict(plan["alias"]), dict(plan["search"])
    alias["inventory"] = read_inventory(
        site / "objects.inv", {alias["name"], alias["canonical"]}
    )
    routes = json.loads((site / "legacy-routes.json").read_text())["routes"]
    old, _, fragment = alias["legacy"].partition("#")
    alias["legacy_target"] = routes[old]["target"] + "#" + fragment
    # Legacy routes redirect to the archive; its banner must link the exact current page.
    mapped = json.loads((site / "route-map.json").read_text())["routes"]
    entry = next((r for r in mapped if r["old_route"] == old), {})
    alias["legacy_current_route"] = {
        "route": entry.get("current_route"),
        "fragment": entry.get("fragments", {}).get(fragment, {}).get("current"),
    }
    shard = shard_for(site, search["target"])
    search.update(shard=shard["file"], shard_id=shard["id"])
    slow = {
        **plan["search_slow_shard"],
        "shard": shard["file"],
        "shard_id": shard["id"],
    }
    if shard["id"] == 0:
        raise ValueError("Late-search target must live in a non-initial shard")
    return {**plan, "alias": alias, "search": search, "search_slow_shard": slow}


SCHEME_JS = """scheme => {
  const i = document.querySelector(`input[name="__palette"][data-md-color-media="(prefers-color-scheme: ${scheme})"]`);
  return {expected_scheme: i ? i.dataset.mdColorScheme : null,
    actual_scheme: document.body.dataset.mdColorScheme ?? null};
}"""


def make_shot(out_dir: Path, name: str, scheme: str) -> Callable[[Page], dict]:
    """Screenshot the current state and record which palette it actually shows."""

    def shot(page: Page) -> dict:
        page.screenshot(path=str(out_dir / name), animations="disabled")
        return {"screenshot": name, "url": page.url, **page.evaluate(SCHEME_JS, scheme)}

    return shot


def run_entry(
    browser,
    base: str,
    case: str,
    spec: dict,
    viewport: dict,
    scheme: str,
    out_dir: Path,
) -> dict:
    """One case at one viewport/scheme in its own context; errors become failures."""
    name = f"{case}-{viewport['width']}-{scheme}.png"
    context = browser.new_context(viewport=viewport, color_scheme=scheme)
    page = context.new_page()
    shot = make_shot(out_dir, name, scheme)
    entry = {"case": case, "viewport": viewport, "scheme": scheme}
    try:
        entry.update(CHECKS[case](page, base, spec, shot))
    except (PlaywrightError, ValueError) as error:
        entry.update(
            passed=False,
            failures=[{"check": case, "reason": "runtime", "error": str(error)}],
        )
    finally:
        # Delayed route handlers may still be waiting; let them drop quietly.
        context.unroute_all(behavior="ignoreErrors")
        context.close()
    screen = entry.get("screen", {})
    if (
        screen.get("expected_scheme")
        and screen["expected_scheme"] != screen["actual_scheme"]
    ):
        entry["failures"].append(
            {"check": case, "reason": "color_scheme_not_applied", **screen}
        )
        entry["passed"] = False
    return entry


def run(site: Path, out_dir: Path, plan: dict = PLAN, base: str | None = None) -> dict:
    """Every case x viewport x scheme; the receipt keeps measurements and failures.

    With `base` (a deployed URL ending in `/`), pages load from that host; `site`
    must hold the same published bytes, which the plan reads for shard names.
    """
    receipt = {"schema_version": 1, "results": [], "failures": []}
    try:
        if not site.is_dir():
            raise ValueError(f"Built site directory does not exist: {site}")
        resolved = resolve_plan(site, plan)
        receipt["plan"] = resolved
        server = nullcontext(base) if base else serve_site(site)
        with sync_playwright() as playwright, server as base:
            browser = playwright.chromium.launch(headless=True)
            try:
                for case, spec in resolved.items():
                    for viewport in VIEWPORTS:
                        for scheme in SCHEMES:
                            entry = run_entry(
                                browser, base, case, spec, viewport, scheme, out_dir
                            )
                            receipt["results"].append(
                                json.loads(json.dumps(entry).replace(base, "/"))
                            )
            finally:
                browser.close()
    except (PlaywrightError, OSError, ValueError, KeyError) as error:
        receipt["failures"].append(
            {"check": "runtime", "reason": "runtime", "error": str(error)}
        )
    return summarize(receipt)


def summarize(receipt: dict) -> dict:
    summary = {}
    for entry in receipt["results"]:
        passed, total = summary.get(entry["case"], (0, 0))
        summary[entry["case"]] = (passed + entry["passed"], total + 1)
    receipt["summary"] = {case: f"{p}/{t}" for case, (p, t) in summary.items()}
    receipt["passed"] = (
        bool(receipt["results"])
        and not receipt["failures"]
        and all(entry["passed"] for entry in receipt["results"])
    )
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument(
        "--out", type=Path, required=True, help="Receipt JSON; screenshots go beside it"
    )
    parser.add_argument("--base", help="Deployed site URL, e.g. https://host/prefix/")
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    base = args.base.rstrip("/") + "/" if args.base else None
    receipt = run(args.site.resolve(), args.out.parent, base=base)
    receipt["site"] = str(args.site)
    receipt["base"] = base
    args.out.write_text(json.dumps(receipt, indent=2) + "\n")
    print(
        f"Interaction acceptance: {'PASS' if receipt['passed'] else 'FAIL'} {receipt['summary']}; receipt: {args.out}"
    )
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
