# this_file: tests/test_reference_pages.py
"""Reference output must retain each identity and render each unique body."""

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
