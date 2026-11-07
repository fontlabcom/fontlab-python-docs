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
writing. Only each configuration's search-worker URL changes, including the
historical absolute URL in 404.html. Original worker/map/index bytes and FontLab7
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
