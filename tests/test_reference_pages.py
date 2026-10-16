# this_file: tests/test_reference_pages.py
"""Reference output must retain each identity and render each unique body."""

import re
import subprocess
import sys
from html import unescape

import yaml

from scripts.api_inventory import inventory_sources, plan_pages
from scripts.reference_pages import render_page


def test_class_page_when_member_body_shared_then_each_class_has_anchor_and_link(
    tmp_path,
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "api.pyi").write_text(
        "class A:\n    def value(self) -> int: ...\nclass B:\n    def value(self) -> int: ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    text = render_page("reference/pkg/api/B.md", plan)
    assert 'id="pkg.api.B.value"' in text, (
        "shared body must not delete the class occurrence"
    )
    assert "members-001.md#pkg.api.A.value" in text, (
        "shared declaration link is missing"
    )
    assert "::: pkg.api.B" in text


def test_member_page_when_generated_then_actual_source_consumer_directives_are_used(
    tmp_path,
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "api.pyi").write_text(
        "class A:\n    def first(self): ...\n    def second(self): ...\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]), chunk_size=1)
    text = render_page("reference/pkg/api/A/members-002.md", plan)
    assert "::: pkg.api.A.second" in text
    assert "::: pkg.api.A.first" not in text
    assert "A.md" in text, "member pages must retain navigation back to the class"


def test_module_page_when_generated_then_classes_and_child_modules_are_discoverable(
    tmp_path,
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text('"""Package."""\n')
    (pkg / "api.pyi").write_text("class A: ...\n")
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert "api.md" in render_page("reference/pkg.md", plan)
    assert "A.md" in render_page("reference/pkg/api.md", plan)


def test_class_page_when_exported_private_class_then_public_title_and_stable_ids(
    tmp_path,
):
    pkg = tmp_path / "pkg"
    pkg.mkdir()
    (pkg / "__init__.py").write_text("from ._impl import Handle as Public\n")
    (pkg / "_impl.py").write_text("class Handle:\n    def close(self): ...\n")
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    text = render_page("reference/pkg/_impl/Handle.md", plan)
    assert "# pkg.Public\n" in text
    assert 'heading: "pkg.Public"' in text, (
        "source consumer heading must use public name"
    )
    assert "::: pkg._impl.Handle" in text, "canonical source directive must stay stable"
    assert 'id="pkg._impl.Handle.close"' in text
    assert plan["symbols"]["pkg._impl.Handle"]["url"].endswith(
        "/_impl/Handle.html#pkg._impl.Handle"
    )
    members = render_page("reference/pkg/_impl/Handle/members-001.md", plan)
    assert "# pkg.Public · declarations 001" in members
    assert "::: pkg._impl.Handle.close" in members


def test_render_when_public_title_and_property_then_static_handler_keeps_anchors(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "__init__.py").write_text(
        "from ._impl import Handle as Public, make as create, Child\n"
    )
    (package / "_impl.py").write_text(
        "raise RuntimeError('never execute')\nfrom types import MappingProxyType\n"
        "def make(text: str, count: int = 3, *, enabled: bool = True) -> tuple[str, int]:\n"
        "    '''Exported function documentation.''' \n    return text, count\n"
        "class Handle:\n"
        "    def close(self, count: int = 3, /, *, timeout: float | None = None) -> None:\n"
        "        '''Typed method documentation.''' \n        pass\n"
        "    @property\n    def namespace(self) -> MappingProxyType[str, object]:\n"
        "        '''Public property documentation.''' \n        return {}\n"
        "    @namespace.setter\n    def namespace(self, value: MappingProxyType[str, object]): pass\n"
        "class Child(Handle):\n    class Nested: pass\n"
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    docs = tmp_path / "content"
    for path in plan["pages"]:
        target = docs / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render_page(path, plan))
    config = tmp_path / "mkdocs.yml"
    config.write_text(
        yaml.safe_dump(
            {
                "site_name": "Source fixture",
                "docs_dir": str(docs),
                "site_dir": str(tmp_path / ".build/site"),
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
                                        "show_signature_annotations": True,
                                        "show_attribute_values": False,
                                        "show_root_full_path": False,
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
    root = tmp_path / ".build/site/reference/pkg/_impl/Handle"
    class_html = root.with_suffix(".html").read_text()
    member_html = (root / "members-001.html").read_text()
    child_html = (root.parent / "Child.html").read_text()
    assert "Handle.html#pkg._impl.Handle" in child_html
    assert "members-001.html#pkg._impl.Handle.close" in child_html
    assert "Child/Nested.html" in child_html
    assert "pkg.Public" in class_html
    assert 'id="pkg._impl.Handle"' in class_html
    assert 'id="pkg._impl.Handle.namespace"' in class_html
    assert 'id="pkg._impl.Handle.namespace"' in member_html
    assert "pkg.Public.namespace" in member_html
    assert "Public property documentation." in member_html
    assert "pkg.Public.close" in member_html
    assert 'id="pkg._impl.Handle.close"' in member_html
    function_html = (root.parent / "members-001.html").read_text()
    assert "pkg.create" in function_html
    assert 'id="pkg._impl.make"' in function_html
    codes = [
        " ".join(unescape(re.sub(r"<[^>]+>", "", block)).split())
        for html in (member_html, function_html)
        for block in re.findall(r"<pre\b[^>]*>(.*?)</pre>", html, re.DOTALL)
    ]
    assert (
        "close(count: int = 3, /, *, timeout: float | None = None) -> None" in codes
    ), "public headings must not erase typed method arguments/defaults/return"
    assert (
        "make(text: str, count: int = 3, *, enabled: bool = True) -> tuple[str, int]"
        in codes
    ), "exported functions must retain complete source-derived signatures"
    assert "namespace: MappingProxyType[str, object]" in codes, (
        "public property headings must retain the getter's declared annotation"
    )


def test_package_page_when_a_guide_exists_then_it_links_overview_install_and_quick_start(
    tmp_path,
):
    """X4r (issue 106): API landing pages lead to the package's narrative guide."""
    pkg = tmp_path / "fly"
    pkg.mkdir()
    (pkg / "__init__.py").write_text('"""Aliases."""\nfl = None\n')
    (pkg / "sub.py").write_text('"""Child."""\n')
    plan = plan_pages(inventory_sources([(tmp_path, "fly")]))
    page = render_page("reference/fly.md", plan)
    assert "[Fly guide](../packages/fly.md)" in page
    assert "packages/" not in render_page("reference/fly/sub.md", plan)
