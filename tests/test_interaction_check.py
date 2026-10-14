# this_file: tests/test_interaction_check.py
"""Tiny local fixture pages prove each R043 interaction check can pass and fail."""

import json
import zlib
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from scripts.a11y_check import serve_site
from scripts.interaction_check import (
    check_alias,
    check_deep_link,
    check_keyboard,
    check_search,
    check_search_slow_shard,
    check_type_link,
    main,
    read_inventory,
    shard_for,
)

FIXTURES = Path(__file__).parent / "fixtures/interactions"
ALIAS = {
    "name": "alias.T",
    "canonical": "m.T",
    "inventory": {"alias.T": "target.html#m.T", "m.T": "target.html#m.T"},
    "legacy": "old.html#legacy.T",
    "legacy_target": "target.html#legacy.T",
}
SEARCH = {
    "page": "search.html",
    "query": "m.T",
    "target": "target.html#m.T",
    "shard": "shard-1.json",
    "delay_ms": 1500,
    "timeout_ms": 5000,
}


@pytest.fixture
def browser():
    with sync_playwright() as playwright:
        if not Path(playwright.chromium.executable_path).exists():
            pytest.skip(
                "Chromium is not installed; run python -m playwright install chromium"
            )
        browser = playwright.chromium.launch(headless=True)
        try:
            yield browser
        finally:
            browser.close()


@pytest.fixture
def site():
    with serve_site(FIXTURES) as url:
        yield url


def new_page(browser, width=1280, height=800):
    return browser.new_context(viewport={"width": width, "height": height}).new_page()


def reasons(result: dict) -> set[str]:
    return {failure["reason"] for failure in result["failures"]}


def test_read_inventory_when_alias_and_dollar_uri_then_expands_to_canonical(tmp_path):
    body = "alias.T py:class 1 target.html#m.T -\nm.T py:class 1 target.html#$ -\n"
    header = b"# Sphinx inventory version 2\n# Project: x\n# Version: 1\n# The remainder of this file is compressed using zlib.\n"
    (tmp_path / "objects.inv").write_bytes(header + zlib.compress(body.encode()))
    found = read_inventory(tmp_path / "objects.inv", {"alias.T", "m.T", "missing"})
    assert found == {"alias.T": "target.html#m.T", "m.T": "target.html#m.T"}, found


def write_shards(directory: Path, shards: list[list[dict]]) -> None:
    (directory / "search/complete").mkdir(parents=True)
    specs = []
    for ordinal, rows in enumerate(shards):
        name = f"rows-{ordinal}.json"
        (directory / "search/complete" / name).write_text(json.dumps(rows))
        specs.append({"id": ordinal, "file": name})
    manifest = {"shards": specs}
    (directory / "search/complete/manifest.json").write_text(json.dumps(manifest))


def test_shard_for_when_row_in_one_later_shard_then_returns_that_gz_file(tmp_path):
    write_shards(tmp_path, [[{"location": "a.html"}], [{"location": "b.html#x"}]])
    shard = shard_for(tmp_path, "b.html#x")
    assert shard == {"id": 1, "file": "search/complete/rows-1.json.gz"}, shard


@pytest.mark.parametrize(
    "shards",
    [[[{"location": "a.html"}]], [[{"location": "b.html"}], [{"location": "b.html"}]]],
)
def test_shard_for_when_row_missing_or_duplicated_then_raises(tmp_path, shards):
    write_shards(tmp_path, shards)
    with pytest.raises(ValueError, match="exactly one shard"):
        shard_for(tmp_path, "b.html")


@pytest.mark.browser
@pytest.mark.parametrize("width,height", [(1280, 800), (375, 812)])
def test_deep_link_when_anchor_clears_sticky_header_then_passes(
    browser, site, width, height
):
    result = check_deep_link(
        new_page(browser, width, height), site, {"page": "deep.html", "anchor": "m.ok"}
    )
    assert result["passed"], result
    assert result["target"]["top"] >= result["target"]["header_bottom"], result


@pytest.mark.browser
@pytest.mark.parametrize(
    "anchor,reason",
    [("m.hidden", "target_not_in_view"), ("m.missing", "target_missing")],
)
def test_deep_link_when_anchor_hidden_or_missing_then_fails(
    browser, site, anchor, reason
):
    result = check_deep_link(
        new_page(browser), site, {"page": "deep.html", "anchor": anchor}
    )
    assert not result["passed"] and reason in reasons(result), result


@pytest.mark.browser
def test_type_link_when_signature_links_type_then_click_lands_on_target(browser, site):
    spec = {"page": "sig.html", "member": "m.f", "target": "target.html#m.T"}
    result = check_type_link(new_page(browser), site, spec)
    assert result["passed"], result
    assert result["landed"] == site + "target.html#m.T", result


@pytest.mark.browser
def test_type_link_when_signature_type_unlinked_then_fails_with_signature(
    browser, site
):
    spec = {"page": "sig.html", "member": "m.g", "target": "target.html#m.T"}
    result = check_type_link(new_page(browser), site, spec)
    assert not result["passed"] and "no_type_link" in reasons(result), result
    assert "g() -> T" in result["signature"], "Receipt must show the unlinked signature"


@pytest.mark.browser
def test_alias_when_inventory_search_and_legacy_resolve_then_passes(browser, site):
    spec = {**ALIAS, "search_page": "search.html", "timeout_ms": 5000}
    result = check_alias(new_page(browser), site, spec)
    assert result["passed"], result
    assert result["search_landed"] == site + "target.html#m.T", result
    assert result["expanded_more_on_page"] is True, (
        "Folded alias hit must be opened like a user"
    )
    assert result["legacy_landed"] == site + "target.html#legacy.T", result


