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

## 2026-10-14: R043 interaction receipts, fix round 1

- Type-link check now reads the member's own `.doc-object` `.doc-signature`
  (mkdocstrings-python `separate_signature` layout). It falls back to the heading
  code for the inline layout and ignores nested members' signatures. New
  `sig_separate.html` fixture covers a parameter link and a return link (pass),
  plus an unlinked signature and a class with only a nested linked signature (fail).
  The new `param_type_link` case uses `fontlab_glyport.receipt.write_receipt(receipt: Receipt, ...)`,
  targeting `reference/fontlab_glyport/receipt/Receipt.html#fontlab_glyport.receipt.Receipt`.
- New `search_slow_shard` case records current behaviour: with the target shard
  delayed 2500 ms (above the 1800 ms worker deadline), search shows "Documentation
  search is unavailable. Retry search" and no result. Passes when Retry appears. The
  worker is unchanged. The run loop now calls `context.unroute_all(behavior="ignoreErrors")`
  because route callbacks still waiting crashed the next context.
- mkdocs.yml: set `separate_signature: true` and `signature_crossrefs: true`
  (committed separately). **Not verified by a build.** `rtk proxy ./build.sh --offline`
  exit 1 after 18 s: `ValueError: API source lock differs: fontlab_glyport/__init__.py,
  _strict.py, errors.py, execution.py, glyphsapp/{__init__,application,bridge,defaults}.py,
  model/{__init__,backend}.py, ...`. The sibling fontlab-glyport moved to 28b8842
  ("Probe-safe model proxies and context close hooks"). Per instructions I did not
  run `--update-source-lock`, so the controller must review the glyport diff and refresh the lock.
  `.build/site` is unchanged (old inline-signature layout). So a11y_check, `--check`,
  site verification and the rebuilt-site receipt were not re-run. The previous a11y result
  (28/28 on this same site, baf9077) still applies to it.
- Commands: `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q tests/test_interaction_check.py`
  exit 0, 27 passed. `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q` exit 0,
  204 passed. `rtk proxy env UV_OFFLINE=true uv run --frozen python -m scripts.interaction_check --site .build/site --out ../verification/issue-101-ecosystem/evidence/r043-interactions/interaction-receipt.json`
  exit 1: deep_link 4/4, type_link 0/4, param_type_link 0/4, alias 4/4, search 4/4,
  keyboard 4/4, search_slow_shard 4/4. Evidence: 28 PNGs, receipt and SHA256SUMS (29 lines).
- Route-map question for the controller: the legacy route `fontgate.fgAnchor.html#-fontgate.fgAnchor.copy`
  redirects (meta refresh plus `location.replace`) to
  `archive/fontlab7/fontgate.fgAnchor.html#-fontgate.fgAnchor.copy`, which is the target in
  `legacy-routes.json` (fragment_policy `preserve`). `route-map.json` also records
  `current_route` `reference/fontgate/fgAnchor.html#fontgate.fgAnchor` for this page,
  with `current: null` for the dashed fragment; undashed `fontgate.fgAnchor.copy` maps to the current page.
  No redirect or archive banner link sends readers to the current route. Should legacy
  routes with an exact current identity redirect to the current page, or at least link to it?

## 2026-10-14: Controller source-lock refresh, rebuild and R043 acceptance

Producer review: every changed or new API input since the last lock comes from this
session's reviewed commits in fontlab-glyport (UI graph/vanilla slices, GlyphsApp facade,
integration tasks) and pythonqtside (inventory routing, phases 3–3d). Then
`./build.sh --offline --update-source-lock`: exit 0, 215.66 s, 4,509,564,928 B max RSS.
Gates on the rebuilt site (separate_signature + signature_crossrefs):
`uv run python -m scripts.interaction_check --site .build/site --out …/receipt-after-rebuild.json`
PASS — deep_link, type_link, param_type_link, alias, search, keyboard, search_slow_shard
each 4/4 (type links were 0/4 before); `scripts/a11y_check.py` PASS (28/28);
`uv run --frozen python -m pytest -q` 204 passed; `./build.sh --offline --check` exit 0
(56.98 s, 2.67 GB). Evidence: parent verification/issue-101-ecosystem/evidence/r043-interactions/.
Open: route-map question (legacy fontgate.fgAnchor.html redirects to the archive though a
current route exists); search shard timeout 1.8 s shows Retry (recorded, unchanged).

