# this_file: scripts/verify_site.py
"""Check complete rendered source identities, inventory and declared budgets."""

import gzip
import hashlib
import json
import re
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path

from mkdocstrings import Inventory


class Anchors(HTMLParser):
    """Use the standard HTML parser to read actual rendered identifiers."""

    def __init__(self):
        super().__init__()
        self.identifiers = set()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key == "id":
                self.identifiers.add(value)


# Optional native modules the captured host did not ship (D8): documented as absent.
REVIEWED_ABSENT_PACKAGES = {"fontlabpr": "absent from FontLab 9.0.9780; documented as absent (D8)"}
HEADING = re.compile(r'class="doc doc-heading')
DOCSTRING = re.compile(r'class="doc doc-contents[^"]*">\s*<p>')


def package_content_problems(site: Path, packages: list[str]) -> list[dict]:
    """Every documented package renders members and docstrings, never an empty page.

    Packages that only import inside FontLab are documented from Echopy captures or
    static source; this gate catches any path that would silently render nothing.
    """
    problems = []
    for package in packages:
        page = site / "reference" / f"{package}.html"
        if not page.exists():
            problems.append({"package": package, "problem": "missing page"})
            continue
        if package in REVIEWED_ABSENT_PACKAGES:
            continue
        folder = site / "reference" / package
        pages = [page, *(sorted(folder.rglob("*.html")) if folder.is_dir() else [])]
        html = "".join(path.read_text() for path in pages)
        if not HEADING.search(html):
            problems.append({"package": package, "problem": "no rendered members"})
        elif not DOCSTRING.search(html):
            problems.append({"package": package, "problem": "no docstrings"})
    return problems


def verify_site(
    site: Path, coverage_path: Path, *, legacy_root: Path | None = None
) -> dict:
    """Fail when any expected source symbol/alias lacks rendered proof."""
    coverage = json.loads(coverage_path.read_text())
    from .legacy_route_map import verify_route_map

    legacy = verify_route_map(
        legacy_root or Path(__file__).resolve().parents[1], site, coverage
    )
    wanted = defaultdict(set)
    for identifier, row in coverage["symbols"].items():
        url = (
            row["body_url"]
            if row["body_target"] == identifier
            and row["kind"] not in {"module", "class"}
            else row["url"]
        )
        path, _, fragment = url.partition("#")
        wanted[path].add(fragment)
    with (site / "objects.inv").open("rb") as stream:
        inventory = Inventory.parse_sphinx(stream)
    expected = set(coverage["symbols"]) | set(coverage["aliases"])
    absent_inventory = expected - set(inventory)
    for identifier in expected - absent_inventory:
        path, _, fragment = inventory[identifier].uri.partition("#")
        wanted[path].add(fragment)
    missing = []
    sizes = {}
    for relative, identifiers in wanted.items():
        path = site / relative
        if not path.exists():
            missing.append({"page": relative, "missing_file": True})
            continue
        html = path.read_text()
        if "/Users/adam/" in html:
            raise ValueError("Private path in published reference: " + relative)
        parser = Anchors()
        parser.feed(html)
        absent = identifiers - parser.identifiers
        if absent:
            missing.append({"page": relative, "missing_ids": sorted(absent)})
        sizes[relative] = path.stat().st_size
    largest = max(sizes.values(), default=0)
    search = (site / "search/search_index.json").read_bytes()
    compressed = len(gzip.compress(search, mtime=0))
    search_data = json.loads(search)
    sharding = None
    if "complete" in search_data.get("config", {}):
        from .search_identities import verify_search_coverage
        from .search_shards import inspect_shards, read_complete_index

        complete = read_complete_index(site / "search/search_index.json")
        verify_search_coverage(complete, coverage["symbols"], coverage["aliases"])
        sharding = inspect_shards(site / "search/search_index.json", deployed=True)
        compressed = sharding["initial_gzip_bytes"]
    packages = sorted({identifier.split(".")[0] for identifier in coverage["symbols"]})
    content_problems = package_content_problems(site, packages)
    report = {
        "schema_version": 1,
        "documented_packages": packages,
        "package_content_problems": content_problems,
        "legacy_routes": legacy,
        "source_symbols": len(coverage["symbols"]),
        "aliases": len(coverage["aliases"]),
        "checked_pages": len(wanted),
        "missing_anchors": missing,
        "missing_inventory": sorted(absent_inventory),
        "largest_api_page_bytes": largest,
        "search_bytes": sharding["aggregate_bytes"] if sharding else len(search),
        "search_gzip_bytes": compressed,
        "initial_search_static_bytes": sharding["initial_static_bytes"]
        if sharding
        else None,
        "aggregate_search_gzip_bytes": sharding["aggregate_gzip_bytes"]
        if sharding
        else compressed,
        "search_rows": sharding["rows"] if sharding else len(search_data["docs"]),
        "search_sharding": sharding,
        "page_budget_bytes": 2 * 1024 * 1024,
        "search_gzip_budget_bytes": (5 if sharding else 7) * 1024 * 1024,
        "initial_search_gzip_budget_bytes": 5 * 1024 * 1024,
        "search_budget_status": "complete explicit-gzip routing plus uncompressed bootstrap/worker/UI"
        if sharding
        else "historical monolithic provisional budget",
        "coverage_sha256": hashlib.sha256(coverage_path.read_bytes()).hexdigest(),
    }
    report["passed"] = (
        not missing
        and not content_problems
        and not absent_inventory
        and largest <= report["page_budget_bytes"]
        and compressed <= report["search_gzip_budget_bytes"]
        and (
            not sharding
            or sharding["initial_static_bytes"]
            <= report["initial_search_gzip_budget_bytes"]
        )
    )
    (site.parent / "site-verification.json").write_text(
        json.dumps(report, indent=2) + "\n"
    )
    print(
        json.dumps(
            {
                k: v
                for k, v in report.items()
                if k not in {"missing_anchors", "missing_inventory"}
            },
            indent=2,
        )
    )
    if not report["passed"]:
        raise ValueError(
            "Rendered coverage/inventory/page/search acceptance failed; see site-verification.json"
        )
    return report
