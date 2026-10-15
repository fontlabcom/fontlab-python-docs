---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/104.md` (section `./fontlab-python-docs/`), extending
`issues/101.md` R037–R044 and G09–G10. Lane L5 of the workspace
`verification/issue-104/LANES.md`. Completed work is summarised in README.md
"Status". Remaining work:

1. **Coverage reconciliation (R014, top priority).** Reconcile `.build/coverage.json`
   against Echopy's capture identity manifest during every build. Each captured
   symbol, member and alias is documented, or carries a machine-checked reason
   (maintained extension, absent optional module, module/class facet, enrichment
   gap). Native spellings of sanitized names are recorded in the coverage report.
   Any unexplained row fails the build. Fix extraction defects at their root
   (for example, single-underscore native members dropped by the inventory).
2. **Shim documentation (issue 104).** Render `fontlabapp`, glyport and
   aidus-code references from Echopy's shims once lane L6 and the glyport lanes
   deliver merged sources.
3. **Build modes (R039).** Run and record `./build.sh --serve` and the
   installed-artifact mode (`FONTLAB_API_SOURCE_ROOT`). `--refresh-native` only
   when the owner asks.
4. **Release audit (R044, R055).** Deterministic offline rebuild from both source
   and artifact modes; privacy and licence audit of the built site, search index
   and source maps.
5. **Open questions.** Decide archive-vs-current routing for pages that exist in
   both, and the behaviour after the 1.8 s shard timeout; implement, test and
   document the decision.
6. **Publication preparation (R042, R044).** The controller publishes. This lane
   lists the exact publish and deployed-host verification commands (redirects
   and fragments in a browser, routes, asset headers, build provenance, live
   search and navigation, the URL path prefix, same-tab navigation/memory) and
   how the previous deployment is kept.

GitHub CI is out of scope (owner decision D3).
