# this_file: tests/test_final_fixes.py
"""Regression gates for complete source identities and build lifecycle."""

import json
from pathlib import Path

from scripts.api_inventory import inventory_sources, plan_pages
from scripts.reference_pages import render_page
from scripts.search_identities import qualify_titles


def test_shared_search_routes_every_occurrence_and_alias_to_its_body():
    symbols = {
        "pkg.A.resize": {
            "kind": "function",
            "url": "a.html#pkg.A.resize",
            "body_target": "pkg.A.resize",
            "body_url": "body.html#pkg.A.resize",
        },
        "pkg.B.resize": {
            "kind": "function",
            "url": "b.html#pkg.B.resize",
            "body_target": "pkg.A.resize",
            "body_url": "body.html#pkg.A.resize",
        },
    }
    data = {
        "docs": [
            {
                "location": "body.html#pkg.A.resize",
                "title": "resize",
                "text": "Documentation",
            }
        ]
    }
    qualify_titles(data, symbols, {"public.B.resize": "pkg.B.resize"})
    assert {"pkg.B.resize", "public.B.resize"} <= set(data["docs"][0]["tags"])
    before = json.dumps(data)
    qualify_titles(data, symbols, {"public.B.resize": "pkg.B.resize"})
    assert json.dumps(data) == before


def test_guarded_inheritance_and_nested_navigation(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text(
        "raise RuntimeError('never import')\nclass Base:\n    def inherited(self): pass\n    def overridden(self): pass\nclass Child(Base):\n    def overridden(self, arg): pass\n    class Nested: pass\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    child = plan["symbols"]["pkg.Child"]
    assert child["bases"] == [{"expression": "Base", "target": "pkg.Base"}]
    assert child["inherited_members"] == {"inherited": "pkg.Base.inherited"}
    assert plan["aliases"]["pkg.Child.inherited"] == "pkg.Base.inherited"
    text = render_page("reference/pkg/Child.md", plan)
    assert "Base.md#pkg.Base" in text
    assert "#pkg.Base.inherited" in text
    assert "Nested.md" in text


def test_actual_void_has_source_proven_point_members():
    root = Path(__file__).resolve().parents[2] / "typerig-lib/Lib"
    plan = plan_pages(inventory_sources([(root, "typerig")]))
    row = plan["symbols"]["typerig.core.objects.point.Void"]
    assert row["bases"] == [
        {"expression": "Point", "target": "typerig.core.objects.point.Point"}
    ]
    for name in ("angle_to", "doSwap", "doFlip", "doTransform"):
        assert (
            row["inherited_members"][name] == "typerig.core.objects.point.Point." + name
        )
    assert "Point.md#typerig.core.objects.point.Point" in render_page(
        "reference/typerig/core/objects/point/Void.md", plan
    )


def test_diamond_inheritance_uses_c3_and_local_overrides(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text(
        "class A:\n    def value(self): pass\n"
        "class B(A): pass\n"
        "class C(A):\n    def value(self, x): pass\n"
        "class D(B, C): pass\n"
        "class E(D):\n    def value(self, y, z): pass\n"
        "class Unknown(Missing): pass\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert plan["symbols"]["pkg.D"]["inherited_members"]["value"] == "pkg.C.value"
    assert not plan["symbols"]["pkg.E"]["inherited_members"]
    assert not plan["symbols"]["pkg.Unknown"]["inherited_members"]
    assert plan["symbols"]["pkg.Unknown"]["bases"][0]["target"] is None


def test_imported_base_and_exported_inherited_alias_are_source_proven(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("from .child import Child as Public\n")
    (pkg / "base.py").write_text("class Base:\n    def value(self): pass\n")
    (pkg / "child.py").write_text(
        "from .base import Base as Parent\nclass Child(Parent): pass\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert plan["symbols"]["pkg.child.Child"]["bases"] == [
        {"expression": "Parent", "target": "pkg.base.Base"}
    ]
    assert plan["aliases"]["pkg.Public.value"] == "pkg.base.Base.value"
