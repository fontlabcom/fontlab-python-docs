---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` and `issues/106.md`. Completed work is in
CHANGELOG.md. Publication is the controller's (runbook: workspace
`verification/issue-104/reports/L5-echopy-docs.md`, Task 7; D11).

1. **Independent review of the consolidated rebuild.** Final-2 at a211a02 passed
   every gate of `verification/issue-101-ecosystem/evidence/docs-104/final-rebuild.sh`
   (evidence: workspace `verification/issue-106/evidence/C3/final-2/`). The
   escaped-JSON audit (RR-docs P2, extended in a211a02 for double escapes and JSON
   nested in strings) needs an X4 re-review before this item closes.
2. **Short rebuild after the issue-106 glyport merge.** Regenerate echopy shims from the
   merged glyport, commit them in echopy, then rerun the runbook; refresh the lock only
   after reviewing the producer diff and commit it if it changed.
