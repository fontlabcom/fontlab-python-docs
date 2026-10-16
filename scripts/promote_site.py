# this_file: scripts/promote_site.py
"""Promote the accepted build into docs/, the GitHub Pages source (master:/docs).

Run only after a strict build and every gate have passed. The site must equal the
accepted build manifest before anything in docs/ changes; afterwards docs/ must
equal it too. Finder metadata (.DS_Store) is never copied. Usage:

    uv run python -m scripts.promote_site
    git add docs && uv run python -m scripts.promote_site --verify-tracked
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

from .build_provenance import file_manifest, verify_build

ROOT = Path(__file__).resolve().parents[1]


def _published_paths(root: Path) -> list[str]:
    accepted = json.loads((root / ".build/accepted-build.json").read_bytes())
    return sorted({*accepted["rendered"], "build-provenance.json", ".nojekyll"})


def _git(root: Path, *args: str, stdin: str | None = None) -> subprocess.CompletedProcess:
    # check=False: check-ignore exits 1 when nothing is ignored; callers read the output.
    return subprocess.run(
        ["git", "-C", str(root), *args], input=stdin, capture_output=True, text=True, check=False
    )


def ignored_by_git(root: Path) -> list[str]:
    """Published paths a `git add` would silently skip (empty outside a repository)."""
    if _git(root, "rev-parse", "--is-inside-work-tree").returncode:
        return []
    paths = "\n".join("docs/" + p for p in _published_paths(root)) + "\n"
    result = _git(root, "check-ignore", "--no-index", "--stdin", stdin=paths)
    return sorted(line for line in result.stdout.splitlines() if line)


def verify_tracked(root: Path = ROOT) -> int:
    """After `git add docs`: the index holds exactly the accepted paths under docs/."""
    tracked = set(_git(root, "ls-files", "docs").stdout.split())
    expected = {"docs/" + p for p in _published_paths(root)}
    if tracked != expected:
        missing, extra = sorted(expected - tracked), sorted(tracked - expected)
        raise ValueError(f"git index differs from accepted docs/: missing {missing[:10]}, extra {extra[:10]}")
    return len(tracked)


def promote(root: Path = ROOT) -> dict:
    """Replace docs/ with the accepted site; return the promoted file count."""
    try:
        verify_build(root)
    except ValueError as error:
        raise ValueError(f"Site differs from accepted build; docs/ unchanged ({error})") from error
    ignored = ignored_by_git(root)
    if ignored:
        raise ValueError(f"Published pages ignored by git, docs/ unchanged: {ignored[:10]}")
    site, docs = root / ".build/site", root / "docs"
    accepted = (root / ".build/accepted-build.json").read_bytes()
    # Copy exactly the accepted manifest: anything else in the site (Finder
    # metadata, __pycache__) is never published.
    wanted = [*json.loads(accepted)["rendered"], "build-provenance.json"]
    if docs.exists():
        shutil.rmtree(docs)
    for relative in wanted:
        target = docs / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(site / relative, target)
    (docs / ".nojekyll").touch()
    published = sorted(p.relative_to(docs).as_posix() for p in docs.rglob("*") if p.is_file())
    if published != sorted({*wanted, ".nojekyll"}):
        raise ValueError("Promoted docs/ holds files outside the accepted build")
    if file_manifest(docs, exclude=("build-provenance.json",)) != json.loads(accepted)["rendered"]:
        raise ValueError("Promoted docs/ differs from accepted build")
    if (docs / "build-provenance.json").read_bytes() != accepted:
        raise ValueError("Promoted docs/ provenance differs from accepted build")
    files = sum(1 for path in docs.rglob("*") if path.is_file())
    return {"files": files, "provenance": "build-provenance.json"}


def main() -> int:
    if sys.argv[1:] == ["--verify-tracked"]:  # run after `git add docs`, before committing
        print(json.dumps({"tracked": verify_tracked()}))
        return 0
    report = promote()
    print(json.dumps(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