## 2026-10-14: R042 route-map question resolved — archive pages link their current page

Decision. Legacy routes keep redirecting to the archive; archived pages with an exact
`current_route` gain a visible "Current version of this page" banner link. Justification
against R042:
- "Every known old route receives a verified redirect or preserved archived page,
  including deep links": the archive is the only target that keeps every deep link.
  Of 128,733 route/fragment pairs, 45,113 have a current target. Redirecting to current
  pages would strand the rest, e.g. `fontgate.fgAnchor.html#-fontgate.fgAnchor.copy`
  (`current: null`). The redirect target logic matches the route map (`archive_route`)
  and `verify_route_map` already enforces it, so it is not wrong and was not changed.
- "Archive content stays clearly versioned and discoverable" and the map's purpose
  (old-to-current): the banner keeps "FontLab7 archive" and now links the exact
  current page, so readers who land on the archive can reach the current version.
- The link is generated in `publish_archive` from the same `make_route_map` report it
  writes to `route-map.json` (no hand edits). `href` is the page-level `current_route`;
  `data-fragment-targets` holds only fragments with a non-null current target. A small
  inline script retargets the link on load and `hashchange` (percent-decoded hash),
  falling back to the page target. Pages without `current_route` get no link, including
  10 `exact-identity` pages whose only matches are fragments (out of scope, recorded here).
- `verify_route_map` now requires, per route, exactly the expected link and fragment
  map plus the script when `current_route` exists, and no link otherwise. The interaction
  receipt asserts the link on the real archived legacy target.
- The banner HTML insertion now splices at the `<body>` match, not via a regex
  replacement string (JSON backslashes would have been reinterpreted). A page with a
  current route and no `<body>` fails the build.

Tests: `tests/test_legacy_route_map.py` adds nested-route/unmapped-fragment helper tests,
banner presence/absence, a quote/backslash/non-ASCII fragment round trip, four
tamper cases (missing/wrong link, wrong fragment map, extra link) and a fixture browser
test (redirect with fragment, Tab reaches the link, Enter lands on the current anchor in
view, unmapped fragment falls back to the page target, `hashchange` retargets).
`tests/test_site_verification.py` fixture now publishes its archive with its own
coverage. `tests/test_interaction_check.py` adds pass and mismatch cases.

Commands (exit codes):
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q tests/test_legacy_route_map.py tests/test_legacy_archive.py tests/test_site_verification.py`: 0, 28 passed.
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q tests/test_interaction_check.py`: 0, 28 passed.
- `rtk proxy ./build.sh --offline`: 0, 212.39 s, 4,518,182,912 B max RSS (no lock refresh).
  Spot check: `.build/site/archive/fontlab7/fontgate.fgAnchor.html` links
  `../../reference/fontgate/fgAnchor.html#fontgate.fgAnchor` with `fontgate.fgAnchor.copy`
  in its fragment map; 221 archived pages carry the link (= routes with `current_route`).
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m scripts.interaction_check --site .build/site --out ../verification/issue-101-ecosystem/evidence/r043-interactions/receipt-after-route-fix.json`:
  0, PASS, every case 4/4; alias legacy link = `reference/fontgate/fgAnchor.html#fontgate.fgAnchor`.
- `rtk proxy env UV_OFFLINE=true uv run --frozen python scripts/a11y_check.py --site .build/site --out ../verification/issue-101-ecosystem/evidence/r043-interactions/a11y-after-route-fix.json`:
  0, PASS. Its page list includes only `archive/fontlab7/index.html` (no current link),
  so link accessibility rests on the fixture browser test.
- `rtk proxy env UV_OFFLINE=true uv run --frozen python -m pytest -q`: 0, 213 passed.
- `rtk proxy ./build.sh --offline --check`: 0, 57.19 s, 2,532,868,096 B max RSS.
- Evidence SHA256SUMS regenerated over 37 files (build/check logs saved as
  `route-fix-build.log`, `route-fix-check.log`).

