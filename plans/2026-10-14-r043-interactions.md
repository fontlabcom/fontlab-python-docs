---
this_file: plans/2026-10-14-r043-interactions.md
---

# R043 interaction receipts on the built site

Spec: parent `issues/101.md` R043 ("Exercise deep links, type links, aliases and a
deliberately late/sharded search entry. Save screenshots and interaction receipts.
A strict build alone is not browser proof; a screenshot alone is not interaction
proof."). Already done: a11y checker 28/28 against the live theme (baf9077), theme
fixes published, sharded search accepted at c42ca1f.

## Global Constraints

- Repo `fontlab-python-docs`, branch `issue-101-ecosystem-docs`; read AGENTS.md,
  README.md, THEME.md. Tests: `UV_OFFLINE=true uv run --frozen python -m pytest -q`
  (focused files while iterating). Do NOT run `./build.sh` (165 s, 4.5 GB) and never
  `--refresh-native`; use the existing built site at `.build/site`.
- Playwright (Python, already a dependency used by scripts/a11y_check.py) against a
  local static server (reuse `serve_site` from scripts/a11y_check.py). Chromium only.
- Receipts are JSON written to a path passed on the command line; screenshots PNG
  next to it. No network beyond localhost; the fltheme26 CDN assets load normally.
- Keep the script small and plain; functions < ~30 lines; Python 3.11+.

## Task 1: Interaction acceptance script and fixtures

Create `scripts/interaction_check.py` with a CLI `--site PATH --out RECEIPT.json`
that, at 1280x800 and 375x812 in light and dark:
1. Deep links: open a reference page with a member fragment (e.g.
   `reference/fontlab/flNode.html#<member anchor>` — choose real anchors by
   reading the built HTML) and assert the target element exists and is scrolled
   into view (bounding box intersects viewport, not under the sticky header).
2. Type links: on a reference page, click a parameter/return-type cross-reference
   (autorefs link) and assert navigation lands on the target page and anchor.
3. Aliases: open an alias route recorded by the site (find alias pages/routes from
   the built site or route map, e.g. legacy/alias pages produced by
   `scripts/export_aliases.py`/`legacy_route_map.py`) and assert it resolves to the
   canonical target.
4. Late/sharded search: type a query whose result lives in a non-initial shard
   (choose by reading the search manifest/shards in `.build/site/search/`) with a
   simulated slow shard response (Playwright route delay ≥ 1.5 s on that shard
   file), assert the result appears after the delay, then Enter/click navigates to
   it in the same tab, and Back returns to the previous page.
5. Keyboard: Tab from page start reaches skip link, search, navigation (on mobile
   via the drawer opener and Enter, as scripts/a11y_check.py does) and the first
   content link; `/` or `s` focuses search if the theme supports it (record
   whether supported rather than failing).
Save one screenshot per case/viewport/scheme and a receipt with per-case pass/fail
and measurements. Add pytest tests using tiny local fixture pages (like
tests/fixtures/a11y) proving each check can pass and fail. Run the script against
`.build/site`, store the receipt and screenshots under the parent workspace
`verification/issue-101-ecosystem/evidence/r043-interactions/` (create it), and
inspect a few screenshots. WORK.md entry with exact commands/results; do not tick
TODO.md; commit.
