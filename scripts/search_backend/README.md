---
this_file: scripts/search_backend/README.md
---
# Complete search backend

`build.cjs` reads the full qualified original index and extracts global postings
with the pinned MaterialX Search class. Python `scripts/search_shards.py` verifies
exact row/config reconstruction and the full coverage separately from browser
bootstrap. Page groups stay whole; each row shard is named by SHA256.

`validation.js` checks metadata counts, the canonical front-coded vocabulary (each term
keeps its shared-prefix length and suffix; decoded terms strictly sorted), canonical unsigned varints,
row ranges, byte lengths and hashes before readiness. `router.js` uses the exact
consumer transformation/parser, conservatively selecting all shards for complex
syntax. `query.js` hydrates complete matching rows and original parent articles,
retains the unchanged engine result fields, and merges optional suggestions.
Its raw byte cache is at most3MiB except a single oversize page group; it schedules
three responses at a time. `worker.js` keeps messages0/1/2/3 and aborts/suppresses
superseded work. A new query's shard fetches abort after 1.8 s; each consecutive Retry doubles
that deadline up to 30 s (`shardDeadline`). Failure/retry status uses a per-page BroadcastChannel; no deployed
test controls or Worker monkeypatches exist.

The page closes its UI channel on pagehide, then reopens/rebinds it on persisted
pageshow and requests the worker's current status. Retry is reconciled before it
is enabled; restoration does not force a reload. The original Lunr QueryParseError
returns the stock ordinary empty result rather than a transport-outage state.

All worker-owned assets are fetched explicitly as `.gz` files and decoded with
native `DecompressionStream("gzip")`, with compressed and expanded size bounds.
The original raw assets remain for offline verification and original-consumer
reconstruction. `initial_static_bytes` counts these actual gzip files plus raw
bootstrap/worker/UI bytes, independent of server HTTP compression policy.
`initial_gzip_bytes` separately models gzip for the other startup assets.

`cacheBytes` counts owned original byte buffers. `liveBytes` counts completed
response-buffer ownership (including cached buffers borrowed for a query), not
JSON objects/indexes, in-flight compression chunks, or expanded JavaScript heap.
`scheduledWindowBound` is the encoded raw-size bound of the selected three-shard
window, not an observed heap peak. Browser acceptance samples actual page/worker
heap separately. No query-time transfer is included in or hidden behind READY.

The current pinned English language/config is retained. Other languages fail
explicitly until their exact assets are vendored. Nontrivial supported pipelines
route all rows rather than guessing normalization. Scores/order vary with candidate
statistics; complete result sets and named target discovery are separately gated.
Fuzzy/internal/leading wildcard and prohibited-only queries can be slow.

Use the root README's compiler bootstrap commands. Ordinary builds use committed
`engine.cjs`, `router.cjs`, `query.cjs` and worker, checked against `bundles.json`,
without npm or the compiler. `compile.cjs` requires locked esbuild0.25.12 and
verifies every original source hash. `source-provenance.json` pins all13sources
from the installed MaterialX10.1.5 worker source map (SHA256
`780dccece24891aa19da6285715e2c7d0cd884237a87a3a9be6684823584921f`).
Original vendored sources remain byte-exact; their paths are recorded there instead
of adding headers that would alter them. Compiled bundles include both original
MIT attributions. Barrel files only supply source-map-omitted export modules.

Focused tests: `python -m pytest -q tests/test_search_shards.py tests/test_search_backend.py`
and `node --test scripts/search_backend/tests.cjs`. The full-corpus read-only
comparison command is `node tests/search_complete_consumer.cjs ORIGINAL_JSON
COMPLETE_DIRECTORY NAMED_QUERY_JSON REPORT_JSON`. It compares all named targets
and complete ordinary/required/prohibited/field/quoted/fuzzy/wildcard result sets.
The shipped-worker test in `tests/test_search_identities.py` reconstructs all
original rows after sharding, preserving an independent original-consumer gate.
