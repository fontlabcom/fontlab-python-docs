---
this_file: src_docs/md/guide/glyport-metadata.md
---
# Legacy Unicode snapshots and ROS metadata

Glyport's current private candidate exposes `GSGlyphInfo.unicodeLegacy` as a
separate metadata field. Reading a legacy encoding does not make it the primary
Unicode, assign it to a glyph or refresh that glyph. ROS processing has a distinct
data boundary: the five proprietary shared-manager maps are unavailable, so a
request for one refuses before metadata writes.

Every example here uses owned Python data outside FontLab. All 24 retained examples
and 11 new [production examples](glyport-production.md) pass in both fresh ordinary
six-wheel prefixes, with installed origins checked and all 702 runtime/data files
matching byte for byte.
Echopy producer provenance matches the corrected source. These offline checks
do not qualify native history, save/reopen or complete original scripts. The
[parameter and Arabic guide](glyport-parameters.md) covers the following presentation stage and retains its own verified examples.

## Keep primary and legacy Unicode separate

The global name factory reads maintained GlyphData. Its `unicode` and
`unicodeLegacy` fields answer different questions:

| Requested name | Canonical name | `unicode` | `unicodeLegacy` |
| --- | --- | --- | --- |
| `A` | `A` | `"0041"` | `None` |
| `alef-ar` | `alef-ar` | `"0627"` | `None` |
| `alef-ar.isol` | `alef-ar.isol` | `None` | `"FE8D"` |
| `aleffinalarabic` | `alef-ar.fina` | `None` | `"FE8E"` |

The owned application fixture supplies no host bridge or persistent defaults.
It does not activate the synthetic `GlyphsApp` module.

<!-- example: glyport-legacy-primary -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
for name, primary, legacy in [
    ("A", "0041", None),
    ("alef-ar", "0627", None),
    ("alef-ar.isol", None, "FE8D"),
]:
    info = app.glyphInfoForName(name)
    assert (info.name, info.unicode, info.unicodeLegacy) == (name, primary, legacy)
```

Aliases resolve to the maintained canonical record, including its legacy field.
They do not create a second independent primary-Unicode record.

<!-- example: glyport-legacy-alias -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
alias = app.glyphInfoForName("aleffinalarabic")
canonical = app.glyphInfoForName("alef-ar.fina")
assert alias.name == canonical.name == "alef-ar.fina"
assert alias.unicode is canonical.unicode is None
assert alias.unicodeLegacy == canonical.unicodeLegacy == "FE8E"
```

The shared Unicode index includes each record’s primary keys followed by its
non-nil legacy key in source order; later assignments replace earlier ones.
[Global Unicode lookup](glyport-unicode.md) therefore selects `alef-ar.isol` for
`FE8D`, with primary Unicode `None` and legacy Unicode `FE8D`. It selects
`hamza-ar.isol` for `FE80` and the later `NULL` record for duplicated `0000`.
These examples qualify specific maintained records, not complete custom GlyphData.
The linked guide separates exact combined-index lookup, raw synthesis on a true
miss and remaining input boundaries.

## Global lookup ignores active-font data

Omitting `font`, passing positional `None` or using `font=None` always selects
global data. Active-font glyphs, custom parameters and stored overrides are not
read. For name strings, an explicit non-`None` font raises
`Glyphs.glyphInfoForName.localData`; font-local GlyphData remains unsupported.
Integer name inputs instead dispatch to `glyphInfoForUnicode` before that guard,
discarding the font argument and preserving instance-method overrides. Direct
Unicode calls refuse an explicit non-None font with
`Glyphs.glyphInfoForUnicode.localData` before payload checks; see the linked
[dispatch and refusal examples](glyport-unicode.md).

<!-- example: glyport-legacy-active-isolation -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSApplication

class UnreadableFont:
    def __getattribute__(self, name):
        raise AssertionError("Global lookup must not read an active font")

active = UnreadableFont()
app = GSApplication(SimpleNamespace(font=active), object(), {}, None, lambda *args: None)
assert app.glyphInfoForName("alef-ar.isol").unicodeLegacy == "FE8D"
assert app.glyphInfoForName("alef-ar.isol", None).unicodeLegacy == "FE8D"
assert app.glyphInfoForName("alef-ar.isol", font=None).unicodeLegacy == "FE8D"
try:
    app.glyphInfoForName("alef-ar.isol", font=active)
except UnsupportedCapability as error:
    assert error.capability == "Glyphs.glyphInfoForName.localData"
