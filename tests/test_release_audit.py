# this_file: tests/test_release_audit.py
"""The release audit must see private data in every published byte form."""

import base64
import gzip
import hashlib
import json
import zlib

import pytest

from scripts.release_audit import audit

TEXTS = {
    "apache-2.0.txt": "Apache License, full text",
    "gfdl-1.3.txt": "GNU Free Documentation License, full text",
    "mit-lunr.txt": "Permission is hereby granted, free of charge, full text",
}
DIGESTS = {name: hashlib.sha256(text.encode()).hexdigest() for name, text in TEXTS.items()}
# Synthetic credentials assembled at run time so this file holds no token literal.
GITHUB_PAT = "github_pat_" + "A1b2C3d4E5" * 3 + "_" + "Z9y8X7w6V5" * 6
TOKENS = [
    GITHUB_PAT,
    "ghp_" + "a1B2" * 9,
    "glpat-" + "x1Y2z3" * 4,
    "xoxb-" + "123456789012-abcdefABCDEF",
    "AIza" + "S" * 35,
    "sk-ant-" + "api03" * 6,
    "AKIA" + "ABCDEFGHIJKLMNOP",
    "npm_" + "a" * 36,
]


def _site(tmp_path, links=None):
    site = tmp_path / "site"
    (site / "licenses").mkdir(parents=True)
    links = TEXTS if links is None else links
    (site / "licenses.html").write_text(
        "".join(f'<a href="licenses/{name}">{name}</a>' for name in links)
    )
    for name, text in TEXTS.items():
        (site / "licenses" / name).write_text(text)
    (site / "index.html").write_text('<script src="https://i.fontlab.com/x.js"></script>')
    (site / "objects.inv").write_bytes(
        b"# Sphinx inventory\nzlib.\n" + zlib.compress(b"fontlab.flNode py:class 1 x.html -\n")
    )
    return site


def _audit(site, tmp_path, **kwargs):
    workspace = tmp_path / "workspace"
    workspace.mkdir(exist_ok=True)
    return audit(site, licences=DIGESTS, workspace=workspace, **kwargs)


def test_audit_when_site_is_clean_then_passes(tmp_path):
    report = _audit(_site(tmp_path), tmp_path)
    assert report["pass"], report["findings"]
    assert report["external_hosts"] == ["https://i.fontlab.com"]


def test_audit_when_private_data_hides_in_compressed_files_then_fails(tmp_path):
    site = _site(tmp_path)
    (site / "search").mkdir()
    (site / "search" / "shard.json.gz").write_bytes(gzip.compress(b'{"t":"/Users/someone/x.py"}'))
    (site / "objects.inv").write_bytes(b"# Sphinx inventory\nzlib.\n" + zlib.compress(b"owner@example.com\n"))
    (site / "app.js").write_text("//# sourceMappingURL=app.js.map\n")
    (site / "app.js.map").write_text('{"sources":["/home/dev/src/app.ts"]}')
    findings = _audit(site, tmp_path)["findings"]
    assert "search/shard.json.gz" in {row["file"] for row in findings["user-path"]}
    assert findings["email-address"][0]["address"] == "owner@example.com"
    assert findings["absolute-source-map-source"][0]["file"] == "app.js.map"


@pytest.mark.parametrize("token", TOKENS, ids=lambda t: t.split("_")[0][:6])
def test_audit_when_credential_published_then_fails(tmp_path, token):
    """R-L5-docs P1: fine-grained github_pat_ and other current formats."""
    site = _site(tmp_path)
    (site / "page.html").write_text(f"<p>token {token} here</p>")
    assert "credential" in _audit(site, tmp_path)["findings"], token


def test_audit_when_inline_source_map_or_escaped_json_hides_paths_then_fails(tmp_path):
    """R-L5-docs P2: decode inline data: maps and JSON-escaped strings."""
    site = _site(tmp_path)
    source_map = {"sources": ["/Users/someone/private/app.ts"], "sourcesContent": ["x"]}
    encoded = base64.b64encode(json.dumps(source_map).encode()).decode()
    (site / "inline.js").write_text(
        f"x()\n//# sourceMappingURL=data:application/json;base64,{encoded}\n"
    )
    (site / "rows.json.gz").write_bytes(gzip.compress(b'{"t":"\\/home\\/someone\\/secret.py"}'))
    findings = _audit(site, tmp_path)["findings"]
    assert findings["absolute-source-map-source"][0]["file"] == "inline.js"
    assert {"inline.js", "rows.json.gz"} <= {row["file"] for row in findings["user-path"]}


