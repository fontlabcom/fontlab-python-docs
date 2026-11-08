# this_file: tests/test_build_lifecycle.py
"""Generation freshness and accepted rendered provenance are separate gates."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

from scripts import build_reference as builder


def _write_export(folder, pages):
    """A fontlab-python-examples docs export: pages plus their manifest."""
    import hashlib

    rows = []
    for path, text in sorted(pages.items()):
        target = folder / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        rows.append({"path": path, "title": text.splitlines()[0][2:],
                     "sha256": hashlib.sha256(text.encode()).hexdigest()})
    manifest = {"format": "fontlab-python-examples.docs-export.v1", "entry": "index.md", "pages": rows}
    (folder / "manifest.json").write_text(json.dumps(manifest))


@pytest.fixture
def project(tmp_path, monkeypatch):
    root = tmp_path / "docs"
    root.mkdir()
    source = tmp_path / "sources"
    (source / "fontlab_echopy").mkdir(parents=True)
    (source / "fontlab_echopy/__init__.py").write_text("class Old: pass\n")
    (source / "fontlab_echopy/fontlab.pyi").write_text("class Native: ...\n")
    (source / "fontlab_echopy/_provenance.json").write_text(
        json.dumps({"capture_identity": {"sha256": "c" * 64}})
    )
    (source / "fontlab_echopy/_identities.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "producer": "fontlab_echopy.tooling.identities",
                "capture_sha256": "c" * 64,
                "scopes": {
                    "fontlab": {
                        "available": True,
                        "kind": "module",
                        "names": ["Native"],
                        "errors": [],
                        "classes": {
                            "Native": {"members": [], "constructors": [], "errors": []}
                        },
                    }
                },
                "native_spellings": {},
                "maintained_extensions": [],
                "merge_unmatched": [],
                "enrichment_gaps": {
                    "qt_document_failures": {},
                    "unmatched_native_classes": [],
                },
            }
        )
    )
    (root / "src_docs/md").mkdir(parents=True)
    (root / "src_docs/md/index.md").write_text("# Current\n")
    (root / "src_docs/md/old.md").write_text("# Old guide\n")
    (root / "scripts").mkdir()
    (root / "scripts/reference_pages.py").write_text("# renderer v1\n")
    (root / "overrides").mkdir()
    (root / "overrides/main.html").write_text("template v1")
    original = Path(builder.__file__).resolve().parents[1]
    shutil.copyfile(original / "src_docs/mkdocs.yml", root / "src_docs/mkdocs.yml")
    export = tmp_path / "examples-export"
    _write_export(export, {"index.md": "# Python examples for FontLab\n\nSee [recipes](recipes/index.md).\n",
                           "recipes/index.md": "# Recipes\n"})
    monkeypatch.setenv("FONTLAB_EXAMPLES_EXPORT", str(export))
    monkeypatch.setattr(builder, "ROOT", root)
    monkeypatch.setattr(builder, "source_roots", lambda: [(source, "fontlab_echopy")])
    # Use actual source-only docname exporter; its code is not a native import.
    monkeypatch.syspath_prepend(str(original.parent / "fontlab-echopy/src"))
    from fontlab_echopy.tooling import docnames

    assert callable(docnames.export_docnames)
    return root, source


def render_fixture(root, source):
    """Build the generated tree with the installed source-only consumer/search."""
    config = {
        "site_name": "Lifecycle fixture",
        "docs_dir": str(root / ".build/content"),
        "site_dir": str(root / ".build/site"),
        "use_directory_urls": False,
        "plugins": [
            "/search",
            {
                "mkdocstrings": {
                    "handlers": {
                        "python": {
                            "paths": [str(root / ".build/native-names"), str(source)],
                            "options": {
                                "allow_inspection": False,
                                "show_source": False,
                            },
                        }
                    }
                }
            },
        ],
    }
    path = root / "fixture.yml"
    path.write_text(yaml.safe_dump(config))
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mkdocs",
            "build",
            "--strict",
            "--clean",
            "-f",
            str(path),
        ],
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_regeneration_removes_renamed_authored_and_api_pages(project):
    root, source = project
    builder.generate(update_source_lock=True)
    render_fixture(root, source)
    assert (root / ".build/site/old.html").exists()
    (root / "src_docs/md/old.md").rename(root / "src_docs/md/new.md")
    (source / "fontlab_echopy/__init__.py").write_text("class New: pass\n")
    builder.generate(update_source_lock=True)
    render_fixture(root, source)
    assert not (root / ".build/site/old.html").exists()
    assert not (root / ".build/site/reference/fontlab_echopy/Old.html").exists()
    search = json.loads((root / ".build/site/search/search_index.json").read_text())
    assert all(
        row["location"].split("#")[0]
        not in {"old.html", "reference/fontlab_echopy/Old.html"}
        for row in search["docs"]
    )
    content = root / ".build/content"
    assert not (content / "old.md").exists()
    assert not (content / "reference/fontlab_echopy/Old.md").exists()
    reused = {
        str(p.relative_to(content)): p.read_bytes()
        for p in content.rglob("*")
        if p.is_file()
    }
    shutil.rmtree(content)
    builder.generate()
    fresh = {
        str(p.relative_to(content)): p.read_bytes()
        for p in content.rglob("*")
        if p.is_file()
    }
    assert reused == fresh, "Reused and fresh input trees must be byte-identical"


def test_check_without_accepted_baseline_fails_without_mutating_generated_files(
    project,
):
    root, _ = project
    builder.generate(update_source_lock=True)
    before = (root / ".build/coverage.json").read_bytes()
    with pytest.raises(ValueError, match="accepted"):
        builder.generate(check=True)
    assert (root / ".build/coverage.json").read_bytes() == before


@pytest.mark.parametrize(
    "changed", ["guide", "renderer", "config", "template", "removal", "html", "extra"]
)
def test_check_detects_drift_without_rewriting_accepted_baseline(project, changed):
    from scripts.build_provenance import accept_build, verify_build

    root, source = project
    builder.generate(update_source_lock=True)
    render_fixture(root, source)
    site = root / ".build/site"
    accept_build(root)
    baseline = (root / ".build/accepted-build.json").read_bytes()
    builder.generate(check=True)
    verify_build(root)
    if changed == "guide":
        (root / "src_docs/md/index.md").write_text("# Changed guide")
    elif changed == "renderer":
        (root / "scripts/reference_pages.py").write_text("# renderer v2")
    elif changed == "config":
        path = root / "src_docs/mkdocs.yml"
        config = yaml.safe_load(path.read_text())
        config["site_name"] = "Changed"
        path.write_text(yaml.safe_dump(config))
    elif changed == "template":
        (root / "overrides/main.html").write_text("template v2")
    elif changed == "removal":
        (root / "src_docs/md/old.md").unlink()
    elif changed == "html":
        (site / "index.html").write_text("<h1>stale</h1>")
    else:
        (root / ".build/content/extra.md").write_text("# Unexpected")
    with pytest.raises(ValueError):
        builder.generate(check=True)
        verify_build(root)
    assert (root / ".build/accepted-build.json").read_bytes() == baseline


def test_echopy_shim_when_generated_then_documented_under_its_own_name(project):
    root, source = project
    shim = source / "fontlab_echopy/fontlabapp_shim"
    shim.mkdir()
    (shim / "__init__.py").write_text('"""Facade."""\n')
    (shim / "__init__.pyi").write_text(
        '"""Static shim of the FontLab menu tree."""\n'
        "class Menu:\n"
        '    """Main menu."""\n'
        "    def add_component(self) -> None:\n"
        '        """Glyph > Add Component."""\n'
        "    def _hidden(self) -> None: ...\n"
    )
    (shim / "_shim.json").write_text('{"capture_sha256": "' + "d" * 64 + '"}\n')
    builder.generate(update_source_lock=True)
    render_fixture(root, source)
    coverage = json.loads((root / ".build/coverage.json").read_text())
    assert "fontlabapp_shim.Menu.add_component" in coverage["symbols"]
    assert "fontlabapp_shim.Menu._hidden" not in coverage["symbols"], (
        "private names are kept only in captured native sidecars"
    )
    page = (root / ".build/site/reference/fontlabapp_shim/Menu.html").read_text()
    assert 'id="fontlabapp_shim.Menu"' in page
    lock = json.loads((root / "api-sources.lock.json").read_text())["sources"]
    assert "fontlab_echopy/fontlabapp_shim/_shim.json" in lock


def test_generate_when_shim_reexports_missing_target_then_build_fails(project):
    """R-L5-docs P2: aliases discarded by resolution must fail through the pipeline."""
    _root, source = project
    shim = source / "fontlab_echopy/GlyphsApp"
    shim.mkdir()
    (shim / "__init__.py").write_text('"""Facade."""\n')
    (shim / "__init__.pyi").write_text(
        "from fontlab_glyport.model import GSAxis as GSAxis\n__all__ = ['GSAxis']\n"
    )
    (shim / "_shim.json").write_text('{"capture_sha256": "' + "e" * 64 + '"}\n')
    with pytest.raises(ValueError, match="alias-unresolved: GlyphsApp.GSAxis"):
        builder.generate(update_source_lock=True)


def test_examples_export_when_generated_then_pages_copied_and_locked(project):
    root, _ = project
    builder.generate(update_source_lock=True)
    assert (root / ".build/content/examples/recipes/index.md").read_text() == "# Recipes\n"
    lock = json.loads((root / "api-sources.lock.json").read_text())["sources"]
    assert {"examples/manifest.json", "examples/index.md", "examples/recipes/index.md"} <= set(lock)


@pytest.mark.parametrize("damage", ["edited", "unlisted", "missing"])
def test_examples_export_when_tampered_or_absent_then_generation_fails(project, monkeypatch, tmp_path, damage):
    _root, _ = project
    export = tmp_path / "examples-export"
    if damage == "edited":
        (export / "index.md").write_text("# Changed\n")
    elif damage == "unlisted":
        (export / "extra.md").write_text("# Extra\n")
    else:
        monkeypatch.setenv("FONTLAB_EXAMPLES_EXPORT", str(tmp_path / "absent"))
    with pytest.raises((ValueError, FileNotFoundError)):
        builder.generate(update_source_lock=True)


@pytest.mark.parametrize("path", ["../../../victim.txt", "/tmp/absolute-victim.md", "a/../../b.md", "a\\\\..\\\\b.md", ""])
def test_examples_export_when_manifest_path_escapes_then_rejected_before_io(project, monkeypatch, tmp_path, path):
    """RR3-docs: manifest paths must be relative POSIX paths inside the export."""
    import hashlib

    root, _ = project
    export = tmp_path / "hostile-export"
    export.mkdir()
    victim = tmp_path / "victim.txt"
    victim.write_text("keep me")
    manifest = {"format": "fontlab-python-examples.docs-export.v1", "entry": "index.md",
                "pages": [{"path": path, "title": "x", "sha256": hashlib.sha256(b"keep me").hexdigest()}]}
    (export / "manifest.json").write_text(json.dumps(manifest))
    monkeypatch.setenv("FONTLAB_EXAMPLES_EXPORT", str(export))
    with pytest.raises(ValueError, match="path"):
        builder.generate(update_source_lock=True)
    assert victim.read_text() == "keep me"
    assert not (root / ".build/content").exists() or not any(
        (root / ".build/content").rglob("victim.txt")
    )


def test_content_files_when_finder_writes_metadata_then_it_is_not_generated_input(tmp_path):
    """Finder's .DS_Store appearing mid-build is not a generated page (final-3, issue 106)."""
    (tmp_path / "reference").mkdir()
    (tmp_path / "reference" / "a.md").write_text("a")
    (tmp_path / ".DS_Store").write_bytes(b"\0")
    (tmp_path / "reference" / ".DS_Store").write_bytes(b"\0")
    assert builder.content_files(tmp_path) == {"reference/a.md"}


