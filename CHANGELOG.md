---
this_file: CHANGELOG.md
---


## 2026-11-11 — Interaction flake: fix landed, row kept open (Issue 250)

- Per-stage log of Complete documentation run 43103878240 (b4bdd851): job `build` logged `Documentation stage: interaction` at 21:51:28Z then `accepted-check` at 21:52:41Z; job `qualify-generated-output` logged `interaction` at 22:18:18Z then `accepted-check` at 22:19:33Z. No retry or "not attached" line in either job; no re-run.
- Run 43103878122 (same SHA) is "pages build and deployment" (jobs build, deploy, report-build-status); it has no `interaction` stage and is not counted.
- One clean run is thin for a flake that failed 1 in 6, so the TODO row stays open, reworded to await a second clean exact-SHA run.

## 2026-11-11 — Interaction check survives a search re-render (Issue 250)

- Cause of the intermittent `interaction` failure (run 43079462598 attempt 1): `open_result` in `scripts/interaction_check.py` held an element handle to a search result while MaterialX re-rendered the result list as shards arrived, so `ElementHandle.click` failed with "Element is not attached to the DOM" (case `alias`). Reproduced locally 1 of 6 times with CPU load (8 busy processes) and not otherwise.
- `open_result` now re-finds the result and retries up to `RERENDER_ATTEMPTS` (3) times, only for that detached-element error; every other error, and a persistently stale result, still fails. Tests in `tests/test_interaction_check.py` re-render the list between find and click (2 fail without the fix with the same error; 4 pass with it); file 37 passed; 8 of 8 loaded local runs of `scripts.interaction_check` pass. Exact-SHA CI proof is pending.
- Evidence for the closed gzip row (2fcf469f, Task 414), checked on 0b47214b by lander1: `scripts/` has no `gzip.compress` (gzip is used only to decompress); `search_shards.py:133` `initial_gzip_bytes` uses `portable_gzip_sizes`; swapping that line back to `gzip.compress` fails 1 test (12 others pass).

## 2026-11-11 — Browser-stage failure is not the runner image; its cause becomes visible (Issue 250)

- Reverted the `ubuntu-24.04` pin from 0ce2fcce: run 43053911785 on ubuntu-24.04 failed the `browser` stage after the same ten minutes as the ubuntu-26.04 runs 43040901865 and 43048681844, so the image was not the cause. The real pin commits are 0ce2fcce and the fflate notice fix 2d2f6ab7; 187567c1 does not exist in the repository.
- Local reproduction of `playwright install --with-deps chromium` (playwright 1.63.0 from uv.lock, macOS arm64) succeeds, so the locked version and the Playwright CDN are fine; the Linux apt part cannot be reproduced without a container.
- `scripts/pages-build.sh` refreshes the apt index (`sudo apt-get update`, CI only, bounded at 120 s, failure tolerated) and bounds the install with `timeout -k 10 300`. On failure the public log gets only fixed strings (stage, exit code, whether the timeout fired as exit 124); no apt, playwright or network output is echoed, and a sentinel test pins that. The cause remains open until the exit code is known. A second test pins the exit-124 message and both timeouts.
- Verified: exact-SHA run 43079462598 on 75d8bd84 passed the `browser` stage and, after re-running its failed job, every stage through `complete`. Caveat: attempt 1 failed at the `interaction` stage (exit 1), which is intermittent and tracked in TODO; green status therefore needed a re-run.

## 2026-11-11 — Complete documentation audit accepts the reviewed fflate notice (Issue 250)

- Cause of the red `Complete documentation` runs since f70f756: Task 414 (db79daa) linked `licenses/mit-fflate.txt` from `src_docs/md/licenses.md` but did not add it to `LICENCES` in `scripts/release_audit.py`. The unchanged auditor therefore reported a fourth finding, `licence: mit-fflate.txt linked-but-unreviewed`, beside the three reviewed private-name rows, and `scripts/pages_inputs.py disposition` correctly refused the non-reviewed result (stage audit-disposition, exit 1). The earlier reds on bd8b94c and cd5357c were a different failure: GitHub Pages builds for d87cd7e errored ("Page build failed"); later Pages builds succeed.
- `LICENCES` now pins `mit-fflate.txt` at sha256 `0a1df3a0…8b551`, byte-identical to the LICENSE in the npm tarball fflate 0.8.3 (the locked version). The disposition rule and the audit are unchanged.
- New test `test_every_licence_linked_from_the_source_page_has_a_reviewed_digest` fails before the fix and passes after; it keeps every notice linked from `licenses.md` pinned in `LICENCES`.
- Reproduced locally with the private input store at the workflow's pinned ref and Python 3.12 (`scripts/pages-build.sh` through every stage): before the fix audit-disposition exit 1 with exactly that extra licence finding; after it, capture exit 1 (the reviewed three rows) and disposition passes.

## 2026-11-10 — Task 414 size-budget metrics use the portable codec (Issue 250)

- `scripts/search_shards.py` gains `portable_gzip_sizes()`: one `node -e` call runs the bundled fflate codec (`search_backend/gzip.cjs`, level 9, mtime 0) over the actual files. `initial_gzip_bytes` now sums the manifest-recorded (verified) gzip sizes of the three shipped assets with a portable-codec estimate for the bootstrap index, worker and UI, which ship no `.gz`; the monolithic `search_gzip_bytes` in `scripts/verify_site.py` is that estimate alone. Budgets no longer vary by Python/zlib build. Committed `docs/search/complete` `.gz` files predate fflate, so only recorded sizes, not re-compression, describe them. Size-budget tests now use fixed, once-measured golden byte counts instead of values derived from the code under test; the README states that `verify_site.py` needs Node. A failing node codec now raises `RuntimeError` with its stderr.
- Tests: portable sizes equal freshly emitted `.gz` sizes; manifest-based oracle for `initial_gzip_bytes`; host `gzip.compress` forbidden.

## 2026-11-11 — Ruff clean on scripts and tests (Issue 250)

Fixed the 21 findings on main: import order (10), unused imports (2), `re.S`/`re.I` aliases (2), explicit `check=False` on four asserted `subprocess.run` calls, `values()` loop, one parenthesised string literal and the `base` with-target rename in `scripts/interaction_check.py` (`served`; the Playwright-only branch is covered by the browser lane, not unit tests). No behaviour change. Suite 606 passed, 1 skipped; `ruff check scripts tests` clean.

## 2026-11-10 — live font editing rule (Issue 250, D44)

- AGENTS.md: agents test and edit the font open in FontLab 9, starting from the Desktop VFJs, and may save them.

## 2026-11-10 — Task 414 portable search gzip

Review fixes (independent review, APPROVE_WITH_FIXES): a 1.2 MB byte golden
pins fflate output (2,967 bytes; native zlib gives 2,970), because the header
check alone cannot tell fflate from Linux zlib. compile.cjs now checks the
installed fflate's lock integrity against `source-provenance.json` and takes
the banner version from provenance. Recompiled bundles are byte-identical; Node
search tests 27/27. Expect a one-time change to all committed
`docs/search/complete/*.gz` bytes on the first CI publish after this lands.

Both search compression sites now use pinned fflate 0.8.3 (MIT), bundled by
esbuild 0.25.12 into Node-only gzip.cjs. Level 9, mtime 0 and upstream OS byte 3
produce header 1f8b0800000000000203. Ordinary builds use the committed-format
bundle without npm. Package lock, bundle hash, provenance and licence agree;
all four existing bundles and all original source records remain unchanged.

RED: 23 passed / 1 failed (actual header ended 0213, expected 0203).
GREEN: 26 passed, including public-fixture payload hashes, repeated identical
bytes and Node gunzip round-trips for empty, short, binary, Unicode and large
inputs. Native Node coverage: build.cjs 100% lines / 88% branches; gzip.cjs
87.25% / 84.25%; compile.cjs 100% / 58.33%. The TypeScript re-export is exercised
through its generated bundle, without separate source-mapped coverage. No Python
production module changed. Compiler error branches are not fully covered.

uv sync --locked --group dev passed. Full requested pytest: 532 passed,
1 skipped, 12 failed, 62 errors. Failures include Chromium launch permissions,
missing typerig/fontlabapp sibling sources and promotion-fixture Git-ignore
checks. Offline build --check failed importing Echopy; an explicit sibling
PYTHONPATH retry then failed because native API sidecars are absent. No source
lock refresh, generated docs changes, native access or publication occurred.
Generated docs changed: 0. No Git mutation was performed.

Detailed commands, gate tails and limits: .build/task414/REPORT.md; raw logs are
in the same ignored worktree directory. Full-site and actual Mac/CI parity
remain open; this source result does not resolve the historical 77-file diff.

## 2026-11-10 — Issue 250 documentation round

- AGENTS.md describes the delegation, integration and release workflow.
- WORK.md reset to the current round; the earlier bytes are archived on the owner's workspace data volume, not public.

## 2026-11-05 — independently approved documentation applied

[Task 2 final review](../verification/issue-230/task-2-fix2-review.md) records
SPEC PASS / QUALITY APPROVED. The [78-file application receipt](../verification/issue-230/task-2-apply.json)
includes this repository's six guides and preserves all 21 repository heads,
branches, indexes and non-selected diffs. This is applied documentation evidence,
not a new product test, installed artifact, native result or publication.

[Round 2 independent review](../verification/issue-230/round-2/repair-review.md),
[application](../verification/issue-230/round-2/apply.json) and
[controller verification](../verification/issue-230/round-2/controller-verification.json)
include this repository's `TODO.md`, `WORK.md`. The complete round
has 26 successors across the workspace; its acceptance is source/documentation-
receipt scope, not runtime/native acceptance.

The complete earlier handoff/history below retains its proposal-stage statements
and dated source pins. Later review, application and delivery status belong in the
[live workspace ledger](../verification/issue-230/progress.md). Original future,
native, artifact and preservation contracts remain binding.

## 2026-11-05 — documentation reconciliation proposal

Prepared repository-specific organization, test and MVP/delivery guidance from current source/test configuration and retained Issue 207–211 evidence. Distinguished current canonical layout from qualified candidates, future plugin ownership and unfinished native/artifact gates. Preserved all prior work and changelog evidence; no runtime completion, installation or publication is claimed. Completed historical task rows were removed from the active checklist and consolidated below from existing local CHANGELOG/WORK receipts. Unfinished native, artifact and integration checks remain open.

## Retained scoped completion receipts — corrected evidence map

These are dated results at the stated source/version and acceptance surface. They do not establish current integrated, installed, native or published acceptance. Full receipts and hashes are indexed in the workspace Issue 230 task-2 manifest. Canonical-preimage line ranges below refer to the unchanged historical documents, before these new entries.

- Manager-state GP5e04d1168:25new+117retained=142 source examples;124oldtags/180oldblocks exact;206compile/55links/7469payloads.
  Historical receipt: CHANGELOG.md:131–170.

- Dynamic/sidebar GP788959172:18new+99retained source examples;106tags/160oldblocks exact;180compiled.
  Historical receipt: CHANGELOG.md:172–188.

- Dynamic/sidebar same source:106tags/160blocks unchanged;180compile;7469protected;nav/lock/archive preserved.
  Historical receipt: WORK.md:157–195.

- Echopy-values stage:nine new+90retained source examples;97tags incl7held;160blocks compile.
  Historical receipt: CHANGELOG.md:190–205.

- Echopy-values same stage:150oldblocks/97tags/7470protected payloads remain exact;nav/lock/archive unchanged.
  Historical receipt: CHANGELOG.md:190–205.

- Generation GP5a54b4b:82retained+8new pass;89oldtags incl7held unchanged;150blocks/44links/7469protected.
  Historical receipt: WORK.md:2258–2283; CHANGELOG.md:1218–1234.

