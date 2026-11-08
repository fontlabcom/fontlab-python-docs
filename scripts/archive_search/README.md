---
this_file: scripts/archive_search/README.md
---

# PythonQt archive search

This derivative repairs ordinary literal completions in the frozen PythonQt
archive. It keeps the original MaterialX query parser and Lunr postings/vector
engine. Ordinary eligible terms gain literal clauses with the same field boosts,
BM25 and theme grouping; scores/order for those queries can change. Explicit
query semantics remain. Purely negative queries now have finite zero scores
instead of the original theme's NaN, using `Query.isNegated()` only.

`provenance/baseline` preserves all original preferred-source bytes, including
the 13 mapped strings and three same-commit resolution modules. MaterialX is
pinned to `c088af2faa3a75dd4b9cded468eca285b6775d71`; the official Lunr 2.3.9 npm
dependency must match its archived string and locked SRI. The nine unchanged
mapped theme modules, three resolution dependencies, three modified modules
and new adapter are individually classified in `identity-inventory.json`.
`provenance/source-provenance.json` is the retained reconstruction evidence;
`sources.json` binds the actual production source. No dependency fork or update
is implied. Full upstream licences remain in this directory and the worker.

Ordinary documentation builds verify and copy the committed distribution;
they never invoke npm. For a maintainer rebuild (Node22+):

```sh
mkdir -p .build/archive-compiler
cp scripts/archive_search/package*.json .build/archive-compiler/
npm ci --prefix .build/archive-compiler --ignore-scripts --no-audit --no-fund
node scripts/archive_search/compile.cjs
node --test scripts/archive_search/tests.cjs
ARCHIVE_SEARCH_COVERAGE=1 node --test scripts/archive_search/tests.cjs
```

Later npm installs can use `--offline` with the populated cache. esbuild0.25.12
emits a map with complete source content, then both map and worker receive their
own full SHA256 filenames. The worker's actual bytes reference the map's actual
name. `receipt.json` binds originals, configuration, source inventory and output
bytes. Commit the source, lock and distribution together after review.

The installer runs after legacy archive verification and wrapping. It checks the
original worker/map/index and all twelve PythonQt page configurations before
writing. Each configuration's search-worker URL changes, with one additional
archived404 base correction described below. Original worker/map/index bytes and FontLab7
remain available unchanged. The new assets carry their full notices and receipt.

Tests retain compressed complete stock and approved derivative messages, all
66 transform annotations and 90 negative-query cases. Compression is solely
storage; assertions compare full decoded messages, scores, order and metadata.
`ARCHIVE_SEARCH_RED_WORKER` points the same repair assertions at an original
worker for the explicit RED reproduction. The coverage option instruments all
four complete TypeScript modules with Istanbul; distribution builds use the
original uninstrumented compiler path. Common X/Y CI provisions the locked test
compiler under `.build` and runs both existing root and archive Node suites.

Source tests and local builds do not establish hosted CI, publication, browser
capacity, latency or native FontLab acceptance. Retained third-party legal and
privacy qualifications remain incomplete at their existing scope.

## PythonQt result presentation

The separate UI derivative escapes literal Python help representations in the
complete search template, preserving only the worker's exact mark delimiters.
Title, teaser and tags use existing escape-html1.0.3; missing-term captions,
translations, parent grouping, scores, thresholds, More and routing are unchanged.
Worker messages/index/corpus and root/FontLab7 renderers are unchanged.

`ui/src` retains115 same-commit MaterialX modules; the search template, content
initializer and visibility dispatcher are the three explicitly recorded overrides. The content initializer
collects the existing component streams in order, retaining RxJS7.8.2's zero/one
`merge` fast paths and using its `from`/`mergeAll` route for larger arrays. This
avoids passing every article link as a function argument without omitting content.
The visibility dispatcher sends each observer entry only to its target's existing
RxJS Subject. It preserves duplicate subscriptions, observe/unobserve ordering,
observer reuse and queued-entry delivery. Last-unsubscribe cleanup releases only
its own unused channel, including errors and reentrant channel replacement.
Whole-module tests retain the original fourteen value/lifecycle cases and measure
entry lookups plus matching deliveries, with exact source-bound caller pipelines.
These source/unit checks do not establish browser readiness or a latency target.
`ui/provenance` retains originals, all211 mapped-source identities, preferred
Mermaid CSS, its frozen browser target set, complete runtime-package sources and
notices. The scoped corpus is the exact frozen40713-document index; a different
index fails the installer preflight and requires a new content contract.

```sh
node scripts/archive_search/compile-ui.cjs
node --test scripts/archive_search/tests-ui.cjs
ARCHIVE_UI_COVERAGE=1 node --test scripts/archive_search/tests-ui.cjs
```

The compiler retains the upstream complete tsconfig, overriding its target with
the actual upstream build's es2015 target. JSX uses h; browser output is one IIFE,
with inline legal comments and a complete external source map. Esbuild performs
transpilation, not TypeScript type checking; strict/interop and module-resolution
settings remain in the original config. The two marker substitutions use
split/join, adding no newer runtime API. Frozen minified Mermaid CSS loads as
text; its preferred source reproduces exactly with postcss8.5.6/cssnano5.1.0 and
the retained resolved browser targets, without a time-dependent query.

`ui-sources.json` binds every source/notice and complete resolved runtime-package
file, plus exact locked tool versions/integrities. The compiler checks resolved
imports, a single entrypoint, no emitted runtime imports, real sourcesContent
and mappings. Map names normalize actual resolved files to stable MaterialX/npm
paths only after checking their complete source strings. Actual JS/map bytes
receive their full SHA256 names. NOTICE and receipt complete the four assets.

The installer validates both worker and UI inputs before any write, including
the original UI bundle/map and one exact script URL on each of the twelve pages.
Only those twelve UI script URLs additionally change, plus the four reviewed
inherited404 asset hrefs and that page's config base. The404 base must uniquely
equal the original `/fontlab-python-docs/pythonqt/` before it becomes `.`;
missing, unexpected or duplicate/ambiguous base values reject before any write.
The other eleven configs retain their base values. The404 favicon/main/palette/fontlab_pyapi.css links
become archive-relative after exact link and original member-byte preflight.
All four worker assets stay exact. Normal site builds use committed artifacts without npm/network.
Both X/Y common CI lanes run the UI, worker and root Node tests. Complete real
messages, actual configuration/translations and full DOM text/ordered UTF16
highlight positions are tested, alongside every template branch. Local tests do
not establish independent approval, hosted CI/Pages or whole-task acceptance.
