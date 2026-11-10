# this_file: tests/test_pages_publish.py
"""Exercise publication against real disposable Git histories, never shared refs."""

import io
import json
import os
import subprocess

import pytest

from scripts import pages_publish as publisher


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


@pytest.fixture
def repository(tmp_path):
    remote, root = tmp_path / "remote.git", tmp_path / "source"
    subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
    subprocess.run(["git", "clone", str(remote), str(root)], check=True, capture_output=True)
    git(root, "config", "user.name", "Test")
    git(root, "config", "user.email", "test@example.invalid")
    git(root, "switch", "-c", "main")
    (root / "docs").mkdir()
    (root / "docs/index.html").write_text("old\n")
    (root / "source.py").write_text("original\n")
    git(root, "add", ".")
    git(root, "commit", "-m", "source")
    git(root, "push", "origin", "HEAD:refs/heads/main")
    return root, git(root, "rev-parse", "HEAD")


def test_publish_when_changed_then_only_docs_normal_push_and_direct_lineage(repository):
    root, source = repository
    (root / "docs/index.html").write_bytes(b"new\r\nbytes\n")
    (root / "docs/new.html").write_text("new page\n")
    generated = publisher.publish(root, source)
    assert generated != source and publisher.remote_main(root) == generated
    publisher.lineage(root, source, generated)
    publisher.parity(root)
    assert git(root, "diff", "--name-only", source, generated).splitlines() == ["docs/index.html", "docs/new.html"]


def test_publish_when_code_only_and_output_unchanged_then_y_equals_x(repository):
    root, _ = repository
    (root / "source.py").write_text("code only change\n")
    git(root, "commit", "-am", "code-only")
    git(root, "push", "origin", "HEAD:refs/heads/main")
    source = git(root, "rev-parse", "HEAD")
    assert publisher.publish(root, source) == source
    publisher.lineage(root, source, source)
    publisher.parity(root)


def test_publish_when_main_stale_then_no_commit_or_push(repository):
    root, source = repository
    git(root, "commit", "--allow-empty", "-m", "newer main")
    git(root, "push", "origin", "HEAD:refs/heads/main")
    git(root, "checkout", "--detach", source)
    (root / "docs/index.html").write_text("stale output\n")
    assert publisher.publish(root, source) == ""
    assert git(root, "rev-parse", "HEAD") == source


@pytest.mark.parametrize("damage", ["head", "index", "source"])
def test_publish_when_source_or_index_unexpected_then_fails(repository, damage):
    root, source = repository
    if damage == "head": source = "a" * 40
    elif damage == "index":
        (root / "source.py").write_text("staged private source\n")
        git(root, "add", "source.py")
    else: (root / "source.py").write_text("unexpected source change\n")
    with pytest.raises(ValueError): publisher.publish(root, source)


@pytest.mark.parametrize("operation", ["remote", "push"])
def test_publish_when_git_fails_then_error_propagates(repository, operation):
    root, source = repository
    if operation == "remote":
        git(root, "remote", "set-url", "origin", str(root / "missing"))
    else:
        git(root, "config", "remote.origin.pushurl", str(root / "missing"))
        (root / "docs/index.html").write_text("changed\n")
    with pytest.raises(subprocess.CalledProcessError): publisher.publish(root, source)


@pytest.mark.parametrize("damage", ["tracked", "untracked"])
def test_parity_when_any_docs_bytes_differ_then_fails(repository, damage):
    root, _ = repository
    path = root / "docs" / ("index.html" if damage == "tracked" else "extra.bin")
    path.write_bytes(b"unexpected\x00bytes")
    with pytest.raises((ValueError, subprocess.CalledProcessError)): publisher.parity(root)


def test_lineage_when_generated_commit_changes_source_then_rejects(repository):
    root, source = repository
    (root / "source.py").write_text("untrusted\n")
    git(root, "commit", "-am", "not docs")
    with pytest.raises(ValueError): publisher.lineage(root, source, git(root, "rev-parse", "HEAD"))


def test_pages_when_exact_y_build_completes_then_receipt_binds_actual_commit(repository, monkeypatch, tmp_path):
    root, source = repository
    calls = []
    def api(method, endpoint):
        calls.append((method, endpoint))
        if endpoint == "pages": return {"source": {"branch": "main", "path": "/docs"}}
        if method == "POST": return {"url": "https://api.github.com/build/latest", "status": "queued"}
        return {"commit": source, "status": "built", "url": "https://api.github.com/build/123"}
    monkeypatch.setattr(publisher, "api", api)
    receipt = tmp_path / "receipt.json"
    publisher.pages(root, source, source, receipt)
    assert json.loads(receipt.read_text())["build"]["commit"] == source
    assert ("POST", "pages/builds") in calls


