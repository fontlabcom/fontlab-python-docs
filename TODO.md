---
this_file: TODO.md
---

# Tasks

- [ ] Reconcile `.build/coverage.json` against the raw Echopy capture: every captured symbol, member and alias accounted for, zero unexplained capture/merge/extraction errors (R014, G09; shared with fontlab-echopy).
- [ ] Run and record `./build.sh --serve` and the installed-artifact mode (`FONTLAB_API_SOURCE_ROOT`); run `--refresh-native` only when the owner asks (R039).
- [ ] Deterministic offline rebuild in source and artifact modes; privacy and licence audit of site, search index and source maps (R044, R055).
- [ ] Decide archive-vs-current routing for pages present in both, and the behaviour after the 1.8 s shard timeout.
- [ ] Publish the audited site; on the deployed host verify redirects/fragments in a browser, routes, asset headers, build provenance, live search and navigation, the site under its URL path prefix, and same-tab navigation/memory; keep the previous deployment (R042, R044).
