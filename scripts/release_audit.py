# this_file: scripts/release_audit.py
"""Privacy and licence audit of the built site, search index and source maps (R044, R055).

Reads every published byte: gzip members, the zlib body of objects.inv, inline
`data:` source maps, and JSON-escaped strings (`\\/`). Fails on local or mounted
paths, credentials, unreviewed e-mail addresses, private repository URLs, checkout
paths and names, absolute source-map sources, and licence texts that differ from
their reviewed digests or are not linked from the licences page.

Private repository names come from the local workspace's git remotes at audit
time, so this public script never lists them.
"""

from __future__ import annotations

import argparse
import base64
import configparser
import getpass
import gzip
import hashlib
import json
import re
import sys
import zlib
from collections import defaultdict
from pathlib import Path

PRIVATE = {
    "user-path": re.compile(rb"/(?:Users|home)/[A-Za-z0-9._-]+/"),
    "temp-path": re.compile(rb"/private/(?:var|tmp)/"),
    "volume-path": re.compile(rb"/Volumes/[^/\s\"'<>]+/"),
    "windows-user-path": re.compile(rb"[A-Za-z]:\\\\?Users\\\\?[A-Za-z0-9._-]+"),
    "file-url": re.compile(rb"file:///[^\s\"'<>)\]\\,;`&]*"),
    "loopback-url": re.compile(rb"https?://(?:localhost|127\.0\.0\.1|0\.0\.0\.0)[:/]"),
    "checkout-path": re.compile(
        rb"(?:vcs\d*/github\.[a-z]+/|\.worktrees/"
        rb"|\b(?:fontlab-[a-z0-9-]+|pythonqtside|typerig-lib)/(?:src|Lib|tests)/)"
    ),
    # Current published formats; synthetic negatives live in the tests.
    "credential": re.compile(
        rb"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{22,}"
        rb"|glpat-[A-Za-z0-9_-]{20,}|xox[abposr]-[A-Za-z0-9-]{10,}"
        rb"|AIza[0-9A-Za-z_-]{35}|sk-(?:ant-|proj-)?[A-Za-z0-9_-]{20,}"
        rb"|(?:AKIA|ASIA)[0-9A-Z]{16}|(?:sk|rk)_live_[0-9A-Za-z]{20,}"
        rb"|npm_[A-Za-z0-9]{36}|pypi-AgEIcHlwaS5vcmc[A-Za-z0-9_-]{50,})"
    ),
    "private-key": re.compile(rb"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}
EMAIL = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")
SOURCE_MAP_URL = re.compile(rb"sourceMappingURL=([^\s*]+)")
INLINE_MAP = re.compile(rb"data:application/json;(?:charset=[^;,]+;)?base64,([A-Za-z0-9+/=]+)")
REPOSITORY_URL = re.compile(rb"github\.com[/:](fontlabcom|fontlaborg)/([A-Za-z0-9_-]+(?:\.(?!git\b)[A-Za-z0-9_-]+)*)")
# Reviewed public repositories that the site may link (visibility checked with gh api).
PUBLIC_REPOSITORIES = {
    "fontlabcom/extend-fontlab",
    "fontlabcom/fontlab-python-docs",
    "fontlabcom/fontlab-python-examples",
    "fontlabcom/typerig-lib",
}
# Addresses that are part of upstream licence texts or public project contacts.
EMAIL_ALLOWLIST = re.compile(rb"@(?:fsf\.org|gnu\.org|qt\.io|qt-project\.org|digia\.com|nokia\.com)$")
_QT = ("reference/PythonQt/", "search/complete/")
_THEME = ("archive/fontlab7/", "assets/javascripts/")
# Reviewed public values: exact upstream examples and attributions in scope.
REVIEWED = {
    **{
        path.encode(): ("Qt reference examples", _QT)
        for path in ("/home/user/", "/home/bob/", "/home/petra/", "/home/mary/", "/home/jana/")
    },
    **{
        value: ("Qt reference examples", _QT)
        for value in (b"C:\\Users\\Bob", b"C:\\Users\\User", b"C:\\\\Users\\\\Bob", b"C:\\\\Users\\\\User")
    },
    **{
        url.encode(): ("Qt reference URL-scheme examples", _QT)
        for url in (
            "file:///home/user/test.html",
            "file:///home/user/file.txt",
            "file:///home/user/schema.xsd",
            "file:///path/to/content",
            "file:///path/to/content/",
            "file:///path/to/content/index.html",
            "file:///path/to/content/images",
            "file:///path/to/content/images/",
            "file:///path/to/content/images/logo.png",
            "file:///path/to/images/logo.png",
            "file:///books/returnOfTheKing.doc",
            "file:///books/returnoftheking.doc",
            "file:///C:/Program",
            "file:///c:/program",
        )
    },
    b"my@content.id": ("Qt QHttpPart example", _QT),
    b"user@foo.com": ("Qt QDesktopServices example", _QT),
    b"martin.donath@squidfunk.com": ("MaterialX MIT attribution in source maps", _THEME),
    b"taku@chasen.org": ("TinySegmenter attribution bundled by MaterialX", _THEME),
}
# Reviewed full licence texts published under licenses/ (sha256 of each file).
LICENCES = {
    "apache-2.0.txt": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "bsd-3-clause-fontlabapp.txt": "bc64fab3ef02924c5e0862040b0a1bbdb67ac59e212bff9b434760430586c571",
    "bsd-3-clause-grablab.txt": "5ebc71a38083ce935885617c652696f5c37fcea106fffa2bfc95b3cb96568caa",
    "gfdl-1.3.txt": "ed8742a95cb9db653a09b050e27ccff5e67ba69c14aa2c3137f2a4e1892f6c0d",
    "gpl-3.0.txt": "245248009fd0af1725d183248380e476c1283383909358a13686606352bf2a17",
    "lgpl-3.0.txt": "9ae1959e86bd49b9680f78e0b49d4e52ae88a3f234d497e175e42a7e8ed59216",
    "mit-glyport.txt": "17597656a8b983a8c62d1d7cfbeaefb30e4874b92d99e45b63cd5278ff1e3801",
    "mit-lunr.txt": "8e8d3a860e35aa6bae65287a63f1a3642a79847e0ec0b2627c6ec258fe56988c",
    "mit-materialx.txt": "e1150f26b4c0f872627b39fda49ae3bd850304f2f7f3171ae0531c1f8f4dd078",
    "mpl-2.0-typerig.txt": "3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04",
}
ROOT = Path(__file__).resolve().parents[1]


def local_identities() -> list[bytes]:
    """Values that identify the auditing machine; computed, never stored."""
    home = Path.home()
    values = [str(home).encode(), ("/Users/" + getpass.getuser() + "/").encode()]
    values.append(str(ROOT.parent).encode())
    return values


def private_repository_names(workspace: Path, documented: set[str]) -> set[bytes]:
    """Names of local git remotes that are neither public nor documented packages."""
    names = set()
    for config in workspace.glob("*/.git/config"):
        parser = configparser.ConfigParser(strict=False)
        try:
            parser.read(config)
        except configparser.Error:
            continue
        for section in parser.sections():
            url = parser[section].get("url", "")
            match = REPOSITORY_URL.search(url.encode())
            if match:
                slug = (match[1] + b"/" + match[2]).decode().lower()
                if slug not in PUBLIC_REPOSITORIES and match[2].decode() not in documented:
                    names.add(match[2])
    return names


def reviewed(value: bytes, relative: str) -> bool:
    entry = REVIEWED.get(value)
    return bool(entry) and relative.startswith(entry[1])


def published_bytes(path: Path) -> bytes:
    """Return the bytes a reader can obtain from this file, decompressed."""
    data = path.read_bytes()
    if path.suffix == ".gz":
        return gzip.decompress(data)
    if path.name == "objects.inv":
        header, _, body = data.partition(b"zlib.\n")
        return header + zlib.decompress(body)
    return data


ESCAPE = re.compile(rb"\\u([0-9a-fA-F]{4})|\\(/)")


def unescape(data: bytes) -> bytes:
    """Decode JSON/JavaScript `\\uXXXX` and `\\/` escapes inside any text."""
    return ESCAPE.sub(
        lambda m: chr(int(m[1], 16)).encode("utf-8", "replace") if m[1] else b"/", data
    )


def json_strings(value: object) -> list[str]:
    """Every string (keys too) in parsed JSON, already escape-decoded by the parser."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        return [s for k, v in value.items() for s in (k, *json_strings(v))]
    if isinstance(value, list):
        return [s for item in value for s in json_strings(item)]
    return []


def decoded_forms(raw: bytes) -> list[bytes]:
    """The text a reader can recover: raw, escape-decoded, and parsed JSON strings."""
    forms = [raw, unescape(raw)]
    try:
        forms.append("\n".join(json_strings(json.loads(raw))).encode())
    except (ValueError, UnicodeDecodeError):
        pass
    return forms


def _source_map_problems(source_map: dict) -> list[str]:
    sources = list(source_map.get("sources", [])) + [source_map.get("sourceRoot") or ""]
    return [s for s in sources if s and (s.startswith("/") or "://" in s)]


def audit(site: Path, *, licences: dict[str, str] = LICENCES, workspace: Path | None = None) -> dict:
    if str(ROOT) not in sys.path:  # Also runnable as a plain script.
        sys.path.insert(0, str(ROOT))
    from scripts.build_reference import PACKAGES

    workspace = ROOT.parent if workspace is None else workspace
    private_names = private_repository_names(workspace, set(PACKAGES))
    private_name = (
        re.compile(rb"\b(?:" + b"|".join(re.escape(n) for n in sorted(private_names)) + rb")\b")
        if private_names
        else None
    )
    findings, emails, maps, external = defaultdict(list), defaultdict(list), {}, set()
    allowed = defaultdict(int)
    local = local_identities()
    seen: set[tuple[str, str, bytes]] = set()

    def record(category: str, relative: str, match: bytes) -> None:
        if (category, relative, match) in seen:  # Same text found in two decoded forms.
            return
        seen.add((category, relative, match))
        # Full detail stays in memory; receipt() redacts before anything is written.
        findings[category].append({"file": relative, "match": match.decode(errors="replace")})
    files = 0
    for path in sorted(p for p in site.rglob("*") if p.is_file()):
        relative = path.relative_to(site).as_posix()
        raw = published_bytes(path)
        files += 1
        decoded = decoded_forms(raw)
        for match in INLINE_MAP.finditer(raw):
            inline = base64.b64decode(match[1])
            decoded += decoded_forms(inline)
            bad = _source_map_problems(json.loads(inline))
            if bad:
                findings["absolute-source-map-source"].append({"file": relative, "sources": bad})
        if path.suffix == ".map":
            bad = _source_map_problems(json.loads(raw))
            if bad:
                findings["absolute-source-map-source"].append({"file": relative, "sources": bad})
        per_form: list[defaultdict] = []
        for data in decoded:
            found = defaultdict(int)
            per_form.append(found)
            for value in local:
                if value in data and ("local-identity", relative, b"") not in seen:
                    seen.add(("local-identity", relative, b""))
                    findings["local-identity"].append({"file": relative})
            for name, pattern in PRIVATE.items():
                for match in pattern.finditer(data):
                    if reviewed(match.group(0), relative):
                        found[match.group(0).decode()] += 1
                        continue
                    record(name, relative, match.group(0))
            for match in REPOSITORY_URL.finditer(data):
                slug = (match[1] + b"/" + match[2]).decode().lower()
                if slug not in PUBLIC_REPOSITORIES:
                    record("private-repository-url", relative, match.group(0))
            if private_name:
                for match in private_name.finditer(data):
                    record("private-repository-name", relative, match.group(0))
            if not relative.startswith("licenses/"):  # Licence texts keep author lines.
                for match in EMAIL.finditer(data):
                    if reviewed(match.group(0), relative):
                        found[match.group(0).decode()] += 1
                    elif not EMAIL_ALLOWLIST.search(match.group(0)):
                        emails[match.group(0).decode(errors="replace")].append(relative)
        for value in {v for form in per_form for v in form}:
            allowed[value] += max(form.get(value, 0) for form in per_form)
        for match in SOURCE_MAP_URL.finditer(raw):
            target = match.group(1).decode(errors="replace")
            if target.startswith("data:"):
                continue  # Decoded and checked above.
            if not (site / Path(relative).parent / target).exists():
                findings["dangling-source-map"].append({"file": relative, "target": target})
            maps.setdefault(relative, []).append(target)
        if path.suffix == ".html":
            external.update(m.decode() for m in re.findall(rb'(?:src|href)="(https?://[^/"]+)', raw))
    if emails:
        findings["email-address"] = [{"address": a, "files": f[:5]} for a, f in sorted(emails.items())]
    page = site / "licenses.html"
    linked = set(re.findall(r'href="(?:\./)?licenses/([^"#?]+)"', page.read_text())) if page.exists() else set()
    for name, digest in sorted(licences.items()):
        text = site / "licenses" / name
        if not text.exists():
            findings["licence"].append({"file": name, "problem": "missing"})
            continue
        if hashlib.sha256(text.read_bytes()).hexdigest() != digest:
            findings["licence"].append({"file": name, "problem": "digest-differs"})
        if name not in linked:
            findings["licence"].append({"file": name, "problem": "not-linked"})
    for name in sorted(linked - set(licences)):
        findings["licence"].append({"file": name, "problem": "linked-but-unreviewed"})
    return {
        "schema_version": 2,
        "files_scanned": files,
        "source_map_references": maps,
        "external_hosts": sorted(external),
        "private_repository_names_checked": len(private_names),
        "reviewed_public_values": {
            value: {"count": count, "reason": REVIEWED[value.encode()][0]}
            for value, count in sorted(allowed.items())
        },
        "findings": dict(findings),
        "pass": not findings,
    }


# Fields of a finding that can carry site text, paths or names.
SENSITIVE_FIELDS = {"match", "file", "address", "files", "sources", "target"}


def redact(text: str) -> str:
    """The single redaction used for receipts: a stable digest, never the text."""
    return "redacted:" + hashlib.sha256(text.encode()).hexdigest()[:12]


def receipt(report: dict) -> dict:
    """Report safe to write to disk: every finding field and filename redacted.

    Public, reviewed data (counts, categories, reviewed example values, external
    hosts of the published theme) stays; use `--reveal` to see findings.
    """

    def clean(value):
        if isinstance(value, list):
            return [clean(item) for item in value]
        return redact(value) if isinstance(value, str) else value

    findings = {
        category: [
            {key: clean(value) if key in SENSITIVE_FIELDS else value for key, value in row.items()}
            for row in rows
        ]
        for category, rows in report["findings"].items()
    }
    return {
        **report,
        "findings": findings,
        "source_map_references": {
            redact(page): [redact(target) for target in targets]
            for page, targets in report["source_map_references"].items()
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--workspace", type=Path, help="Folder of sibling git checkouts")
    parser.add_argument(
        "--reveal", action="store_true", help="Print unredacted findings to stderr only"
    )
    args = parser.parse_args(argv)
    report = audit(args.site, workspace=args.workspace)
    args.out.write_text(json.dumps(receipt(report), indent=2, sort_keys=True) + "\n")
    if args.reveal:
        print(json.dumps(report["findings"], indent=2, sort_keys=True), file=sys.stderr)
    print(json.dumps({"pass": report["pass"], "files": report["files_scanned"],
                      "findings": {k: len(v) for k, v in report["findings"].items()}}))
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
