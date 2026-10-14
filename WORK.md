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

Source-reference-fidelity Task 1 implements those four source-extraction gaps.
Every consumed Python input is pinned once, including hidden private modules and
runtime/stub counterparts. Explicit module/class export chains now expose real
descendants; canonical source/body identities remain unchanged. Private authored
classes prefer their public package export in page and consumer headings, while
native names and existing URLs stay primary. Properties are attributes with
getter/setter/deleter occurrence records and source-only Griffe-compatible labels.

Focused verification: 33 tests pass; full suite: 41 tests pass; scoped Ruff and
diff checks pass. A strict temporary MkDocs fixture verifies actual public titles,
canonical class/member anchors and property documentation without importing its
guarded source. A read-only current-source probe preserves all previous coverage
symbols and body targets, pins 259 inputs and confirms AppHandle.close plus the
namespace/reports/identity_report properties. Current plan: 237 modules, 1,898
classes, 244,682 member identities, 33,331 bodies and 4,122 pages. Complete alias
expansion produces 490,143 aliases, including fly.qt descendants; full render and
search-size acceptance plus source-lock refresh remain with the root task.

Task 1 review round 1 fixes alias prefix overrides: replacement aliases, source
declarations and unresolved explicit prefixes suppress every inherited descendant
below that prefix, including forwarded member targets. Four covering fixtures,
37 source-inventory regressions and the 45-test full suite pass. The read-only
current-source probe matches root's refreshed 259-input lock and preserves all
490,143 existing aliases, previous symbols and body targets without build writes.

Task 1 root review round 2 qualifies whole-page native module/class search rows
from their coverage URLs, giving the fontlab module its proven fly.fl alias and
existing module/class priority. Source fragment behavior, authored sections and
member-body page titles remain intact. Six search fixtures and the 49-test full
suite pass; a read-only built-index probe confirms the exact missing module tags
and preserves empty page text and all 59,695 rows. Browser acceptance remains
with root after the scoped re-review/rebuild.

The same round also preserves source-derived signatures under exported member
headings: supported separate_signature/annotation options render method/function
arguments, defaults and returns plus property types beneath public names. The
strict guarded-source renderer fixture now verifies these with source display
disabled, alongside public class titles and canonical anchors. Full suite remains
49 passing tests; root will verify actual typed body rendering and native/public
search queries after rebuilding.

Task 1 root review round 3 verifies I2 on the shipped MaterialX consumer rather
than metadata alone. A private routed browser fixture loads the unchanged worker
and complete 38,245,018-byte / 59,695-row index; the previous module/class-equal
priority reproduces the missing fly.fl module. Supported module boost 1,000 and
class boost 100 rank its native module group first. All twelve native/public
queries pass under unchanged two-second deadlines; every original index row,
native title, text and alias tag is retained. Root's built site is not modified;
7 search fixtures, 36 focused regressions and all 50 tests pass. The complete UI
rebuild/browser acceptance remains with root.

Remaining acceptance: complete dynamic/short alias extraction, all internal
links/legacy routes and keyboard/focus behavior, --serve/--refresh-native and
artifact-mode execution, dependency/license/public-content audit, CI and actual
deployment. No new site published. Expanded ecosystem compatibility remains
active and is not established by these documentation results.

FontLab API and PythonQt source/generator configurations use MaterialX and fltheme26. The main API build passed. The 35 MB generated QtGui HTML exposed pathological nesting in MaterialX search; explicitly using the bundled ProperDocs `/search` plugin completes the PythonQt build in 64.03 seconds. Raw API bodies retain their generated HTML and anchors. The former published API stylesheet is now part of the input trees and generator post-copy trees. `./build.sh` builds the root API first, then its PythonQt child.

Final root/child rebuilds passed in 53.43/70.31 seconds. Both API and both generator configurations now set their exact Pages site_url so 404 assets and home links retain the project prefix. The core search bridge preserves all index entries (idempotency regression passes); MaterialX header/search UI works and QAbstractButton returns a matching result without browser errors.

Browser stress verification found that whole-page QtGui text was duplicated alongside section entries, consuming excessive worker memory. The search bridge now retains every section and page title while omitting duplicated whole-page bodies; payload falls from 23.8 MB to 8.0 MB and QAbstractButton search passes within a few seconds. The regression checks both preservation and idempotency.

### Source-reference fidelity acceptance

Reviewed implementation9980225 passes50tests, including actual MaterialX worker
regression on the full index. Independent scoped reviews resolve alias-prefix,
whole-page alias search, complete visible signatures/types and ranking findings.
Root strict offline build and locked check pass:259source inputs independently
discovered/hashed,246816unique source identities,490143aliases,4122pages. Search
gzip3988494bytes remains below5MiB; largest API page310685bytes below2MiB.
All12native/public browser queries resolve in at most0.030seconds after readiness;
4desktop/mobile light/dark native-anchor/layout checks and4typed public-body cases
pass with0errors/overflow. Shared4theme assets return200. Public class heading,
3attribute rows, close()->None and3MappingProxyType annotations are visible.
Exact local-path/native-review-marker scan checks4811public text assets with0hits;
this bounded scan does not replace the broader licensing/privacy release audit.

Task-specific source/render gates pass; final whole-branch review and broader
site/runtime/corpus/publication gates remain required. Source lock/TODO/plan
follow-up changes only input pins and progress evidence; no producer code/tag/
release/push/deployment. Detailed receipts remain in the parent verification
archive; historical failures are retained separately.

## Final whole-branch review fix wave

I1–I5 and M2/M3 are implemented; M1 now has an explicit non-skipping consumer
command (`./scripts/accept-consumer.sh --offline`, provisioning Chromium first).
All 66 tests pass with FONTLAB_REQUIRE_CONSUMER=1; scoped Ruff and diff checks
pass. Test-first failures reproduced shared-search omission, missing inheritance,
stale generated pages, missing accepted baseline and inaccurate root route policy.

