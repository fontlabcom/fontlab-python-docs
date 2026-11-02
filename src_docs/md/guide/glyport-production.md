---
this_file: src_docs/md/guide/glyport-production.md
---

# Stored production names in Glyph Info


The numerical ordinary-artifact results below identify their retained predecessor
checkpoint. The [current manager/profile guide](glyport-managers.md) documents
the H source changes. Earlier source assumptions are corrected below; original
preimages remain in verification evidence. Old receipts do not qualify the new
ordinary tuple or native behavior.

Read `GSGlyphInfo.productionName` when you need the stored production metadata of
an identified record. Keep `None`, empty text and explicit text distinct. An
explicit value equal to the nice name remains that text; it is not changed to
`None`. This describes the retained Glyphs 4 getter contract implemented by the
current private source candidate, not every Glyphs version or a published release.

The field is separate from `GSGlyph.production`, glyph storage flags and
`Glyphs.productionGlyphName`. A Glyph Info read does not qualify those glyph
write/export or application conversion workflows.

| Access | Production result |
| --- | --- |
| Direct Unicode record | Read its stored value without filling it |
| Exact represented name or accepted alias | Fill a known nil value, then read it |
| Explicit empty value | Preserve it; exact-name access does not fill it |
| Copied record | Retain the value present when the copy was made |
| Generic derived suffix | Compute the derived output from its base and exact suffix tokens |
| Metadata with no established production source | Raise an explicit unsupported-capability error |

All examples below use owned data and actual exported classes outside FontLab.
They exercise source behavior through `ExecutionContext` and `FontLabSession`,
with empty packages/defaults and inert host objects. They do not run an original
script, access user fonts or create a native application. Both fresh ordinary wheel/sdist prefixes pass all 35 owned examples (24 retained
and 11 here), 5,697 Glyport tests and 370 Echopy tests. All 702 runtime/data files
match the exact six-wheel tuple; all 40 third-party pins and installed origins
verify. The same tuple passes 4,481 Scriptmix tests with one existing skip and
2,436 Examples tests. These are private artifact checks; native and publication
gates remain separate. Earlier hashes identify their retained predecessor tuples.

## Prepare an owned offline session

Run this setup once before the examples. It temporarily substitutes a small
owned in-memory dataset and restores the maintained dataset in `finally`.
It never edits the dependency's source files or dictionaries. This is a test
fixture; a normal script obtains `Glyphs` and the classes from its own
`GlyphsApp` execution context.

```python
from contextlib import contextmanager
from pathlib import Path
from types import ModuleType

from glyphsLib import glyphdata
from fontlab_glyport import ExecutionContext
from fontlab_glyport.glyphsapp.fontlab_session import FontLabSession

@contextmanager
def owned_glyphs(rows):
    glyphdata.get_glyph("A")
    previous = glyphdata.GLYPHDATA
    records = [dict(row) for row in rows]
    names = {row["name"]: row for row in records}
    alternatives, productions, encodings = {}, {}, {}
    for row in records:
        for alias in row.get("altNames", "").replace(" ", "").split(","):
            if alias:
                alternatives[alias] = row
        if row.get("production"):
            productions[row["production"]] = row
        if row.get("unicode"):
            encodings[row["unicode"]] = row
    owned = glyphdata.GlyphData(names, alternatives, productions, encodings)
    ctx = ExecutionContext(Path.cwd(), "glyphs3")
    session = FontLabSession(
        ctx, version=(3.2, 3234.0), packages=[], defaults={},
        qt=object(), fontlab=ModuleType("fontlab"),
    )
    ctx.adapters.update(session.adapters())
    glyphdata.GLYPHDATA = owned
    try:
        with ctx:
            yield ctx.import_module("GlyphsApp")
    finally:
        ctx.close()
        glyphdata.GLYPHDATA = previous
        assert records == rows, "Queries must preserve the owned source records"
```

## Preserve nil, empty, equal and explicit values

A known absent field is `None`. Empty text is a present value. Both an explicit
nice-name value and a different explicit production value survive direct and
exact-name reads. The raw nil example uses a fresh dataset: an earlier name
query can already have filled that shared record.

