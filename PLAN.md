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

The 2026-10-18 local src_docs layout, docs/ output and requested plugin setup
are complete, with full local source/archive/search/browser gates. Remaining
whole-branch/release/publication tasks above are outside that setup milestone.


## Authored Echopy guide acceptance

Offline examples are verified separately from generated-reference acceptance.
The authored signature-reading and owned descriptor pipeline examples pass in
Echopy0.2.4.dev6 wheel/sdist installs; rendering remains unverified.
The two native identity snippets still require installed-host execution. Rebuild
and browser/publication checks remain behind D29 and the full source-lock review.

- [ ] Verify the two authored UI examples in native PythonQt and their rendered page after D29 permits a full build. Standalone Qt cases pass; actual QFileDialog isolation requires a disposable OS account or VM.

- [ ] Qualify the native writer guide with real installed FontLab operations and final rendered pages after D29 permits rebuilding; fourteen offline snippet checks do not close those gates.

- [ ] Qualify the authored background preview/apply example in native FontLab and its rendered page once D29 permits a full build. Offline snippets pass with installed App .158 and owned native doubles.
