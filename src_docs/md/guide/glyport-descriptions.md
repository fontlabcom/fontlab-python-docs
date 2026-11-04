---
this_file: src_docs/md/guide/glyport-descriptions.md
---
# Read the description on the selected record

`GSGlyphInfo.desc` is stored metadata. It can be `None`, empty text or an actual
description. A name, encoding or compound spelling does not authorize inventing
that text from Python's Unicode database.

The current source candidate preserves the selected public record's description
through lookup and copy stages. The [manager guide](glyport-managers.md) adds
parent/document/shared selection, canonical views and exact wrapper profiles.
Matching companion artifacts and ordinary consumers remain a separate gate.
The public dataset is a versioned subset, with separate native, proprietary-data
and original-workflow limits.

## Prepare owned records

First run the [owned session setup](glyport-production.md#prepare-an-owned-offline-session).
It yields actual `GlyphsApp` exports in an offline session with empty packages and
inert host objects, then restores the public data. These controls use owned input
records; they do not load FontLab, edit fonts or qualify a native workflow.

```python
def described_letters():
    return [
        {"name": "A", "unicode": "0041", "category": "Letter", "script": "latin",
         "description": "Owned first Ω", "altNames": "OwnedAlias"},
        {"name": "B", "unicode": "0042", "category": "Letter", "script": "latin",
         "description": "Owned second"},
    ]
```

## Keep stored text across name and alias lookup

The exact record supplies the same description when reached through its alias
or a synthesized Unicode spelling. The string is not derived from that spelling.

<!-- example: glyport-description-stored -->
```python
with owned_glyphs(described_letters()) as exports:
    app = exports.Glyphs
    for name in ("A", "OwnedAlias", "uni0041", "A.alt"):
        info = app.glyphInfoForName(name)
        assert type(info) is exports.GSGlyphInfo
        assert info.desc == "Owned first Ω"
```

## Distinguish nil from empty text

A known parsed record without the attribute has nil description. Explicit empty
text remains empty; neither case is replaced with a Unicode character name.

<!-- example: glyport-description-nil-empty -->
```python
for value in (None, ""):
    rows = described_letters()
    if value is None:
        del rows[0]["description"]
    else:
        rows[0]["description"] = value
    with owned_glyphs(rows) as exports:
        assert exports.Glyphs.glyphInfoForName("A").desc == value
```

## Read descriptions without filling stored production

The Unicode route returns the selected raw record. Reading `desc` does not
perform the separate ordinary-name production fill.

<!-- example: glyport-description-unicode-read -->
```python
with owned_glyphs(described_letters()) as exports:
    info = exports.Glyphs.glyphInfoForUnicode("0042")
    assert info.productionName is None
    assert info.desc == "Owned second"
    assert info.productionName is None
```

## Follow the selected seed through composition

A compound retains its selected seed's description. It does not concatenate
descriptions from its components. A suffix wrapper can retain a nested compound.
Exact whole-name hits and Indic donor replacement can select another seed.

<!-- example: glyport-description-selected-seed -->
```python
with owned_glyphs(described_letters()) as exports:
    app = exports.Glyphs
    assert app.glyphInfoForName("uni00410042").desc == "Owned first Ω"
    assert app.glyphInfoForName("uni00420041").desc == "Owned second"
    wrapped = app.glyphInfoForName("uni00410042.ss01")
    assert wrapped.desc == wrapped.components[0].desc == "Owned first Ω"
```

## Preserve the value in a read-only copy

The copy retains stored text. The property has no assignment operation; editing a
glyph or its exported font is a different contract.

<!-- example: glyport-description-copy -->
```python
from copy import copy
from fontlab_glyport.errors import UnsupportedCapability

with owned_glyphs(described_letters()) as exports:
    info = exports.Glyphs.glyphInfoForName("A")
    duplicate = copy(info)
    assert duplicate is not info and duplicate.desc == info.desc
    try:
        duplicate.desc = "Changed"
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.desc"
    else:
        raise AssertionError("Description must remain read-only")
    assert duplicate.desc == info.desc == "Owned first Ω"
```

## Exercise the existing model snapshot constructor

This uses the exported `GSGlyphInfo(glyph)` frozen constructor. The current
`glyph.glyphInfo` property instead delegates through its parent's manager;
the [attached-glyph example](glyport-managers.md#follow-document-ownership-and-retain-old-views)
exercises that implemented entry path. A detached glyph's property refuses.

<!-- example: glyport-description-model-snapshot -->
```python
with owned_glyphs(described_letters()) as exports:
    glyph = exports.GSGlyph("A")
    info = exports.GSGlyphInfo(glyph)
    assert info.desc == "Owned first Ω"
```

## Refuse a source that does not establish the field

An arbitrary external object with no description contract is different from a
known parsed record with a nil description. Do not turn that uncertainty into nil.

<!-- example: glyport-description-unknown-source -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability

with owned_glyphs(described_letters()) as exports:
    raw = SimpleNamespace(name="Owned", unicode=None, category="Letter",
                          subCategory=None, script="latin", case=0)
    try:
        _ = exports.GSGlyphInfo(raw).desc
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.desc.source"
    else:
        raise AssertionError("Unknown source must refuse")
```

## Retain the acceptance boundaries

The source candidate matches all 146,378 public name/Unicode queries against
their selected input descriptions. This proves the versioned public-input
relation, not proprietary database completeness or every Glyphs version.
The actual stored getter and wrapper agree with the
[documented property](https://docu.glyphsapp.com/Core/GlyphsCore/GSGlyphInfo/).

An original HTML tool reads descriptions for glyph-grid tooltips, but its complete
parent-aware manager, font/UI effects and native workflow remain unqualified.
The owned reader and model constructor checks do not prove that whole script.
Fresh matching archives, ordinary providers/consumers, native histories and
saved/reopened outputs retain separate gates. Source-lock refresh, generated
references, rendering, accessibility and publication remain held under D29/D30.
See [stored production](glyport-production.md), [compound metadata](glyport-compounds.md)
and the [Glyport package](../packages/glyport.md).
