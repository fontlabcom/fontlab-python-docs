---
this_file: CHANGELOG.md
---

## Issue 106 — completed (lane C3, 2026-10-16)

- [x] Release audit decodes layered escapes (JSON/JS `\uXXXX \xXX \/ \\`, percent, HTML
  character references incl. numeric ones without `;`), re-parses JSON nested in strings and
  fails closed (`decode-limit`) beyond its bounds (a211a02, 4e61a68, f712bec, 9633e1d).
  X4b/X4c findings; X4f and X4n APPROVE.
- [x] Finder `.DS_Store` written into the generation stage no longer breaks a build (d6a4280).
- [x] lunr 2.3.9 TokenSet key collision (upstream olivernn/lunr.js#503) patched in every
  shipped search engine: complete-search bundles at compile time, stock MaterialX worker after
  each build (3ad6570). X4n APPROVE.
- [x] Front-coded routing vocabulary keeps the R041 5 MiB initial search budget: initial
  payload 3,078,385 bytes (2118409). X4n APPROVE (862,620 terms round-trip).
- [x] Consolidated rebuilds at merged glyport: final-10 all 16 gates exit 0 (300 tests; release
  audit 6,002 files, 0 findings; determinism identical; 242,654/242,654 identities); lock
  6395a8f. Evidence: workspace `verification/issue-106/evidence/C3/final-1/` .. `final-10/`.

## Issue 104 — completed (lane L5, 2026-10-15)

- [x] Coverage reconciled against Echopy's capture identity manifest in every
  build: 242,654/242,654 captured identities documented, 0 unexplained; native
  spellings recorded; single-underscore native members documented (R014, G09).
- [x] Shim references: `fontlabapp_shim`, `GlyphsApp`, `GlyphsApp.plugins`,
  `vanilla`, `vanilla.dialogs`, `AppKit`, `Cocoa`, `Foundation`, `objc`,
  `aidus_code_tools`; unresolved shim exports and discarded aliases fail the build.
- [x] `./build.sh --serve` (under `/fontlab-python-docs/`) and installed-artifact
  mode (`FONTLAB_API_SOURCE_ROOT`) run and recorded (R039).
- [x] Deterministic rebuild: source and artifact modes render identical bytes;
  privacy/licence audit of site, search shards and source maps (R044, R055).
- [x] Decisions: archive routing (redirect + current link) and shard deadline
  (no partial results; Retry doubles the deadline to 30 s).
- [x] Publication runbook with deployed-host checks (`deployed_check.py`,
  `interaction_check --base`), previous deployment kept by tag (R042, R044).
- [x] Browser checks fixed at their cause (server backlog, readiness waits);
  five consecutive interaction runs pass.
- [x] Examples docs export integrated and pinned.
- [x] Review rounds R-L5-docs, RR-docs, RR2-docs fixed test-first.

## Unreleased — issue 104 review fixes (R-L5-docs)

- Release audit: current credential formats (incl. `github_pat_`), inline
  `data:` source maps and JSON-escaped strings decoded, mounted-volume and
  checkout paths, private repository URLs and names (from local git remotes),
  exact reviewed example values instead of a `file:///` prefix, licence texts
  verified by digest and linked from the licences page.
- Reconciliation: multiple declarations explained only by exact structure
  (getter/setter/deleter, module+class facet, module+parent attribute) or a
  line-pinned review; aliases discarded by resolution are reported.
- `deployed_check`: every `assets/` file (worker, search UI, theme) and header
  validation (media types; no Content-Encoding on explicit `.gz`).

## Unreleased — issue 104 coverage reconciliation (R014)

- `scripts/reconcile_coverage.py` reconciles every build against Echopy's capture
  identity manifest; the build fails on any missing, uncaptured or multiply
  declared native identity, capture error, unmatched overlay or dangling alias.
- Single-underscore members of captured native classes (14, e.g.
  `PythonQt.private.MainWindow._clear_outline_controls`) are now documented.
- `_identities.json` and `_provenance.json` are pinned in the API source lock.

## 2026-10-15 — completed checklist (moved from TODO.md)

- Verify source-only native documentation names through actual mkdocstrings.
- Add explicit locked mkdocstrings Python handler/autorefs/Griffe dependencies.
- Test full-occurrence inventory, exact body sharing, pagination and facets.
- Generate current native and ecosystem API pages, coverage report and aliases: strict full build 212 s, 4,331 pages, 245,151 member identities, 60,048 search rows, `--check` pass (docs f8bb92a, 3ddc4e0). Reconciliation against the raw Echopy capture (R014) remains open.
- Rebuild the current local root with verified shared theme asset/search ownership.
- Implement and verify locked offline build/check and API source byte pins.
- Verify actual inventory URI anchors, nine native searches and responsive method page.
- Verify remaining internal links, alias families and keyboard/focus interactions (R043 receipts: deep/type/param-type links, aliases, late shard search and keyboard 4/4 each; a11y 28/28; workspace evidence r043-interactions/, tg8-theme/).
- Complete consumed private-input locking, exported class-member aliases/public titles and @property index semantics; see docs/superpowers/plans/source-reference-fidelity.md.
- Resolve final I1–I5 and M2/M3 documentation defects with 66-test source/browser regressions.
- Provide a build-plus-consumer command that fails on missing inputs and provisions Chromium.
- Implement complete search sharding, original consumer comparisons and checked initial5MiB startup transfer.

## 2026-10-14 — R042 archive pages link their current page

- Archived FontLab7 pages whose route map has an exact `current_route` now carry a
  visible "Current version of this page" link in the archive banner. It is generated
  at build time from the same `route-map.json` report; on load and on `hashchange`
  it retargets to the mapped current anchor for the URL fragment, else the page target.
- Legacy routes still redirect to the archive with their fragment (unchanged).
- Site verification fails when an archived page's link, or its fragment map,
  disagrees with the recomputed route map, or a page without a current route has one.
- The interaction receipt now asserts the link on the archived legacy target.

## 2026-10-14 — R043 interaction receipts

- Add `scripts/interaction_check.py`: Playwright receipts at 1280x800 and 375x812
  in light/dark for member deep links (hit-tested clear of sticky chrome),
  signature type links, alias resolution (inventory, search by alias, legacy
  redirect), a search result held back by a 1.5 s delayed non-initial shard
  (absent before the delay, same-tab open, Back) and keyboard reach (skip link,
  search, navigation or its drawer opener, first content link, `/`/`s` recorded).
- Add passing and failing fixture pages for every check.
- Built-site receipt: type links fail 0/4; the rendered signatures carry no
  cross-reference links (signature_crossrefs is not enabled). Other cases pass 4/4.

## 2026-10-14 — R043/R044 accessibility and CI gates

- Correct accessibility checker timing for animated focus rings, hidden-control
  naming and responsive search/navigation targeting. Test reachability in any
  order within 40 Tabs; retain off-screen/absent focus indicators as failures.
- Record unmeasurable contrast separately under `needs_manual`; retain the
  strict 4.5:1 failure threshold and fail provably transparent unreadable text.
  Add passing/failing regression fixtures for each correction.
- Add local Playwright accessibility acceptance with JSON receipts for seven
  representative pages at desktop/mobile sizes in light/dark schemes. Check
  overflow, keyboard reach/focus, headings, image alternatives, control names
  and 4.5:1 text contrast; retain unmeasurable backgrounds for manual review.
- Add tiny passing/failing browser fixtures and workflow/receipt regression tests.
- Add Ubuntu documentation CI with locked dependencies, sibling producer
  checkouts, consumer/build/accessibility gates and retained artifacts. Document
  the private-source read secret and distinguish CI acceptance from deployment.

## 2026-10-14 — legacy route map

- Emit deterministic `route-map.json` with all original HTML routes/fragments,
  exact public identity targets and broken-in-original internal link diagnostics.
- Verify map completeness, archived anchors and redirect agreement during build
  and check; retain named anchors as well as HTML IDs.

## Unreleased — native source reference verification

- Reopen and reconcile search status/retry channels after persisted page restoration;
  preserve the original empty-result behavior for Lunr query parse failures.
- Shard complete search rows without dropping identities, aliases or fields;
  route globally through checked vocabulary/postings and hydrate with the original
  pinned MaterialX/Lunr engine. Gate actual initial static transfer at5MiB,
  including explicit gzip metadata, bootstrap, worker and retry UI.
- Preserve configured search suggestions, show unavailable/retry states separately
  from no matches, reject corrupt metadata/shards and suppress superseded results.
  Ordinary source builds remain offline after dependency bootstrap.
- Keep known empty namespaces authoritative, evaluate source decorator approval
  against its active declaration/dependencies, and invalidate shared class
  attributes across aliases after source writes or deletes.
- Resolve source bases from declaration-time bindings and class-body scopes;
  preserve source-known imports/aliases/star exports while leaving overwritten,
  future and dynamic bindings unresolved. Correct Qt wrapper and dialog lineage
  without changing source identities, URLs or existing supported aliases.
- Rank native module namespaces ahead of descendant class prefix matches using
  supported MaterialX document boosts; verify twelve real worker queries against
  the complete index while retaining every source row and exported alias.
- Keep source-derived callable signatures and property annotations visible below
  exported member headings using supported consumer signature rendering options.
- Qualify native module/class whole-page search entries from source coverage URLs
  so exact public module aliases such as fly.fl reach their primary native page.
- Respect explicit aliases and source declarations at every intervening export
  prefix; replacement classes cannot inherit unsupported descendant aliases or
  resolve nonexistent forwarded members through an overridden ancestor.
- Pin every consumed private/runtime/stub input once and reject duplicate lock
  identities; source input changes still require explicit lock refresh.
- Expand proven module/class re-exports to descendant aliases, preserving native
  names, canonical identities and shared declaration bodies.
- Display public package exports for authored private implementation classes while
  retaining stable source directives, URLs and canonical anchors.
- Classify source properties as attributes and retain getter/setter/deleter
  provenance, exact declaration hashes and occurrence accounting.
- Verify the changes with focused fixtures, a strict source-only MkDocs render,
  the existing suite and a complete read-only source inventory comparison.
- Preserve qualified native method names and exported aliases in search; skip
  stemming of API identifiers and rank module/class targets ahead of prefixes.
- Verify every expected objects.inv URI against actual rendered HTML anchors.
- Pin API input bytes across source/artifact modes; require explicit lock refresh.
- Add repeatable Chromium search/deep-anchor and mobile/light/dark smoke receipts.

## Expanded reference — unreleased

- Generate complete native and ecosystem source references with actual native
  identities, retained occurrence indexes and paginated shared declaration text.
- Add source-only namespace/import discovery, complete anchor and objects.inv
  verification, locked build/check/serve/explicit native-refresh entry points.
- Preserve the previous FontLab7 site in a verified archive with fragment-aware
  redirects and archive context.
- Add current installation/native/UI/compatibility/build guides and shared-theme
  styling; full browser/search and deployment acceptance remain in progress.

## 2026-09-23

- Publish the API documentation with ProperDocs/MaterialX and shared fltheme26 assets.
- Keep generated API HTML, routes, anchors and styling; use core search for the large PythonQt pages.
- Add a reproducible root-then-child build with source-owned CSS.

- Preserve API 404 asset/home routes under the GitHub Pages project prefix.
- Bridge the core search index to the existing MaterialX search UI and verify index preservation.


## Source-reference final review fixes

- Index every shared occurrence and alias at its canonical body; enforce complete
  search identity coverage and a non-skipping 15-query shipped-consumer gate.
- Generate into fresh owned input trees and seal accepted input/rendered manifests;
  deterministic checks reject missing baselines and stale content without rewriting
  accepted artifacts.
- Preserve legacy root fragments under static-host prefixes and expose the archive.
- Render source-proven bases and inherited canonical member indexes with Griffe C3
  ordering, authoritative overrides and nested-class navigation.
- Correct the PySide runner guide to describe its implemented scoped contract.
- Record the provisional 7 MiB complete-search allowance; initial 5 MiB payload
  sharding, clean CI and broader publication acceptance remain unfinished.

- Removed the GitHub Actions docs workflow (owner decision); acceptance gates run locally.


## Issue120 current documentation Z5

Static reference generation retains authored Griffe extensions, including namespace visits; reviewed TypeRig array-index literals render as code. Duplicate Table.__eq__ definitions remain recorded with their exact source fingerprints. The reviewed producer lock now binds 678 current inputs.

## Unreleased — Issue120 Z19

- Refresh the reviewed API producer lock to App 0.2.62.dev0 and Glyport 1.0.8.dev28: 705 inputs, 27 additions and no removals.
- Restore explicit same-name absolute re-exports, literal `__all__` exports and public inherited members from private bases. Keep canonical source bodies, source-order invalidation and C3 ordering; exclude unrelated private declarations and undefined export names.
- Retain complete native identity reconciliation and local build/search/browser gates. Native execution, whole-branch integration, released dependencies and publication remain pending.

- Keep the full real search-worker fixture on loopback HTTP, preserving all complete-index bytes, ranking assertions and deadlines; verify UTF-8 transport explicitly.

## Issue120 Z24 — browser notices

Add source-bound full texts and provenance for named frontend components, including transitive JavaScript dependencies, icons, shared theme inputs and external font responses. Keep the full transitive/publication review explicitly open; runtime assets and retained archives are unchanged.

## Issue120 Z26

Preserve exact upstream notice bytes through Git filters, fresh checkout and archives; add a CRLF distribution regression. Source manifests and pending publication scope remain unchanged.

## Unreleased — isolate temporary notice repositories

- Clear Git's documented repository-local environment for temporary notice
  distribution commands and bound each child call to10seconds.
- Exercise inherited hook context with both default and alternate parent indexes;
  require byte-exact preservation of parent config, refs, index, objects, files
  and caller environment. Keep every notice/filter/checkout/archive assertion.
- Preserve all upstream notice payloads and existing attributes/manifests.
  Source-only correction awaits fresh independent review; no new commit/push.

## 2026-10-21 — private final-producer docs candidate

- Preserve reviewed public-source/browser-notice producer payload and all owner
  preimages; explicitly pin734 reviewed current source inputs.
- Locally build/verify final App220/Glyport115 API with5925pages; retain unchanged
  archive/route/search limits,343tests and28/28interaction/accessibility gates.
- Keep canonical application and publication pending root review.

## 2026-10-21 — App.74/Fontport7a source checkpoint, not publication

- Pin the reviewed Fontport App Vanilla compatibility import within734API inputs.
- Build/verify current checkpoint aliases with343tests and targeted browser/worker
  controls; preserve prior N60 evidence and all owner source/index/docs preimages.
- Keep later App.76/.80 producer refresh, root-reviewed feature/canonical delivery
  and publication separate; no native acceptance is advanced.

## 2026-10-21 — N83 final source graph and actual TypeRig discovery

Private checkpoint aligns App86721bf(.80), Glyport2c46, Fontport7a,
Examples657bb1e(31) and Scriptmixd54ee17f(105). Reviewed734→743APIinputs:
nine new Pattern Lab/report-pair modules and one owned dialog-close fix.
Preserve N65 .74 evidence as historical. Actual TypeRig sources live in
TypeRig/Lib; producer and real Void inheritance regression now share source_roots,
including explicit installed-artifact roots, without a fabricated legacy alias.
Before-fix regression fails; corrected targeted25tests pass. Final strict
three-site, routes, browser/worker/accessibility and exact notice checks follow
in verification/issue-120/docs-final-checkpoint-z33; no native/publication claim.

N83 verification: all three strict sites pass; API348 required-consumer tests
pass without skips, existing interaction28/28 and accessibility28/28 pass.
Every136menu source block matches its current source; actual worker13queries
and18body views pass. Exact served notices25API/26per menu site and release
audits pass with each site's existing licence policy. All185actual TypeRig
inputs match the reviewed lock/snapshot, and unchanged Void/Point assertions
pass on configured TypeRig/Lib. Extra menu-site accessibility discovered mobile
notice-page navigation reach failures; retained as a separate N90 publication
gate. No checker budget was waived. This source checkpoint is App.80/105menus;
it does not include the private .84/106candidate, native acceptance or publication.