- Connected manager:75prior+7new=82 source examples;82 prior tag bodies unchanged.
  Historical receipt: CHANGELOG.md:207–218.

- Connected manager:142compiled/43links/7467protected payloads;index/nav/lock/archive unchanged.
  Historical receipt: CHANGELOG.md:207–218.

- Connected-manager final source run369passes/1inheritedD29skip,exit0;first13-pass scratch-path interruption retained.
  Historical receipt: WORK.md:216–242.

- Parent-aware H:75current examples pass;17 documented migrations;63oldG controls pass;12new meaningful negative controls;7held bodies unchanged.
  Historical receipt: CHANGELOG.md:220–239.

- Parent-aware final source run369/1skip;233payloads/7228sparsepaths/lock/archive state preserved.
  Historical receipt: WORK.md:244–288.

- Represented-production guide:11new+24prior source examples and older-install negative matrix;369/1skip;source-lock/sparse/archive preserved.
  Historical receipt: CHANGELOG.md:326–345.

- Combined-index exact six-wheel/701runtime tuple;24installed examples;earlier consumer/provenance bytes preserved.
  Historical receipt: CHANGELOG.md:347–361.

- Local docs setup2026-10-18:src_docs migration;strict5368page/6293file build+check;allroute/archive/budget gates;20queries;309tests;28/28interactions;0privacy findings.
  Historical receipt: WORK.md:1832–1868.

- Receiver-name fixture:Echopy0.2.4.dev6 dirty wheel/sdist each8offline snippets pass;old artifact fails metadata;10blocks compile;2native held.
  Historical receipt: CHANGELOG.md:683–697.

- Script metadata fixture:each fresh wheel/sdist8examples pass;16blocks compile;older lookup-only artifact fails GSGlyphInfo.script.
  Historical receipt: CHANGELOG.md:622–635.

- Case metadata fixture:each installed private artifact8examples pass;old script-only artifact fails case;native blocks compile only.
  Historical receipt: CHANGELOG.md:605–620.

## 2026-11-05 — planning chronology reconciliation

Authored source-guide, example/static and local2026-10-18 layout receipts are past work. Keep each exact stage denominator and held native bodies distinct. Future current source/ordinary/native/rendered/site acceptance remains open; Node tests/compiler are separate lanes. Old exact source stages and historical source-lock commands are not instructions to reset current inputs. Historical passing results retain their dated source and acceptance scope in the entries above and original history below. This documentation change creates no new runtime acceptance.

---
this_file: CHANGELOG.md
---

## 2026-11-04 — Source lock and generated reference refreshed for the 1.2.x cohort (Issue 204 Task 6, interim)

- `api-sources.lock.json` now pins 1103 inputs, up from 765. Against the previous lock: 228 removed, 566 added, 163 changed.
  - All 1060 package inputs equal the committed HEAD bytes of their repositories.
  - Every removed or changed input's previous hash appears in that file's committed history.
  - The 43 examples pages equal the committed retained export.
  - The cohort: App v1.2.4, Glyport v1.2.1, Remopy, Fly and Fontport v1.2.0, the current Echopy, pythonqtside, TypeRig and Grablab heads, and the committed Aidus HEAD.
- The inventory reads imports in both branches of a top-level conditional, so platform-selected re-exports such as Remopy `platforms.launch` resolve.
- The inventory skips dataclass `InitVar` pseudo-fields, which are `__init__` arguments, not attributes; griffe also drops them.
- The generated reference and staged `docs/` are rebuilt for the moved App domain modules; the old module pages are removed.
  - The App, Glyport and Grablab licence texts left over from before 70becfbb are dropped.
  - Strict build, `--check`, 380 tests and the release audit (7992 files, no findings) pass.
- This lock is interim. Issue 204 items 1 (main promotion), 3 (Aidus retirement) and 12 (FL provenance) will change inputs and need a refresh. Not published: `docs/` on main is the Pages source.

<!-- workspace-handoff:2026-11-03 -->
## 2026-11-03 — Issue 205 canonical module paths

- Migrate authored App examples and source-reference helpers to canonical
  domain paths; update Remopy identities and interaction-check URL routes.
- Correct the App/Fontport editor ownership guidance and add path migration
  regression tests using the reviewed tool. Generated site and source locks
  remain unchanged.

## 2026-11-03 — installer options, licence and cleanup

- Licences page: Fontlabapp, Glyport and Grablab are Apache-2.0; Fontlabapp's notice is
  refreshed (third-party MIT/BSD terms retained); retired the BSD/MIT texts for them.
  The generated `docs/` site needs a rebuild to show this.
- Removed `plans/` and three tracked `.DS_Store` files.

## 2026-11-03 — documentation handoff for November 2–3

Accepted feature d9c15dc adds the owned-window recovery guide after extensive generation/resource/manager/discovery/node/layer guides.

Authored source/ordinary examples were checked; generated references, source-lock, rendered site and publication remain gated.

Observed canonical checkout: `main` at `5ec628a388fa`. No source integration is performed by this update.

Updated the requested AGENTS/TODO/PLAN/CHANGELOG/README documentation and
recorded the paused state. Existing project text, examples and history remain;
no runtime source, installation, native session, branch/ref, release or site was
changed by this documentation maintenance. Source/archive/ordinary/native and
promotion acceptance remain separate claims. Detailed workspace evidence is
recorded in the root CHANGELOG and retained verification reports.
<!-- /workspace-handoff -->
## Owned-window recovery authored guide — 2026-11-03

Add practical FontLab usage and six executable standalone experiments covering
floating priority, refusal, staged cleanup, factory failure ownership and parent
destruction. Retain all inherited examples and generated/native/publication holds.
All6pass in final source and both genuine App.dev334 prefixes; normal369/1existing
skip. Preserve7482inherited modes,7476protected bodies,229old Python fences/173old
tags;8newblocks compile and new links resolve. No generated/reference publication.

## Foreground-layer identity guide verified — 2026-11-03

New glyport-layer-identities.md has eight independent exact-setup experiments
executing actual FontLabBackend/Model/proxy code over owned primitive objects.
Same-name identity/order, ID-only lookup, read-only repeats, interpolation roles,
masks/services, pending master no-creation, first-exposure history replacement
and auxiliary-to-master retirement all pass in exact source and both fresh
ordinary prefixes with genuine GP1.0.8.dev196+g40ac49ab4 and unchanged App.dev333.
No projection/cache/history algorithm is replaced by a fixture.

Complete ordinary suites pass7206GP/600Echo/4496Scriptmix(+1oldskip) in each prefix;
46installed dependencies are compatible,990provider/RECORD hashes unchanged per
suite and all loaded provider files remain inside their own prefix. The unchanged
source-only GPpath assertion passes in exact source, separately from installed
behavior. App/Examples/TypeRig/all-earlier-guide scopes retain their own Y/Vproof;
these were not relabeled as whole Zconsumer qualification.

Docs normal gate369pass/1existing D29built-inventory skip, exit0; zero changed
production modules/no coverage claim. Exact rtk proxy quality.sh argv/environment/
log/receipt is external foreground-layer-identity-20261102/docs-normal-quality.
The direct protection audit checks7481inherited modes,7475protected bodies,
all220old Python fences/164setup-example tags unchanged, nine new blocks compile,
new links resolve, README199lines. Actual13-target shim comparison has39identical
files; accepted XEcho and every native/manual/generated/source-lock/site/archive
payload remain unchanged. Normal/ordinary/source receipts retain exact versions,
origins and snippet hashes. Fullsource7203/3archive skips plus one further exact
GPguide case pass; normal7128/79old skips/all58modules>80%; all9archive tests pass
and wholewheel reproduces after materializing every508sdist member.

Native four-font imported roles/order/full preservation/cache/date/lifetime/
history/Undo/Redo/save-reopen, TypeRig window priority, actual binding/resource/
version, full Transform and all migration/retirement goals remain open. D29native
capture/generated/source-lock/strict rendering/browser/accessibility/archive/
licence/publication and D30live safety holds remain separate. Pending declared
slots do not make glyph.layers a literal stored-only Transform iterator.

## Original node-action guide verified — 2026-11-02

New161line original-node-actions.md explains three distinct Scriptmix actions,
genuine App.dev333 and the guarded entry point. Four independent experiments
execute actual App planning with fresh visible setup. Exact source and both
ordinary installations pass all4 without native/Qt/font/document access.
Both ordinary tuples also pass7485App/4496Scriptmix(+1oldskip)/600Echo checks.

Normal Docs gate369pass/1existing D29built-inventory skip; zero changed production
modules, no coverage claim. Command: rtk proxy /bin/sh .metaswarm/quality.sh
coverage <this-checkout> fontlab-python-docs, exit0. Exact argv/environment/logs
are in external original-workflows-20261102/docs-normal-quality.

The direct protection review verifies7474protected file bodies and7480inherited
modes against X, all215old Python fences/159setup-example tags exact. Five new
blocks compile and new local links resolve. README is198lines after whitespace-
only reflow. Source/installed origins, snippet hashes and review input pins are
retained. Native selection/copy/four-font/history/window/lifetime, D29generated/
source-lock/site/browser/publication and complete original scope remain open.

## Namespace discovery authored companion — 2026-11-02

Added linked echopy-discovery.md with five independent actual-tooling experiments:
dictionary names omitted by custom dir, loaded PythonQt children and root-object
precedence, failed import dependency, deadline propagation, and complete owned
capture/generate/merge declarations. Examples use only owned modules/objects,
scoped registry/import hooks and disposable temporary declaration trees.
No native API calls or real capture/generated/site/source-lock refresh. All5new
examples pass exact source and both ordinary installed prefixes. Each ordinary
Echopy suite passes600tests, no skips; Docs normal369pass/1existing D29built-
inventory skip, zero changed production/no coverage claim. All7472protected
tracked payloads and210inherited Python fences/154setup-example tags stay exact.
The new guide has175lines. Prior full consumer/142guide qualification remains
separately pinned to V; it is not rerun or relabeled as a new full consumer tuple.


## Manager state authored source companion — 2026-11-02

New linked guide glyport-manager-state.md explains raw identity/nil setters,
exact script/sidebar-category rank sources and retained caches, initDebug queue/
group creation and actual parser adoption/failures, shared load/drain/observer
order and retained URL/flag state, explicit dealloc/superclass dispatch, class
placeholder-font cache/duplicates/partial failure/invalidation/current provider,
exact observed key and error/recovery conditions/repeated reads/nil failures.

25independent experiments execute the actual source algorithms against frozen
Glyport5e04d1168b4e33823bed4940fce308637f8abadd. Three visible setups run afresh per
body. Relevant global singleton/font-cache/once/provider identities are visibly
scoped/restored and independently checked by the runner. Shared initialization
uses the earlier complete invented-resource lifecycle, actual parser/sidebar/
38281-row generation/indexes/queues, without replacing algorithm entry points.
The primitive font tokens record operations and do not load real native fonts.

Before editing, independently pinned 7,478 payloads/modes, 124 tags and 180 Python
blocks. All 117 inherited active examples and 25 new examples pass exact U source
(142 total); all old tags/blocks remain exact. The static audit compiles all 206
blocks, verifies 55 local links and 7,469 protected payloads/modes, preserves the
source lock/navigation/generated/archive state, and retains ten inherited D29
reference links as held. Nine negative CLI cases reject source overrides before
installed-mode imports/writes. New examples independently restore shared/font-
cache/once/provider identities; all 219 producer/primary/report input pins match.

