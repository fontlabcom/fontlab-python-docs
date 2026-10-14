# this_file: scripts/build_reference.py
"""Build complete source-derived reference inputs; never import native APIs."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from pathlib import Path

import yaml

from .api_inventory import inventory_sources, plan_pages
from .export_aliases import resolved_aliases
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
    """Regenerate all pages and verify coverage without host/runtime imports."""
    roots = source_roots()
    native_root = next(root for root, package in roots if package == "fontlab_echopy")
    sys.path.insert(0, str(native_root))
    from fontlab_echopy.tooling.docnames import export_docnames

    namespace_root = ROOT / ".build/native-names"
    export_docnames(namespace_root, source=native_root / "fontlab_echopy")
    plan = plan_pages(inventory_sources(roots))
    apply_lock(
        ROOT / "api-sources.lock.json", plan["inputs"], update=update_source_lock
    )
    aliases = _aliases(plan)
    content = ROOT / ".build/content"
    content.mkdir(parents=True, exist_ok=True)
    for source in (ROOT / "site-src").rglob("*"):
        if source.is_file():
            target = content / source.relative_to(ROOT / "site-src")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
    page_hashes = {}
    for relative in plan["pages"]:
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
    }
    metadata = ROOT / ".build/coverage.json"
    payload = json.dumps(coverage, sort_keys=True, separators=(",", ":")) + "\n"
    digest = hashlib.sha256(payload.encode()).hexdigest()
    previous = metadata.read_bytes() if metadata.exists() else None
    if check and previous is not None and previous != payload.encode():
        raise ValueError(
            "Generated coverage changed; run a normal build after source changes."
        )
    metadata.write_text(payload)
    public = {
        "schema_version": 1,
        "summary": plan["summary"],
        "coverage_sha256": digest,
        "source_inputs": plan["inputs"],
        "generated_pages": page_hashes,
        "runtime_inspection": False,
    }
    (content / "build-info.json").write_text(
        json.dumps(public, indent=2, sort_keys=True) + "\n"
    )
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    config["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["paths"] = [
        str(namespace_root)
    ] + list(dict.fromkeys(str(root) for root, _ in roots))
    config["plugins"][-1]["mkdocstrings"]["handlers"]["python"]["options"][
        "extensions"
    ] = [
        str(native_root / "fontlab_echopy/tooling/griffe_native.py"),
        str(ROOT / "scripts/griffe_sources.py"),
    ]
    config["docs_dir"] = str(content)
    config["site_dir"] = str(ROOT / ".build/site")
    config["hooks"] = [str(ROOT / "scripts/site_hooks.py")]
    config["theme"]["custom_dir"] = str(ROOT / "overrides")
    (ROOT / ".build/mkdocs.yml").write_text(yaml.safe_dump(config, sort_keys=False))
    assert all(
        row["body_target"] in plan["symbols"] for row in plan["symbols"].values()
    )
    print(
        json.dumps(
            {**plan["summary"], "aliases": len(aliases), "coverage_sha256": digest},
            indent=2,
        )
    )
    return public


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    generate(check=parser.parse_args().check)
