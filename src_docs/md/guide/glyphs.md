---
this_file: src_docs/md/guide/glyphs.md
---

# Glyphs compatibility

Use [sidebar trees and document metadata](glyport-sidebar.md) to experiment with
current visibility, row identity, resource order, delayed counts and local URL
loading. The guide states each owned primitive and the remaining native gaps.


The numerical ordinary-artifact results below identify their retained predecessor
checkpoint. The [current manager/profile guide](glyport-managers.md) documents
the H source changes. Earlier source assumptions are corrected below; original
preimages remain in verification evidence. Old receipts do not qualify the new
ordinary tuple or native behavior.

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

## Ordered parameters and Arabic encodings

The private candidate's [parameter and Arabic guide](glyport-parameters.md) explains
first-active duplicate selection, live object edits, master/userData isolation and
explicit encoding refresh. Its self-contained examples use owned offline models.
Typed macOS string conversion, stored-script ordering and remaining ROS/native
limits are documented separately from running an original script in FontLab.

The [legacy Unicode and ROS guide](glyport-metadata.md) distinguishes primary
from legacy encodings, canonical aliases, active-font isolation and independent
read-only snapshots. It also explains the exact ROS text boundary and explicit
refusal before writes when a proprietary mapping is required. Full ROS mapping
and native workflow qualification remain open. Selected-manager and qualified
custom-file capabilities are covered in the [manager/profile guide](glyport-managers.md);
its connected local-manager examples exercise actual constructors, reload,
parser/sidebar dispatch and typed failures with explicit lawful invented providers.
Complete default/private resources and native initialization/reload remain separate.

## Global Unicode metadata

The private candidate’s [global Unicode guide](glyport-unicode.md) supplies eight
owned examples for `Glyphs.glyphInfoForUnicode(String, font=None)`, integer/bool
formatting and early integer name dispatch. It explains exact combined primary/legacy-index
lookup, raw-spelling synthesis on a true miss, UTF16 gates, historical classification
and explicit local-manager/bridge refusals. Global queries never read the active
font. Index insertion follows record order, primary then legacy, with later keys
winning; returned primary and legacy fields remain separate. The corrected guide
and all 35 owned examples pass in both current ordinary six-wheel prefixes with
installed origins and current Echopy producer provenance checked; all 702
runtime/data files match byte for byte.
That tuple passes 4,481 Scriptmix tests with 1 existing selection-read skip and
2,436 Examples tests without skips.
Maintained data and these offline checks do not qualify proprietary database
completeness or native workflows.

## Stored production metadata

The [production metadata guide](glyport-production.md) separates the stored
`GSGlyphInfo.productionName` getter from helper output, shared name fills and
independent copies. Its owned examples use the actual GlyphsApp exports in an
offline execution context. Represented public records now pass source and both ordinary installed-artifact
checks: all 35 authored examples, 5,697 Glyport and 370 Echopy tests per prefix,
with 702 runtime/data files matching the six-wheel tuple. The exact consumer
tuple passes 4,481 Scriptmix tests/one existing skip and 2,436 Examples tests. Glyph production writes, application conversion, all 1,580
unqualified factory routes and native/original workflows remain separate.