Exact rtk proxy argv, exits, origins, setup/body hashes and receipts are in
external manager-state-companions-20261102/docs-evidence: baseline-command.json,
all-source-command.json and summary, static-second-command.json and cli-command.json.
The initial static attempt lacked full baseline preimages; all 7,478 were filled
from exact frozen T bytes after matching their before hashes. Its failed receipt
is retained. Scoped runner Ruff/format checks pass with AST-identical formatting.
Root owns complete normal Docs checks, ordinary prefixes/full consumers and
commits/pushes. No unchanged full Docs suite is rerun by this lane.

Wait, but: these are authored/source experiments. Actual private/default
resources, native Foundation/CF/CG/CT/NSNumber/NSObject/once/destruction/races,
FontLab original font workflows, D16/D29/D30/D31 and canonical/generated/source-
lock/site/archive/browser/publication qualification remain independent. No native
module/framework/MCP/app operation, install, capture, build, commit or push.

## Dynamic sidebar and document source guide — 2026-11-02

Added a linked practical guide with 18 independent executable experiments for
actual dynamic trees, defaults/visibility/predicate paths, row identity and
copy/reparenting, ordering/icons/once caches, current resource reads/reload
failure, delayed weak-font counts, list expansion/collisions, count publication/
Smallcaps and document parent-URL loading. Explicit invented primitives keep
algorithms in the package and preserve missing FontLab/native dependencies.

All 18 new plus 99 inherited active examples pass source with actual origins
checked. All 106 prior tagged bodies (including seven held native/UI cases) and
160 prior Python blocks are unchanged. Static compilation covers 180 blocks;
7,469 protected payloads/modes and navigation/source-lock/generated/archive
state remain exact. Reusable installed runner rejects source overrides and runs
all 117 active examples independently. WORK.md and external evidence retain
commands, failed first attempts, pins and the separate ordinary/native/root gates.
No dependency, generated-reference, native capture or publication change.

## Echopy module values and documentation — 2026-11-02

Added the authored module-values guide and index/package links. Nine executable
owned examples cover live object identity, sanitized aliases, accepted prefix
names, write/delete/dir behavior, absent offline annotations, captured descriptor
docs without getter execution, all three value collections, source-identifier
keyed overlays/precedence, actual Griffe consumption and lazy native facades.
The guide preserves retained capture/Any/variadic/Qt enrichment limits and keeps
source, ordinary-installed, native and publication evidence separate.

All nine new and 90 inherited active examples pass source with asserted origins;
all 97 inherited tags (including seven held native/UI bodies) and all 150 prior
Python blocks retain exact bytes. Static audit compiles 160 blocks, checks
23 local links and preserves 7,470 protected payloads/modes, navigation, source
lock and held generated/archive trees. WORK.md and external docs-evidence record
commands, byte pins, runners and the remaining root gates. No dependencies changed.

## Connected local-manager source companion — 2026-11-02

Expanded the manager/profile guide with connected constructor/reload/base-parser/
sidebar/resource/queue/error/summary semantics and seven executable invented-provider
examples. Linked authored index and package/Glyphs entrypoints. All 75 prior active
and 7 held native/UI bodies retain exact bytes; 82 active examples pass source.
Static audit: 142 compiled Python blocks, 43 local links, 7,467 protected payloads/modes,
unchanged navigation/index/generated/archive/source-lock state. WORK.md records
full-suite results, retained failed harness attempts and exact evidence.
Fresh full authored docs source suite: 369 passed, one inherited D29 skip, exit 0.
Source-only acceptance does not close ordinary/native/resource/original workflow
or D29/D30 generated/publication gates. No dependencies/runtime modules changed.

## Parent-aware manager/profile authored companion — 2026-11-02

Added a linked practical guide for selected managers, six stored overlays,
groupIdx/direction, raw/copy/frozen distinctions, exact complete Glyphs2/3/4
wrappers through both providers, and bounded custom parsing/finalization/discovery.
Corrected stale missing-manager/localData/NFD and independent-view prose.

All 75 current selected examples pass actual H source exports. Seventeen earlier
examples receive visible source-qualified fixtures or corrected source oracles;
exact originals remain externally pinned, and all 63 original G controls pass.
The 12 new examples all fail meaningfully against G. All other 53 original tag
bodies, including seven held native/UI controls, remain unchanged.

Static audit compiles 134 Python blocks, resolves 76 local links and verifies
233 unrelated payloads, 7,228 sparse paths and unchanged lock/generated/archive
state. Fresh full docs source suite: 369 passed, one inherited D29 skip, exit 0.
WORK.md records the restored historical AST context, failed attempts and evidence.
No dependencies/runtime modules or existing tests/skips/thresholds changed.
Ordinary tuple/consumers, complete local/resources/original/native workflows,
generated/reference/site/browser and publication remain separate gates.

## Stored-description guide and source verification — 2026-11-02

Added seven owned actual-export examples for exact nullable descriptions,
name/alias/Unicode routes, selected compound seeds, copies, model snapshots and
unknown-source refusal. Navigation, package pages and the compound guide link
this guidance with explicit source/artifact/parent-aware/native boundaries.

All 63 selected Glyport examples pass: 56 prior + seven new. Against the unchanged
prior compound source, all 56 earlier controls pass and all seven new examples
fail meaningfully. All 63 pre-existing tagged examples remain byte-identical,
including seven held native/UI controls. Audit: 89 Python blocks compile, 26 local
links resolve, 238 unrelated payloads and 7,228 absent sparse paths are preserved,
as are the source lock and held archive/reference trees. Nine inherited generated
reference links remain explicitly held under D29. Navigation/privacy checks pass.

Fresh full docs source: 369 passed / one existing D29 inventory skip, 123.57 s.
An earlier attempt retains 368 passes / one fixture ENOSPC failure / that skip;
the complete unchanged suite passes after verified recovery of closed own scratch.
No test or budget assertion was weakened. No dependencies/runtime code changed.
Matching provider artifacts, ordinary consumers, native/original workflows,
generated references/site, accessibility and publication remain separate gates.


## Compound Glyph Info guide and source verification — 2026-11-02

Added a practical compound guide with nine owned examples through the actual
session exports. It covers core fields, shared fills, shallow duplicate lists,
raw/helper production, suffix nesting, exact-name precedence, Arabic alternate
records, read-only metadata and the long-production rebuild. Navigation and
Glyport/Echopy/production/Unicode pages describe its measured scope and limits.

All 56 selected Glyport examples pass against current source. The older ordinary
producer passes the 47 existing examples and one exact-lookup control, while the
other eight new examples fail meaningfully. All 54 existing tagged examples are
byte-identical, including seven held native/UI examples. The audit compiles 81
Python blocks, checks 31 local links and preserves 236 unrelated payloads, 7,228
sparse paths, the source lock and held trees. Nine existing generated-reference
links remain held under D29; no new unresolved link was introduced.

Fresh docs source tests: 369 passed / one existing full-built-inventory skip,
123.10 s. No runtime code, dependency, generated reference/site or native result
changed. Fresh matching committed artifacts and ordinary consumers, rendering,
accessibility and publication remain separate acceptance gates.


## Reviewed production checkpoint source gate — 2026-11-02

Corrected the stale ordinary-qualification sentence while retaining native,
factory/custom/local/version and publication boundaries. All47tagged examples
remain unchanged. The unchanged quality gate passes369tests/1existing D29skip;
no changed executable module and no module-coverage claim. WORK.md records exact
commands and independent3.12environment provenance. Corrected ordinary/committed
artifact qualification, generated/site/browser and native workflows remain open.

## Production ordinary artifact/cohort acceptance — 2026-11-01

Both fresh normal arm64Python3.11.14 prefixes install the six exact provider
wheels plus40unchanged pins without source overrides. Per prefix:5,697full
Glyport tests/0skips,370full Echopy/0skips,479focused checks,46isolation checks,
15package and35central metadata examples. All12other tagged Glyphs/package
examples also pass in each prefix:47tagged examples across six pages, using owned
input files for inspect/compile only. Exact extra commands: ../additional-example-commands.json.
All702runtime files match the exact
source/wheel/installed tuple before and after consumers. Exact consumer result:
Scriptmix4,481pass/1existing selection-read skip; Examples1,933+503=2,436/0skip.
All69rescued originals and7historical generated-doc fixture hashes are retained.
Glyport wheel SHA d92d425e58933ad100fbf439ec13398da54ef3409ed316ab4892a16cea7c5331;
Echopy wheel SHA a9abee1955b9639b5740319595995ed0605727b53d80501d50440ff5757a2172.
Standard source and complete-sdist builds reproduce identical wheels; all123+95
Glyport/Echopy runtime files match current source and all412+145source members
verify. Echopy's13catalogues are current and124protected files unchanged. Parent
artifact hashes remain historical. Source lock and7228sparse paths remain intact.

Exact root commands/exits0: ../artifact-check-commands.json (both final prefixes),
../wheel-authored-command.json,../sdist-authored-command.json and ../consumer-commands.json
(final applicable suites); artifacts/inputs in ../inputs.json and
../wheel-reproduction.json. A missing basetemp parent and an empty wrong-alias
consumer glob caused task-runner failures before correction; their complete
first-attempt logs/XML/commands remain, with no product test or dependency edits.
Fresh full docs source369pass/1D29skip is unchanged; subsequent status-only edits
receive the complete static/example-byte/link/sparse/privacy audit, not another
unchanged full run. Native/publication and1,580factory/glyph/application/full
original workflow scope remain open. No new source commit/push or main/canonical
promotion, live install, native call, source-lock/site rebuild, tag or publication.

## Authored represented production metadata guide — 2026-11-01

- Added a linked central guide with 11 owned examples plus an offline session
  fixture using actual ExecutionContext/FontLabSession GlyphsApp exports and
  Echopy declaration identity checks. Separate stored getter/shared fill/copy,
  helper normalization, Unicode/alias/suffix/model routes and explicit refusal.
- Corrected the present-tense claim that all production metadata is unqualified;
  represented-record source behavior is now distinct from glyph/application
  production and all 1,580 unqualified factory routes. Preserve historical results.
- Source examples pass 11 new plus all 24 old; older ordinary-install negative
  matrix retains all 11 failures and 24 passing old examples. Static verifies
  53 compiled blocks, 34 links, 51 nav targets, old anchors, privacy, all inherited
  244-file hashes, sparse 7,228 skipped paths and unchanged source lock.
- Fresh full docs source suite: 369 passed, 1 existing D29 inventory/search skip
  in 123.93 s; pytest and recorder exit 0. Borrowed context remains explicit.
- Fresh successor ordinary wheel/sdist, producer provenance and exact consumer
  checks remain root-owned and pending. Native/generated/publication and all
  D16/D29/D30/D31 holds remain open; no source/example semantic rewrites.

## Corrected Unicode-index cohort authored status — 2026-11-01

- Replaced stale corrected-artifact/provenance/consumer pending claims across
  the five authored Glyport/Glyphs/Unicode/metadata/parameter pages with inspected
  exact six-wheel results and current archive hashes; earlier hashes stay historical.
- Fresh ordinary installed execution passes 24 owned examples; all 701 runtime/data
  files match byte for byte before and after, with 40 pins and installed origins checked. Preserve all 24 example
  bytes,41 blocks,50 nav targets,57 heading anchors and25links; audit 244 inherited
  source files and retain complete 9 file preimages plus the bounded diff.
- Retain 369 passed/1D29skip as historical full-suite evidence; fresh acceptance
  is the scoped authored/static/installed check. Source lock unchanged. No new
  native9801capture, generated build, promotion or publication; D16/D29/D30/D31
  and all full original native-workflow gates remain open.

## Private authored shared Unicode-index correction — 2026-11-01

- Corrected primary-only lookup claims across current authored guides/package
  pages. Document primary-then-legacy insertion in record order, last-write
  precedence, FE8D/FE80 records, duplicate0000 winnerNULL and separate fields.
  Pinned public data adds730legacy keys to71401primary keys:72131combined keys.