TODO "Preserve legacy routes…" stays open: the static-host browser check at the
deployed project prefix (R042/R044) is still outstanding.

## 2026-10-15: Issue 104 lane L5 — R014 coverage reconciliation

Capture `5a405eb5…` (verification/issue-101-ecosystem/echopy-refresh/) is the
generation input; `fontlab-echopy/.local/native.json` (`d7d0c6f1…`) is not.
Before: 1,230 of 242,654 captured identities had no coverage symbol or alias
(573 keyword members, 15 C++-named classes with 628 constructors/members, 14
single-underscore members dropped by the inventory). Fixes: Echopy ships the
identity manifest with native spellings; the inventory keeps `_x` members in
native sidecars; `reconcile_coverage` runs in every build.

Lock: only Echopy-owned entries refreshed by hand (`_identities.json`,
`_provenance.json`, `tooling/cli.py`, `tooling/identities.py`). Other lanes'
uncommitted/unreviewed changes (fontlabapp, pythonqtside, glyport,
aidus-code) are not locked, so source-mode builds fail the lock until the
controller reviews them. The build ran in installed-artifact mode against a
staged root holding exactly the locked bytes.

- `UV_OFFLINE=true uv run --frozen python -m pytest -q`: 0, 220 passed.
- `FONTLAB_API_SOURCE_ROOT=<staged locked root> ./build.sh --offline`: 0, 223.76 s,
  4,515,446,784 B max RSS; reconciliation 242,654/242,654 documented, 0 unexplained.
  Evidence: verification/issue-101-ecosystem/evidence/docs-104/r014-*.

## 2026-10-15: Issue 104 lane L5 — build modes, determinism, audit, decisions

All builds below ran from the locked bytes (artifact root staged with
`evidence/docs-104/stage_locked.py`; source mode in a sibling-layout copy of the
same bytes, because other lanes' unreviewed changes fail the lock).

- Shard deadline decision: no partial results after 1.8 s; Retry doubles the
  deadline (cap 30 s). `node --test scripts/search_backend/tests.cjs`: 18 pass.
  `search_slow_shard` now clicks Retry and requires recovery: 4/4 on the real site.
- Archive routing decision recorded in README (unchanged behaviour, see 2026-10-14).
- `scripts/release_audit.py`: 5,193 files incl. decompressed shards and
  objects.inv; pass, 0 findings; upstream Qt examples (`/home/bob/`, `file:///`,
  `user@foo.com`) allowed only by reviewed list and scope. Licences page added.
- Artifact rebuild twice: generation and 5,191 rendered files identical.
- Source mode vs artifact mode: rendered files identical; only the generation
  `config` digest differs (absolute source paths in mkdocs.yml, by design).
- `./build.sh --offline --check` (artifact): exit 0, 62 s.
- `./build.sh --offline --serve` (source mode): serving on
  `http://127.0.0.1:8000/fontlab-python-docs/`; probed pages 200; stopped by signal.
- `scripts/deployed_check.py` and `interaction_check --base` against the real site
  mounted under `/fontlab-python-docs/` locally: 785 targets byte-equal; all
  interaction cases 4/4.
- Tests: `UV_OFFLINE=true uv run --frozen python -m pytest -q` 226 passed before
  deployed_check; deployed_check + interaction tests 31 passed.
Evidence: parent `verification/issue-101-ecosystem/evidence/docs-104/`.

## 2026-10-15: Issue 104 lane L5 — shim documentation

Shims from echopy (fontlabapp_shim from fontlab-fontlabapp 9cbaf69; GlyphsApp and
aidus_code_tools generated by `fontlab-echopy shims`). Root fixes found by the
strict build: `docnames` now exports module-level type aliases (`ActionPath`);
the inventory registers shim re-exports under the documented name
(`GlyphsApp.GSFont` → `fontlab_glyport.model.proxies.GSFont`).
Artifact build (locked bytes): exit 0, 216 s; 4,503 pages, 246,038 member
identities; fontlabapp_shim 920, GlyphsApp 21, aidus_code_tools 5 identities;
reconciliation 242,654/242,654, 0 unexplained. `--check` 0; release audit pass
(5,365 files); interaction 4/4 all cases; a11y PASS.

## 2026-10-15: Issue 104 lane L5 — intermittent keyboard check fixed at the root

Two harness causes, no site bug (diagnosis: parent
`verification/issue-101-ecosystem/evidence/docs-104/keyboard-flake-fix/DIAGNOSIS.md`):
1. `serve_site` listened with Python's default backlog of 5; Chromium's
   per-load socket burst reset the MaterialX bundle request in ~1 load in 30, so
   `no-js` stayed and `.no-js .md-search` hid search. `SiteServer` sets 128:
   0 resets in 300 loads; real keyboard check 0 failures in 200.
2. `networkidle` waited on MaterialX's api.github.com repository facts (8–10 s,
   rate-limited): 4 timeouts in 120 loads. `open_page()` waits for `load` plus the
   page's own readiness (`no-js` removed): 0 timeouts, none over 3 s in 120.