<!-- example: glyport-production-stored-values -->
```python
rows = [
    {"name": "nil", "unicode": "0041", "category": "Letter"},
    {"name": "empty", "unicode": "0042", "production": "", "category": "Letter"},
    {"name": "equal", "unicode": "0043", "production": "equal", "category": "Letter"},
    {"name": "explicit", "unicode": "0044", "production": "OwnedProd", "category": "Letter"},
]
with owned_glyphs(rows) as exports:
    app = exports.Glyphs
    assert app.glyphInfoForUnicode("0041").productionName is None
    for code, name, expected in [
        ("0042", "empty", ""), ("0043", "equal", "equal"),
        ("0044", "explicit", "OwnedProd"),
    ]:
        assert app.glyphInfoForUnicode(code).productionName == expected
        assert app.glyphInfoForName(name).productionName == expected
    assert app.glyphInfoForName("nil").productionName == "nil"
```

## Observe shared fill and independent copies

Exact names, alternate names and accepted production aliases refer to the same
represented record. A name read fills only a nil stored value. A raw handle
obtained earlier observes that fill. `copy` and `deepcopy` retain independent
production values from the time they were copied; neither is a live view of the
later shared fill.

<!-- example: glyport-production-shared-copy -->
```python
from copy import copy, deepcopy

with owned_glyphs([{
    "name": "ownedLetter", "unicode": "0041", "altNames": "ownedAlias",
    "script": "latin", "category": "Letter",
}]) as exports:
    app = exports.Glyphs
    raw = app.glyphInfoForUnicode("0041")
    shallow, deep = copy(raw), deepcopy(raw)
    assert raw.productionName is None
    alias = app.glyphInfoForName("ownedAlias")
    assert (alias.name, alias.productionName) == ("ownedLetter", "ownedLetter")
    assert raw.productionName == "ownedLetter"
    assert shallow.productionName is None and deep.productionName is None
```

## Distinguish Unicode text, uni/u copies and synthesized records

A bare character that reaches Unicode lookup retains the raw shared record.
A represented single-record `uni` or `u` name takes a copy, preserving its raw
production at that time. Exact stored names still take priority over decoding.
A direct Unicode miss can synthesize a record whose production is its constructed
name. The name-factory fallback for a rejected scalar is a different route with
a known nil value; these results do not qualify general complex-name synthesis.

<!-- example: glyport-production-unicode-copy -->
```python
with owned_glyphs([{
    "name": "ownedLetter", "unicode": "0041", "category": "Letter",
}]) as exports:
    app = exports.Glyphs
    raw = app.glyphInfoForName("A")
    uni = app.glyphInfoForName("uni0041")
    u = app.glyphInfoForName("u0041")
    assert raw.productionName is None
    assert uni.productionName is None and u.productionName is None
    app.glyphInfoForName("ownedLetter")
    assert raw.productionName == "ownedLetter"
    assert uni.productionName is None and u.productionName is None
    synthesized = app.glyphInfoForUnicode("0378")
    assert (synthesized.name, synthesized.productionName) == ("uni0378", "uni0378")
    assert app.glyphInfoForName("u10FFFF").productionName is None
```

## Keep normalization separate from the stored getter

The manager's production helper computes an output; it does not rewrite an
existing explicit raw field. Its represented rules are:

- Preserve nonempty explicit text, except a seven-UTF16-unit lowercase `uni`
  value with four-UTF16-unit Unicode produces `uni` plus that Unicode.
- For nil or empty helper input with Unicode, private-use encodings and Latin
  dotted/hyphenated names use `uni` or `u` plus the unchanged Unicode text.
  Other encoded names use the nice name.
- Without Unicode, remove hyphens and retain dots. If removal leaves empty
  text, retain the original name.

Those helper rules do not override the getter's empty-value preservation.
Derived suffix results expose the distinction. UTF16 units matter: a
supplementary character occupies two units, unlike Python's scalar count.

<!-- example: glyport-production-helper-output -->
```python
with owned_glyphs([
    {"name": "owned-ar", "unicode": "0627", "production": "uniFFFF",
     "script": "arabic", "category": "Letter"},
    {"name": "empty-latin", "unicode": "00C1", "production": "",
     "script": "latin", "category": "Letter"},
    {"name": "utf16", "unicode": "0041", "production": "uni😀xx",
     "category": "Letter"},
    {"name": "owned-name", "category": "Letter"},
]) as exports:
    app = exports.Glyphs
    assert app.glyphInfoForUnicode("0627").productionName == "uniFFFF"
    assert app.glyphInfoForName("owned-ar.ss01.alt").productionName == "uni0627.ss01.alt"
    assert app.glyphInfoForUnicode("0627").productionName == "uniFFFF"
    assert app.glyphInfoForName("empty-latin").productionName == ""
    assert app.glyphInfoForName("empty-latin.alt").productionName == "uni00C1.alt"
    assert app.glyphInfoForName("utf16.alt").productionName == "uni0041.alt"
    assert app.glyphInfoForUnicode("0041").productionName == "uni😀xx"
    assert app.glyphInfoForName("owned-name").productionName == "ownedname"
```

