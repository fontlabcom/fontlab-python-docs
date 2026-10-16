# this_file: tests/test_promote_site.py
"""docs/ (the Pages source) must be exactly the accepted build, never stale or partial."""

import json

import pytest

from scripts.build_provenance import file_manifest
from scripts.promote_site import promote


def _accepted(root, files):
    site = root / ".build/site"
    for name, text in files.items():
        (site / name).parent.mkdir(parents=True, exist_ok=True)
        (site / name).write_text(text)
    rendered = file_manifest(site, exclude=("build-provenance.json",))
    payload = json.dumps({"schema_version": 1, "generation": {}, "rendered": rendered},
                         sort_keys=True, separators=(",", ":")) + "\n"
    (site / "build-provenance.json").write_text(payload)
    (root / ".build/accepted-build.json").write_text(payload)
    return site


def test_promote_when_build_is_accepted_then_docs_is_an_exact_copy_without_finder_metadata(tmp_path):
    site = _accepted(tmp_path, {"index.html": "new", "reference/a.html": "a", ".nojekyll": ""})
    (site / ".DS_Store").write_bytes(b"\0")
    (tmp_path / "docs/old").mkdir(parents=True)
    (tmp_path / "docs/old/stale.html").write_text("historical")
    (tmp_path / "docs/.DS_Store").write_bytes(b"\0")
    report = promote(tmp_path)
    docs = tmp_path / "docs"
    assert sorted(p.relative_to(docs).as_posix() for p in docs.rglob("*") if p.is_file()) == [
        ".nojekyll", "build-provenance.json", "index.html", "reference/a.html"]
    assert report["files"] == 4


def test_promote_when_site_differs_from_accepted_build_then_docs_is_untouched(tmp_path):
    site = _accepted(tmp_path, {"index.html": "new", ".nojekyll": ""})
    (site / "index.html").write_text("tampered")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs/index.html").write_text("historical")
    with pytest.raises(ValueError, match="differs from accepted"):
        promote(tmp_path)
    assert (tmp_path / "docs/index.html").read_text() == "historical"
