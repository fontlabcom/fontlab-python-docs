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
    from scripts.release_audit import receipt

    written = json.dumps(receipt(audit(site, licences=DIGESTS, workspace=workspace)))
    for secret in ("secret-assets-priv", "fontlab-glyport/src", "fontlabcom/fontlab-glyport"):
        assert secret not in written, f"receipt leaks {secret}"
    assert findings["private-repository-name"][0]["match"] == "secret-assets-priv", "audit() keeps detail"


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


def test_audit_when_escaped_path_survives_json_decoding_then_fails(tmp_path):
    """C3 replay (issue 106): escapes left inside decoded strings, and JSON nested in a string."""
    site = _site(tmp_path)
    (site / "double.json").write_text('{"x": "\\\\/Users\\\\/someone\\\\/x.py"}')
    (site / "nested.json").write_text(
        '{"inner": "{\\"p\\": \\"\\\\/Users\\\\/someone\\\\/nested.py\\"}"}'
    )
    # Only the re-parse finds this: the inner JSON value is itself double-escaped.
    inner = json.dumps({"p": "\\/Users\\/someone\\/deep.py"})
    (site / "deep.json").write_text(json.dumps({"inner": inner}))
    findings = _audit(site, tmp_path)["findings"]
    assert {r["file"] for r in findings["user-path"]} == {
        "double.json",
        "nested.json",
        "deep.json",
    }


def test_receipt_when_findings_name_private_things_then_nothing_private_is_written(tmp_path):
    """RR2-docs: no category may write a private name, path or URL into the receipt."""
    from scripts.release_audit import main

    workspace = tmp_path / "workspace"
    (workspace / "vault" / ".git").mkdir(parents=True)
    (workspace / "vault" / ".git" / "config").write_text(
        '[remote "origin"]\n\turl = https://github.com/fontlabcom/vault-priv.git\n'
    )
    site = _site(tmp_path)
    private = [
        "vault-priv",
        "/Volumes/VaultDisk/",
        "file:///Volumes/VaultDisk/x.py",
        "/Users/vaultowner/",
        "owner@vault.example",
        "github.com/fontlabcom/vault-priv",
        GITHUB_PAT,
    ]
    (site / "vault-priv-notes.html").write_text(" ".join(private))
    (site / "map.js").write_text("//# sourceMappingURL=vault-priv.js.map\n")
    (site / "real.js").write_text("//# sourceMappingURL=real.js.map\n")
    (site / "real.js.map").write_text('{"sources":["/Users/vaultowner/app.ts"]}')
    out = tmp_path / "receipt.json"
    code = main(["--site", str(site), "--out", str(out), "--workspace", str(workspace)])
    receipt = out.read_text()
    assert code == 1 and '"pass": false' in receipt
    for text in private + ["vault-priv.js.map", "vault-priv-notes.html", "/Users/vaultowner/app.ts"]:
        assert text not in receipt, f"receipt leaks {text}"
    findings = json.loads(receipt)["findings"]
    assert {"volume-path", "file-url", "user-path", "email-address", "credential",
            "private-repository-name", "private-repository-url",
            "absolute-source-map-source", "dangling-source-map"} <= set(findings)


def test_reveal_when_requested_then_terminal_shows_detail_and_file_does_not(tmp_path, capsys):
    from scripts.release_audit import main

    site = _site(tmp_path)
    (site / "a.html").write_text("https://github.com/fontlabcom/fontlab-glyport")
    out = tmp_path / "receipt.json"
    main(["--site", str(site), "--out", str(out), "--workspace", str(tmp_path), "--reveal"])
    assert "fontlabcom/fontlab-glyport" in capsys.readouterr().err
    assert "fontlab-glyport" not in out.read_text()


def test_receipt_when_html_links_private_hosts_then_hosts_are_redacted(tmp_path):
    """RR3-docs: external_hosts goes through the same redaction helper."""
    from scripts.release_audit import receipt

    site = _site(tmp_path)
    (site / "x.html").write_text('<a href="https://vault-priv.internal/x">x</a>')
    written = json.dumps(receipt(_audit(site, tmp_path)))
    assert "vault-priv.internal" not in written and "i.fontlab.com" not in written


@pytest.mark.parametrize(
    "text",
    [
        "%2FUsers%2Fsomeone%2Fx.py",
        "%252FUsers%252Fsomeone%252Fx.py",  # percent-encoded twice
        "&#47;Users&#47;someone&#47;x.py",
        "&#x2f;Users&#x2F;someone&#x2f;x.py",
        "&sol;Users&sol;someone&sol;x.py",
        "\\x2fUsers\\x2fsomeone\\x2fx.py",
        "%26%2347%3BUsers%26%2347%3Bsomeone%26%2347%3Bx.py",  # entity inside percent
        "\\\\u0025\\\\u0032\\\\u0046Users%2Fsomeone%2Fx.py",  # escaped percent, mixed
    ],
)
def test_audit_when_path_is_percent_entity_or_hex_encoded_then_fails(tmp_path, text):
    """X4b (issue 106): URL, HTML-entity and \\x escapes, alone and combined."""
    site = _site(tmp_path)
    (site / "page.js").write_text(f'var p = "{text}";')
    findings = _audit(site, tmp_path)["findings"]
    assert [r["file"] for r in findings.get("user-path", [])] == ["page.js"], findings


@pytest.mark.parametrize("times", [2, 3])
def test_audit_when_json_string_scalar_is_serialized_repeatedly_then_fails(tmp_path, times):
    """X4b (issue 106): a path inside a JSON string scalar serialized again and again."""
    value = "\\/Users\\/someone\\/x.py"
    for _ in range(times):
        value = json.dumps(value)
    site = _site(tmp_path)
    (site / "data.json").write_text(json.dumps({"v": value}))
    findings = _audit(site, tmp_path)["findings"]
    assert [r["file"] for r in findings.get("user-path", [])] == ["data.json"], findings


@pytest.mark.parametrize("depth", [1000, 100_000])
def test_audit_when_json_nesting_exceeds_the_bound_then_fails_closed(tmp_path, depth):
    """X4b (issue 106): unbounded nesting must not crash or pass; it is a finding."""
    site = _site(tmp_path)
    (site / "deep.json").write_text("[" * depth + '"x"' + "]" * depth)
    report = _audit(site, tmp_path)
    assert [r["file"] for r in report["findings"]["decode-limit"]] == ["deep.json"]
    assert report["pass"] is False


def test_audit_when_encoding_layers_exceed_the_bound_then_fails_closed(tmp_path):
    """Layers beyond the decode bound are reported, never silently skipped."""
    text = "/Users/someone/x.py"
    for _ in range(12):
        text = text.replace("%", "%25").replace("/", "%2F")
    site = _site(tmp_path)
    (site / "page.js").write_text(f'var p = "{text}";')
    assert [r["file"] for r in _audit(site, tmp_path)["findings"]["decode-limit"]] == ["page.js"]
