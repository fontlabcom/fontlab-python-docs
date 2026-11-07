# this_file: tests/test_frontend_notices.py
"""Full source-bound browser notices must survive documentation builds."""
import hashlib
import json
from pathlib import Path

import pytest

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

    git = shutil.which("git")
    if git is None:
        pytest.skip("Git distribution check requires Git; manifest byte checks still run")
    env = _git_environment(git, tmp_path)
    repository = tmp_path / "repository"
    repository.mkdir()

    def run(*args):
        return subprocess.check_output(
            [git, "-c", "core.autocrlf=input", "-C", str(repository), *args],
            stderr=subprocess.PIPE, env=env, timeout=10,
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


def _git_environment(git, directory):
    """Drop Git's documented repository-local variables for a foreign repository."""
    import os
    import subprocess

    names = subprocess.check_output(
        [git, "rev-parse", "--local-env-vars"], cwd=directory,
        stderr=subprocess.PIPE, timeout=10,
    ).decode().splitlines()
    return {key: value for key, value in os.environ.items() if key not in names}


@pytest.mark.parametrize("alternate_index", [False, True])
def test_notice_distribution_when_git_context_is_inherited_then_parent_is_unchanged(
    tmp_path, monkeypatch, alternate_index,
):
    """Hook variables may name another repository despite Git's -C option."""
    import os
    import shutil
    import subprocess

    git = shutil.which("git")
    if git is None:
        pytest.skip("Git isolation check requires Git; manifest byte checks still run")
    parent = tmp_path / "parent"
    parent.mkdir()
    env = _git_environment(git, tmp_path)

    def run(*args):
        return subprocess.check_output(
            [git, "-C", str(parent), *args], env=env,
            stderr=subprocess.PIPE, timeout=10,
        )

    run("init", "--quiet")
    (parent / "sentinel.txt").write_bytes(b"preserve parent index and working tree\n")
    run("add", "sentinel.txt")
    tree = run("write-tree").decode().strip()
    commit = subprocess.check_output(
        [git, "-C", str(parent), "-c", "user.name=Notice fixture",
         "-c", "user.email=fixture@example.invalid", "commit-tree", tree],
        input=b"Private isolation fixture\n", env=env, stderr=subprocess.PIPE, timeout=10,
    ).decode().strip()
    run("update-ref", "refs/heads/notice-fixture", commit)
    (parent / "sentinel.txt").write_bytes(b"unstaged parent bytes must also survive\n")
    index = parent / ".git/index"
    if alternate_index:
        index = parent / "alternate-index"
        shutil.copyfile(parent / ".git/index", index)
    alternate_objects = tmp_path / "alternate-objects"
    alternate_objects.mkdir()
    inherited = {
        "GIT_DIR": str(parent / ".git"),
        "GIT_WORK_TREE": str(parent),
        "GIT_COMMON_DIR": str(parent / ".git"),
        "GIT_INDEX_FILE": str(index),
        "GIT_OBJECT_DIRECTORY": str(parent / ".git/objects"),
        "GIT_ALTERNATE_OBJECT_DIRECTORIES": str(alternate_objects),
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "core.autocrlf",
        "GIT_CONFIG_VALUE_0": "true",
    }
    if not alternate_index:
        # A hook can leave work-tree discovery to the foreign command's -C.
        inherited.pop("GIT_WORK_TREE")
    for key, value in inherited.items():
        monkeypatch.setenv(key, value)
    outer_env = dict(os.environ)

    def snapshot():
        return {path.relative_to(parent).as_posix(): path.read_bytes()
                for path in parent.rglob("*") if path.is_file()}

    before = snapshot()
    try:
        test_frontend_notice_bytes_survive_git_filters_checkout_and_archive(tmp_path)
    finally:
        assert dict(os.environ) == outer_env, "Foreign Git commands changed the caller environment"
        assert snapshot() == before, "Foreign Git commands changed parent index/config/refs/tree/objects"
        assert not any(alternate_objects.iterdir()), "Foreign Git commands wrote alternate objects"


def test_archive_notices_when_bound_then_exact_component_sources_and_scope():
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    components = {item["name"]: item for item in manifest["components"]}
    archive_url = "https://registry.npmjs.org/lunr-languages/-/lunr-languages-1.14.0.tgz"
    cases = [
        ("TinySegmenter", "0.1", "tinyseg.js", "bsd-tinysegmenter.txt", 1485,
         "ba1aea1dfa045e96563b5a7a6878d91a88231fc4acef57d7109345f3d9153ee1"),
        ("stopwords-filter French data", "vendored in lunr-languages 1.14.0",
         "min/lunr.fr.min.js", "mit-stopwords-filter.txt", 1059,
         "0905c5c7efbf514976764ba3a8fe324ea3bf805ebbce8e902517fbe02d750bcf"),
    ]
    for name, version, member, filename, size, digest in cases:
        component = components[name]
        assert component["version"] == version
        assert component["source_url"] == archive_url
        assert component["shipped_member"] == "package/" + member
        assert component["shipped_paths"] == [
            prefix + "assets/javascripts/lunr/" + member
            for prefix in ("", "archive/fontlab7/", "archive/fontlab7/pythonqt/")
        ]
        assert component["notices"] == [{"path": "licenses/" + filename, "sha256": digest}]
        data = (DOCS / "licenses" / filename).read_bytes()
        assert len(data) == size and hashlib.sha256(data).hexdigest() == digest
        assert b"\r" not in data
    tiny = components["TinySegmenter"]
    assert tiny["notice_source_url"] == "http://chasen.org/~taku/software/TinySegmenter/LICENCE.txt"
    assert tiny["shipped_sha256"] == "1b044c239610ef65fceff6039567442bb1692d413f5ee8686fee81b1a3067761"
    assert b"<ORGANIZATION>" in (DOCS / "licenses/bsd-tinysegmenter.txt").read_bytes()
    french = components["stopwords-filter French data"]
    assert french["source_member"] == "package/build/stopwords-filter/lib/stopwords/snowball/locales/fr.csv"
    assert french["derived_language"] == "fr"
    assert french["shipped_sha256"] == "4dd56aa2551e770ad26ef4b85092cd31447671e0e84b39514278547f54177377"
    assert french["source_sha256"] == "7145f68621c83e98c2ff6db9d3b7b44bbefd85913a6fa3f0bf8a2ccd7e4cdba3"
    assert french["notice_member"] == "package/build/stopwords-filter/LICENSE.txt"
    assert french["scope"] == "French stopword-data derivation only; no claim about other languages."
    assert manifest["complete_transitive_inventory"] is False
    assert manifest["publication_qualified"] is False


@pytest.mark.parametrize("field", ["version", "shipped_member", "derived_language", "notices"])
def test_archive_notice_when_binding_is_missing_or_wrong_then_contract_rejects(
    tmp_path, monkeypatch, field,
):
    import shutil
    import sys

    shutil.copytree(DOCS / "licenses", tmp_path / "licenses")
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    french = next(item for item in manifest["components"] if item["name"] == "stopwords-filter French data")
    french[field] = [] if field == "notices" else "unproved"
    (tmp_path / "frontend-notices.json").write_text(json.dumps(manifest))
    monkeypatch.setattr(sys.modules[__name__], "DOCS", tmp_path)
    with pytest.raises(AssertionError):
        test_archive_notices_when_bound_then_exact_component_sources_and_scope()
