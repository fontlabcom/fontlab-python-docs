# this_file: tests/test_search_shards.py
"""Complete rows are durable; browser bootstrap must never replace coverage."""

import gzip
import json
import subprocess
from collections import Counter
from pathlib import Path

import pytest

from scripts.search_shards import (
    build_shards,
    inspect_shards,
    portable_gzip_sizes,
    read_complete_index,
)


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


def test_manifest_when_producer_gzip_differs_then_records_actual_size(
    tmp_path, corpus, monkeypatch
):
    from scripts import search_shards

    run = search_shards.subprocess.run

    def alternate_gzip(command, **kwargs):
        result = run(command, **kwargs)
        if command[1] == str(search_shards.BACKEND / "build.cjs"):
            compressed = Path(command[3]) / "manifest.json.gz"
            raw = gzip.decompress(compressed.read_bytes())
            alternate = gzip.compress(raw, compresslevel=0, mtime=0)
            assert len(alternate) != len(gzip.compress(raw, mtime=0))
            compressed.write_bytes(alternate)
        return result

    monkeypatch.setattr(search_shards.subprocess, "run", alternate_gzip)
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)
    spec = json.loads(path.read_bytes())["config"]["complete"]["manifest"]
    assert spec["gzip"] == (tmp_path / "complete/manifest.json.gz").stat().st_size
    assert read_complete_index(path) == corpus


@pytest.mark.parametrize("name", ["manifest.json", "manifest.json.gz"])
def test_manifest_when_asset_missing_then_read_fails(tmp_path, corpus, name):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)
    (tmp_path / "complete" / name).unlink()
    with pytest.raises(FileNotFoundError):
        read_complete_index(path)


def test_portable_gzip_sizes_when_asset_is_shipped_then_equals_emitted_gz_size(
    tmp_path, corpus
):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)
    shipped = sorted((tmp_path / "complete").glob("*.json.gz"))
    assert shipped, "Build must emit gzip companions"
    raw = [p.with_suffix("") for p in shipped]
    assert portable_gzip_sizes(raw) == [p.stat().st_size for p in shipped]


def test_portable_gzip_sizes_when_no_paths_then_empty():
    assert portable_gzip_sizes([]) == []


def test_portable_gzip_sizes_when_path_missing_then_raises(tmp_path):
    with pytest.raises(RuntimeError, match="absent.json"):
        portable_gzip_sizes([tmp_path / "absent.json"])


def test_initial_gzip_bytes_when_host_gzip_unavailable_then_uses_portable_codec(
    tmp_path, corpus, monkeypatch
):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)

    def forbidden(*args, **kwargs):
        raise AssertionError("host zlib must not define size budgets")

    monkeypatch.setattr(gzip, "compress", forbidden)
    report = inspect_shards(path)
    from scripts import search_shards

    bootstrap = json.loads(path.read_text())
    spec = bootstrap["config"]["complete"]["manifest"]
    manifest = json.loads((tmp_path / "complete/manifest.json").read_text())
    recorded = spec["gzip"] + manifest["terms"]["gzip"] + manifest["postings"]["gzip"]
    estimated = portable_gzip_sizes([path, search_shards.WORKER, search_shards.UI])
    assert report["initial_gzip_bytes"] == recorded + sum(estimated)


def test_initial_gzip_bytes_when_shipped_gz_differs_then_recorded_manifest_sizes_win(
    tmp_path, corpus
):
    path = tmp_path / "search_index.json"
    path.write_text(json.dumps(corpus))
    build_shards(path)
    before = inspect_shards(path)["initial_gzip_bytes"]
    spec = json.loads(path.read_text())["config"]["complete"]["manifest"]
    spec["gzip"] += 1000
    data = json.loads(path.read_text())
    data["config"]["complete"]["manifest"] = spec
    path.write_text(json.dumps(data))
    # The recorded size feeds the budget; a stale-looking edit must show through.
    try:
        after = inspect_shards(path)["initial_gzip_bytes"]
    except ValueError:
        return  # the recorded size is verified against the asset: tampering is refused
    assert after == before + 1000
