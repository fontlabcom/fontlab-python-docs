# this_file: scripts/release_audit.py
"""Privacy and licence audit of the built site, search index and source maps (R044, R055).

Reads every published byte, including gzip members and the zlib body of
objects.inv. Fails on private paths, credentials, e-mail addresses outside the
allowlist, absolute or private source-map sources, and missing licence notices.
"""

from __future__ import annotations

import argparse
import getpass
import gzip
import json
import re
import zlib
from collections import defaultdict
from pathlib import Path

PRIVATE = {
    "user-path": re.compile(rb"/(?:Users|home)/[A-Za-z0-9._-]+/"),
    "temp-path": re.compile(rb"/private/(?:var|tmp)/"),
    "windows-user-path": re.compile(rb"[A-Za-z]:\\\\?Users\\\\?[A-Za-z0-9._-]+"),
    "file-url": re.compile(rb"file:///"),
    "loopback-url": re.compile(rb"https?://(?:localhost|127\.0\.0\.1|0\.0\.0\.0)[:/]"),
    "github-token": re.compile(rb"\bgh[pousr]_[A-Za-z0-9]{36}\b"),
    "api-key": re.compile(rb"\b(?:sk-[A-Za-z0-9]{20,}|AKIA[0-9A-Z]{16})\b"),
    "private-key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
EMAIL = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
SOURCE_MAP_URL = re.compile(rb"sourceMappingURL=([^\s*]+)")
# Addresses that are part of upstream licence texts or public project contacts.
EMAIL_ALLOWLIST = re.compile(rb"@(?:fsf\.org|gnu\.org|qt\.io|qt-project\.org|digia\.com|nokia\.com)$")
# Reviewed public values: upstream examples and attributions, never local data.
# Each is allowed only under the listed published prefixes.
REVIEWED = {
    b"/home/user/": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"/home/bob/": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"/home/petra/": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"/home/mary/": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"/home/jana/": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"C:\\Users\\Bob": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"C:\\Users\\User": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"C:\\\\Users\\\\Bob": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"C:\\\\Users\\\\User": ("Qt reference examples", ("reference/PythonQt/", "search/complete/")),
    b"file:///": ("Qt reference URL-scheme examples", ("reference/PythonQt/", "search/complete/")),
    b"my@content.id": ("Qt QHttpPart example", ("reference/PythonQt/", "search/complete/")),
    b"user@foo.com": ("Qt QDesktopServices example", ("reference/PythonQt/", "search/complete/")),
    b"martin.donath@squidfunk.com": ("MaterialX MIT attribution in source maps", ("archive/fontlab7/", "assets/javascripts/")),
    b"taku@chasen.org": ("TinySegmenter attribution bundled by MaterialX", ("archive/fontlab7/", "assets/javascripts/")),
}


def local_identities() -> list[bytes]:
    """Values that identify the auditing machine; computed, never stored."""
    home = Path.home()
    values = [str(home).encode(), ("/Users/" + getpass.getuser() + "/").encode()]
    values.append(str(Path(__file__).resolve().parents[2]).encode())
    return values


def reviewed(value: bytes, relative: str) -> bool:
    entry = REVIEWED.get(value)
    return bool(entry) and relative.startswith(entry[1])
LICENCES = {
    "Apache-2.0": b"Apache License",
    "GFDL-1.3": b"GNU Free Documentation License",
    "LGPL-3.0": b"GNU LESSER GENERAL PUBLIC LICENSE",
    "MIT": b"Permission is hereby granted, free of charge",
}


def published_bytes(path: Path) -> bytes:
    """Return the bytes a reader can obtain from this file, decompressed."""
    data = path.read_bytes()
    if path.suffix == ".gz":
        return gzip.decompress(data)
    if path.name == "objects.inv":
        header, _, body = data.partition(b"zlib.\n")
        return header + zlib.decompress(body)
    return data


def audit(site: Path) -> dict:
    findings, emails, maps, external = defaultdict(list), defaultdict(list), {}, set()
    allowed = defaultdict(int)
    local = local_identities()
    texts = 0
    for path in sorted(p for p in site.rglob("*") if p.is_file()):
        relative = path.relative_to(site).as_posix()
        data = published_bytes(path)
        texts += 1
        for value in local:
            if value in data:
                findings["local-identity"].append({"file": relative})
        for name, pattern in PRIVATE.items():
            for match in pattern.finditer(data):
                if reviewed(match.group(0), relative):
                    allowed[match.group(0).decode()] += 1
                    continue
                findings[name].append({"file": relative, "match": match.group(0).decode(errors="replace")})
        for match in EMAIL.finditer(data):
            # Licence texts must keep their authors' attribution lines verbatim.
            if relative.startswith("licenses/"):
                continue
            if reviewed(match.group(0), relative):
                allowed[match.group(0).decode()] += 1
                continue
            if not EMAIL_ALLOWLIST.search(match.group(0)):
                emails[match.group(0).decode(errors="replace")].append(relative)
        for match in SOURCE_MAP_URL.finditer(data):
            maps.setdefault(relative, []).append(match.group(1).decode(errors="replace"))
        if path.suffix == ".map":
            source_map = json.loads(data)
            bad = [s for s in source_map.get("sources", []) if s.startswith("/") or "://" in s]
            if bad:
                findings["absolute-source-map-source"].append({"file": relative, "sources": bad})
        if path.suffix == ".html":
            external.update(
                m.decode() for m in re.findall(rb'(?:src|href)="(https?://[^/"]+)', data)
            )
    if emails:
        findings["email-address"] = [{"address": a, "files": f[:5]} for a, f in sorted(emails.items())]
    for referrer, targets in maps.items():
        for target in targets:
            if not (site / Path(referrer).parent / target).exists() and not target.startswith("data:"):
                findings["dangling-source-map"].append({"file": referrer, "target": target})
    notice = site / "licenses.html"
    notice_bytes = notice.read_bytes() if notice.exists() else b""
    licence_texts = b"".join(
        published_bytes(p) for p in (site / "licenses").glob("*.txt")
    ) if (site / "licenses").is_dir() else b""
    missing = [name for name, marker in LICENCES.items() if marker not in licence_texts]
    if not notice_bytes or missing:
        findings["licence-notice"].append({"page": notice.exists(), "missing_texts": missing})
    return {
        "schema_version": 1,
        "files_scanned": texts,
        "source_map_references": maps,
        "external_hosts": sorted(external),
        "reviewed_public_values": {
            value: {"count": count, "reason": REVIEWED[value.encode()][0]}
            for value, count in sorted(allowed.items())
        },
        "findings": dict(findings),
        "pass": not findings,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = audit(args.site)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"pass": report["pass"], "files": report["files_scanned"],
                      "findings": {k: len(v) for k, v in report["findings"].items()}}))
    raise SystemExit(0 if report["pass"] else 1)
