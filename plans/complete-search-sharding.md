---
this_file: docs/superpowers/plans/complete-search-sharding.md
---
# Complete documentation search with bounded browser memory

Authority: ../../../../issues/101.md R040/R041 and current source-binding browser acceptance. Both complete example collections and compatibility packages remain separate active requirements.

## Global Constraints

- Preserve every original search document, text, tag, identity and alias. Current reviewed coverage has246816identities and521767aliases; current search has60048distinct locations,71587122raw bytes and6715183gzip bytes.
- Retain MaterialX10.1.5, ProperDocs, actual search UI, prefix-hosted URLs, archive/current distinction, correct inherited links and19existing named queries.
- Initial compressed search payload at most5MiB; current HTML pages at most2MiB; named targets within2seconds after readiness. Do not redefine readiness to hide arbitrary query-time downloads.
- No fresh browser/context per case, forced garbage collection, raised heap limits or dropped cases to conceal reproduced V8 OOM.
- Feature branch only; preserve other changes, no publication/push/tag or upstream history rewrite. All commands rtk proxy. Workers no subagents.
- Keep raw failed browser evidence. Root owns full build/check/staticlinks and actual same-tab browser acceptance, including18changed relationships/12layouts and memory measurements.

## Task 1: Validate complete search architecture with executable prototype

Own an isolated prototype and architecture report in this plan workspace; do not change production code yet. Inspect scripts/site_hooks.py, search_identities.py, actual shipped source maps and existing consumer tests. The authoritative extracted protocol/source hashes are in ../verification/issue-101-ecosystem/evidence/docs-search-protocol.json and search-protocol/. Current page fetches the entire JSON then structured-clones docs to worker. SETUP0/READY1/QUERY2/RESULT3; RESULT data.items grouped arrays with target/title/text/score/terms. Source alone does not identify the retention cause.

Consult current official documentation and dependency sources before API choices. Compare reuse of existing worker/Lunr with loadable shards against a precomputed search backend; do not choose a custom parser or matching algorithm merely to make a handful of tests pass. Preserve current query normalization, useful unqualified/qualified discovery, alias targeting and grouped result navigation. Search must find identities across shard boundaries, including generic queries; namespace-only routing is insufficient. Keep unchanged original rows in reconstructable shards with exact multiset reconciliation. Decouple cheap startup metadata from full text/alias payload; fetch and retain index data inside the worker where possible, with bounded lifetime and stale-query protection. Avoid blind injection into minified bundled code; use documented/configured template integration verified against installed templates.

Produce an executable complete-index prototype, not just prose. Measure actual initial gzip bytes, request trace/shard selection, first and warm named-query latency, page/worker heap and peak live shard data in the actual Playwright browser. Use all19queries from ../verification/issue-101-ecosystem/docs-source-binding-browser.py; include cross-shard unqualified resize/Signal and deliberately missing/delayed shard failures. Compare current consumer result target semantics and text/tag coverage. Record realistic cold-query costs separately from ready-query costs. Prove full reconstruction of all60048rows and retain complete identity/alias coverage verifier. Select the architecture only after observations support meeting R041. If a candidate fails, retain failure and try another grounded option without altering budgets or denominator. Write exact architecture/interfaces/filenames/remaining work, covering commands/results and limitations to task-1-report.md. No full site rebuild or native FontLab changes in this task.

## Task 2: Implement reviewed complete search architecture

After prototype review, root records selected interfaces and exact task brief. Own narrow search generation/worker/template integration and focused regression tests plus scoped docs. Test first: exact all-row shard reconstruction, all identity/alias targets, request selection for qualified/unqualified/multi-term queries, missing/corrupt/delayed shard behavior, stale-query cancellation and prefix-hosted routes. Preserve original search rows in generated sections, separate build-time coverage from browser startup payload. Run focused regressions then relevant full suite, commit and report. No weakening of existing coverage/browser assertions. Task review required before root build.

## Task 3: Root full-site and browser acceptance

Rebuild strict complete site and check manifest; audit all internal links. Re-run the original19queries/12routes/all18changedtables/all12layouts in the same browser/tab and same deadlines, plus cold shard loading/search failure/recovery evidence. Record page and worker memory across all navigation, peak shard/index memory, transferred/initial gzip bytes and build time/RSS. Require no renderer crash, no JavaScript errors, correct target URLs/anchors and continued full search coverage. Archive old failure and new receipts separately. Complete whole-branch review before publication; source-binding Task2 remains unaccepted until this browser gate passes.