- Corrected one global-index example with its complete preimage retained;
  preserved23/24examples,40/41blocks, all50navigation targets and the former
  heading anchor. A rejected model-snapshot change is preserved as failed evidence;
  its parentless Arabic nil-return example was restored byte-for-byte.
- Verified24source examples with seven explicit Glyport source origins and seven
  public dependency hashes,41compiled blocks,25local links and unchanged source
  lock. The unchanged old six-wheel tuple/701payload files rejects only the newly
  corrected snippet. Fresh corrected artifacts/cohort/provenance remain pending.
- Docs suite369passed/1existing D29skip, exit0. RetainedENOSPC receipt-write failures,
  recovered the recorder entry explicitly and did not repeat the unchanged suite.
  No generated/native/build/browser/promotion/publication gate is closed.

## Private authored global Unicode guidance — 2026-11-01

- Added a dedicated linked global Unicode guide and eight owned examples for
  exact wrapper dispatch, primary lookup, raw synthesis, UTF16/error boundaries
  and historical parsing/classification. Corrected stale absent-API and font prose.
- Retained all16earlier examples and all49existing nav routes. Verified24examples
  in the NEW six-wheel tuple,701payload bytes and seven installed module origins;
  compiled41blocks and checked24local links plus authored privacy.
- Full source suite:369passed/1existing D29 generated-inventory skip, exit0.
  Source-lock bytes unchanged. No generated/native/publication gate is cleared;
  D16/D29/D30/D31 and proprietary data/full-workflow limits remain unchanged.

## Private authored legacy Unicode and ROS guidance — 2026-11-01

- Added a dedicated legacy/ROS guide with8owned examples: separate primary and
  legacy metadata, canonical aliases, global font isolation, exact independent
  snapshots, model/suffix/nil behavior and ROS refusal/no-op/value boundaries.
- Corrected stale facade/ROS prose and cross-linked guide/package/navigation.
  Retained all8prior parameter examples unchanged and48existing routes.
- Verified16examples in the new six-wheel tuple with701payload-byte checks;
  compiled33Python blocks and checked15local links plus authored privacy.
  Full authored-source suite:369passed/1D29 generated-index skip (exit0).
  Source-lock bytes remain unchanged. Source/generated/native/publication
  acceptance levels and open D16/D29/D30/D31 holds remain distinct.

## Ordered parameters and Arabic authored guide verified — 2026-11-01

Added a dedicated central guide with8self-contained owned examples for duplicate
selection, live object/positional edits, master/userData isolation, legacy storage,
Arabic refresh, stored script, metadata-only reset and typed macOS values. The
new guide explains the exact spaced key, direct/nil/empty legacy precedence,
float32/sentinel behaviour and all current nonmacOS/ROS/native/facade limits.
Navigation and the existing Glyport guide/package page link to it; historical
artifact hashes and examples remain unchanged.

Fresh installed cohort execution passes8examples with installed-origin/hash
checks;25Python blocks compile and8local links plus navigation resolve. The
existing docs baseline is368passed/1skipped plus1missing-TypeRig-sibling failure.
The exact failed real-provider test passes with FONTLAB_API_SOURCE_ROOT pointed
at the fresh installed cohort; no declarations or locks were substituted. The
remaining skip requires a full built source inventory and MaterialX search index.
No generated build, source-lock refresh, native call, rendered-page acceptance,
canonical edit, commit, push or publication occurred.

Exact argv/cwd/nonsecret environment and outputs are retained in the controller
evidence under cohort-presentation-20261101/docs-evidence/commands.json,
authored-check.json and docs-receipt.json. Commands use rtk proxy, including:
`rtk proxy env -u PYTHONPATH -u SCRIPTMIX_APP_SOURCE -u SCRIPTMIX_FONTPORT_SOURCE
-u EXAMPLES_APP_SOURCE PYTHONDONTWRITEBYTECODE=1 "$COHORT_PYTHON" -I -B
"$DOCS_EVIDENCE/check_authored.py"` (exit0). Existing docs tests use the already
provisioned docs interpreter, not a new build environment.

## Additional-Unicode guide verified — 2026-11-01

Added an owned I/dotless-I/encoding-owner example and explained rename versus
refresh, legacy-only Arabic data, the Unicode17/macOS27.2 casing boundary and
remaining native/custom-manager limits. Both fresh installs pass12examples;
20Python blocks compile. Exact commands exit0 in glyph-additional-unicode-artifacts-20261101/
scalar-guide-commands.json; receipt verification/issue-123/docs-additional-unicode-20261101.json.
No generated build, source-lock refresh, browser run or publication.

## Shared metadata resolver guide verified — 2026-11-01

Updated classification limits and added one owned Unicode-precedence/reset example.
Both fresh Glyport installs pass eleven examples; nineteen Python blocks compile.
Historical artifact hashes remain historical. Exact isolated commands exit0 in
`docs-glyph-metadata-20261101/commands.json`; root receipt is
verification/issue-123/docs-glyph-metadata-20261101.json. Generated output, source
locks, browser verification and publication remain held under D29.

## Glyph classification and shared resolver gaps reproduced — 2026-11-01

Original callers require both category/subcategory setters and independent storage
flags on drafts and attached glyphs. Installed owned probes reproduce missing
members and read-time Unicode recategorization. AST inventory records61actual
assignments across2,329files, with100parse/encoding failures retained explicitly;
UI/mocks are not counted as native behavior. Root baseline153checks pass, proving
that the old suite did not cover these missing contracts.

Following reset setters into glyphInfoForGlyph found a broader problem in the
existing case/script implementation: Unicode resolution precedes name lookup.
Root independently reproduced4conflicting-name/Unicode resets; the agent retained
matching-name/unencoded controls and independent stored-overlay controls. Static
expectations are not native observations. The keep-name early return uses Icon
and SF-Symbol; synthesis, font-local suffix/base and stored overlays matter too.
The addendum corrects the earlier unknown-name/0031 example: the full resolver
would find Unicode metadata, so this is not a genuine missing-record case.

Evidence, source/caller/binary hashes, commands and installed origins:
verification/issue-123/glyph-classification-contract-20261101.json. Root baseline
and installed repro commands exited0. No originals or retained native binary were
executed. All recorded input hashes verify; no candidate runtime bytes changed.

Authored guide and candidate compatibility notes now disclose the counterexamples
without changing historical artifact hashes. Both existing installs still pass
10offline examples;18Python blocks compile. Receipt:
verification/issue-123/docs-classification-limits-20261101.json. These examples
do not cover the new counterexamples. No generated rebuild or publication.

Next repair shared resolution and all four metadata lifecycles together; adding
two name-only setters would reproduce the defect. Native history/reopen, custom
managers and D16/D27/D29/D30/D31 remain open. The broad goal is not complete.

## Glyph script lifecycle source, artifacts and guide verified — 2026-11-01

Named metadata supplies script defaults, including unencoded names. Explicit
None/empty/string values, temporary assignments, storage transitions, rename,
refresh, copy and unique attachment share existing case/lib state and recovery.
The round17 fixture now uses the Gurmukhi glyph name; upstream setUnicodes does
not replace script metadata. Previous failed expectations remain in the logs.

Source suite:4,053passes/3archive skips; regression-first suite35fails/10passes.
Root independently passed141focused checks before the final parameter expansion.
Fresh wheel/sdist each pass304checks with0skips, including all70script cases and
all3distribution checks. All116runtime files match source/archives/both installs;
28distribution versions match. Prior wheel fails56new cases and passes14controls.
Both installs run10authored offline examples;18Python blocks compile. The prior
wheel fails the new example. Earlier artifact hashes in the guide stay intact.

Exact commands, environment, exits, preimages, source/archive hashes and JUnit:
verification/issue-123/glyph-script-lifecycle-20261101.json,
verification/issue-123/glyph-script-artifacts-20261101.json and
verification/issue-123/docs-glyph-script-lifecycle-20261101.json.
Commands: rtk proxy /opt/homebrew/bin/python3.11 followed by the external
artifacts-run.py, artifact-installs.py and audit.py each exited0. Installed
example check.py exited0 twice; old-artifact pytest and example controls exited1.
Read-only candidate/docs git diff --check exited0. Scoped lint passes;2inherited
E731 remain. The red run's outer tail masked its status; retained JUnit proves
35failures. No dependency changes, native calls, canonical edits or promotion.

New consumer qualification is next. D16/D27/D29/D30/D31 and native history,
save/reopen, backend atomicity, detached reset/custom managers remain open.

## Echopy decorator artifacts and guide verified — 2026-11-01

Fresh wheel/sdist installs each pass245selected tooling checks, zero skips.
Same-process tooling origins are installed; all95runtime files match source,
archives and both installs.142sdist files pass inclusion/privacy/licence and
copied-test checks.117protected generated/provenance files remain unchanged.
The prior same-version wheel fails18new checks and passes5controls.

The authored pipeline example now accepts qualified decorators and checks real
raw/merged descriptor identity with captured staticmethod/classmethod members.
Both installs pass10offline examples; all12blocks compile. The earlier wheel
raises NativeUnavailable in the new fixture. Earlier bare-syntax guide failure
is retained; it prompted the behavior-based example update. Only that fixture's
archive hashes changed; other examples retain their own historical hashes.

Exact commands, exit codes, origins, bytes and negative controls are retained in
verification/issue-123/echopy-decorator-artifacts-20261101.json and
verification/issue-123/docs-decorator-resolution-20261101.json. Diff check passes.
The coverage fixture is historical, not a fresh capture. Native/generated,
consumer-cohort, browser and publication acceptance remain open; no canonical
promotion or live installation. D16/D27/D29/D30/D31 remain unchanged.

## Glyph-case artifacts and authored examples verified — 2026-11-01

Fresh wheel and sdist installs each pass 219 selected tests with zero skips,
including the three distribution gates. Same-process module origins remain in
the selected install; all 116 runtime files match source/archives/both installs.
Both environments have the same 28 distribution versions and pass dependency
checks. The earlier case-info-only artifact fails 52 lifecycle tests (3 controls
pass). Bounded independent source review found no implementation findings.

The authored Glyport guide adds an owned lifecycle example, preserves earlier
archive hashes and identifies the new ones separately. Each fresh install runs
all nine offline examples; all 17 Python blocks compile. The preceding artifact
fails the new example. Native snippets remain compile-only. Exact commands,
exit codes, archive/source hashes, failed controls and reports are retained in
verification/issue-123/glyph-case-artifacts-20261101.json and
verification/issue-123/docs-glyph-case-lifecycle-20261101.json. Diff check passes.

No native run, canonical promotion, generated rebuild or publication. Native
case/history/reopen, detached reset, custom metadata and the new consumer cohort
remain open; D16/D27/D29/D30/D31 are unchanged.

## Echopy helper-name guidance verified — 2026-11-01

Expanded the authored preflight example to reject _bind and _echopy_unavailable
while preserving previous output bytes. Documented all8explicit names, normalized
spellings, class-member allowance and remaining low-level/built-in limits. New
artifact hashes identify this example. Both fresh installs pass10offline examples;
all12blocks compile. Older deletion artifact fails the helper-rejection assertion.

Receipt: verification/issue-123/docs-helper-names-20261101.json. Diff check passes;
2native examples remain compile-only. Generated/build/browser/publication holds
are unchanged.

## Aidus read-preservation guidance verified — 2026-11-01

Authored guide distinguishes v0.2.1installation guidance from private dev4
repair evidence. It explains inner Unicode ownership checks and the remaining
CurrentGlyph preflight failure, and clarifies single-glyph metrics versus batch
script execution. Added offline package identity and tool-inventory examples.
Both fresh installs pass2offline blocks;1native snippet compiles only. Exact
artifact hashes identify the candidate; no native read-safety claim.

