# this_file: tests/test_source_lock.py
"""Source locks must catch missing, modified and unexpected API inputs."""

import pytest

from scripts.api_inventory import inventory_sources
from scripts.source_lock import verify_inputs


def test_source_lock_when_input_hash_changes_then_build_fails():
    with pytest.raises(ValueError, match="source lock"):
        verify_inputs(
            {"pkg/api.pyi": "original"},
            [{"source": "pkg/api.pyi", "sha256": "changed"}],
        )


def test_source_lock_when_input_set_changes_then_build_fails():
    with pytest.raises(ValueError, match="source lock"):
        verify_inputs({"pkg/api.pyi": "original"}, [])


def test_source_lock_when_all_source_bytes_match_then_passes():
    verify_inputs(
        {"pkg/api.pyi": "original"}, [{"source": "pkg/api.pyi", "sha256": "original"}]
    )


@pytest.mark.parametrize("change", ["modified", "added", "removed"])
def test_source_lock_when_consumed_private_input_changes_then_fails(tmp_path, change):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("raise RuntimeError('never import')\n")
    private = package / "_native.py"
    private.write_text("def hidden(): ...\n")
    original = inventory_sources([(tmp_path, "pkg")])
    locked = {row["source"]: row["sha256"] for row in original["inputs"]}
    assert "pkg/_native.py" in locked, "consumed private bytes must be pinned"
    assert "pkg._native" not in original["symbols"], "pinning does not imply visibility"
    if change == "modified":
        private.write_text("def changed(): ...\n")
    elif change == "added":
        (package / "_extra.py").write_text("def extra(): ...\n")
    else:
        private.unlink()
    with pytest.raises(ValueError, match="source lock"):
        verify_inputs(locked, inventory_sources([(tmp_path, "pkg")])["inputs"])


def test_inputs_when_stub_has_runtime_counterpart_then_both_are_pinned_once(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "api.py").write_text("raise RuntimeError('never import')\n")
    (package / "api.pyi").write_text("class Native: ...\n")
    inventory = inventory_sources([(tmp_path, "pkg"), (tmp_path, "pkg")])
    assert [row["source"] for row in inventory["inputs"]] == [
        "pkg/api.py",
        "pkg/api.pyi",
    ], "consumer inputs must be pinned exactly once, including merged counterparts"


def test_source_lock_when_duplicate_input_conflicts_then_fails():
    with pytest.raises(ValueError, match="Duplicate"):
        verify_inputs(
            {"pkg/api.py": "original"},
            [
                {"source": "pkg/api.py", "sha256": "original"},
                {"source": "pkg/api.py", "sha256": "changed"},
            ],
        )
