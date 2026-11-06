# this_file: tests/test_pages_inputs.py
"""Private packet failures must precede extraction; audit exceptions stay exact."""

import hashlib
import io
import json
import tarfile
from pathlib import Path

import pytest
import yaml

from scripts import pages_inputs


def test_light_config_keeps_complete_search_and_one_shared_menu():
    root = Path(__file__).resolve().parents[1]
    config = yaml.safe_load((root / "src_docs/mkdocs.yml").read_text())
    assert config["theme"]["palette"] == {"scheme": "default", "primary": "indigo"}
    assert (config["docs_dir"], config["site_dir"]) == ("md", "../docs")
    template = (root / "overrides/main.html").read_text()
    assert template.count("<fontlab-menu ") == template.count("<fontlab-footer ") == 1
    assert 'mobile-search="materialx"' in template
    assert 'mode="light"' in template
    assert "complete-search-ui.js" in template and "workers/complete-search.js" in template


def packet(tmp_path, monkeypatch, *, unsafe=False):
    store = tmp_path / "store"
    store.mkdir()
    archive = store / pages_inputs.ARCHIVE
    with tarfile.open(archive, "w:gz") as tar:
        row = tarfile.TarInfo("../escape" if unsafe else "packages/demo/__init__.py")
        row.size = 8
        tar.addfile(row, io.BytesIO(b"# source"))
    names = {"schema_version": 1, "private_slugs": [f"fontlabcom/private-{i}" for i in range(13)]}
    (store / pages_inputs.NAMES).write_text(json.dumps(names))
    monkeypatch.setattr(pages_inputs, "HASHES", {
        path.name: hashlib.sha256(path.read_bytes()).hexdigest() for path in store.iterdir()
    })
    return store


def test_prepare_when_packet_valid_then_extracts_and_builds_private_audit_workspace(tmp_path, monkeypatch):
    store = packet(tmp_path, monkeypatch)
    target = tmp_path / "private"
    pages_inputs.prepare(store, target)
    assert (target / "inputs/packages/demo/__init__.py").read_bytes() == b"# source"
    configs = list((target / "audit").glob("*/.git/config"))
    assert len(configs) == 14, "Every approved name plus the infrastructure store stays checked"
    assert all("[remote" in path.read_text() for path in configs)


@pytest.mark.parametrize("damage", ["archive", "names", "schema", "slug", "count"])
def test_prepare_when_input_damaged_then_rejects_before_source_extraction(tmp_path, monkeypatch, damage):
    store = packet(tmp_path, monkeypatch)
    if damage in {"archive", "names"}:
        path = store / (pages_inputs.ARCHIVE if damage == "archive" else pages_inputs.NAMES)
        path.write_bytes(path.read_bytes() + b"corrupt")
    else:
        path = store / pages_inputs.NAMES
        data = json.loads(path.read_text())
        if damage == "schema":
            data["schema_version"] = 2
        elif damage == "slug":
            data["private_slugs"][0] = "../../escape"
        else:
            data["private_slugs"].pop()
        path.write_text(json.dumps(data))
        monkeypatch.setitem(pages_inputs.HASHES, pages_inputs.NAMES, hashlib.sha256(path.read_bytes()).hexdigest())
    with pytest.raises(ValueError):
        pages_inputs.prepare(store, tmp_path / "private")
    assert not (tmp_path / "private/inputs").exists()


def test_prepare_when_member_escapes_then_stdlib_data_filter_rejects(tmp_path, monkeypatch):
    store = packet(tmp_path, monkeypatch, unsafe=True)
    with pytest.raises(tarfile.OutsideDestinationError):
        pages_inputs.prepare(store, tmp_path / "private")
    assert not (tmp_path / "private/escape").exists()


def reviewed_report():
    return {"pass": False, "findings": {"private-repository-name": [
        {"file": "packages/plugmix.html", "match": "reviewed-installation"},
        {"file": "search/complete/rows-" + "a" * 64 + ".json", "match": "reviewed-installation"},
        {"file": "search/complete/rows-" + "a" * 64 + ".json.gz", "match": "reviewed-installation"},
    ]}}


def test_disposition_when_exact_three_reviewed_surfaces_then_keeps_raw_exit_one(monkeypatch):
    report = reviewed_report()
    monkeypatch.setattr(pages_inputs, "REVIEWED_NAME_DIGEST", hashlib.sha256(b"reviewed-installation").hexdigest()[:12])
    pages_inputs.disposition(report, 1)
    assert report["pass"] is False


@pytest.mark.parametrize("damage", ["exit", "pass", "extra", "name", "path", "pair", "missing", "category"])
def test_disposition_when_boundary_broadens_then_fails(monkeypatch, damage):
    report = reviewed_report()
    monkeypatch.setattr(pages_inputs, "REVIEWED_NAME_DIGEST", hashlib.sha256(b"reviewed-installation").hexdigest()[:12])
    rows = report["findings"]["private-repository-name"]
    code = 1
    if damage == "exit": code = 2
    elif damage == "pass": report["pass"] = True
    elif damage == "extra": rows.append(dict(rows[0]))
    elif damage == "name": rows[0]["match"] = "new-private-name"
    elif damage == "path": rows[0]["file"] = "other.html"
    elif damage == "pair": rows[2]["file"] = "search/complete/rows-" + "b" * 64 + ".json.gz"
    elif damage == "missing": rows.pop()
    else: report["findings"]["credential"] = [{"file": "x", "match": "secret"}]
    with pytest.raises(ValueError):
        pages_inputs.disposition(report, code)


def test_capture_when_real_audit_fails_then_retains_raw_exit_and_redacted_receipt(tmp_path):
    site, workspace = tmp_path / "site", tmp_path / "audit"
    site.mkdir()
    workspace.mkdir()
    (site / "index.html").write_text("<h1>No licence inventory</h1>")
    output = tmp_path / "raw.json"
    assert pages_inputs.main(["capture", str(site), str(workspace), str(output)]) == 1
    raw = json.loads(output.read_text())
    redacted = json.loads(output.with_suffix(".redacted.json").read_text())
    assert raw["pass"] is False and raw["findings"]["licence"]
    assert redacted["findings"]["licence"][0]["file"].startswith("redacted:")
    with pytest.raises(ValueError):
        pages_inputs.main(["disposition", str(output), "1"])


def test_main_when_valid_prepare_and_disposition_then_runs_real_boundaries(tmp_path, monkeypatch):
    store = packet(tmp_path, monkeypatch)
    assert pages_inputs.main(["prepare", str(store), str(tmp_path / "private")]) == 0
    report = tmp_path / "report.json"
    report.write_text(json.dumps(reviewed_report()))
    monkeypatch.setattr(pages_inputs, "REVIEWED_NAME_DIGEST", hashlib.sha256(b"reviewed-installation").hexdigest()[:12])
    assert pages_inputs.main(["disposition", str(report), "1"]) == 0
    with pytest.raises(ValueError): pages_inputs.main(["unknown"])
