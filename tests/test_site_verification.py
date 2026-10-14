# this_file: tests/test_site_verification.py
"""A green generation count cannot replace actual anchor/inventory evidence."""

import json

import pytest
from mkdocstrings import Inventory

from scripts.verify_site import verify_site


def fixture_site(tmp_path, *, anchor=True):
    site = tmp_path / "site"
    (site / "search").mkdir(parents=True)
    (site / "search/search_index.json").write_text('{"docs":[]}')
    (site / "page.html").write_text(
        '<h1 id="pkg.value">value</h1>' if anchor else "<h1>value</h1>"
    )
    coverage = {
        "symbols": {
            "pkg.value": {
                "kind": "function",
                "body_target": "pkg.value",
                "url": "page.html#pkg.value",
                "body_url": "page.html#pkg.value",
            }
        },
        "aliases": {"pkg.alias": "pkg.value"},
    }
    path = tmp_path / "coverage.json"
    path.write_text(json.dumps(coverage))
    inventory = Inventory(project="fixture", version="1")
    inventory.register("pkg.value", "py", "function", "page.html#pkg.value")
    inventory.register("pkg.alias", "py", "function", "page.html#pkg.value")
    (site / "objects.inv").write_bytes(inventory.format_sphinx())
    return site, path


def test_site_when_anchors_and_alias_inventory_exist_then_passes(tmp_path):
    site, coverage = fixture_site(tmp_path)
    assert verify_site(site, coverage)["passed"]


def test_site_when_generated_member_anchor_missing_then_fails(tmp_path):
    site, coverage = fixture_site(tmp_path, anchor=False)
    with pytest.raises(ValueError, match="acceptance failed"):
        verify_site(site, coverage)


def test_site_when_alias_inventory_points_to_missing_anchor_then_fails(tmp_path):
    site, coverage = fixture_site(tmp_path)
    inventory = Inventory(project="fixture", version="1")
    inventory.register("pkg.value", "py", "function", "page.html#pkg.value")
    inventory.register("pkg.alias", "py", "function", "page.html#wrong")
    (site / "objects.inv").write_bytes(inventory.format_sphinx())
    with pytest.raises(ValueError, match="acceptance failed"):
        verify_site(site, coverage)


def test_sharded_site_verifies_complete_coverage_and_requires_deployed_worker(tmp_path):
    import shutil

    from scripts.search_shards import ROOT, build_shards

    site, coverage = fixture_site(tmp_path)
    index = site / "search/search_index.json"
    index.write_text(
        json.dumps(
            {
                "config": {
                    "lang": ["en"],
                    "separator": r"[\s\-]+",
                    "pipeline": ["trimmer"],
                    "fields": {
                        "title": {"boost": 1000},
                        "text": {"boost": 1},
                        "tags": {"boost": 1000000},
                    },
                },
                "docs": [
                    {
                        "location": "page.html#pkg.value",
                        "title": "pkg.value",
                        "text": "Complete body.",
                        "tags": ["pkg.alias"],
                    }
                ],
            }
        )
    )
    build_shards(index)
    for relative in (
        "assets/javascripts/workers/complete-search.js",
        "assets/javascripts/complete-search-ui.js",
    ):
        (site / relative).parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / "overrides" / relative, site / relative)
    report = verify_site(site, coverage)
    assert report["search_rows"] == 1, (
        "An empty page bootstrap cannot replace complete coverage"
    )
    assert report["search_gzip_budget_bytes"] == 5 * 1024 * 1024
    assert report["search_sharding"]["aggregate_bytes"] > 0
    assert (
        report["search_gzip_bytes"] == report["search_sharding"]["initial_gzip_bytes"]
    )
    (site / "assets/javascripts/workers/complete-search.js").write_bytes(
        b"a" * (5 * 1024 * 1024)
    )
    with pytest.raises(ValueError, match="acceptance failed"):
        verify_site(site, coverage)
    (site / "assets/javascripts/workers/complete-search.js").unlink()
    with pytest.raises(FileNotFoundError, match="complete-search"):
        verify_site(site, coverage)
