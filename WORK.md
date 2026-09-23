---
this_file: WORK.md
---

# Shared theme migration

FontLab API and PythonQt source/generator configurations use MaterialX and fltheme26. The main API build passed. The 35 MB generated QtGui HTML exposed pathological nesting in MaterialX search; explicitly using the bundled ProperDocs `/search` plugin completes the PythonQt build in 64.03 seconds. Raw API bodies retain their generated HTML and anchors. The former published API stylesheet is now part of the input trees and generator post-copy trees. `./build.sh` builds the root API first, then its PythonQt child.

Final root/child rebuilds passed in 53.43/70.31 seconds. Both API and both generator configurations now set their exact Pages site_url so 404 assets and home links retain the project prefix. The core search bridge preserves all index entries (idempotency regression passes); MaterialX header/search UI works and QAbstractButton returns a matching result without browser errors.

Browser stress verification found that whole-page QtGui text was duplicated alongside section entries, consuming excessive worker memory. The search bridge now retains every section and page title while omitting duplicated whole-page bodies; payload falls from 23.8 MB to 8.0 MB and QAbstractButton search passes within a few seconds. The regression checks both preservation and idempotency.
