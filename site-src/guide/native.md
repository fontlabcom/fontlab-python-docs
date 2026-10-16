---
this_file: site-src/guide/native.md
---
# Native scripting

Inside FontLab, `echopy.fontlab` delegates to the original `fontlab` objects;
`echopy.fontgate` and `echopy.fontpr` follow the same contract.

```python
from echopy import fontlab as fl

font = fl.CurrentFont()
glyph = fl.CurrentGlyph()
node = fl.flNode(120, 340)
```

Use [flNode][fontlab.flNode] and the complete class member indexes to inspect
captured signatures and enriched documentation. `Any` and variadic arguments
mark incomplete native signature information. They are not permission to pass
arbitrary objects; confirm an uncertain operation against the running host.

The optional [fontlabpr](../reference/fontlabpr.md) module was absent from the
captured host. Its absence is recorded rather than represented by invented APIs.

## Short imports

Fly provides seven lazy module aliases:

| Alias | Target |
| --- | --- |
| `fly.fl` | `echopy.fontlab` |
| `fly.fg` | `echopy.fontgate` |
| `fly.tr` | `typerig` |
| `fly.pr` | `echopy.fontpr` |
| `fly.qt` | native `PythonQt` |
| `fly.ap` | `fontlabapp` |
| `fly.qs` | `pythonqtside` |

They share the canonical module objects. Documentation names use the live API's
natural namespaces, while source and enrichment hashes retain provenance.

Outside FontLab, native construction and operations fail with `NativeUnavailable`.
Documentation builds read source and stubs without invoking these operations.
