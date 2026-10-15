# this_file: tests/test_reconcile_coverage.py
"""Every captured identity must be documented or carry a machine-checked reason."""

import copy

import pytest

from scripts.api_inventory import inventory_sources
from scripts.reconcile_coverage import enforce, reconcile

MANIFEST = {
    "schema_version": 1,
    "producer": "fontlab_echopy.tooling.identities",
    "capture_sha256": "a" * 64,
    "scopes": {
        "fontlab": {
            "available": True,
            "kind": "module",
            "names": ["Box::Inner", "Node", "get_value"],
            "errors": [],
            "classes": {
                "Box::Inner": {"members": ["size"], "constructors": ["__init__"], "errors": []},
                "Node": {"members": ["_p", "raise"], "constructors": ["__init__"], "errors": []},
            },
        },
        "fontlabpr": {
            "available": False,
            "reason": "native module absent",
            "kind": "module",
            "names": [],
            "errors": [],
            "classes": {},
        },
        "PythonQt": {
            "available": True,
            "kind": "module",
            "names": ["BoolResult"],
            "errors": [],
            "classes": {},
        },
        "PythonQt.BoolResult": {
            "available": True,
            "kind": "type",
            "names": [],
            "errors": [],
            "classes": {},
        },
    },
    "native_spellings": {
        "fontlab.Box::Inner": "fontlab.Box__Inner",
        "fontlab.Box::Inner.__init__": "fontlab.Box__Inner.__init__",
        "fontlab.Box::Inner.size": "fontlab.Box__Inner.size",
        "fontlab.Node.raise": "fontlab.Node.raise_",
    },
    "maintained_extensions": ["fontlab.Node.helper"],
    "merge_unmatched": [],
    "enrichment_gaps": {
        "qt_document_failures": {"Node": "HTTP Error 404: Not Found"},
        "unmatched_native_classes": ["Box::Inner"],
    },
}

IDS = [
    "fontlab",
    "fontlab.Box__Inner",
    "fontlab.Box__Inner.__init__",
    "fontlab.Box__Inner.size",
    "fontlab.Node",
    "fontlab.Node.__init__",
    "fontlab.Node._p",
    "fontlab.Node.raise_",
    "fontlab.Node.helper",
    "fontlab.get_value",
    "fontlabpr",
    "PythonQt",
    "PythonQt.BoolResult",
    "typerig",
]


def _symbols():
    rows = {i: {"id": i, "kind": "function", "occurrences": 1} for i in IDS}
    rows["PythonQt.BoolResult"].update(kind="class", occurrences=2, facets=[{"kind": "module"}])
    rows["typerig"].update(occurrences=2, declarations=[{"line": 1}, {"line": 9}])
    return rows


def _unexplained(manifest=MANIFEST, symbols=None, aliases=None):
    report = reconcile(
        manifest,
        _symbols() if symbols is None else symbols,
        aliases or {"fly.qt": "PythonQt"},
        provenance_capture_sha256="a" * 64,
    )
    return report, {(row["problem"], row["id"]) for row in report["unexplained"]}


def test_reconcile_when_everything_is_documented_or_explained_then_no_gap():
    report, unexplained = _unexplained()
    assert unexplained == set(), unexplained
    assert report["counts"]["captured_identities"] == 12
    assert report["counts"]["documented_under_native_spelling"] == 4
    assert report["explained"]["maintained_extension"] == ["fontlab.Node.helper"]
    assert report["explained"]["absent_optional_module"] == {
        "fontlabpr": "native module absent"
    }
    assert report["explained"]["multiple_declarations"] == {
        "PythonQt.BoolResult": "module-and-class-facet",
        "typerig": "ecosystem-source-redefinition",
    }
    assert report["native_spellings"]["fontlab.Node.raise"] == "fontlab.Node.raise_"
    enforce(report)


def test_reconcile_when_identity_lacks_documentation_then_reported():
    symbols = _symbols()
    del symbols["fontlab.Node.raise_"]
    del symbols["fontlab.Node._p"]
    report, unexplained = _unexplained(symbols=symbols)
    assert unexplained == {
        ("missing", "fontlab.Node.raise"),
        ("missing", "fontlab.Node._p"),
    }
    with pytest.raises(ValueError, match="2 unexplained"):
        enforce(report)


def test_reconcile_when_capture_or_merge_errors_then_reported():
    manifest = copy.deepcopy(MANIFEST)
    manifest["scopes"]["fontlab"]["errors"] = [{"name": "get_value", "error": "RuntimeError"}]
    manifest["scopes"]["fontlab"]["classes"]["Node"]["errors"] = [{"name": "raise", "error": "TypeError"}]
    manifest["merge_unmatched"] = ["fontlab.Gone"]
    _, unexplained = _unexplained(manifest)
    assert unexplained == {
        ("capture-error", "fontlab.get_value"),
        ("capture-error", "fontlab.Node.raise"),
        ("merge-unmatched", "fontlab.Gone"),
    }


def test_reconcile_when_native_symbol_was_never_captured_then_reported():
    symbols = _symbols()
    symbols["fontlab.Node.invented"] = {"id": "fontlab.Node.invented", "kind": "function", "occurrences": 1}
    _, unexplained = _unexplained(symbols=symbols)
    assert unexplained == {("not-captured", "fontlab.Node.invented")}


def test_reconcile_when_manifest_belongs_to_other_capture_then_reported():
    report = reconcile(MANIFEST, _symbols(), {}, provenance_capture_sha256="b" * 64)
    assert ("capture-mismatch", "a" * 64) in {
        (row["problem"], row["id"]) for row in report["unexplained"]
    }


def test_reconcile_when_alias_target_missing_or_redeclared_then_reported():
    symbols = _symbols()
    symbols["fontlab.get_value"]["occurrences"] = 2
    _, unexplained = _unexplained(symbols=symbols, aliases={"fly.gone": "fontlab.gone"})
    assert unexplained == {
        ("alias-target-missing", "fly.gone"),
        ("multiple-declarations", "fontlab.get_value"),
    }


def test_inventory_when_native_member_is_private_then_it_is_kept(tmp_path):
    native = tmp_path / "fontlab_echopy"
    native.mkdir()
    (native / "fontlab.pyi").write_text(
        "class Node:\n    def _p(self) -> None: ...\n    _q: int\n"
    )
    ecosystem = tmp_path / "pkg"
    ecosystem.mkdir()
    (ecosystem / "api.py").write_text("class Tool:\n    def _helper(self): ...\n")
    symbols = inventory_sources([(tmp_path, "fontlab_echopy"), (tmp_path, "pkg")])["symbols"]
    assert {"fontlab.Node._p", "fontlab.Node._q"} <= set(symbols), (
        "captured native members were dropped"
    )
    assert "pkg.api.Tool._helper" not in symbols, "ecosystem private policy changed"
