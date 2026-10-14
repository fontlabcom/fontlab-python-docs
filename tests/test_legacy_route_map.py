# this_file: tests/test_legacy_route_map.py
"""Exact mappings and independently verified preservation of original deep links."""

import hashlib
import io
import json
import tarfile

import pytest

from scripts.legacy_archive import publish_archive
from scripts.legacy_route_map import LegacyHTML, make_route_map, verify_route_map


def archive_fixture(root, site):
    (root / "archive").mkdir(parents=True, exist_ok=True)
    site.mkdir(parents=True, exist_ok=True)
    (site / "index.html").write_text("<html><body>Current</body></html>")
    pages = {
        "pkg.Type.html": b'<body><h1 id="pkg.Type">pkg.Type</h1><h2 id="short">pkg.Type.member</h2><a id="Unknown" href="missing.html#lost">Link</a><a name="named"></a></body>',
        "index.html": b'<body><h1 id="legacy">Old</h1></body>',
        "404.html": b"<body>Missing</body>",
    }
    archive = root / "archive/fontlab7-site.tar.gz"
    with tarfile.open(archive, "w:gz") as stream:
        for name, content in pages.items():
            member = tarfile.TarInfo(name)
            member.size = len(content)
            stream.addfile(member, io.BytesIO(content))
    (root / "archive/fontlab7-manifest.json").write_text(
        json.dumps(
            {
                "archive_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
                "files": [
                    {"path": name, "sha256": hashlib.sha256(content).hexdigest()}
                    for name, content in pages.items()
                ],
            }
        )
    )
    (site / "404.html").write_text("<body>Current error</body>")
    coverage = {
        "symbols": {
            "pkg.Type": {"url": "api/type.html#pkg.Type"},
            "pkg.Type.member": {"url": "api/member.html#pkg.Type.member"},
        },
        "aliases": {},
    }
    publish_archive(root, site, coverage)
    return coverage


def test_exact_identity_fallback_fragments_and_broken_link(tmp_path):
    coverage = archive_fixture(tmp_path / "root", tmp_path / "site")
    report = json.loads((tmp_path / "site/route-map.json").read_text())
    row = next(row for row in report["routes"] if row["old_route"] == "pkg.Type.html")
    assert row["current_route"] == "api/type.html#pkg.Type"
    assert row["fragments"]["short"]["current"] == "api/member.html#pkg.Type.member"
    assert row["fragments"]["Unknown"] == {
        "archive": "archive/fontlab7/pkg.Type.html#Unknown",
        "current": None,
    }
    assert row["fragments"]["named"]["current"] is None
    assert report["routes"][0]["match"] == "archive-only"
    assert (
        report["diagnostics"]["broken_in_original"][0]["status"] == "broken-in-original"
    )
    assert (
        verify_route_map(tmp_path / "root", tmp_path / "site", coverage)["routes"] == 3
    )


def test_determinism_and_no_case_or_short_name_guessing():
    pages = {
        "pkg.Type.html": LegacyHTML(
            '<h2 id="member">Member</h2><h2 id="PKG.Type">Type</h2>'
        ),
        "other.html": LegacyHTML('<a href="pkg.Type.html#missing">x</a>'),
    }
    coverage = {
        "symbols": {"pkg.Type.member": {"url": "api.html#member"}},
        "aliases": {},
    }
    first = make_route_map(pages, coverage)
    assert json.dumps(first, sort_keys=True) == json.dumps(
        make_route_map(dict(reversed(list(pages.items()))), coverage), sort_keys=True
    )
    assert all(row["match"] == "archive-only" for row in first["routes"])
    assert len(first["diagnostics"]["broken_in_original"]) == 1


@pytest.mark.parametrize(
    "damage",
    [
        "route",
        "fragment",
        "target",
        "current",
        "archive",
        "redirect",
        "fallback",
        "root",
        "policy",
        "missing-map",
    ],
)
def test_verification_rejects_incomplete_or_disagreeing_targets(tmp_path, damage):
    root, site = tmp_path / "root", tmp_path / "site"
    coverage = archive_fixture(root, site)
    path = site / "route-map.json"
    report = json.loads(path.read_text())
    if damage == "route":
        report["routes"].pop()
    elif damage == "fragment":
        report["routes"][-1]["fragments"].pop("short")
    elif damage == "target":
        report["routes"][-1]["archive_route"] = "wrong.html"
    elif damage == "current":
        report["routes"][-1]["fragments"]["Unknown"]["current"] = (
            "api/type.html#pkg.Type"
        )
    elif damage == "archive":
        (site / "archive/fontlab7/pkg.Type.html").write_text("<body></body>")
    elif damage in {"redirect", "fallback"}:
        redirect = site / "pkg.Type.html"
        html = redirect.read_text()
        html = (
            html.replace('href="archive/fontlab7/pkg.Type.html"', 'href="wrong.html"')
            if damage == "fallback"
            else html.replace("location.hash", '""')
        )
        redirect.write_text(html)
    elif damage == "root":
        (site / "index.html").write_text("<body>Current</body>")
    elif damage == "policy":
        policy = json.loads((site / "legacy-routes.json").read_text())
        policy["routes"]["pkg.Type.html"]["target"] = "wrong.html"
        (site / "legacy-routes.json").write_text(json.dumps(policy))
    path.write_text(json.dumps(report))
    if damage == "missing-map":
        path.unlink()
    with pytest.raises((ValueError, FileNotFoundError)):
        verify_route_map(root, site, coverage)


def test_link_resolution_handles_encoded_fragments_prefixes_and_external_links():
    pages = {
        "nested/old.html": LegacyHTML(
            '<a href="../target.html?q=1#old%20id">a</a><a href="/fontlab-python-docs/target.html#old%20id">b</a><a href="https://fontlabcom.github.io/fontlab-python-docs/target.html#bad">c</a><a href="https://elsewhere.test/missing.html">d</a><a href="image.png">e</a>'
        ),
        "target.html": LegacyHTML('<h1 id="old id">Original</h1>'),
    }
    broken = make_route_map(pages, {})["diagnostics"]["broken_in_original"]
    assert len(broken) == 1
    assert broken[0]["target_route"] == "target.html"
    assert broken[0]["fragment"] == "bad"


def test_emitted_map_bytes_are_deterministic(tmp_path):
    from scripts.legacy_route_map import write_route_map

    root, site = tmp_path / "root", tmp_path / "site"
    coverage = archive_fixture(root, site)
    first = (site / "route-map.json").read_bytes()
    write_route_map(root, site, coverage)
    assert (site / "route-map.json").read_bytes() == first
