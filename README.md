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
Chromium (network needed if uncached) and requires all 15 shipped-worker queries;
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
nor npm cache. Search failures expose Retry beside the stock search results.
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
anchors and redirect targets against this deterministic map.

## Contribute

Agree to the FontLab Individual Contributor License Agreement before contributing:
https://cla-assistant.io/fontlabcom/fontlab-python-docs.
Update source/enrichment or authored guides, regenerate, and verify real rendered
anchors, inventory, search and browser behavior. Do not edit generated output as
its source. Documentation retains the repository Apache2 license and upstream
Qt/PySide documentation attribution. Shared theme ownership is in THEME.md.
