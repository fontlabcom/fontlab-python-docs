---
this_file: WORK.md
---

# Shared theme migration

## 2026-10-14 — R043 checker correction from controller receipt

Read the controller's complete `a11y-first.json`: 28 results with 633 failures
(278 focus, 183 contrast, 88 unmeasurable, 56 names, 28 keyboard reach).
The focus sample already recognised `auto` as visible; its indicator failed
because the MaterialX skip link begins with opacity zero and fades in over
250 ms. Focus measurement now waits two animation frames and for active-element
and ancestor transitions (bounded at 700 ms), recognises non-none positive-width
outlines, and records rendered/visible state. No-ring or off-screen focus still
fails. Body focus resets the starting point before the traversal.

Names now trim each candidate, resolve explicit label[for]/aria-labelledby and
exclude unrendered controls. Any control actually reached by Tab is checked
again, so hidden-looking but keyboard-focusable unnamed controls still fail.
Search targets the real field or focusable trigger, not the non-focusable mobile
icon label. Navigation targets the first rendered link rather than the hidden
desktop logo. An absent skip link is optional; existing skip/search/nav targets
must be reached in any order within 40 Tabs. Focus-indicator checks continue for
the complete Tab cycle, including elements after the reachability bound. This
is the project's sample bound,
not a WCAG tab-count or ordering requirement.

Unmeasurable contrast is retained separately as non-failing `needs_manual`.
Known ratios below 4.5 still fail without rounding the comparison. Fully
transparent text without a text shadow fails even over an unknown background.
Ten new browser fixtures cover auto rings/transitions, hidden and explicitly
labelled controls, opacity-zero unnamed focusable controls, responsive targets,
untabbable navigation, manual contrast, transparent text and off-screen focus.
Three browser-independent receipt tests prove manual findings remain non-failing,
observed keyboard focus retains the naming requirement, and the reachability
bound does not truncate focus checking.

The controller's original 183 contrast failures have eight distinct combinations
(foreground RGBA; background RGB; ratio; element/content type; occurrences):
- (64,81,181,1); (30,33,41); 2.346942; p/body; 2.
- (226,228,233,.56); (53.52,56.4,64.04); 4.063016; a/link; 2.
- (147,131,226,1); (39,42,53); 4.483287; span/code; 8.
- (230,105,91,1); (39,42,53); 4.449907; span/code; 12.
- (84,136,232,1); (36.3,39.24,47.09); 4.298601; a/link; 136.
- (226,228,233,.56); (53.52,56.4,64.04); 4.063016; div/body; 12.
- (64,81,181,1); (33.4,37.8,55); 2.193786; span/link; 7.
- (84,136,232,1); (39,42,53); 4.128278; code/code; 4.
Values above are rounded for display only; the receipt retains full precision.

Corrected existing-site audit attempted: `/private/tmp/fontlab-a11y-corrected.json`
records installed Chromium's sandbox Mach-port launch denial (1100), zero page
results and a failed operational gate. No corrected-site pass/count is claimed.
Focused non-browser checker tests: 4 passed, 22 deselected. Scoped Ruff, JavaScript
syntax and diff checks pass. Required full run with writable UV_CACHE_DIR:
**150 passed, 3 failed, 22 browser fixture setup errors in 15.88s**. All failing
browser launches report the sandbox Mach-port denial; the original three failures
remain unchanged, and browser tests are not skipped for installed-but-blocked
Chromium. The controller must rerun the corrected audit and all browser
fixtures with Chromium launch permitted, and review `needs_manual` separately.
No theme, generated site, archive, source lock or TODO changes in this correction.

## 2026-10-14 — R043/R044 accessibility and CI

Added `scripts/a11y_check.py` and its DOM measurement helper. The fixed sample is
index, install/native/PySide guides, flNode, Signal and the FontLab 7 archive
index. Every page runs at 1280×800 and 375×812 with light/dark media emulation
and the MaterialX palette when available. A complete Tab cycle measures focused
outline/shadow changes and reachability of skip/search/first navigation links.
DOM checks cover one h1, heading progression, image alt attributes and control
names. Text-node contrast composites ancestor backgrounds and foreground alpha
against the browser canvas colour; the minimum remains 4.5:1. Gradients/images,
opacity and blending produce explicit unmeasurable failures rather than passes.
Receipts include page/viewport/scheme, selectors and measurements; operational
errors also produce a failing receipt. Tiny static fixtures cover every rule.

Added `.github/workflows/docs.yml`: Ubuntu, Python 3.12, uv, Node 22, all nine
sibling producer checkouts, Chromium/system-library provisioning, locked tests,
network-enabled consumer acceptance, build check and accessibility acceptance.
Receipts/site upload even when a gate fails. `api-sources.lock.json` has only
schema_version and source-file hashes, so producer default branches are used;
the existing build rejects byte drift. README documents FONTLAB_DOCS_READ_TOKEN
for eight private repositories and states that CI is not deployment.

