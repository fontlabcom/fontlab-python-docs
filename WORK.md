---
this_file: WORK.md
---

# Work in progress

## 2026-11-17 — Public download links and release boundaries

Standalone installation links now use the canonical public installer asset.
The temporary App/Plugmix wheel example retains its checked versions and PyPI
publisher warning without embedding direct repository download URLs. Privacy
oracles, disposition rules, frozen inputs and API source locks are unchanged.
Independent 1.0.10 release review verifies the canonical installer download:
HTTP 200, 7143 bytes, SHA256
5e7b64584ddfef9e276add3d465343c641b91c29840db34967735d4d00ab643e.
This is HTTP-byte acceptance, not installer execution or API-site publication.


## 2026-11-17 — Instamix installation guide source update

Added an Instamix package guide and navigation entry; updated installation,
package boundaries and the App/Plugmix version relationship. The guide requires
Instamix 1.0.9 or newer before legacy upgrades, explains failed-upgrade recovery,
explicit data/target facts, extension identity, shared venv behavior and timeout
outcomes. It distinguishes checked GitHub releases from the App/Remopy/Plugmix
PyPI publisher failures and records the 9.1.9813 native MCP bridge limitation.

Baseline affected-source tests: 11 passed. Final complete Python source suite: 625 passed, 2 existing skips (200.47 seconds). Search backend: 27 passed (458.50 milliseconds). Printed
manifest/CLI/Python examples and the book project/draft fixtures pass against
an ordinary corrected candidate wheel.

The controller provisioned the exact approved packet SHA256
b2cb1eb27a359913d8b90d573105deee1a00c8bf4d29cee43bb37f08b4e7a703 from pinned
store cff3cbcd531df18e1588e5b2572c5b8edf05b222. The API source lock is unchanged.
Normal build and offline consumer acceptance pass: 9,883 generated files
including provenance; the complete-index browser gate covers 90,308 rows and
passes in 11.40 seconds. The final raw privacy audit exits 1 with exactly three
approved private-name findings and zero private URLs; the existing disposition
exits 0. No privacy oracle or input lock was changed.

Independent rendered review passes for the bounded API/Book guide scope: five
pages and 46 internal links, with no missing files or anchors. Initial missing-
Echopy/provider build failures are superseded by this matched-input evidence.
The generated review candidate remains local. Deliver the eleven source files
through normal CI: verify source commit X, generated commit Y, exact-SHA Actions
and live Pages separately. Native installation and connection remain unverified.

## 2026-11-14 — Functional work order documented

Updated AGENTS, PLAN and TODO to prioritize useful functional changes and compatible package boundaries, with detailed testing deferred. Existing backlog and prior records are retained. Documentation preservation and policy consistency were checked; no runtime, installed or native checks ran in this documentation-only pass.

Next: reconcile the pending Aidus provider/source-lock rename and current App/Plugmix/Fly teaching with focused affected-page checks before the full rendering/search/browser pass.

Earlier WORK.md (181,813 bytes, SHA256 `2ecde40cf56b84b1a214ae5ecb8d561c4df5b0ef6a2cd0cbda38b6469393ccc8`) is archived on the owner's workspace data volume (not public) under `issue250/work-archives/` (Issue 250). Completed work is in CHANGELOG.md; open work is in TODO.md and PLAN.md.
