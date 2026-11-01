---
this_file: src_docs/md/packages/glyport.md
---
# Glyport

Glyport runs Glyphs scripts and plugins inside FontLab. It inspects and adapts
the original source (including Glyphs 2 / Python 2 code), gives each run a live
`GlyphsApp` model backed by the FontLab font, and translates Vanilla, AppKit and
NIB/XIB interfaces to FontLab's Qt. Original files are never modified.

The detached-transform examples below were checked with the ordinary development
artifact `1.0.8.dev58+g753b55548` and App `0.2.26.dev159+gb1e905b61`. They do not
claim a published release or qualify native FontLab behavior. Older packages may
not have the same input checks or overflow preflight.

## Install

Install `fontlab-glyport` into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab). Its inspection API also
works outside FontLab.

## Quick start

Assess a script without running it:

<!-- example: glyport-inspect -->
```python
from fontlab_glyport import inspect_source

assessment = inspect_source("OriginalScript.py")
print(assessment.required_capabilities)
```

Run a Glyphs script inside FontLab:

```python
# Inside FontLab
from fontlab_glyport import run_script

handle = run_script("OriginalScript.py")      # profile chosen from the source
print(handle.state, handle.receipt)
handle.close()
```

## Examples

Install a plugin bundle and remove it again:

```python
from fontlab_glyport import install_plugin

plugin = install_plugin("MyReporter.glyphsReporter")
# ... the reporter now draws in the Glyph window ...
plugin.unload()                                # removes every registration
```

Adapt Glyphs 2 source into an owned cache, keeping a map back to original lines:

<!-- example: glyport-adapt -->
```python
from fontlab_glyport import adapt_source

adapted = adapt_source("OldScript.py", profile="glyphs2", cache_dir=".glyport-cache")
code = adapted.compile()           # compiles; does not execute
print(adapted.translate(1, 1))     # generated position -> original position
```

## Work with detached geometry

These examples run outside FontLab. They create Python-owned draft objects and
change no open font. They demonstrate Glyport's arithmetic and object semantics;
they do not test copying a native layer, native rounding, Undo or saved fonts.

### Apply one affine matrix

The six values `(a, b, c, d, tx, ty)` map a point as
`x_new = a*x + c*y + tx`, `y_new = b*x + d*y + ty`. This example changes a path
and an anchor on an owned detached layer. It does not resolve components or
measure a native layer's bounds.

<!-- example: glyport-detached-transform -->
```python
from fontlab_glyport.model import GSAnchor, GSNode, GSPath
from fontlab_glyport.model.copies import DetachedLayer

layer = DetachedLayer()
layer.paths = [GSPath([GSNode((2, 3)), GSNode((-4, 5))])]
layer.anchors = [GSAnchor("top", (11, 19))]
layer.applyTransform((2, 1, 3, 4, 5, 6))

assert [tuple(node.position) for node in layer.paths[0].nodes] == [
    (18, 20), (12, 22)
]
assert tuple(layer.anchors[0].position) == (84, 93)
```

Composition order matters. A clockwise rotation followed by one combined
scale/shear matrix differs from scale, then shear, then counterclockwise rotation.
Do not use a similarly named menu as proof that two scripts implement the same
transform, layer scope or component policy.

### Reject invalid coefficients and overflow before writing

Layer/path transform entry points reject NaN and infinity before backend calls,
history or geometry mutation. Finite zero and negative scales retain their
existing behavior; this check does not forbid flattening or reflecting geometry.

<!-- example: glyport-nonfinite-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

path = GSPath([GSNode((2, 3))])
before = [tuple(node.position) for node in path.nodes]
try:
    path.applyTransform((float("nan"), 0, 0, 1, 0, 0))
except ValueError as error:
    print(error)
else:
    raise AssertionError("The non-finite matrix should be refused.")
