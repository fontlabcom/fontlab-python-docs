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
    (root / "site-src").mkdir()
    (root / "site-src/index.md").write_text("# Current\n")
    (root / "site-src/old.md").write_text("# Old guide\n")
    (root / "scripts").mkdir()
    (root / "scripts/reference_pages.py").write_text("# renderer v1\n")
    (root / "overrides").mkdir()
    (root / "overrides/main.html").write_text("template v1")
    original = Path(builder.__file__).resolve().parents[1]
    shutil.copyfile(original / "mkdocs.yml", root / "mkdocs.yml")
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
    (root / "site-src/old.md").rename(root / "site-src/new.md")
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
        (root / "site-src/index.md").write_text("# Changed guide")
    elif changed == "renderer":
        (root / "scripts/reference_pages.py").write_text("# renderer v2")
    elif changed == "config":
        path = root / "mkdocs.yml"
        config = yaml.safe_load(path.read_text())
        config["site_name"] = "Changed"
        path.write_text(yaml.safe_dump(config))
    elif changed == "template":
        (root / "overrides/main.html").write_text("template v2")
    elif changed == "removal":
        (root / "site-src/old.md").unlink()
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
    root, source = project
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
    root, _ = project
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
