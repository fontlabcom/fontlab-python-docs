# this_file: scripts/lunr_patch.py
"""Fix lunr 2.3.9's TokenSet key in the stock MaterialX search worker after a build.

lunr keys TokenSet nodes as label + id with no terminator, so a digit label next to
an id collides ("1"+234 equals "1"+2, "3"+4) and minimisation merges distinct nodes.
Large indexes then lose words and Index.query throws, so the stock worker found
nothing for "fontlab" over the full index (issue 106, final-6). The complete-search
bundles get the same fix at compile time (scripts/search_backend/compile.cjs).
"""

from pathlib import Path

UNPATCHED = "e=e+s+o.id}"
PATCHED = 'e=e+s+o.id+";"}'


def patch_stock_worker(site: Path) -> Path:
    """Rewrite the key in the one stock worker; fail unless it matches exactly once."""
    workers = sorted((Path(site) / "assets/javascripts/workers").glob("search.*.min.js"))
    if len(workers) != 1:
        raise ValueError(f"Expected one stock search worker, found {len(workers)}")
    source = workers[0].read_text(encoding="utf-8")
    if source.count(UNPATCHED) != 1 or PATCHED in source:
        raise ValueError("lunr TokenSet key patch must match exactly once")
    workers[0].write_text(source.replace(UNPATCHED, PATCHED), encoding="utf-8")
    return workers[0]
