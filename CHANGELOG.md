---
this_file: CHANGELOG.md
---

## v1.0.2 — complete v1.0.1 publication (2026-10-16)

- Publishes 4 TypeRig pages (`typerig.core.objects.instance`) that a template `.gitignore` rule
  dropped from v1.0.1; their 20 identities and 20 Fly aliases resolve again. `docs/` can no
  longer lose pages to ignore rules.

## v1.0.1 — published reference (2026-10-16)

- Publishes the reviewed reference at https://code.fontlab.com/fontlab-python-docs/ (master:/docs):
  242,654 captured native identities documented; Echopy shims for GlyphsApp, vanilla, AppKit,
  Cocoa, Foundation, objc, FontLab menus/panels and the Aidus tools; ecosystem packages Echopy,
  Fly, Fontlabapp, Remopy, Grablab, Pythonqtside, Glyport, Fontport (D14), TypeRig and Aidus Code.
- New Packages section: overview, install, quick start, examples and limits for each package.
- The previous FontLab 7 / PythonQt reference stays available under `archive/fontlab7/` with its
  original routes.
- Artifact: final-11 (docs 9161c0c), all 16 gates passed; review X4r2 APPROVE.

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
