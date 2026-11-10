# this_file: scripts/search_shards.py
"""Build and reconcile complete search rows before replacing the page bootstrap."""

import gzip
import hashlib
import json
import shutil
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "scripts/search_backend"
WORKER = ROOT / "overrides/assets/javascripts/workers/complete-search.js"
UI = ROOT / "overrides/assets/javascripts/complete-search-ui.js"
INITIAL_BUDGET = 5 * 1024 * 1024


# Assets with no shipped .gz (bootstrap index, worker, UI) get an estimate under the
# portable codec (fflate, level 9, mtime 0), not whatever zlib build Python links.
# Shipped complete/ assets use the gzip sizes their manifest records and verifies.
PORTABLE_GZIP_SIZES = (
    "const {gzipSync}=require(process.argv[1]);const fs=require('node:fs');"
    "console.log(JSON.stringify(process.argv.slice(2).map("
    "f=>gzipSync(fs.readFileSync(f),{level:9,mtime:0}).length)))"
)


def portable_gzip_sizes(paths: list[Path]) -> list[int]:
    """Gzip sizes of files under the bundled portable codec, in one node call."""
    if not paths:
        return []
    done = subprocess.run(
        [
            "node",
            "-e",
            PORTABLE_GZIP_SIZES,
            str(BACKEND / "gzip.cjs"),
            *map(str, paths),
        ],
        check=False,
        capture_output=True,
        text=True,
        timeout=60,
    )
    if done.returncode:
        raise RuntimeError(f"portable gzip codec failed: {done.stderr.strip()}")
    return json.loads(done.stdout)


def encode(data: dict) -> bytes:
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).encode()


def checked_asset(directory: Path, spec: dict) -> bytes:
    name = spec["file"]
    if Path(name).name != name:
        raise ValueError("Invalid search asset path")
    data = (directory / name).read_bytes()
    if len(data) != spec["raw"] or hashlib.sha256(data).hexdigest() != spec["sha256"]:
        raise ValueError(f"Search asset size/hash mismatch: {name}")
    compressed = (directory / (name + ".gz")).read_bytes()
    if len(compressed) != spec["gzip"] or gzip.decompress(compressed) != data:
        raise ValueError(f"Search compressed asset size/hash mismatch: {name}")
    return data


def read_shards(directory: Path, manifest: dict) -> dict:
    """Rehydrate every field; count/hash failures cannot become empty coverage."""
    docs = []
    for ordinal, spec in enumerate(manifest["shards"]):
        if spec["id"] != ordinal or spec["start"] != len(docs):
            raise ValueError("Search shard range mismatch")
        rows = json.loads(checked_asset(directory, spec))
        if len(rows) != spec["rows"]:
            raise ValueError("Search shard row count mismatch")
        docs.extend(rows)
    if len(docs) != manifest["rows"]:
        raise ValueError("Complete search row count mismatch")
    return {"config": manifest["config"], "docs": docs}


def read_complete_index(path: Path) -> dict:
    """Read monolithic originals or reconstruct the new complete consumer corpus."""
    bootstrap = json.loads(path.read_bytes())
    if "complete" not in bootstrap.get("config", {}):
        return bootstrap
    directory = path.parent / "complete"
    manifest = json.loads(
        checked_asset(directory, bootstrap["config"]["complete"]["manifest"])
    )
    return read_shards(directory, manifest)