Every shared occurrence and alias is searchable at its canonical body without
removing any existing search row/text/tag. All 15 shipped MaterialX worker queries
pass (maximum measured 0.080 seconds). A complete current-source probe preserves
246,816 symbols and every previous body target/alias; source-proven inheritance
adds 20,804 aliases, for 510,947 total. Void(Point) exposes 31 inherited members.
Griffe C3 ordering handles diamonds; local overrides remain authoritative.
Public body names do not change merely because an inherited alias is shorter.

Generation uses a fresh owned temporary tree, verifies its file set and replaces
the previous owned input tree while preserving Finder metadata. Fixture rebuilds
prove removed/renamed authored and API pages disappear from HTML and search.
After strict render/coverage acceptance, the build seals input, dependency-version
and rendered-byte manifests. --check independently regenerates and compares
without replacing the accepted baseline; missing baseline and guide/renderer/
config/template/removal/extra-file/HTML drift fail. Existing anchor/inventory
checks remain. Final full-corpus build/check are assigned to the controller.

Known legacy root hashes migrate under project prefixes; unfragmented root stays
current. Browser fixtures preserve archived anchors and ordinary page redirects.
The root exposes the archive, class pages link nested classes, and the PySide
guide documents the implemented run_app/AppHandle contract and its limitations.

Complete search has a measured cost: original gzip 3,988,494 bytes; shared-member
completion alone 6,446,911; with new inherited aliases on the existing index
6,571,419 bytes (69,896,577 uncompressed). The controller approved a provisional
7 MiB gzip bound for this fix wave conditional on complete coverage and all
15 queries within two seconds. The 2 MiB API-page bound is unchanged. R041 index
splitting/shard acceptance and restoration of the initial 5 MiB payload behavior
remain concrete parent work; this is not complete R041/site acceptance.
Clean CI wiring, source/artifact bootstrap parity, full routes/accessibility,
theme revision provenance, licenses/privacy and deployment remain unfinished.
No producer, archive original, historical docs, user font/settings or root
verification artifact was changed; no native imports, publication or deployment.

## Parent source-binding relationship correction

Declaration-time AST bindings now resolve bases in source order and the current
class-body namespace. Local declarations, subsequent imports, known class aliases
and source-known star exports establish the binding; overwritten/deleted/future,
conditional and unsupported dynamic bindings remain unresolved. Nested class
bodies use module globals rather than inheriting an outer class namespace.
Source-known registration decorators preserve class identity only under a narrow
non-mutating pattern; unknown calls and class mutation remain unresolved.

All 117 tests pass, including 51 binding cases and a strict guarded-source HTML
fixture. Scoped Ruff and diff checks pass. A read-only complete-corpus comparison
preserves 246,816 identities/body targets, every URL/body URL, all 259 source
inputs and every prior alias. Eighteen relationships correct Qt wrapper bases and
their dialog descendants, adding 10,820 proven aliases (521,767 total).

The controller owns the complete rebuild, search/browser and accepted-baseline
checks. The historical final-wave search allowance and N1 receipts remain intact;
this source-only result does not establish current full-site or release acceptance.

Parent source-binding review round 1 fixes deleted declarations recovered from
empty namespaces, stale decorator approvals/dependencies and alias-mediated class
attribute writes/deletes. Decorator policy now receives the active function AST
and live dependency bindings in a small independently tested helper. All 128 tests
pass; scoped lint/diff checks pass. Full-corpus relationships/aliases/inputs/body
targets/URLs exactly match the prior task receipt. Controller review and full-site
acceptance remain pending; earlier failed receipts and historical bounds remain.

Complete-search Task 2 implements the reviewed global token/document router with
complete original row hydration and unchanged pinned MaterialX 10.1.5/Lunr 2.3.9
consumer source. Reconciliation preserves 60,048 rows, 246,816 identities and
521,767 aliases in 63 content-addressed shards; all 822,237 token lists are checked
for valid counts/canonical varints/ranges. Original corpus remains 71,587,122 bytes
and 6,715,183 gzip bytes. Initial static transfer is 4,939,810 bytes, including
explicit gzip metadata plus uncompressed bootstrap/worker/retry UI, below 5 MiB
without assuming HTTP compression. Gzip for other startup assets yields 4,859,492 bytes.

All 135 tests pass with FONTLAB_REQUIRE_CONSUMER=1; the unchanged shipped worker
loads all 60,048 original rows and passes all 19 targets (maximum 0.084 seconds).
The new full-corpus consumer matches all 29 complete result sets, including fields,
required/prohibited clauses, quotes, fuzzy, leading/internal wildcards and
prohibited-only syntax. Configured suggestions, keyboard acceptance, prefix
specialization, plain-static gzip decoding, visible startup/row failure/retry,
corrupt metadata and stale-query suppression pass focused fixtures. Offline
compiler provisioning/recompilation succeeds from the locked npm cache; ordinary
source builds invoke committed bundles and perform no npm/npx/network fetch.

Final 100 Mbps/20 ms same-tab UI measurement passes 19 cold/warm targets, with
maxima 1.424/1.363 seconds after real metadata readiness. Local cold/warm also passes;
the retained 20 Mbps/100 ms cold run takes 2.505 seconds for fly.fl and 3.748 for Signal.
Complex complete fallback queries can take 5–8 seconds. Scores/order can vary with
candidate statistics. Raw-cache/completed-response accounting and scheduled
encoded-window bounds remain separate from sampled page/worker heap. Full-site
strict build/check/links and original navigation/OOM acceptance remain controller
Task 3 after review; no publication, native call or full-site rebuild occurred.
