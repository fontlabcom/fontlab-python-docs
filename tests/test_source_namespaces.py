# this_file: tests/test_source_namespaces.py
"""Missing __init__ files must not delete real source from the reference."""

import griffe

from scripts.griffe_sources import SourceNamespaceExtension


def test_source_when_namespace_inside_package_then_static_consumer_retains_module(
    tmp_path,
):
    root = tmp_path / "pkg"
    folder = root / "namespace"
    folder.mkdir(parents=True)
    (root / "__init__.py").write_text('"""Package."""\n')
    (folder / "actual.py").write_text(
        'raise RuntimeError("never execute")\ndef value() -> int:\n    """An actual source function."""\n    return 42\n'
    )
    loader = griffe.GriffeLoader(
        search_paths=[tmp_path],
        allow_inspection=False,
        extensions=griffe.load_extensions(SourceNamespaceExtension),
    )
    package = loader.load("pkg")
    value = package.get_member("namespace.actual.value")
    assert str(value.returns) == "int"
    assert value.docstring.value == "An actual source function."


def test_source_when_tuple_assignment_declares_names_then_griffe_has_attributes(tmp_path):
    """The inventory indexes `A, B = 0, 1`; mkdocstrings must be able to render them."""
    root = tmp_path / "pkg"
    root.mkdir()
    (root / "__init__.py").write_text(
        "NSMiter, NSRound, NSBevel = 0, 1, 2\n"
        "class Style:\n    LEFT, RIGHT = 'l', 'r'\n"
    )
    loader = griffe.GriffeLoader(
        search_paths=[tmp_path],
        allow_inspection=False,
        extensions=griffe.load_extensions("scripts/griffe_sources.py"),
    )
    package = loader.load("pkg")
    assert package["NSBevel"].is_attribute and str(package["NSBevel"].value) == "2"
    assert str(package["Style.RIGHT"].value) == "'r'"
