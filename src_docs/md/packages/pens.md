---
this_file: src_docs/md/packages/pens.md
---
# Pens

Pens implements the fontTools Pen and PointPen protocol for FontLab 9 with no
runtime dependencies. For the selected APIs it keeps the class and function names
of `fontTools.pens`, so protocol-compatible code draws, measures, transforms and
reverses outlines without installing fontTools. It is not the complete fontTools
pen set. Fontport builds its FontGate point pens on it.

## Install

Pens is not on a package index. Install a tagged release from GitHub, or open
`install.vfpy` from a checkout in FontLab and restart; see
[Install into FontLab](index.md#install-into-fontlab). It needs Python 3.11 or
later. Importing `fontlab_pens` is safe outside FontLab: the native pens load
`fontgate` and `fontlab` lazily.

## Quick start

```python
from fontlab_pens import BoundsPen, RecordingPen, TransformPen

rec = RecordingPen()
pen = TransformPen(rec, (2, 0, 0, 2, 10, 0))
pen.moveTo((0, 0))
pen.curveTo((0, 50), (50, 100), (100, 100))
pen.closePath()
print(rec.value)
```

## Limits

- Native pens must target an explicit layer or element, never a glyph.
- Only the selected fontTools pen APIs are implemented; see the API reference.

See the [Pens API reference](../reference/fontlab_pens.md).