def test_stage_cleanup_when_finder_writes_metadata_then_build_does_not_fail(tmp_path):
    """Removing the stage tolerates .DS_Store files Finder adds while it is removed."""
    with builder.stage_directory(tmp_path) as stage:
        (stage / "content").mkdir()
        (stage / "content" / ".DS_Store").write_bytes(b"\0")
    assert not list(tmp_path.glob("generation-*"))


def test_checkout_roots_when_typerig_repository_then_use_actual_lib_layout(tmp_path, monkeypatch):
    """Checkout discovery names the actual sibling repository, without a legacy alias."""
    monkeypatch.setattr(builder, "ROOT", tmp_path / "docs")
    monkeypatch.delenv("FONTLAB_API_SOURCE_ROOT", raising=False)
    root = next(root for root, package in builder.source_roots() if package == "typerig")
    assert root == tmp_path / "TypeRig" / "Lib"


def test_artifact_roots_when_explicit_then_typerig_uses_package_directory(tmp_path, monkeypatch):
    """Installed artifacts retain their shared package-root contract."""
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", str(tmp_path / "installed"))
    root = next(root for root, package in builder.source_roots() if package == "typerig")
    assert root == (tmp_path / "installed").resolve()


@pytest.fixture
def explicit_generation(project, monkeypatch):
    """Generate real fixture metadata with aligned, owned explicit source roots."""
    root, source = project
    monkeypatch.setattr(builder, "source_roots", lambda: [(source, "fontlab_echopy")])
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", str(source))
    builder.generate(update_source_lock=True)
    runtime = (root / ".build/mkdocs.yml").read_bytes()
    expected = runtime.decode().replace(str(root), "<docs-root>")
    for tail in ("", "/fontlab_echopy/tooling/griffe_native.py"):
        literal = f"- {source}{tail}\n"
        assert expected.count(literal) == 1
        expected = expected.replace(literal, f"- <api-source-root>{tail}\n")
    return root, source, runtime, expected


