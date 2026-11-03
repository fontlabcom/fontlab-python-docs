---
this_file: src_docs/md/packages/fontport.md
---
# Fontport

Fontport connects FontLab 9 to FontParts, UFO and DesignSpace data, and to the
fontTools, fontPens and ufoLib2 libraries around them. It provides point pens over
native FontGate glyphs, detached FontParts and UFO snapshots, and live FontParts
objects bound to an open FontLab document.

!!! note "No user interface"
    Fontport has no UI (issue 201). Its Qt editors now live in
    [`fontlabapp.fontui`](fontlabapp.md#fontui-font-and-glyph-browsers-and-editors).

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

## UFO and DesignSpace

Fontport exports a whole FontLab font to UFO and DesignSpace, and opens UFO and
DesignSpace files as new FontLab documents.

Export a multi-master font as a `.designspace` plus one UFO per master:

```python
from fontlab_fontport.designspace_io import export_designspace

path, losses = export_designspace(backend, "/absolute/path/Family.designspace")
print(path)
print(*losses, sep="\n")          # what the export did not carry
```

`export_designspace(backend, destination, document=None)` reads the backend and
never changes it. Axes, master locations and instances come from the native
package unless you pass your own `DesignSpaceDocument`. Each master is written as
`<stem>-<master>.ufo` beside the `.designspace`, with its own outlines, anchors
and kerning. `write_designspace(font, document, destination, master_kerning)`
does the file writing for a font you already exported. Nothing is overwritten.

Open UFO and DesignSpace files through FontLab's native `open_font`:

```python
from fontlab_fontport.native_import import import_designspace, import_ufo_native

backend = import_designspace("/absolute/path/Family.designspace")
# or: import_ufo_native("/absolute/path/Master.ufo")  # one master
backend.close()                    # the result is an owned document
```

Both need absolute paths, a matching suffix and an existing file; FontLab
resolves the source UFOs of a designspace. Import converts nothing in Fontport.

**What an export loses.** The `losses` list names it: designspace rules, axis and
location labels, instances' generated UFOs (instances are listed only), and
per-master groups, info, lib and features, which come from the key master and are
shared by every master UFO. Brace layers are not exported. Kerning is the
exception: each master's own kerning is exported.

**Why Fontport does not use `fgFont.save("x.ufo")`.** The native UFO save is
lossy. In a measured case it wrote the current master only (a three-master font gave
one layer), no `kerning.plist`, and no anchors. The MCP `save_font` tool writes
only VFJ, VFC and VFJP. Fontport's own exporter reads every master, so it keeps
all masters, kerning and anchors. Use VFJ when you need a lossless native archive.
See `docs/UFO-INTERCHANGE.md` in the Fontport repository for the full table.

## The editors moved to Fontlabapp

The six FontParts-bound Qt editors (`font_info_editor`, `groups_editor`,
`kerning_editor`, `transform_editor`, `batch_panel` and `glyph_sequence`) live in
`fontlabapp.fontui`. They call Fontport lazily; install both with the
`fontport` extra:

```sh
pip install "fontlab-fontlabapp[fontport]"
```

```python
# old (removed): from fontlab_fontport.ui import font_info_editor
from fontlabapp.fontui import font_info_editor
```

`fontlab_fontport.ui` remains for one release as a tombstone: reading any name
from it raises `ImportError("fontlab_fontport.ui moved to fontlabapp.fontui")`.
The batch panel still starts a separate Python 3.11+ process that needs
`fontlab-fontport`. Vanilla support moved to `fontlab_glyport.ui.session`.

Fontport also reads and writes feature blocks (`fontlab_fontport.feature_blocks`:
`read_feature_blocks` and `write_feature_blocks`), which need the original font
to be active and compare the source snapshot before writing.

## Behaviour and limits (Fontport v1.0.2)

- **Undo:** an edit through the live binding is undone by the first Edit > Undo.
  FontLab records one extra, empty Undo row with it (exact one-row Undo is the
  unsupported capability `glyph.exactSingleUndo`; information batches likewise
  report `info.exactSingleUndo`).
- **Font information:** metrics (`ascender`, `descender`, `capHeight`, `xHeight`,
  `italicAngle`), `styleName` and `note` are written to the current key master
  only; family name, version fields, copyright and units per em are stored on the
  font. Supported fields: `familyName`, `styleName`, `unitsPerEm`, `ascender`,
  `descender`, `capHeight`, `xHeight`, `italicAngle`, `versionMajor`, `versionMinor`,
  `note` and `copyright`. The structured fields `openTypeOS2Panose`,
  `openTypeOS2WeightClass`, `openTypeOS2WidthClass`, `postscriptStemSnapH` and
  `postscriptStemSnapV` are also written to the key master only. OpenType name
  records are refused, since FontLab does not persist them through this route.
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
