---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` (section `./fontlab-python-docs/`). Completed
issue 104 work is in CHANGELOG.md ("Issue 104 — completed"). Publication is the
controller's (runbook: workspace `verification/issue-104/reports/L5-echopy-docs.md`, Task 7).

1. **Final consolidated rebuild (blocked on two inputs).** Run
   `verification/issue-101-ecosystem/evidence/docs-104/final-rebuild.sh` once:
   - lane L6 has replaced the three examples-export links to private
     repositories (recipes glyph_actions_batch, glyphs_path_report,
     glyphs_tabular_figures), which the release audit correctly rejects; and
   - the controller has merged glyport `issue-104-glyport-r020` and echopy has
     committed the regenerated `GlyphsApp/_shim.json`.
   Every gate must exit 0, including five consecutive interaction runs, the
   prefix rehearsal and determinism; commit the refreshed source lock.
