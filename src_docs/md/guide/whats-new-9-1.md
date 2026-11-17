---
this_file: src_docs/md/guide/whats-new-9-1.md
---
# What's new in FontLab 9.1 for Python

FontLab 9.1 (build 9812) adds clipboard JSON exchange, live stroke parameters,
an inktrap length for smart corners, axis extrapolation and presentation
overrides for glyph cells. It also changes the FontGate brush: `fgBrush.size`
is gone.

!!! warning "Verification status"
    Verified live on 9.1.9812: every member on this page exists, `fgBrush.size`
    is gone, the clipboard JSON round trip works with a `QByteArray`, and
    passing Python `bytes` to `getObjectsFromJsonData` crashes FontLab. The
    behavior of the stroke, inktrap and presentation-override members is read
    from the FontLab 9.1 source and has not been checked in a running FontLab
    yet. The examples have not been run end to end. The API reference pages come from a FontLab 9.0 capture and
    do not list these members until Echopy ships a 9.1 capture.

Detect features with `hasattr`, not with the build number:

```python
from fontlab import flModelProducer, flShape

has_json = hasattr(flModelProducer, "getClipboardDataJson")
has_strokes = hasattr(flShape, "expandStroke")
```

Echopy records every change in `fontlab_echopy.api91`; `api91.detect()` returns
a name-to-bool map for the running host.

## Copy objects as JSON

`flModelProducer.getClipboardDataJson(package_id, upm, objects)` serializes
contours, shapes, layers or glyphs to FontLab clipboard JSON and returns a
`QByteArray`. It does not touch the system clipboard. Images are dropped and
component references stay unresolved.

`flModelProducer.getObjectsFromJsonData(data)` reads that JSON back and returns
a list of detached objects with fresh ids, or `None` when the data is malformed.

```python
import fontlab
from fontlab import flGlyph, flModelProducer, flPackage

font = flPackage(fontlab.CurrentFont())
glyph = flGlyph(fontlab.CurrentGlyph(), font)
layer = glyph.layers[0]

data = flModelProducer.getClipboardDataJson(font.id, font.upm, [layer])
print(data.data()[:80])          # read bytes with data()

objects = flModelProducer.getObjectsFromJsonData(data)   # pass the QByteArray
```

!!! danger "Never pass `bytes` to `getObjectsFromJsonData`"
    Pass the `QByteArray` that `getClipboardDataJson` returned, unchanged. On
    9.1.9812, passing a Python `bytes` object instead crashes FontLab (SIGBUS
    in the native QByteArray converter).

    If you only have bytes, for example read from a file, wrap them first.
    This route is also verified on 9.1.9812:

    ```python
    from PythonQt import QtCore

    objects = flModelProducer.getObjectsFromJsonData(QtCore.QByteArray(raw))
    ```

    Do not pass `bytes`, `bytearray` or `str`. Echopy's
    `api91.objects_from_json(data)` does the wrapping for you.

Two more PythonQt details:

- `bytes(qbytearray)` raises `TypeError` in FontLab's PythonQt. Use
  `qbytearray.data()`.
- Wrong arity raises `IndexError`; an unsupported object in the list raises
  `TypeError`.

The returned objects are not in any font and carry no history. Add them to a
layer yourself.

## Stroke parameters

`flShape.penParameters` reads and writes a shape's stroke as a plain Python
dict. On 9.1.9812 the getter returns string caps and join, not enums (verified
live, read only). A shape with no pen reads like this:

```python
{'cap0': 'butt', 'cap1': 'butt', 'join': 'miter', 'miter_limit': 2.0, 'thickness': 0.0}
```

Writing it is not verified live yet:

```python
shape = layer.shapes[0]
pen = shape.penParameters
pen.update(thickness=40, join=2, cap0="round", cap1="round")
shape.penParameters = pen          # the setter replaces the whole stroke
```

Keys: `thickness` (alias `width`), `join`, `miter_limit`, `proportion`,
`contrast`, `rotation`, `cap0`, `cap1`, `cap_offset0`, `cap_offset1`,
`cap_shaping0`, `cap_shaping1`, `cap_curvature0`, `cap_curvature1`,
`cap_rotation0`, `cap_rotation1`, `remove_overlap`, `tolerance`.

- The setter replaces everything: omitted keys revert to defaults. Read the
  dict, change it, then assign it back.
