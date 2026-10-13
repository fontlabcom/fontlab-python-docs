# this_file: tests/test_api_inventory.py
"""Coverage must preserve source occurrences and distinguish shared bodies."""

from scripts.api_inventory import inventory_sources, plan_pages


def test_inventory_when_identical_methods_then_each_identity_is_preserved(tmp_path):
    source = tmp_path / "pkg"
    source.mkdir()
    (source / "api.pyi").write_text('''"""Native API."""
class First:
    def method(self, value: int) -> int:
        """A shared captured declaration."""
        ...
class Second:
    def method(self, value: int) -> int:
        """A shared captured declaration."""
        ...
''')
    inventory = inventory_sources([(tmp_path, "pkg")])
    planned = plan_pages(inventory)
    first = planned["symbols"]["pkg.api.First.method"]
    second = planned["symbols"]["pkg.api.Second.method"]
    assert first["id"] != second["id"], "source identities were collapsed"
    assert first["body_target"] == second["body_target"], (
        "identical content should be rendered once"
    )
    assert first["url"] != second["url"], "each class needs its own member anchor"


def test_inventory_when_documentation_differs_then_bodies_are_distinct(tmp_path):
    source = tmp_path / "pkg"
    source.mkdir()
    (source / "api.pyi").write_text('''class First:
    def method(self):
        """One description."""
        ...
class Second:
    def method(self):
        """A different description."""
        ...
''')
    planned = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    assert (
        planned["symbols"]["pkg.api.First.method"]["body_target"]
        != planned["symbols"]["pkg.api.Second.method"]["body_target"]
    )


def test_inventory_when_stub_and_runtime_coexist_then_stub_is_authority(tmp_path):
    source = tmp_path / "pkg"
    source.mkdir()
    (source / "api.py").write_text("raise RuntimeError('never import')\n")
    (source / "api.pyi").write_text("class Native:\n    value: int\n")
    inventory = inventory_sources([(tmp_path, "pkg")])
    assert "pkg.api.Native.value" in inventory["symbols"]
    assert inventory["modules"]["pkg.api"]["source"] == "pkg/api.pyi"


def test_pages_when_more_than_chunk_size_then_every_member_body_is_planned(tmp_path):
    source = tmp_path / "pkg"
    source.mkdir()
    methods = "".join(
        f"    def method{i}(self):\n        return {i}\n" for i in range(81)
    )
    (source / "api.py").write_text("class Many:\n" + methods)
    planned = plan_pages(inventory_sources([(tmp_path, "pkg")]), chunk_size=40)
    chunks = [page for page in planned["pages"].values() if page["kind"] == "members"]
    assert len(chunks) == 3, "pagination should split the complete body set"
    ids = [identifier for page in chunks for identifier in page["members"]]
    assert len(ids) == 81 and len(set(ids)) == 81, (
        "pagination omitted or duplicated a body"
    )


def test_inventory_when_attribute_has_adjacent_docstring_then_content_is_preserved(
    tmp_path,
):
    source = tmp_path / "pkg"
    source.mkdir()
    (source / "api.pyi").write_text(
        'class Native:\n    value: int\n    """Property description."""\n'
    )
    inventory = inventory_sources([(tmp_path, "pkg")])
    assert (
        inventory["symbols"]["pkg.api.Native.value"]["docstring"]
        == "Property description."
    )
