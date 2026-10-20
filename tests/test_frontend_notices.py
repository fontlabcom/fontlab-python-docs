# this_file: tests/test_frontend_notices.py
"""Full source-bound browser notices must survive documentation builds."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "src_docs/md"


def test_frontend_notices_when_authored_then_every_full_text_is_present():
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    page = (DOCS / "frontend-notices.md").read_text()
    assert manifest["components"], "Browser notices must name their components"
    for component in manifest["components"]:
        assert component["source_url"].startswith("https://"), component["name"]
        for item in component["notices"]:
            path = DOCS / item["path"]
            assert path.is_file(), item["path"]
            assert len(path.read_bytes()) > 200, "An abbreviated licence link is not a full notice"
            assert hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"], item["path"]
            assert item["path"] in page, "Every retained notice must be visible on the licences route"
    assert "frontend-notices.md" in (DOCS / "licenses.md").read_text()


def test_frontend_notices_when_review_is_partial_then_pending_scope_is_explicit():
    manifest = json.loads((DOCS / "frontend-notices.json").read_text())
    if not manifest["complete_transitive_inventory"]:
        assert manifest["pending"], "A partial audit must retain every unresolved component group"
        assert "still being reviewed" in (DOCS / "frontend-notices.md").read_text()
    assert "publication_qualified" not in manifest or manifest["publication_qualified"] is False
