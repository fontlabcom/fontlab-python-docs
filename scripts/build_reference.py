# this_file: scripts/build_reference.py
"""Build complete source-derived reference inputs; never import native APIs."""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import yaml

from .api_inventory import inventory_sources, plan_pages
from .export_aliases import resolved_aliases
from .reconcile_coverage import enforce, reconcile
from .reference_pages import relative_link, render_page
from .source_lock import apply_lock

ROOT = Path(__file__).resolve().parents[1]
PACKAGES = {
    "fontlab-echopy": ("src", "fontlab_echopy"),
    "fontlab-fontlabapp": ("src", "fontlabapp"),
    "fontlab-remopy": ("src", "fontlab_remopy"),
    "fontlab-grablab": ("src", "grablab"),
    "pythonqtside": ("src", "pythonqtside"),
    "fontlab-fly": ("src", "fly"),
    "typerig-lib": ("Lib", "typerig"),
    "fontlab-glyport": ("src", "fontlab_glyport"),
    "fontlab-aidus-code": ("", "fontlab_aidus_code"),
    "fontlab-fontport": ("src", "fontlab_fontport"),  # D14: docstrings/signatures only
}


EXAMPLES_FORMAT = "fontlab-python-examples.docs-export.v1"
# Relative POSIX page paths only: no absolute paths, `..`, backslashes or dots.
EXAMPLES_PAGE = re.compile(r"[A-Za-z0-9_-]+(?:/[A-Za-z0-9_-]+)*\.md")


def _contained(folder: Path, path: object) -> Path:
    """Validate a manifest page path before any read or write uses it."""
    if not isinstance(path, str) or not EXAMPLES_PAGE.fullmatch(path):
        raise ValueError(f"Unsafe examples export path: {path!r}")
    target = (folder / path).resolve()
    if not target.is_relative_to(folder.resolve()):
        raise ValueError(f"Examples export path leaves its folder: {path!r}")
    return target


def examples_export() -> dict[str, bytes]:
    """Verified pages of the fontlab-python-examples docs export, keyed by path.

    Every page must match the manifest's sha256 and no unlisted page may exist.
    A missing export fails the build; examples are never silently skipped.
    """
    folder = Path(
        os.environ.get("FONTLAB_EXAMPLES_EXPORT")
        or ROOT.parent / "fontlab-python-examples" / "docs-export"
    )
    manifest_bytes = (folder / "manifest.json").read_bytes()
    manifest = json.loads(manifest_bytes)
    if manifest.get("format") != EXAMPLES_FORMAT:
        raise ValueError(f"Unsupported examples export format: {manifest.get('format')}")
    pages = {"manifest.json": manifest_bytes}
    targets = {row.get("path"): _contained(folder, row.get("path")) for row in manifest["pages"]}
    for row in manifest["pages"]:
        data = targets[row["path"]].read_bytes()
        if hashlib.sha256(data).hexdigest() != row["sha256"]:
            raise ValueError("Examples export page differs from its manifest: " + row["path"])
        pages[row["path"]] = data
    present = {p.relative_to(folder).as_posix() for p in folder.rglob("*.md")}
    if present - set(pages):
        raise ValueError("Examples export pages missing from its manifest: " + ", ".join(sorted(present - set(pages))))
    return pages


def source_roots() -> list[tuple[Path, str]]:
    """Use sibling checkouts or an explicit installed-artifact source directory."""
    artifact_root = os.environ.get("FONTLAB_API_SOURCE_ROOT")
    if artifact_root:
        return [
            (Path(artifact_root).expanduser().resolve(), package)
            for _, package in PACKAGES.values()
        ]
    return [
        (ROOT.parent / repo / source, package)
        for repo, (source, package) in PACKAGES.items()
    ]


def _aliases(plan: dict) -> dict[str, str]:
    aliases = dict(plan["aliases"])
    aliases.update(
        {
            "fontlabapp.FontLab": "fontlabapp.controls.FontLab",
            "fontlabapp.Application": "fontlabapp.application.application.Application",
            "fly.qt": "PythonQt",
        }
    )
    for identifier, row in plan["symbols"].items():
        canonical = row.get("canonical_id")
        if canonical and canonical != identifier:
            aliases[canonical] = identifier
    return resolved_aliases(aliases, plan["symbols"])


