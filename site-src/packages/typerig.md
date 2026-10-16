---
this_file: site-src/packages/typerig.md
---
# TypeRig

TypeRig is Vassil Kateliev's font-development library: outline objects, points
and contours, interpolation and adaptive scaling, and proxies over FontLab's
objects. This package distributes the complete library; TypeRig's GUI scripts,
panels and toolbars stay in [kateliev/TypeRig](https://github.com/kateliev/TypeRig).

## Install

```sh
python -m pip install typerig
```

The core needs no FontLab. Install it into FontLab's Python folder as well to use
the FontLab proxies; see [Install into FontLab](index.md#install-into-fontlab).

## Quick start

```python
from typerig.core.objects.point import Point

point = Point(10, 20) + Point(2, 3)
print(point.x, point.y)        # 12.0 23.0
```

## Examples

Inside FontLab, use the proxy layer on the current glyph:

```python
from typerig.proxy.fl.objects.glyph import eGlyph

glyph = eGlyph()               # wraps the current glyph
print(glyph.name, glyph.getBounds())
```

## Limits

- Proxy modules need their host API (FontLab, or Glyphs for the Glyphs proxies).
- Licence: Mozilla Public License 2.0 (upstream TypeRig).

Reference: [typerig](../reference/typerig.md).