## Preserve alias order and lowercase uni exclusions

The represented name lookup follows record order. Each record contributes its
primary name, its production alias unless it starts with lowercase `uni`, and
then alternate names. Later assignments win, even over an earlier primary name.
The maintained public loader normalizes separator spaces in alternate names.
Direct Unicode still selects its own stored record, even when that record's
name has been shadowed in the name index. Lowercase `uni` exclusion applies to
a production alias alone; it does not remove an exact stored primary name.

<!-- example: glyport-production-alias-order -->
```python
with owned_glyphs([
    {"name": "earlier", "unicode": "0041", "category": "Letter"},
    {"name": "later", "production": "earlier", "altNames": "First, Second",
     "category": "Letter"},
    {"name": "uni0041", "production": "Exact", "category": "Letter"},
    {"name": "excludedAlias", "production": "uni0041", "category": "Letter"},
]) as exports:
    app = exports.Glyphs
    assert app.glyphInfoForName("earlier").name == "later"
    assert app.glyphInfoForUnicode("0041").name == "earlier"
    assert app.glyphInfoForUnicode("0041").productionName is None
    assert app.glyphInfoForName("First").name == "later"
    assert app.glyphInfoForName("Second").name == "later"
    assert app.glyphInfoForName("uni0041").productionName == "Exact"
```

## Retain suffix tokens and choose the represented longest prefix

Generic suffix output appends the exact remaining tokens to the base helper
output. Repeated and empty suffix tokens are retained. A represented longer
prefix takes priority over a shorter base; intermediate synthesized prefixes
are not invented. Global lookup can fill the chosen shared base. The special
`case`/`cap` context copies before its fill, preserving the earlier raw record.

<!-- example: glyport-production-generic-suffix -->
```python
with owned_glyphs([
    {"name": "A", "unicode": "0041", "category": "Letter"},
    {"name": "A.alt", "unicode": "0042", "production": "OwnedLongest",
     "category": "Letter"},
]) as exports:
    app = exports.Glyphs
    assert app.glyphInfoForName("A.alt.ss01..ss01").productionName == "OwnedLongest.ss01..ss01"
    raw = app.glyphInfoForUnicode("0041")
    assert raw.productionName is None
    cap = app.glyphInfoForName("A.cap")
    assert (cap.case, cap.productionName) == (1, "A.cap")
    assert raw.productionName is None
```

A represented canonical suffix after a `uni/u` copy has a separate boundary.
When the last token is consumed, the copy retains the raw production of that
canonical record. With tokens remaining, the helper computes their derived
output. The canonical record's explicit raw value remains unchanged.

<!-- example: glyport-production-canonical-suffix -->
```python
with owned_glyphs([
    {"name": "A", "unicode": "0041", "category": "Letter"},
    {"name": "A.alt", "unicode": "0042", "unicodeLegacy": "E001",
     "production": "uniFFFF", "category": "Letter"},
]) as exports:
    app = exports.Glyphs
    consumed = app.glyphInfoForName("uni0041.alt")
    assert (consumed.name, consumed.unicode, consumed.unicodeLegacy) == ("A.alt", None, None)
    assert consumed.productionName == "uniFFFF"
    assert app.glyphInfoForName("uni0041.alt.ss01").productionName == "uni0042.ss01"
    assert app.glyphInfoForUnicode("0042").productionName == "uniFFFF"
```

## Keep model copy boundaries distinct

A model's Glyph Info can share a global raw production field until a copy branch
applies. An enabled stored metadata flag forces a copy even when its value is
equal to the resolved value. The example uses an owned fake font backend;
it does not qualify an actual FontLab edit, history step or saved font.

<!-- example: glyport-production-model-stored-copy -->
```python
from fontlab_glyport.model import Model
from fontlab_glyport.model.fake_backend import FakeBackend

with owned_glyphs([{"name": "A", "unicode": "0041", "category": "Letter"}]) as exports:
    app, Info = exports.Glyphs, exports.GSGlyphInfo
    shared_glyph = Model(FakeBackend()).font.glyphs["A"]
    stored_glyph = Model(FakeBackend()).font.glyphs["A"]
    shared = Info(shared_glyph)
    stored_glyph.case = 0
    stored_glyph.storeCase = True
    detached = Info(stored_glyph)
    assert shared.productionName is None and detached.productionName is None
    app.glyphInfoForName("A")
    assert shared.productionName == "A"
    assert detached.productionName is None
```

