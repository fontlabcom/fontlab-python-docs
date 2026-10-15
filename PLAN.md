---
this_file: PLAN.md
---

# Plan

Authority: parent `issues/101.md` R037–R044 and G09–G10. Completed work is
summarised in README.md "Status". Remaining work:

1. **Coverage reconciliation (R014).** Check `.build/coverage.json` against the raw
   Echopy capture; report every unaccounted symbol and error.
2. **Build modes (R039).** Run and record `./build.sh --serve`, the
   installed-artifact mode (`FONTLAB_API_SOURCE_ROOT`) and, when the owner asks,
   `--refresh-native`.
3. **Release audit (R044, R055).** Deterministic offline rebuild from both source
   and artifact modes; privacy and licence audit of the built site, search index
   and source maps.
4. **Open questions.** Decide archive-vs-current routing for pages that exist in
   both, and the behaviour after the 1.8 s shard timeout.
5. **Publication (R042, R044).** Publish the audited site; on the deployed host
   verify redirects and fragments in a browser, routes, asset headers, build
   provenance, live search and navigation, the URL path prefix and same-tab
   navigation/memory; keep the previous deployment.

GitHub CI is out of scope (owner decision D3).
