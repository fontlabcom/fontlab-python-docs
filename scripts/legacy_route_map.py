# this_file: scripts/legacy_route_map.py
"""Inventory original legacy links and map only exact public API identities."""

import hashlib
import json
import posixpath
import re
import tarfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class LegacyHTML(HTMLParser):
    """Read identifiers, links and exact heading text without normalizing names."""

    def __init__(self, html: str) -> None:
        super().__init__()
        self.ids = set()
        self.hrefs = set()
        self.headings = {}
        self.heading = None
        self.feed(html)

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs = dict(attrs)
        identifier = attrs.get("id")
        if identifier is not None:
            self.ids.add(identifier)
        if tag == "a" and attrs.get("name") is not None:
            self.ids.add(attrs["name"])
        if attrs.get("href") is not None:
            self.hrefs.add(attrs["href"])
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading = (tag, identifier, [])

    def handle_data(self, data: str) -> None:
        if self.heading:
            self.heading[2].append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.heading and tag == self.heading[0]:
            _, identifier, text = self.heading
            if identifier is not None:
                self.headings[identifier] = "".join(text).strip().rstrip("¶").strip()
            self.heading = None


def original_pages(root: Path) -> dict[str, LegacyHTML]:
    """Read original HTML; publication separately verifies the archive bytes."""
    manifest = json.loads((root / "archive/fontlab7-manifest.json").read_text())
    path = root / "archive/fontlab7-site.tar.gz"
    if hashlib.sha256(path.read_bytes()).hexdigest() != manifest["archive_sha256"]:
        raise ValueError("Legacy archive checksum mismatch")
    with tarfile.open(path) as archive:
        return {
            member.name: LegacyHTML(archive.extractfile(member).read().decode("utf-8"))
            for member in archive
            if member.name.endswith(".html")
        }


def current_targets(coverage: dict) -> dict[str, str]:
    """Reuse exact symbol and public alias URLs from the current inventory."""
    symbols = coverage.get("symbols", {})
    return {
        **{name: row["url"] for name, row in symbols.items()},
        **{
            name: symbols[target]["url"]
            for name, target in coverage.get("aliases", {}).items()
        },
    }


def make_route_map(pages: dict[str, LegacyHTML], coverage: dict) -> dict:
    """Keep every fragment and report unresolved original internal HTML links."""
    targets = current_targets(coverage)
    routes, broken = [], []
    for route, page in sorted(pages.items()):
        archive = "archive/fontlab7/" + route
        identity = route.removesuffix(".html")
        current = targets.get(identity)
        fragments = {}
        for identifier in sorted(page.ids):
            candidates = {
                targets[name]
                for name in (identifier, page.headings.get(identifier))
                if name in targets
            }
            fragments[identifier] = {
                "archive": archive + "#" + identifier,
                "current": next(iter(candidates)) if len(candidates) == 1 else None,
            }
        exact = current is not None or any(row["current"] for row in fragments.values())
        routes.append(
            {
                "old_route": route,
                "archive_route": archive,
                "current_route": current,
                "fragments": fragments,
                "match": "exact-identity" if exact else "archive-only",
                "reason": "Exact qualified name in current public inventory."
                if exact
                else "No exact qualified identity; preserve original archive route and fragments.",
            }
        )
        for href in sorted(page.hrefs):
            link = urlsplit(href)
            if (link.scheme or link.netloc) and (
                link.netloc != "fontlabcom.github.io"
                or not link.path.startswith("/fontlab-python-docs/")
            ):
                continue
            path = link.path.removeprefix("/fontlab-python-docs/")
            if link.path.startswith("/"):
                target = unquote(path.lstrip("/"))
            else:
                target = unquote(urlsplit(urljoin(route, href)).path)
            if not target or target.endswith("/"):
                target += "index.html"
            target = posixpath.normpath(target)
            fragment = unquote(link.fragment)
            if target not in pages and not target.endswith(".html"):
                continue
            if target not in pages or (fragment and fragment not in pages[target].ids):
                broken.append(
                    {
                        "source_route": route,
                        "href": href,
                        "target_route": target,
                        "fragment": fragment,
                        "status": "broken-in-original",
                    }
                )
    return {
        "schema_version": 1,
        "archive_version": "FontLab7",
        "routes": routes,
        "diagnostics": {"broken_in_original": broken},
    }


def write_route_map(root: Path, site: Path, coverage: dict) -> dict:
    report = make_route_map(original_pages(root), coverage)
    (site / "route-map.json").write_text(
        json.dumps(report, sort_keys=True, indent=2) + "\n"
    )
    return report


def verify_route_map(root: Path, site: Path, coverage: dict) -> dict:
    """Recompute completeness from originals, then check rendered archive/redirects."""
    expected = make_route_map(original_pages(root), coverage)
    actual = json.loads((site / "route-map.json").read_text())
    if actual != expected:
        raise ValueError(
            "Legacy route map disagrees with original routes/fragments or current inventory"
        )
    policies = json.loads((site / "legacy-routes.json").read_text())["routes"]
    for row in expected["routes"]:
        route, archive = row["old_route"], row["archive_route"]
        page = LegacyHTML((site / archive).read_text())
        if not set(row["fragments"]) <= page.ids:
            raise ValueError("Missing archived fragment: " + route)
        policy = policies.get(route, {})
        if policy.get("target") != archive or set(
            policy.get("known_fragments", [])
        ) != set(row["fragments"]):
            raise ValueError(
                "Legacy redirect policy disagrees with route map: " + route
            )
        html = (site / route).read_text()
        if route == "404.html":
            continue
        if route == "index.html":
            if (
                json.dumps(archive) not in html
                or json.dumps(policy["known_fragments"]) not in html
                or "target.hash=location.hash;location.replace(target.href)" not in html
                or policy.get("fragment_targets")
                != {
                    identifier: fragment["archive"]
                    for identifier, fragment in row["fragments"].items()
                }
            ):
                raise ValueError("Legacy root redirect disagrees with route map")
        else:
            url = posixpath.relpath(archive, posixpath.dirname(route) or ".")
            if not re.search(
                r"location\.replace\("
                + re.escape(json.dumps(url))
                + r"\+location\.hash\)",
                html,
            ):
                raise ValueError("Legacy redirect disagrees with route map: " + route)
            if ('content="0;url=' + url + '"') not in html:
                raise ValueError(
                    "Legacy meta redirect disagrees with route map: " + route
                )
            if url not in LegacyHTML(html).hrefs:
                raise ValueError(
                    "Legacy redirect fallback disagrees with route map: " + route
                )
    return {
        "routes": len(expected["routes"]),
        "fragments": sum(len(row["fragments"]) for row in expected["routes"]),
        "broken_in_original": len(expected["diagnostics"]["broken_in_original"]),
    }