assert [tuple(node.position) for node in path.nodes] == before
```

Finite coefficients can still overflow when multiplied by a large coordinate.
Python-managed paths, detached layers and selection-aware layer transforms
calculate all results before entering history or writing. A failure on a later
point therefore leaves earlier points untouched:

<!-- example: glyport-overflow-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

path = GSPath([GSNode((2, 3)), GSNode((1e308, 5))])
before = [tuple(node.position) for node in path.nodes]
try:
    path.applyTransform((2, 0, 0, 2, 13, -7))
except ValueError as error:
    print(error)
else:
    raise AssertionError("The overflowing result should be refused.")
assert [tuple(node.position) for node in path.nodes] == before
```

This is arithmetic preflight, not a transaction. Setter failures after preflight,
native coordinate conversion, and the native whole-layer transform remain outside
that guarantee. The native layer route calls FontLab's `flLayer.applyTransform`;
it must not be assumed to preserve metrics and guides like the detached example.

### Repeated objects are transformed per occurrence

The following deliberate alias illustrates draft-object identity. It is not a
recommendation to create duplicate nodes in a font. Each occurrence uses the
previous virtual result, so two factors of two give a factor of four. If a later
occurrence overflows, preflight refuses the operation before the first write.

<!-- example: glyport-repeated-transform -->
```python
from fontlab_glyport.model import GSNode, GSPath

node = GSNode((2, 3))
path = GSPath([node, node])
path.applyTransform((2, 0, 0, 2, 0, 0))
assert tuple(node.position) == (8, 12)
```

This identity rule covers the same draft object and ordinary cached live proxies.
It does not prove equivalent behavior for distinct wrappers sharing external
storage. A script that repeats a parent glyph may also need to recompute each
layer's bounds between visits; repeatedly applying one fixed matrix is not a
substitute for that workflow.

## Distinguish layer names from layer identity

A layer's name is not its identifier. Ordinary auxiliaries have their own
`layerId` and an `associatedMasterId`; a missing name must not make an auxiliary
look like its master. Use the ID to address a layer, and keep the raw name when
checking a source script's condition. Converting it with `str()` turns `None`
into the text `"None"`; `if not layer.name` also matches an empty string.

| Layer | Raw `name` | `isMasterLayer` | Matches `name is None and not isMasterLayer` |
| --- | --- | --- | --- |
| Master | Master name | `True` | No |
| Unnamed auxiliary | `None` | `False` | Yes |
| Empty-string auxiliary | `""` | `False` | No |
| Named auxiliary | `"Backup"` | `False` | No |

The following diagnostic fixture runs outside FontLab. `FakeBackend` is a test
double, not a font importer. It supplies the three auxiliary name values to the
same proxy model used by Glyport. The example reads every glyph, keeps names
unmodified and collects matching identities without deleting anything.

<!-- example: glyport-auxiliary-names -->
```python
from fontlab_glyport.model import Model
from fontlab_glyport.model.backend import LayerInfo
from fontlab_glyport.model.fake_backend import FakeBackend

backend = FakeBackend()
for identity, name in [("unnamed", None), ("empty", ""), ("backup", "Backup")]:
    backend.layers["glyph", identity] = LayerInfo(
        id=f"layer-{identity}", masterId="master", width=500,
        layerId=identity, name=name,
    )

font = Model(backend).font
layers = list(font.glyphs[0].layers)
assert [layer.name for layer in layers] == ["Regular", None, "", "Backup"]
assert [layer.isMasterLayer for layer in layers] == [True, False, False, False]
assert layers[1].associatedMasterId == layers[0].layerId
assert font.glyphs[0].layers["unnamed"] is layers[1]
assert layers[1].copy().name is None

matches = [
    (glyph.name, layer.layerId)
    for glyph in font.glyphs
    for layer in glyph.layers
    if layer.name is None and not layer.isMasterLayer
]
assert matches == [(font.glyphs[0].name, "unnamed")]
```

All fixture layers have empty geometry, but only the absent-name auxiliary
matches. The condition describes a missing name, not an empty outline. It also
has whole-font scope; substituting selected glyphs changes the workflow.

This example was verified with the private, uncommitted development artifact
`1.0.8.dev58+g753b55548.d20261101`. The earlier clean artifact
`1.0.8.dev58+g753b55548` fails the raw-name assertion: its proxy substitutes the
master name for both `None` and `""`. Master and background naming retain their
existing behavior in the repaired candidate. This is not a published release.