Page hash, commands and results:
verification/issue-123/docs-aidus-read-20261101.json. Diff check passes. Generated
references, rendered/browser acceptance and publication remain held.

## Echopy deletion example verified — 2026-11-01

Authored example now checks external deletion of an ordinary native-double
attribute, disappearance from lookup/dir and rebinding. Latest wheel/sdist each
pass10offline examples; all12blocks compile. Earlier alias-only wheel fails at
block12line41, the ordinary-deletion assertion. Module cleanup and installed
origins are checked. New archive hashes identify this example; prior constructor
and collision examples retain their historical evidence. Diff check passes.

Commands/page hash: verification/issue-123/docs-native-deletion-20261101.json.
Two native snippets remain compile-only. Generated reference, source-lock,
rendered/browser qualification and publication remain open under D29/D30.

## Echopy alias documentation example verified — 2026-11-01

Added an owned generation/merge example: absent offline annotation, live alias
reads after native-double reassignment, writes/deletes to original spelling and
finally cleanup. Exact archive hashes identify the private repaired artifacts.
Both fresh installs pass10offline examples;12blocks compile, including2native
snippets held at compile-only. The older artifact fails the missing-name
assertion. Explicit cleanup checks confirm no owned module registrations remain.

Commands, logs, page hash and limits:
verification/issue-123/docs-top-level-aliases-20261101.json. Diff check passes.
Authored docs remain uncommitted. Real FontLab, source-lock/generated rebuild,
rendered/browser checks and publication remain open under D29/D30.

## Glyph Info case documentation verified — 2026-11-01

Extended the owned Glyph Info example with database case filtering: exclam is
upper, while less and acutecomb are lower; these values are not Unicode general
categories. The fixture preserves active font metadata. Both installed private
case artifacts pass all eight authored examples; ten Glyport and six native-guide
Python blocks compile. Native blocks remain compile-only. The older script-only
artifact fails at GSGlyphInfo.case, as expected.

Commands use each existing artifact environment's python -I -B with external
TMPDIR. Exact commands, exit codes, installed origins, archive and page hashes
are retained under issue123/docs-glyph-info-case-20261101 in the external evidence
tree. Tested archive hashes are also recorded in the authored page.
No generated reference refresh, source-lock update, site build, browser check,
native execution or publication. D29/D30 and complete metadata/custom database
acceptance remain open.

## Glyph Info script documentation verified — 2026-11-01

Extended the owned global-lookup fixture with script metadata, Greek-name
filtering and None preservation. The fixture asserts active font metadata stays
unchanged. Fresh wheel and sdist installs each pass all eight authored Glyport
examples; all sixteen Python blocks across the package/native guide compile.
The older lookup-only artifact fails at GSGlyphInfo.script, as expected.
Archive hashes identify the tested private snapshots despite repeated versions.

Commands, exit codes, installed origins and page hash are retained in
verification/issue-123/docs-glyph-info-script-20261101.json. Diff check passes.
No generated reference refresh, source-lock change, site build, browser check,
native run or publication. D29/D30 remain open; full metadata and custom databases
remain incomplete. This verifies the authored example, not whole native scripts.

## Echopy collision example verified — 2026-11-01

Added a runnable owned example proving collision refusal preserves an existing
output file byte-for-byte and creates no replacement report. It explains scope,
retaining conflicting capture data, and limits on filesystem transactions,
reserved identifiers and identical-name duplicate records. Archive hashes identify
the new private snapshot despite a repeated version string.

Both installed artifacts pass all9offline Echopy snippets;11blocks compile,
including2native identity blocks that remain compile-only. Older constructor
artifact fails precisely the collision-refusal assertion. Glyport page bytes are
unchanged; diff check passes. Exact commands, logs and page hash are retained in
verification/issue-123/docs-name-collisions-20261101.json. Authored docs remain
uncommitted; no generated refresh, source-lock, site build, browser, native capture
or publication. D29/D30 and whole-workflow gates remain open.

## Echopy constructor-binding example verified — 2026-11-01

Extended the existing owned pipeline example with static/class constructors.
Captured bindings/unbound receiver and merged AST decorators, positional-only
arguments, defaults and None return annotations are checked without executing
generated declarations or fixture constructors. Both new installed artifacts pass
all8offline snippets;10blocks compile, with2native snippets compile-only.
The older same-version receiver artifact fails precisely AssertionError: StaticInit.

Page now records tested wheel/sdist SHA256 values. Glyport page bytes are unchanged.
Exact commands, expected exit1/positive exit0, logs and page hashes are retained in
verification/issue-123/docs-constructor-bindings-20261101.json. Diff check passes.
Authored docs remain uncommitted: no generated refresh, source-lock update, full
site build, browser check, native capture or publication. D29/D30 remain open.

## Glyph Info documentation example verified — 2026-11-01

Added an owned offline fixture contrasting name-derived0041 with current glyph
encoding0042. The lookup preserves current data; explicit local-font queries
raise the documented capability refusal. Both new installed artifacts pass all
8offline Glyport examples; all16Python blocks across Glyport/native guide compile.
The older same-version artifact fails precisely the new Unicode assertion.
Tested wheel/sdist SHA256 values are included because version strings repeat.

Exact commands, expected negative exit1, positive exit0, logs and page hash:
verification/issue-123/docs-glyph-info-20261101.json. Diff whitespace check passes.
This authored-doc candidate remains uncommitted. No source-lock update, generated
refresh, full site build, browser check, publication or native run; D29/D30 remain.
Custom-global/local databases and full lookup/native workflows stay open.

## Echopy receiver example verified — 2026-11-01

Extended the authored Echopy pipeline fixture with ordinary/constructor receivers
named receiver. AST assertions preserve positional-only arguments and defaults,
and reject invented self parameters without executing generated declarations or
calling fixture methods. The earlier clean artifact fails the exact new metadata
assertion; both installed dirty candidates pass all8offline snippets. All10blocks
compile; two native identity snippets remain compile-only. Existing Glyport page
hash2f0fd4bd remains unchanged in the shared isolated docs worktree.

Receipt: verification/issue-123/docs-receivers-20261101.json. Exact commands and
negative/positive logs retained under docs-receivers-20261101. Docs remain
uncommitted in docs-layer-names-20261101/fontlab-python-docs. No generated refresh,
source-lock update, site build, browser check, native calls or publication.
D29/D30 and whole-workflow acceptance remain open.

## Glyport layer-name examples verified — 2026-11-01

Expanded authored packages/glyport.md with identity/name distinctions, a raw
None-only whole-font filter and a clearly labelled FakeBackend fixture. The
example collects identities without deleting layers. Version and native-import
limits are explicit; existing master/background behavior is preserved.

All7offline examples execute unchanged with both installed candidate artifacts;
15Python blocks across Glyport/native guide compile. The older clean Glyport
artifact fails exactly at the new raw-name assertion, retained as a negative
control. Installed origins and fixture-byte preservation pass. Receipt:
verification/issue-123/docs-layer-names-20261101.json; external check.py,
run-checks.py, commands.json and logs retain exact commands/results.

Isolated docs-layer-names-20261101/fontlab-python-docs remains uncommitted. No
source lock, generated reference, full build, browser check or publication;
D29/D30 native/rendered acceptance stays open.

## 2026-11-01 — Read recorded signatures and test owned metadata

Expanded the authored Echopy page with a signature-reading table, a constructor
AST example and an owned static/class descriptor fixture through capture,
generation and merge. Explains positional/keyword-only parameters, defaults,
variadic fallback, unknown types, overload evidence and declaration age.
Known Python descriptors are not evidence for unknown PythonQt wrappers.

All10Python fences compile. Eight offline fences execute unchanged in separate
ordinary wheel and sdist installations of Echopy0.2.4.dev6+ga4f2fbf48; package
origins are under each environment and no native modules are imported. The two
native identity snippets remain unexecuted. No generated declaration is executed.
The first verifier run expected11blocks instead of10; only its count assertions
were corrected. Both failed commands and final outputs are retained externally.

Exact commands/exit codes: ../commands-initial.json (exit1 twice), ../commands.json
(exit0 twice), using the external verify_examples.py with -I -B. Evidence root:
/Volumes/Falstaff4T/fontlab-scripting-data/issue123/docs-signatures-20261101/.
AST reference: https://docs.python.org/3.11/library/ast.html#ast.arguments .

No generated reference, source-lock refresh, full site build, browser check,
canonical promotion or publication. D29 and native D30 remain open.

## 2026-11-01 — owned dialog/settings examples and chooser boundary

Expanded authored guide/ui.md with an owned-dialog example using App completion,
explicit temporary-INI settings, geometry lifecycle guidance, and pinned Qt5.15.2
QFileDialog findings. Its scoped QtProject constructor hardcodes NativeFormat;
setDefaultFormat/setPath do not isolate the macOS store. Cocoa helper refuses a
priority-hint native chooser. No actual QFileDialog or owner preferences touched.
These source findings do not qualify FontLab's compiled Qt or the three routes.

Two new examples pass six cases each under standalone Qt5.15.19 and Qt6.12.0:
INI roundtrip, forwarded clicked(True), actual Close button, Close, Escape and
replacement. Real App completion/cleanup/launcher, owned substitute main window.
Qt5 uses source App; Qt6 uses ordinary installed App. Initial cold from-package
import failed; direct submodule imports fixed it. Explicit bool forwarding then
reproduced the Close bug; a lambda discards arguments. An actual Qt6 click alone
had passed, so it was not used as proof of PythonQt signal semantics.

Independent review clears the final page. Raw-source physical anchors and hashes
verified; earlier web-extracted line-number suggestions were discarded. Page hash
04c7c03985f1816ab4bba49dde99a7c92dad0055d023d219383e289745f84c7d.
No generated page, source lock, theme, canonical checkout or publication change.
D29 still blocks the complete site build/render/publication acceptance.

Commands through rtk proxy, final exit0 (initial failures retained):
- env QT_QPA_PLATFORM=offscreen PYTHONDONTWRITEBYTECODE=1 /Volumes/Falstaff4T/fontlab-scripting-data/issue123/standard-message-priority-20261101/ordinary-artifacts/wheel-env/bin/python -B /Volumes/Falstaff4T/fontlab-scripting-data/issue123/chooser-settings-audit-20261101/verify_guide.py /Volumes/Falstaff4T/fontlab-scripting-data/issue123/docs-guide-20261101/src_docs/md/guide/ui.md
- env QT_QPA_PLATFORM=offscreen PYTHONDONTWRITEBYTECODE=1 FONTLABAPP_TEST_QT5=1 PYTHONPATH=/Volumes/Falstaff4T/fontlab-scripting-data/issue123/standard-message-priority-20261101/fontlab-fontlabapp/src:/Users/adam/Developer/vcs3/github.fontlabcom/fontlab-scripting/fontlab-fly/src /Volumes/Falstaff4T/fontlab-scripting-data/verification/issue-120/typed-date-z11/qt5-env/bin/python -B /Volumes/Falstaff4T/fontlab-scripting-data/issue123/chooser-settings-audit-20261101/verify_guide.py /Volumes/Falstaff4T/fontlab-scripting-data/issue123/docs-guide-20261101/src_docs/md/guide/ui.md
- Docs candidate: git diff --check:exit0.

Wait, but: only the two new examples were exercised, not the older controller
example or every API. Native PythonQt, actual chooser and rendered-site acceptance
remain open. Evidence: external chooser-settings-audit-20261101; root report
verification/issue-123/chooser-settings-boundary-20261101.md.

## Unreleased — issue 122 package pages

