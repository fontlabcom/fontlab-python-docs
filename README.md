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

The new build writes .build/site. Full coverage, browser/search, CI and deployment
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
history, not a Python2 dependency of the new build.

## Contribute

Agree to the FontLab Individual Contributor License Agreement before contributing:
https://cla-assistant.io/fontlabcom/fontlab-python-docs.
Update source/enrichment or authored guides, regenerate, and verify real rendered
anchors, inventory, search and browser behavior. Do not edit generated output as
its source. Documentation retains the repository Apache2 license and upstream
Qt/PySide documentation attribution. Shared theme ownership is in THEME.md.
