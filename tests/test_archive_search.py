# this_file: tests/test_archive_search.py
"""Verify the narrow archive installer against the immutable full original inputs."""

import hashlib
import json
import re
import shutil
import tarfile
from pathlib import Path
from urllib.parse import urljoin

import pytest

from scripts.archive_search import ASSETS, CONFIG, OLD, PAGES, UI_ASSETS, UI_OLD, SCRIPT, install_archive_search

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_404_ASSETS = (
    "assets/images/favicon.png",
    "assets/stylesheets/main.5cda52a2.min.css",
    "assets/stylesheets/palette.d7242098.min.css",
    "style/fontlab_pyapi.css",
)


@pytest.fixture
def archive_search(tmp_path):
    root, archive = tmp_path / "root", tmp_path / "archive"
    shutil.copytree(ROOT / "scripts/archive_search/dist", root / "scripts/archive_search/dist")
    shutil.copyfile(ROOT / "scripts/archive_search/sources.json", root / "scripts/archive_search/sources.json")
    for name in ("ui", "ui-dist"):
        shutil.copytree(ROOT / "scripts/archive_search" / name, root / "scripts/archive_search" / name)
    for name in ("ui-sources.json", "compile-ui.cjs", "package.json", "package-lock.json"):
        shutil.copyfile(ROOT / "scripts/archive_search" / name, root / "scripts/archive_search" / name)
    (root / "archive").mkdir()
    shutil.copyfile(ROOT / "archive/fontlab7-manifest.json", root / "archive/fontlab7-manifest.json")
    receipt = json.loads((root / "scripts/archive_search/dist/receipt.json").read_text())
    ui = json.loads((root / "scripts/archive_search/ui-dist/receipt.json").read_text())
    with tarfile.open(ROOT / "archive/fontlab7-site.tar.gz") as stream:
        for name in [*("pythonqt/" + name for name in PAGES),
                     *("pythonqt/" + row["path"] for row in receipt["original"].values()),
                     *("pythonqt/" + row["path"] for row in ui["original"].values()),
                     *("pythonqt/" + name for name in EXPECTED_404_ASSETS)]:
            target = archive / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(stream.extractfile(name).read())
    return root, archive, receipt


def tree(path):
    return {file.relative_to(path).as_posix(): file.read_bytes()
            for file in path.rglob("*") if file.is_file()}


def test_installer_when_verified_then_all_twelve_urls_resolve_and_only_urls_change(archive_search):
    root, archive, receipt = archive_search
    before = tree(archive)
    assert install_archive_search(root, archive) == receipt
    after = tree(archive)
    ui = json.loads((root / "scripts/archive_search/ui-dist/receipt.json").read_text())
    expected_new = {"pythonqt/" + ASSETS + name for name in [*receipt["files"], "receipt.json"]}
    expected_new |= {"pythonqt/" + UI_ASSETS + name for name in [*ui["files"], "receipt.json"]}
    assert set(after) - set(before) == expected_new
    for name, content in before.items():
        if not name.endswith(".html"):
            assert after[name] == content
            continue
        old, new = CONFIG.search(content), CONFIG.search(after[name])
        old_config, new_config = json.loads(old[2]), json.loads(new[2])
        assert old_config.pop("search") in {OLD, "/fontlab-python-docs/pythonqt/" + OLD}
        url = new_config.pop("search")
        if name.endswith("404.html"):
            assert old_config.pop("base") == "/fontlab-python-docs/pythonqt/"
            assert new_config.pop("base") == "."
        assert old_config == new_config
        config_changed = old[2].replace(
            json.dumps(json.loads(old[2])["search"]).encode(), json.dumps(url).encode()
        )
        if name.endswith("404.html"):
            config_changed = config_changed.replace(b'"/fontlab-python-docs/pythonqt/"', b'"."')
        worker_changed = content[:old.start(2)] + config_changed + content[old.end(2):]
        original_ui = ("/fontlab-python-docs/pythonqt/" if name.endswith("404.html") else "") + UI_OLD
        expected_ui = UI_ASSETS + ui["bundle"]
        expected_html = worker_changed.replace(original_ui.encode(), expected_ui.encode())
        if name.endswith("404.html"):
            for asset in EXPECTED_404_ASSETS:
                token = f'href="/fontlab-python-docs/pythonqt/{asset}"'.encode()
                assert expected_html.count(token) == 1
                expected_html = expected_html.replace(token, f'href="{asset}"'.encode())
        assert after[name] == expected_html
        assert sum(script[1] == expected_ui.encode() for script in SCRIPT.finditer(after[name])) == 1
        resolved_ui = urljoin("https://example.test/fontlab-python-docs/archive/fontlab7/" + name, expected_ui)
        assert resolved_ui.endswith("/archive/fontlab7/pythonqt/" + expected_ui)
        resolved = urljoin("https://example.test/fontlab-python-docs/archive/fontlab7/" + name, url)
        assert resolved == "https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/" + ASSETS + receipt["worker"]
    for name in receipt["files"]:
        assert after["pythonqt/" + ASSETS + name] == (root / "scripts/archive_search/dist" / name).read_bytes()


