---
this_file: README.md
---
# FontLab Python documentation

Current source-derived documentation for FontLab's native Python APIs and
scripting ecosystem. Echopy captures inside FontLab, then produces enriched,
typed Python source. Mkdocstrings renders that source under the actual native
fontlab/fontgate/fontpr/PythonQt names without runtime inspection.

## Build

Use Python3.12+ and uv. Clone the ecosystem repositories beside this checkout.

```bash
./build.sh
./build.sh --check
./build.sh --serve
./build.sh --offline
# After reviewing changed producer source:
./build.sh --update-source-lock
```

`api-sources.lock.json` pins every documented input by SHA256. Normal builds
reject missing, new or modified inputs; source changes require an explicit lock
refresh. Checkout and installed-artifact modes enforce the same bytes.

The first synchronization may fetch locked build dependencies. Subsequent offline
builds use the provisioned cache and source checkouts. To use installed artifacts,
set FONTLAB_API_SOURCE_ROOT to their Python package directory; all documented
packages must be available there. Private sources use normal authenticated GitHub
provisioning without credentials in build configuration.

Explicit ./build.sh --refresh-native captures through the running FontLab's
scripting surface, then regenerates/enriches Echopy before building the site.
It requires sibling Echopy/Remopy checkouts and FontLab. Ordinary builds do not.

The new build writes .build/site. A successful strict build seals generated-input and rendered-file manifests.
`--check` regenerates in a temporary tree and compares those manifests without
rewriting the accepted baseline; missing baselines or stale HTML fail.

Run `./scripts/accept-consumer.sh --offline` for the required build-plus-consumer
gate after dependency/source provisioning. The gate provisions Playwright
Chromium (network needed if uncached) and requires all 20 shipped-worker queries;
missing inputs cannot silently skip. Lightweight test-only runs may skip this
full-corpus case.

Accessibility acceptance is local: run `uv run python scripts/a11y_check.py --site .build/site --out
a11y.json` locally; `--pages` overrides the fixed representative page list.
Interaction receipts (deep links, type links, aliases, a deliberately late search
shard, keyboard paths) come from `uv run python -m scripts.interaction_check --site
.build/site --out DIR/receipt.json`; screenshots are written beside the receipt.

Complete search retains every original row in content-addressed page shards.
Its checked global vocabulary/postings load before readiness; queries hydrate
complete matching rows through the original MaterialX/Lunr engine. The initial
5 MiB budget includes bootstrap, metadata, worker and retry UI even on a plain
static server. Explicit `.gz` assets use native `DecompressionStream`; search
requires a modern browser and HTTP(S). API pages retain the 2 MiB limit.

Install Node 22+ before building. Ordinary builds invoke the committed pinned
engine bundle and never run npm/npx or download language assets. The current
English configuration remains intact; other languages fail explicitly until
their exact engine assets are provisioned. To update handwritten backend source:

```bash
mkdir -p .build/search-compiler
cp scripts/search_backend/package*.json .build/search-compiler/
npm ci --prefix .build/search-compiler --ignore-scripts --no-audit --no-fund
node scripts/search_backend/compile.cjs
```

The one-time compiler bootstrap installs locked esbuild 0.25.12. Later use
`npm ci --offline --prefix .build/search-compiler --ignore-scripts --no-audit --no-fund`
from its populated cache, or rebuild with the existing compiler. Commit updated
bundles and hashes together. Regular `./build.sh --offline` needs neither compiler
nor npm cache. Search failures expose Retry beside the stock search results; each Retry doubles the shard deadline.
Complex fuzzy/wildcard/prohibited-only queries can require all shards. Tested
100 Mbps/20 ms named-query latency passes; cold broad queries at 20 Mbps/100 ms
can exceed two seconds. Global BM25 scores/order can vary while complete result
sets and named target discovery are retained. Final full-site acceptance is pending.

Full coverage, browser/search and deployment
acceptance remain in progress; do not treat this source rewrite as a published
site. The historical docs/ tree remains intact until that acceptance completes.

## Coverage and archive

Each public source identity and alias has a coverage record. Class indexes retain
every member occurrence; identical captured declaration text is rendered once
and linked, without assuming native inheritance. References are paginated rather
than dropping declarations to fit page budgets.

The previous FontLab7/PythonQt site is preserved byte-for-byte in a verified
archive. Published archival pages retain original fragments and an archive banner;
old routes redirect while preserving fragments. Legacy generators remain source
history, not a Python2 dependency of the new build. Built `route-map.json` records
every old HTML route and fragment, exact current API targets when proven, and
internal links broken in the original snapshot. Build verification checks archive
anchors and redirect targets against this deterministic map. Archived pages with an exact current
identity link to it ("Current version of this page"), using the mapped
current anchor for the URL fragment when one exists.

