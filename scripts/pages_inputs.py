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

ARCHIVE = "inputs-282d9761d557.tar.gz"
NAMES = "private-repository-names.json"
HASHES = {
    ARCHIVE: "282d9761d5576f014ab67f8e7ae911bf3f3d8635d7b7b1fd2f6515a65f352b3d",
    NAMES: "9aaf92ea8816ed59c604d537a3626ee907137f722b753e64323d64529889d15a",
}


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
    """Accept only a green release audit; no reviewed waiver remains.

    The former plugmix installation-name waiver ended when plugmix became a
    documented package (issue 257); any finding now fails the build.
    """
    if raw_exit != 0 or report.get("pass") is not True or any(report.get("findings", {}).values()):
        raise ValueError("Release audit is not green")


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
