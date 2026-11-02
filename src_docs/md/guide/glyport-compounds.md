---
this_file: src_docs/md/guide/glyport-compounds.md
---
# Compound Glyph Info without losing record state

Use `Glyphs.glyphInfoForName` to inspect a multi-code spelling such as
`uni00660069`. Read the resulting name, stored production and components together;
the final spelling alone does not describe how the records were resolved.
A whole-name database hit can preempt composition, and a suffix can introduce
a nested compound. These metadata queries do not implement glyph editing/export.

The current private candidate follows the retained Glyphs 4 compound contract.
Source and genuine Glyport archives pass their recorded checks; the new matching
Echopy/ordinary consumer cohort is still being qualified. Native FontLab/Glyphs
workflows, custom/local managers and complete proprietary recipes remain open.

## Prepare owned offline records

For the controls below, first run the [owned session setup](glyport-production.md#prepare-an-owned-offline-session).
It exports the actual classes through `ExecutionContext`/`FontLabSession`, using
empty packages/defaults and inert host objects outside FontLab. It restores the
maintained dataset afterward. A normal script gets `Glyphs` from its own Glyport
execution context; this fixture is for reproducible offline checks.

```python
def two_letters():
    return [
        {"name": name, "unicode": code, "category": "Letter", "script": "latin"}
        for name, code in [("A", "0041"), ("B", "0042")]
    ]
```

## Read the compound and its fields

Composition clears the compound's primary encoding while retaining component
order. This owned two-Letter case has the retained Ligature classification.

<!-- example: glyport-compound-fields -->
```python
with owned_glyphs(two_letters()) as exports:
    info = exports.Glyphs.glyphInfoForName("uni00410042")
    assert type(info) is exports.GSGlyphInfo
    assert (info.name, info.productionName, info.unicode) == ("A_B", "A_B", None)
    assert (info.category, info.subCategory, info.script, info.case) == (
        "Letter", "Ligature", "latin", 0)
    assert [part.name for part in info.components] == ["A", "B"]
```

## Observe the first fill and later component fill

The first ordinary name lookup fills a known nil production. A later exact B
lookup is visible through the shared B component, while the compound keeps the
production it already stored. This does not make every metadata field a live view.

<!-- example: glyport-compound-shared-fill -->
```python
with owned_glyphs(two_letters()) as exports:
    app = exports.Glyphs
    a, b = app.glyphInfoForUnicode("0041"), app.glyphInfoForUnicode("0042")
    info = app.glyphInfoForName("uni00410042")
    assert (a.productionName, b.productionName) == ("A", None)
    assert info.components[1].productionName is None
    app.glyphInfoForName("B")
    assert info.components[1].productionName == "B"
    assert info.productionName == "A_B"
```

## Keep duplicate positions and shallow component references

The list getter returns a separate container. Repeated positions can still refer
to the same component object; clearing your list does not clear the compound.

<!-- example: glyport-compound-duplicate-positions -->
```python
with owned_glyphs(two_letters()) as exports:
    info = exports.Glyphs.glyphInfoForName("uni00410041")
    assert len(info.components) == 2
    assert info.components[0] is info.components[1]
    copied_list = info.components
    copied_list.clear()
    assert [part.name for part in info.components] == ["A", "A"]
```

## Distinguish raw production from helper output

The raw field can differ from the helper's effective component output. Mixed
Unicode rebuilding uses the saved raw record list, including an explicit value.

<!-- example: glyport-compound-raw-fallback -->
```python
rows = two_letters()
rows[0]["production"] = "uniFFFF"
with owned_glyphs(rows) as exports:
    raw = exports.Glyphs.glyphInfoForUnicode("0041")
    info = exports.Glyphs.glyphInfoForName("uni00410042")
    assert raw.productionName == "uniFFFF"
    assert info.productionName == "uniFFFF0042"
```

## Traverse a suffix wrapper once

A global suffix may wrap one unsuffixed compound. Preserve that nested record
instead of assuming every result exposes a flat A/B list.

<!-- example: glyport-compound-nested-suffix -->
```python
with owned_glyphs(two_letters()) as exports:
    info = exports.Glyphs.glyphInfoForName("uni00410042.ss01")
    assert (info.name, info.productionName) == ("A_B.ss01", "A_B.ss01")
    assert len(info.components) == 1 and info.components[0].name == "A_B"
    assert [part.name for part in info.components[0].components] == ["A", "B"]
```

## Let an exact whole-name record win

Do not infer a compound from spelling alone. An exact represented name wins
before decoding and does not fill the unused A/B records.

<!-- example: glyport-compound-exact-precedence -->
```python
rows = two_letters() + [{
    "name": "uni00410042", "production": "OwnedWinner", "category": "Mark",
}]
with owned_glyphs(rows) as exports:
    app = exports.Glyphs
    info = app.glyphInfoForName("uni00410042")
    assert (info.productionName, info.category, info.components) == ("OwnedWinner", "Mark", [])
    assert app.glyphInfoForUnicode("0041").productionName is None
    assert app.glyphInfoForUnicode("0042").productionName is None
```

## Keep positional records separate from production inputs

Actual Arabic alternates can replace final components. Their raw nil productions
remain nil; the compound's production still uses the earlier saved inputs.

<!-- example: glyport-compound-arabic-alternates -->
```python
rows = [
    {"name": "beh-ar", "unicode": "0628", "production": "uni0628", "script": "arabic", "category": "Letter"},
    {"name": "alef-ar", "unicode": "0627", "production": "uni0627", "script": "arabic", "category": "Letter"},
    {"name": "beh-ar.init", "unicodeLegacy": "FE91", "script": "arabic", "category": "Letter"},
    {"name": "alef-ar.fina", "unicodeLegacy": "FE8E", "script": "arabic", "category": "Letter"},
]
with owned_glyphs(rows) as exports:
    info = exports.Glyphs.glyphInfoForName("uni06280627")
    assert [part.name for part in info.components] == ["beh-ar.init", "alef-ar.fina"]
    assert [part.productionName for part in info.components] == [None, None]
    assert info.productionName == "uni06280627"
```

## Keep metadata reads separate from writes

The returned stored production is read-only. Use the separate glyph/export
contracts for editing; assigning to this snapshot must refuse without a change.

<!-- example: glyport-compound-read-only -->
```python
from fontlab_glyport.errors import UnsupportedCapability
with owned_glyphs(two_letters()) as exports:
    info = exports.Glyphs.glyphInfoForName("uni00410042")
    try:
        info.productionName = "changed"
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.productionName"
    else:
        raise AssertionError("Stored metadata must remain read-only")
    assert info.productionName == "A_B"
```

## Account for the retained long-production rebuild

At 62 UTF16 units, a successful raw Unicode rebuild replaces the assembled
production, including its earlier global suffix. Name and production can differ.

<!-- example: glyport-compound-long-production -->
```python
rows = two_letters()
rows[0]["production"], rows[1]["production"] = "P" * 56, "Q"
with owned_glyphs(rows) as exports:
    info = exports.Glyphs.glyphInfoForName("uni00410042.alt")
    assert info.name == "A_B.alt"
    assert info.productionName == "uni00410042"
```

## Retain the evidence boundaries

Independent source checks cover 1,580 public queries, persistent shared state
and owned boundaries. Public data does not establish existing proprietary recipes
or optional fields. The positional R-versus-other predicate and script mappings
have their own retained-version/public-input qualification; this is not a general
Unicode joining API. Whole-name casing is calibrated against standalone Foundation,
with no runtime native bridge. Neither proof qualifies all Glyphs versions.

Genuine source/archive checks remain separate from a fresh ordinary installed
provider/consumer cohort and native FontLab histories, saved/reopened results,
UI/cache/lifetime preservation and original workflows. Generated references,
source-lock refresh, rendered pages, browser accessibility and publication remain
held under D29/D30. See [stored production](glyport-production.md),
[descriptions](glyport-descriptions.md), [global Unicode](glyport-unicode.md) and the [Glyport package](../packages/glyport.md).