Five consecutive `interaction_check` runs: all PASS, every case 4/4. a11y PASS.
`UV_OFFLINE=true uv run --frozen python -m pytest -q`: 233 passed.

## 2026-10-15: Issue 104 lane L5 — review rounds R-L5-docs and RR-docs, final rebuild

Fixed test-first: credential formats (incl. `github_pat_`); JSON parsed and
`\u002f`/`\/` escapes decoded (inline maps, gzip shards, scripts) before path
and secret checks; private repository URLs/names (from local git remotes,
redacted in receipts), volume and checkout paths; exact reviewed values;
licence texts by digest and page links; structural declaration reasons with
line-pinned reviews; aliases discarded by resolution; deployed_check asset
coverage and header validation. Final-rebuild attempts exposed and fixed:
tuple-unpacked declarations never indexed (inventory + Griffe extension), a
literal `<title>` docstring swallowing three pages (escaped outside code), and
upstream redefinitions (fontlabapp MENU_API, TypeRig test_objects d1/d2,
TypeRig trAnchor.y missing @y.setter). The runbook now builds from a
git-archive snapshot of producer HEADs. Docs tests: 257 passed.
Evidence: parent `verification/issue-101-ecosystem/evidence/docs-104/final*`.

2026-10-15 workspace reconciliation: fresh source suite 269passed/0skipped, exit0.
Exact command and retained initial failures: parent verification/plan-todo-audit-20261015/baseline-tests.json.
Completed repository plans were archived where no repository tasks remain;
workspace integration/release gates remain separate.

## 2026-10-15: issue 106 lane C3 — consolidated rebuild; nested-escape audit gap

Lock review: inputs computed from a git-archive snapshot of every producer HEAD
(echopy 6ff0d24, fontlabapp dd96cb0, remopy 0eeb15a, grablab 2473ee1, pythonqtside
0255411, fly bc20854, typerig-lib ccb2f0b, glyport df8afe6, aidus-code 957ff44,
examples 605f829) equal the committed lock f790088: 0 package differences, 41/41
examples pins. Runbook `final-rebuild.sh` (evidence parent
`verification/issue-106/evidence/C3/final-1/`): all 16 gates exit 0, 5/5 interaction
runs, determinism identical, 242,654/242,654 identities, 652 shim exports, 269 docs
tests, release audit 5,817 files pass; lock unchanged afterwards (`git diff --quiet`).

End-to-end replay on an APFS clone of the built site (evidence `C3/escaped-json-replay/`):
`\/`, `/`, gzip JSON and `github_pat_` carriers were flagged, but a JSON value whose
decoded text still holds `\/Users\/…` and JSON nested inside a JSON string were not.
`decoded_forms` now escape-decodes parsed strings again and re-parses JSON-looking
strings (depth 3). New test failed first, then 21/21 audit tests pass; the real site
still passes (5,817 files, 135 s); the clone flags all six carriers.
Follow-up: the first new test cases were caught by the second unescape alone; added a
carrier (nested JSON whose inner value is double-escaped) that fails with `depth=0`
and passes with the shipped `depth=3` (21 passed). Test-only change: the 88 build
inputs (`scripts/`, `site-src/`, `overrides/`, `archive/`, config) equal final-2's
accepted manifest. Final-2 (runbook at a211a02): all 16 gates exit 0, 270 docs tests.

