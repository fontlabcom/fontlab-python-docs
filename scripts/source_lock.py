# this_file: scripts/source_lock.py
"""Pin the exact API source bytes across checkout and installed-artifact builds."""

import json
from pathlib import Path


def input_hashes(inputs: list[dict]) -> dict[str, str]:
    """Reject duplicate input identities instead of silently dropping their bytes."""
    actual = {}
    for row in inputs:
        if row["source"] in actual:
            raise ValueError("Duplicate API source input: " + row["source"])
        actual[row["source"]] = row["sha256"]
    return actual


def verify_inputs(locked: dict[str, str], inputs: list[dict]) -> None:
    """Fail for missing, new or modified source; never silently refresh a lock."""
    actual = input_hashes(inputs)
    changed = sorted(
        name
        for name in locked.keys() | actual.keys()
        if locked.get(name) != actual.get(name)
    )
    if changed:
        raise ValueError(
            "API source lock differs: "
            + ", ".join(changed[:10])
            + "; use --update-source-lock after reviewing source changes."
        )


def apply_lock(path: Path, inputs: list[dict], *, update: bool) -> dict:
    """Write only when explicitly requested; ordinary builds verify the pin."""
    sources = input_hashes(inputs)
    if update:
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "sources": sources,
                },
                indent=2,
                sort_keys=True,
            )
            + "\n"
        )
    if not path.exists():
        raise FileNotFoundError("API source lock missing; use --update-source-lock.")
    lock = json.loads(path.read_text())
    verify_inputs(lock["sources"], inputs)
    return lock
