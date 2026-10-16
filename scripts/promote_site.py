# this_file: scripts/promote_site.py
"""Promote the accepted build into docs/, the GitHub Pages source (master:/docs).

Run only after a strict build and every gate have passed. The site must equal the
accepted build manifest before anything in docs/ changes; afterwards docs/ must
equal it too. Finder metadata (.DS_Store) is never copied. Usage:

    uv run python -m scripts.promote_site
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

from .build_provenance import file_manifest, verify_build

ROOT = Path(__file__).resolve().parents[1]


def promote(root: Path = ROOT) -> dict:
    """Replace docs/ with the accepted site; return the promoted file count."""
    try:
        verify_build(root)
    except ValueError as error:
        raise ValueError(f"Site differs from accepted build; docs/ unchanged ({error})") from error
    site, docs = root / ".build/site", root / "docs"
    accepted = (root / ".build/accepted-build.json").read_bytes()
    if docs.exists():
        shutil.rmtree(docs)
    shutil.copytree(site, docs, ignore=shutil.ignore_patterns(".DS_Store"))
    (docs / ".nojekyll").touch()
    if file_manifest(docs, exclude=("build-provenance.json",)) != json.loads(accepted)["rendered"]:
        raise ValueError("Promoted docs/ differs from accepted build")
    if (docs / "build-provenance.json").read_bytes() != accepted:
        raise ValueError("Promoted docs/ provenance differs from accepted build")
    files = sum(1 for path in docs.rglob("*") if path.is_file())
    return {"files": files, "provenance": "build-provenance.json"}


def main() -> int:
    report = promote()
    print(json.dumps(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
