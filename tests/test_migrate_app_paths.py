# this_file: tests/test_migrate_app_paths.py
"""Migration boundaries and repeatability, independent of native FontLab."""

import importlib.util
from pathlib import Path

import pytest


def test_rewrite_when_paths_overlap_then_preserve_boundaries_and_bindings():
    path = Path(__file__).resolve().parents[1] / "tools/migrate_app_paths.py"
    spec = importlib.util.spec_from_file_location("migrate_app_paths", path)
    migration = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migration)
    mapping = migration.load_mapping()
    source = '''from fly.ap import scripting as api
from fontlabapp import masters, draft_signals
from fontlabapp.masters.inspect import model
import fly.ap.glyph_catalog as catalog
monkeypatch.setattr("fontlabapp.scripting.capture", callback)
mock.patch('fly.ap.scripting.capture')
importlib.import_module("fontlab_remopy.control")
fly.fp.feature_blocks.read_feature_blocks(font)
fontlab_fontport.ui.fontinfo
fontlabapp.scripting_extra other.fontlabapp.scripting fly.ap.scripting_extra
fontlabapp.masters.inspect.model.capture
{"api_module": "glyph_tree", "unrelated": "glyph_tree"}
assert row["api_module"] == "glyph_tree"
'''
    expected = '''import fly.ap.core.scripting as api
import fontlabapp.masters.inspect.model as masters
import fontlabapp.core.signals.scope as draft_signals
from fontlabapp.masters.inspect import model
import fly.ap.glyphs.catalog.model as catalog
monkeypatch.setattr("fontlabapp.core.scripting.capture", callback)
mock.patch('fly.ap.core.scripting.capture')
importlib.import_module("fontlab_remopy.client")
fly.ap.fontui.feature_blocks.read_feature_blocks(font)
fontlabapp.fontui.fontinfo
fontlabapp.scripting_extra other.fontlabapp.scripting fly.ap.scripting_extra
fontlabapp.masters.inspect.model.capture
{"api_module": "glyphs.tree.model", "unrelated": "glyph_tree"}
assert row["api_module"] == "glyphs.tree.model"
'''
    rewritten = migration.rewrite(source, mapping)
    assert rewritten == expected, "Change only complete module paths; retain imported local names"
    assert migration.rewrite(rewritten, mapping) == rewritten, "Canonical paths must be stable"


def test_migrate_when_archive_present_then_leave_it_untouched(tmp_path):
    path = Path(__file__).resolve().parents[1] / "tools/migrate_app_paths.py"
    spec = importlib.util.spec_from_file_location("migrate_app_paths", path)
    migration = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migration)
    for name in ("scripts/current.py", "scripts/_reference/archived.py"):
        target = tmp_path / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("import fly.ap.scripting\n")
    assert migration.migrate(tmp_path, migration.load_mapping()) == ["scripts/current.py"]
    assert (tmp_path / "scripts/_reference/archived.py").read_text() == "import fly.ap.scripting\n"


def test_reference_aliases_when_public_then_target_canonical_definitions():
    from scripts.build_reference import _aliases

    expected = {
        "fontlabapp.FontLab": "fontlabapp.core.controls.FontLab",
        "fontlabapp.Application": "fontlabapp.core.application.context.Application",
    }
    plan = {"aliases": {}, "symbols": {target: {"kind": "class"} for target in expected.values()}}
    assert _aliases(plan) == expected, "Public aliases must reach defining modules"


def test_interaction_plan_when_remopy_then_members_and_routes_are_canonical():
    from scripts.interaction_check import PLAN

    type_link = PLAN["type_link"]
    assert type_link["page"] == "reference/fontlab_remopy/client/FontLab/members-001.html"
    assert type_link["member"] == "fontlab_remopy.client.FontLab.run"
    assert type_link["target"] == (
        "reference/fontlab_remopy/results/ExecutionResult.html"
        "#fontlab_remopy.results.ExecutionResult"
    )
    for case in ("search", "search_slow_shard"):
        assert PLAN[case]["target"] == (
            "reference/fontlab_remopy/results/members-001.html"
            "#fontlab_remopy.results.decode_execution"
        ), "Search routes must agree with their canonical member identities"


