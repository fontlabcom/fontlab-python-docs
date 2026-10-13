---
this_file: WORK.md
---

# Shared theme migration

## Expanded native reference rebuild

The root build now consumes current Echopy and nine ecosystem source families,
with runtime inspection disabled. Source generation includes232modules,
1894classes,244654member identities,33303unique captured bodies and4104pages.
Actual strict full render passed112.56s, peak resident3.35GB. Rendered verification
checks246779symbols and242719aliases in actual anchors/objects.inv with no gaps.
Largest current API page305773bytes; search32.57MB raw/3.49MB gzip, within declared
budgets. Locked offline --check passes.17meaningful parser/render/archive/consumer
tests and Ruff pass.

Legacy snapshot374files byte-verifies in the immutable archive. Published archive
pages keep original fragments, show version context, and old routes redirect
with location.hash preserved. Historical docs/ output remains intact while
new local output is .build/site.

Full rendering exposed C++operator[] being parsed as links and Griffe skipping
TypeRig namespace directories. Fixed upstream Markdown escaping with regression
and a source-only Griffe namespace loader using actual files. Eight TypeRig array
expressions received inline-code docstrings; runtime AST unchanged.

Actual desktop browser screenshot confirms the new homepage layout. Browser
search initially lacked its input under MaterialX search_index_only; reused this
repository's existing compatible header override. A fresh full rebuild is running
under exec session75269. Current local acceptance is partial: browser/search,
mobile/dark/keyboard, aliases beyond current extraction, source pinning/license
CI and publication still need verification. No new site deployed.

FontLab API and PythonQt source/generator configurations use MaterialX and fltheme26. The main API build passed. The 35 MB generated QtGui HTML exposed pathological nesting in MaterialX search; explicitly using the bundled ProperDocs `/search` plugin completes the PythonQt build in 64.03 seconds. Raw API bodies retain their generated HTML and anchors. The former published API stylesheet is now part of the input trees and generator post-copy trees. `./build.sh` builds the root API first, then its PythonQt child.

Final root/child rebuilds passed in 53.43/70.31 seconds. Both API and both generator configurations now set their exact Pages site_url so 404 assets and home links retain the project prefix. The core search bridge preserves all index entries (idempotency regression passes); MaterialX header/search UI works and QAbstractButton returns a matching result without browser errors.

Browser stress verification found that whole-page QtGui text was duplicated alongside section entries, consuming excessive worker memory. The search bridge now retains every section and page title while omitting duplicated whole-page bodies; payload falls from 23.8 MB to 8.0 MB and QAbstractButton search passes within a few seconds. The regression checks both preservation and idempotency.
