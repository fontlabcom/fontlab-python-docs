---
this_file: CHANGELOG.md
---

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
