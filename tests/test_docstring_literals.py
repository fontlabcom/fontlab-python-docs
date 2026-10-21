# this_file: tests/test_docstring_literals.py
"""Display array indexing as code without changing source or suppressing links."""

from types import SimpleNamespace as NS

import pytest
from griffe import load, load_extensions
from scripts.docstring_literals import LiteralIndexes


def test_reviewed_math_when_static_loaded_then_literal_and_never_imported(tmp_path):
    folder = tmp_path / "typerig/core/algo"
    folder.mkdir(parents=True)
    for parent in (folder, folder.parent, folder.parent.parent):
        (parent / "__init__.py").write_text("")
    source = folder / "outline_cleanup.py"
    source.write_text(
        'raise RuntimeError("never execute source")\ndef clean(masters):\n    """masters[m][c] describes a contour. [Valid][other.Target] stays a link."""\n'
    )
    before = source.read_bytes()
    mod = load(
        "typerig.core.algo.outline_cleanup",
        search_paths=[tmp_path],
        extensions=load_extensions(LiteralIndexes()),
        allow_inspection=False,
    )
    assert (
        mod["clean"].docstring.value
        == "`masters[m][c]` describes a contour. [Valid][other.Target] stays a link."
    )
    assert source.read_bytes() == before and [
        p.name for p in mod["clean"].parameters
    ] == ["masters"]


def test_extension_when_unrelated_or_missing_docstring_then_unchanged():
    ext = LiteralIndexes()
    doc = NS(value="plain[n][i]")
    ext.on_function_instance(func=NS(path="other.func", docstring=doc))
    ext.on_function_instance(
        func=NS(path="typerig.core.algo.outline_cleanup.clean", docstring=None)
    )
    assert doc.value == "plain[n][i]"


def test_extension_when_already_literal_then_idempotent_and_stale_rule_fails():
    ext = LiteralIndexes()
    f = NS(
        path="typerig.core.algo.outline_cleanup.clean",
        docstring=NS(value="`masters[m][c]`"),
    )
    ext.on_function_instance(func=f)
    assert f.docstring.value == "`masters[m][c]`"
    f.docstring.value = "changed prose"
    with pytest.raises(ValueError, match="reviewed"):
        ext.on_function_instance(func=f)


def test_namespace_collection_when_extra_modules_visited_then_keep_extensions(tmp_path):
    from scripts.griffe_sources import SourceNamespaceExtension

    package = tmp_path / "typerig"
    package.mkdir()
    (package / "__init__.py").write_text("")
    namespace = package / "core/algo"
    namespace.mkdir(parents=True)
    (namespace / "outline_cleanup.py").write_text(
        'raise RuntimeError("never import a producer")\ndef clean(masters):\n    """masters[m][c] describes a contour."""\n'
    )
    mod = load(
        "typerig",
        search_paths=[tmp_path],
        extensions=load_extensions(SourceNamespaceExtension(), LiteralIndexes()),
        allow_inspection=False,
    )
    assert (
        mod["core.algo.outline_cleanup.clean"].docstring.value
        == "`masters[m][c]` describes a contour."
    )