def content_files(content: Path) -> set[str]:
    """Generated input pages; Finder's .DS_Store (written while a window shows .build) is not one."""
    return {
        path.relative_to(content).as_posix()
        for path in content.rglob("*")
        if path.is_file() and path.name != ".DS_Store"
    }


@contextmanager
def stage_directory(build: Path) -> Iterator[Path]:
    """A fresh generation stage inside .build, removed afterwards.

    Finder can add .DS_Store to a directory while it is being removed, so a failed
    removal is repeated once; the build result never depends on that cleanup.
    """
    stage = Path(tempfile.mkdtemp(prefix="generation-", dir=build))
    try:
        yield stage
    finally:
        try:
            shutil.rmtree(stage)
        except OSError:
            shutil.rmtree(stage, ignore_errors=True)


def generate(*, check: bool = False, update_source_lock: bool = False) -> dict:
    """Generate in isolation; checks never rewrite accepted inputs or artifacts."""
    from .build_provenance import check_generation, generation_manifest

    if check and update_source_lock:
        raise ValueError("A check cannot update the source lock")
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    with stage_directory(build) as stage:
        public = _generate(stage, update_source_lock=update_source_lock)
        manifest = generation_manifest(ROOT, stage)
        if check:
            check_generation(ROOT, manifest)
            return public
        for name in ("content", "native-names"):
            old, fresh = build / name, stage / name
            # Preserve Finder metadata while replacing only our owned tree.
            if old.exists():
                for path in old.rglob(".DS_Store"):
                    target = fresh / path.relative_to(old)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(path, target)
                shutil.rmtree(old)
            fresh.rename(old)
        for name in ("coverage.json", "mkdocs.yml"):
            (stage / name).replace(build / name)
        (build / "generation-manifest.json").write_text(
            json.dumps(manifest, sort_keys=True, separators=(",", ":")) + "\n"
        )
        return public


