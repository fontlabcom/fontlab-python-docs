# this_file: tests/test_release_audit.py
"""The release audit must see private data in every published byte form."""

import gzip
import zlib

from scripts.release_audit import audit

LICENCE_TEXTS = {
    "apache-2.0.txt": "Apache License",
    "gfdl-1.3.txt": "GNU Free Documentation License",
    "lgpl-3.0.txt": "GNU LESSER GENERAL PUBLIC LICENSE",
    "mit.txt": "Permission is hereby granted, free of charge",
}


def _site(tmp_path):
    site = tmp_path / "site"
    (site / "licenses").mkdir(parents=True)
    (site / "licenses.html").write_text("<h1>Licences</h1>")
    for name, text in LICENCE_TEXTS.items():
        (site / "licenses" / name).write_text(text)
    (site / "index.html").write_text('<script src="https://i.fontlab.com/x.js"></script>')
    (site / "objects.inv").write_bytes(b"# Sphinx inventory\nzlib.\n" + zlib.compress(b"fontlab.flNode py:class 1 x.html -\n"))
    return site


def test_audit_when_site_is_clean_then_passes(tmp_path):
    report = audit(_site(tmp_path))
    assert report["pass"], report["findings"]
    assert report["external_hosts"] == ["https://i.fontlab.com"]


def test_audit_when_private_data_hides_in_compressed_files_then_fails(tmp_path):
    site = _site(tmp_path)
    (site / "search").mkdir()
    (site / "search" / "shard.json.gz").write_bytes(gzip.compress(b'{"t":"/Users/someone/x.py"}'))
    (site / "objects.inv").write_bytes(b"# Sphinx inventory\nzlib.\n" + zlib.compress(b"owner@example.com\n"))
    (site / "app.js").write_text("//# sourceMappingURL=app.js.map\n")
    (site / "app.js.map").write_text('{"sources":["/home/dev/src/app.ts"]}')
    findings = audit(site)["findings"]
    assert "search/shard.json.gz" in {row["file"] for row in findings["user-path"]}
    assert findings["email-address"][0]["address"] == "owner@example.com"
    assert findings["absolute-source-map-source"][0]["file"] == "app.js.map"


def test_audit_when_email_is_licence_attribution_then_allowed(tmp_path):
    site = _site(tmp_path)
    (site / "licenses" / "mit.txt").write_text(LICENCE_TEXTS["mit.txt"] + " Jane <jane@example.com>")
    assert audit(site)["pass"]


def test_audit_when_licence_text_missing_then_fails(tmp_path):
    site = _site(tmp_path)
    (site / "licenses" / "gfdl-1.3.txt").unlink()
    findings = audit(site)["findings"]
    assert findings["licence-notice"] == [{"page": True, "missing_texts": ["GFDL-1.3"]}]


def test_audit_when_value_is_reviewed_upstream_example_then_allowed_only_in_scope(tmp_path):
    site = _site(tmp_path)
    (site / "reference" / "PythonQt").mkdir(parents=True)
    (site / "reference" / "PythonQt" / "QDir.html").write_text("cd /home/user/docs")
    (site / "guide.html").write_text("cd /home/user/docs")
    report = audit(site)
    assert [row["file"] for row in report["findings"]["user-path"]] == ["guide.html"]
    assert report["reviewed_public_values"]["/home/user/"]["count"] == 1