def test_generation_config_when_explicit_roots_relocated_then_all_fields_match(
    explicit_generation, monkeypatch,
):
    from scripts.build_provenance import digest, generation_manifest

    root, source, runtime, expected = explicit_generation
    first = generation_manifest(root, root / ".build")
    second_root, second_source = root.with_name("second-docs"), source.with_name("second-sources")
    shutil.copytree(root, second_root)
    shutil.copytree(source, second_source)
    monkeypatch.setattr(builder, "ROOT", second_root)
    monkeypatch.setattr(builder, "source_roots", lambda: [(second_source, "fontlab_echopy")])
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", str(second_source))
    builder.generate()
    second_runtime = (second_root / ".build/mkdocs.yml").read_bytes()
    second = generation_manifest(second_root, second_root / ".build")
    assert {k: v for k, v in first.items() if k != "config"} == {
        k: v for k, v in second.items() if k != "config"
    }
    assert first["config"] == second["config"], "Equivalent separately owned explicit roots must be portable"
    assert first["config"] == digest(expected.encode())
    assert (root / ".build/mkdocs.yml").read_bytes() == runtime
    assert (second_root / ".build/mkdocs.yml").read_bytes() == second_runtime
    assert runtime != second_runtime, "Runtime YAML must retain each actual absolute path"