Fresh required full gate with a writable UV_CACHE_DIR: **147 passed, 3 failed,
12 browser fixture setup errors** (12.68s). Before changes the same sandbox had
145 passed and the same three existing browser failures. All 15 unsuccessful
browser cases encounter installed Chromium's macOS MachPortRendezvous launch
denial (Permission denied 1100); new tests skip only for absent Chromium, never
for launch denial. A separate non-browser diagnostic passes all 147 tests with
15 browser cases explicitly deselected (5.67s); this is not the required full
gate passing. The two added non-browser regressions pass. Workflow YAML
parses with installed locked PyYAML (21 steps); `uv lock --check`, scoped Ruff,
JavaScript syntax and diff checks pass. The attempted existing-site audit wrote
`/private/tmp/fontlab-a11y.json` with a browser-launch failure and zero page
results: no real-site accessibility findings can be claimed in this sandbox.

Controller must rerun the complete tests and real-site accessibility audit where
Chromium can launch, inspect all 28 sample results, provision the read secret and
run clean CI to verify private checkout, source-hash agreement, consumer gate,
build check and artifact retention. Full build/consumer acceptance was not run
locally. No theme, archive, generated output, source lock or TODO items changed;
no commit or deployment. Browser acceptance remains unverified here.

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

Task 2 review fix round 1 corrects status-channel restoration after persisted
pagehide/pageshow: close on hide, reopen/rebind on restored show, request the
worker's current status and reconcile Retry before enabling it. A bounded real
Node BroadcastChannel fixture covers two restoration cycles, subsequent failure,
retry and cleanup. Actual Chrome persisted Back/Forward remains a controller gate.
Original Lunr QueryParseError now returns an ordinary empty RESULT; network and
corruption remain unavailable. Actual compiled-worker and configured stock UI
fixtures cover Signal~x, Signal^foo and title:Signal~x without hiding transport errors.
Seventeen Node checks and ten focused Python/UI/shard/site tests pass; scoped
lint/diff checks pass. Current static startup is 4,940,411 bytes (production gzip
4,859,641); the original corpus/shard counts are unchanged. The report distinguishes
the prior 4,859,492 production accounting from 4,859,537 measured harness bytes.
No unchanged full suite/benchmark or full-site build was repeated in this round.

## 2026-10-14 — R042 legacy route map

Added deterministic built-root `route-map.json` (schema 1, archive version
`FontLab7`). Each original HTML route records archive/current targets, every ID
and named anchor, fragment targets, match classification and reason. Only exact
qualified filenames, IDs or heading text found in current symbols/public aliases
receive current targets; ambiguous and unmatched fragments remain archive-only.
All redirects continue to preserve original archive fragments. Original internal
HTML hrefs are resolved relative to their source, including project-prefixed and
same-site absolute URLs, queries and percent-encoded fragments. Unresolved links
are separately classified `broken-in-original`; repeated identical hrefs on one
page count once.

The existing archive publisher emits the map through the post-build hook using
current coverage. Site verification independently recomputes it from the pinned
original tarball and current coverage, checks actual archived IDs/named anchors,
and checks redirect policies, JavaScript, meta refresh, fallback links and root
fragment migration. Missing maps, routes, fragments, archive pages or disagreeing
current/archive targets fail. Root and 404 retain their existing current-page
exceptions. No source-lock refresh or TODO changes.

Read-only real-data probe against existing `.build/coverage.json`: 278 HTML
routes, 128,733 unique route/fragment pairs, 221 exact current page targets,
45,113 exact current fragment targets, 96,989 broken original source/href pairs.
This uses the existing coverage artifact rather than regenerating producer input.

Verification (commands routed through `rtk proxy`):
- `uv run --frozen pytest -q tests`: blocked by default uv cache write permission.
- `env UV_CACHE_DIR=/private/tmp/fontlab-route-uv UV_OFFLINE=true uv run --frozen pytest -q tests`:
  14 collection errors because the console entry point omits the repository import path.
- `env UV_CACHE_DIR=/private/tmp/fontlab-route-uv UV_OFFLINE=true uv run --frozen python -m pytest -q tests`:
  145 passed, 3 failed. The same three baseline browser tests fail at Chromium
  launch because sandboxed macOS Mach-port registration is denied; baseline was
  131 passed, 3 failed. No network was used.
- `env UV_CACHE_DIR=/private/tmp/fontlab-route-uv UV_OFFLINE=true uv run --frozen python -m pytest -q tests/test_legacy_route_map.py tests/test_site_verification.py`:
  18 passed, covering exact/fallback mappings, fragment preservation, original
  broken links, encoded/prefixed URLs, determinism and verification failures.
- `ruff check scripts/legacy_route_map.py scripts/legacy_archive.py scripts/site_hooks.py scripts/verify_site.py tests/test_legacy_route_map.py tests/test_site_verification.py`:
  passed. Scoped `ruff format` applied; `git diff --check` passed.

Wait, but the full gate is not green in this sandbox: browser launch remains
blocked. The controller still owns the full build/check and browser acceptance.
No full build/native refresh, archive/manifest edits, generated-site writes,
theme changes, dependency changes, publication or commit were performed.