The fixture does not show whether FontLab's importer preserves a Glyphs `None`
name or converts it to an empty string. Do not use this filter as a qualified
native deletion script. Removing layers additionally requires preservation of
locks, active layers, automatic dependants, history and saved/reopened payloads.
Those native workflows remain unverified. The broader Layer Cleanup menu has
its own explicit selection and layer-kind behavior; it is not an equivalent
implementation of this predicate.

## Query glyph metadata without copying the current encoding

A glyph's stored Unicode is editable font data. A name-based Glyph Info lookup
asks for database metadata. These differ when a glyph has been re-encoded: a
script that resets Unicode cannot use the current encoding as its reference.

For name strings, the candidate `Glyphs.glyphInfoForName(name)` queries
glyphsLib’s global fallback without reading the active font. Passing `font=None`
does the same. An explicit non-None font raises
`Glyphs.glyphInfoForName.localData`, because document-local GlyphData is not
implemented. Integer inputs, including bool and int subclasses, dispatch first
to `self.glyphInfoForUnicode(name)` and discard the font argument.
The [global Unicode guide](../guide/glyport-unicode.md) covers the executable
`String` keyword, percent formatting, override preservation and direct Unicode
local-data refusal precedence.

This diagnostic fixture runs outside FontLab. It instantiates the application
facade with owned model/bridge doubles; it does not activate GlyphsApp, load a
native host or edit an open font. The deliberately incorrect encoding on `A`
remains untouched after the query.

<!-- example: glyport-global-glyph-info -->
```python
from types import SimpleNamespace

from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp.application import GSApplication

current_glyph = SimpleNamespace(
    name="A", unicode="0042", category="Symbol", subCategory=None, script="custom-script", case=2, layers=[],
)
current_font = SimpleNamespace(glyphs={"A": current_glyph})
model = SimpleNamespace(font=current_font)
# This fixture never calls bridge methods or reads/writes persistent defaults.
app = GSApplication(model, object(), {}, None, lambda *args: None)

info = app.glyphInfoForName("A")
assert info.unicode == "0041", "Name-derived data must not copy current encoding"
assert info.category == "Letter"
assert info.script == "latin"
assert current_glyph.script == "custom-script", "A lookup must not edit script metadata"

# Filter by database script metadata; an unassigned script remains None.
names = ["A", "Alpha", "alpha", "acutecomb"]
greek = [name for name in names if app.glyphInfoForName(name).script == "greek"]
assert greek == ["Alpha", "alpha"]
assert app.glyphInfoForName("acutecomb").script is None
# Case is a database enum: upper=1, lower=2, not a Unicode category.
case_names = ["A", "a", "exclam", "less", "acutecomb"]
upper = [name for name in case_names if app.glyphInfoForName(name).case == 1]
lower = [name for name in case_names if app.glyphInfoForName(name).case == 2]
assert upper == ["A", "exclam"]
assert lower == ["a", "less", "acutecomb"]
assert app.glyphInfoForName("acutecomb").category == "Mark"
assert current_glyph.case == 2, "A lookup must not edit case metadata"
assert app.glyphInfoForName("A", font=None).unicode == "0041"
assert current_glyph.unicode == "0042", "A lookup must not edit the glyph"

try:
    app.glyphInfoForName("A", font=current_font)
except UnsupportedCapability as error:
    assert error.capability == "Glyphs.glyphInfoForName.localData"
else:
    raise AssertionError("Font-local GlyphData is not implemented")
```

The read-only `script` field snapshots metadata supplied by the database. This
example uses it to select Greek names without changing the font. An unassigned
script stays `None`; do not treat that as a missing glyph or invent a script from
its Unicode.

The read-only `case` field also snapshots database metadata. Its values are
no-case (0), upper (1), lower (2), small-caps (3), minor (4) and other (5).
They are not Unicode general categories: `exclam` has upper case metadata,
while `less` and the combining mark `acutecomb` have lower case metadata.
Missing case metadata maps to no-case; an unknown label raises an unsupported
capability error. Other Glyph Info fields remain incomplete.

