# this_file: tests/test_export_aliases.py
"""Statically exported package APIs must not disappear behind lazy imports."""

from scripts.api_inventory import inventory_sources, plan_pages
from scripts.build_reference import _aliases
from scripts.export_aliases import resolved_aliases


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


def test_export_when_chained_private_class_then_real_descendants_are_exposed(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("from ._bridge import Public\n")
    (package / "_bridge.py").write_text("from ._impl import Handle as Public\n")
    (package / "_impl.py").write_text(
        "raise RuntimeError('never import')\n"
        "class Handle:\n    def close(self): ...\n"
        "    class Nested:\n        value: int\n"
        "    def _secret(self): ...\n"
        "class Unexported: ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    aliases = _aliases(plan)
    assert aliases["pkg.Public"] == "pkg._impl.Handle"
    assert aliases["pkg.Public.close"] == "pkg._impl.Handle.close"
    assert aliases["pkg.Public.Nested.value"] == "pkg._impl.Handle.Nested.value"
    assert "pkg.Public._secret" not in aliases, "private members are not public exports"
    assert "pkg._impl.Unexported" not in plan["symbols"]
    assert "pkg._impl.Handle.close" in plan["symbols"]
    assert "pkg.Public.close" not in plan["symbols"], (
        "aliases must not duplicate bodies"
    )


def test_export_when_private_module_alias_then_module_descendants_are_exposed(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("from . import _impl as api\n")
    (package / "_impl.py").write_text("class Handle:\n    def close(self): ...\n")
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan)["pkg.api.Handle.close"] == "pkg._impl.Handle.close"


def test_export_when_module_reexports_class_then_descendant_aliases_are_exposed(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("from . import _bridge as api\n")
    (package / "_bridge.py").write_text("from ._impl import Handle as Public\n")
    (package / "_impl.py").write_text("class Handle:\n    def close(self): ...\n")
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    aliases = _aliases(plan)
    assert aliases["pkg.api.Public"] == "pkg._impl.Handle"
    assert aliases["pkg.api.Public.close"] == "pkg._impl.Handle.close"


def test_export_when_cycle_or_unproven_target_then_no_members_are_invented(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text(
        "ALIASES = {'First': 'pkg.Second', 'Second': 'pkg.First', "
        "'Unknown': 'native.Unknown'}\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan) == {}, "cyclic/unproven exports must stay unresolved"


def test_export_when_native_module_alias_then_native_body_identity_is_primary(tmp_path):
    native = tmp_path / "fontlab_echopy"
    native.mkdir()
    (native / "fontlab.pyi").write_text("class Node:\n    def close(self): ...\n")
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text(
        "ALIASES = {'api': 'fontlab_echopy.fontlab'}\n"
    )
    plan = plan_pages(
        inventory_sources([(tmp_path, "fontlab_echopy"), (tmp_path, "pkg")])
    )
    row = plan["symbols"]["fontlab.Node.close"]
    assert _aliases(plan)["pkg.api.Node.close"] == "fontlab.Node.close"
    assert row["canonical_id"] == "fontlab_echopy.fontlab.Node.close"
    assert row["body_target"] == "fontlab.Node.close"


def test_export_when_module_graph_cycles_then_finite_source_descendants_are_kept():
    aliases = {"pkg.api": "pkg.impl", "pkg.impl.back": "pkg"}
    symbols = {
        "pkg": {"kind": "module"},
        "pkg.impl": {"kind": "module"},
        "pkg.impl.value": {"kind": "function"},
    }
    resolved = resolved_aliases(aliases, symbols)
    assert resolved["pkg.api.value"] == "pkg.impl.value"
    assert len(resolved) < 20, (
        "recursive module exports must not create infinite aliases"
    )


def test_export_when_target_is_member_through_alias_prefix_then_real_identity_is_kept():
    aliases = {"pkg.Public": "pkg.impl.Handle", "pkg.close": "pkg.Public.close"}
    symbols = {
        "pkg.impl.Handle": {"kind": "class"},
        "pkg.impl.Handle.close": {"kind": "function"},
    }
    resolved = resolved_aliases(aliases, symbols)
    assert (
        resolved["pkg.close"] == resolved["pkg.Public.close"] == "pkg.impl.Handle.close"
    )