@pytest.mark.parametrize("damage", ["settings", "failed", "wrong-commit", "stale"])
def test_pages_when_unqualified_or_superseded_then_never_claims_success(repository, monkeypatch, tmp_path, damage):
    root, source = repository
    def api(method, endpoint):
        if endpoint == "pages": return {"source": {"branch": "main", "path": "/" if damage == "settings" else "/docs"}}
        if method == "POST": return {"status": "queued"}
        return {"commit": "a" * 40 if damage == "wrong-commit" else source,
                "status": "errored" if damage == "failed" else "built"}
    monkeypatch.setattr(publisher, "api", api)
    monkeypatch.setattr(publisher.time, "sleep", lambda _: None)
    monkeypatch.setattr(publisher, "PAGES_ATTEMPTS", 2)
    if damage == "stale": monkeypatch.setattr(publisher, "remote_main", lambda _: "b" * 40)
    with pytest.raises((ValueError, TimeoutError)): publisher.pages(root, source, source, tmp_path / "receipt.json")


def test_epoch_when_generated_commit_crosses_utc_day_then_render_preserves_x_date(repository, monkeypatch, tmp_path):
    root, source = repository
    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    publisher.output("epoch", git(root, "show", "-s", "--format=%ct", source))
    transferred = int(output.read_text().split("=")[1])
    assert transferred == int(git(root, "show", "-s", "--format=%ct", source))
    (tmp_path / "content").mkdir()
    (tmp_path / "content/index.md").write_text("# Epoch fixture\n")
    config = tmp_path / "mkdocs.yml"
    config.write_text("site_name: Epoch fixture\ndocs_dir: content\nsite_dir: rendered\nsite_url: https://example.invalid/\ntheme: materialx\nplugins: []\n")
    command = ["properdocs", "build", "--strict", "--clean", "-f", str(config)]
    subprocess.run(command, check=True, capture_output=True, env=os.environ | {"SOURCE_DATE_EPOCH": str(transferred)})
    baseline = (tmp_path / "rendered/sitemap.xml").read_bytes()
    subprocess.run(command, check=True, capture_output=True, env=os.environ | {"SOURCE_DATE_EPOCH": str(transferred + 86400)})
    assert (tmp_path / "rendered/sitemap.xml").read_bytes() != baseline, "Control: UTC date changes rendered output"
    subprocess.run(command, check=True, capture_output=True, env=os.environ | {"SOURCE_DATE_EPOCH": str(transferred)})
    assert (tmp_path / "rendered/sitemap.xml").read_bytes() == baseline, "Y must retain X's captured epoch"


def test_publish_when_precommit_hook_rejects_then_never_bypasses_hook(repository):
    root, source = repository
    hook = root / ".git/hooks/pre-commit"
    hook.write_text("#!/bin/sh\nexit 23\n")
    hook.chmod(0o755)
    (root / "docs/index.html").write_text("changed\n")
    with pytest.raises(subprocess.CalledProcessError): publisher.publish(root, source)
    assert publisher.remote_main(root) == source


@pytest.mark.parametrize("method,status", [("GET", 200), ("POST", 201), ("POST", 200)])
def test_api_when_request_then_checks_status_and_uses_only_job_token(monkeypatch, method, status):
    class Response(io.BytesIO):
        pass
    requests = []
    def urlopen(request, *, timeout):
        requests.append((request, timeout))
        response = Response(b'{"status":"queued"}')
        response.status = status
        return response
    monkeypatch.setenv("GITHUB_TOKEN", "synthetic-job-token")
    monkeypatch.setattr(publisher.urllib.request, "urlopen", urlopen)
    if method == "POST" and status != 201:
        with pytest.raises(ValueError): publisher.api(method, "pages/builds")
    else:
        assert publisher.api(method, "pages/builds") == {"status": "queued"}
    request, timeout = requests[0]
    assert request.full_url == "https://api.github.com/repos/fontlabcom/fontlab-python-docs/pages/builds"
    assert request.get_header("Authorization") == "Bearer synthetic-job-token"
    assert timeout == 60


def test_main_when_real_publication_and_qualification_then_writes_bound_output(repository, monkeypatch, tmp_path):
    root, source = repository
    monkeypatch.chdir(root)
    output = tmp_path / "output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    publisher.main(["publish", source])
    assert output.read_text() == f"sha={source}\n"
    publisher.main(["lineage", source, source])
    publisher.main(["parity"])
    def api(method, endpoint):
        if endpoint == "pages": return {"source": {"branch": "main", "path": "/docs"}}
        return {"commit": source, "status": "built"}
    monkeypatch.setattr(publisher, "api", api)
    publisher.main(["pages", source, source, str(tmp_path / "receipt.json")])
    with pytest.raises(ValueError): publisher.main(["unknown"])