This fixture needs the private global-lookup, script-field and case-field repairs.
Several uncommitted builds share `1.0.8.dev58+g753b55548.d20261101`; version text
alone does not identify them. The earlier lookup-only build raises an unsupported
attribute error at `info.script`; the later script-only build fails at the first
`.case` read. These archives are not published releases.

Tested private archive SHA256 values:

| Archive | SHA256 |
| --- | --- |
| Wheel | `f174ab43d51c83dd1115e1509bd5920db5bee77cf771bffe1ca98fca8f8d3679` |
| sdist | `64793db733288cef3131f14e47ff9b1074425d6f5e82487ceb62bcf353242eb6` |

The fallback does not load Glyphs’ custom global GlyphData overlays. Name-based
unknown-name results and full `GSGlyphInfo` records also remain incomplete.
The new global Unicode route has its own audited raw-spelling synthesis; it does
not establish arbitrary name-factory synthesis or proprietary data completeness.
This example qualifies the default lookup's independence from font data, not
complete Glyphs database equivalence or a native Unicode-reset workflow. The
[legacy Unicode and ROS guide](../guide/glyport-metadata.md) covers the newer
`GSGlyphInfo.unicodeLegacy` snapshot, canonical aliases and active-font isolation.
Legacy Unicode remains separate from the primary encoding. The corrected source
candidate implements
[`Glyphs.glyphInfoForUnicode(String, font=None)`](../guide/glyport-unicode.md)
with exact uppercase lookup in the shared primary/legacy index, followed by
source-backed synthesis only on a miss. In source order each record contributes
primary keys then its legacy key; later assignments win. `FE8D` selects
`alef-ar.isol` with primary Unicode `None`, and duplicated `0000` selects `NULL`.
The corrected ordinary six-wheel cohort passes all 24 owned examples across the
parameter, metadata and Unicode guides, with installed origins checked. All 701
runtime/data files match byte for byte before and after consumer execution. It passes 4,481 Scriptmix tests
with 1 existing skip (`Spacing Preview has no selection read`) and 2,436 Examples
tests without skips;69 original Scriptmix hashes are independently audited.
The corrected Glyport wheel SHA256 is
`607ed7a0417120dd12f486ee9fc72f0d2ddbb78bbd2a6242ecdf79897a68cc20`.
The current Echopy wheel SHA256 is
`8f74fa6ae7d9041103d6516c1360bd66a412e7f12333142153a09bca83342fc7`;
its sdist SHA256 is
`e678a77c6178894dfe4f7b363825999e39ae166feec83d95a5af24d85e88ed7d`.
The exact six-wheel tuple is:

| Package | Version | Wheel SHA256 |
| --- | --- | --- |
| fontlab-fly | `0.2.3.dev7+g42d106154` | `191b1daff6ac075c84737a5b377e97aecbc94eb7a7338530e941b1e864ec7eb6` |
| fontlab-fontlabapp | `0.2.26.dev332+g73011d1ee` | `f31a76c7450a1c75f5412c243c2aa1facfaa9905de3fa2f1c0dd83b29acf5716` |
| fontlab-fontport | `1.0.3.dev23+gcdf5200cc` | `294d0e66d992db651aaa1d1c00c4d9c849145cc7e7bf368b676e7102005e0c1c` |
| pythonqtside | `0.2.2.dev2+g52d226291` | `27e49b526266e5a924d463cddeffacfb1bbd7fe690e4ebb230d8daa77dd91c6f` |
| fontlab-glyport | `1.0.8.dev182+g94d4226dc.d20261101` | `607ed7a0417120dd12f486ee9fc72f0d2ddbb78bbd2a6242ecdf79897a68cc20` |
| fontlab-echopy | `0.2.4.dev9+gac22b37ea.d20261101` | `8f74fa6ae7d9041103d6516c1360bd66a412e7f12333142153a09bca83342fc7` |