- The App page shows font-level master edits as one Undo step (`master_metrics.write_master_metrics`, `zone_native.backend()`), their refusals and rollback, the fl#8574 guideline caveat, and `outline_extent` for stale boxes (fl#8575). Authored page only; no build.
- The App page lists only the `[fontui]` extra and its five tools (browsers, preview, features editor, designspace panel); the `[fontedit]` and `[fontsequence]` extras no longer exist.
- The FontParts-bound editors (`font_info_editor`, `groups_editor`, `kerning_editor`, `transform_editor`, `batch_panel`, `glyph_sequence`) are documented on the Fontport page under "UI editors", with an example. Authored pages only; the generated site and source lock are not rebuilt (publication stays gated).

## Unreleased — preserve generated distribution bytes (N132)

- Publish 5,996 API pages for the reviewed App .98 source checkpoint used by
  the 37 Examples / 107 Scriptmix menus. Their source/download pairs belong to
  separate menu sites; this release does not establish those sites' deployment.
  Later candidates are outside this checkpoint; complete native workflows remain open.
- Retain all 278 legacy routes and 128,733 archive fragments, full native API
  identity reconciliation, search, licences and desktop/mobile navigation.
- Preserve the accepted 6,950-file publication payload byte-for-byte through
  Git staging and checkout, including three CRLF upstream licence notices.
- Verify the unchanged release hook: 370 tests, all nine changed production
  modules above 80% statements and branches, with zero exclusions. Local browser
  interaction checks pass all 28 cases; deployment verification follows upload.

## v1.0.5 — Glyport v1.0.1, Aidus Code v0.2.1, Echopy v0.2.2 (2026-10-16)

- Rebuilt from Glyport v1.0.1 (a81c6f5), Aidus Code v0.2.1 (32523d4) and Echopy v0.2.2 (f6e2d75); the Glyport,
  Aidus Code and Echopy guides state the documented versions.