def test_rewrite_when_reference_routes_then_use_canonical_module_paths():
    path = Path(__file__).resolve().parents[1] / "tools/migrate_app_paths.py"
    spec = importlib.util.spec_from_file_location("migrate_app_paths", path)
    migration = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(migration)
    source = (
        "reference/fontlab_remopy/control/FontLab.html fontlabapp/component_graph.md "
        "fontlabapp/components/graph.md fontlabapp/masters/inspect.md"
    )
    expected = (
        "reference/fontlab_remopy/client/FontLab.html fontlabapp/components/graph/model.md "
        "fontlabapp/components/graph.md fontlabapp/masters/inspect.md"
    )
    rewritten = migration.rewrite(source, migration.load_mapping())
    assert rewritten == expected, "Reference routes must follow the same alias oracle"
    assert migration.rewrite(rewritten, migration.load_mapping()) == rewritten


@pytest.fixture
def migration(tmp_path, monkeypatch):
    path = Path(__file__).resolve().parents[1] / "tools/migrate_app_paths.py"
    spec = importlib.util.spec_from_file_location("migrate_app_paths", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    monkeypatch.setattr(module, "ROOT", tmp_path / "docs")
    return module


def test_load_mapping_when_explicit_root_then_precedes_sibling_without_native_import(
    tmp_path, monkeypatch, migration
):
    package = tmp_path / "frozen inputs/fontlabapp"
    package.mkdir(parents=True)
    (package / "__init__.py").write_text("raise AssertionError('native package imported')\n")
    (package / "_legacy.py").write_text(
        "ALIASES = {'fontlabapp.old': 'fontlabapp.canonical'}\n"
    )
    sibling = tmp_path / "fontlab-fontlabapp/src/fontlabapp"
    sibling.mkdir(parents=True)
    (sibling / "_legacy.py").write_text(
        "ALIASES = {'fontlabapp.old': 'fontlabapp.wrong_sibling'}\n"
    )
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", "frozen inputs/../frozen inputs")
    mapping = migration.load_mapping()
    assert mapping["fontlabapp.old"] == "fontlabapp.canonical"
    assert mapping["fly.ap.old"] == "fly.ap.canonical"
    assert mapping["fontlabapp/old"] == "fontlabapp/canonical"


@pytest.mark.parametrize("setting", [None, ""])
def test_load_mapping_when_no_explicit_root_then_preserves_sibling(
    tmp_path, monkeypatch, migration, setting
):
    sibling = tmp_path / "fontlab-fontlabapp/src/fontlabapp"
    sibling.mkdir(parents=True)
    (sibling / "__init__.py").write_text("raise AssertionError('native package imported')\n")
    (sibling / "_legacy.py").write_text(
        "ALIASES = {'fontlabapp.old': 'fontlabapp.sibling'}\n"
    )
    monkeypatch.delenv("FONTLAB_API_SOURCE_ROOT", raising=False)
    if setting is not None:
        monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", setting)
    assert migration.load_mapping()["fontlabapp.old"] == "fontlabapp.sibling"


def test_load_mapping_when_explicit_oracle_missing_then_fails_without_sibling_fallback(
    tmp_path, monkeypatch, migration
):
    sibling = tmp_path / "fontlab-fontlabapp/src/fontlabapp"
    sibling.mkdir(parents=True)
    (sibling / "_legacy.py").write_text("ALIASES = {}\n")
    root = tmp_path / "missing inputs"
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", str(root))
    with pytest.raises(FileNotFoundError) as failure:
        migration.load_mapping()
    assert Path(failure.value.filename) == root / "fontlabapp/_legacy.py"

