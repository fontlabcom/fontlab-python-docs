# this_file: tests/test_frontend_notices.py
"""Full source-bound browser notices must survive documentation builds."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "src_docs/md"


def test_frontend_notices_when_authored_then_every_full_text_is_present():
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    page = (DOCS / "frontend-notices.md").read_text()
    assert manifest["components"], "Browser notices must name their components"
    for component in manifest["components"]:
        assert component["source_url"].startswith("https://"), component["name"]
        for item in component["notices"]:
            path = DOCS / item["path"]
            assert path.is_file(), item["path"]
            assert len(path.read_bytes()) > 200, "An abbreviated licence link is not a full notice"
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], item["path"]
            assert item["path"] in page, "Every retained notice must be visible on the licences route"
    assert "frontend-notices.md" in (DOCS / "licenses.md").read_text()


def test_frontend_notices_when_review_is_partial_then_pending_scope_is_explicit():
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    if not manifest["complete_transitive_inventory"]:
        assert manifest["pending"], "A partial audit must retain every unresolved component group"
        assert "still being reviewed" in (DOCS / "frontend-notices.md").read_text()
    assert "publication_qualified" not in manifest or manifest["publication_qualified"] is False


def test_frontend_notice_bytes_survive_git_filters_checkout_and_archive(tmp_path):
    """Exercise distribution filters even from an SDK or a Git-free source archive."""
    import io
    import shutil
    import subprocess
    import tarfile

    import pytest

    git = shutil.which("git")
    if git is None:
        pytest.skip("Git distribution check requires Git; manifest byte checks still run")
    repository = tmp_path / "repository"
    repository.mkdir()

    def run(*args):
        return subprocess.check_output(
            [git, "-c", "core.autocrlf=input", "-C", str(repository), *args],
            stderr=subprocess.PIPE,
        )

    run("init", "--quiet")
    attributes = ROOT / ".gitattributes"
    if attributes.exists():
        shutil.copyfile(attributes, repository / ".gitattributes")
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    notices = {item["path"] for component in manifest["components"] for item in component["notices"]}
    notices.update(path.relative_to(DOCS).as_posix() for path in (DOCS / "licenses").rglob("*") if path.is_file())
    payloads = {}
    for notice in sorted(notices):
        relative = "src_docs/md/" + notice
        payload = (DOCS / notice).read_bytes()
        # Include CRLF probes for LF-only notices: every listed payload must be protected.
        probe = payload.replace(b"\r\n", b"\n").replace(b"\n", b"\r\n")
        target = repository / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(probe)
        payloads[relative] = probe
    run("add", ".")
    checkout = tmp_path / "checkout"
    checkout.mkdir()
    run("checkout-index", "--all", "--prefix=" + str(checkout) + "/")
    tree = run("write-tree").decode().strip()
    with tarfile.open(fileobj=io.BytesIO(run("archive", "--format=tar", tree))) as archive:
        for relative, payload in payloads.items():
            assert run("show", ":" + relative) == payload, relative + " normalized in index"
            assert (checkout / relative).read_bytes() == payload, relative + " changed on checkout"
            assert archive.extractfile(relative).read() == payload, relative + " changed in archive"
