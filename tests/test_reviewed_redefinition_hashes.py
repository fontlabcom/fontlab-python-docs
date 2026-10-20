# this_file: tests/test_reviewed_redefinition_hashes.py
"""Reviewed duplicate definitions must remain bound to their exact source AST."""

import copy

from scripts.reconcile_coverage import _declaration_reason
from test_reconcile_coverage import MANIFEST

IDENTITY = "typerig.core.objects.matrix.Table.__eq__"
HASHES = (
    "3156add7aeedd303cb7a93e269699b339bb79ebc9129b3e7e27e32c3f0ecedfa",
    "18d85701aa0c6c0551ab850cc55966e9a28512bb0d111cd2a234c794edad3369",
)


def row():
    return {
        "occurrences": 2,
        "declarations": [
            {"kind": "function", "line": line, "declaration_sha256": sha}
            for line, sha in zip((77, 180), HASHES)
        ],
    }


def test_reviewed_duplicate_when_exact_then_preserve_reason_and_both_occurrences():
    value = row()
    before = copy.deepcopy(value)
    assert (
        _declaration_reason(IDENTITY, value, MANIFEST)
        == "reviewed-redefinition: upstream defines __eq__ twice; the second wins"
    )
    assert value == before and len(value["declarations"]) == 2


def test_reviewed_duplicate_when_body_changes_at_same_lines_then_unexplained():
    value = row()
    value["declarations"][1]["declaration_sha256"] = "different"
    assert _declaration_reason(IDENTITY, value, MANIFEST) is None