The other four wheels and 40 third-party pins are unchanged. Independent ordinary
wheel and complete 144-member-sdist installs each pass 32 isolation checks,
356 Echopy tests,388 Glyport feature tests and14package examples, with project
origins confined to each installed prefix. A standard build from the extracted
sdist reproduces the source wheel byte-for-byte. All 13 Echopy producer catalogues
match current source; only GlyphsApp shim provenance changes at runtime, with
all 124 protected declarations/exports unchanged. This is producer refresh, not
a new FontLab 9.0.9801 capture. Earlier archive hashes and results stay historical.
Remaining fields, bridge conversion, local managers and native workflows remain
separate acceptance boundaries. The
[upstream lookup contract](https://docu.glyphsapp.com/#GSApplication.glyphInfoForName)
describes the optional font-local database behavior still to implement.

## Preserve a glyph's case override

`GSGlyph.case` is mutable glyph metadata; `GSGlyphInfo.case` above is a read-only
database snapshot. A glyph can have a temporary case value while `storeCase` is
false. Setting that flag to true preserves the current value through supported
name changes and metadata refreshes. Setting an attached glyph's flag from true
to false restores its database default. Assigning false when it is already false
leaves a temporary value intact.

The following owned fixture runs outside FontLab. It demonstrates the same
minor-figure predicate used by kerning scripts, then changes case without editing
an open font. `FakeBackend` supplies the attachment target; it is not a font file.

<!-- example: glyport-case-lifecycle -->
```python
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

names = ["A", "ordfeminine", "one"]
assert [name for name in names if GSGlyph(name).case == 4] == ["ordfeminine"]

glyph = GSGlyph("f_f_i")
assert glyph.case == 2
glyph.case = 3
assert glyph.storeCase is False
glyph.storeCase = False
assert glyph.case == 3  # An unchanged flag does not refresh metadata.

font = Model(FakeBackend()).font
font.glyphs.append(glyph)
assert glyph.case == 3  # Unique attachment retains the temporary value.
glyph.storeCase = True
glyph.name = "less"
assert glyph.case == 3  # The stored value survives this name change.
glyph.storeCase = False
assert glyph.case == 2  # Attached reset restores the database classification.

copied = glyph.copy()
copied.storeCase = True
copied.case = 5
assert glyph.case == 2
try:
    copied.storeCase = False
except UnsupportedCapability as error:
    assert error.capability == "GSGlyph.storeCase.detachedReset"
else:
    raise AssertionError("Detached reset is not yet qualified")
assert (copied.case, copied.storeCase) == (5, True)
```

Detached true-to-false reset currently refuses before mutation; its upstream
manager behavior still needs qualification. Custom global/font-local databases,
synthesized names and complete `updateGlyphInfo` behavior remain incomplete.
That historical candidate refused unknown-name updates. This fixture does not prove
native history, saved/reopened metadata or complete kerning-script workflows.

The lifecycle candidate uses the same private development version as the earlier
case-field build above. These new archive hashes identify the added behavior:

| Archive | SHA256 |
| --- | --- |
| Wheel | `4054cafb86a86559711361314f9ea0f29812e1b05ee8c985cdc56134a6bc2633` |
| sdist | `8ea0e2ba569df0a662fbc0da17f0a36a48591c333449867891bb931ecce1288e` |

## Preserve a glyph's script override

`GSGlyph.script` reads named-glyph metadata, including for unencoded glyphs.
Assignment changes the current value without enabling `storeScript`. An enabled
flag preserves the value through supported name changes and refreshes. Disabling
it on an attached glyph restores the database default. An already-false flag
leaves a temporary assignment intact. `None` and an empty string are distinct
explicit values.

This owned fixture runs outside FontLab. It exercises the draft-before-append
pattern used by script builders, followed by a stored override and reset.

<!-- example: glyport-script-lifecycle -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
glyph = GSGlyph("f_f")
assert glyph.script == "latin"
glyph.script = "Rovas"
glyph.storeScript = False
assert glyph.script == "Rovas"
font.glyphs.append(glyph)
assert glyph.script == "Rovas"

glyph.storeScript = True
glyph.name = "Alpha"
assert glyph.script == "Rovas"
glyph.storeScript = False
assert glyph.script == "greek"

glyph.script = None
assert glyph.script is None  # Explicit None does not fall back to Greek.
copied = glyph.copy()
assert copied.script is None
copied.script = ""
assert copied.script == "" and glyph.script is None
copied.name = "A-cy"
assert copied.script == "cyrillic"  # A known name refreshes unstored metadata.
```

Detached true-to-false reset refuses before mutation, as with case metadata.
Custom metadata managers, synthesized names, complete original-script workflows,
native Undo/Redo and saved/reopened metadata remain unqualified. The fixture uses
an owned backend double and does not edit any font file.

The script-lifecycle candidate retains version `1.0.8.dev58+g753b55548.d20261101`.
These hashes distinguish it from the earlier case-only artifacts:

| Archive | SHA256 |
| --- | --- |
| Wheel | `383ab1378bcea5e60034ba3548348d19d46734efb2e1a64f5a9bef641ccaafdc` |
| sdist | `9218f4a61318f3cccb895e53b479711c60ce056858eecfba5097e75fe3715580` |

### Classification and shared resolver

The source candidate now supports independent `category`, `subCategory`,
`storeCategory` and `storeSubCategory` values. Classification accepts strings,
including the empty string, or `None`. Assigning Unicode alone does not refresh
classification. Turning an enabled storage flag off refreshes only that field;
a flag already off is a no-op. Detached resets remain explicitly unsupported.

Case, script and classification resets share Unicode-first resolution. For an
`A` encoded as `0061`, case resets to lowercase; for `0A15`, script resets to
Gurmukhi. The first resolvable encoding wins, including synthesized metadata:
an unassigned `0378` prevents a later `0A15` from supplying Gurmukhi metadata,
while `10FFFF`, which yields no record, allows the next encoding to be tried.
The `Icon` and `SF-Symbol` categories use the audited keep-name path.

This owned example exercises the shared resolver without opening FontLab:

<!-- example: glyport-classification-resolver -->
```python
from fontlab_glyport.model import Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
glyph = font.glyphs["A"]
glyph.unicodes = ["0061"]
glyph.category = "Symbol"
glyph.storeCategory = True
glyph.case = 3
glyph.storeCase = True
glyph.storeCase = False
assert glyph.case == 2  # Unicode metadata wins over the name A.
assert glyph.category == "Symbol" and glyph.storeCategory
glyph.storeCategory = False
assert glyph.category == "Letter"
assert glyph.name == "A" and glyph.unicodes == ["0061"]
```

These are owned offline checks against retained upstream analysis, not native
measurements. Custom data, full ROS mapping, complex small-cap mapping and language suffixes remain
unqualified. The current private parameter/presentation update is described in
the [ordered parameter guide](../guide/glyport-parameters.md). Additional encodings now follow the
audited helper gates; native workflow acceptance remains open. Earlier artifact hashes and examples above identify their
historical, narrower candidates; they do not identify this source revision.


### Additional encodings during refresh

Refreshing an attached uppercase glyph can add its lowercase encoding when no
other glyph owns that code. `I` can also gain dotless i; each ownership check is
independent. Refresh applies the resolved metadata’s encoding list plus these
additions; it does not preserve every arbitrary previous glyph encoding.
Additions preserve the resolved list’s order and do not duplicate its entries.
This uses the glyph's current case/script, including temporary overrides, before
stored metadata overlays. Resetting a storage flag does not write encodings.

The owned example below runs without FontLab:

<!-- example: glyport-additional-unicode -->
```python
from fontlab_glyport.model import GSGlyph, Model
from fontlab_glyport.model.fake_backend import FakeBackend

font = Model(FakeBackend()).font
glyph = GSGlyph("I")
font.glyphs.append(glyph)
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0049", "0069", "0131"]
glyph.updateGlyphInfo(changeName=False)
assert glyph.unicodes == ["0049", "0069", "0131"]  # No duplicates.

other_font = Model(FakeBackend()).font
other_font.glyphs.append(GSGlyph("i"))
capital = GSGlyph("I")
other_font.glyphs.append(capital)
capital.updateGlyphInfo(changeName=False)
assert capital.unicodes == ["0049", "0131"]  # Another glyph owns ordinary i.
```

Greek-script expansion requires both Phi and Sigma encodings in the font.
U+0130 and the audited out-of-range sentinel bypass expansion. Ordinary rename
and explicit refresh remain distinct: rename clears non-PUA encodings before
resolution, while a subsequent refresh can add encodings. Parentless glyphs and
keep-name categories have separate audited branches. The retained parentless
Arabic branch can yield no metadata; it is not equivalent to attached refresh.
Legacy-only Arabic .isol data does not become primary Unicode automatically.

The bundled Unicode17 scalar mapping matches actual NSString.lowercaseString
for all1,112,064 valid scalars on macOS27.2. Python3.11 casing differs on55scalars.
This pins that measured casing contract, not all Foundation versions. The
public data and licence ship with the package; no Objective-C bridge is loaded
for this operation. Native history/reopen, custom managers and full ROS mapping remain unqualified. The newer
source/artifact-tested Arabic presentation stage is described in the
[ordered parameter guide](../guide/glyport-parameters.md); it does not establish
native font-workflow acceptance.


## Ordered parameters and Arabic presentation forms

The current private candidate preserves ordered duplicate parameters and live
name/value/active edits. Name lookup selects the first active value; name writes
and removal address the first matching object, even when inactive. Master and
font parameter storage remain distinct from ordinary userData. The Arabic stage
uses the exact `Use Arabic Presentation Form Unicodes` key and appends maintained
legacy data during an explicit refresh.

Read the [parameter and Arabic guide](../guide/glyport-parameters.md) for owned
examples, direct/nil/empty legacy precedence, stored overlays, refresh/reset and
macOS locale/float32 conversion. The [legacy Unicode and ROS guide](../guide/glyport-metadata.md)
adds public `GSGlyphInfo.unicodeLegacy` snapshots, distinct primary/legacy values
and the exact ROS shared-manager refusal/no-op boundary. The five proprietary
map requests refuse before presentation and metadata writes; no maps or
approximations ship. Non-macOS strings, arbitrary object conversion, full ROS
mapping, custom managers and native collisions remain open.
Earlier archive hashes on this page stay historical; they do not
identify this newer source candidate. No published release or native
workflow acceptance is implied.

## What is supported

- The private candidate’s [global Unicode Glyph Info](../guide/glyport-unicode.md):
  exact combined primary/legacy lookup and audited synthesis on a miss, returning
  read-only name, Unicode, separate legacy Unicode, category, subCategory, script,
  case and supported component snapshots. Font-local managers, arbitrary bridge
  inputs, remaining
  fields and native workflows retain explicit limits.
- The `GlyphsApp` module for each run: `Glyphs`, the GS* model classes, callback
  events and dialogs ([GlyphsApp reference](../reference/GlyphsApp.md)).
- The seven Glyphs SDK plugin classes (`GeneralPlugin`, `FilterWithoutDialog`,
  `FilterWithDialog`, `ReporterPlugin`, `PalettePlugin`, `SelectTool`,
  `FileFormatPlugin`), registered as real FontLab menu actions, windows,
  export items and Glyph-window painters where supported. `SelectTool` is
  explicitly blocked, as noted below.
- Vanilla controls and dialogs, Qt-backed AppKit classes, NSBezierPath drawing and
  NIB/XIB interface loading ([vanilla](../reference/vanilla.md),
  [AppKit](../reference/AppKit.md)).

## Limits

- Compatibility is partial and still being extended; each run records a receipt
  with the outcome, and unsupported features raise `UnsupportedCapability` at the
  script line instead of failing silently.
- FontLab host limits block `SelectTool` and drawing before FontLab's own glyph
  layer; plugins that need them are reported as blocked.
- Bundles that ship only compiled macOS code cannot run.
- Creating glyphs makes FontLab rebuild auto-layer composites. Glyport restores
  existing composites afterwards and refuses with a named reason when it cannot.
  A FontLab defect can still drop component locks and attaching anchors on
  composites it rebuilds.
- Edits on auto layers (outlines, anchors, guides, hints, width, background) are
  refused before anything changes: telling FontLab about an auto-layer edit
  makes it rebuild every auto layer in the font.
- Test with a copy of your font: scripts can change the font they run on.

See the [Glyphs compatibility guide](../guide/glyphs.md). Reference:
[fontlab_glyport](../reference/fontlab_glyport.md).
