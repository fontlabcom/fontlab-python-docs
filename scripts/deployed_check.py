# this_file: scripts/deployed_check.py
"""Verify a deployed site against the local accepted build (R042, R044).

Compares build provenance bytes, every legacy route, a deterministic page
sample and every search asset with the local `.build/site`, records response
headers, and checks that a missing page returns 404 under the URL prefix.
Browser behaviour (fragments, search, navigation) is `interaction_check --base`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import urllib.error
import urllib.request
from pathlib import Path

HEADERS = ("content-type", "content-encoding", "cache-control", "content-length")
SAMPLE_EVERY = 50  # one reference page in fifty, by sorted path
# Acceptable media types by suffix; the search worker decodes explicit `.gz`
# itself, so a host must not also mark those files Content-Encoding: gzip.
TYPES = {
    ".html": ("text/html",),
    ".js": ("text/javascript", "application/javascript"),
    ".css": ("text/css",),
    ".json": ("application/json",),
    ".gz": ("application/gzip", "application/x-gzip", "application/octet-stream"),
    ".svg": ("image/svg+xml",),
    ".png": ("image/png",),
    ".woff2": ("font/woff2",),
    ".xml": ("application/xml", "text/xml"),
    ".txt": ("text/plain",),
}


def header_problem(relative: str, header: dict[str, str]) -> str | None:
    """Why a response's headers would break the browser for this asset, if they would."""
    encoding = (header.get("content-encoding") or "identity").lower()
    if relative.endswith(".gz") and encoding != "identity":
        return f"content-encoding {encoding} on an explicit .gz asset"
    if encoding != "identity":
        return f"content-encoding {encoding} despite Accept-Encoding: identity"
    expected = TYPES.get(Path(relative).suffix)
    media = (header.get("content-type") or "").split(";")[0].strip().lower()
    if expected and media not in expected:
        return f"content-type {media or 'missing'}"
    return None


def fetch(url: str) -> tuple[int, dict[str, str], bytes]:
    request = urllib.request.Request(url, headers={"Accept-Encoding": "identity"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            headers = {k.lower(): v for k, v in response.headers.items()}
            return response.status, headers, response.read()
    except urllib.error.HTTPError as error:
        return error.code, {k.lower(): v for k, v in error.headers.items()}, b""


def targets(site: Path) -> list[str]:
    """Pages and assets whose deployed bytes must equal the local build."""
    routes = json.loads((site / "route-map.json").read_text())["routes"]
    pages = sorted(
        p.relative_to(site).as_posix() for p in (site / "reference").rglob("*.html")
    )
    # Every search shard plus every theme/worker/UI asset the pages load.
    assets = sorted(
        p.relative_to(site).as_posix()
        for folder in ("search", "assets")
        for p in (site / folder).rglob("*")
        if p.is_file() and p.name != ".DS_Store"
    )
    fixed = [
        "index.html",
        "licenses.html",
        "build-info.json",
        "build-provenance.json",
        "route-map.json",
        "objects.inv",
        "sitemap.xml",
    ]
    legacy = sorted({r["old_route"] for r in routes} | {r["archive_route"] for r in routes})
    return [t for t in fixed if (site / t).exists()] + legacy + pages[::SAMPLE_EVERY] + assets


def check(base: str, site: Path) -> dict:
    base = base.rstrip("/") + "/"
    failures, headers = [], {}
    for relative in targets(site):
        status, header, body = fetch(base + relative)
        if status != 200:
            failures.append({"path": relative, "status": status})
            continue
        if hashlib.sha256(body).digest() != hashlib.sha256((site / relative).read_bytes()).digest():
            failures.append({"path": relative, "reason": "bytes differ from local build"})
        problem = header_problem(relative, header)
        if problem:
            failures.append({"path": relative, "reason": problem})
        suffix = "".join(Path(relative).suffixes[-2:]) if relative.endswith(".gz") else Path(relative).suffix
        headers.setdefault(suffix, {k: header.get(k) for k in HEADERS})
    status, _, _ = fetch(base + "no-such-page-r042.html")
    if status != 404:
        failures.append({"path": "no-such-page-r042.html", "status": status, "expected": 404})
    return {
        "schema_version": 1,
        "base": base,
        "checked": len(targets(site)),
        "headers_by_suffix": headers,
        "failures": failures,
        "passed": not failures,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    report = check(args.base, args.site)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"passed": report["passed"], "checked": report["checked"],
                      "failures": len(report["failures"])}))
    raise SystemExit(0 if report["passed"] else 1)
