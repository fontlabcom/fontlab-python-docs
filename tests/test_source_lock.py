# this_file: tests/test_source_lock.py
"""Source locks must catch missing, modified and unexpected API inputs."""

import pytest

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
