# this_file: scripts/verify_site.py
"""Check complete rendered source identities, inventory and declared budgets."""

import gzip
import hashlib
import json
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


def verify_site(site: Path, coverage_path: Path) -> dict:
    """Fail when any expected source symbol/alias lacks rendered proof."""
    coverage = json.loads(coverage_path.read_text())
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
    report = {
        "schema_version": 1,
        "source_symbols": len(coverage["symbols"]),
        "aliases": len(coverage["aliases"]),
        "checked_pages": len(wanted),
        "missing_anchors": missing,
        "missing_inventory": sorted(absent_inventory),
        "largest_api_page_bytes": largest,
        "search_bytes": len(search),
        "search_gzip_bytes": compressed,
        "page_budget_bytes": 2 * 1024 * 1024,
        "search_gzip_budget_bytes": 7 * 1024 * 1024,
        "initial_search_gzip_budget_bytes": 5 * 1024 * 1024,
        "search_budget_status": "provisional; complete index sharding remains required",
        "coverage_sha256": hashlib.sha256(coverage_path.read_bytes()).hexdigest(),
    }
    report["passed"] = (
        not missing
        and not absent_inventory
        and largest <= report["page_budget_bytes"]
        and compressed <= report["search_gzip_budget_bytes"]
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
