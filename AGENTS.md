---
this_file: AGENTS.md
---

## Current scope — 2026-11-05

Issue 230 documentation reconciliation is current. Issue 123 remains paused. The qualified Issue 207 isolated candidate is separate from canonical source, installed artifacts, native acceptance and publication. Reconcile that candidate with later work before integration. Issue 210 specifies future architecture; Issue 211 retains unfinished follow-up checks. Retained dated receipts describe their original source and acceptance surface only.

Canonical source inspected for this proposal: `a07ffa5c1258`. This is a dated source observation, not an installed or native acceptance claim.

Reconcile Issue 207 provider/source-lock and generated documentation with current App/Plugmix APIs. Complete the source/export and artifact tuple before intentional lock refresh.

Qualify strict rendering, every provider, complete search, archive routes, browser accessibility and licences; owner installation, native capture and publication need their own evidence.

## Organization and checks

`src_docs/` contains authored pages/configuration; `scripts/` builds and checks the site; `tests/` checks contracts; `api-sources.lock.json` pins inputs; `docs/` is generated output; `archive/` preserves old documentation.

Use Python 3.12+, Node 22+ and `uv sync --locked --group dev`. Provision Playwright Chromium and the matching approved Echopy/source tuple. Run `uv run --group dev --with-editable ../fontlab-echopy python -B -m pytest -q -p no:cacheprovider tests` for Python source tests; run the separate Node lane below. After source/export provisioning, `./scripts/accept-consumer.sh --offline` runs the build/consumer gate. `./build.sh --check` checks the accepted baseline; ordinary builds can update `docs/`.

<!-- this_file: AGENTS.md -->

# fontlab-python-docs: agent guidance

<!-- shared-theme-integration:start -->
## Shared theme maintenance

Read [THEME.md](THEME.md) before changing shared chrome, MaterialX configuration
or component assets. This repository’s role is: python and pythonqt api reference.
Shared browser behavior belongs in `fontlab-www-docstheme`; FontLab global menu
source belongs in `img/docs/menu/fontlab.js`, Vexy menu source in
`i.vexy.art/docs/menu/vexy.js`. Keep per-site content, branding and native builds here.
Preserve one menu and one search control, documented ownership defaults, scoped
`.fltheme-components` styles and `du-` component prefixes. Verify final generated
HTML after overlays; a source-only change is not proof of a live deployment.
Do not commit unrelated local edits or hand-edit generated CSS as the source fix.
Work directly unless the current user explicitly requests delegation.
<!-- shared-theme-integration:end -->

## Milestones and delivery

Read [PLAN.md](PLAN.md), [TODO.md](TODO.md) and [WORK.md](WORK.md) before work.
Make the smallest complete MVP for one named acceptance task. Find all callers,
tests, fixtures, exports and documentation first. Use graph impact before source
symbol edits; confirm stale or unknown graph results against current source.
Keep product work in isolated successors and preserve the owner's checkout.

Run this repository's exact checks and the unchanged 80% gate for each complete
changed production module. Use an independent review before a milestone commit.
Under the current owner task, commit and push reviewed, passing milestones;
verify remote heads rather than inferring delivery from local tracking refs.
Before main integration, reconcile concurrent work and all consumers, run graph
change analysis and repeat the required acceptance on the combined source.

Before removing obsolete branches or files, prove integration, retain recoverable
unique work and check fresh owner/worktree attachments. Preserve sealed reports,
licences, archives and private data. Do not rewrite history by implication.
Remove verified completed work from PLAN/TODO and record scoped evidence in
CHANGELOG. Keep implemented-only native/artifact checks open in TODO. Issue 123
remains paused; no instruction here authorizes driving the owner's FontLab,
installing into its user folder or publishing a site.

## Search backend development lane

Use Node22+ for this documentation site. Run `node --test scripts/search_backend/tests.cjs` separately from Python pytest. If handwritten backend source changes, follow README's locked compiler setup with esbuild0.25.12 and `node scripts/search_backend/compile.cjs`; commit the rebuilt bundle and its hashes together. Ordinary builds consume the committed bundle. Offline recompilation needs the provisioned npm cache. Browser/search, source-lock, archive and publication checks remain separate.

## Integration rounds

After each important round, independently verify the result, refresh the actual upstream main (or existing default branch), and reconcile concurrent team work in an isolated successor. Integrate qualified changes upstream through normal gates without force-pushing. Move only verified solved TODO items to cumulative CHANGELOG, update PLAN for remaining work, and continue the authorized backlog. Existing preservation rules, exclusions, pauses, native/install restrictions, private P/L holds and capability gates remain in force.
