---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` and `issues/106.md`. Completed work is in
CHANGELOG.md. Publication is the controller's (runbook: workspace
`verification/issue-104/reports/L5-echopy-docs.md`, Task 7; D11).

1. **Independent re-review.** X4c approved echopy and asked for two audit fixes (done in
   9633e1d). Later fixes need review: lunr 2.3.9 TokenSet key patch in every shipped search
   engine (3ad6570), the reviewed `fly.fp -> fontlab_fontport` alias explanation (e406122)
   and the front-coded routing vocabulary that keeps the R041 5 MiB initial budget (2118409).
2. **Consolidated rebuild at merged glyport.** Final-9 (glyport 0baafb4, echopy d5c0ba3):
   13 gates green, stopped by the controller during build-2; rerun to completion and commit
   the reviewed lock (evidence: workspace `verification/issue-106/evidence/C3/final-9/`).
3. **Owner decision on Fontport.** fly now aliases `fp` to the private fontlab-fontport; publish
   its API reference (like D10) or keep the reviewed exception.
