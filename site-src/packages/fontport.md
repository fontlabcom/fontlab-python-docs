---
this_file: site-src/packages/fontport.md
---
# Fontport

Fontport connects FontLab 9 to the Python font libraries most tools are built on:
FontParts, fontTools and fontPens pens, and ufoLib2. It provides point pens over
native FontGate glyphs, detached FontParts and UFO snapshots, and live FontParts
objects bound to an open FontLab document.

## Install

Install `fontlab-fontport` with fontTools, fontPens, FontParts and ufoLib2 into
FontLab's Python folder; see [Install into FontLab](index.md#install-into-fontlab).
Importing the package outside FontLab is safe; native access loads on demand.

## Quick start

Draw into a native glyph with a fontTools pen:

```python
# Inside FontLab, with a glyph you own
from fontlab_fontport.pens import FontGatePointPen
from fontTools.pens.pointPen import SegmentToPointPen

pen = SegmentToPointPen(FontGatePointPen(glyph))
pen.moveTo((0, 0))
pen.lineTo((200, 0))
pen.lineTo((100, 300))
pen.closePath()
```

## Examples

Edit a detached FontParts copy, then write it back explicitly:

```python
from fontlab_fontport.transfer import to_fontparts, write_glyph

snapshot = to_fontparts(native_glyph)     # a real fontshell RGlyph
snapshot.width = 600
write_glyph(snapshot, target_glyph)       # explicit destination
```

Bind live FontParts objects to an open FontLab document:

```python
from fontlab_fontport.host import NativeFontBackend
from fontlab_fontport.live import RFont

font = RFont(NativeFontBackend(font_id))  # font_id: the document's FontLab id
font["A"].width = 600                     # updates the FontLab glyph
font.close()                              # detaches; the document stays open
```

## Limits

- Fontport is work in progress (issue 105): groups, kerning, features, font lib,
  layer operations and glyph undo are still being completed.
- UFO object identifiers, anchor colours, guidelines and images are refused
  explicitly rather than dropped.
- Develop with copies of fonts: a failure during the final write can leave
  partial changes until native transactions land.

Reference: [fontlab_fontport](../reference/fontlab_fontport.md). Licence:
Apache 2.0.
