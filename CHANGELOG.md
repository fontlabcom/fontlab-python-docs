---
this_file: CHANGELOG.md
---

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
