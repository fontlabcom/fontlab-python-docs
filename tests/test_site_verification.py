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
