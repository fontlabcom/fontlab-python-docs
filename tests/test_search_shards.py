# this_file: tests/test_search_shards.py
"""Complete rows are durable; browser bootstrap must never replace coverage."""

import json
from collections import Counter

import pytest

from scripts.search_shards import build_shards, read_complete_index


@pytest.fixture
def corpus():
    return {
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
                "location": "a.html",
                "title": "Alpha",
                "text": "Signal resize",
                "boost": 100,
            },
            {
                "location": "a.html#close",
                "title": "Alpha.close",
                "text": "Close Signal",
                "tags": ["fly.Alpha.close"],
            },
            {"location": "b.html", "title": "Beta", "text": "Signal other"},
            {
                "location": "b.html#resize",
                "title": "Beta.resize",
                "text": "Resize widget",
                "tags": ["fly.Beta.resize"],
            },
        ],
    }


def test_complete_rows_reconstruct_exactly_and_build_is_deterministic(tmp_path, corpus):
    search = tmp_path / "search"
    search.mkdir()
    path = search / "search_index.json"
    path.write_text(json.dumps(corpus))
    report = build_shards(path, shard_bytes=150)
    restored = read_complete_index(path)
    assert restored["config"] == corpus["config"], "Do not normalize language/config"
    canonical = lambda rows: Counter(json.dumps(row, sort_keys=True) for row in rows)
    assert canonical(restored["docs"]) == canonical(corpus["docs"]), (
        "Keep every original field"
    )
    from scripts.search_identities import verify_search_coverage

    symbols = {
        "Alpha.close": {
            "kind": "function",
            "url": "a.html#close",
            "body_url": "a.html#close",
        },
        "Beta.resize": {
            "kind": "function",
            "url": "b.html#resize",
            "body_url": "b.html#resize",
        },
    }
    verify_search_coverage(
        restored,
        symbols,
        {"fly.Alpha.close": "Alpha.close", "fly.Beta.resize": "Beta.resize"},
    )
    assert report["rows"] == 4 and report["initial_gzip_bytes"] > 0
    assert json.loads(path.read_text())["docs"] == [], "Page bootstrap must stay tiny"
    before = {p.name: p.read_bytes() for p in (search / "complete").iterdir()}
    path.write_text(json.dumps(corpus))
    build_shards(path, shard_bytes=150)
    assert before == {
        p.name: p.read_bytes() for p in (search / "complete").iterdir()
    }, "Rebuild reproducibly"
    manifest = json.loads((search / "complete/manifest.json").read_text())
    assert all(
        len(shard["file"].split("-")[1].split(".")[0]) == 64
        for shard in manifest["shards"]
    )
    assert len(manifest["shards"]) == 2, "Keep parent pages and sections together"


def test_corrupt_complete_rows_fail_instead_of_reporting_zero_coverage(
    tmp_path, corpus
):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path, shard_bytes=150)
    shard = next((tmp_path / "complete").glob("rows-*.json"))
    shard.write_text("[]")
    with pytest.raises(ValueError, match="hash|size"):
        read_complete_index(path)


def test_budget_failure_preserves_original_bootstrap_input(
    tmp_path, corpus, monkeypatch
):
    from scripts import search_shards

    path = tmp_path / "search_index.json"
    original = json.dumps(corpus).encode()
    path.write_bytes(original)
    monkeypatch.setattr(search_shards, "INITIAL_BUDGET", 1)
    with pytest.raises(ValueError, match="exceeds"):
        build_shards(path)
    assert path.read_bytes() == original, "Do not publish a failed tiny-bootstrap build"


def test_corrupt_gzip_companion_fails_even_when_raw_rows_are_intact(tmp_path, corpus):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)
    compressed = next((tmp_path / "complete").glob("rows-*.json.gz"))
    compressed.write_bytes(b"broken gzip")
    with pytest.raises(ValueError, match="compressed"):
        read_complete_index(path)
