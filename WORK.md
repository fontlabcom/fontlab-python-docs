---
this_file: WORK.md
---

# Shared theme migration

## Expanded native reference rebuild

The root build consumes captured/enriched Echopy and nine source families with
runtime inspection disabled. Current inventory: 232 modules, 1,894 classes,
244,654 member identities, 33,303 unique captured bodies and 4,104 pages. Strict
full offline render passed in 118.37s. Actual HTML and every expected inventory
URI verify 246,779 source symbols and 242,719 aliases without missing anchors.
Largest current API page: 310,685 bytes; initial search: 3,818,297 bytes gzip.
Locked offline --check passes; 23 meaningful tests and Ruff pass.

Search retains native qualified names, skips word stemming, includes explicit
aliases and prefers module/class identities over incidental prefix matches.
Actual Chromium finds all nine required searches within 0.08s after readiness,
including native QWidget.resize, Signal, fly.fl and late QXmlQuery.setQuery.
The method page has no viewport overflow at 1440/390px in light/dark modes;
deep anchors scroll into view, four shared theme assets return 200, and browser
errors are absent. Screenshots wait for theme transitions to settle.

Echopy now renders reference overloads as separate code lines. Source inputs are
pinned by SHA256 in api-sources.lock.json; ordinary builds reject changes until
explicit --update-source-lock. Installed-artifact mode uses the same byte pins.
Legacy archive retains 374 byte-verified files and versioned fragment routes.
Historical docs/ remains intact; current local output is .build/site.

Runner-source refresh: strict offline build 121.10 seconds and locked offline
check pass after adding the reviewed Pythonqtside runner inputs. Current inventory
is 237 modules, 1,897 classes, 244,678 member identities and 4,119 pages; coverage
SHA256 1484dc3a159cc1816216837b90d54f1686f86791f3365a727c85902f0c16f835.
All expected source/inventory anchors pass. Nine previous real browser searches,
desktop/mobile light/dark layout and four shared theme assets pass again. New
public searches pythonqtside.AppHandle/run_app resolve in 0.024 seconds each;
AppHandle.close index anchors render at both widths without overflow or errors.
The source-derived method bodies remain linked from their member index.

Concrete remaining fidelity checks: expand public class aliases to member aliases
(pythonqtside.AppHandle.close is absent), prefer public exported class names in
page titles, classify @property correctly in the AST member index, and lock every
source file consumed during alias extraction, including otherwise hidden private
modules. These observations are retained in the runner-docs-refresh receipt;
the passing verifier covers its enumerated symbols, not these missing semantics.

Remaining acceptance: complete dynamic/short alias extraction, all internal
links/legacy routes and keyboard/focus behavior, --serve/--refresh-native and
artifact-mode execution, dependency/license/public-content audit, CI and actual
deployment. No new site published. Expanded ecosystem compatibility remains
active and is not established by these documentation results.

FontLab API and PythonQt source/generator configurations use MaterialX and fltheme26. The main API build passed. The 35 MB generated QtGui HTML exposed pathological nesting in MaterialX search; explicitly using the bundled ProperDocs `/search` plugin completes the PythonQt build in 64.03 seconds. Raw API bodies retain their generated HTML and anchors. The former published API stylesheet is now part of the input trees and generator post-copy trees. `./build.sh` builds the root API first, then its PythonQt child.

Final root/child rebuilds passed in 53.43/70.31 seconds. Both API and both generator configurations now set their exact Pages site_url so 404 assets and home links retain the project prefix. The core search bridge preserves all index entries (idempotency regression passes); MaterialX header/search UI works and QAbstractButton returns a matching result without browser errors.

Browser stress verification found that whole-page QtGui text was duplicated alongside section entries, consuming excessive worker memory. The search bridge now retains every section and page title while omitting duplicated whole-page bodies; payload falls from 23.8 MB to 8.0 MB and QAbstractButton search passes within a few seconds. The regression checks both preservation and idempotency.
