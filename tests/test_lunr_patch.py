# this_file: tests/test_lunr_patch.py
"""The stock MaterialX worker ships with the lunr TokenSet key fix (issue 106)."""

import pytest

from scripts.lunr_patch import PATCHED, UNPATCHED, patch_stock_worker

WORKER = "assets/javascripts/workers/search.2c215733.min.js"


def _site(tmp_path, body):
    worker = tmp_path / WORKER
    worker.parent.mkdir(parents=True)
    worker.write_text(body)
    return worker


def test_patch_stock_worker_when_original_key_present_then_rewrites_it_once(tmp_path):
    worker = _site(tmp_path, "a;" + UNPATCHED + "return e};b")
    assert patch_stock_worker(tmp_path) == worker
    assert worker.read_text() == "a;" + PATCHED + "return e};b"


@pytest.mark.parametrize("body", ["no lunr here", UNPATCHED * 2, PATCHED])
def test_patch_stock_worker_when_match_is_not_exactly_one_then_fails(tmp_path, body):
    """A MaterialX upgrade must fail loudly instead of shipping or double-patching."""
    _site(tmp_path, body)
    with pytest.raises(ValueError, match="exactly once"):
        patch_stock_worker(tmp_path)


def test_patch_stock_worker_when_worker_missing_then_fails(tmp_path):
    with pytest.raises(ValueError, match="one stock search worker"):
        patch_stock_worker(tmp_path)
