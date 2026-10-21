# this_file: scripts/build_provenance.py
"""Deterministic input/output manifests for the accepted local artifact."""

import hashlib
import json
from importlib.metadata import version
from pathlib import Path

PACKAGES = (
    "properdocs",
    "mkdocs-materialx",
    "mkdocstrings",
    "mkdocstrings-python",
    "mkdocs-autorefs",
    "griffe",
    "pymdown-extensions",
)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_manifest(root: Path, *, exclude=()) -> dict:
    return {
        path.relative_to(root).as_posix(): digest(path.read_bytes())
        for path in sorted(root.rglob("*"))
        if path.is_file()
        and path.name != ".DS_Store"
        and path.relative_to(root).as_posix() not in exclude
        and "__pycache__" not in path.parts
    }


def generation_manifest(root: Path, stage: Path) -> dict:
    inputs = {}
    for directory in ("src_docs/md", "scripts", "overrides", "archive"):
        inputs.update(
            {
                directory + "/" + path: value
                for path, value in file_manifest(root / directory).items()
            }
        )
    for name in ("src_docs/mkdocs.yml", "api-sources.lock.json", "pyproject.toml", "uv.lock"):
        path = root / name
        if path.exists():
            inputs[name] = digest(path.read_bytes())
    return {
        "inputs": inputs,
        "packages": {name: version(name) for name in PACKAGES},
        "content": file_manifest(stage / "content"),
        "native_names": file_manifest(stage / "native-names"),
        "coverage": digest((stage / "coverage.json").read_bytes()),
        # Normalize owned paths; source/artifact location parity is a separate gate.
        "config": digest(
            (stage / "mkdocs.yml")
            .read_text()
            .replace(str(root), "<docs-root>")
            .encode()
        ),
    }


def check_generation(root: Path, candidate: dict) -> None:
    baseline = root / ".build/accepted-build.json"
    if not baseline.exists():
        raise ValueError(
            "Missing accepted build baseline; run a normal strict build first"
        )
    accepted = json.loads(baseline.read_text())["generation"]
    if candidate != accepted or generation_manifest(root, root / ".build") != accepted:
        raise ValueError("Generated content/input manifest differs from accepted build")


def accept_build(root: Path) -> None:
    """Seal final rendered bytes only after the caller's strict verification."""
    build = root / ".build"
    generation = json.loads((build / "generation-manifest.json").read_text())
    if generation != generation_manifest(root, build):
        raise ValueError("Build inputs changed while rendering")
    receipt = {
        "schema_version": 1,
        "generation": generation,
        "rendered": file_manifest(build / "site", exclude=("build-provenance.json",)),
    }
    payload = json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n"
    (build / "site/build-provenance.json").write_text(payload)
    (build / "accepted-build.json").write_text(payload)


def verify_build(root: Path) -> None:
    build = root / ".build"
    baseline = build / "accepted-build.json"
    if not baseline.exists():
        raise ValueError("Missing accepted build baseline")
    accepted = json.loads(baseline.read_text())
    if (
        file_manifest(build / "site", exclude=("build-provenance.json",))
        != accepted["rendered"]
    ):
        raise ValueError("Rendered artifact differs from accepted build")
    receipt = build / "site/build-provenance.json"
    if not receipt.exists() or receipt.read_bytes() != baseline.read_bytes():
        raise ValueError("Rendered artifact provenance differs from accepted build")
