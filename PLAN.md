---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` and `issues/106.md`. Completed work is in
CHANGELOG.md. Publication is the controller's (runbook: workspace
`verification/issue-104/reports/L5-echopy-docs.md`, Task 7; D11).

1. **Independent re-review of the release audit.** X4b requested changes on a211a02
   (percent/entity/`\x` bypasses, multi-serialized JSON scalars, unbounded traversal).
   Fixed test-first in f712bec (bounded layered decoding, `decode-limit` fails closed)
   and d6a4280 (Finder `.DS_Store` in the generation stage). Final-5 passes every gate
   of `verification/issue-101-ecosystem/evidence/docs-104/final-rebuild.sh` (evidence:
   workspace `verification/issue-106/evidence/C3/final-5/`). Needs X4 approval.
2. **Short rebuild after the issue-106 glyport merge.** Regenerate echopy shims from the
   merged glyport, commit them in echopy, then rerun the runbook; refresh the lock only
   after reviewing the producer diff and commit it if it changed.
