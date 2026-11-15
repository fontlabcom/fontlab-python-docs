# this_file: tests/test_reviewed_source_notices.py
"""Actual default audit inputs: exact upstream notices and public/private controls."""
import hashlib
import json
import re
import shutil
from pathlib import Path

import pytest

from scripts import release_audit as audit

SOURCE = Path(__file__).resolve().parents[1] / "src_docs/md/licenses"
REVIEWED = {
    "echopy-qt-provenance.json": "46a9e88d0432cb647f739a6dd392333ab20a5b2054a454b001c29cd2d65693e3",
    "fontlabapp-notice.txt": "6695d925f4eaa38a2160938dfe5cd3dd70a0133ca625c84de68945e3ad6d2d53",
    "fontlabapp-current-notice.txt": "0acc1a436737b7eec88a61b44f2983d4df6e0a38d52aa018101551d8f2d75362",
    "simon-cozens-mit.txt": "6463ad87fde6016bb3bc48dc58fdf2c8fa82ba33fbefb995038eb90a5b0b93a5",
}


def test_qt_provenance_preserves_reviewed_metadata_without_private_report_context():
    records = json.loads((SOURCE / "echopy-qt-provenance.json").read_text())
    assert set(records) == {"this_file", "source", "documents", "upstream"}
    assert records["this_file"] == "src_docs/md/licenses/echopy-qt-provenance.json"
    assert records["source"] == {
        "project": "FontLab Echopy",
        "commit": "617d077413e2950de6fdb80633ef997d80fe4b99",
        "report": "reports/qt-enrichment.json",
        "sha256": "ce03defef8d33fea2518dbfe4b14dd64621d1c0ba7c62ec4b7e9244b1f5a0d92",
    }
    assert len(records["documents"]) == 576
    for record in records["documents"].values():
        assert set(record) == {"url", "sha256"}
        assert record["url"].startswith("https://doc.qt.io/archives/qt-5.15/")
        assert re.fullmatch(r"[0-9a-f]{64}", record["sha256"])
    assert set(records["upstream"]) == {"metadata_url", "project", "sha256", "url", "version", "wheel"}
    # Canonical digests bind every mapping and upstream field to the reviewed original report.
    assert hashlib.sha256(json.dumps(records["documents"], sort_keys=True).encode()).hexdigest() == (
        "d15ad867e33c4ca8d1cb89580ded30ce39052924fbed55552a169aa5d573b909"
    )
    assert hashlib.sha256(json.dumps(records["upstream"], sort_keys=True).encode()).hexdigest() == (
        "76bbd481a7cd44322cd2eaae6564e1908b6a5f30643d33ef0007845ee643d71e"
    )


def actual_site(tmp_path):
    site = tmp_path / "site"
    (site / "licenses").mkdir(parents=True)
    for name in audit.LICENCES:
        shutil.copyfile(SOURCE / name, site / "licenses" / name)
    (site / "licenses.html").write_text("".join(
        f'<a href="licenses/{name}">{name}</a>' for name in audit.LICENCES
    ))
    (site / "index.html").write_text("Public documentation")
    return site


def test_default_policy_keeps_public_scriptmix_and_rejects_unrelated_private_repository(tmp_path):
    workspace = tmp_path / "workspace"
    for folder, slug in (("public", "fontlab-python-scriptmix"), ("private", "unrelated-fixture-priv")):
        config = workspace / folder / ".git/config"
        config.parent.mkdir(parents=True)
        config.write_text(f'[remote "origin"]\nurl = https://github.com/fontlabcom/{slug}.git\n')
    site = actual_site(tmp_path)
    (site / "index.html").write_text(
        '<a href="https://github.com/fontlabcom/fontlab-python-scriptmix">fontlab-python-scriptmix</a>'
    )
    report = audit.audit(site, workspace=workspace)
    assert report["pass"], report["findings"]
    with (site / "index.html").open("a") as stream:
        stream.write(' unrelated-fixture-priv https://github.com/fontlabcom/unrelated-fixture-priv')
    report = audit.audit(site, workspace=workspace)
    assert not report["pass"]
    assert report["findings"]["private-repository-name"]
    assert report["findings"]["private-repository-url"]
    assert "unrelated-fixture-priv" not in str(audit.receipt(report))


@pytest.mark.parametrize("name", REVIEWED)
@pytest.mark.parametrize("corruption", ["missing", "digest-differs", "not-linked"])
def test_default_policy_rejects_incomplete_or_altered_reviewed_notice(tmp_path, name, corruption):
    assert audit.LICENCES[name] == REVIEWED[name]
    assert hashlib.sha256((SOURCE / name).read_bytes()).hexdigest() == REVIEWED[name]
    site = actual_site(tmp_path)
    assert audit.audit(site, workspace=tmp_path)["pass"]
    if corruption == "missing":
        (site / "licenses" / name).unlink()
    elif corruption == "digest-differs":
        with (site / "licenses" / name).open("a") as stream:
            stream.write(" altered owned control")
    else:
        page = site / "licenses.html"
        page.write_text(page.read_text().replace(f'<a href="licenses/{name}">{name}</a>', ""))
    report = audit.audit(site, workspace=tmp_path)
    assert not report["pass"]
    assert {"file": name, "problem": corruption} in report["findings"]["licence"]


def test_every_licence_linked_from_the_source_page_has_a_reviewed_digest():
    """A notice linked from licenses.md but absent from LICENCES fails the release audit
    as linked-but-unreviewed; the fflate MIT text (Task 414) was missed this way."""
    page = (SOURCE.parent / "licenses.md").read_text()
    linked = set(re.findall(r"\]\((?:\./)?licenses/([^)#?]+)\)", page))
    assert linked, "licenses.md links no notices"
    assert linked - set(audit.LICENCES) == set(), "linked notices lack a reviewed digest"
    for name in linked:
        digest = hashlib.sha256((SOURCE / name).read_bytes()).hexdigest()
        assert audit.LICENCES[name] == digest, f"{name} differs from its reviewed digest"