@pytest.mark.parametrize("asset", ["worker", "map", "index"])
def test_installer_when_original_asset_differs_then_no_output_changes(archive_search, asset):
    root, archive, receipt = archive_search
    target = archive / "pythonqt" / receipt["original"][asset]["path"]
    target.write_bytes(target.read_bytes() + b" ")
    before = tree(archive)
    with pytest.raises(ValueError, match="Original archived search asset differs"):
        install_archive_search(root, archive)
    assert tree(archive) == before


@pytest.mark.parametrize("problem", [
    "schema", "compiler", "library", "sources", "artifact", "output-inventory",
    "unsafe-path", "map-reference", "map-content", "map-count", "config", "docs",
    "index-schema", "url", "ambiguous-url", "missing-page", "duplicate-config",
])
def test_installer_when_input_is_unexpected_then_preflight_is_read_only(archive_search, problem):
    root, archive, receipt = archive_search
    dist = root / "scripts/archive_search/dist"
    if problem in {"schema", "compiler", "library"}:
        receipt[{"schema": "schema_version", "compiler": "compiler", "library": "lunr"}[problem]] = "wrong"
    elif problem == "sources":
        (root / "scripts/archive_search/sources.json").write_text("{}")
    elif problem == "artifact":
        (dist / receipt["worker"]).write_bytes(b"wrong")
    elif problem == "output-inventory":
        receipt["files"]["extra.txt"] = {}
    elif problem == "unsafe-path":
        receipt["worker"] = "../wrong"
        receipt["files"]["../wrong"] = receipt["files"].pop(next(name for name in receipt["files"] if name.endswith(".js")))
    elif problem in {"map-reference", "map-content", "map-count"}:
        name = receipt["worker"] if problem == "map-reference" else receipt["map"]
        content = (dist / name).read_bytes()
        if problem == "map-reference":
            content += b"wrong"
        else:
            mapping = json.loads(content)
            mapping["mappings"] = "" if problem == "map-content" else mapping["mappings"]
            if problem == "map-count":
                mapping["sourcesContent"].pop()
            content = json.dumps(mapping).encode()
        (dist / name).write_bytes(content)
        receipt["files"][name] = {"sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}
    elif problem in {"config", "docs", "index-schema"}:
        target = archive / "pythonqt/search/search_index.json"
        data = json.loads(target.read_bytes())
        if problem == "config":
            data["config"]["separator"] = "wrong"
        elif problem == "docs":
            data["docs"].pop()
        else:
            data["extra"] = True
        content = json.dumps(data).encode()
        target.write_bytes(content)
        receipt["original"]["index"]["sha256"] = hashlib.sha256(content).hexdigest()
    else:
        page = archive / "pythonqt/index.html"
        content = page.read_bytes()
        if problem == "missing-page":
            page.unlink()
        elif problem == "duplicate-config":
            page.write_bytes(content + CONFIG.search(content)[0])
        elif problem == "ambiguous-url":
            match = CONFIG.search(content)
            config = json.loads(match[2])
            config["extra"] = config["search"]
            page.write_bytes(content[:match.start(2)] + json.dumps(config).encode() + content[match.end(2):])
        else:
            page.write_bytes(content.replace(OLD.encode(), b"wrong.js"))
    (dist / "receipt.json").write_text(json.dumps(receipt))
    before = tree(archive)
    with pytest.raises(ValueError):
        install_archive_search(root, archive)
    assert tree(archive) == before


def test_installer_when_fixture_has_no_pythonqt_search_then_no_output_is_created(tmp_path):
    assert install_archive_search(tmp_path / "root", tmp_path / "archive") is None
    assert not list(tmp_path.iterdir())


def test_installer_when_real_index_has_no_configs_then_rejects_instead_of_skipping(archive_search):
    root, archive, _ = archive_search
    for name in PAGES:
        (archive / "pythonqt" / name).unlink()
    with pytest.raises(ValueError, match="page inventory"):
        install_archive_search(root, archive)


@pytest.mark.parametrize("problem", ["receipt-schema", "receipt-compiler", "receipt-target", "inventory", "source", "source-path", "original-bundle", "original-map", "inventory-output", "output-path", "asset", "address", "map-reference", "map-content", "map-count", "map-path", "missing-ui", "duplicate-ui", "duplicate-ui-attribute", "wrong-ui", "missing-source", "missing-asset"])
def test_ui_when_any_input_fails_then_both_installations_remain_unwritten(archive_search, problem):
    root, archive, _ = archive_search
    source = root / "scripts/archive_search"
    dist = source / "ui-dist"
    receipt = json.loads((dist / "receipt.json").read_bytes())
    inventory = json.loads((source / "ui-sources.json").read_bytes())
    if problem.startswith("receipt-"):
        receipt[{"receipt-schema": "schema_version", "receipt-compiler": "compiler", "receipt-target": "target"}[problem]] = "wrong"
    elif problem == "inventory":
        (source / "ui-sources.json").write_text("{}")
    elif problem in {"source", "missing-source"}:
        target = source / inventory["files"][0]["path"]
        target.unlink() if problem == "missing-source" else target.write_bytes(b"wrong")
    elif problem == "source-path":
        inventory["files"][0]["path"] = "../outside"
        payload = json.dumps(inventory).encode()
        (source / "ui-sources.json").write_bytes(payload)
        receipt["sources_sha256"] = hashlib.sha256(payload).hexdigest()
    elif problem.startswith("original-"):
        target = archive / "pythonqt" / receipt["original"][problem[9:]]["path"]
        target.write_bytes(b"wrong")
    elif problem == "inventory-output":
        receipt["files"]["extra"] = {}
    elif problem == "output-path":
        receipt["files"]["../outside"] = receipt["files"].pop(receipt["bundle"])
        receipt["bundle"] = "../outside"
    elif problem in {"asset", "missing-asset"}:
        target = dist / receipt["bundle"]
        target.unlink() if problem == "missing-asset" else target.write_bytes(b"wrong")
    elif problem in {"address", "map-reference", "map-content", "map-count", "map-path"}:
        key = "bundle" if problem in {"address", "map-reference"} else "map"
        name = receipt[key]
        content = (dist / name).read_bytes()
        if key == "bundle":
            content += b"wrong"
        else:
            mapping = json.loads(content)
            if problem == "map-content": mapping["mappings"] = ""
            elif problem == "map-count": mapping["sourcesContent"].pop()
            else: mapping["sources"][0] = "/private/source.ts"
            content = json.dumps(mapping).encode()
        if problem != "address":
            new = "bundle." + hashlib.sha256(content).hexdigest() + (".js" if key == "bundle" else ".js.map")
            receipt["files"].pop(name)
            receipt[key] = new
            if key == "map":
                bundle = (dist / receipt["bundle"]).read_bytes().replace(name.encode(), new.encode())
                old_bundle = receipt["bundle"]
                new_bundle = "bundle." + hashlib.sha256(bundle).hexdigest() + ".js"
                (dist / new_bundle).write_bytes(bundle)
                receipt["files"].pop(old_bundle)
                receipt["bundle"] = new_bundle
                receipt["files"][new_bundle] = {"sha256": hashlib.sha256(bundle).hexdigest(), "bytes": len(bundle)}
            name = new
        (dist / name).write_bytes(content)
        receipt["files"][name] = {"sha256": hashlib.sha256(content).hexdigest(), "bytes": len(content)}
    else:
        page = archive / "pythonqt/index.html"
        content = page.read_bytes()
        match = next(script for script in SCRIPT.finditer(content) if script[1] == UI_OLD.encode())
        if problem == "duplicate-ui": content += match[0]
        elif problem == "duplicate-ui-attribute": content = content[:match.start()] + match[0].replace(b"<script ", b'<script src="wrong.js" ') + content[match.end():]
        elif problem == "missing-ui": content = content[:match.start()] + content[match.end():]
        else: content = content.replace(UI_OLD.encode(), b"assets/javascripts/bundle.wrong.js")
        page.write_bytes(content)
    (dist / "receipt.json").write_text(json.dumps(receipt))
    before = tree(archive)
    with pytest.raises((ValueError, FileNotFoundError)):
        install_archive_search(root, archive)
    assert tree(archive) == before


def test_archived_404_when_installed_then_four_actual_link_assets_resolve_with_exact_bytes(archive_search):
    root, archive, _ = archive_search
    before = tree(archive)
    install_archive_search(root, archive)
    content = (archive / "pythonqt/404.html").read_bytes()
    manifest = json.loads((root / "archive/fontlab7-manifest.json").read_bytes())
    for asset in EXPECTED_404_ASSETS:
        assert content.count(f'href="{asset}"'.encode()) == 1
        assert f'href="/fontlab-python-docs/pythonqt/{asset}"'.encode() not in content
        resolved = urljoin("https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/404.html", asset)
        assert resolved == "https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/" + asset
        raw = (archive / "pythonqt" / asset).read_bytes()
        assert raw == before["pythonqt/" + asset]
        identity = next(row for row in manifest["files"] if row["path"] == "pythonqt/" + asset)
        assert len(raw) == identity["bytes"]
        assert hashlib.sha256(raw).hexdigest() == identity["sha256"]


def test_archived_404_when_installed_then_config_resolves_the_exact_existing_index(archive_search):
    root, archive, _ = archive_search
    before = tree(archive)
    install_archive_search(root, archive)
    config = json.loads(CONFIG.search((archive / "pythonqt/404.html").read_bytes())[2])
    base = urljoin("https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/404.html", config["base"])
    assert urljoin(base + "/", "search/search_index.json") == "https://example.test/fontlab-python-docs/archive/fontlab7/pythonqt/search/search_index.json"
    assert (archive / "pythonqt/search/search_index.json").read_bytes() == before["pythonqt/search/search_index.json"]


@pytest.mark.parametrize("base", [
    b'', b'"base":"unexpected",', b'"base":".",',
    b'"base":"/fontlab-python-docs/pythonqt/","base":"/fontlab-python-docs/pythonqt/",',
    b'"base":"unexpected","base":"/fontlab-python-docs/pythonqt/",',
    b'"base":"/fontlab-python-docs/pythonqt/","base":"unexpected",',
    b'"base":"/fontlab-python-docs/pythonqt/","\\u0062ase":"/fontlab-python-docs/pythonqt/",',
    b'"base":"/fontlab-python-docs/pythonqt/","other":"/fontlab-python-docs/pythonqt/",',
])
def test_archived_404_when_base_is_missing_unexpected_or_ambiguous_then_late_preflight_writes_nothing(archive_search, base):
    root, archive, _ = archive_search
    page = archive / "pythonqt/404.html"
    content = page.read_bytes()
    changed, count = re.subn(rb'"base"\s*:\s*"/fontlab-python-docs/pythonqt/"\s*,', lambda _: base, content)
    assert count == 1
    page.write_bytes(changed)
    before = tree(archive)
    with pytest.raises(ValueError, match="archived 404 search base"):
        install_archive_search(root, archive)
    assert tree(archive) == before
    assert not (archive / "pythonqt" / ASSETS).exists()
    assert not (archive / "pythonqt" / UI_ASSETS).exists()


@pytest.mark.parametrize("asset", EXPECTED_404_ASSETS)
@pytest.mark.parametrize("problem", ["missing-link", "duplicate-tag", "duplicate-attribute", "unexpected-href", "already-relative", "outside-tag-duplicate", "missing-asset", "corrupt-asset"])
def test_archived_404_when_any_late_link_or_asset_preflight_fails_then_no_partial_output(archive_search, asset, problem):
    root, archive, _ = archive_search
    page = archive / "pythonqt/404.html"
    content = page.read_bytes()
    token = f'href="/fontlab-python-docs/pythonqt/{asset}"'.encode()
    tag = next(match[0] for match in re.finditer(rb"<link\b[^>]*>", content) if token in match[0])
    if problem == "missing-link": content = content.replace(tag, b"")
    elif problem == "duplicate-tag": content += tag
    elif problem == "duplicate-attribute": content = content.replace(tag, tag.replace(b"<link ", b'<link href="wrong" '))
    elif problem == "unexpected-href": content = content.replace(token, f'href="/unexpected/{asset}"'.encode())
    elif problem == "already-relative": content = content.replace(token, f'href="{asset}"'.encode())
    elif problem == "outside-tag-duplicate": content += b"<!-- " + token + b" -->"
    elif problem == "missing-asset": (archive / "pythonqt" / asset).unlink()
    else:
        target = archive / "pythonqt" / asset
        raw = target.read_bytes()
        target.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])
    page.write_bytes(content)
    before = tree(archive)
    with pytest.raises((ValueError, FileNotFoundError)):
        install_archive_search(root, archive)
    assert tree(archive) == before
    assert not (archive / "pythonqt" / ASSETS).exists()
    assert not (archive / "pythonqt" / UI_ASSETS).exists()
