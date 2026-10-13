# this_file: scripts/source_lock.py
"""Pin the exact API source bytes across checkout and installed-artifact builds."""

import json
from pathlib import Path


def verify_inputs(locked: dict[str, str], inputs: list[dict]) -> None:
    """Fail for missing, new or modified source; never silently refresh a lock."""
    actual = {row["source"]: row["sha256"] for row in inputs}
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
    if update:
        path.write_text(
            json.dumps(
                {
                    "schema_version": 1,
                    "sources": {row["source"]: row["sha256"] for row in inputs},
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
