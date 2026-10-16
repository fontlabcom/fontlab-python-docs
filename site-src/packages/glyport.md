---
this_file: site-src/packages/glyport.md
---
# Glyport

Glyport runs Glyphs scripts and plugins inside FontLab. It inspects and adapts
the original source (including Glyphs 2 / Python 2 code), gives each run a live
`GlyphsApp` model backed by the FontLab font, and translates Vanilla, AppKit and
NIB/XIB interfaces to FontLab's Qt. Original files are never modified.

This page describes Glyport v1.0.2.

## Install

Install `fontlab-glyport` into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab). Its inspection API also
works outside FontLab.

## Quick start

Assess a script without running it:

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

```python
from fontlab_glyport import adapt_source

adapted = adapt_source("OldScript.py", profile="glyphs2", cache_dir=".glyport-cache")
code = adapted.compile()           # compiles; does not execute
print(adapted.translate(1, 1))     # generated position -> original position
```

## What is supported

- The `GlyphsApp` module for each run: `Glyphs`, the GS* model classes, callback
  events and dialogs ([GlyphsApp reference](../reference/GlyphsApp.md)).
- The seven Glyphs SDK plugin classes (`GeneralPlugin`, `FilterWithoutDialog`,
  `FilterWithDialog`, `ReporterPlugin`, `PalettePlugin`, `SelectTool`,
  `FileFormatPlugin`), registered as real FontLab menu actions, windows,
  export items and Glyph-window painters.
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