@pytest.mark.parametrize(
    "value, logical",
    [
        ("{api}", "<api-source-root>"),
        ("'{api}'", "'<api-source-root>'"),
        ('"{api}"', '"<api-source-root>"'),
        ("{api}/folder with spaces/tool.py", "<api-source-root>/folder with spaces/tool.py"),
        ("'{api}/folder with spaces/tool.py'", "'<api-source-root>/folder with spaces/tool.py'"),
        ('"{api}/folder with spaces/tool.py"', '"<api-source-root>/folder with spaces/tool.py"'),
        ("{api}  ", "<api-source-root>  "),
        ('"{api}"  ', '"<api-source-root>"  '),
        ("{api}-extra/tool.py", "{api}-extra/tool.py"),
        ("{api}2/tool.py", "{api}2/tool.py"),
        ("{api} extra/tool.py", "{api} extra/tool.py"),
        ("'{api} extra/tool.py'", "'{api} extra/tool.py'"),
        ('"{api} extra/tool.py"', '"{api} extra/tool.py"'),
        ("{outside}/tool.py", "{outside}/tool.py"),
        ("prefix {api}/tool.py", "prefix {api}/tool.py"),
        ('"{escaped}/tool.py"', '"{escaped}/tool.py"'),
    ],
)
def test_generation_config_when_list_path_boundary_then_only_selected_root_changes(
    explicit_generation, value, logical,
):
    from scripts.build_provenance import digest, generation_manifest

    root, source, runtime, expected = explicit_generation
    fields = {"api": str(source), "outside": str(source.parent / "outside"),
              "escaped": str(source.parent / r"sour\u0063es")}
    before = runtime.decode().replace(f"- {source}\n", f"- {value.format(**fields)}\n")
    wanted = expected.replace("- <api-source-root>\n", f"- {logical.format(**fields)}\n")
    path = root / ".build/mkdocs.yml"
    path.write_text(before)
    actual = generation_manifest(root, root / ".build")
    assert actual["config"] == digest(wanted.encode())
    assert path.read_text() == before, "Fingerprinting must not rewrite runtime YAML"


