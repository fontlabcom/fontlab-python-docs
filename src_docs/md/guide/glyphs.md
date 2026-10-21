---
this_file: src_docs/md/guide/glyphs.md
---
# Glyphs compatibility

[Glyport](../packages/glyport.md) runs Glyphs scripts and plugins inside FontLab
9. Each run gets the `GlyphsApp` module a Glyphs script expects: `Glyphs`, the GS*
model classes over the FontLab font, callback events and dialogs, plus Vanilla,
AppKit and `objc` translated to FontLab's Qt. The
[`GlyphsApp` reference](../reference/GlyphsApp.md) lists every name.

## Assess before running

Inspection never executes or changes the source. It records file hashes, imports,
plugin protocols, resources and anything that needs a missing capability:

```python
from fontlab_glyport import inspect_source

assessment = inspect_source("OriginalScript.py")
print(assessment.required_capabilities)
```

## Run a script

```python
# Inside FontLab, on a copy of your font
from fontlab_glyport import run_script

handle = run_script("OriginalScript.py")
print(handle.state)
handle.close()
```

Profiles `glyphs2`, `glyphs3` and `glyphs4` are chosen from the source or bundle
metadata; pass `profile=` to choose one. Glyphs 2 (Python 2) source is adapted
into a cache first; tracebacks point at the original lines.

## Install a plugin

```python
from fontlab_glyport import install_plugin

plugin = install_plugin("MyFilter.glyphsFilter")
plugin.unload()
```

The seven SDK plugin classes register as real FontLab menu actions, tool windows,
export items and Glyph-window painters; `unload()` removes them all.

## What to expect

- Compatibility is partial and actively extended. Every run writes a receipt;
  a missing feature raises `UnsupportedCapability` at the script line.
- FontLab host limits block `SelectTool` and drawing before FontLab's own glyph
  layer. Bundles that contain only compiled macOS code cannot run.
- Run scripts on a copy of your font until you trust them.