## 2026-10-15: issue 106 lane C3 — X4b audit findings fixed

X4b (REQUEST CHANGES) on a211a02: percent, HTML-entity and `\x` encodings bypassed the
audit; serialized JSON string scalars were never re-parsed; container traversal was
recursive and crashed at 1,000 levels. Tests first (13 failed): eight encoded forms incl.
double percent, entity-in-percent and escaped-percent mixes; 2× and 3× serialized
scalars; 1,000 and 100,000 nesting levels; 12 encoding layers. Fix: `unescape` decodes one
layer (JS/JSON `\uXXXX \xXX \/ \\`, percent, HTML references) and `text_layers` repeats
to a fixed point (6 rounds); `decoded_forms` re-parses strings starting with `{`, `[` or
`"` (4 JSON layers); `json_strings` walks iteratively (256 levels). Any exhausted bound
or parser `RecursionError` (also in source maps) is a `decode-limit` finding: fail closed.
`pytest -q tests/test_release_audit.py`: 34 passed; ruff check clean. Real built site
(final-2 `.build/site`): exit 0, 5,817 files, 0 findings, 128 s.

## 2026-10-15/16: issue 106 lane C3 — echopy v2 stubs; Finder metadata race

Echopy 0d48b79 (generator v2, declared class members) changed 12 locked inputs
(11 shim files + tooling/shims.py); reviewed and refreshed by the runbook (final-3).
Final-3: build/check, 283 docs tests, release audit (5,823 files), a11y, 5/5 interaction,
prefix rehearsal all exit 0; build-2 and check-after exit 1: Finder wrote `.DS_Store`
into the temporary generation stage (`content/`, `content/reference/`) mid-build, so the
generated file-set check failed and stage removal hit "Directory not empty". Fix:
`content_files()` ignores `.DS_Store` like `file_manifest` already does;
`stage_directory()` repeats a failed stage removal once. Two tests failed first; 22
lifecycle tests pass.

## 2026-10-16: issue 106 lane C3 — final-5 (echopy v3 facades, GetGo examples page)

Lock refresh reviewed before commit: echopy 3db4bc9 (generator v3: facades read export
names lazily; 19 shim files + tooling/shims.py) and fontlab-python-examples f151195
(docs-export adds `getgo.md`, the 13 GetGo examples with their native receipt; `index.md`
link; `manifest.json`). Runbook final-5 (evidence parent
`verification/issue-106/evidence/C3/final-5/`): all 16 gates exit 0; 285 docs tests;
release audit 5,827 files, 0 findings; 5/5 interaction; determinism identical;
242,654/242,654 identities; 4,919 pages. README: release-audit decoding and fail-closed
bounds documented.

## 2026-10-16: issue 106 lane C3 — X4c audit findings fixed

X4c: echopy APPROVE (836bdfa..0d48b79); audit REQUEST CHANGES, two Important.
(a) numeric HTML references without `;` (`&#47Users`, `&#x2fUsers`) bypassed: ENTITY now
accepts an optional `;` for numeric references (html.unescape decodes them).
(b) the boundary parse beyond JSON_LAYERS ran outside the DecodeLimit handler, so a
100,000-level array serialized 4 times raised from audit(); it now records the limit.
Tests first: 3 semicolon cases and the combined-limit case at 4 serializations failed
(RecursionError -> DecodeLimit escaped); combined case parametrized over 3–7 times.
`pytest -q tests/test_release_audit.py`: 42 passed; ruff clean. Real site (final-5
`.build/site`): exit 0, 5,827 files, 0 findings, 128 s.

## 2026-10-16: issue 106 lane C3 — final-6 and the lunr 2.3.9 TokenSet defect