@pytest.mark.parametrize("quote", ["", "'", '"'])
@pytest.mark.parametrize("tail, selected", [("", True), ("/folder with spaces/tool.py", True),
                                           (" extra/tool.py", False), ("-extra/tool.py", False)])
def test_generation_config_when_literal_root_contains_spaces_then_full_scalar_boundary_is_used(
    explicit_generation, monkeypatch, quote, tail, selected,
):
    from scripts.build_provenance import digest, generation_manifest

    root, source, runtime, expected = explicit_generation
    spaced = source.with_name("api packages")
    shutil.copytree(source, spaced)
    monkeypatch.setattr(builder, "source_roots", lambda: [(spaced, "fontlab_echopy")])
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", str(spaced))
    # Author a valid literal scalar unit input; do not claim folded-YAML parity or a site build.
    before = runtime.decode().replace(str(source), str(spaced))
    assert before.count(str(spaced)) == 2
    before = before.replace(f"- {spaced}\n", f"- {quote}{spaced}{tail}{quote}\n")
    value = "<api-source-root>" if selected else str(spaced)
    wanted = expected.replace("- <api-source-root>\n", f"- {quote}{value}{tail}{quote}\n")
    path = root / ".build/mkdocs.yml"
    path.write_text(before)
    assert generation_manifest(root, root / ".build")["config"] == digest(wanted.encode())
    assert path.read_text() == before


def test_generation_config_when_semantics_comments_or_tails_change_then_digest_stays_sensitive(
    explicit_generation,
):
    from scripts.build_provenance import digest, generation_manifest

    root, source, runtime, expected = explicit_generation
    path = root / ".build/mkdocs.yml"
    base = generation_manifest(root, root / ".build")
    fingerprints = []
    for marker in ("first", "second"):
        comment = f"\n# - {source}/{marker}.py\n"
        before = runtime.decode() + comment
        wanted = expected + comment
        path.write_text(before)
        actual = generation_manifest(root, root / ".build")
        assert actual["config"] == digest(wanted.encode())
        assert {k: v for k, v in actual.items() if k != "config"} == {
            k: v for k, v in base.items() if k != "config"
        }
        assert path.read_text() == before
        fingerprints.append(actual["config"])
    assert fingerprints[0] != fingerprints[1]
    for marker in ("first", "second"):
        before = runtime.decode().replace("site_name:", f"site_name: {source}/{marker} #")
        wanted = expected.replace("site_name:", f"site_name: {source}/{marker} #")
        path.write_text(before)
        actual = generation_manifest(root, root / ".build")
        assert actual["config"] == digest(wanted.encode()), "Map-scalar values are semantic, not selected list paths"
        fingerprints.append(actual["config"])
    assert fingerprints[2] != fingerprints[3]
    for marker in ("first", "second"):
        original_tail = "/fontlab_echopy/tooling/griffe_native.py"
        changed_tail = f"/fontlab_echopy/tooling/{marker}.py"
        before = runtime.decode().replace(original_tail, changed_tail)
        wanted = expected.replace(original_tail, changed_tail)
        path.write_text(before)
        actual = generation_manifest(root, root / ".build")
        assert actual["config"] == digest(wanted.encode()), "Relative extension tails remain fingerprint inputs"
        assert path.read_text() == before
        fingerprints.append(actual["config"])
    assert fingerprints[4] != fingerprints[5]