def inspect_shards(path: Path, *, deployed: bool = False) -> dict:
    bootstrap = json.loads(path.read_bytes())
    directory = path.parent / "complete"
    spec = bootstrap["config"]["complete"]["manifest"]
    manifest = json.loads(checked_asset(directory, spec))
    corpus = read_shards(directory, manifest)
    # Inspect all routing bytes, not merely the bootstrap's empty docs list.
    for asset in (manifest["terms"], manifest["postings"]):
        checked_asset(directory, asset)
    subprocess.run(
        ["node", str(BACKEND / "verify.cjs"), str(directory)],
        check=True,
        capture_output=True,
        text=True,
        timeout=60,
    )
    initial = [path, directory / spec["file"]]
    initial.extend(
        directory / asset["file"] for asset in (manifest["terms"], manifest["postings"])
    )
    for source in (WORKER, UI):
        relative = source.relative_to(ROOT / "overrides")
        asset = path.parent.parent / relative
        initial.append(asset if deployed else source)
    initial_sizes = [file.stat().st_size for file in initial]
    original = encode(corpus)
    return {
        "rows": len(corpus["docs"]),
        "shards": len(manifest["shards"]),
        "tokens": manifest["tokens"],
        "input_sha256": manifest["input_sha256"],
        "aggregate_bytes": manifest["input_raw"],
        "aggregate_gzip_bytes": manifest["input_gzip"],
        "reconstructed_bytes": len(original),
        "shard_bytes": sum(s["raw"] for s in manifest["shards"]),
        "shard_gzip_bytes": sum(s["gzip"] for s in manifest["shards"]),
        # Recorded (verified) gzip for the three shipped assets; estimate for the rest.
        "initial_gzip_bytes": sum(portable_gzip_sizes([initial[0], *initial[-2:]]))
        + spec["gzip"]
        + manifest["terms"]["gzip"]
        + manifest["postings"]["gzip"],
        "initial_static_bytes": initial_sizes[0]
        + spec["gzip"]
        + manifest["terms"]["gzip"]
        + manifest["postings"]["gzip"]
        + sum(initial_sizes[-2:]),
        "largest_shard_bytes": max((s["raw"] for s in manifest["shards"]), default=0),
    }


def build_shards(path: Path, *, shard_bytes: int = 1024 * 1024) -> dict:
    """Use committed pinned engine bundles; ordinary source builds need no npm/network."""
    original = json.loads(path.read_bytes())
    if "complete" in original.get("config", {}):
        raise ValueError("Expected complete original rows, not a bootstrap")
    pins = json.loads((BACKEND / "bundles.json").read_text())
    for name, digest in pins["files"].items():
        if hashlib.sha256((BACKEND / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Search bundle drift; run the documented pinned compile")
    with tempfile.TemporaryDirectory(
        prefix="complete-search-", dir=path.parent
    ) as temporary:
        directory = Path(temporary) / "complete"
        directory.mkdir()
        subprocess.run(
            [
                "node",
                str(BACKEND / "build.cjs"),
                str(path),
                str(directory),
                str(shard_bytes),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=180,
        )
        manifest_bytes = (directory / "manifest.json").read_bytes()
        restored = read_shards(directory, json.loads(manifest_bytes))
        canonical = lambda rows: Counter(
            json.dumps(row, sort_keys=True) for row in rows
        )
        if restored["config"] != original["config"] or canonical(
            restored["docs"]
        ) != canonical(original["docs"]):
            raise ValueError("Complete search reconstruction differs from original")
        bootstrap = {
            "docs": [],
            "config": {
                "complete": {
                    "manifest": {
                        "file": "manifest.json",
                        "raw": len(manifest_bytes),
                        "gzip": (directory / "manifest.json.gz").stat().st_size,
                        "sha256": hashlib.sha256(manifest_bytes).hexdigest(),
                    }
                }
            },
        }
        staged_bootstrap = Path(temporary) / "search_index.json"
        staged_bootstrap.write_bytes(encode(bootstrap))
        report = inspect_shards(staged_bootstrap)
        if report["initial_static_bytes"] > INITIAL_BUDGET:
            raise ValueError(
                f"Initial complete-search payload exceeds {INITIAL_BUDGET} bytes: {report}"
            )
        output = path.parent / "complete"
        if output.exists():
            shutil.rmtree(output)
        shutil.copytree(directory, output)
        path.write_bytes(encode(bootstrap))
    return report