def _generate(stage: Path, *, update_source_lock: bool) -> dict:
    """Create one complete fresh generation without touching previous output."""
    roots = source_roots()
    native_root = next(root for root, package in roots if package == "fontlab_echopy")
    old_path = list(sys.path)
    try:
        sys.path.insert(0, str(native_root))
        from fontlab_echopy.tooling.docnames import export_docnames
    finally:
        sys.path[:] = old_path

    namespace_root = stage / "native-names"
    export_docnames(namespace_root, source=native_root / "fontlab_echopy")
    plan = plan_pages(inventory_sources(roots))
    identity_files = {}
    shims = sorted(
        path.relative_to(native_root / "fontlab_echopy").as_posix()
        for path in (native_root / "fontlab_echopy").glob("*/_shim.json")
    )
    for name in ("_identities.json", "_provenance.json", *shims):
        data = (native_root / "fontlab_echopy" / name).read_bytes()
        identity_files[name] = data
        plan["inputs"].append(
            {
                "source": "fontlab_echopy/" + name,
                "sha256": hashlib.sha256(data).hexdigest(),
                "bytes": len(data),
            }
        )
    examples = examples_export()
    plan["inputs"] += [
        {"source": "examples/" + path, "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
        for path, data in examples.items()
    ]
    plan["inputs"].sort(key=lambda row: row["source"])
    apply_lock(
        ROOT / "api-sources.lock.json", plan["inputs"], update=update_source_lock
    )
    aliases = _aliases(plan)
    shim_exports = {}
    for shim in shims:
        tree = ast.parse(
            (native_root / "fontlab_echopy" / shim)
            .with_name("__init__.pyi")
            .read_bytes()
        )
        shim_exports[shim.partition("/")[0]] = next(
            (
                ast.literal_eval(node.value)
                for node in tree.body
                if isinstance(node, ast.Assign)
                and getattr(node.targets[0], "id", "") == "__all__"
            ),
            [],
        )  # Without __all__, every export is a declaration the inventory already holds.
    reconciliation = reconcile(
        json.loads(identity_files["_identities.json"]),
        plan["symbols"],
        aliases,
        provenance_capture_sha256=json.loads(identity_files["_provenance.json"])
        .get("capture_identity", {})
        .get("sha256"),
        shim_exports=shim_exports,
        raw_aliases=plan["aliases"],
    )
    enforce(reconciliation)
    content = stage / "content"
    content.mkdir(parents=True, exist_ok=True)
    expected_files = set()
    for source in (ROOT / "site-src").rglob("*"):
        if source.is_file() and source.name != ".DS_Store":
            expected_files.add(source.relative_to(ROOT / "site-src").as_posix())
            target = content / source.relative_to(ROOT / "site-src")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    for path, data in examples.items():
        if path == "manifest.json":
            continue
        expected_files.add("examples/" + path)
        target = _contained(content / "examples", path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    page_hashes = {}
    for relative in plan["pages"]:
        expected_files.add(relative)
        text = render_page(relative, plan)
        target = content / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        page_hashes[relative] = hashlib.sha256(text.encode()).hexdigest()
    families = [
        "fontlab",
        "fontgate",
        "fontpr",
        "fontlabpr",
        "PythonQt",
        "fontlab_echopy",
        "fontlabapp",
        "fontlabapp_shim",
        "GlyphsApp",
        "vanilla",
        "AppKit",
        "Cocoa",
        "Foundation",
        "objc",
        "aidus_code_tools",
        "fontlab_remopy",
        "grablab",
        "pythonqtside",
        "fly",
        "typerig",
        "fontlab_glyport",
        "fontlab_aidus_code",
    ]
    index = [
        "# API reference",
        "",
        "Generated from the current captured/enriched native API and ecosystem Python source.",
        "",
    ]
    index += [
        f"- [`{family}`](../{relative_link('reference/index.md', plan['symbols'][family]['url'])})"
        for family in families
        if family in plan["symbols"]
    ]
    # Links are relative to reference/index.md; no extra parent prefix is needed.
    index = [line.replace("](../", "](") for line in index]
    (content / "reference/index.md").write_text("\n".join(index) + "\n")
    coverage = {
        "schema_version": 1,
        "summary": plan["summary"],
        "inputs": plan["inputs"],
        "symbols": {
            identifier: {key: value for key, value in row.items() if key != "docstring"}
            for identifier, row in plan["symbols"].items()
        },
        "aliases": aliases,
        "pages": plan["pages"],
        "reconciliation": reconciliation,
    }
    metadata = stage / "coverage.json"
    payload = json.dumps(coverage, sort_keys=True, separators=(",", ":")) + "\n"
    digest = hashlib.sha256(payload.encode()).hexdigest()
    metadata.write_text(payload)
    public = {
        "schema_version": 1,
        "summary": plan["summary"],
        "coverage_sha256": digest,
        "source_inputs": plan["inputs"],
        "generated_pages": page_hashes,
        "runtime_inspection": False,
        "reconciliation": {
            "capture_sha256": reconciliation["capture_sha256"],
            **reconciliation["counts"],
        },
    }
    (content / "build-info.json").write_text(
        json.dumps(public, indent=2, sort_keys=True) + "\n"
    )
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    config["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["paths"] = [
        str(ROOT / ".build/native-names")
    ] + list(dict.fromkeys(str(root) for root, _ in roots))
    config["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["options"][
        "extensions"
    ] = [
        str(native_root / "fontlab_echopy/tooling/griffe_native.py"),
        str(ROOT / "scripts/griffe_sources.py"),
    ]
    config["docs_dir"] = str(ROOT / ".build/content")
    config["site_dir"] = str(ROOT / ".build/site")
    config["hooks"] = [str(ROOT / "scripts/site_hooks.py")]
    config["theme"]["custom_dir"] = str(ROOT / "overrides")
    (stage / "mkdocs.yml").write_text(yaml.safe_dump(config, sort_keys=False))
    expected_files.update({"reference/index.md", "build-info.json"})
    if expected_files != content_files(content):
        raise ValueError("Generated input file set differs from plan")
    assert all(
        row["body_target"] in plan["symbols"] for row in plan["symbols"].values()
    )
    print(
        json.dumps(
            {
                **plan["summary"],
                "aliases": len(aliases),
                "coverage_sha256": digest,
                "reconciliation": reconciliation["counts"],
            },
            indent=2,
        )
    )
    return public


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    generate(check=parser.parse_args().check)
