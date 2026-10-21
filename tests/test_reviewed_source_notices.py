# this_file: tests/test_reviewed_source_notices.py
"""Actual default audit inputs: exact upstream notices and public/private controls."""
from pathlib import Path
import hashlib
import shutil

import pytest
from scripts import release_audit as audit

SOURCE = Path(__file__).resolve().parents[1] / "src_docs/md/licenses"
REVIEWED = {
    "fontlabapp-notice.txt": "e5c71a4e9132541184840f344da2bd53ab67946dae1e2530cd747a0aaa8f6e89",
    "simon-cozens-mit.txt": "6463ad87fde6016bb3bc48dc58fdf2c8fa82ba33fbefb995038eb90a5b0b93a5",
}


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
