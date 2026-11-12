# this_file: tests/sibling_sources.py
"""Skip a real-source test only when its sibling checkout is genuinely absent.

Some tests read real sibling sources (TypeRig for inheritance, App `_legacy.py`
for the migration mapping). The documentation build sets
`FONTLAB_API_SOURCE_ROOT`, so there the tests always run and a missing source
fails. A lone clone has neither the variable nor the siblings; there the test
skips with the reason instead of failing on a missing checkout.
"""

import os
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
ENV = "FONTLAB_API_SOURCE_ROOT"


def require_sibling(repo: str, root: Path = ROOT) -> None:
    """Skip unless `ENV` is set or the sibling `../<repo>` directory exists."""
    if os.environ.get(ENV) or (root.parent / repo).is_dir():
        return
    pytest.skip(f"needs sibling checkout ../{repo} or {ENV}; absent in this clone")
