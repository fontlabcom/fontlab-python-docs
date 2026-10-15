---
this_file: site-src/guide/glyphs.md
---
# Glyphs compatibility

`GlyphsApp` scripts and plugins are the target of this compatibility layer.

The [`GlyphsApp` reference](../reference/GlyphsApp.md) lists the module that
glyport gives each Glyphs script: `Glyphs`, callback events, dialogs and the GS*
model classes.

Glyport owns the Glyphs-to-FontLab model, script/plugin execution and dynamic
Vanilla/AppKit/NIB/XIB-to-Qt translation. Current implementation provides
read-only inspection of original scripts and plugin bundles.

```python
from fontlab_glyport import inspect_source

assessment = inspect_source("OriginalScript.py")
print(assessment.required_capabilities)
```

Inspection records hashes, imports, protocol declarations, resources and
limitations. It does not execute or modify source, and does not establish native
compatibility. Profiles are `auto`, `glyphs2`, `glyphs3`, and `glyphs4`; auto
detection currently remains unresolved.

The supplied corpus includes Python, native-only bundles, binary/bytecode
dependencies, drawing and GUI resources. Native runtime, all seven plugin
protocols, automatic source adaptation and dynamic GUI translation remain
required implementation work. Unsupported required cases retain explicit
unexecuted/failed/blocked outcomes.

The eventual `run_script()` and `install_plugin()` interfaces are specification
contracts. They are not shipped runtime functions in the current inspection
foundation. All compatibility code belongs to the independent Glyport repository.
