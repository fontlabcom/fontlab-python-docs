# this_file: tests/test_sibling_sources.py
"""The sibling guard skips only when both the variable and the checkout are absent."""

import pytest
from sibling_sources import ENV, require_sibling


def assert_runs(repo, root, message):
    """A skip here is a failure: a "runs" case must never silently skip."""
    try:
        require_sibling(repo, root)
    except pytest.skip.Exception as skip:
        pytest.fail(f"{message}; skipped instead: {skip}")


def test_require_sibling_when_absent_and_unset_then_skips_with_reason(
    tmp_path, monkeypatch
):
    monkeypatch.delenv(ENV, raising=False)
    root = tmp_path / "docs"
    root.mkdir()
    with pytest.raises(
        pytest.skip.Exception, match=r"\.\./TypeRig or FONTLAB_API_SOURCE_ROOT"
    ):
        require_sibling("TypeRig", root)


def test_require_sibling_when_checkout_present_then_runs(tmp_path, monkeypatch):
    monkeypatch.delenv(ENV, raising=False)
    root = tmp_path / "docs"
    root.mkdir()
    (tmp_path / "TypeRig").mkdir()
    assert_runs("TypeRig", root, "a present sibling checkout must run the test")


def test_require_sibling_when_variable_set_then_runs_even_without_checkout(
    tmp_path, monkeypatch
):
    monkeypatch.setenv(ENV, str(tmp_path / "missing"))
    root = tmp_path / "docs"
    root.mkdir()
    assert_runs("TypeRig", root, "the build must fail on a missing source, not skip")


def test_require_sibling_when_sibling_is_a_file_then_skips(tmp_path, monkeypatch):
    monkeypatch.delenv(ENV, raising=False)
    root = tmp_path / "docs"
    root.mkdir()
    (tmp_path / "TypeRig").write_text("")
    with pytest.raises(pytest.skip.Exception):
        require_sibling("TypeRig", root)
