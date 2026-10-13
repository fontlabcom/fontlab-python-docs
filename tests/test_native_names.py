# this_file: tests/test_native_names.py
"""Current reference identities must match the public live FontLab namespaces."""

from scripts.api_inventory import inventory_sources


def test_native_stub_when_indexed_then_live_namespace_is_primary(tmp_path):
    package = tmp_path / "fontlab_echopy"
    package.mkdir()
    (package / "fontlab.pyi").write_text(
        "class flNode:\n    def angleTo(self) -> float: ...\n"
    )
    inventory = inventory_sources([(tmp_path, "fontlab_echopy")])
    assert "fontlab.flNode.angleTo" in inventory["symbols"]
    assert (
        inventory["symbols"]["fontlab.flNode"]["canonical_id"]
        == "fontlab_echopy.fontlab.flNode"
    )


def test_native_class_when_empty_namespace_also_exists_then_class_facet_is_kept(
    tmp_path,
):
    qt = tmp_path / "fontlab_echopy" / "PythonQt"
    qt.mkdir(parents=True)
    (qt / "BoolResult.pyi").write_text('"""Empty pseudo-namespace."""\n__all__ = []\n')
    (qt / "__init__.pyi").write_text(
        "class BoolResult:\n    def __init__(self, value: bool): ...\n"
    )
    inventory = inventory_sources([(tmp_path, "fontlab_echopy")])
    assert inventory["symbols"]["PythonQt.BoolResult"]["kind"] == "class"
    assert "PythonQt.BoolResult.__init__" in inventory["symbols"]
    assert inventory["symbols"]["PythonQt.BoolResult"]["facets"][0]["kind"] == "module"
