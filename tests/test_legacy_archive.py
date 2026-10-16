# this_file: tests/test_legacy_archive.py
"""Preserve historical bytes and route fragments while marking the archive."""

import hashlib
import io
import json
import tarfile

from scripts.legacy_archive import publish_archive


def test_archive_when_published_then_original_fragment_survives_redirect_and_banner(
    tmp_path,
):
    root, site = tmp_path / "root", tmp_path / "site"
    archive = root / "archive"
    archive.mkdir(parents=True)
    site.mkdir()
    html = b'<html><body><h1 id="old-member">Legacy</h1></body></html>'
    path = archive / "fontlab7-site.tar.gz"
    with tarfile.open(path, "w:gz") as data:
        member = tarfile.TarInfo("pythonqt/old.html")
        member.size = len(html)
        data.addfile(member, io.BytesIO(html))
    metadata = {
        "archive_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "files": [
            {"path": "pythonqt/old.html", "sha256": hashlib.sha256(html).hexdigest()}
        ],
    }
    (archive / "fontlab7-manifest.json").write_text(json.dumps(metadata))
    report = publish_archive(root, site)
    redirect = (site / "pythonqt/old.html").read_text()
    assert "+location.hash" in redirect
    assert "../archive/fontlab7/pythonqt/old.html" in redirect
    saved = (site / "archive/fontlab7/pythonqt/old.html").read_text()
    assert 'id="old-member"' in saved and "FontLab7 archive" in saved
    assert report["routes"]["pythonqt/old.html"]["known_fragments"] == ["old-member"]


def test_legacy_root_migration_preserves_current_root_under_project_prefix(tmp_path):
    from playwright.sync_api import sync_playwright

    root, site = tmp_path / "root", tmp_path / "site"
    (root / "archive").mkdir(parents=True)
    site.mkdir()
    (site / "index.html").write_text(
        "<html><body><h1>Current reference</h1></body></html>"
    )
    pages = {
        "index.html": b'<html><body><h1 id="fl">Old FL</h1><h2 id="pythonqt">Old Qt</h2></body></html>',
        "pythonqt/old.html": b'<html><body><h1 id="old-member">Old member</h1></body></html>',
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
    report = publish_archive(root, site)
    assert report["routes"]["index.html"]["fragment_policy"] == "known-fragments-only"
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()

        def serve(route):
            from urllib.parse import urlparse

            relative = urlparse(route.request.url).path.removeprefix("/project/")
            path = site / (relative or "index.html")
            route.fulfill(
                body=path.read_text(), content_type="text/html"
            ) if path.is_file() else route.fulfill(status=404)

        context.route("http://legacy.test/**", serve)
        page = context.new_page()
        for path in ("", "index.html"):
            page.goto("http://legacy.test/project/" + path)
            assert page.locator("h1").inner_text() == "Current reference"
            for fragment in ("fl", "pythonqt"):
                page.goto("http://legacy.test/project/" + path + "#" + fragment)
                page.wait_for_url("**/archive/fontlab7/index.html#" + fragment)
                assert page.locator("#" + fragment).count() == 1
        page.goto("http://legacy.test/project/pythonqt/old.html#old-member")
        page.wait_for_url("**/archive/fontlab7/pythonqt/old.html#old-member")
        assert page.locator("#old-member").count() == 1
        browser.close()
