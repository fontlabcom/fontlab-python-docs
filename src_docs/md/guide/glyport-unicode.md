---
this_file: src_docs/md/guide/glyport-unicode.md
---
# Global Unicode Glyph Info

Use `Glyphs.glyphInfoForUnicode(string_or_int, font=None)` in the default Glyphs4
profile. Glyphs2/3 use `String` instead. The current private candidate returns
the selected manager's read-only `GSGlyphInfo` view or `None`; omitting font
selects shared metadata without reading the active font. Its maintained
GlyphData index includes primary and legacy encodings. The returned record keeps
those fields separate; lookup does not assign either encoding to a glyph or run
font-local postprocessing.

The [manager/profile guide](glyport-managers.md) supplies current runnable
replacements. The examples below now select their intended profiles explicitly, use real
font-manager delegation and distinguish unknown public recipes from finalized
owned recipes. Run its [owned graph setup](glyport-managers.md#prepare-an-owned-graph)
first for the `owned_application` and `owned_parsed_manager` fixtures. Original
predecessor bodies remain preserved in external verification evidence.

These eight examples use owned offline application fixtures and the linked setup.
They import actual package exports without activating a synthetic `GlyphsApp`
module, opening FontLab or executing an original script. At the earlier named checkpoint, all 24 retained examples
and 11 then-new [production examples](glyport-production.md) passed in both ordinary
six-wheel prefixes, with installed module origins checked and all 702 runtime/data
files matching byte for byte. Echopy producer
provenance matches the corrected Glyport source; exact artifact identities and
consumer results are on the existing Glyport package page linked below.
These offline checks do not qualify a published release or native workflow.

## Call the executable keyword

Glyphs2/3 bind `String`, with a capital S; Glyphs4 binds `string_or_int`.
The human-readable label `Unicode` is not a keyword alias. Missing/unknown/
duplicate arguments fail at Python binding before lookup. Current indexed records
retain canonical record views. Public NFD does not establish a physical metadata
recipe; an unknown `components` source now refuses instead of publishing NFD as
that recipe. The example checks that public refusal, then verifies a known owned recipe.

<!-- example: glyport-unicode-keyword-snapshot -->
```python
from fontlab_glyport.errors import UnsupportedCapability
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication, GSGlyphInfo

app = owned_application("glyphs3", SimpleNamespace(font=None))
assert app.glyphInfoForUnicode(String="004a", font=None).name == "J"
info = app.glyphInfoForUnicode("00C1")
assert isinstance(info, GSGlyphInfo) and info.name == "Aacute"
try:
    _ = info.components
except UnsupportedCapability as error:
    assert error.capability == "GSGlyphInfo.components.source"
else:
    raise AssertionError("Public NFD does not establish a physical recipe")
manager = owned_parsed_manager()
manager.updateComponentsInfos()
info = manager.infoFromDataForUnicode_("00C1")
assert [part.name for part in info.components] == ["A", "acutecomb"]
assert all(isinstance(part, GSGlyphInfo) for part in info.components)
info.components.clear()
assert [part.name for part in info.components] == ["A", "acutecomb"]
try:
    app.glyphInfoForUnicode(Unicode="0041")
except TypeError:
    pass
else:
    raise AssertionError("Unicode is not the executable keyword")
```

Current known component records are shallow references in independent returned
lists. [Explicit custom finalization](glyport-managers.md#finalize-the-selected-graph-explicitly)
shows an established recipe without inferring one from an encoding or outline.

## Preserve integer formatting

Glyphs3 tests `isinstance(String, int)` and applies exactly `"%04X" % String`;
Glyphs2 uses an exact-int test. Glyphs4 uses `isinstance` and f-string `04X`
formatting, including subclass `__format__`. Four is a minimum width and does
not validate scalar range. The example selects the real Glyphs3 profile to retain its percent-formatting
assertions. The new guide also exercises Glyphs2 and Glyphs4.

<!-- example: glyport-unicode-integer-format -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

class OwnedInt(int):
    def __int__(self):
        raise AssertionError("Do not coerce an integer subclass")
    def __format__(self, specification):
        raise AssertionError("Preserve percent formatting")

app = owned_application("glyphs3", SimpleNamespace(font=None))
for value, spelling in [(65, "0041"), (OwnedInt(65), "0041"),
                        (True, "0001"), (False, "0000"), (-1, "-001")]:
    actual = app.glyphInfoForUnicode(value)
    expected = app.glyphInfoForUnicode(spelling)
    assert (actual.name, actual.unicode) == (expected.name, expected.unicode)
assert app.glyphInfoForUnicode(OwnedInt(65)).name == "A"
assert app.glyphInfoForUnicode(-1).name == "uni-001"
assert app.glyphInfoForUnicode(0x10FFFF) is None
```

<a id="integer-name-lookup-discards-the-font-first"></a>

## Glyphs2/3 integer name lookup discards the font first

Glyphs2/3 integer Name dispatch calls the instance Unicode method without a font
keyword. Glyphs4 passes `font=font`, including None, through the instance method.
An explicit-font string Name query selects that font's manager in all three
profiles. The former unconditional `.localData` refusal is superseded; a selected
manager's actual result/error now propagates. The explicit Glyphs3 example below retains its integer/override contract while
checking real string-name font delegation and its access-error propagation.

<!-- example: glyport-unicode-name-dispatch -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSApplication

class UnreadableFont:
    def __getattribute__(self, name):
        raise AssertionError("Global lookup must not read the active font")

active = UnreadableFont()
app = owned_application("glyphs3", SimpleNamespace(font=active))
assert app.glyphInfoForName(65, font=active).name == "A"
assert app.glyphInfoForUnicode("0041", font=None).name == "A"
local = owned_parsed_manager()
explicit = SimpleNamespace(glyphsInfo=lambda: local)
assert app.glyphInfoForName("A", font=explicit) is local.glyphInfoForName_("A")
try:
    app.glyphInfoForName("A", font=active)
except AssertionError as error:
    assert str(error) == "Global lookup must not read the active font"
else:
    raise AssertionError("Explicit font access errors must propagate")

calls = []
class OwnedApplication(type(app)):
    def glyphInfoForUnicode(self, *args, **kwargs):
        calls.append((args, kwargs))
        return "owned override"

owned = OwnedApplication(SimpleNamespace(font=active), object(), {}, None, lambda *args: None)
assert owned.glyphInfoForName(True, font=active) == "owned override"
assert calls == [((True,), {})]
```

Both global routes ignore active-font glyph state, parameters, ROS and stored
overrides. They do not invoke the per-glyph metadata postprocessing pipeline.
A result of `None` does not trigger a search of `font.glyphs`.

## Respect refusal precedence

Integer formatting occurs before selecting an explicit font manager. Only None
selects shared; a false-valued font still receives `glyphsInfo()`. There is no
unconditional `.localData` refusal. A malformed object used as a font can fail
at its own method access. With the default manager, built-in strings and None
remain supported after profile-specific integer dispatch; unqualified bridge
payload types retain `.inputType` refusal. The example exercises conversion and selected-manager identity before default
manager payload checks; it does not manufacture a blanket local-data refusal.

<!-- example: glyport-unicode-error-order -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSApplication

class NoCoercion:
    def __str__(self):
        raise AssertionError("Do not stringify bridge inputs")
    def __index__(self):
        raise AssertionError("Do not coerce bridge inputs to integers")

class OwnedString(str):
    pass

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
class Recorder:
    def glyphInfoForUnicode_(self, value):
        return value
class ExplicitFont:
    def glyphsInfo(self):
        return Recorder()
    def __bool__(self):
        return False
for value in (None, [], 65, True, "", "\ud80000"):
    actual = app.glyphInfoForUnicode(value, font=ExplicitFont())
    if isinstance(value, int):
        assert actual == f"{value:04X}"
    else:
        assert actual is value
try:
    app.glyphInfoForUnicode("0041", font=False)
except AttributeError as error:
    assert "glyphsInfo" in str(error)
else:
    raise AssertionError("False is an explicit font object, not omitted font")
for value in (65.0, b"0041", [], NoCoercion(), OwnedString("0041")):
    try:
        app.glyphInfoForUnicode(value)
    except UnsupportedCapability as error:
        assert error.capability == "Glyphs.glyphInfoForUnicode.inputType"
    else:
        raise AssertionError("Unqualified bridge inputs must refuse")
```

<a id="exact-primary-lookup-precedes-raw-synthesis"></a>

## Exact combined-index lookup precedes raw synthesis

After the original-length gate, the uppercase text is the exact Unicode-index
key. There is no trimming, zero padding, prefix removal or numeric
canonicalization. Thus `004a` selects `J`, while `041` and `000041` miss `0041`
and synthesize their own raw names. Each source record contributes its
primary encodings, then its non-nil legacy encoding to the same index, in
record/file order; the last assignment wins. The parser/loader contract and
retained ARM instructions establish this ordering, rather than a new native run.

The pinned public glyphsLib 6.16.2 GlyphData snapshot has 74,247 records and
71,401 primary keys.
Its 730 distinct legacy keys produce 72,131 combined keys, with no overlap or
change to existing primary entries in this snapshot. The duplicated legacy key
`0000` belongs first to `.null`, then to `NULL`; lookup selects `NULL`.
`FE8D` selects `alef-ar.isol`, and `FE80` selects `hamza-ar.isol`. Their primary
Unicode remains `None`; a legacy hit never promotes its key into that field.
These public counts do not establish proprietary database completeness or the
same record set in every resource/version. Synthesis applies only after a true
combined-index miss.

<!-- example: glyport-unicode-primary-legacy -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
assert app.glyphInfoForUnicode("004a").name == "J"
for text, name in [("041", "uni041"), ("000041", "uni000041")]:
    info = app.glyphInfoForUnicode(text)
    assert (info.name, info.unicode, info.unicodeLegacy) == (name, text, None)
for text, name, primary, legacy in [
    ("FE8D", "alef-ar.isol", None, "FE8D"),
    ("FE80", "hamza-ar.isol", None, "FE80"),
    ("0000", "NULL", None, "0000"),
]:
    info = app.glyphInfoForUnicode(text)
    assert (info.name, info.unicode, info.unicodeLegacy) == (name, primary, legacy)
    named = app.glyphInfoForName(name)
    assert (named.name, named.unicode, named.unicodeLegacy) == (name, primary, legacy)
    assert info is named  # Canonical views of the same selected raw record.
assert app.glyphInfoForUnicode("fe8d").name == "alef-ar.isol"
assert app.glyphInfoForUnicode("U+0041") is None
assert app.glyphInfoForUnicode("0x41") is None
```

## Check original UTF16 length before uppercase expansion

None and text shorter than three UTF-16 code units return `None` before
uppercasing, lookup or parsing. Count UTF-16 units rather than Python code
points: a supplementary scalar occupies two. An uppercase expansion cannot rescue
a too-short input. `0ﬀ` returns None; `00ﬀ` becomes `00FF` and selects `ydieresis`;
`000ﬀ` becomes `000FF` and synthesizes.

Actual malformed UTF16 and hex text naming a surrogate are different domains.
After the minimum-length gate, malformed actual UTF16 refuses with `.UTF16`:
Foundation can return a NULL UTF8 pointer that the retained upstream helper
would dereference unchecked. Do not execute that native failure path. A shorter
lone surrogate returns None at the earlier length gate; valid surrogate pairs
are not rejected as malformed. Literal ASCII `D800` is accepted synthesis text.

<!-- example: glyport-unicode-utf16-gates -->
```python
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
for value in (None, "", "0", "00", "0ﬀ", "\ud800", "\ud8000", "😀0", "\ud83d\ude000"):
    assert app.glyphInfoForUnicode(value) is None
assert app.glyphInfoForUnicode("00ﬀ").name == "ydieresis"
assert app.glyphInfoForUnicode("000ﬀ").name == "uni000FF"
for value in ("\ud80000", "00\ud800", "\udc0000"):
    try:
        app.glyphInfoForUnicode(value)
    except UnsupportedCapability as error:
        assert error.capability == "Glyphs.glyphInfoForUnicode.UTF16"
    else:
        raise AssertionError("Unsafe malformed UTF16 must refuse")
assert app.glyphInfoForUnicode("D800").unicode == "D800"
```

Standalone macOS 27.2 Foundation calibration checked all 1,112,064 valid Unicode
scalars against Python 3.11 Unicode 14 uppercasing. There were 55 differences;
only non-ASCII `ﬀ` uppercased entirely into the parser alphabet, identically in
both systems. That establishes this measured parser-alphabet boundary. It does
not establish arbitrary Foundation-version equivalence, PyObjC conversion or
native font-workflow compatibility.

## Preserve the historical parser and raw encoding

On a combined-index miss, the retained helper scans ASCII hex in reverse. Spaces
contribute nothing; any minus sign requests final negation, regardless of its
position, and repeated minuses do not toggle the sign. Both are skipped without
advancing the nibble position. Other characters return sentinel `0x7FFFFFFF`,
which fails the manager’s range check. Nonempty spaces/minuses alone parse as zero.

Nibble contributions are **added** modulo 2³² with shifts `(4 * position) & 31`.
This differs from parsing an unlimited integer and truncating it: `100000000`
parses as 1 and `FFFFFFFFF` as 14. Signed values below `0x10000` use the `uni`
prefix; other accepted values use `u`. Signed high-bit patterns take the BMP
branch and bypass its upper-range guard. On the other branch, `10FFFE` passes
but `10FFFF` fails. This is not a strict Unicode scalar validator.

Names use that prefix plus the **uppercase original text**, not a reformatted
parsed integer. The synthesized primary encoding preserves the same text only
when its uppercase UTF16 length is 1–7. A longer valid record has `unicode=None`.
No encoding is assigned to a font by reading one of these snapshots.

<!-- example: glyport-unicode-raw-parser -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
for text in ("--41", "04-1", " 4 1 ", "   ", "---"):
    info = app.glyphInfoForUnicode(text)
    assert info.name == "uni" + text and info.unicode == text
for text in ("00000041", "80000000", "FFFFFFFF", "100000000", "FFFFFFFFF"):
    info = app.glyphInfoForUnicode(text)
    assert info.name == "uni" + text and info.unicode is None
assert app.glyphInfoForUnicode("10FFFE").name == "u10FFFE"
for text in ("10FFFF", "110000", "7FFFFFFF", "nothex"):
    assert app.glyphInfoForUnicode(text) is None
```

## Classify synthesis using historical ranges

Synthesized case is 0; subCategory and unicodeLegacy are None. Private Use gets
category `Private Use` and no script in exactly E000–F8FF, F0000–FFFFD and
100000–10FFFD. Otherwise the audited historical Han set gives script `han` and
category `Letter`; other synthesized records have script None and category
`Other`. Surrogate hex text, unassigned points, controls, punctuation and
noncharacters are not generally filtered out. Direct indexed entries retain
their maintained metadata and can mask these synthesis rules.

The Han intervals are the following hexadecimal **start/count** pairs; each
covers `[start, start + count)`. They describe retained source, not current Unicode
Script data:

| Start | Count | Start | Count |
| --- | --- | --- | --- |
| 2E80 | 1A | 2E9B | 59 |
| 2F00 | D6 | 3005 | 1 |
| 3007 | 1 | 3021 | 9 |
| 3038 | 3 | 303B | 1 |
| 3400 | 19B6 | 4E00 | 51CD |
| F900 | 16E | FA70 | 6A |
| 2F800 | 21E | 20000 | A6D7 |
| 2A700 | 1035 | 2B740 | DE |
| 2B820 | 1682 | 2CEB0 | 1D31 |
| 30000 | 134B | 1F200 | 100 |

The seven-digit spellings below force a combined-index miss so the historical
classification can be observed independently of canonical maintained entries.

<!-- example: glyport-unicode-historical-classification -->
```python
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSApplication

app = GSApplication(SimpleNamespace(font=None), object(), {}, None, lambda *args: None)
for value, script, category in [(0x9FCC, "han", "Letter"),
                                (0x9FCD, None, "Other"),
                                (0x3134A, "han", "Letter"),
                                (0x3134B, None, "Other"),
                                (0xF8FF, None, "Private Use")]:
    text = "%07X" % value
    info = app.glyphInfoForUnicode(text)
    assert (info.script, info.category) == (script, category)
    assert info.unicode == text and info.case == 0
    assert info.subCategory is None and info.unicodeLegacy is None
for value in (0xE000, 0xF0000, 0xFFFFD, 0x100000, 0x10FFFD):
    info = app.glyphInfoForUnicode(value)
    assert info.category == "Private Use" and info.script is None
```

## Keep acceptance boundaries explicit

Supported snapshot fields here are name, primary Unicode, separate legacy
Unicode, category, subCategory, script, case and supported component snapshots.
A synthesized record’s minimal fields do not qualify every Glyph Info property.
Maintained glyphsLib data is not proof of Glyphs’ proprietary database
completeness, the same record contents or Unicode version. Source-supported
index ordering alone does not qualify custom resource loading or replacement.
The [stored production guide](glyport-production.md) now describes the bounded
represented-record source contract; it remains separate from glyph production
write/export and application conversion. The retained production successor passes
both ordinary prefixes and the exact consumer checks; the checkpoint suffix-route
correction has separate source/archive evidence. The [compound guide](glyport-compounds.md)
now covers raw/shared/copy state and multi-record composition; its new ordinary
provider/consumer cohort remains pending. Private global overlays, font-local
managers, remaining fields and arbitrary bridge conversion remain unimplemented
or unqualified.

See [legacy Unicode and ROS](glyport-metadata.md) for legacy snapshots and the
proprietary ROS mapping refusal, [parameters and Arabic encodings](glyport-parameters.md)
for ordered font-local postprocessing, and the [Glyport package](../packages/glyport.md)
for the broader compatibility surface. Whole original scripts, native collisions,
history and saved/reopened workflows remain separate acceptance work. The
source-lock review, generated reference/site, archive/routes, browser/accessibility
and publication gates remain open; this authored candidate does not clear them.
