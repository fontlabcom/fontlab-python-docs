# this_file: scripts/archive_search.py
"""Install the verified PythonQt search derivative after legacy archive extraction."""

import hashlib
import json
import re
from pathlib import Path

CONFIG = re.compile(rb'(<script\b[^>]*\bid="__config"[^>]*>)(.*?)(</script>)', re.S)
PAGES = {
    "404.html", "index.html", "PythonQt.html", "PythonQt.private.html",
    *{f"PythonQt.{name}.html" for name in (
        "Qt", "QtCore", "QtGui", "QtOpenGL", "QtSvg", "QtUiTools", "QtXml", "QtXmlPatterns"
    )},
}
ASSETS = "assets/javascripts/workers/archive-search/"
OLD = "assets/javascripts/workers/search.2c215733.min.js"


def install_archive_search(root: Path, archive: Path) -> dict | None:
    """Preflight every original and replacement byte before changing any output.

    Small legacy publisher fixtures without a PythonQt search are unaffected.
    A real PythonQt index requires the entire frozen twelve-page configuration.
    """
    destination = archive / "pythonqt"
    pages = {}
    for page in destination.glob("*.html"):
        content = page.read_bytes()
        matches = list(CONFIG.finditer(content))
        if matches:
            if len(matches) != 1:
                raise ValueError("Ambiguous archived search configuration")
            pages[page.name] = (page, content, matches[0])
    index = destination / "search/search_index.json"
    if not pages and not index.exists():
        return None
    if set(pages) != PAGES:
        raise ValueError("Archived PythonQt page inventory differs")
    source = root / "scripts/archive_search"
    dist = source / "dist"
    receipt = json.loads((dist / "receipt.json").read_bytes())
    if receipt["schema_version"] != 1 or receipt["compiler"] != "esbuild0.25.12" or receipt["lunr"] != "2.3.9":
        raise ValueError("Unsupported archive search build identity")
    if hashlib.sha256((source / "sources.json").read_bytes()).hexdigest() != receipt["sources_sha256"]:
        raise ValueError("Archive search source inventory differs")
    for row in receipt["original"].values():
        if hashlib.sha256((destination / row["path"]).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError("Original archived search asset differs")
    data = json.loads(index.read_bytes())
    if set(data) != {"config", "docs"} or data["config"] != receipt["config"] or len(data["docs"]) != 40713:
        raise ValueError("Unsupported archived search schema or configuration")
    payloads = {}
    if set(receipt["files"]) != {receipt["worker"], receipt["map"], "NOTICE.txt"}:
        raise ValueError("Archive derivative output inventory differs")
    for name, identity in receipt["files"].items():
        if Path(name).name != name:
            raise ValueError("Invalid archive derivative path")
        content = (dist / name).read_bytes()
        if len(content) != identity["bytes"] or hashlib.sha256(content).hexdigest() != identity["sha256"]:
            raise ValueError("Archive derivative checksum differs")
        payloads[name] = content
    worker, mapping = payloads[receipt["worker"]], payloads[receipt["map"]]
    if not worker.endswith(f'//# sourceMappingURL={receipt["map"]}\n'.encode()):
        raise ValueError("Archive derivative map reference differs")
    metadata = json.loads(mapping)
    if not metadata["mappings"] or not metadata["sourcesContent"] or len(metadata["sources"]) != len(metadata["sourcesContent"]):
        raise ValueError("Incomplete archive derivative source map")
    replacements = []
    for page, content, match in pages.values():
        config = json.loads(match[2])
        old = config["search"]
        if old not in {OLD, "/fontlab-python-docs/pythonqt/" + OLD}:
            raise ValueError("Unexpected archived search worker URL")
        token = json.dumps(old).encode()
        if match[2].count(token) != 1:
            raise ValueError("Ambiguous archived search worker URL")
        changed = match[2].replace(token, json.dumps(ASSETS + receipt["worker"]).encode())
        replacements.append((page, content[:match.start(2)] + changed + content[match.end(2):]))
    # All preflight checks above are read-only. Only the derivative and URL values change.
    target = destination / ASSETS
    target.mkdir(parents=True, exist_ok=True)
    for name, content in payloads.items():
        (target / name).write_bytes(content)
    (target / "receipt.json").write_bytes((dist / "receipt.json").read_bytes())
    for page, content in replacements:
        page.write_bytes(content)
    return receipt