else:
    raise AssertionError("Explicit font-local lookup must refuse")
```

## Snapshot raw values without normalizing them

Direct `GSGlyphInfo` construction from a namespace snapshots the supplied legacy
value exactly. Missing means `None`; empty strings, lowercase hex and arbitrary
owned text remain distinct. Editing the source object later does not edit the
snapshot. This package makes snapshots read-only and refuses assignment with
`GSGlyphInfo.unicodeLegacy`. Native Glyph Info has a setter; package read-only
policy does not describe the native object's mutability.

<!-- example: glyport-legacy-raw-snapshot -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSGlyphInfo

for legacy in (None, "", "fe8d", "unparsed owned value"):
    source = SimpleNamespace(name="owned", unicode=None, unicodeLegacy=legacy,
        category="Letter", subCategory=None, script="arabic", case=0)
    snapshot = GSGlyphInfo(source)
    source.unicodeLegacy = "changed"
    assert snapshot.unicodeLegacy == legacy
    try:
        snapshot.unicodeLegacy = "FE8D"
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo.unicodeLegacy"
    else:
        raise AssertionError("The package snapshot must be read-only")
    assert snapshot.unicodeLegacy == legacy
    del source.unicodeLegacy
    assert GSGlyphInfo(source).unicodeLegacy is None
```

## Construct from an owned model glyph

For an actual package `GSGlyph`, the constructor resolves **only the new legacy
field** through owned metadata. Existing name, primary Unicode, category,
subcategory, script and case snapshot behaviour is retained. This constructor
does not replace those fields with a wholesale resolved record. Resolution can
refuse unsupported data; it does not query a native application.

An unencoded `alef-ar.isol` draft has a legacy value without acquiring an
encoding. A generic derived suffix clears inherited legacy metadata. A nil
resolved record gives no legacy value, even when the stored name resembles an
isolated-form record. An already captured snapshot remains independent.

Global indexing and model postprocessing are different paths. The detached,
already encoded Arabic glyph below still reaches the retained parentless Arabic
nil-return branch: its snapshot keeps stored primary `FE8D` and legacy `None`.
Direct global lookup of `FE8D` returns `alef-ar.isol` with database primary `None`
and legacy `FE8D`. The shared-index correction does not bypass the model branch.

<!-- example: glyport-legacy-model-snapshot -->
```python
from fontlab_glyport.glyphsapp import GSGlyphInfo
from fontlab_glyport.model import GSGlyph

glyph = GSGlyph("alef-ar.isol")
snapshot = GSGlyphInfo(glyph)
assert (snapshot.name, snapshot.unicode, snapshot.unicodeLegacy) == (
    "alef-ar.isol", None, "FE8D")
assert glyph.unicodes == []
glyph.name = "alef-ar.isol.owned"
assert GSGlyphInfo(glyph).unicodeLegacy is None
assert snapshot.unicodeLegacy == "FE8D"

encoded = GSGlyph("alef-ar.isol")
encoded.unicode = "FE8D"
current = GSGlyphInfo(encoded)
assert current.unicode == "FE8D" and current.unicodeLegacy is None
assert encoded.unicodes == ["FE8D"]
assert GSGlyphInfo(GSGlyph("unknown-owned")).unicodeLegacy is None
```

## Recognize ROS requests before writing

The audited shared manager places ROS replacement after additional Unicode and
before Arabic presentation. With its actual maps, it replaces the complete
ordered Unicode set using the **resolved metadata name**. Glyport does not bundle
those proprietary MapFiles. Adobe CMaps and maintained GlyphData are not
equivalent substitutes; no approximated map is supplied.

The exact shared-manager text contract is:

1. Split on a hyphen (`-`).
2. Only when that result has a count other than three, retry with comma plus
   one space (`, `).
3. Require exactly three pieces. Preserve case and whitespace.
4. Use the first two pieces for the map name. Ignore the supplement; it need
   not be numeric or nonempty.

Requests naming `Adobe-CNS1`, `Adobe-GB1`, `Adobe-Japan1`, `Adobe-KR` or
`Adobe-Korea1` raise `GSGlyphInfo.ROS.mappingData` before presentation and metadata
writes. The guard cannot know whether a particular glyph would be absent from
the unavailable map, so that does not bypass refusal. The revision comparison
below is an explicitly owned backend diagnostic, not native dirty-state proof.

