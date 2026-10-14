# this_file: tests/test_api_inventory.py
"""Coverage must preserve source occurrences and distinguish shared bodies."""

import griffe

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


def test_inventory_when_property_has_accessors_then_griffe_semantics_and_records(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    source = package / "api.py"
    source.write_text('''raise RuntimeError("never import")
class Handle:
    @property
    def namespace(self) -> dict:
        """The getter documentation."""
        return {}
    @namespace.setter
    def namespace(self, value: dict):
        """The setter documentation."""
        pass
    @namespace.deleter
    def namespace(self):
        """The deleter documentation."""
        pass
''')
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    row = plan["symbols"]["pkg.api.Handle.namespace"]
    model = griffe.GriffeLoader(search_paths=[tmp_path], allow_inspection=False).load(
        "pkg.api"
    )
    prop = model.get_member("Handle.namespace")
    assert row["kind"] == prop.kind.value == "attribute"
    assert set(row["labels"]) == prop.labels == {"property", "writable", "deletable"}
    assert row["docstring"] == prop.docstring.value == "The getter documentation."
    assert row["occurrences"] == 3, (
        "getter/setter/deleter declarations must all survive"
    )
    records = row["declarations"]
    assert [record["accessor"] for record in records] == ["getter", "setter", "deleter"]
    assert len({record["declaration_sha256"] for record in records}) == 3
    assert [record["line"] for record in records] == [4, 8, 12]
    assert all(record["source"] == "pkg/api.py" for record in records)
    assert row["canonical_id"] == "pkg.api.Handle.namespace"
    assert row["body_target"] == "pkg.api.Handle.namespace"
    assert plan == plan_pages(inventory_sources([(tmp_path, "pkg")]))


def test_inventory_when_cached_property_import_alias_then_matches_griffe(tmp_path):
    package = tmp_path / "pkg"
    package.mkdir()
    (package / "api.py").write_text(
        "from functools import cached_property as cached\n"
        "class Handle:\n    @cached\n    def reports(self) -> list: return []\n"
    )
    row = inventory_sources([(tmp_path, "pkg")])["symbols"]["pkg.api.Handle.reports"]
    model = griffe.GriffeLoader(search_paths=[tmp_path], allow_inspection=False).load(
        "pkg.api"
    )
    prop = model.get_member("Handle.reports")
    assert row["kind"] == prop.kind.value == "attribute"
    assert set(row["labels"]) == prop.labels == {"property", "cached"}


def test_inventory_when_shared_properties_then_each_occurrence_keeps_body_identity(
    tmp_path,
):
    package = tmp_path / "pkg"
    package.mkdir()
    getter = "    @property\n    def value(self) -> int: return 1\n"
    (package / "api.py").write_text(
        "class First:\n" + getter + "class Second:\n" + getter
    )
    plan = plan_pages(inventory_sources([(tmp_path, "pkg")]))
    first = plan["symbols"]["pkg.api.First.value"]
    second = plan["symbols"]["pkg.api.Second.value"]
    assert first["body_target"] == second["body_target"] == "pkg.api.First.value"
    assert first["url"] != second["url"]
    assert first["declarations"][0]["line"] != second["declarations"][0]["line"]