Final-6 (glyport cb611bd, echopy d5c0ba3, docs 9633e1d): 15/16 gates exit 0; docs-tests
1 failed / 292 passed: `test_search_when_full_index_uses_materialx_worker_then_module_alias_is_discoverable`
(stock MaterialX worker, full index: `fontgate`/`fontlab` -> 0 groups; console
"Cannot read properties of undefined (reading '_index')" in lunr Index.query).
Deterministic (3/3 reruns). No single document causes it (bisect: needs both halves).
Cause: upstream lunr 2.3.9 `TokenSet.prototype.toString` keys nodes as `label + id`
without a terminator; a digit label beside an id collides and minimisation merges
distinct nodes. Query-independent check: full-index `tokenSet.toArray()` != sorted
`invertedIndex` keys; all 68 complete-search shards equal. Confirmed by patching the
key to `label + ":" + id + ";"`: fontgate 250 groups (reference/fontgate.html first),
fontlab 4,256. The live sharded path already returned those counts.
Fix, test-first (both new node tests and 5 Python tests failed first):
- `compile.cjs` rewrites the one `toString` line of the byte-exact vendored lunr.js while
  bundling (async esbuild 0.25.12 plugin, exactly-one match) and records the patch in
  `bundles.json`; before the patch the bundles reproduced byte-for-byte; after it each of
  engine/router/query/complete-search changes by one line. `node --test`: 20 passed.
- `scripts/lunr_patch.py` rewrites the key in the stock MaterialX worker after each build
  (`on_post_build`), failing unless it matches exactly once (MaterialX upgrades fail loudly).

Final-7 (glyport 0baafb4, fly c8e7b44, typerig-lib fc802ef, examples 3106531): build exit 1,
R014 "1 unexplained coverage gaps: alias-unresolved: fly.fp". fly c8e7b44 added `fp` ->
`fontlab_fontport`; fontlab-fontport is a private repository and not a documented package.
Not documented without an owner decision (as D10 was for Remopy/Aidus): reconcile now
explains exactly `fly.fp -> fontlab_fontport` (`REVIEWED_UNDOCUMENTED_ALIASES`, reported
under `explained.undocumented_alias_target`); any other target or alias stays a gap.
Test first (the explained case failed); 17 reconcile tests pass.

Final-8 (with the fly.fp fix): build exit 1, "Initial complete-search payload exceeds 5242880
bytes": initial_static_bytes 5,254,609 (last success 5,215,829). Cause: fly c8e7b44's `gp`
alias adds 7,039 `fly.gp.*` aliases (552,376 vs 545,337) and +7,037 routing tokens. R041
says to restructure rather than drop members, so the global vocabulary is now front-coded
(`{"format":"front-coded-1","prefix":[...],"suffix":[...]}`, canonical maximal prefixes,
decoded and strictly-sorted-checked before READY). Measured on the final-8 index:
terms.json.gz 3,678,973 -> 1,501,986 bytes. `encodeTerms` lives beside `decodeRouting`
(validation.js, exported by router.cjs) and `build.cjs` uses it; bundles recompiled with
esbuild 0.25.12. Tests first (3 failed): round-trip, built asset format, 9 malformed
encodings rejected. `node --test`: 22 passed; Python search tests 6 passed.

## 2026-10-16: issue 106 lane C3 — D14 Fontport reference; lunr upstream reference

D14 (owner): document fontlab-fontport (docstrings/signatures, Apache-2.0). `PACKAGES` gains
`fontlab-fontport` (src/fontlab_fontport, canonical main c9fee00), nav "Ecosystem > Fontport",
licences row "Pythonqtside, Fly, Fontport: Apache 2.0". The reviewed `fly.fp` exception is
removed: no alias may target an undocumented package (test: fly.fp/fly.zz to missing targets
are gaps; 16 reconcile tests pass). Being a documented package also exempts the Fontport repo
name from the release audit's private-name check, as for the other documented packages.
Upstream lunr report found: https://github.com/olivernn/lunr.js/issues/503 (open; same
`TokenSet.toString` collision, also seen in Material for MkDocs). Cited in `bundles.json`
(patch record) and `scripts/search_backend/README.md`; bundles recompile byte-identically.
Final-9 (glyport 0baafb4 etc.): 13 gates green, stopped by the controller during build-2.

