---
this_file: PLAN.md
---

<!-- workspace-handoff:2026-11-03 -->
## Current workspace handoff —2026-11-03

**Implementation paused.** Authored guides and source-derived native API documentation.

Observed canonical checkout: `main` at `5ec628a388fa`. No source integration is performed by this update.

Accepted feature d9c15dc adds the owned-window recovery guide after extensive generation/resource/manager/discovery/node/layer guides.

Authored source/ordinary examples were checked; generated references, source-lock, rendered site and publication remain gated.

1. Document only reviewed current behavior and execute new examples against matching source and ordinary artifacts.
2. Complete applicableD29 native/generated/strict-build/routes/archive/browser/accessibility/licence/publication gates.
<!-- /workspace-handoff -->

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

- [ ] Verify authored Glyport layer-name guide rendering after D29 permits rebuilding, and qualify native import None/empty preservation before presenting the predicate as native workflow guidance. Offline candidate examples and older-artifact negative control pass; see WORK.md.

- [x] Verify the authored receiver-name pipeline example against installed wheel/sdist candidates and the older-artifact negative control; native identity and rendered-site acceptance remain open. See WORK.md.

Glyph Info authored example is checked against both installed private artifacts
and an earlier negative control. Keep source-lock/build/browser/publication and
custom-data/native lookup acceptance open; evidence is in workspace issue123
docs-glyph-info-20261101.json.

- [ ] Carry the installed-tested constructor-binding example through source-lock, generated/site build, browser and publication gates once D29 permits; native capture remains separate.

- [ ] Carry the installed-tested collision-preservation example through source-lock, site build/browser and publication gates once D29 permits.

- [x] Verify the authored script-metadata fixture in both fresh installed artifacts and the older-artifact negative control; see WORK.md.

- [x] Verify authored database-case filtering in both installed private artifacts and an older script-only negative control; all eight examples pass, native and rendered-site gates remain open. See WORK.md.

- [ ] Carry the installed-tested top-level alias example through the reviewed generated/site build, browser and publication gates; owned doubles do not qualify native effects.

Classification/resolver counterexamples now qualify the existing lifecycle examples.
Reverify and update these limits after the shared resolver is repaired; ten passing
offline examples do not prove conflicting-name/Unicode reset fidelity.