## Shims of runtime-built APIs (issue 104)

Echopy ships static shims for APIs that only exist at run time; they render as
their own top-level references: `fontlabapp_shim` (FontLab menus, 606 QActions,
panels, glyph actions; from fontlabapp's read-only capture), `GlyphsApp` (the
module glyport synthesizes per Glyphs script; GS* classes link to fontlab_glyport)
and `aidus_code_tools` (the FontLab tools the Aidus agent calls). A shim is a
`fontlab_echopy/<name>/` package marked by `_shim.json`, which is a locked input.

## Routing and search decisions (issue 104)

- **Pages present in the archive and the current reference.** Old FontLab7 routes
  keep redirecting to their archived page, with the fragment. Only the archive
  preserves every one of the 128,733 old route/fragment pairs; 45,113 have a current
  target. Archived pages with an exact current identity carry a "Current version of
  this page" link that follows the mapped fragment. `verify_site` enforces both.
- **After the 1.8 s shard deadline.** A search whose shard misses the deadline
  shows no partial results (ranking and completeness need every candidate shard);
  it shows "Documentation search is unavailable" with Retry. Each consecutive Retry
  of the same query doubles the per-shard deadline (3.6, 7.2, 14.4, 28.8 s, capped
  at the 30 s startup deadline), so a slow but live host completes while a dead host
  still fails fast. Typing a new query resets the deadline to 1.8 s. Tested in
  `scripts/search_backend/tests.cjs` and the `search_slow_shard` interaction case.

## Examples

`examples/` is the docs export of fontlab-python-examples (`tools/docs_export.py`
there): an index, 28 category pages, insights and recipes. The build reads it
from `FONTLAB_EXAMPLES_EXPORT` (default `../fontlab-python-examples/docs-export`),
verifies every page against the export's `manifest.json` sha256s, rejects
unlisted pages, and pins the manifest and pages in `api-sources.lock.json`.
A missing export fails the build.

## Release audit

`uv run python scripts/release_audit.py --site .build/site --out audit.json` reads
every published byte (gzip shards and `objects.inv` decompressed) and fails on
local paths, the auditing user's identity, credentials, unreviewed e-mail
addresses, absolute source-map sources and missing licence texts. Upstream Qt
examples such as `/home/bob/` are allowed only in the reviewed list and scope.
The site's [licences page](site-src/licenses.md) carries every applicable text.
The written receipt redacts every finding's text and filename (digests only);
`--reveal` prints the unredacted findings to the terminal, never to a file.

## Contribute

Agree to the FontLab Individual Contributor License Agreement before contributing:
https://cla-assistant.io/fontlabcom/fontlab-python-docs.
Update source/enrichment or authored guides, regenerate, and verify real rendered
anchors, inventory, search and browser behavior. Do not edit generated output as
its source. Documentation retains the repository Apache2 license and upstream
Qt/PySide documentation attribution. Shared theme ownership is in THEME.md.

## Status

Built and verified locally (unpublished; evidence in the workspace
`verification/issue-101-ecosystem/evidence/`):

- Source-only reference from Echopy and the ecosystem packages with ProperDocs,
  MaterialX, fltheme26, mkdocstrings (Python handler), autorefs and Griffe; no
  native imports in normal builds. Strict full build about 212 s / 4.5 GB.
- Coverage report: 245,169 member identities on 4,333 pages, native aliases,
  per-class inherited indexes, declaration-time base binding (N1).
- Reconciliation (R014): every build checks coverage against Echopy's shipped
  capture identity manifest (`fontlab_echopy/_identities.json`, locked). All
  242,654 captured identities are documented, 1,216 of them under the source
  spelling of a sanitized native name (`QWidget.raise` → `raise_`,
  `QPainter::PixmapFragment` → `QPainter__PixmapFragment`), recorded in
  `coverage.json` `reconciliation.native_spellings`. Extensions, the absent
  `fontlabpr`, multiple declarations and enrichment gaps carry derived reasons.
  Any unexplained row fails the build.
- Sharded search over all 60,048 rows with a 4,940,411-byte initial transfer;
  named native searches reach the right anchors.
- Legacy routes: route map, versioned archive, fragment mapping; archived pages
  link to their current page.
- Browser acceptance (R043): keyboard, focus, deep/type links, aliases, late shard
  search, accessibility 28/28 against the published fltheme26 theme.
- Pinned API sources (`api-sources.lock.json`) and `--check` regeneration.

GitHub CI was removed by owner decision (workspace DECISIONS.md D3).