def test_audit_when_private_repository_or_volume_path_published_then_fails(tmp_path):
    """R-L5-docs P2: private repo URLs, checkout paths, mounted volumes."""
    workspace = tmp_path / "workspace"
    (workspace / "secret-assets" / ".git").mkdir(parents=True)
    (workspace / "secret-assets" / ".git" / "config").write_text(
        '[remote "origin"]\n\turl = https://github.com/fontlabcom/secret-assets-priv.git\n'
    )
    site = _site(tmp_path)
    (site / "a.html").write_text(
        "see https://github.com/fontlabcom/fontlab-glyport/blob/main/x.py and"
        " git@github.com:fontlabcom/secret-assets-priv.git and"
        " /Volumes/PrivateDisk/private-repository/app.py and"
        " fontlab-glyport/src/fontlab_glyport/model.py and secret-assets-priv"
    )
    (site / "b.html").write_text("public https://github.com/fontlabcom/fontlab-python-docs")
    findings = audit(site, licences=DIGESTS, workspace=workspace)["findings"]
    assert len(findings["private-repository-url"]) == 2
    assert findings["volume-path"][0]["file"] == "a.html"
    assert len(findings["checkout-path"]) == 1 and len(findings["private-repository-name"]) == 1
    report = json.dumps(audit(site, licences=DIGESTS, workspace=workspace))
    for secret in ("secret-assets-priv", "fontlab-glyport/src", "fontlabcom/fontlab-glyport"):
        assert secret not in report, f"receipt leaks {secret}"
    assert findings["private-repository-name"][0]["match"].startswith("redacted:")


def test_audit_when_file_url_is_not_a_reviewed_example_then_fails(tmp_path):
    """R-L5-docs P2: exceptions are exact values in scope, not a prefix."""
    site = _site(tmp_path)
    (site / "search" / "complete").mkdir(parents=True)
    (site / "search" / "complete" / "rows.json").write_text(
        '{"a":"file:///home/user/test.html","b":"file:///Volumes/Disk/repo/app.py"}'
    )
    report = _audit(site, tmp_path)
    assert [r["match"] for r in report["findings"]["file-url"]] == ["file:///Volumes/Disk/repo/app.py"]
    assert report["reviewed_public_values"]["file:///home/user/test.html"]["count"] == 1


def test_audit_when_licence_text_differs_or_page_link_missing_then_fails(tmp_path):
    """R-L5-docs P2: full texts by digest and every licence linked from the page."""
    site = _site(tmp_path, links=["apache-2.0.txt", "gfdl-1.3.txt"])
    (site / "licenses" / "gfdl-1.3.txt").write_text("GNU Free Documentation License")
    findings = _audit(site, tmp_path)["findings"]["licence"]
    assert {(r["file"], r["problem"]) for r in findings} == {
        ("gfdl-1.3.txt", "digest-differs"),
        ("mit-lunr.txt", "not-linked"),
    }


def test_audit_when_email_is_licence_attribution_then_allowed(tmp_path):
    site = _site(tmp_path)
    with (site / "licenses" / "mit-lunr.txt").open("a") as stream:
        stream.write(" Jane <jane@example.com>")
    report = audit(site, licences={**DIGESTS, "mit-lunr.txt": hashlib.sha256(
        (site / "licenses" / "mit-lunr.txt").read_bytes()).hexdigest()}, workspace=tmp_path)
    assert report["pass"], report["findings"]


def test_audit_when_value_is_reviewed_upstream_example_then_allowed_only_in_scope(tmp_path):
    site = _site(tmp_path)
    (site / "reference" / "PythonQt").mkdir(parents=True)
    (site / "reference" / "PythonQt" / "QDir.html").write_text("cd /home/user/docs")
    (site / "guide.html").write_text("cd /home/user/docs")
    report = _audit(site, tmp_path)
    assert [row["file"] for row in report["findings"]["user-path"]] == ["guide.html"]
    assert report["reviewed_public_values"]["/home/user/"]["count"] == 1


def test_audit_when_paths_hide_behind_json_or_js_escapes_then_fails(tmp_path):
    """RR-docs P2: \\u002f and \\/ escapes in gzip JSON, inline maps and scripts."""
    site = _site(tmp_path)
    (site / "rows.json.gz").write_bytes(
        gzip.compress(b'{"t":"\\u002fUsers\\u002fsomeone\\u002fsecret.py"}')
    )
    source_map = '{"sources":["app.ts"],"sourcesContent":["// \\/home\\/dev\\/x \\u002fVolumes\\u002fDisk\\u002fa"]}'
    encoded = base64.b64encode(source_map.encode()).decode()
    (site / "inline.js").write_text(
        f"x()\n//# sourceMappingURL=data:application/json;base64,{encoded}\n"
    )
    (site / "app.js").write_text('const p = "\\u002fUsers\\u002fother\\u002fx";')
    findings = _audit(site, tmp_path)["findings"]
    assert {r["file"] for r in findings["user-path"]} >= {"rows.json.gz", "inline.js", "app.js"}
    assert findings["volume-path"][0]["file"] == "inline.js"