## 2026-10-14: R043 accessibility audit and R044 CI workflow (controller)

Controller re-ran 175 tests (pass) and the corrected checker on the strict
offline build: 28 page/viewport/scheme results, 433 failures (focus 250:
198 focusable elements off-viewport, e.g. closed drawer links, and 52 with no
focus indicator, mostly search inputs; contrast 183 across 8 colour pairs,
worst 2.19:1 link/primary on dark), 88 needs_manual. These are shared-theme
(fltheme26/MaterialX) defects; fixes belong in fontlab-www-docstheme per
AGENTS.md. Receipts: parent verification/issue-101-ecosystem/evidence/tg6-a11y/.
CI workflow added but not yet run on GitHub (needs FONTLAB_DOCS_READ_TOKEN).

## 2026-10-14: CI workflow removed (owner decision D3)

Deleted .github/workflows/docs.yml and its test; the private-repository read token is not wanted. Builds, checks and accessibility audits stay local.

## 2026-10-14: R043 checker — closed mobile navigation via opener (baf9077)

With the fixed shared theme, closed mobile drawers are inert, so a visible nav link
is correctly unreachable at 375 px. `a11y_checks.js` now targets the focusable
element whose `aria-controls` panel contains navigation links; `a11y_check.py`
activates it with Enter and requires focus inside the panel (`nav_after_open`
failure otherwise). Two new fixtures (working and broken disclosure). 28 tests pass.
Audit of `.build/site` against the published theme: 28/28 cases pass, 0 failures.

## 2026-10-14: R043 interaction receipts (Task 1 of plans/2026-10-14-r043-interactions.md)

Added `scripts/interaction_check.py` (5 cases x 1280x800/375x812 x light/dark),
fixtures in `tests/fixtures/interactions/` and `tests/test_interaction_check.py`
(21 tests; each check shown to pass and fail). No build, no `--refresh-native`.

Commands (all from this repository):
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q tests/test_interaction_check.py`: exit 0, 21 passed.
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q`: exit 0, 198 passed.
- `rtk proxy uvx ruff check scripts/interaction_check.py tests/test_interaction_check.py`: exit 0.
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m scripts.interaction_check --site .build/site --out ../verification/issue-101-ecosystem/evidence/r043-interactions/interaction-receipt.json`:
  exit 1 (FAIL), ~3 min. Summary: deep_link 4/4, type_link 0/4, alias 4/4, search 4/4, keyboard 4/4.
  20 screenshots + receipt + SHA256SUMS in that evidence directory.

Results on `.build/site`:
- Deep link `flNode.html#fontlab.flNode.isExtreme`: lands at top ~72 px under a 48 px
  sticky header; hit test finds no fixed/sticky element covering it.
- Type link: **site defect.** `fontlab_remopy.control.FontLab.run` renders
  `run(code: str, /, **variables: Any) -> ExecutionResult` with no link, although
  `fontlab_remopy.execution.ExecutionResult` has its own page. A scan of all
  `.build/site/reference/**/*.html` signatures found 33,353 signature code blocks,
  0 containing links. Probable cause: mkdocs.yml's mkdocstrings-python options lack
  `signature_crossrefs` (2.0.9 needs `separate_signature` with it). Not fixed here;
  it needs a config change and a full rebuild.
- Alias `fly.fg.fgKerning`: objects.inv maps the alias and `fontgate.fgKerning` to the same
  URI. Searching for the alias returns the canonical hit, which MaterialX folds under
  "1 more on this page"; the check expands it, clicks, and lands on
  `reference/fontgate/fgKerning.html#fontgate.fgKerning` in view. The legacy route
  `fontgate.fgAnchor.html#-fontgate.fgAnchor.copy` redirects with its fragment to the
  archive page (anchor in view). Recorded, not asserted: the route map has
  `current_route` reference/fontgate/fgAnchor.html#fontgate.fgAnchor, but no current
  mapping for this dashed fragment. Legacy redirects go to the archive, not to the
  current API page.
- Late search `decode_execution`: the target row lives only in shard 58 of 63. With a
  1500 ms Playwright route delay on that `.gz`, the result is absent at delay-200 ms and
  appears at 1522-1657 ms. Clicking it opens the page in the same tab; Back returns to flNode.
  Note: the worker aborts each shard fetch at 1800 ms (`query.js`), so any shard slower
  than 1.8 s shows the Retry/error state. A blocking `time.sleep` delay serialised the
  10 per-keystroke shard requests past that deadline; the check uses `page.wait_for_timeout`.
- Keyboard: skip link at Tab 1, navigation at 2 (on mobile, the drawer opener
  `#fl-native-navigation`, then Enter reaches a link), search at 4. Skip link + Enter + Tab
  focuses the first content link. Shortcuts `/` and `s` focus search on desktop, but not
  at 375 px (recorded only).
- Every screenshot's palette matches the requested scheme (default/slate). Reviewed
  search-375-dark, deep_link-1280-light, type_link-1280-dark, alias-375-dark and
  keyboard-375-dark/1280-light: each shows what its receipt claims.

TODO.md not ticked: R043 type links still fail.
