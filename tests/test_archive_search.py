# this_file: tests/test_archive_search.py
"""Verify the narrow archive installer against the immutable full original inputs."""

import hashlib
import json
import shutil
import tarfile
from pathlib import Path
from urllib.parse import urljoin

import pytest

from scripts.archive_search import ASSETS, CONFIG, OLD, PAGES, install_archive_search

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def archive_search(tmp_path):
    root, archive = tmp_path / "root", tmp_path / "archive"
    shutil.copytree(ROOT / "scripts/archive_search/dist", root / "scripts/archive_search/dist")
    shutil.copyfile(ROOT / "scripts/archive_search/sources.json", root / "scripts/archive_search/sources.json")
    receipt = json.loads((root / "scripts/archive_search/dist/receipt.json").read_text())
    with tarfile.open(ROOT / "archive/fontlab7-site.tar.gz") as stream:
        for name in [*("pythonqt/" + name for name in PAGES),
                     *("pythonqt/" + row["path"] for row in receipt["original"].values())]:
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
    expected_new = {"pythonqt/" + ASSETS + name for name in [*receipt["files"], "receipt.json"]}
    assert set(after) - set(before) == expected_new
    for name, content in before.items():
        if not name.endswith(".html"):
            assert after[name] == content
            continue
        old, new = CONFIG.search(content), CONFIG.search(after[name])
        old_config, new_config = json.loads(old[2]), json.loads(new[2])
        assert old_config.pop("search") in {OLD, "/fontlab-python-docs/pythonqt/" + OLD}
        url = new_config.pop("search")
        assert old_config == new_config
        assert after[name] == content[:old.start(2)] + old[2].replace(
            json.dumps(json.loads(old[2])["search"]).encode(), json.dumps(url).encode()
        ) + content[old.end(2):]
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
