# this_file: scripts/pages_inputs.py
"""Materialize the reviewed CI packet and qualify the bounded D40 audit result.

All output and diagnostics from this module belong in private ephemeral files.
The unchanged release auditor retains its actual exit status and full findings.
"""

import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

ARCHIVE = "inputs-be7df9c8dc66.tar.gz"
NAMES = "private-repository-names.json"
HASHES = {
    ARCHIVE: "b499e0ba639bb23eeac10525b902f85d821bcd8558fb5aec892b94ce5cf5c9aa",
    NAMES: "9aaf92ea8816ed59c604d537a3626ee907137f722b753e64323d64529889d15a",
}
REVIEWED_NAME_DIGEST = "be75b7ba5b4d"


def prepare(store: Path, target: Path) -> None:
    """Hash both private inputs before extracting the already-reviewed archive."""
    for name, expected in HASHES.items():
        if hashlib.sha256((store / name).read_bytes()).hexdigest() != expected:
            raise ValueError("Private input digest differs")
    data = json.loads((store / NAMES).read_text())
    names = data.get("private_slugs", [])
    if (data.get("schema_version") != 1 or len(names) != 13 or len(set(names)) != 13
            or not all(isinstance(name, str) and re.fullmatch(r"fontlabcom/[a-z0-9-]+", name) for name in names)):
        raise ValueError("Private audit inventory differs")
    inputs = target / "inputs"
    inputs.mkdir(parents=True)
    with tarfile.open(store / ARCHIVE) as archive:
        archive.extractall(inputs, filter="data")
    # No live sibling discovery: the unchanged auditor sees only approved names.
    for index, slug in enumerate([*names, "fontlabcom/fontlab-python-docs-inputs"]):
        config = target / "audit" / str(index) / ".git/config"
        config.parent.mkdir(parents=True)
        config.write_text(f'[remote "origin"]\nurl = https://github.com/{slug}.git\n')


def disposition(report: dict, raw_exit: int) -> None:
    """Accept exactly the three reviewed installation-name surfaces, without waiver drift."""
    findings = report["findings"]
    rows = findings.get("private-repository-name", [])
    if raw_exit != 1 or report["pass"] is not False or set(findings) != {"private-repository-name"} or len(rows) != 3:
        raise ValueError("Release audit differs from the reviewed non-green result")
    if any(hashlib.sha256(row["match"].encode()).hexdigest()[:12] != REVIEWED_NAME_DIGEST for row in rows):
        raise ValueError("Unreviewed private name")
    paths = {row["file"] for row in rows}
    shards = [path for path in paths if re.fullmatch(r"search/complete/rows-[a-f0-9]{64}\.json", path)]
    if len(shards) != 1 or paths != {"packages/plugmix.html", shards[0], shards[0] + ".gz"}:
        raise ValueError("Unreviewed audit surface")


def capture(site: Path, workspace: Path, output: Path) -> int:
    """Preserve the raw oracle result in runner-private diagnostics, including exit 1."""
    from .release_audit import audit, receipt

    report = audit(site, workspace=workspace)
    output.write_text(json.dumps(report, indent=2) + "\n")
    output.with_suffix(".redacted.json").write_text(json.dumps(receipt(report), indent=2) + "\n")
    return 0 if report["pass"] else 1


def main(args: list[str]) -> int:
    match args:
        case ["prepare", store, target]:
            prepare(Path(store), Path(target))
        case ["capture", site, workspace, output]:
            return capture(Path(site), Path(workspace), Path(output))
        case ["disposition", report, raw_exit]:
            disposition(json.loads(Path(report).read_text()), int(raw_exit))
        case _:
            raise ValueError("Expected prepare, capture or disposition arguments")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