<!-- example: glyport-ros-refusal -->
```python
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.model import Model
from fontlab_glyport.model.fake_backend import FakeBackend

for ordering in ("CNS1", "GB1", "Japan1", "KR", "Korea1"):
    for separator in ("-", ", "):
        for supplement in ("7", "", "owned"):
            backend = FakeBackend()
            font = Model(backend).font
            glyph = font.glyphs["A"]
            font.customParameters["ROS"] = separator.join(("Adobe", ordering, supplement))
            before = (glyph.name, glyph.unicodes, glyph.case, glyph.script, glyph.category)
            revision = backend.revision("font")
            try:
                glyph.updateGlyphInfo(changeName=False)
            except UnsupportedCapability as error:
                assert error.capability == "GSGlyphInfo.ROS.mappingData"
            else:
                raise AssertionError("Unavailable ROS mapping must refuse")
            assert (glyph.name, glyph.unicodes, glyph.case, glyph.script, glyph.category) == before
            assert backend.revision("font") == revision
```

## Distinguish an unknown resource from a no-op refresh

Nil, malformed text and unknown map names leave the preceding record unchanged
at the ROS stage. That shared-bundle no-op does not make an entire metadata
refresh a no-op: earlier additional-Unicode processing can still add encodings.
It is not a guarantee about arbitrary custom managers or user-supplied resources.

For example, `Adobe,Japan1,7` lacks the required spaces. `Adobe, Japan1, 7-extra-more`
has exactly three hyphen pieces, so comma fallback is suppressed and no shipped
map matches. Conversely, `Adobe-Japan1-7\n` and `Adobe, Japan1, 7-extra` still
require the missing map: the supplement is ignored after delimiter selection.

<!-- example: glyport-ros-unknown-text -->
```python
from fontlab_glyport.model import Model
from fontlab_glyport.model.fake_backend import FakeBackend

for value in (None, "", "Adobe-Japan1", "Adobe-Japan1-7-extra", "Adobe,Japan1,7",
              "Adobe,  Japan1, 7", " Adobe-Japan1-7", "adobe-Japan1-7",
              "Adobe-Unknown-7", "Adobe, Japan1, 7-extra-more"):
    font = Model(FakeBackend()).font
    glyph = font.glyphs["A"]
    font.customParameters["ROS"] = value
    glyph.updateGlyphInfo(changeName=False)
    assert glyph.name == "A"
    assert glyph.unicodes == ["0041", "0061"]  # Earlier additional-Unicode stage.
```

Normal first-active parameter selection applies to ROS. An inactive or shadowed
map request is not the selected value. Nontext values require an unqualified
Objective-C description conversion; they raise `GSGlyphInfo.ROS.value` rather
than using Python `str`, truthiness or an invented native representation.

<!-- example: glyport-ros-selection-and-value -->
```python
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
glyph = font.glyphs["A"]
first = GSCustomParameter("ROS", "Adobe-Unknown-7")
font.customParameters.extend([first, GSCustomParameter("ROS", "Adobe-Japan1-7")])
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0041", "0061"]
first.active = False
try:
    glyph.updateGlyphInfo(changeName=False)
except UnsupportedCapability as error:
    assert error.capability == "GSGlyphInfo.ROS.mappingData"
else:
    raise AssertionError("The now-selected map request must refuse")

other = Model(FakeBackend()).font
other.customParameters["ROS"] = False
try:
    other.glyphs["A"].updateGlyphInfo(changeName=False)
except UnsupportedCapability as error:
    assert error.capability == "GSGlyphInfo.ROS.value"
else:
    raise AssertionError("Nontext ROS description is unqualified")
```

## Acceptance boundaries

These owned paths do not qualify full lawful ROS mapping, custom managers,
native name collisions, complete suffix synthesis, Undo/Redo, saved/reopened
fonts or original callers. Metadata early returns can bypass these stages;
the guard is not a global validator for every font with a ROS parameter.

Use archive hashes and installed-origin/byte checks to identify a private
candidate; repeated dirty development versions are not sufficient. Historical
hashes on the [Glyport package page](../packages/glyport.md) stay historical.
The central generated source-lock review, full build, archive/routes, browser
accessibility and publication gates remain separate. Authored-source checks do
not establish a generated, live or released page.

## Stored production is a separate field

The [production metadata guide](glyport-production.md) covers known nil, empty,
equal and explicit stored values, raw Unicode versus exact-name fill, aliases
and detached copies. A legacy encoding does not authorize a production-name
rewrite. The new represented-record source contract does not establish glyph
production storage, application conversion or complete native workflows.
