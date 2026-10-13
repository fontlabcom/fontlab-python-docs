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
