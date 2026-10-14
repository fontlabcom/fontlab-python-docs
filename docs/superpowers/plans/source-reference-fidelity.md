---
this_file: docs/superpowers/plans/source-reference-fidelity.md
---
# Source reference fidelity

Authority: issues/101.md complete source-derived reference/aliases/manifests and
the user's beautiful enriched-source/native-namespace documentation requirement.
Current runner refresh exposes concrete gaps; green coverage only checks currently
enumerated symbols. This task does not replace other site/deployment acceptance.

## Global Constraints

- Extract from source; never import FontLab/PythonQt/native packages during builds.
- Preserve every current source declaration, original/canonical/native identity,
  body-sharing relationship and provenance; do not invent native APIs.
- Native fontlab/fontgate/fontpr/PythonQt public documentation names stay primary.
- Every consumed source input must be pinned; silent producer drift is a failure.
- Keep historical docs/ unchanged; output the current site only under .build/site.
- No private paths/prompts/credentials in public output, no tag/push/deployment.
- Work on issue-101-ecosystem-docs, preserve others' work and .DS_Store.
- Every source/document has this_file; rtk proxy commands; no subagents in workers.

## Task 1: Complete consumed inputs, exported members and property semantics

Own scripts/api_inventory.py, export_aliases.py, source_lock.py,
reference_pages.py/build_reference.py only if required, their focused tests and
progress documentation. No package producer/recovery source changes. Root owns
this plan, actual full builds/native/browser acceptance and source-lock refresh.

Read current scripts/README/WORK/PLAN/TODO and existing tests. Observed gaps:
1. api_inventory parses private modules for aliases but excludes their bytes from
   input locking when they do not expose a selected public target. _app_native.py
   is one actual consumed input absent from api-sources.lock.json. Pin all actually
   consumed files exactly once regardless of emitted declaration visibility.
2. pythonqtside.AppHandle maps to pythonqtside._app.AppHandle, but public member
   alias pythonqtside.AppHandle.close is absent. Expand provable class/module
   aliases to their real exposed descendants, preserving canonical body targets,
   source records, complete alias inventory and accurate source-only visibility.
   Handle chains/cycles without inventing unsupported dynamic native members.
3. AppHandle page title exposes pythonqtside._app.AppHandle despite its public
   package export. Prefer the declared public package export for authored private
   implementation classes; preserve stable URLs/canonical links and native names.
4. @property namespace/reports/identity_report currently appear as functions in
   the AST member index. Respect source decorator/property semantics consistently
   with source-only Griffe, including getter/setter declaration accounting. Keep
   all occurrence/provenance/body identities; do not lose declarations.

Use current official Griffe/mkdocstrings docs and installed dependency source if
changing their APIs; do not assume handler schemas. Build minimal focused fixture
tests first for private input drift/addition/removal, public descendant/chained
aliases, preserved native identities/canonical bodies, public display titles,
property getter/setter accounting and deterministic source-only output. Follow
existing architecture, avoid new dependencies unless necessary. Run covering and
existing relevant tests, scoped lint/diff checks, record exact results. Commit
owned files only; no push or publication. Write full report to named task report.

## Task 2: Complete source/render verification

Root refreshes the input lock explicitly, performs full strict offline build and
locked check, audits complete inventory/source/body/alias anchors and consumed
inputs, and verifies public AppHandle/run_app/close searches plus native browser
regressions and actual method bodies. Independent task review/fix loop is required.
Retain all broader complete-site/legacy/serve/refresh/artifact-mode/license/CI/live
deployment requirements; none are completed by a selected reference page.
