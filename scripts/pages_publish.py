# this_file: scripts/pages_publish.py
"""Normal docs-only publication and immutable X/Y qualification for the public site.

Call with all diagnostics redirected to the private runner directory. A generated
commit must be X itself or its direct docs-only child; Pages is requested only
after its complete rebuild and byte parity, and its actual build must bind Y.
"""

import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

REPOSITORY = "fontlabcom/fontlab-python-docs"
PAGES_ATTEMPTS = 120


def git(root: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(root), *args], check=True,
                          capture_output=True, text=True, timeout=120).stdout.strip()


def remote_main(root: Path) -> str:
    """A failed ls-remote is an error, never an empty/superseded publication."""
    result = git(root, "ls-remote", "--exit-code", "origin", "refs/heads/main").split()
    if len(result) != 2 or result[1] != "refs/heads/main":
        raise ValueError("Unexpected main ref response")
    return result[0]


def output(name: str, value: str) -> None:
    with Path(os.environ["GITHUB_OUTPUT"]).open("a") as stream:
        stream.write(f"{name}={value}\n")


def publish(root: Path, source: str) -> str:
    """Push exactly docs/, preserving an ordinary hook-respecting Git path."""
    if git(root, "rev-parse", "HEAD") != source or git(root, "diff", "--cached", "--name-only"):
        raise ValueError("Unexpected source identity or staged changes")
    changed = git(root, "diff", "--name-only").splitlines()
    if any(not name.startswith("docs/") for name in changed):
        raise ValueError("Source changed during the build")
    if remote_main(root) != source:
        return ""
    git(root, "add", "--", "docs")
    if git(root, "diff", "--cached", "--name-only"):
        git(root, "-c", "user.name=github-actions[bot]", "-c",
            "user.email=41898282+github-actions[bot]@users.noreply.github.com",
            "commit", "-m", "docs: rebuild generated site")
        git(root, "push", "origin", "HEAD:refs/heads/main")
    return git(root, "rev-parse", "HEAD")


def lineage(root: Path, source: str, generated: str) -> None:
    if git(root, "rev-parse", "HEAD") != generated:
        raise ValueError("Generated checkout identity differs")
    if generated != source:
        if git(root, "rev-parse", "HEAD^") != source:
            raise ValueError("Generated output is not the direct source child")
        names = git(root, "diff", "--name-only", source, generated).splitlines()
        if not names or any(not name.startswith("docs/") for name in names):
            raise ValueError("Generated commit contains non-docs changes")


def parity(root: Path) -> None:
    git(root, "diff", "--exit-code", "HEAD", "--", "docs")
    if git(root, "ls-files", "--others", "--exclude-standard", "--", "docs"):
        raise ValueError("Untracked generated output differs")


def api(method: str, endpoint: str) -> dict:
    """Only the current job's repository-scoped GITHUB_TOKEN reaches GitHub."""
    request = urllib.request.Request(
        f"https://api.github.com/repos/{REPOSITORY}/{endpoint}", method=method,
        headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"],
                 "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2026-03-10"},
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        if response.status != (201 if method == "POST" else 200):
            raise ValueError("Unexpected Pages API status")
        return json.load(response)


def pages(root: Path, source: str, generated: str, receipt: Path) -> None:
    lineage(root, source, generated)
    parity(root)
    if api("GET", "pages").get("source") != {"branch": "main", "path": "/docs"}:
        raise ValueError("Pages must use main:/docs")
    if remote_main(root) != generated:
        raise ValueError("Publication superseded by main")
    requested = api("POST", "pages/builds")
    record = {"source": source, "generated": generated, "request": requested}
    receipt.write_text(json.dumps(record, indent=2) + "\n")
    for _ in range(PAGES_ATTEMPTS):
        if remote_main(root) != generated:
            raise ValueError("Pages request superseded by main")
        build = api("GET", "pages/builds/latest")
        record["build"] = build
        receipt.write_text(json.dumps(record, indent=2) + "\n")
        if build.get("commit") == generated:
            if build.get("status") == "built":
                return
            if build.get("status") == "errored":
                raise ValueError("Pages build failed")
        time.sleep(5)
    raise TimeoutError("Exact generated Pages build did not complete")


def main(args: list[str]) -> None:
    root = Path.cwd()
    match args:
        case ["publish", source]:
            output("sha", publish(root, source))
        case ["lineage", source, generated]:
            lineage(root, source, generated)
        case ["parity"]:
            parity(root)
        case ["pages", source, generated, receipt]:
            pages(root, source, generated, Path(receipt))
        case _:
            raise ValueError("Expected publish, lineage, parity or pages arguments")


if __name__ == "__main__":
    main(sys.argv[1:])
