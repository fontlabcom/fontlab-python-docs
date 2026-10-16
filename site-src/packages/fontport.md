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

Stage font information and apply it in one validated batch:

```python
font.info.apply({"familyName": "My Family", "ascender": 810.5},
                undo_name="Edit font information")
```

## Behaviour and limits (Fontport v1.0.1)

- **Undo:** an edit through the live binding is undone by the first Edit > Undo.
  FontLab records one extra, empty Undo row with it (exact one-row Undo is the
  unsupported capability `glyph.exactSingleUndo`; information batches likewise
  report `info.exactSingleUndo`).
- **Font information:** metrics (`ascender`, `descender`, `capHeight`, `xHeight`,
  `italicAngle`), `styleName` and `note` are written to the current key master
  only; family name, version fields, copyright and units per em are stored on the
  font. Supported fields: `familyName`, `styleName`, `unitsPerEm`, `ascender`,
  `descender`, `capHeight`, `xHeight`, `italicAngle`, `versionMajor`, `versionMinor`,
  `note` and `copyright`. OpenType name records are refused, since FontLab does not
  persist them through this route.
- **Default and strict modes:** the v1.0.0 editing contract is the default. Stricter
  guarantees are opt-in: `require_single_undo=True` on `font.info.apply` and
  `require_persistence=True` on group and save operations refuse instead of
  accepting the extra Undo row or a legacy group mode.
- **Named refusals:** layer create, delete and rename; glyph rename; guidelines and
  images; hinted outlines; fractional anchors and kerning; non-ASCII names for new
  glyphs and groups; multi-layer UFO import; world selection. Each raises
  `UnsupportedCapability` with its name before anything is written.
- `font.capabilities()` lists every capability with its evidence. Edits made in
  FontLab itself do not notify the binding: call `font.refresh()` and reacquire
  glyph and layer handles afterwards.
- FontParts coverage (FontParts 1.1.1 upstream tests, host-free backend run):
  1,748 of 1,797 pass, 48 raise a named `UnsupportedCapability`, one is skipped
  upstream, none fail unclassified. These are not FontLab-native passes.
- An unexpected FontLab error during the final write can leave partial changes;
  develop on a copy of your font.

Reference: [fontlab_fontport](../reference/fontlab_fontport.md). Licence:
Apache 2.0.