Final-10 (glyport 0baafb4, echopy 3b213dc, fly c8e7b44, typerig-lib fc802ef, examples 3106531,
fontport c9fee00; evidence `verification/issue-106/evidence/C3/final-10/`): runbook exit 0,
all 16 gates exit 0; 300 docs tests; release audit 6,002 files, 0 findings (covers the new
Fontport pages); 5/5 interaction; determinism identical; 242,654/242,654 identities,
0 unexplained; `fly.fp` -> fontlab_fontport (215 symbols, 358 fly.fp.* aliases). Lock diff
reviewed against the committed lock: fly (1 file, reviewed gp/fp aliases) and
fontlab_fontport (26 new files, canonical main c9fee00).

## 2026-10-16: owner tag v1.0.0; package content gate; package narrative docs

Owner tag: `v1.0.0` (e3afa28) was created by the owner's own `gitnextver` run at 02:03. Its
lock is the final-6 state: docs-tests 1 of 293 failing (the lunr 2.3.9 TokenSet collision,
upstream olivernn/lunr.js#503). The fix (3ad6570) and everything after it ship under the next
tag. The tag is never moved or deleted.

API page production (owner request), measured on the final-10 site:
- native `fontlab`, `fontgate`, `fontpr`, `PythonQt`: Echopy in-host captures (`.pyi`
  sidecars), reconciled 242,654/242,654; `fontlabpr` documented as absent (D8);
- runtime-built APIs (`GlyphsApp`, `vanilla`, `AppKit`, `Cocoa`, `Foundation`, `objc`,
  `aidus_code_tools`, `fontlabapp_shim`): Echopy shims generated from the real providers;
- ecosystem packages (echopy, fontlabapp, remopy, grablab, pythonqtside, fly, typerig,
  glyport, aidus-code, fontport): static source analysis (Griffe), never imported, so code
  that needs FontLab documents completely.
New gate `verify_site.package_content_problems`: every documented top-level package (23)
must render a page with member headings and docstrings; only `fontlabpr` (absent, D8) is
exempt. Tests first (4 failed); 8 site-verification tests pass; final-10 site: 0 problems.
Narrative docs: new Packages section (overview/install/quick start/examples/limits for all
ten packages, verified against the packages' source APIs); the stale Glyphs guide is
rewritten for `run_script`/`install_plugin`; the start page links the package pages.

Final-11 (evidence `verification/issue-106/evidence/C3/final-11/`; failed attempts kept as
`final-11-shimdrift/` (aidus 7da6a08 changed executor.py -> echopy 10427cd provenance refresh) and
`final-11-menuapi/` (fontlabapp 43cc126 moved the reviewed MENU_API lines -> 4f331a1)):
producers echopy 10427cd, fontlabapp 43cc126, remopy 824d690, grablab 2473ee1, pythonqtside
2777e85, fly a35a09d, typerig-lib f589189, glyport 0baafb4, aidus-code c8c1537, fontport
77aa6df, examples 37924b6. Runbook exit 0, all 16 gates exit 0; 304 docs tests; release audit
6,018 files, 0 findings; package-content gate 0 problems (23 packages); 11 package pages built;
242,654/242,654 identities. Lock delta (11 inputs): fly/__init__.py,
fontlab_aidus_code/install.py, fontlab_echopy/aidus_code_tools/_shim.json, fontlab_fontport
native_feature_split.py + native_features.py, fontlabapp _qtsafe.py + application/ui.py +
host.py + views.py, pythonqtside _app.py + _app_native.py.

Final-12 (evidence `verification/issue-106/evidence/C3/final-12/`; failed attempts kept:
`final-12-shimdrift/` (glyport 526f165 -> echopy a65a488) and `final-12-guidelinks/` (9 lifecycle
fixtures without site-src/packages -> be174ae)): producers echopy a65a488, fontlabapp 4557967,
glyport 526f165, aidus-code ed318c3, others as final-11. All 16 gates exit 0; 307 docs tests;
release audit 6,128 files 0 findings; 242,654/242,654 identities; 820 shim exports. Lock delta:
echopy shims (+ vanilla.test, vanilla.vanillaBase), glyport src (F25–F47), fontlabapp `fontui`
(21 new modules from issue 105, merged into canonical fontlabapp).
