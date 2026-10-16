---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` and `issues/106.md`. Completed work is in
CHANGELOG.md. Publication is the controller's (runbook: workspace
`verification/issue-104/reports/L5-echopy-docs.md`, Task 7; D11).

1. **Review of D14.** Owner decision D14 adds the fontlab-fontport reference (Apache-2.0,
   docstrings/signatures only) and removes the reviewed fly.fp exception (d2ed4c1); final-10
   passed every gate with it (lock 6395a8f). Needs an X4 scoped review.
2. **Short rebuild after the glyport release candidate.** X1 round 7 changes glyport `src`;
   after its merge and RC, echopy regenerates shims, then
   `verification/issue-101-ecosystem/evidence/docs-104/final-rebuild.sh` must pass every gate
   and the reviewed lock is committed.
