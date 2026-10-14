# this_file: tests/test_reference_pages.py
"""Reference output must retain each identity and render each unique body."""

import subprocess
import sys

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
    (package / "__init__.py").write_text("from ._impl import Handle as Public\n")
    (package / "_impl.py").write_text(
        "raise RuntimeError('never execute')\nclass Handle:\n"
        "    @property\n    def namespace(self) -> dict:\n"
        "        '''Public property documentation.''' \n        return {}\n"
        "    @namespace.setter\n    def namespace(self, value: dict): pass\n"
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
                                    "options": {"allow_inspection": False},
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
    assert "pkg.Public" in class_html
    assert 'id="pkg._impl.Handle"' in class_html
    assert 'id="pkg._impl.Handle.namespace"' in class_html
    assert 'id="pkg._impl.Handle.namespace"' in member_html
    assert "pkg.Public.namespace" in member_html
    assert "Public property documentation." in member_html
