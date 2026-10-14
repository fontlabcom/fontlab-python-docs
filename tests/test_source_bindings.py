# this_file: tests/test_source_bindings.py
"""Resolve inheritance from declaration-time bindings without executing source."""

import subprocess
import sys

import pytest
import yaml

from scripts.api_inventory import inventory_sources, plan_pages
from scripts.reference_pages import relative_link, render_page

LOCAL = "class Base:\n    def local(self): pass\n"
IMPORTED = "from .base import Base\n"
CHILD = "class Child(Base): pass\n"


@pytest.mark.parametrize(
    ("source", "child", "target", "member"),
    [
        (IMPORTED + LOCAL + CHILD, "Child", "pkg.child.Base", "local"),
        (LOCAL + IMPORTED + CHILD, "Child", "pkg.base.Base", "imported"),
        (LOCAL + CHILD + IMPORTED, "Child", "pkg.child.Base", "local"),
        (CHILD + LOCAL, "Child", None, None),
        (IMPORTED + "Base = factory()\n" + CHILD, "Child", None, None),
        (IMPORTED + "del Base\n" + CHILD, "Child", None, None),
        (
            IMPORTED
            + "class Outer:\n    class Base:\n        def local(self): pass\n    class Child(Base): pass\n",
            "Outer.Child",
            "pkg.child.Outer.Base",
            "local",
        ),
        (
            "class Outer:\n    from .base import Base\n    class Child(Base): pass\n",
            "Outer.Child",
            "pkg.base.Base",
            "imported",
        ),
        (
            LOCAL + "Alias = Base\nclass Child(Alias): pass\n",
            "Child",
            "pkg.child.Base",
            "local",
        ),
        (
            "import pkg.base as origin\nclass Child(origin.Base): pass\n",
            "Child",
            "pkg.base.Base",
            "imported",
        ),
        (
            "import pkg.base\nclass Child(pkg.base.Base): pass\n",
            "Child",
            "pkg.base.Base",
            "imported",
        ),
        (IMPORTED + "if unknown:\n    Base = factory()\n" + CHILD, "Child", None, None),
        (IMPORTED + "exec(code)\n" + CHILD, "Child", None, None),
        (CHILD + IMPORTED, "Child", None, None),
        (IMPORTED + "def Base(): pass\n" + CHILD, "Child", None, None),
        (IMPORTED + "Base += replacement\n" + CHILD, "Child", None, None),
        (IMPORTED + "Base, other = values\n" + CHILD, "Child", None, None),
        (IMPORTED + "for Base in values:\n    pass\n" + CHILD, "Child", None, None),
        (IMPORTED + "with context as Base:\n    pass\n" + CHILD, "Child", None, None),
        (
            IMPORTED + "try:\n    pass\nexcept Exception as Base:\n    pass\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (
            IMPORTED + "match value:\n    case Base:\n        pass\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (IMPORTED + "from unknown import *\n" + CHILD, "Child", None, None),
        (IMPORTED + "globals()['Base'] = factory()\n" + CHILD, "Child", None, None),
        (IMPORTED + "Base: type\n" + CHILD, "Child", "pkg.base.Base", "imported"),
        (
            IMPORTED
            + "class Outer:\n    Base = factory()\n    class Child(Base): pass\n",
            "Outer.Child",
            None,
            None,
        ),
        (
            IMPORTED
            + "class Outer:\n    class Base: pass\n    del Base\n    class Child(Base): pass\n",
            "Outer.Child",
            "pkg.base.Base",
            "imported",
        ),
        (
            IMPORTED
            + "class Outer:\n    class Base: pass\n    class Inner:\n        class Child(Base): pass\n",
            "Outer.Inner.Child",
            "pkg.base.Base",
            "imported",
        ),
        (
            LOCAL
            + "@decorate\nclass Wrapped(Base): pass\nclass Child(Wrapped): pass\n",
            "Child",
            None,
            None,
        ),
        (
            LOCAL + "class Base:\n    def replacement(self): pass\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (
            IMPORTED + "class Earlier((Base := factory())): pass\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (
            IMPORTED + "def f(arg=(Base := factory())): pass\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (
            IMPORTED + "class Outer:\n    global Base\n    Base = factory()\n" + CHILD,
            "Child",
            None,
            None,
        ),
        (IMPORTED + "class Child[Base](Base): pass\n", "Child", None, None),
        (
            "class Outer:\n    class Base: pass\n    Base = factory()\nclass Child(Outer.Base): pass\n",
            "Child",
            None,
            None,
        ),
    ],
    ids=[
        "import-local",
        "local-import",
        "late-import",
        "forward-local",
        "unknown-assignment",
        "deleted",
        "nested-local",
        "class-import",
        "known-alias",
        "dotted-import",
        "dotted-package",
        "conditional",
        "dynamic",
        "forward-import",
        "function-rebind",
        "augmented",
        "destructured",
        "loop",
        "with",
        "except",
        "match",
        "star-import",
        "namespace-write",
        "annotation-only",
        "nested-unknown",
        "nested-delete",
        "outer-class-not-lexical",
        "decorated",
        "duplicate-class",
        "base-walrus",
        "function-default-walrus",
        "global-write",
        "generic-shadow",
        "dotted-class-rebind",
    ],
)
def test_base_when_bindings_change_then_uses_declaration_environment(
    tmp_path, source, child, target, member
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text(
        "from .child import " + child.split(".")[0] + " as Public\n"
    )
    (pkg / "base.py").write_text(
        "raise RuntimeError('never import source')\nclass Base:\n    def imported(self): pass\n"
    )
    (pkg / "child.py").write_text(
        "raise RuntimeError('never import source')\n" + source
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    identifier = "pkg.child." + child
    row = plan["symbols"][identifier]
    assert row["bases"][0]["target"] == target, (
        "Base must come from its declaration-time binding"
    )
    page = "reference/" + identifier.replace(".", "/") + ".md"
    text = render_page(page, plan)
    public = "pkg.Public" + ("." + child.partition(".")[2] if "." in child else "")
    if target:
        inherited = target + "." + member
        assert row["inheritance_status"] == "source-proven"
        assert row["inherited_members"] == {member: inherited}
        assert plan["aliases"][identifier + "." + member] == inherited
        assert plan["aliases"][public + "." + member] == inherited
        assert relative_link(page, plan["symbols"][target]["url"]) in text
        assert relative_link(page, plan["symbols"][inherited]["body_url"]) in text
    else:
        assert row["inheritance_status"].startswith("Unresolved source base:")
        assert not row["inherited_members"]
        assert identifier + ".imported" not in plan["aliases"]
        assert public + ".imported" not in plan["aliases"]
        assert "not resolved from selected source" in text
        assert "Inherited member index" not in text


@pytest.mark.parametrize(
    "imported",
    [
        "from .base import Base\nclass Child(Base): pass\n",
        "import pkg.base as origin\nclass Child(origin.Base): pass\n",
    ],
)
def test_import_when_source_binding_overwritten_then_does_not_use_stale_class(
    tmp_path, imported
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("raise RuntimeError('never import')\n")
    (pkg / "base.py").write_text(
        "class Base:\n    def stale(self): pass\nBase = factory()\n"
    )
    (pkg / "child.py").write_text(imported)
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    row = plan["symbols"]["pkg.child.Child"]
    assert row["bases"][0]["target"] is None
    assert not row["inherited_members"]
    assert "pkg.child.Child.stale" not in plan["aliases"]


@pytest.mark.parametrize(
    "source", ["object = factory()\n", "object = factory()\ndel object\n"]
)
def test_object_when_shadowed_or_deleted_then_distinguishes_builtin(tmp_path, source):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text(source + "class Child(object): pass\n")
    row = inventory_sources([(tmp_path, "pkg")])["symbols"]["pkg.Child"]
    assert row["bases"] == [{"expression": "object", "target": None}]
    expected = (
        "source-proven"
        if "del object" in source
        else "Unresolved source base: pkg.Child"
    )
    assert row["inheritance_status"] == expected


@pytest.mark.parametrize(
    ("base", "expected"),
    [
        ("class Base:\n    def value(self): pass\n", "pkg.base.Base"),
        (
            "__all__ = ['Base']\nclass Base:\n    def value(self): pass\n",
            "pkg.base.Base",
        ),
        ("from .origin import Base\n", "pkg.origin.Base"),
        (
            "registry = {}\ndef keep(cls):\n    if hasattr(cls, '__name__'):\n        registry[cls.__name__] = cls\n    return cls\n@keep\nclass Base:\n    def value(self): pass\n",
            "pkg.base.Base",
        ),
        (
            "def keep(cls):\n    cls.__bases__ = replacement\n    return cls\n@keep\nclass Base: pass\n",
            None,
        ),
        (
            "def keep(cls):\n    mutate(cls)\n    return cls\n@keep\nclass Base: pass\n",
            None,
        ),
        (
            "def keep(cls):\n    setattr(cls, '__bases__', replacement)\n    return cls\n@keep\nclass Base: pass\n",
            None,
        ),
        ("class Base: pass\n__all__ = dynamic()\n", None),
        (
            "def keep(cls):\n    alias = cls\n    alias.__bases__ = replacement\n    return cls\n@keep\nclass Base: pass\n",
            None,
        ),
        (
            "def keep(cls):\n    cls.__dict__['value'] = replacement\n    return cls\n@keep\nclass Base: pass\n",
            None,
        ),
        ("class Base: pass\nif condition:\n    Base = factory()\n", None),
        ("__all__ = ['Other']\nclass Base: pass\nclass Other: pass\n", None),
    ],
    ids=[
        "public-declarations",
        "literal-all",
        "reexport",
        "identity-decorator",
        "decorator-bases-mutation",
        "decorator-unknown-call",
        "decorator-setattr",
        "dynamic-all",
        "decorator-alias-mutation",
        "decorator-dict-mutation",
        "conditional-export",
        "excluded",
    ],
)
def test_star_import_when_exports_known_then_preserves_proven_bindings(
    tmp_path, base, expected
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text(
        "raise RuntimeError('never import')\nfrom .base import *\nclass Child(Base): pass\n"
    )
    (pkg / "base.py").write_text("raise RuntimeError('never import')\n" + base)
    (pkg / "origin.py").write_text("class Base:\n    def value(self): pass\n")
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    row = plan["symbols"]["pkg.Child"]
    assert row["bases"][0]["target"] == expected
    if expected:
        assert row["inherited_members"] == {"value": expected + ".value"}
        assert plan["aliases"]["pkg.Child.value"] == expected + ".value"
    else:
        assert row["inheritance_status"].startswith("Unresolved source base:")
        assert not row["inherited_members"]


def test_render_when_local_class_replaces_import_then_links_local_source(tmp_path):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("from .child import Child as Public\n")
    (pkg / "base.py").write_text("class Base:\n    def imported(self): pass\n")
    (pkg / "child.py").write_text(
        "raise RuntimeError('never execute')\n" + IMPORTED + LOCAL + CHILD
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    docs = tmp_path / "content"
    for path in plan["pages"]:
        target = docs / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_page(path, plan))
    config = tmp_path / "mkdocs.yml"
    site = tmp_path / "site"
    config.write_text(
        yaml.safe_dump(
            {
                "site_name": "Source binding fixture",
                "docs_dir": str(docs),
                "site_dir": str(site),
                "use_directory_urls": False,
                "plugins": [
                    {
                        "mkdocstrings": {
                            "handlers": {
                                "python": {
                                    "paths": [str(tmp_path)],
                                    "options": {
                                        "allow_inspection": False,
                                        "show_source": False,
                                    },
                                }
                            }
                        }
                    }
                ],
            }
        )
    )
    result = subprocess.run(
        [sys.executable, "-m", "mkdocs", "build", "--strict", "-f", str(config)],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    child = (site / "reference/pkg/child/Child.html").read_text()
    assert 'href="Base.html#pkg.child.Base"' in child
    assert 'href="Base/members-001.html#pkg.child.Base.local"' in child
    assert (
        'id="pkg.child.Base.local"'
        in (site / "reference/pkg/child/Base/members-001.html").read_text()
    )
    assert "pkg.base.Base.imported" not in child
