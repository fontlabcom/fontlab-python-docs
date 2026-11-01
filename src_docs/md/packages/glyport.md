---
this_file: src_docs/md/packages/glyport.md
---
# Glyport

Glyport runs Glyphs scripts and plugins inside FontLab. It inspects and adapts
the original source (including Glyphs 2 / Python 2 code), gives each run a live
`GlyphsApp` model backed by the FontLab font, and translates Vanilla, AppKit and
NIB/XIB interfaces to FontLab's Qt. Original files are never modified.

The detached-transform examples below were checked with the ordinary development
artifact `1.0.8.dev58+g753b55548` and App `0.2.26.dev159+gb1e905b61`. They do not
claim a published release or qualify native FontLab behavior. Older packages may
not have the same input checks or overflow preflight.

## Install

Install `fontlab-glyport` into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab). Its inspection API also
works outside FontLab.

## Quick start

Assess a script without running it:

<!-- example: glyport-inspect -->
```python
from fontlab_glyport import inspect_source

assessment = inspect_source("OriginalScript.py")
print(assessment.required_capabilities)
```

Run a Glyphs script inside FontLab:

```python
# Inside FontLab
from fontlab_glyport import run_script

handle = run_script("OriginalScript.py")      # profile chosen from the source
print(handle.state, handle.receipt)
handle.close()
```

## Examples

Install a plugin bundle and remove it again:

```python
from fontlab_glyport import install_plugin

plugin = install_plugin("MyReporter.glyphsReporter")
# ... the reporter now draws in the Glyph window ...
plugin.unload()                                # removes every registration
```

Adapt Glyphs 2 source into an owned cache, keeping a map back to original lines:

<!-- example: glyport-adapt -->
```python
from fontlab_glyport import adapt_source

adapted = adapt_source("OldScript.py", profile="glyphs2", cache_dir=".glyport-cache")
code = adapted.compile()           # compiles; does not execute
print(adapted.translate(1, 1))     # generated position -> original position
```

## Work with detached geometry

These examples run outside FontLab. They create Python-owned draft objects and
change no open font. They demonstrate Glyport's arithmetic and object semantics;
they do not test copying a native layer, native rounding, Undo or saved fonts.

### Apply one affine matrix

The six values `(a, b, c, d, tx, ty)` map a point as
`x_new = a*x + c*y + tx`, `y_new = b*x + d*y + ty`. This example changes a path
and an anchor on an owned detached layer. It does not resolve components or
measure a native layer's bounds.

<!-- example: glyport-detached-transform -->
```python
from fontlab_glyport.model import GSAnchor, GSNode, GSPath
from fontlab_glyport.model.copies import DetachedLayer

layer = DetachedLayer()
layer.paths = [GSPath([GSNode((2, 3)), GSNode((-4, 5))])]
layer.anchors = [GSAnchor("top", (11, 19))]
layer.applyTransform((2, 1, 3, 4, 5, 6))

assert [tuple(node.position) for node in layer.paths[0].nodes] == [
    (18, 20), (12, 22)
]
assert tuple(layer.anchors[0].position) == (84, 93)
```

Composition order matters. A clockwise rotation followed by one combined
scale/shear matrix differs from scale, then shear, then counterclockwise rotation.
Do not use a similarly named menu as proof that two scripts implement the same
transform, layer scope or component policy.

### Reject invalid coefficients and overflow before writing

Layer/path transform entry points reject NaN and infinity before backend calls,
history or geometry mutation. Finite zero and negative scales retain their
existing behavior; this check does not forbid flattening or reflecting geometry.

<!-- example: glyport-nonfinite-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

path = GSPath([GSNode((2, 3))])
before = [tuple(node.position) for node in path.nodes]
try:
    path.applyTransform((float("nan"), 0, 0, 1, 0, 0))
except ValueError as error:
    print(error)
else:
    raise AssertionError("The non-finite matrix should be refused.")
assert [tuple(node.position) for node in path.nodes] == before
```

Finite coefficients can still overflow when multiplied by a large coordinate.
Python-managed paths, detached layers and selection-aware layer transforms
calculate all results before entering history or writing. A failure on a later
point therefore leaves earlier points untouched:

<!-- example: glyport-overflow-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

path = GSPath([GSNode((2, 3)), GSNode((1e308, 5))])
before = [tuple(node.position) for node in path.nodes]
try:
    path.applyTransform((2, 0, 0, 2, 13, -7))
except ValueError as error:
    print(error)
else:
    raise AssertionError("The overflowing result should be refused.")
assert [tuple(node.position) for node in path.nodes] == before
```

This is arithmetic preflight, not a transaction. Setter failures after preflight,
native coordinate conversion, and the native whole-layer transform remain outside
that guarantee. The native layer route calls FontLab's `flLayer.applyTransform`;
it must not be assumed to preserve metrics and guides like the detached example.

### Repeated objects are transformed per occurrence

The following deliberate alias illustrates draft-object identity. It is not a
recommendation to create duplicate nodes in a font. Each occurrence uses the
previous virtual result, so two factors of two give a factor of four. If a later
occurrence overflows, preflight refuses the operation before the first write.

<!-- example: glyport-repeated-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

node = GSNode((2, 3))
path = GSPath([node, node])
path.applyTransform((2, 0, 0, 2, 0, 0))
assert tuple(node.position) == (8, 12)
```

This identity rule covers the same draft object and ordinary cached live proxies.
It does not prove equivalent behavior for distinct wrappers sharing external
storage. A script that repeats a parent glyph may also need to recompute each
layer's bounds between visits; repeatedly applying one fixed matrix is not a
substitute for that workflow.

## What is supported

- The `GlyphsApp` module for each run: `Glyphs`, the GS* model classes, callback
  events and dialogs ([GlyphsApp reference](../reference/GlyphsApp.md)).
- The seven Glyphs SDK plugin classes (`GeneralPlugin`, `FilterWithoutDialog`,
  `FilterWithDialog`, `ReporterPlugin`, `PalettePlugin`, `SelectTool`,
  `FileFormatPlugin`), registered as real FontLab menu actions, windows,
  export items and Glyph-window painters where supported. `SelectTool` is
  explicitly blocked, as noted below.
- Vanilla controls and dialogs, Qt-backed AppKit classes, NSBezierPath drawing and
  NIB/XIB interface loading ([vanilla](../reference/vanilla.md),
  [AppKit](../reference/AppKit.md)).

## Limits

- Compatibility is partial and still being extended; each run records a receipt
  with the outcome, and unsupported features raise `UnsupportedCapability` at the
  script line instead of failing silently.
- FontLab host limits block `SelectTool` and drawing before FontLab's own glyph
  layer; plugins that need them are reported as blocked.
- Bundles that ship only compiled macOS code cannot run.
- Creating glyphs makes FontLab rebuild auto-layer composites. Glyport restores
  existing composites afterwards and refuses with a named reason when it cannot.
  A FontLab defect can still drop component locks and attaching anchors on
  composites it rebuilds.
- Edits on auto layers (outlines, anchors, guides, hints, width, background) are
  refused before anything changes: telling FontLab about an auto-layer edit
  makes it rebuild every auto layer in the font.
- Test with a copy of your font: scripts can change the font they run on.

See the [Glyphs compatibility guide](../guide/glyphs.md). Reference:
[fontlab_glyport](../reference/fontlab_glyport.md).
