# this_file: scripts/archive_search.py
"""Install the verified PythonQt search derivative after legacy archive extraction."""

import hashlib
import json
import re
from pathlib import Path

CONFIG = re.compile(rb'(<script\b[^>]*\bid="__config"[^>]*>)(.*?)(</script>)', re.DOTALL)
PAGES = {
    "404.html", "index.html", "PythonQt.html", "PythonQt.private.html",
    *{f"PythonQt.{name}.html" for name in (
        "Qt", "QtCore", "QtGui", "QtOpenGL", "QtSvg", "QtUiTools", "QtXml", "QtXmlPatterns"
    )},
}
ASSETS = "assets/javascripts/workers/archive-search/"
OLD = "assets/javascripts/workers/search.2c215733.min.js"
UI_ASSETS = "assets/javascripts/archive-ui/"
UI_OLD = "assets/javascripts/bundle.1a8646e9.min.js"
SCRIPT = re.compile(rb'<script\b[^>]*\bsrc="([^"]+)"[^>]*>')
LINK = re.compile(rb"<link\b[^>]*>")
HREF = re.compile(rb'\shref="([^"]+)"')
NOT_FOUND_ASSETS = (
    "assets/images/favicon.png", "assets/stylesheets/main.5cda52a2.min.css",
    "assets/stylesheets/palette.d7242098.min.css", "style/fontlab_pyapi.css",
)


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
    # UI and worker checks are one read-only transaction before any directory/write.
    ui_dist = source / "ui-dist"
    ui = json.loads((ui_dist / "receipt.json").read_bytes())
    if ui["schema_version"] != 1 or ui["compiler"] != "esbuild0.25.12" or ui["target"] != "es2015":
        raise ValueError("Unsupported archive UI build identity")
    inventory_bytes = (source / "ui-sources.json").read_bytes()
    if hashlib.sha256(inventory_bytes).hexdigest() != ui["sources_sha256"]:
        raise ValueError("Archive UI source inventory differs")
    for row in json.loads(inventory_bytes)["files"]:
        name = row["path"]
        if Path(name).is_absolute() or ".." in Path(name).parts or "\\" in name:
            raise ValueError("Unsafe archive UI source path")
        content = (source / name).read_bytes()
        if len(content) != row["bytes"] or hashlib.sha256(content).hexdigest() != row["sha256"]:
            raise ValueError("Archive UI preferred source differs")
    for row in ui["original"].values():
        if hashlib.sha256((destination / row["path"]).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError("Original archived UI asset differs")
    if set(ui["files"]) != {ui["bundle"], ui["map"], "NOTICE.txt"}:
        raise ValueError("Archive UI output inventory differs")
    ui_payloads = {}
    for name, identity in ui["files"].items():
        if Path(name).name != name or "\\" in name:
            raise ValueError("Invalid archive UI output path")
        content = (ui_dist / name).read_bytes()
        if len(content) != identity["bytes"] or hashlib.sha256(content).hexdigest() != identity["sha256"]:
            raise ValueError("Archive UI checksum differs")
        ui_payloads[name] = content
    for key, suffix in (("bundle", ".js"), ("map", ".js.map")):
        if ui[key] != "bundle." + hashlib.sha256(ui_payloads[ui[key]]).hexdigest() + suffix:
            raise ValueError("Archive UI content address differs")
    if not ui_payloads[ui["bundle"]].endswith(f'//# sourceMappingURL={ui["map"]}\n'.encode()):
        raise ValueError("Archive UI map reference differs")
    mapping = json.loads(ui_payloads[ui["map"]])
    if not mapping["mappings"] or not mapping["sourcesContent"] or len(mapping["sources"]) != len(mapping["sourcesContent"]):
        raise ValueError("Incomplete archive UI source map")
    if any(Path(name).is_absolute() or ".." in Path(name).parts or "\\" in name for name in mapping["sources"]):
        raise ValueError("Unsafe archive UI map source path")
    replacements = []
    for page, content, match in sorted(pages.values(), key=lambda row: row[0].name == "404.html"):
        config = json.loads(match[2])
        old = config["search"]
        if old not in {OLD, "/fontlab-python-docs/pythonqt/" + OLD}:
            raise ValueError("Unexpected archived search worker URL")
        token = json.dumps(old).encode()
        if match[2].count(token) != 1:
            raise ValueError("Ambiguous archived search worker URL")
        changed = match[2].replace(token, json.dumps(ASSETS + receipt["worker"]).encode())
        if page.name == "404.html":
            bases = [value for key, value in json.loads(match[2], object_pairs_hook=list) if key == "base"]
            token = json.dumps("/fontlab-python-docs/pythonqt/").encode()
            if bases != ["/fontlab-python-docs/pythonqt/"] or changed.count(token) != 1:
                raise ValueError("Unexpected or ambiguous archived 404 search base")
            changed = changed.replace(token, json.dumps(".").encode())
        updated = content[:match.start(2)] + changed + content[match.end(2):]
        scripts = [script for script in SCRIPT.finditer(updated) if b"/bundle." in script[1]]
        expected_ui = ("/fontlab-python-docs/pythonqt/" if page.name == "404.html" else "") + UI_OLD
        if len(scripts) != 1 or scripts[0][1] != expected_ui.encode() or scripts[0][0].count(b"src=") != 1:
            raise ValueError("Unexpected or ambiguous archived UI bundle URL")
        script = scripts[0]
        updated = updated[:script.start(1)] + (UI_ASSETS + ui["bundle"]).encode() + updated[script.end(1):]
        if page.name == "404.html":
            manifest = json.loads((root / "archive/fontlab7-manifest.json").read_bytes())
            for asset in NOT_FOUND_ASSETS:
                suffix = asset.encode()
                original = b"/fontlab-python-docs/pythonqt/" + suffix
                token = b'href="' + original + b'"'
                targets = [tag for tag in LINK.finditer(updated)
                           if any(value.endswith(suffix) for value in HREF.findall(tag[0]))]
                if len(targets) != 1 or HREF.findall(targets[0][0]) != [original] or updated.count(token) != 1:
                    raise ValueError("Unexpected or ambiguous archived 404 asset href")
                identities = [row for row in manifest["files"] if row["path"] == "pythonqt/" + asset]
                if len(identities) != 1:
                    raise ValueError("Archived 404 asset identity differs")
                identity = identities[0]
                content_bytes = (destination / asset).read_bytes()
                if len(content_bytes) != identity["bytes"] or hashlib.sha256(content_bytes).hexdigest() != identity["sha256"]:
                    raise ValueError("Original archived 404 asset differs")
                updated = updated.replace(token, b'href="' + suffix + b'"')
        replacements.append((page, updated))
    # All preflight checks above are read-only. Only the derivative and URL values change.
    target = destination / ASSETS
    target.mkdir(parents=True, exist_ok=True)
    for name, content in payloads.items():
        (target / name).write_bytes(content)
    (target / "receipt.json").write_bytes((dist / "receipt.json").read_bytes())
    ui_target = destination / UI_ASSETS
    ui_target.mkdir(parents=True, exist_ok=True)
    for name, content in ui_payloads.items():
        (ui_target / name).write_bytes(content)
    (ui_target / "receipt.json").write_bytes((ui_dist / "receipt.json").read_bytes())
    for page, content in replacements:
        page.write_bytes(content)
    return receipt