@pytest.mark.browser
@pytest.mark.parametrize(
    "override,reason",
    [
        (
            {"inventory": {"alias.T": "sig.html#m.T", "m.T": "target.html#m.T"}},
            "inventory_mismatch",
        ),
        ({"legacy": "old_broken.html#legacy.T"}, "legacy_not_resolved"),
        ({"name": "nothing.T"}, "search_result_missing"),
    ],
)
def test_alias_when_any_route_misresolves_then_fails(browser, site, override, reason):
    spec = {**ALIAS, "search_page": "search.html", "timeout_ms": 3000, **override}
    result = check_alias(new_page(browser), site, spec)
    assert not result["passed"] and reason in reasons(result), result


@pytest.mark.browser
def test_search_when_shard_is_late_then_result_waits_navigates_and_back_returns(
    browser, site
):
    result = check_search(new_page(browser), site, SEARCH)
    assert result["passed"], result
    assert result["delayed_requests"] >= 1, result
    assert result["result_after_first_delay_ms"] >= 1500 - 50, result
    assert result["absent_before_delay"] is True, result
    assert result["back_url"] == site + "search.html", result


@pytest.mark.browser
@pytest.mark.parametrize(
    "override,reason",
    [
        ({"query": "absent"}, "search_result_missing"),
        ({"shard": "shard-2.json"}, "delayed_shard_not_requested"),
    ],
)
def test_search_when_result_missing_or_not_late_then_fails(
    browser, site, override, reason
):
    result = check_search(
        new_page(browser), site, {**SEARCH, "timeout_ms": 3000, **override}
    )
    assert not result["passed"] and reason in reasons(result), result


@pytest.mark.browser
def test_keyboard_when_skip_search_nav_and_content_reachable_then_passes(browser, site):
    result = check_keyboard(new_page(browser), site, {"page": "keyboard.html"})
    assert result["passed"], result
    assert result["content_path"] == "skip_link", result
    assert result["shortcuts"]["/"] is True and result["shortcuts"]["s"] is False, (
        result
    )


@pytest.mark.browser
def test_keyboard_when_nav_behind_mobile_drawer_then_opener_reaches_nav(browser, site):
    page = new_page(browser, 375, 812)
    result = check_keyboard(page, site, {"page": "keyboard_drawer.html"})
    assert result["passed"], result
    assert result["nav_via_opener"] is True, result


@pytest.mark.browser
def test_keyboard_when_targets_unreachable_then_fails_each_target(browser, site):
    result = check_keyboard(new_page(browser), site, {"page": "keyboard_broken.html"})
    assert not result["passed"], result
    assert {
        "skip_unreachable",
        "search_unreachable",
        "nav_unreachable",
        "content_unreachable",
    } <= reasons(result), result


def test_cli_when_site_missing_then_writes_failed_receipt(tmp_path, monkeypatch):
    receipt = tmp_path / "out/receipt.json"
    argv = [
        "interaction_check",
        "--site",
        str(tmp_path / "missing"),
        "--out",
        str(receipt),
    ]
    monkeypatch.setattr("sys.argv", argv)
    assert main() == 1, "Missing site must fail acceptance"
    data = json.loads(receipt.read_text())
    assert data["schema_version"] == 1 and data["passed"] is False, data
    assert data["failures"][0]["reason"] == "runtime", data


@pytest.mark.browser
@pytest.mark.parametrize(
    "target,kind", [("target.html#m.T", "parameter"), ("target.html#m.U", "return")]
)
def test_type_link_when_separate_signature_links_type_then_lands(
    browser, site, target, kind
):
    spec = {"page": "sig_separate.html", "member": "m.h", "target": target}
    result = check_type_link(new_page(browser), site, spec)
    assert result["passed"], (kind, result)
    assert result["layout"] == "separate" and result["landed"] == site + target, result


@pytest.mark.browser
@pytest.mark.parametrize("member", ["m.k", "m.C"])
def test_type_link_when_separate_signature_unlinked_or_only_nested_then_fails(
    browser, site, member
):
    spec = {"page": "sig_separate.html", "member": member, "target": "target.html#m.T"}
    result = check_type_link(new_page(browser), site, spec)
    assert not result["passed"] and "no_type_link" in reasons(result), result
    assert result["layout"] == "separate", "Must read the object's own signature block"


SLOW = {
    "page": "search_deadline.html",
    "query": "m.T",
    "target": "target.html#m.T",
    "shard": "shard-1.json",
    "timeout_ms": 5000,
}


@pytest.mark.browser
def test_slow_shard_when_beyond_worker_deadline_then_retry_is_recorded(browser, site):
    result = check_search_slow_shard(
        new_page(browser), site, {**SLOW, "delay_ms": 2500}
    )
    assert result["passed"], result
    assert (
        "Retry search" in result["retry"]["text"] and result["result_shown"] is False
    ), result


@pytest.mark.browser
def test_slow_shard_when_shard_arrives_in_time_then_retry_missing_fails(browser, site):
    result = check_search_slow_shard(
        new_page(browser), site, {**SLOW, "delay_ms": 0, "timeout_ms": 3000}
    )
    assert not result["passed"] and "retry_not_shown" in reasons(result), result
    assert result["result_shown"] is True, result
