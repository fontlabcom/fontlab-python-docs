# this_file: scripts/build_reference.py
"""Build complete source-derived reference inputs; never import native APIs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
import tempfile
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
}


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


def generate(*, check: bool = False, update_source_lock: bool = False) -> dict:
    """Generate in isolation; checks never rewrite accepted inputs or artifacts."""
    from .build_provenance import check_generation, generation_manifest

    if check and update_source_lock:
        raise ValueError("A check cannot update the source lock")
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="generation-", dir=build) as temporary:
        stage = Path(temporary)
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
    plan["inputs"].sort(key=lambda row: row["source"])
    apply_lock(
        ROOT / "api-sources.lock.json", plan["inputs"], update=update_source_lock
    )
    aliases = _aliases(plan)
    reconciliation = reconcile(
        json.loads(identity_files["_identities.json"]),
        plan["symbols"],
        aliases,
        provenance_capture_sha256=json.loads(identity_files["_provenance.json"])
        .get("capture_identity", {})
        .get("sha256"),
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
    actual_files = {
        path.relative_to(content).as_posix()
        for path in content.rglob("*")
        if path.is_file()
    }
    if expected_files != actual_files:
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
