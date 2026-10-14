# this_file: scripts/legacy_archive.py
"""Publish a verified legacy snapshot and preserve original route fragments."""

import hashlib
import json
import re
import tarfile
from html import escape
from pathlib import Path

from .legacy_route_map import (
    CURRENT_LINK_CLASS,
    CURRENT_LINK_SCRIPT,
    LegacyHTML,
    current_link_targets,
    make_route_map,
    original_pages,
    save_route_map,
)


def current_link(page: str, targets: dict[str, str]) -> str:
    """Visible archive-banner link to the page's exact current identity."""
    return (
        ' · <a class="'
        + CURRENT_LINK_CLASS
        + '" style="color:inherit;font-weight:bold" href="'
        + escape(page, quote=True)
        + '" data-fragment-targets="'
        + escape(json.dumps(targets, sort_keys=True, separators=(",", ":")), quote=True)
        + '">Current version of this page</a>'
        + CURRENT_LINK_SCRIPT
    )


def publish_archive(root: Path, site: Path, coverage: dict | None = None) -> dict:
    """Verify every archived byte before wrapping HTML or creating redirects."""
    manifest = json.loads((root / "archive/fontlab7-manifest.json").read_text())
    archive = root / "archive/fontlab7-site.tar.gz"
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest["archive_sha256"]:
        raise ValueError("Legacy archive checksum mismatch")
    destination = site / "archive/fontlab7"
    routes = {}
    route_map = make_route_map(original_pages(root), coverage or {})
    mapped = {row["old_route"]: row for row in route_map["routes"]}
    with tarfile.open(archive) as data:
        for row in manifest["files"]:
            relative = Path(row["path"])
            if relative.is_absolute() or ".." in relative.parts:
                raise ValueError("Invalid archived path")
            stream = data.extractfile(row["path"])
            content = stream.read()
            if hashlib.sha256(content).hexdigest() != row["sha256"]:
                raise ValueError("Legacy member checksum mismatch: " + row["path"])
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            if relative.suffix == ".html":
                html = content.decode("utf-8")
                fragments = sorted(LegacyHTML(html).ids)
                current = "/".join([".."] * (len(relative.parts) + 1)) + "/index.html"
                link = current_link_targets(mapped[row["path"]])
                banner = (
                    '<div style="padding:1rem;background:#ffe7ad;color:#241900;text-align:center">FontLab7 archive · <a style="color:inherit" href="'
                    + current
                    + '">Current Python reference</a>'
                    + (current_link(*link) if link else "")
                    + "</div>"
                )
                body = re.search(r"<body\b[^>]*>", html)
                if body:
                    html = html[: body.end()] + banner + html[body.end() :]
                elif link:
                    raise ValueError("Archived page has no body for its current link")
                content = html.encode("utf-8")
                routes[row["path"]] = {
                    "target": "archive/fontlab7/" + row["path"],
                    "fragment_policy": "preserve",
                    "known_fragments": fragments,
                    "original_sha256": row["sha256"],
                }
                # Root landing page is current; all other old HTML routes remain reachable.
                if row["path"] not in {"index.html", "404.html"}:
                    old = site / relative
                    if old.exists():
                        raise ValueError(
                            "Legacy redirect would overwrite a current page: "
                            + row["path"]
                        )
                    url = "/".join(
                        [".."] * (len(relative.parts) - 1)
                        + ["archive", "fontlab7", *relative.parts]
                    )
                    redirect = (
                        '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>FontLab7 archive</title><meta http-equiv="refresh" content="0;url='
                        + escape(url, quote=True)
                        + '"></head><body><a href="'
                        + escape(url, quote=True)
                        + '">Archived reference</a><script>location.replace('
                        + json.dumps(url)
                        + "+location.hash)</script></body></html>"
                    )
                    old.parent.mkdir(parents=True, exist_ok=True)
                    old.write_text(redirect)
            target.write_bytes(content)
    if "index.html" in routes:
        route = routes["index.html"]
        route["fragment_policy"] = "known-fragments-only"
        route["unfragmented_policy"] = "current-root"
        route["fragment_targets"] = {
            fragment: route["target"] + "#" + fragment
            for fragment in route["known_fragments"]
        }
        root_page = site / "index.html"
        if not root_page.exists():
            raise ValueError("Current root missing during legacy migration")
        script = (
            "<script>/* Legacy root fragments only; retain current landing page. */"
            "(()=>{const fragments=" + json.dumps(route["known_fragments"]) + ";"
            "function migrate(){const hash=location.hash.slice(1);"
            "if(fragments.includes(hash)){const target=new URL("
            + json.dumps(route["target"])
            + ",location.href);"
            "target.hash=location.hash;location.replace(target.href);}}"
            "addEventListener('hashchange',migrate);migrate();})();</script>"
        )
        html = root_page.read_text()
        if "</body>" not in html:
            raise ValueError("Current root has no body for fragment migration")
        root_page.write_text(html.replace("</body>", script + "</body>"))
    if "404.html" in routes:
        routes["404.html"]["fragment_policy"] = "archive-only"
        routes["404.html"]["unfragmented_policy"] = "current-error-page"
    report = {
        "schema_version": 1,
        "archive_sha256": manifest["archive_sha256"],
        "routes": routes,
    }
    (site / "legacy-routes.json").write_text(
        json.dumps(report, separators=(",", ":")) + "\n"
    )
    save_route_map(site, route_map)
    return report
