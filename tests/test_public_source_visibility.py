# this_file: tests/test_public_source_visibility.py
"""Explicit exports and inherited public APIs must survive private source files."""

import ast

import pytest

from scripts.api_inventory import inventory_sources, plan_pages
from scripts.build_reference import _aliases
from scripts.export_aliases import exported_aliases


@pytest.mark.parametrize(
    "source, expected",
    [
        ("__all__ = ['Missing', 'Cpp::Nested']", {}),
        (
            "from pkg._impl import value as value",
            {"public.api.value": "pkg._impl.value"},
        ),
        ("from pkg._impl import value", {}),
        ("from pkg._impl import value as internal", {}),
        ("from pkg._impl import value as value\n__all__ = []", {}),
        ("import pkg as pkg", {"public.api.pkg": "pkg"}),
        ("import pkg", {}),
        ("import pkg as pkg\n__all__ = []", {}),
        ("import pkg.sub as api\n__all__ = ['api']", {"public.api.api": "pkg.sub"}),
        ("import pkg.sub\n__all__ = ['pkg']", {"public.api.pkg": "pkg"}),
        (
            "import pkg as _private\n__all__ = ['_private']",
            {"public.api._private": "pkg"},
        ),
    ],
)
def test_export_when_explicit_source_forms_then_only_declared_aliases_are_visible(
    source, expected
):
    assert exported_aliases(ast.parse(source), "public.api", package=False) == expected


@pytest.mark.parametrize("extension", ["py", "pyi"])
def test_inventory_when_absolute_self_alias_then_private_body_has_public_route(
    tmp_path, extension
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / f"api.{extension}").write_text("from pkg._impl import value as value\n")
    (package / f"_impl.{extension}").write_text(
        "raise RuntimeError('source must never execute')\n"
        "def value(owner, name):\n    '''Read a known value.'''\n    ...\n"
        "def unused(): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan)["pkg.api.value"] == "pkg._impl.value"
    assert plan["symbols"]["pkg._impl.value"]["source"] == f"pkg/_impl.{extension}"
    assert "pkg._impl.unused" not in plan["symbols"]
    assert "pkg.api.value" not in plan["symbols"], "Keep one canonical body"


@pytest.mark.parametrize("private_file", [False, True])
def test_inventory_when_public_class_uses_private_base_then_public_inheritance_is_complete(
    tmp_path, private_file
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    base = "class _Base:\n    def close(self): ...\n    def _secret(self): ...\nclass _Unused: ...\n"
    if private_file:
        (package / "_base.py").write_text(base)
        source = "from pkg._base import _Base\nclass Public(_Base): ...\n"
        origin = "pkg._base._Base"
    else:
        source = base + "class Public(_Base): ...\n"
        origin = "pkg.api._Base"
    (package / "api.py").write_text(source)
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan)["pkg.api.Public.close"] == origin + ".close"
    assert plan["symbols"]["pkg.api.Public"]["inheritance_status"] == "source-proven"
    assert origin + "._secret" not in plan["symbols"]
    assert not any(name.endswith("._Unused") for name in plan["symbols"])


def test_inventory_when_private_base_chain_then_overrides_and_c3_order_are_preserved(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "_base.py").write_text(
        "class _Root:\n    def close(self): ...\n    def value(self): ...\n"
        "class _Left(_Root):\n    def value(self): ...\n"
        "class _Right(_Root): ...\n"
    )
    (package / "api.py").write_text(
        "from pkg._base import _Left, _Right\n"
        "class Public(_Left, _Right):\n    def close(self): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    aliases = _aliases(plan)
    assert aliases["pkg.api.Public.value"] == "pkg._base._Left.value"
    assert "pkg.api.Public.close" not in aliases, "A real override owns its body"
    assert "pkg.api.Public.close" in plan["symbols"]


@pytest.mark.parametrize("header", ["factory()", "Missing"])
def test_inventory_when_base_is_unproven_then_private_members_are_not_invented(
    tmp_path, header
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "api.py").write_text(
        f"class _Base:\n    def close(self): ...\nclass Public({header}): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert "pkg.api.Public.close" not in _aliases(plan)
    assert "pkg.api._Base" not in plan["symbols"]


@pytest.mark.parametrize("export", ["local", "imported"])
def test_inventory_when_private_function_is_explicitly_exported_then_only_that_body_is_kept(
    tmp_path, export
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    if export == "local":
        (package / "api.py").write_text(
            "__all__ = ['_value']\ndef _value(): ...\ndef _unused(): ...\n"
        )
        target = "pkg.api._value"
    else:
        (package / "api.py").write_text(
            "from pkg._impl import _value as value\n__all__ = ['value']\n"
        )
        (package / "_impl.py").write_text("def _value(): ...\ndef _unused(): ...\n")
        target = "pkg._impl._value"
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert target in plan["symbols"]
    assert not any(name.endswith("._unused") for name in plan["symbols"])
    if export == "imported":
        assert _aliases(plan)["pkg.api.value"] == target


def test_inventory_when_private_base_has_private_nested_class_then_unrelated_members_stay_hidden(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "api.py").write_text(
        "class _Base:\n    def close(self): ...\n    def _secret(self): ...\n"
        "    class _Unrelated:\n        def leaked(self): ...\n"
        "class Public(_Base): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan)["pkg.api.Public.close"] == "pkg.api._Base.close"
    assert not any(
        "_Unrelated" in name or name.endswith("._secret") for name in plan["symbols"]
    )


def test_inventory_when_private_nested_class_is_a_real_base_then_only_its_scope_is_exposed(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text("")
    (package / "api.py").write_text(
        "class _Outer:\n    def unrelated(self): ...\n"
        "    class _Base:\n        def close(self): ...\n"
        "class Public(_Outer._Base): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert _aliases(plan)["pkg.api.Public.close"] == "pkg.api._Outer._Base.close"
    assert "pkg.api._Outer.unrelated" not in plan["symbols"]
