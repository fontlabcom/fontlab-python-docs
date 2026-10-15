# this_file: tests/test_deployed_check.py
"""The deployed-host check must see wrong bytes, missing routes and soft 404s."""

import json

from scripts.a11y_check import serve_site
from scripts.deployed_check import check


def _site(root):
    site = root / "fontlab-python-docs"
    (site / "reference").mkdir(parents=True)
    (site / "search").mkdir()
    (site / "index.html").write_text("home")
    (site / "old.html").write_text("redirect")
    (site / "archive.html").write_text("archive")
    (site / "reference" / "a.html").write_text("a")
    (site / "search" / "manifest.json.gz").write_bytes(b"\x1f\x8b")
    routes = [{"old_route": "old.html", "archive_route": "archive.html"}]
    (site / "route-map.json").write_text(json.dumps({"routes": routes}))
    return site


def test_check_when_prefixed_host_serves_same_bytes_then_passes(tmp_path):
    site = _site(tmp_path)
    with serve_site(tmp_path) as url:
        report = check(url + "fontlab-python-docs", site)
    assert report["passed"], report["failures"]
    assert report["headers_by_suffix"][".json.gz"]["content-type"]


def test_check_when_deployed_bytes_or_routes_differ_then_fails(tmp_path):
    deployed = tmp_path / "deployed"
    site = _site(deployed)
    local = _site(tmp_path / "local")
    (local / "index.html").write_text("newer home")
    (site / "old.html").unlink()
    with serve_site(deployed) as url:
        report = check(url + "fontlab-python-docs/", local)
    assert {f["path"] for f in report["failures"]} == {"index.html", "old.html"}