- `thickness` 0 removes the pen.
- The getter returns `join` as a string (`"miter"`, `"bevel"`, `"round"`).
  When writing, send `join` as an int (0 bevel, 1 round, 2 miter); see fl#8630.
  Caps read and take `"butt"`, `"round"` or `"square"`.
- The getter may omit keys you can set (the read above has five).
- A non-dict raises `TypeError`; a bad number raises `ValueError`.

`flShape.expandStroke(outer_only=False)` turns the stroke into outlines and
returns `True`, or `False` when the shape has no stroke.

```python
if shape.expandStroke():
    # Unverified: notifyGlyphUpdated is not yet confirmed as the right refresh.
    fontlab.flItems.notifyGlyphUpdated(font.id, glyph.id)   # see the note below
```

!!! note "No Undo, no notification"
    `getClipboardDataJson`, `getObjectsFromJsonData`, `penParameters` and
    `expandStroke` record no Undo step and send no change notification.
    Save a copy first and refresh the view yourself.

## Smart corners, axes and preferences

- `SmartCornerParameters.inktrap_len` (float, default 2.0). The parameters are
  a value: read `package.smartCornerParameters`, change the field, then assign
  it back.
- `flAxis.extrapolate` (bool, default `False`). When `True`, the UI allows
  values up to 25% beyond the axis range.
- `flPreferences.editorIndependentGlyphMasters` and
  `flPreferences.generalActivateFontWindowOnOpen` (bool).
- Font Info: `font.info.nametablePath` (str or `None`) and
  `font.info.otherData` (dict).

```python
params = package.smartCornerParameters
params.inktrap_len = 4.0
package.smartCornerParameters = params
```

## Presentation overrides

A glyph cell can show a different layer or design location without changing
the glyph.

- `flGlyphInfo.setActiveLayer(layer)`, `setLocation(location)` and
  `clearPresentationOverride()` return `bool`. Read-only: `activeLayer`,
  `isEditable`, `hasPresentationOverride`.
- `fgSymbol.setLayerOverride(name)`, `setLocation(location)` and
  `clearPresentationOverride()`. Read-only: `location`, `hasLocation`.

Do not call `fgSymbol()` without arguments. It segfaulted FontLab in earlier
builds, and its behavior on 9.1 is not verified. Use the proven constructor
signatures.

## FontGate brushes and caps

`fontgate.fgBrush` gains stroke members: `thickness`, `proportion` (0 to 1),
`contrast` (1.0 means none), `rotation`, `tolerance`, `remove_overlap`,
`join_type` (0 bevel, 1 round, 2 miter), `miter_limit`, `cap0` and `cap1`.
`cap0` and `cap1` return copies; assign them back after editing.

Defaults of a new `fgBrush()` on 9.1.9812 (verified live, read only):

| Member | Default |
| --- | --- |
| `thickness` | 1.0 |
| `proportion` | 0.5 |
| `contrast` | 1.0 |
| `rotation` | 0.0 |
| `tolerance` | 1.0 |
| `remove_overlap` | `False` |
| `join_type` | 2 (miter) |
| `miter_limit` | 3.0 |
| `cap0`, `cap1` | `fgCapParams(type=0, offset=0, shaping=0, rotation=0, curvature=0.554)` (butt) |

Note the different names: `fgBrush` uses `join_type` (int), while the
`flShape.penParameters` dict uses `join`.

!!! warning "Removed: `fgBrush.size`"
    `fgBrush.size` no longer exists in 9.1. Code that reads or writes it fails.
    Use `thickness` and the other stroke members.

`fontgate.fgCapParams(type=0, offset=0, shaping=0, rotation=0, curvature=0.554)`
describes a cap. Types: 0 butt, 1 square, 2 round, 3 horizontal, 4 vertical,
5 fixed. It has a copy constructor and `asDict()`.

`fgShape.makeStroke([cap0, cap1])` returns a new detached stroked `fgShape`, or
`None`. This and `flShape.expandStroke` are read from the source and not
verified live.

```python
from fontgate import fgBrush, fgCapParams

brush = fgBrush()
brush.thickness = 30
cap = brush.cap0
cap.type = 2                  # round
brush.cap0 = cap              # assign the copy back
```

## Not in 9.1.9812

A typed `flJson` API exists only on a development branch. It is not in 9.1.9812.
