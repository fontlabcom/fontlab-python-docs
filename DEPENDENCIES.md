---
this_file: DEPENDENCIES.md
---
# Documentation build dependencies

ProperDocs1.6.7 builds the site; MaterialX10.1.5 is the tested compatible theme
baseline. Evaluate10.2 against full browser/theme evidence before adopting it.
Mkdocstrings1.0.7, Python handler2.0.9, autorefs1.4.4 and Griffe2.3.2 consume
actual source/stub pairs. PyMdown Extensions render authored Markdown features.
Pytest verifies extraction and consumer contracts; Playwright verifies actual
browser interaction. All resolved packages are pinned in uv.lock.

Echopy supplies source metadata, native-named documentation aliases and the
Griffe native-facet extension. Other ecosystem package source roots provide
their own public API. Ordinary builds must consume source/artifacts off-host;
FontLab and Remopy are needed only for explicit native refresh/acceptance.

Shared fltheme26 assets retain their source/URL ownership described in THEME.md.
Capture/upstream hashes and source licenses remain part of public provenance.

Complete search uses Node 22+ at build time and committed bundles of the unchanged
MaterialX10.1.5/Lunr2.3.9 source-map sources. `scripts/search_backend/source-provenance.json`
pins all 13 original sources; generated bundles include their MIT attribution.
No Node runtime package is fetched during an ordinary/offline documentation build.
Locked esbuild 0.25.12 is needed only for explicit maintainer recompilation;
`scripts/search_backend/package-lock.json` pins its packages/integrities. Bootstrap
installs it under the ignored `.build/search-compiler` tree. Browser gzip decoding
uses the standard native `DecompressionStream` API, without another library.

## Documentation plugins

Added codeinclude 0.3.1, awesome-nav 3.3.0, live-edit 0.4.1, categories 0.6.0
and include-markdown 7.3.0. Scriptmix also uses print-site 2.9. Existing
mkdocstrings/Python/autorefs/Griffe and PyMdown provide reference and Markdown
support. MaterialX supplies meta, tags, search, native breadcrumbs and ToC.
The complete tested resolution is in uv.lock. The old breadcrumbs and
ToC-sidebar packages are excluded after compatibility trials; see
`src_docs/md/plugins.md` in the smaller sites.

## PythonQt archive search maintainer lane

The separate scripts/archive_search/package-lock.json pins official Lunr2.3.9
and esbuild0.25.12. Lunr source must equal the archived mapped dependency and
its official npm SRI; the nine unchanged mapped MaterialX modules and three
resolution modules retain individual upstream identities. No existing dependency
is upgraded. c8 10.1.3 measures the compiler; istanbul-lib-instrument6.0.3
instruments complete TypeScript modules in tests. Dependencies install only
under .build/archive-compiler, outside all hashed production-script inputs.

The PythonQt-only UI derivative additionally pins clipboard2.0.11,
escape-html1.0.3, focus-visible5.2.1, RxJS7.8.2 and tslib2.7.0, with clipboard's
exact good-listener1.2.2, delegate3.2.0, select1.1.2 and tiny-emitter2.1.0 helpers.
Preferred sources/full notices are retained under scripts/archive_search/ui.
Postcss8.5.6 and cssnano5.1.0 reproduce the frozen Mermaid CSS target set only
in maintainer tests. The existing esbuild0.25.12 compiler emits es2015 browser
syntax for the UI, retaining original JSX/strict/interop/module settings.
The existing locked Python Playwright supplies the actual DOM test runtime;
no new browser/DOM package or ordinary-build network dependency is added.
