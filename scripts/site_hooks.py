# this_file: scripts/site_hooks.py
"""Register complete reference identities and preserve MaterialX search shape."""

import json
import sys
from collections import defaultdict
from pathlib import Path

from properdocs.plugins import event_priority

_coverage = {}
_anchors = defaultdict(list)
_aliases = defaultdict(list)


def on_config(config):
    global _coverage
    _coverage = json.loads((Path(config.docs_dir).parent / "coverage.json").read_text())
    _anchors.clear()
    _aliases.clear()
    root = str(Path(__file__).resolve().parents[1])
    if root not in sys.path:
        sys.path.insert(0, root)
    for identifier, row in _coverage["symbols"].items():
        _anchors[row["url"].split("#")[0]].append(identifier)
    for alias, target in _coverage["aliases"].items():
        _aliases[target].append(alias)


def on_page_markdown(markdown, page, config, files):
    autorefs = config.plugins["autorefs"]
    inventory = config.plugins["mkdocstrings"].handlers.inventory
    for identifier in _anchors.get(page.url, []):
        row = _coverage["symbols"][identifier]
        primary = row["kind"] in {"module", "class"} or row["body_target"] != identifier
        autorefs.register_anchor(page, identifier, identifier, primary=primary)
        inventory.register(identifier, "py", row["kind"], page.url + "#" + identifier)
        for alias in _aliases[identifier]:
            autorefs.register_anchor(page, alias, identifier, primary=primary)
            inventory.register(alias, "py", row["kind"], page.url + "#" + identifier)
    return markdown


@event_priority(-100)
def on_post_build(config):
    path = Path(config.site_dir) / "search/search_index.json"
    data = json.loads(path.read_text())
    from scripts.search_identities import qualify_titles, verify_search_coverage

    qualify_titles(data, _coverage["symbols"], _coverage["aliases"])
    verify_search_coverage(data, _coverage["symbols"], _coverage["aliases"])
    # Keep section identities, avoiding duplicate whole-page body copies.
    section_pages = {
        r["location"].split("#")[0] for r in data["docs"] if "#" in r["location"]
    }
    for row in data["docs"]:
        if row["location"] in section_pages:
            row["text"] = ""
    data["config"].update(
        pipeline=["trimmer"],
        fields={
            "title": {"boost": 1000.0},
            "text": {"boost": 1.0},
            "tags": {"boost": 1000000.0},
        },
    )
    path.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    (Path(config.site_dir) / ".nojekyll").touch()
    from scripts.legacy_archive import publish_archive

    publish_archive(Path(__file__).resolve().parents[1], Path(config.site_dir))
