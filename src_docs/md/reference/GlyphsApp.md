---
this_file: src_docs/md/reference/GlyphsApp.md
---

# GlyphsApp

Glyport constructs a `GlyphsApp` module for each adapted Glyphs script. Its
`Glyphs` object belongs to that script's FontLab context. Use the
[Glyphs scripting guide](../guide/glyphs.md) for the supported script entry point
and the [Glyport guide](../packages/glyport.md) for installation and adaptation.

The source-backed
[`fontlab_glyport.glyphsapp` reference](fontlab_glyport/glyphsapp.md) documents
`make_glyphsapp_module`, the factory that assembles this runtime namespace.
The constructed `GlyphsApp` module and the importable helper namespace
`fontlab_glyport.glyphsapp` have distinct roles: the former exposes the
per-script compatibility API; the latter provides its factory and supporting
functions. Runtime exports depend on the supplied script context and bridges.

This page preserves the `reference/GlyphsApp.html` entry point. Source-derived
factory documentation does not establish native FontLab workflow acceptance.
