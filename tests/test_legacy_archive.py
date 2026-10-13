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
