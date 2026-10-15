---
this_file: TODO.md
---

# Tasks

- [x] Reconcile `.build/coverage.json` against the Echopy capture identity manifest in every build: every captured symbol, member and alias accounted for, zero unexplained capture/merge/extraction errors (R014, G09; shared with fontlab-echopy).
- [x] Document single-underscore native members that the inventory currently drops (R014).
- [ ] Build docs for `fontlabapp`, glyport and aidus-code from the Echopy shims (issue 104).
- [x] Run and record `./build.sh --serve` and the installed-artifact mode (`FONTLAB_API_SOURCE_ROOT`); run `--refresh-native` only when the owner asks (R039).
- [x] Deterministic offline rebuild in source and artifact modes; privacy and licence audit of site, search index and source maps (R044, R055).
- [x] Decide archive-vs-current routing for pages present in both, and the behaviour after the 1.8 s shard timeout; implement, test, document.
- [x] Prepare publication for the controller: exact publish and deployed-host verification commands, keeping the previous deployment (R042, R044).