- Glyport guide: glyph creation keeps existing composites that FontLab re-resolves (fontlab/fl#8512).
- Aidus Code guide: installer note.
- Artifact: final-18 (docs deb4171), all 16 gates passed; review X4s APPROVE.

## v1.0.4 — Fontport v1.0.2 and Fontlabapp v0.2.4 (2026-10-16)

- Rebuilt from Fontport v1.0.2 and Fontlabapp v0.2.4 (with glyport acca128, Echopy 791fa55).
- Fontport guide describes v1.0.2: the first Undo restores glyph edits (one extra empty row,
  `glyph.exactSingleUndo`); info metrics, style name, note and the structured Panose, OS/2
  weight/width class and stem snaps go to the key master only; named refusals; opt-in strict mode.
- Fontlabapp guide: FontUI structured info fields (key master), unfinished-script-edits note,
  `.refresh()` availability per tool.
- Packages page: editable install from a checkout into FontLab's Python environment.
- Artifact: final-17 (docs 266b3f3), all 16 gates passed; review X4r7 APPROVE.

## v1.0.3 — reference rebuilt on the latest packages (2026-10-16)

- Rebuilt from glyport acca128 (Glyphs 4.1.1 profile, geometry helpers), Echopy shims 791fa55
  (adds `vanilla.test` and `vanilla.vanillaBase`), Fontlabapp v0.2.2 (FontUI browsers and editors)
  and Fontport v1.0.0.
- Fontlabapp guide: new FontUI section (extras, minimal browser example, handle lifecycle).
- Search starts on plain-http pages too (fallback when `crypto.randomUUID` is unavailable).
- Publication safety: `docs/` is promoted from the accepted build path for path, and the release
  checks that git tracks every published page.
- Artifact: final-13 (docs a54ee2d), all 16 gates passed; review X4r4 APPROVE.

## v1.0.2 — complete v1.0.1 publication (2026-10-16)

- Publishes 4 TypeRig pages (`typerig.core.objects.instance`) that a template `.gitignore` rule
  dropped from v1.0.1; their 20 identities and 20 Fly aliases resolve again. `docs/` can no
  longer lose pages to ignore rules.

## v1.0.1 — published reference (2026-10-16)

- Publishes the reviewed reference at https://code.fontlab.com/fontlab-python-docs/ (master:/docs):
  242,654 captured native identities documented; Echopy shims for GlyphsApp, vanilla, AppKit,
  Cocoa, Foundation, objc, FontLab menus/panels and the Aidus tools; ecosystem packages Echopy,
  Fly, Fontlabapp, Remopy, Grablab, Pythonqtside, Glyport, Fontport (D14), TypeRig and Aidus Code.
- New Packages section: overview, install, quick start, examples and limits for each package.
- The previous FontLab 7 / PythonQt reference stays available under `archive/fontlab7/` with its
  original routes.
- Artifact: final-11 (docs 9161c0c), all 16 gates passed; review X4r2 APPROVE.

## Issue 106 — completed (lane C3, 2026-10-16)

- [x] Release audit decodes layered escapes (JSON/JS `\uXXXX \xXX \/ \\`, percent, HTML
  character references incl. numeric ones without `;`), re-parses JSON nested in strings and
  fails closed (`decode-limit`) beyond its bounds (a211a02, 4e61a68, f712bec, 9633e1d).
  X4b/X4c findings; X4f and X4n APPROVE.
- [x] Finder `.DS_Store` written into the generation stage no longer breaks a build (d6a4280).
- [x] lunr 2.3.9 TokenSet key collision (upstream olivernn/lunr.js#503) patched in every
  shipped search engine: complete-search bundles at compile time, stock MaterialX worker after
  each build (3ad6570). X4n APPROVE.
- [x] Front-coded routing vocabulary keeps the R041 5 MiB initial search budget: initial
  payload 3,078,385 bytes (2118409). X4n APPROVE (862,620 terms round-trip).
- [x] Consolidated rebuilds at merged glyport: final-10 all 16 gates exit 0 (300 tests; release
  audit 6,002 files, 0 findings; determinism identical; 242,654/242,654 identities); lock
  6395a8f. Evidence: workspace `verification/issue-106/evidence/C3/final-1/` .. `final-10/`.

## Issue 104 — completed (lane L5, 2026-10-15)

- [x] Coverage reconciled against Echopy's capture identity manifest in every
  build: 242,654/242,654 captured identities documented, 0 unexplained; native
  spellings recorded; single-underscore native members documented (R014, G09).
- [x] Shim references: `fontlabapp_shim`, `GlyphsApp`, `GlyphsApp.plugins`,
  `vanilla`, `vanilla.dialogs`, `AppKit`, `Cocoa`, `Foundation`, `objc`,
  `aidus_code_tools`; unresolved shim exports and discarded aliases fail the build.
- [x] `./build.sh --serve` (under `/fontlab-python-docs/`) and installed-artifact
  mode (`FONTLAB_API_SOURCE_ROOT`) run and recorded (R039).
- [x] Deterministic rebuild: source and artifact modes render identical bytes;
  privacy/licence audit of site, search shards and source maps (R044, R055).
- [x] Decisions: archive routing (redirect + current link) and shard deadline
  (no partial results; Retry doubles the deadline to 30 s).
- [x] Publication runbook with deployed-host checks (`deployed_check.py`,
  `interaction_check --base`), previous deployment kept by tag (R042, R044).
- [x] Browser checks fixed at their cause (server backlog, readiness waits);
  five consecutive interaction runs pass.
- [x] Examples docs export integrated and pinned.
- [x] Review rounds R-L5-docs, RR-docs, RR2-docs fixed test-first.

## Unreleased — issue 104 review fixes (R-L5-docs)

- Release audit: current credential formats (incl. `github_pat_`), inline
  `data:` source maps and JSON-escaped strings decoded, mounted-volume and
  checkout paths, private repository URLs and names (from local git remotes),
  exact reviewed example values instead of a `file:///` prefix, licence texts
  verified by digest and linked from the licences page.
- Reconciliation: multiple declarations explained only by exact structure
  (getter/setter/deleter, module+class facet, module+parent attribute) or a
  line-pinned review; aliases discarded by resolution are reported.
- `deployed_check`: every `assets/` file (worker, search UI, theme) and header
  validation (media types; no Content-Encoding on explicit `.gz`).

## Unreleased — issue 104 coverage reconciliation (R014)

- `scripts/reconcile_coverage.py` reconciles every build against Echopy's capture
  identity manifest; the build fails on any missing, uncaptured or multiply
  declared native identity, capture error, unmatched overlay or dangling alias.
- Single-underscore members of captured native classes (14, e.g.
  `PythonQt.private.MainWindow._clear_outline_controls`) are now documented.
- `_identities.json` and `_provenance.json` are pinned in the API source lock.

## 2026-10-15 — completed checklist (moved from TODO.md)

- Verify source-only native documentation names through actual mkdocstrings.
- Add explicit locked mkdocstrings Python handler/autorefs/Griffe dependencies.
- Test full-occurrence inventory, exact body sharing, pagination and facets.
- Generate current native and ecosystem API pages, coverage report and aliases: strict full build 212 s, 4,331 pages, 245,151 member identities, 60,048 search rows, `--check` pass (docs f8bb92a, 3ddc4e0). Reconciliation against the raw Echopy capture (R014) remains open.
- Rebuild the current local root with verified shared theme asset/search ownership.
- Implement and verify locked offline build/check and API source byte pins.
- Verify actual inventory URI anchors, nine native searches and responsive method page.
- Verify remaining internal links, alias families and keyboard/focus interactions (R043 receipts: deep/type/param-type links, aliases, late shard search and keyboard 4/4 each; a11y 28/28; workspace evidence r043-interactions/, tg8-theme/).
- Complete consumed private-input locking, exported class-member aliases/public titles and @property index semantics; see docs/superpowers/plans/source-reference-fidelity.md.
- Resolve final I1–I5 and M2/M3 documentation defects with 66-test source/browser regressions.
- Provide a build-plus-consumer command that fails on missing inputs and provisions Chromium.
- Implement complete search sharding, original consumer comparisons and checked initial5MiB startup transfer.

## 2026-10-14 — R042 archive pages link their current page

- Archived FontLab7 pages whose route map has an exact `current_route` now carry a
  visible "Current version of this page" link in the archive banner. It is generated
  at build time from the same `route-map.json` report; on load and on `hashchange`
  it retargets to the mapped current anchor for the URL fragment, else the page target.
- Legacy routes still redirect to the archive with their fragment (unchanged).
- Site verification fails when an archived page's link, or its fragment map,
  disagrees with the recomputed route map, or a page without a current route has one.
- The interaction receipt now asserts the link on the archived legacy target.

## 2026-10-14 — R043 interaction receipts

- Add `scripts/interaction_check.py`: Playwright receipts at 1280x800 and 375x812
  in light/dark for member deep links (hit-tested clear of sticky chrome),
  signature type links, alias resolution (inventory, search by alias, legacy
  redirect), a search result held back by a 1.5 s delayed non-initial shard
  (absent before the delay, same-tab open, Back) and keyboard reach (skip link,
  search, navigation or its drawer opener, first content link, `/`/`s` recorded).
- Add passing and failing fixture pages for every check.
- Built-site receipt: type links fail 0/4; the rendered signatures carry no
  cross-reference links (signature_crossrefs is not enabled). Other cases pass 4/4.

## 2026-10-14 — R043/R044 accessibility and CI gates

- Correct accessibility checker timing for animated focus rings, hidden-control
  naming and responsive search/navigation targeting. Test reachability in any
  order within 40 Tabs; retain off-screen/absent focus indicators as failures.
- Record unmeasurable contrast separately under `needs_manual`; retain the
  strict 4.5:1 failure threshold and fail provably transparent unreadable text.
  Add passing/failing regression fixtures for each correction.
- Add local Playwright accessibility acceptance with JSON receipts for seven
  representative pages at desktop/mobile sizes in light/dark schemes. Check
  overflow, keyboard reach/focus, headings, image alternatives, control names
  and 4.5:1 text contrast; retain unmeasurable backgrounds for manual review.
- Add tiny passing/failing browser fixtures and workflow/receipt regression tests.
- Add Ubuntu documentation CI with locked dependencies, sibling producer
  checkouts, consumer/build/accessibility gates and retained artifacts. Document
  the private-source read secret and distinguish CI acceptance from deployment.

## 2026-10-14 — legacy route map

- Emit deterministic `route-map.json` with all original HTML routes/fragments,
  exact public identity targets and broken-in-original internal link diagnostics.
- Verify map completeness, archived anchors and redirect agreement during build
  and check; retain named anchors as well as HTML IDs.

## Unreleased — native source reference verification

- Reopen and reconcile search status/retry channels after persisted page restoration;
  preserve the original empty-result behavior for Lunr query parse failures.
- Shard complete search rows without dropping identities, aliases or fields;
  route globally through checked vocabulary/postings and hydrate with the original
  pinned MaterialX/Lunr engine. Gate actual initial static transfer at5MiB,
  including explicit gzip metadata, bootstrap, worker and retry UI.
- Preserve configured search suggestions, show unavailable/retry states separately
  from no matches, reject corrupt metadata/shards and suppress superseded results.
  Ordinary source builds remain offline after dependency bootstrap.
- Keep known empty namespaces authoritative, evaluate source decorator approval
  against its active declaration/dependencies, and invalidate shared class
  attributes across aliases after source writes or deletes.
- Resolve source bases from declaration-time bindings and class-body scopes;
  preserve source-known imports/aliases/star exports while leaving overwritten,
  future and dynamic bindings unresolved. Correct Qt wrapper and dialog lineage
  without changing source identities, URLs or existing supported aliases.
- Rank native module namespaces ahead of descendant class prefix matches using
  supported MaterialX document boosts; verify twelve real worker queries against
  the complete index while retaining every source row and exported alias.
- Keep source-derived callable signatures and property annotations visible below
  exported member headings using supported consumer signature rendering options.
- Qualify native module/class whole-page search entries from source coverage URLs
  so exact public module aliases such as fly.fl reach their primary native page.
- Respect explicit aliases and source declarations at every intervening export
  prefix; replacement classes cannot inherit unsupported descendant aliases or
  resolve nonexistent forwarded members through an overridden ancestor.
- Pin every consumed private/runtime/stub input once and reject duplicate lock
  identities; source input changes still require explicit lock refresh.
- Expand proven module/class re-exports to descendant aliases, preserving native
  names, canonical identities and shared declaration bodies.
- Display public package exports for authored private implementation classes while
  retaining stable source directives, URLs and canonical anchors.
- Classify source properties as attributes and retain getter/setter/deleter
  provenance, exact declaration hashes and occurrence accounting.
- Verify the changes with focused fixtures, a strict source-only MkDocs render,
  the existing suite and a complete read-only source inventory comparison.
- Preserve qualified native method names and exported aliases in search; skip
  stemming of API identifiers and rank module/class targets ahead of prefixes.
- Verify every expected objects.inv URI against actual rendered HTML anchors.
- Pin API input bytes across source/artifact modes; require explicit lock refresh.
- Add repeatable Chromium search/deep-anchor and mobile/light/dark smoke receipts.

## Expanded reference — unreleased

- Generate complete native and ecosystem source references with actual native
  identities, retained occurrence indexes and paginated shared declaration text.
- Add source-only namespace/import discovery, complete anchor and objects.inv
  verification, locked build/check/serve/explicit native-refresh entry points.
- Preserve the previous FontLab7 site in a verified archive with fragment-aware
  redirects and archive context.
- Add current installation/native/UI/compatibility/build guides and shared-theme
  styling; full browser/search and deployment acceptance remain in progress.

## 2026-09-23

- Publish the API documentation with ProperDocs/MaterialX and shared fltheme26 assets.
- Keep generated API HTML, routes, anchors and styling; use core search for the large PythonQt pages.
- Add a reproducible root-then-child build with source-owned CSS.

- Preserve API 404 asset/home routes under the GitHub Pages project prefix.
- Bridge the core search index to the existing MaterialX search UI and verify index preservation.


## Source-reference final review fixes

- Index every shared occurrence and alias at its canonical body; enforce complete
  search identity coverage and a non-skipping 15-query shipped-consumer gate.
- Generate into fresh owned input trees and seal accepted input/rendered manifests;
  deterministic checks reject missing baselines and stale content without rewriting
  accepted artifacts.
- Preserve legacy root fragments under static-host prefixes and expose the archive.
- Render source-proven bases and inherited canonical member indexes with Griffe C3
  ordering, authoritative overrides and nested-class navigation.
- Correct the PySide runner guide to describe its implemented scoped contract.
- Record the provisional 7 MiB complete-search allowance; initial 5 MiB payload
  sharding, clean CI and broader publication acceptance remain unfinished.

- Removed the GitHub Actions docs workflow (owner decision); acceptance gates run locally.

## 2026-10-18 — documentation source layout

Set up `src_docs/mkdocs.yml` and `src_docs/md/` with ProperDocs 1.6.7,
MaterialX 10.1.5 and the shared fltheme26 assets. Local builds write `docs/`.
Source-backed code blocks use codeinclude; shared prose uses include-markdown.
Tags, directory metadata, categories, navigation and local editing use the tested
plugins. The two smaller sites have a combined print page. The API site retains
its complete search, archive and source-only reference pipeline.

The obsolete ToC-sidebar plugin fails on removed `mkdocs.utils.string_types`.
The breadcrumbs plugin mutates Markdown inputs and pulls in the overlapping
Material distribution. Use MaterialX's native ToC and `navigation.path` instead.
These decisions follow isolated installation/build trials; neither plugin is
installed in the final environments. No remote publication is included here.

## 2026-10-21 — private final-producer docs candidate

- Preserve reviewed public-source/browser-notice producer payload and all owner
  preimages; explicitly pin734 reviewed current source inputs.
- Locally build/verify final App220/Glyport115 API with5925pages; retain unchanged
  archive/route/search limits,343tests and28/28interaction/accessibility gates.
- Keep canonical application and publication pending root review.

## 2026-10-21 — App.74/Fontport7a source checkpoint, not publication

- Pin the reviewed Fontport App Vanilla compatibility import within734API inputs.
- Build/verify current checkpoint aliases with343tests and targeted browser/worker
  controls; preserve prior N60 evidence and all owner source/index/docs preimages.
- Keep later App.76/.80 producer refresh, root-reviewed feature/canonical delivery
  and publication separate; no native acceptance is advanced.

## 2026-10-21 — N83 final source graph and actual TypeRig discovery

Private checkpoint aligns App86721bf(.80), Glyport2c46, Fontport7a,
Examples657bb1e(31) and Scriptmixd54ee17f(105). Reviewed734→743APIinputs:
nine new Pattern Lab/report-pair modules and one owned dialog-close fix.
Preserve N65 .74 evidence as historical. Actual TypeRig sources live in
TypeRig/Lib; producer and real Void inheritance regression now share source_roots,
including explicit installed-artifact roots, without a fabricated legacy alias.
Before-fix regression fails; corrected targeted25tests pass. Final strict
three-site, routes, browser/worker/accessibility and exact notice checks follow
in verification/issue-120/docs-final-checkpoint-z33; no native/publication claim.

N83 verification: all three strict sites pass; API348 required-consumer tests
pass without skips, existing interaction28/28 and accessibility28/28 pass.
Every136menu source block matches its current source; actual worker13queries
and18body views pass. Exact served notices25API/26per menu site and release
audits pass with each site's existing licence policy. All185actual TypeRig
inputs match the reviewed lock/snapshot, and unchanged Void/Point assertions
pass on configured TypeRig/Lib. Extra menu-site accessibility discovered mobile
notice-page navigation reach failures; retained as a separate N90 publication
gate. No checker budget was waived. This source checkpoint is App.80/105menus;
it does not include the private .84/106candidate, native acceptance or publication.


## 2026-10-21 — Primary site navigation audit correction

- Prefer actual primary tabs/sidebar navigation over article tag metadata; keep
  the original40Tab/5Tab limits and every existing accessibility assertion.
- Add six focused browser regressions; preserve N83's743-input .80/105 source
  checkpoint and all existing menu/theme/notice bytes. Publication remains gated.


## 2026-10-21 — N118 reviewed .98 documentation checkpoint

Pin the reviewed App .98/Examples37/Scriptmix107 source checkpoint and unchanged other producers; retain .80 history and exclude moving .100. Add source checkpoint and current App/SimonCozens licence notices. Preserve inherited owner prose and publication/native gates.


## 2026-11-01 — Authored Echopy guide

Expanded packages/echopy.md with installed version/origin, alias identity,
sidecar discovery/AST reading, NativeUnavailable handling, provenance reading,
native identity-only checks and PythonQt/session limits. Removed obsolete fixed
v0.2.3 claim and misleading placeholder signature inspection example.
Six offhost Python blocks executed with the verified Echopy environment's Python
using -I -c, exit0 each; two native blocks compile only, not host-tested.
Evidence: external issue123/docs-guide-evidence-20261101/snippet-results.json
and per-block logs. No generated reference, source-lock, site build, theme,
canonical checkout or publication change. D29 remains in force.

## Native writer result/error examples — 2026-11-01

Expanded authored guide/native.md with queue-warning/result fields, a host-free
formatter and a Raise Ascender wrapper that retains disclosure and reraises the
original error. Explains no-op queue-not-sampled semantics, exact all-layer scope,
Perpendicular Guides output, partial-write uncertainty and no automatic retry.
Contract is explicitly the ordinary App0.2.26.dev155+g5513c0783 candidate, not a
published release or native acceptance claim. Independent source review passes.

Exact marked snippets pass14checks with real installed formatting helpers and
a substitute native backend; both scopes, success/no-op, early/partial/constructor
failure, warning de-duplication and original exception identity are checked. All
3Python blocks compile; the original native identity/construction block is not
executed. No generated reference, producer lock, theme or build output changed.

Command from /Volumes/Falstaff4T/fontlab-scripting-data/issue123/native-guide-20261101
(exit0; result.log):
`rtk proxy env UV_CACHE_DIR=/Volumes/Falstaff4T/fontlab-scripting-data/uv-cache TMPDIR=/Volumes/Falstaff4T/fontlab-scripting-data/tmp PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run --isolated --no-project --python /opt/homebrew/bin/python3.11 --with /Volumes/Falstaff4T/fontlab-scripting-data/issue123/perpendicular-queue-20261101/dist/fontlab_fontlabapp-0.2.26.dev155+g5513c0783-py3-none-any.whl --with pytest python -I -B -m pytest -q -p no:cacheprovider test_guide.py`.
`rtk proxy git diff --check`:exit0. External report.json pins the final page.
Wait, but substituted native calls do not qualify FontLab editing or preservation.
Native execution and site build/browser/publication remain behind existing gates.

## 2026-11-01 — background removal preview and failure example

Extend the authored native guide with explicit preview/apply functions for complete
background-object removal. Document both whole-font scopes, shared-mask refusal,
counts, no-op disclosure, stale previews, partial errors and interruption notes.
Use actual Scriptmix menu titles. Update example checkpoint to ordinary App
0.2.26.dev158+g55fc09868 and correct duplicated Perpendicular Guides wording.

Exact snippets:27checks pass against each ordinary wheel/sdist. Four Python blocks
compile. Background12cases use the actual installed backend/planner and owned
native doubles; Raise Ascender10wrapper cases substitute its backend, while
four formatter cases use the shared helper. Compilation adds one check.
No native, rendered-page, generated-reference/source-lock or publication claim.
D29 still holds those stages; source-only authored documentation is permitted.

Evidence: external issue123/background-guide-20261101/checks.log and sdist-checks.log.
Command cwd is that evidence directory:
`rtk proxy env UV_CACHE_DIR=/Volumes/Falstaff4T/fontlab-scripting-data/uv-cache TMPDIR=/Volumes/Falstaff4T/fontlab-scripting-data/tmp PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 uv run --isolated --no-project --python /opt/homebrew/bin/python3.11 --with /Volumes/Falstaff4T/fontlab-scripting-data/issue123/background-interruption-20261101/dist/fontlab_fontlabapp-0.2.26.dev158+g55fc09868-py3-none-any.whl --with pytest python -I -B -m pytest -q -p no:cacheprovider test_guide.py test_background_guide.py` — exit0.
Repeat with the same version's .tar.gz in place of the wheel — exit0.

## 2026-11-01 — bound selection examples

Add two authored native-guide examples: bound Font-window selection read with
package.id/fgId distinction and deadline; additive report selection with total
name count and partial-failure semantics. Document empty scope, stale identity,
active-window guard, duplicate chart cells, no UpdateAll and the unresolved
filtered-cell snapshot. Existing writer examples/version checkpoints unchanged.

Execute exact Markdown snippets against ordinary installed App0.2.26.dev159+
gb1e905b61, replacing only native module access with owned doubles. Fourteen
behavior cases pass; all366installed App runtime hashes also match (15checks
total). SixPythonblocks compile. No generated references/source-lock/site output
changed; no full build, browser or native run under D29.

Command from external docs-selection-20261101/tests:
rtk proxy env -u PYTHONPATH PYTHONDONTWRITEBYTECODE=1 PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
/Volumes/Falstaff4T/fontlab-scripting-data/issue123/colour-selection-20261101/env/bin/python
-I -B -m pytest -q -p no:cacheprovider test_selection_examples.py test_artifact_integrity.py
(exit0). Tests, hashes and exact snippets retained externally; root report records
review and commit. git diff --check exits0.

Wait, but: doubles do not prove native font, history, view-state or timing
preservation. Rendered-page and whole-branch publication gates remain open.

## 2026-11-01 — Glyport detached-transform examples

Added four executable examples for matrix mapping, non-finite refusal, overflow
preflight and repeated object identities, with explicit native/setter limits.
Added existing fly.gp/fly.fp aliases to the native guide. No dependencies changed.

Verification: six marked examples extracted directly from Markdown pass in both
the final Glyport dev58 wheel and sdist environments with App dev159. Owned source
fixtures retain their exact bytes; inspect/adapt never execute them. Both new
aliases resolve to canonical modules. All 14 Python blocks in the two pages compile.
Commands and exit codes: external docs-transform-20261101/commands.json; both
`rtk proxy <final-wheel-env or final-sdist-env>/bin/python -I <check.py>` exit 0.
The initial harness completed example/alias assertions but failed reporting with
PackageNotFoundError: fontlabapp; corrected distribution names to
fontlab-fontlabapp/fontlab-fly and reran both.

No native calls, full site build, generated reference refresh, source-lock change,
browser verification, promotion or publication (D29/D30 remain open).

## 2026-11-01 — Consolidate the final candidate

Merged the retained candidate into the consolidated branch, preserving the newer
branch changes. Verification from the workspace root:
`rtk proxy sh .metaswarm/quality.sh coverage "$CHECKOUT" fontlab-python-docs`
(`CHECKOUT` is this isolated checkout): 369 passed, one full-corpus test skipped; exit 0.
Authored guides are merged; the restored published build is retained.
This test run does not qualify a new rendered site or native guide examples.
No native FontLab operation was run.


## 2026-11-02 — Complete-generation authored companion

Document actual ten-job Chinese and full queued Hangul algorithms using four
explicit invented banks and owned Jamo/targets. Replace the obsolete recording-only
shared setup; preserve all 89prior tagged bodies (82 active/seven held). Add eight
runnable examples for complete fixed ranges/profile/field/index checks, collision
identity, callback completion order, actual Jamo tuples, component storage,
current queued lookup and explicit missing-input/partial-failure state.

All90active examples pass exact GP5a54b4b source;150 Python blocks compile,
44 local links resolve,141 of 142 prior blocks retain exact bytes (only the setup
changes), and all 7,469protected payloads/modes plus index/nav/lock remain exact.
Retain the seven expected baseline setup failures and correction ruling in
external info-generation-companions-20261102/docs-evidence/. Root owns the normal
docs gate and matching ordinary tuples/consumers. No dependency/generated/native/
canonical/publication change; D16/D29/D30/D31 and native/default-resource gates
remain. This authored source result does not complete Issue123.


## 2026-11-06 — GlyphsApp documentation entry point

Restore `reference/GlyphsApp.html` through an authored compatibility page that
explains Glyport's actual per-script factory and links the source-derived helper
reference. Preserve every existing source identity, producer lock and whole-index
search assertion. The complete frozen-input local consumer passes; native
workflow acceptance and publication remain separate.

## Issue 233 complete light-theme/CI candidate — 2026-11-06

- Added supported fixed light palette, shared menu/footer and a scoped real search-dialog stacking fix without replacing the complete worker/index.
- Added immutable private-input bootstrap, private diagnostics, strict three-surface audit disposition and main-only X/Y build/publication/Pages qualification with source-epoch transfer.
- Expanded real acceptance checks for shadow controls; positive and deliberately broken focus/name/reach/opener/stacking fixtures retain existing oracles.
- Final local gates: 435 Python / 0 skips / 1 inherited warning, 23 Node, 20 mandatory worker queries, 28 accessibility, 28 interaction, 2 stored-dark/global-control cases, accepted check and promotion; raw audit remains exit1 with exactly 3 reviewed findings. Whole changed Python module coverage remains above 80% with no exclusions. Local interaction-server BrokenPipeError is retained.
- Preserved the exact source lock, complete native/reference/search/archive identities and legal inventory. Independent review, installed hook, actual main/CI/Pages/live behavior, current providers and native workflows remain separate. No product commit or push occurred.

## 2026-11-06 — Search manifest compressed-size correction

- Record the actual produced manifest gzip size in the bootstrap; preserve raw
  hash, compressed size, decompression, complete-search and budget checks.
- Add real alternate-gzip and missing-manifest regressions. All 17 focused tests
  pass; complete changed-module coverage is 87.0968% with no exclusions.

## 2026-11-06 — Migration oracle source-root correction

- Honor the existing frozen package-root setting in the migration helper while
  preserving sibling checkout use and strict missing-input errors.
- Cover explicit-root precedence, absent/empty settings, missing inputs and
  native-package import avoidance. Existing migration assertions remain unchanged.
- Nine focused tests pass; complete module combined coverage exceeds 80% with
  no exclusions. Hosted source CI and publication remain separate gates.

## 2026-11-07 — Two source-bound archive helper notices

- Retain the exact TinySegmenter BSD and stopwords-filter MIT notices with their
  original copyright, wording and verified source/member bindings.
- Attribute only the demonstrated French stopword derivation; preserve all 102
  helpers, existing legal texts and incomplete transitive-review fields.
- Ten focused notice tests pass, including malformed bindings and real Git
  stage/checkout/archive checks. Full build and delivery remain separate gates.

## 2026-11-07 — PythonQt archive search repair candidate

- Restore ordinary literal completions, including callable and available QPen
  help, with the approved existing-engine BM25/boost/grouping policy.
- Preserve explicit query parsing and messages. Pure-negative queries now score
  finite zero instead of the original theme ratio producing NaN.
- Retain preferred sources, exact original dependencies/licences, locked compiler,
  truthful maps, full regression fixtures and preflight installation. All twelve
  PythonQt configurations use the content-addressed derivative, including404.
- Source/local candidate only; hosted delivery and publication require review.


## Task43 PythonQt archive rendering candidate

- Escape literal help representations only in the archived PythonQt search
  template while retaining worker messages, marks, grouping and routing.
- Add a pinned preferred-source UI build, truthful maps/full notices and complete
  joint worker/UI preflight; retain original assets and add four UI artifacts.
- Add full-message DOM/branch/build failure tests and run the UI suite in both
  common hosted build lanes. Independent review and actual delivery remain gates.


### Task43 scoped archived-404 asset correction

- Rewrite only four inherited absolute asset hrefs on archived PythonQt404 to
  their existing archive-relative destinations, with exact link/member preflight
  and no partial worker/UI output on missing, corrupt or ambiguous input.
- Retain all other page bytes, existing assets, worker messages and8001 published paths;
  qualify the corrected source/output cohort separately from its predecessor.


### Task46 archived content initialization and404 search base

- Keep existing content component streams/order and RxJS zero/one lifecycle while
  avoiding a large function-argument list for multiple streams. Cover the complete
  module at the real source-bound lexical article-link scale and every feature.
- Correct only archived404's uniquely expected search base through the existing
  buffered preflight; reject missing, unexpected and duplicate/ambiguous bases
  without partial output. Preserve the earlier four href corrections and index.
- Record both preferred-source overrides and regenerate the content-addressed UI
  assets. Whole module source/local tests do not establish browser or delivery acceptance.


### Task49 source-only visibility dispatch candidate

- Route observer entries through per-target RxJS Subjects, preserving existing
  observer, duplicate-subscription, ordering, error and cleanup semantics. Release
  unused channels even on unobserve failure without deleting reentrant replacements.
- Retain fourteen old/new lifecycle oracles, add bounded dispatch-work/edge tests
  and actual source-bound checks of all four caller pipelines and boundary export.
- Record the third preferred-source override and rebuild the exact UI artifacts;
  all56 Node tests pass. Current full builds, browser and delivery remain unqualified.


### Task61 source-only generation provenance portability candidate

- Normalize only the explicitly selected resolved API root in literal generated
  YAML list-path fingerprint inputs, after the existing docs-root replacement.
  Preserve exact scalar boundaries, relative tails, semantic values and runtime
  YAML; unset/empty selection keeps the existing behavior.
- Add actual generated-root relocation, aligned fixture/environment, real
  expanduser/resolve, literal space/quote and outside/prefix/semantic regressions.
  Folded and escaped representations are outside this literal-path correction.
- Focused64/full601 Python and all56 Node tests pass; all13 complete production
  coverage gates exceed80%. Retain the inherited Python warning and ten Lunr
  notices. Reused predecessor consumer prerequisites are not a new successor
  site or independent pair/browser/delivery qualification.


### Task64 separator-root provenance correction candidate

- Correct the reviewed separator-ending root branch: exact-root scalars consume
  the separator; descendants retain the canonical slash and relative tail after
  the logical token. Preserve the ordinary-root pattern and runtime YAML.
- Add six whole-function exact-root/descendant quote regressions, retaining the
  rejected implementation's three descendant failures and passing root controls.
- Fresh70 focused tests pass; complete provenance coverage is92.5%. The other12
  unchanged-source coverage gates and601/56 suites remain dated Task61 evidence.
  New full checks await storage/release; independent review and all later site,
  commit, browser and delivery gates remain open.


- Complete current source validation:607 Python tests,56 Node tests and all13
  whole-module gates pass; minimum combined coverage81.8182%, provenance92.5%.
  Preserve one inherited SyntaxWarning and ten inherited Lunr notices.
- Correct the validation harness PATH to expose the existing properdocs
  entrypoint; retain the first failed attempt and clock-measurement erratum.
  Product tests and oracles are unchanged.
- Keep this source-only qualification separate from a new site/build pair,
  native behavior, main integration and publication, which remain unqualified.

## 2026-11-10 — integration-round guidance

Require independent verification, fresh upstream/team reconciliation and normal nonforce integration after important rounds. Move only verified solved TODO scope into cumulative history, update remaining plans and continue authorized work; existing preservation and admission holds remain unchanged.