@pytest.mark.parametrize("setting", [None, ""])
def test_generation_config_when_explicit_root_unset_or_empty_then_current_hash_is_retained(
    explicit_generation, monkeypatch, setting,
):
    from scripts.build_provenance import digest, generation_manifest

    root, _source, runtime, _expected = explicit_generation
    if setting is None:
        monkeypatch.delenv("FONTLAB_API_SOURCE_ROOT")
    else:
        monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", setting)
    actual = generation_manifest(root, root / ".build")
    assert actual["config"] == digest(runtime.decode().replace(str(root), "<docs-root>").encode())
    assert (root / ".build/mkdocs.yml").read_bytes() == runtime


def test_source_roots_when_explicit_home_and_parent_components_then_real_resolver_is_used(
    tmp_path, monkeypatch,
):
    home = tmp_path / "owned home"
    source = home / "api packages"
    source.mkdir(parents=True)
    (home / "scratch").mkdir()
    monkeypatch.setenv("HOME", str(home))
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", "~/scratch/../api packages")
    roots = builder.source_roots()
    assert len(roots) == len(builder.PACKAGES)
    assert {path for path, _package in roots} == {source.resolve()}


def test_generation_config_when_explicit_value_expands_and_resolves_then_generated_root_matches(
    explicit_generation, monkeypatch,
):
    from scripts.build_provenance import digest, generation_manifest

    root, source, runtime, expected = explicit_generation
    (source.parent / "scratch").mkdir()
    monkeypatch.setenv("HOME", str(source.parent))
    monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", "~/scratch/../sources")
    assert generation_manifest(root, root / ".build")["config"] == digest(expected.encode())
    assert (root / ".build/mkdocs.yml").read_bytes() == runtime


@pytest.mark.parametrize("quote", ["", "'", '"'])
@pytest.mark.parametrize("tail", ["", "/fontlab_echopy/tooling/griffe_native.py"])
def test_generation_config_when_separator_root_then_exact_root_and_descendants_match(
    tmp_path, monkeypatch, quote, tail,
):
    from scripts.build_provenance import digest, generation_manifest

    # Actual whole-function metadata input; API paths are strings, never traversed.
    root = tmp_path / "docs"
    stage = root / "stage"
    stage.mkdir(parents=True)
    for folder in ("content", "native-names"):
        (stage / folder).mkdir()
    (stage / "coverage.json").write_text("{}\n")
    ordinary = tmp_path / "owned-api"
    ordinary.mkdir()
    expected = f"paths:\n  - {quote}<api-source-root>{tail}{quote}\n"
    manifests = []
    for api_root in (str(ordinary), "/"):
        value = api_root.rstrip("/") + tail if tail else api_root
        runtime = f"paths:\n  - {quote}{value}{quote}\n"
        path = stage / "mkdocs.yml"
        path.write_text(runtime)
        monkeypatch.setenv("FONTLAB_API_SOURCE_ROOT", api_root)
        manifests.append(generation_manifest(root, stage))
        assert path.read_text() == runtime, "Fingerprinting must not rewrite runtime YAML"
    first, second = manifests
    assert first["config"] == digest(expected.encode()), "Ordinary external-root control must match"
    assert {k: v for k, v in first.items() if k != "config"} == {
        k: v for k, v in second.items() if k != "config"
    }
    assert second["config"] == digest(expected.encode()), "Separator root retains the canonical tail separator"
    assert first["config"] == second["config"]
