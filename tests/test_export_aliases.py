# this_file: tests/test_export_aliases.py
"""Statically exported package APIs must not disappear behind lazy imports."""

from scripts.api_inventory import inventory_sources


def test_export_when_explicit_relative_import_then_public_alias_is_indexed(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text(
        "from .api import Example as Public\n__all__ = ['Public']\n"
    )
    (package / "api.py").write_text("class Example:\n    def value(self): ...\n")
    data = inventory_sources([(tmp_path, "pkg")])
    assert data["aliases"]["pkg.Public"] == "pkg.api.Example"


def test_export_when_private_module_public_class_then_source_target_is_kept(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text(
        "from ._runtime import HostError\n__all__ = ['HostError']\n"
    )
    (package / "_runtime.py").write_text("class HostError(RuntimeError): ...\n")
    data = inventory_sources([(tmp_path, "pkg")])
    assert data["aliases"]["pkg.HostError"] == "pkg._runtime.HostError"
    assert "pkg._runtime.HostError" in data["symbols"], (
        "exported error class lost with private file"
    )
