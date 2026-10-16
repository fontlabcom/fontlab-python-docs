---
this_file: site-src/packages/fly.md
---
# Fly

Fly gives the FontLab Python ecosystem nine short, lazy import aliases. Each
alias is the exact original module object, not a copy or wrapper.

| Alias | Module |
| --- | --- |
| `fl` | `echopy.fontlab` |
| `fg` | `echopy.fontgate` |
| `pr` | `echopy.fontpr` |
| `qt` | `PythonQt` |
| `tr` | `typerig` |
| `ap` | `fontlabapp` |
| `qs` | `pythonqtside` |
| `gp` | `fontlab_glyport` |
| `fp` | `fontlab_fontport` |

## Install

Install `fontlab-fly` with its target packages (Echopy, TypeRig, Fontlabapp,
Pythonqtside, Glyport, Fontport) into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab).

## Quick start

```python
# Inside FontLab
from fly import fl, fg, qt, gp, fp

font = fl.CurrentFont()                 # same function as fontlab.CurrentFont
import fly.gp, fontlab_glyport
assert fly.gp is fontlab_glyport
```

## Examples

Child imports route to the canonical package:

```python
from fly.fp.pens import FontGatePointPen     # same object as fontlab_fontport.pens
from fly.tr.core.objects.point import Point
```

## Behaviour and limits

- Importing `fly` loads none of its targets; each alias loads on first access.
- `qt` needs FontLab's native PythonQt; outside FontLab it raises a clear
  `ModuleNotFoundError`. Missing target packages raise the same way.

Reference: [fly](../reference/fly.md).
