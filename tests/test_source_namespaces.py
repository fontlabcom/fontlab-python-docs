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


def test_docstring_when_it_names_a_raw_text_element_then_it_is_escaped(tmp_path):
    """A literal `<title>` swallowed the rest of FontLabPluginHost's page and search rows."""
    root = tmp_path / "pkg"
    root.mkdir()
    (root / "__init__.py").write_text(
        'def export():\n    """File > "Export with <title>..." uses `<title>` and <b>bold</b>.\n\n'
        '    ```html\n    <script>x()</script>\n    ```\n    """\n'
    )
    loader = griffe.GriffeLoader(
        search_paths=[tmp_path],
        allow_inspection=False,
        extensions=griffe.load_extensions("scripts/griffe_sources.py"),
    )
    doc = loader.load("pkg")["export"].docstring.value
    assert 'Export with &lt;title>..."' in doc
    assert "`<title>`" in doc and "<b>bold</b>" in doc, "code spans and inline HTML stay"
    assert "<script>x()</script>" in doc, "fenced code stays verbatim"


def test_namespace_root_when_multiple_search_paths_then_do_not_scan_unknown_roots(tmp_path):
    """A namespace root has no single owned initializer to augment."""
    package=griffe.Module("pkg",filepath=[tmp_path])
    SourceNamespaceExtension().on_package(pkg=package,loader=None)
    assert package.members=={}


def test_source_namespace_when_class_shadows_folder_then_preserve_class(tmp_path):
    root=tmp_path/"pkg";(root/"Shadow").mkdir(parents=True)
    (root/"__init__.py").write_text('class Shadow: """The public class wins."""\n')
    (root/"Shadow/Hidden.py").write_text('raise RuntimeError("do not execute")\ndef value(): return 1\n')
    loader=griffe.GriffeLoader(search_paths=[tmp_path],allow_inspection=False)
    package=griffe.Module("pkg",filepath=root/"__init__.py")
    package.set_member("Shadow",griffe.Class("Shadow",parent=package,docstring=griffe.Docstring("The public class wins.")))
    SourceNamespaceExtension().on_package(pkg=package,loader=loader)
    assert package["Shadow"].is_class and package["Shadow"].docstring.value=="The public class wins."
    assert "Hidden" not in package["Shadow"].members