Private-use renaming also copies before a later global fill. Additional-Unicode
and Arabic presentation processing have distinct lookup order: the additional
stage can fill an isolated named record, while presentation reads that record
raw. Copying can occur even if an encoding is already present. None of these
metadata fixtures establish glyph production storage or export behavior.

<!-- example: glyport-production-model-private-copy -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

with owned_glyphs([{
    "name": "ownedPrivate", "unicode": "E123", "category": "Private Use",
}]) as exports:
    app = exports.Glyphs
    glyph = Model(FakeBackend()).font.glyphs.append(GSGlyph("ownedPrivate"))
    detached = exports.GSGlyphInfo(glyph)
    assert detached.productionName is None
    app.glyphInfoForName("ownedPrivate")
    assert app.glyphInfoForUnicode("E123").productionName == "uniE123"
    assert detached.productionName is None
```

<!-- example: glyport-production-model-arabic-copy -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

rows = [
    {"name": "owned-ar", "unicode": "0627", "script": "arabic", "category": "Letter"},
    {"name": "owned-ar.isol", "unicodeLegacy": "FE8D", "script": "arabic", "category": "Letter"},
]
with owned_glyphs(rows) as exports:
    app = exports.Glyphs
    isolated = app.glyphInfoForUnicode("FE8D")
    glyph = Model(FakeBackend()).font.glyphs.append(GSGlyph("owned-ar"))
    detached = exports.GSGlyphInfo(glyph)
    assert isolated.productionName == "ownedar.isol"
    assert detached.productionName is None
    app.glyphInfoForName("owned-ar")
    assert detached.productionName is None

with owned_glyphs(rows) as exports:
    app = exports.Glyphs
    isolated = app.glyphInfoForUnicode("FE8D")
    font = Model(FakeBackend()).font
    glyph = font.glyphs.append(GSGlyph("owned-ar"))
    glyph.unicodes = []
    font.customParameters["Use Arabic Presentation Form Unicodes"] = True
    detached = exports.GSGlyphInfo(glyph)
    assert isolated.productionName is None
    assert detached.productionName is None
```

## Refuse an unavailable source explicitly

Known nil metadata is different from metadata whose production source is
unestablished. Classification inferred by a library does not establish a
production value. The latter getter raises
`GSGlyphInfo.productionName.source`; do not replace that exception with a guessed
`None`, empty string or sanitized export name. The qualified snapshot remains
read-only: attempts to assign its production name refuse separately.

<!-- example: glyport-production-unknown-source -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability

with owned_glyphs([{"name": "A", "unicode": "0041", "category": "Letter"}]) as exports:
    unknown = exports.GSGlyphInfo(SimpleNamespace(
        name="owned", unicode=None, category=None, subCategory=None, script=None, case=0,
    ))
    try:
        value = unknown.productionName
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.productionName.source"
    else:
        raise AssertionError("An unavailable source must refuse")
    known = exports.Glyphs.glyphInfoForName("A")
    try:
        known.productionName = "changed"
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.productionName"
    else:
        raise AssertionError("The snapshot must remain read-only")
    assert known.productionName == "A"
```

## Keep the qualified scope visible

The source work covers represented records from a versioned public subset,
owned ordering/copy cases and the retained version-qualified getter/helper
contract. The maintained public input has 74,247 records; it is not proprietary
GlyphData completeness or proof that resource contents agree across versions.
Those earlier diagnostic gaps now have a [compound metadata candidate](glyport-compounds.md)
with independent core-field/state qualification across all 1,580 public inputs.
Existing proprietary recipes/optional fields, full custom/global/font-local
managers, remaining resource/version branches and complete original/native
workflows remain in scope. The new compound ordinary consumer cohort is pending.

Glyph production setters, storage flags and application production conversion
remain separate contracts. Source examples and normal installed artifacts do
not establish native FontLab conformance, history, cache/font/dirty preservation
or saved/reopened results. The observed FontLab 9.0.9801 process is not a new
capture. Canonical promotion, source-lock refresh, generated reference/site,
archive/routes, browser/accessibility and publication remain separate gates.
D29 and D30 remain open.

Continue with [global Unicode](glyport-unicode.md), [legacy Unicode and ROS](glyport-metadata.md),
[parameters and Arabic encodings](glyport-parameters.md), the [Glyphs compatibility guide](glyphs.md)
or the [Glyport package](../packages/glyport.md).
