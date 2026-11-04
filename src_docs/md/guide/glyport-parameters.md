---
this_file: src_docs/md/guide/glyport-parameters.md
---

# Ordered parameters and Arabic presentation forms


The numerical ordinary-artifact results below identify their retained predecessor
checkpoint. The [current manager/profile guide](glyport-managers.md) documents
the H source changes. Earlier source assumptions are corrected below; original
preimages remain in verification evidence. Old receipts do not qualify the new
ordinary tuple or native behavior. Run the [owned graph setup](glyport-managers.md#prepare-an-owned-graph)
first for examples using `owned_parsed_manager`; those examples explicitly select
actual parsed owned data before a metadata refresh or rename.

Glyport's private candidate now preserves parameter order, duplicate names,
active flags and live parameter objects. Its Arabic presentation stage can append
legacy presentation-form encodings during an explicit metadata refresh. These
are source and installed-artifact capabilities; native FontLab history,
save/reopen and complete original-script workflows remain unqualified.

All examples below create owned `FakeBackend` data outside FontLab. They do not
open a font file, execute an original script, install a filter or change a live
FontLab document. Examples use public model operations except the clearly named
backend-storage diagnostic. They require the repaired candidate, not merely a
matching development-version label: [artifact identity](#candidate-identity-and-acceptance)
matters when several dirty builds share that label.

## Choose a value or an object

The same collection supports two different questions:

| Operation | Meaning |
| --- | --- |
| `parameters["Name"]` | Value of the first **active** matching parameter, or `None` |
| `"Name" in parameters` | A matching object exists, including an inactive one |
| `parameters[index]` | The actual ordered parameter object |
| `parameters["Name"] = value` | Change the first matching object, retaining its active flag; append if absent |
| `parameters["Name"] = None` | Remove the first matching object |
| `del parameters["Name"]` | Remove the first match; missing or empty names are a no-op |
| `parameters.remove(parameter)` | Remove that parameter object (by identity); `ValueError` if it is not in the collection |
| Indexed replacement/deletion | Replace/remove that position and detach the old object |

Do not treat name lookup as an ordinary dictionary when duplicates or inactive
entries matter. A name assignment can change an inactive object while a later
active duplicate still supplies the effective value.

<!-- example: glyport-ordered-parameters -->
```python
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
first = GSCustomParameter("Owned Setting", "first")
second = GSCustomParameter("Owned Setting", "second")
font.customParameters.extend([first, second])
assert font.customParameters[0] is first
assert font.customParameters["Owned Setting"] == "first"

first.active = False
assert "Owned Setting" in font.customParameters
assert font.customParameters["Owned Setting"] == "second"
font.customParameters["Owned Setting"] = "changed inactive object"
assert first.value == "changed inactive object" and not first.active
assert font.customParameters["Owned Setting"] == "second"

font.customParameters["Owned Setting"] = None
assert list(font.customParameters) == [second]
assert first.parent is None
first.value = "detached edit"
assert font.customParameters["Owned Setting"] == "second"
```

## Keep positional edits explicit

Insertion order is retained. `insert` uses strict bounds rather than clamping a
large positive or negative index. A negative index adds the current length once;
`insert(-1, parameter)` therefore inserts before the last item. Replacing or
removing an object detaches it, while the supplied replacement becomes live.

<!-- example: glyport-parameter-indexes -->
```python
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
first = GSCustomParameter("Owned duplicate", 1)
later = GSCustomParameter("Owned duplicate", 2)
font.customParameters.extend([first, later])
font.customParameters.remove(later)
assert list(font.customParameters) == [first]  # Removal is by object identity.
assert later.parent is None

before = GSCustomParameter("Before last", 3)
font.customParameters.insert(-1, before)
assert list(font.customParameters) == [before, first]
replacement = GSCustomParameter("Replacement", 4)
font.customParameters[-1] = replacement
assert first.parent is None and replacement.parent is font
try:
    font.customParameters.insert(99, GSCustomParameter("Outside", 0))
except IndexError:
    pass
else:
    raise AssertionError("Out-of-range insertion must not clamp silently")
```

Iteration captures the initial count and fetches each object as it advances.
Appending does not extend an existing iterator; shrinking the collection can
make its next indexed access raise `IndexError`. Finish iteration before editing
its structure, or collect the intended positions first. Nested mutation of an
attached value container is not a qualified notification route; assign the whole
replacement value instead. Same-object multiple insertion, cross-owner
reparenting and complete native identity remain open. A copied parameter owns
its nested value but retains its recorded parent pointer; a copy is not proven
to be a detached native object.

## Separate font, master and user data

A font and its masters have distinct parameter collections. Ordinary master
`userData` excludes reserved parameter storage and preserves it when other user
data changes. The presentation setting is read from the glyph's parent **font**;
a master parameter does not enable the font setting.

<!-- example: glyport-parameter-master-isolation -->
```python
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
master = font.masters[0]
master.userData["Owned note"] = {"tags": ["proof"]}
font.userData["Owned font data"] = 7
master.customParameters.append(GSCustomParameter("Owned Setting", "master"))
font.customParameters.append(GSCustomParameter("Owned Setting", "font"))
assert master.customParameters["Owned Setting"] == "master"
assert font.customParameters["Owned Setting"] == "font"
assert dict(master.userData) == {"Owned note": {"tags": ["proof"]}}
master.userData["Another note"] = 8
assert master.customParameters["Owned Setting"] == "master"
assert dict(font.userData) == {"Owned font data": 7}
```

The persistence representation uses ordered records and compatible flat-key
mirrors. Old flat values import in their former sorted order because the old
format recorded no original insertion order or active flags. New external flat
names are retained. An external edit or deletion of an existing mirrored value
wins: the collection follows the flat keys, reads never raise, and one
`CUSTOM_PARAMETERS_REBUILT` warning is queued.

This storage diagnostic reconstructs a Python model over the same owned backend.
It is not a native font save/reopen test:

<!-- example: glyport-parameter-legacy-storage -->
```python
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend
from fontlab_glyport.model.proxies import CUSTOM_PARAMETER_PREFIX

backend = FakeBackend()
# "font" is this test backend's owned font identity, not a native font ID.
backend.set_lib("font", {
    CUSTOM_PARAMETER_PREFIX + "Z owned": [1],
    CUSTOM_PARAMETER_PREFIX + "A owned": 2,
    "unrelated": {"keep": [3]},
})
font = Model(backend).font
assert [p.name for p in font.customParameters] == ["A owned", "Z owned"]
font.customParameters.append(GSCustomParameter("A owned", 4))
font.customParameters[0].active = False
reconstructed = Model(backend).font
assert [(p.name, p.active) for p in reconstructed.customParameters] == [
    ("A owned", False), ("Z owned", True), ("A owned", True)
]
assert reconstructed.customParameters["A owned"] == 4
assert backend.lib("font")["unrelated"] == {"keep": [3]}
```

## Enable Arabic presentation encodings

The exact key is **`Use Arabic Presentation Form Unicodes`**, including its
spaces and case. `UseArabicPresentationFormUnicodes` is a different key. Prefer
an explicit Boolean for a setting; raw Python truthiness does not describe the
upstream string-conversion rules.

<!-- example: glyport-arabic-presentation -->
```python
from fontlab_glyport.model import GSCustomParameter, GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

KEY = "Use Arabic Presentation Form Unicodes"
font = Model(FakeBackend()).font
font.parent._local_glyph_info = owned_parsed_manager()
glyph = font.glyphs.append(GSGlyph("alef-ar"))
font.masters[0].customParameters[KEY] = True
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0627"]  # A master setting does not enable it.

font.customParameters[KEY] = True
glyph.updateGlyphInfo(changeName=False)
assert glyph.name == "alef-ar"
assert glyph.unicodes == ["0627", "FE8D"]
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0627", "FE8D"]  # Ordered deduplication.
font.customParameters[KEY] = False
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0627"]  # Refresh removes the previous addition.
```

The ordinary additional-Unicode helper and this presentation stage are separate.
The former has its own gates and uses ordinary `.isol.unicode`; legacy-only
`.isol` data does not become a primary encoding just because that helper ran.
Presentation instead reads `unicodeLegacy`. A separately named `.isol` glyph can
block the earlier helper's manager lookup without blocking the presentation
stage's raw legacy lookup.

### Direct, nil and empty legacy data

The stage tests the **resolved record's** script, then uses its canonical name.
A direct non-nil `unicodeLegacy` takes precedence. Only nil triggers a raw
`<resolved name>.isol` database lookup. An empty string is non-nil: it blocks
fallback, then adds no encoding. Additions retain order, deduplicate and follow
the upstream nonempty/shorter-than-eight length gate. Generic constructed
suffixes clear inherited legacy; direct database suffix records retain their own.

Implemented ordering is resolution/private-use handling, the ordinary
additional-Unicode helper, ROS processing, presentation processing, then stored
metadata overlays. Requests for the five proprietary shipped ROS maps now refuse
before presentation and metadata writes because their mapping data is unavailable.
Malformed/unknown text leaves this stage unchanged under the audited shared-bundle
contract. See the [legacy and ROS guide](glyport-metadata.md) for exact delimiters,
supplement handling, nontext refusal and owned no-write examples. Full ROS mapping,
complete local initialization/private resources and unqualified suffix routes
remain outside this bounded example matrix.

A stored Latin script does not suppress presentation on an Arabic resolved
record; the overlay runs later. Conversely, storing Arabic script on a Latin
resolved record does not make it an Arabic presentation candidate.

<!-- example: glyport-arabic-stored-overlay -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

KEY = "Use Arabic Presentation Form Unicodes"
font = Model(FakeBackend()).font
font.parent._local_glyph_info = owned_parsed_manager()
alias = font.glyphs.append(GSGlyph("OwnedArabicAlias"))
alias.unicode = "0627"
alias.storeScript = True
alias.script = "latin"
font.customParameters[KEY] = True
alias.updateGlyphInfo(changeName=False)
assert alias.name == "OwnedArabicAlias" and alias.script == "latin"
assert alias.unicodes == ["0627", "FE8D"]
```

Resetting a storage flag refreshes that metadata field without writing
encodings. The next explicit refresh can apply presentation encodings. Native
name-collision adjustment is a separate open route: it can clear encodings even
with `changeName=False`. The no-conflict examples do not prove that route.

<!-- example: glyport-arabic-reset-and-refresh -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

KEY = "Use Arabic Presentation Form Unicodes"
font = Model(FakeBackend()).font
font.parent._local_glyph_info = owned_parsed_manager()
glyph = font.glyphs.append(GSGlyph("alef-ar"))
glyph.storeScript = True
glyph.script = "latin"
font.customParameters[KEY] = True
glyph.storeScript = False
assert glyph.script == "arabic" and glyph.unicodes == ["0627"]
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0627", "FE8D"]
```

## Read typed values on macOS

For this exact BOOL-schema key, plain Python `bool`, `int` and `float` retain their
numeric type and precision; `None` on the object becomes `False`. Assigning
`None` by parameter name still removes the first matching object. A string
containing the current locale's decimal separator uses real NSNumberFormatter
parsing, then float32. Other strings use NSString.integerValue. The default
formatter is process-cached; an explicit locale below owns a temporary formatter
and changes no global preferences.

| Input and route | Result | Enables presentation? |
| --- | --- | --- |
| Numeric `0.5` | Retained `0.5` | Yes |
| Numeric `1e-46` | Retained double precision | Yes |
| String `"YES"` or `"true"` | Integer `0` | No |
| String `"1e-3"` without the decimal separator | Leading integer `1` | Yes |
| String `"1.0e-46"`, dot-decimal locale | Float32 `0.0` | No |
| String `"0,5"`, comma-decimal locale | Float32 `0.5` | Yes |
| Malformed decimal `"0.5junk"`, dot-decimal locale | Nonzero float `2**63` sentinel | Yes |

The failed-parse sentinel is an upstream quirk established by retained machine
code and independent Foundation observations. It is not a recommendation to use
malformed input. Guessing `bool(text)` or treating every parse failure as zero
would change the setting's behaviour.

<!-- example: glyport-parameter-numeric-macos -->
```python
from fontlab_glyport.model import GSCustomParameter, Model
from fontlab_glyport.model.fake_backend import FakeBackend
from fontlab_glyport.model.parameter_numbers import normalize

assert normalize("YES", locale_name="en_US") == 0
assert normalize("true", locale_name="en_US") == 0
assert normalize("0,5", locale_name="de_DE") == 0.5
assert normalize("1.0e-46", locale_name="en_US") == 0.0
assert normalize(1e-46) == 1e-46
assert normalize("0.5junk", locale_name="en_US") == float(2**63)

KEY = "Use Arabic Presentation Form Unicodes"
font = Model(FakeBackend()).font
parameter = GSCustomParameter(KEY, True)
font.customParameters.append(parameter)
parameter.value = None
assert parameter.value is False and len(font.customParameters) == 1
font.customParameters[KEY] = None
assert len(font.customParameters) == 0
```

This string route is measured on macOS 27.2 arm64 Foundation, not every Foundation
version. Non-macOS strings and arbitrary object/container conversions explicitly
raise `UnsupportedCapability`; their implementation/qualification remains open.
Existing numeric NaN retains numeric enabling semantics and must not be mistaken
for an external mirror conflict. Active-value cache construction validates all
active duplicates, including shadowed ones. Indexed/name/active inspection and name-based removal remain available for an
inactive imported value whose conversion is unsupported. Name membership is a
separate object lookup that can still validate the first matching object; it is
not a substitute for those recovery operations.

## Candidate identity and acceptance

These authored examples require the current private source/ordinary-artifact
candidate. Several uncommitted builds can share one hatch-vcs version string;
use its wheel/sdist hashes and byte/origin audit to identify the tested tuple.
Historical hashes on the [Glyport package page](../packages/glyport.md) remain
historical and are not silently updated to identify this candidate.

The parameter and presentation source suites, fresh wheel/sdist checks and
measured Foundation conversion establish bounded offline behaviour. They do not
establish native history, complete font/UI/cache/dirty preservation, save/reopen,
original-script acceptance, canonical promotion or a published release. The public
`GSGlyphInfo.unicodeLegacy` field now exposes owned read-only legacy snapshots,
separately from primary Unicode. The [metadata guide](glyport-metadata.md) explains
the global factory, namespace snapshots and actual model-glyph constructor route;
read-only is package policy, not a claim about native Glyph Info setters.
The shared global index now resolves legacy keys as well as primary keys, while
keeping both returned fields separate. See the [global Unicode guide](glyport-unicode.md)
for record-order replacement and the corrected `FE8D`/`0000` examples. All 24 owned
examples across these three guides now pass in the corrected ordinary six-wheel
cohort; installed origins and current Echopy producer provenance are checked,
and all 701 runtime/data files match byte for byte. The same exact tuple passes 4,481 Scriptmix tests with
1 existing selection-read skip and 2,436 Examples tests without skips. Exact current
hashes are recorded on the existing package page linked above; earlier hashes
continue to identify their historical stages.

The central site's generated source lock, rendered pages, browser accessibility,
archive/routes and publication gates remain open. This authored page is not
proof of a generated or deployed page. Continue with the [general Glyphs
compatibility guide](glyphs.md) or the [Glyport package reference](../packages/glyport.md).
