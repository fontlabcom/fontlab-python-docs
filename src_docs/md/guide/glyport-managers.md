---
this_file: src_docs/md/guide/glyport-managers.md
---
# Select the metadata manager before reading Glyph Info

Use `glyph.glyphInfo` for metadata resolved through that glyph's parent font and
document. Use `Glyphs.glyphInfoForName(..., font=font)` or the Unicode method when
you explicitly choose a font. Omitting the font selects the shared manager; it
does not mean the current font. These routes return the selected manager's result.

This guide describes private Glyport source checkpoint
`97304f34ffa7ec19ee4132c4e67e2205cb30e269` with matching Echopy source
`500542d333ed964788b3d06ae9caeff353c4b156`.
Owned Python examples qualify the source contracts below. Fresh ordinary
wheel/sdist tuples and their complete consumers need separate qualification.
None of these examples establishes native FontLab history, document preservation,
saved/reopened results, proprietary resource completeness or every Glyphs version.

## Distinguish manager reads and snapshots

| Operation | Meaning |
| --- | --- |
| `font.glyphsInfo()` | Ask the parent document for `valueForKey_("glyphsInfo")`; only nil falls back to the shared manager |
| `glyph.glyphInfo` | Ask that selected manager for `glyphInfoForGlyph_(glyph)` |
| `manager.infoFromDataForName_` / `infoFromDataForUnicode_` | Read a canonical raw indexed view, without name synthesis or production filling |
| `manager.glyphInfoForName_` | Resolve a name in this manager and fill eligible nil production metadata |
| `copy(info)` / `deepcopy(info)` | Copy the record containers and production cell; component objects remain shallow references |
| `GSGlyphInfo(glyph)` | Freeze a snapshot of raw glyph getters; this is distinct from the parent-aware property |

A detached `GSGlyph("A")` has no parent manager. Its `glyphInfo` property refuses;
the explicit snapshot constructor remains available. An owned manager can also
accept that glyph directly through `glyphInfoForGlyph_`; this does not attach it.

## Prepare an owned graph

Run this setup before the tagged examples. It uses real exported model and
manager classes with `FakeBackend`, empty defaults and an inert bridge. The
underscored `_from_index` and document `_local_glyph_info` assignments are explicit
test seams, not public upstream manager setters or a local-file initializer.
They never replace the shared manager or import FontLab or a native framework.

```python
from pathlib import Path
from fontlab_glyport.glyphsapp import make_glyphsapp_module
from fontlab_glyport.model import Model
from fontlab_glyport.model.fake_backend import FakeBackend
from fontlab_glyport.model.info_records import GlyphInfoIndex, add_unicode, new_record

def owned_manager(label="Owned local", *, shared=None):
    # Known defaults belong to fresh owned records, never to unknown public data.
    from fontlab_glyport.glyphsapp import GSGlyphsInfo
    record = new_record("A")
    add_unicode(record, "0041")
    record.category, record.subCategory = "Letter", "Owned subcategory"
    record.script, record.case = "latin", 1
    record.desc, record.group, record.groupIdx, record.direction = label, "Local", 7, 0
    record.altNames = ["OwnedAlias"]
    record._locked = True
    index = GlyphInfoIndex(shared=shared)
    index.append(record)
    return GSGlyphsInfo._from_index(index), record

def owned_exports(manager, profile="glyphs4"):
    model = Model(FakeBackend())
    font = model.font
    font.parent._local_glyph_info = manager
    exports = make_glyphsapp_module(
        model, object(), profile=profile, defaults={}, error_sink=lambda *args: None,
    )
    return exports, font

def owned_application(profile, model):
    return make_glyphsapp_module(
        model, object(), profile=profile, defaults={}, error_sink=lambda *args: None,
    ).Glyphs

def owned_parsed_manager():
    # Explicit authored rows for the older edit examples, not copied public data.
    from tempfile import TemporaryDirectory
    from types import SimpleNamespace
    from xml.sax.saxutils import quoteattr
    from fontlab_glyport.glyphsapp import GSGlyphsInfo

    rows = [
        {"name": "A", "unicode": "0041", "script": "latin", "case": "upper"},
        {"name": "a", "unicode": "0061", "script": "latin", "case": "lower"},
        {"name": "I", "unicode": "0049", "script": "latin", "case": "upper"},
        {"name": "i", "unicode": "0069", "script": "latin", "case": "lower"},
        {"name": "dotlessi", "unicode": "0131", "script": "latin", "case": "lower"},
        {"name": "f_f", "script": "latin", "case": "lower"},
        {"name": "f_f_i", "script": "latin", "case": "lower"},
        {"name": "less", "unicode": "003C", "category": "Symbol", "case": "lower"},
        {"name": "Alpha", "unicode": "0391", "script": "greek", "case": "upper"},
        {"name": "A-cy", "unicode": "0410", "script": "cyrillic", "case": "upper"},
        {"name": "alef-ar", "unicode": "0627", "script": "arabic"},
        {"name": "alef-ar.isol", "script": "arabic"},
        {"name": "acutecomb", "unicode": "0301", "category": "Mark", "subCategory": "Nonspacing"},
        {"name": "Aacute", "unicode": "00C1", "script": "latin", "case": "upper", "decompose": "A, acutecomb"},
    ]
    entries = []
    for row in rows:
        attributes = {"category": "Letter", "direction": "LTR", "decompose": "", **row}
        entries.append("<glyph " + " ".join(
            f"{key}={quoteattr(value)}" for key, value in attributes.items()
        ) + "/>")
    manager = GSGlyphsInfo._from_index(GlyphInfoIndex())
    with TemporaryDirectory(dir=Path.cwd()) as temporary:
        path = Path(temporary) / "GlyphData.xml"
        path.write_text("<glyphData>" + "".join(entries) + "</glyphData>", encoding="utf-8")
        assert manager.loadCustomGlyphDataFromURL_error_(SimpleNamespace(path=lambda: str(path)), None) is True
    # Custom XML does not merge legacy Unicode. Establish this invented fixture
    # field separately, without claiming that the loader accepts that attribute.
    manager._index.names["alef-ar.isol"].unicodeLegacy = "FE8D"
    return manager
```

The linked earlier edit guides run this same setup first. `owned_parsed_manager`
establishes fresh known group/groupIdx defaults by actual parsing, rather than
turning missing public fields into nil/zero. Its explicit legacy assignment is
an owned fixture extension, not an implemented custom-file attribute. Each edit
example selects that manager on its own font; detached-name examples use its
explicit temporary resolver scope. No maintained public record is changed.

### Follow document ownership and retain old views

Two fonts can resolve the same name and encoding against different managers.
Replacing the document's selected manager affects later reads, while a retained
old view continues to describe its original record. A returned nil is returned
as nil; it is not permission to query another font.

<!-- example: glyport-manager-document-selection -->
```python
from fontlab_glyport.glyphsapp import GSGlyphsInfo

first, _ = owned_manager("First document")
second, _ = owned_manager("Second document")
exports, font = owned_exports(first)
glyph = font.glyphs["A"]
assert font.glyphsInfo() is first
assert exports.Glyphs.currentDocument is font.parent
retained = glyph.glyphInfo
assert retained.desc == "First document"
raw = exports.Glyphs.glyphInfoForName("A", font=font)
assert raw.desc == retained.desc
assert exports.Glyphs.glyphInfoForUnicode(65, font=font) is raw
font.parent._local_glyph_info = second
assert glyph.glyphInfo.desc == "Second document"
assert retained.desc == "First document"
assert exports.Glyphs.glyphInfoForName("A") is GSGlyphsInfo.sharedManager().glyphInfoForName_("A")
```

### Keep canonical identity and independent production copies

An exact raw name, an alias and an indexed encoding can share one public view.
A local miss can return the shared index's same view. A name fill changes the
shared record's production cell; copies taken before that fill retain nil.

<!-- example: glyport-manager-raw-copy -->
```python
from copy import copy, deepcopy
from fontlab_glyport.glyphsapp import GSGlyphsInfo

manager, _ = owned_manager()
local = GSGlyphsInfo._from_index(GlyphInfoIndex(shared=manager._index))
raw = manager.infoFromDataForName_("A")
assert raw is manager.infoFromDataForName_("OwnedAlias")
assert raw is manager.infoFromDataForUnicode_("0041")
assert raw is local.infoFromDataForName_("A")
shallow, deep = copy(raw), deepcopy(raw)
assert raw.productionName is shallow.productionName is deep.productionName is None
assert manager.glyphInfoForName_("OwnedAlias") is raw
assert raw.productionName == "A"
assert shallow.productionName is deep.productionName is None
assert manager.infoFromDataForUnicodes_(["FFFF", "0041"]) is raw
assert manager.glyphInfoForUnicodes_(["FFFF", "0041"]).name == "uniFFFF"
```

### Freeze raw glyph values explicitly

Raw glyph fields can differ from the effective selected record. The constructor
preserves raw case, group, groupIdx and direction, while the property applies
the selected record and enabled stored overlays. Neither read refreshes the glyph.

<!-- example: glyport-manager-frozen-constructor -->
```python
from fontlab_glyport.errors import UnsupportedCapability

manager, _ = owned_manager()
exports, font = owned_exports(manager)
glyph = font.glyphs["A"]
glyph.case = 5
glyph.group, glyph.groupIdx, glyph.direction = "Raw", -3, 2
snapshot = exports.GSGlyphInfo(glyph)
assert (snapshot.case, snapshot.group, snapshot.groupIdx, snapshot.direction) == (5, "Raw", -3, 2)
assert (glyph.glyphInfo.case, glyph.glyphInfo.group, glyph.glyphInfo.direction) == (1, "Local", 0)
glyph.case = 2
assert snapshot.case == 5 and glyph.case == 2
detached = exports.GSGlyph("A")
try:
    _ = detached.glyphInfo
except UnsupportedCapability:
    pass
else:
    raise AssertionError("A detached glyph has no parent manager")
assert detached.parent is None
assert exports.GSGlyphInfo(detached).name == "A"
```

## Apply the six stored overlays independently

The resolver selects Unicode/name metadata, applies additional Unicode, ROS and
Arabic presentation stages, then applies enabled stored fields. The six fields
are `case`, `group`, `script`, `category`, `subCategory` and `direction`; their
flags are `storeCase`, `storeGroup`, `storeScript`, `storeCategory`,
`storeSubCategory` and `storeDirection`. Setting a raw value alone does not enable
its overlay. Keep-name categories and earlier explicit refusals have their own
branches; do not infer a universal overlay result from this owned letter case.

<!-- example: glyport-manager-six-overlays -->
```python
manager, record = owned_manager()
exports, font = owned_exports(manager)
glyph = font.glyphs["A"]
values = {"case": 5, "group": "Stored", "script": "greek",
          "category": "Symbol", "subCategory": "Math", "direction": 2}
baseline = {name: getattr(glyph.glyphInfo, name) for name in values}
for name, value in values.items():
    setattr(glyph, name, value)
    assert getattr(glyph.glyphInfo, name) == baseline[name]
    setattr(glyph, "store" + name[0].upper() + name[1:], True)
    assert getattr(glyph.glyphInfo, name) == value
assert all(getattr(glyph.glyphInfo, name) == value for name, value in values.items())
assert (record.case, record.group, record.script, record.category,
        record.subCategory, record.direction) == (1, "Local", "latin", "Letter", "Owned subcategory", 0)
```

`groupIdx` is a separate raw signed 16-bit field, not a seventh overlay flag.
Group flag transitions do not look up/reset raw group or groupIdx. Turning an
enabled direction flag off resolves and stores the selected direction, and a
detached direction reset refuses. Raw direction accepts owned integers 0–255;
bool and arbitrary bridge coercions are outside these scalar setters.

<!-- example: glyport-manager-group-direction-reset -->
```python
manager, _ = owned_manager()
exports, font = owned_exports(manager)
glyph = font.glyphs["A"]
glyph.group, glyph.groupIdx = "Stored", -32768
glyph.storeGroup = True
glyph.storeGroup = False
assert (glyph.group, glyph.groupIdx) == ("Stored", -32768)
assert glyph.glyphInfo.groupIdx == 7
glyph.direction = 2
glyph.storeDirection = True
assert glyph.glyphInfo.direction == 2
glyph.storeDirection = False
assert glyph.direction == glyph.glyphInfo.direction == 0
for field, value, error in [("groupIdx", 32768, ValueError), ("direction", 256, ValueError),
                            ("direction", True, TypeError)]:
    try:
        setattr(glyph, field, value)
    except error:
        pass
    else:
        raise AssertionError("The raw scalar boundary must reject this value")
```

Known fresh custom-record defaults do not establish missing maintained public
fields. In particular public group/groupIdx and physical metadata recipes remain
explicit unavailable capabilities where the input does not establish them.
Outline components and Unicode NFD do not supply those recipes. Description,
stored production and raw primary/legacy Unicode remain separate contracts.

<!-- example: glyport-manager-public-unknown -->
```python
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSGlyphsInfo

info = GSGlyphsInfo.sharedManager().infoFromDataForName_("A")
assert info.name == "A" and info.category == "Letter"
for field in ("group", "groupIdx", "components"):
    try:
        getattr(info, field)
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphInfo." + field + ".source"
    else:
        raise AssertionError("Unknown public data must not become an empty default")
```

## Select one complete wrapper profile

The execution profile chooses application wrapper semantics. FontLab's version
or build does not identify a Glyphs generation. Direct `GSApplication(...)` and
factory calls with no profile use Glyphs4; factory profiles must be explicit
`glyphs2`, `glyphs3` or `glyphs4`. The execution layer resolves `auto` before it
constructs these providers. Do not combine the public Glyphs3 keyword/formatting
contract with Glyphs4 integer font forwarding.

| Observable detail | Glyphs2 | Glyphs3 | Glyphs4 |
| --- | --- | --- | --- |
| Name first keyword | `String` | `name` | `name` |
| Unicode first keyword | `String` | `String` | `string_or_int` |
| Integer test | `type(value) is int` | `isinstance(value, int)` | `isinstance(value, int)` |
| Integer Unicode conversion | `"%04X" % value` | `"%04X" % value` | `f"{value:04X}"` |
| Integer Name call | instance Unicode method without font keyword | same | instance Unicode method with `font=font`, including None |
| Explicit-font string Name / direct Unicode | exact font manager | exact font manager | exact font manager |

An int subclass or bool reaches the Glyphs2 manager unchanged. Glyphs3 percent
formatting does not call its `__format__`; Glyphs4 f-string formatting does.
Four is minimum width, not a scalar validator. Negative/huge integers retain
wrapper spelling. Wrong-version keywords fail ordinary Python binding.

<!-- example: glyport-manager-profile-signatures -->
```python
import inspect

manager, _ = owned_manager()
for profile, name_key, unicode_key in [("glyphs2", "String", "String"),
                                      ("glyphs3", "name", "String"),
                                      ("glyphs4", "name", "string_or_int")]:
    exports, font = owned_exports(manager, profile)
    app = exports.Glyphs
    assert str(inspect.signature(app.glyphInfoForName)) == f"({name_key}, font=None)"
    assert str(inspect.signature(app.glyphInfoForUnicode)) == f"({unicode_key}, font=None)"
    assert app.glyphInfoForName(**{name_key: "A", "font": font}).desc == "Owned local"
    assert app.glyphInfoForUnicode(**{unicode_key: 65, "font": font}).desc == "Owned local"
    rejected = "String" if profile == "glyphs4" else "string_or_int"
    try:
        app.glyphInfoForUnicode(**{rejected: "0041"})
    except TypeError:
        pass
    else:
        raise AssertionError("Wrong-version keywords must fail binding")
```

For wrapper observations, an owned recorder manager deliberately returns the
received object. This tests the real wrapper before metadata input validation;
it does not claim arbitrary bridge objects are valid raw Unicode keys.

<!-- example: glyport-manager-profile-format-forward -->
```python
class Recorder:
    def glyphInfoForUnicode_(self, value):
        return value
    def glyphInfoForName_(self, value):
        return value

class OwnedFont:
    def glyphsInfo(self):
        return Recorder()
    def __bool__(self):
        raise AssertionError("Select fonts by None, never truthiness")

class FormattedInt(int):
    def __format__(self, spec):
        assert spec == "04X"
        return "OwnedFormat"

manager, _ = owned_manager()
font = OwnedFont()
for profile in ("glyphs2", "glyphs3", "glyphs4"):
    app = owned_exports(manager, profile)[0].Glyphs
    value = FormattedInt(65)
    actual = app.glyphInfoForUnicode(value, font=font)
    if profile == "glyphs2":
        assert actual is value
        assert app.glyphInfoForUnicode(True, font=font) is True
        assert app.glyphInfoForName(value, font=font) is value
    else:
        assert actual == ("0041" if profile == "glyphs3" else "OwnedFormat")
        assert app.glyphInfoForUnicode(True, font=font) == "0001"
        named = app.glyphInfoForName(value, font=font)
        assert named.name == "A" if profile == "glyphs3" else named == "OwnedFormat"
    for integer in (-1, 2**128):
        assert app.glyphInfoForUnicode(integer, font=font) == "%04X" % integer
    calls = []
    object.__setattr__(app, "glyphInfoForUnicode", lambda *a, **kw: calls.append((a, kw)))
    app.glyphInfoForName(65, font=font)
    app.glyphInfoForName(65)
    assert calls == [((65,), {"font": font} if profile == "glyphs4" else {}),
                     ((65,), {"font": None} if profile == "glyphs4" else {})]
```

### Preserve profiles through both providers

`FontLabSession.adapters()` and `fontlab_glyphsapp_provider(ctx, ...)` both pass
`ctx.profile` to the application factory. The following source fixture substitutes
only the latter's host constructors with owned inert objects. It invokes neither
a real backend nor a Qt/application/framework API. Context closure closes the
owned bridge. Production scripts obtain their provider from the execution host.

<!-- example: glyport-manager-provider-profiles -->
```python
from unittest.mock import patch
import inspect
from fontlab_glyport import ExecutionContext
from fontlab_glyport.glyphsapp.fontlab_session import FontLabSession
from fontlab_glyport.glyphsapp import fontlab_bridge

class OwnedBridge:
    def __init__(self, **options):
        self.closed = False
    def close(self):
        self.closed = True

for profile in ("glyphs2", "glyphs3", "glyphs4"):
    context = ExecutionContext(Path.cwd(), profile)
    model = Model(FakeBackend())
    selected, _ = owned_manager("Provider marker")
    model.font.parent._local_glyph_info = selected
    session = object.__new__(FontLabSession)
    session.ctx, session.model, session.bridge = context, model, object()
    session.defaults, session._menu, session._filters = {}, object(), {}
    try:
        session_app = session.adapters()["GlyphsApp"]().Glyphs
        with patch.object(fontlab_bridge, "FontLabBackend", return_value=object()), \
             patch.object(fontlab_bridge, "Model", return_value=model), \
             patch.object(fontlab_bridge, "FontLabGlyphsBridge", OwnedBridge):
            provider = fontlab_bridge.fontlab_glyphsapp_provider(
                context, version=(99, 999), packages=[], defaults={},
            )
            bridge_app = provider().Glyphs
        name = "String" if profile == "glyphs2" else "name"
        unicode = "string_or_int" if profile == "glyphs4" else "String"
        for app in (session_app, bridge_app):
            assert str(inspect.signature(app.glyphInfoForName)) == f"({name}, font=None)"
            assert str(inspect.signature(app.glyphInfoForUnicode)) == f"({unicode}, font=None)"
            font = model.font
            raw = selected.infoFromDataForUnicode_("0041")
            assert app.glyphInfoForName("A", font=font) is raw
            assert app.glyphInfoForUnicode(65, font=font) is raw
            expected = raw if profile == "glyphs4" else app.glyphInfoForUnicode("0041")
            assert app.glyphInfoForName(65, font=font) is expected
    finally:
        context.close()
    assert bridge_app._bridge.closed
```

## Load explicit custom files in order

`loadCustomGlyphDataFromURL_error_(url, None)` accepts the qualified `path()` URL
protocol and returns a bool. The synthetic `objc.NULL` singleton is also accepted;
this does not import native objc or establish arbitrary NSError output-slot/tuple
bridging. Non-null error arguments refuse before reading a URL. Missing files
succeed; too-short or malformed files return false. Non-regular files and
unsupported UTF8/URL conversion remain explicit unavailable capabilities.

The parser implements the retained glyph-token/custom-attribute contract rather
than general XML normalization. Supplied file order and duplicates remain visible.
Completed rows survive a later failure, and later files are not consumed.
Custom description, group and legacy Unicode are not merge fields; fresh known
nil/zero defaults differ from unknown maintained public data. Reused records can
remain addressable in dictionaries without being appended again to a row list.

<!-- example: glyport-manager-custom-partial-failure -->
```python
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSGlyphsInfo

with TemporaryDirectory(dir=Path.cwd()) as temporary:
    folder = Path(temporary)
    payloads = [("one.xml", '<glyph name="First" unicode="0041"/>'),
                ("bad.xml", '<glyph name="Completed"/><glyph name=Bad/>'),
                ("last.xml", '<glyph name="Never"/>')]
    urls = []
    for filename, text in payloads:
        path = folder / filename
        path.write_text(text, encoding="utf-8")
        urls.append(SimpleNamespace(path=lambda path=path: str(path)))
    manager = GSGlyphsInfo._from_index(GlyphInfoIndex())
    consumed = []
    def ordered():
        for url in urls:
            consumed.append(url)
            yield url
    assert manager.loadLocalGlyphInfoFiles_error_(ordered(), None) is False
    assert consumed == urls[:2]
    assert manager.infoFromDataForName_("First").unicode == "0041"
    assert manager.infoFromDataForName_("Completed").name == "Completed"
    assert manager.infoFromDataForName_("Never") is None
```

### Finalize the selected graph explicitly

Loading preserves raw decomposition name tokens. `updateComponentsInfos()` resolves
them through the receiver's graph/full-name callback and retains canonical child
references. Copies have separate component containers but the same child records.
Finalization also computes qualified base strings and reference fields; private
Arabic fallback marks and fraction resources remain unavailable when unknown.
It is a source-order mutation, not a generally repeatable reset or transaction.

<!-- example: glyport-manager-custom-finalize -->
```python
from copy import copy
from tempfile import TemporaryDirectory
from types import SimpleNamespace

manager, _ = owned_manager()
with TemporaryDirectory(dir=Path.cwd()) as temporary:
    path = Path(temporary) / "GlyphData.xml"
    path.write_text('<glyph name="pair" decompose="A, A"/>', encoding="utf-8")
    assert manager.loadCustomGlyphDataFromURL_error_(SimpleNamespace(path=lambda: str(path)), None) is True
    pair = manager.infoFromDataForName_("pair")
    assert pair.components == ["A", "A"]
    manager.updateComponentsInfos()
    child = manager.infoFromDataForName_("A")
    assert pair.components[0] is pair.components[1] is child
    duplicate = copy(pair)
    assert duplicate is not pair and duplicate.components[0] is child
    duplicate.components.clear()
    assert len(pair.components) == len(duplicate.components) == 2
    # This internal field is evidence of the owned finalizer, not a public API.
    assert pair._resolved_record.baseString == "AA"
```

### Discover only within the qualified filesystem domain

Candidate construction keeps the supplied path itself, its `Info` child, then
parent and parent/Info unless that parent is the expanded home. A project-file
input is not silently changed to its directory. Root repeats remain repeats.
Folder enumeration selects exact `GlyphData.xml` or case-sensitive
`GlyphData_*.xml`, filters before resolution, and preserves provider order and
duplicate URLs. It neither sorts nor deduplicates the selected files.

The current default provider is qualified for macOS canonical absolute POSIX
paths, its hidden/package boundary and supported symlinks. Foundation enumeration
order, Finder aliases, arbitrary NSString/NSURL conversions and other filesystem
domains remain separate. This example uses a private temporary directory with one
matching file; it does not assume order among multiple directory entries.

<!-- example: glyport-manager-custom-discovery -->
```python
from tempfile import TemporaryDirectory
from fontlab_glyport.glyphsapp import GSGlyphsInfo

with TemporaryDirectory(dir=Path.cwd()) as temporary:
    folder = Path(temporary)
    match = folder / "GlyphData_owned.xml"
    match.write_text('<glyph name="Discovered"/>', encoding="utf-8")
    (folder / "glyphdata_ignored.xml").write_text('<glyph name="Never"/>', encoding="utf-8")
    supplied = str(folder)
    candidates = GSGlyphsInfo.foldersForCustomInfoForFolder_(supplied)
    assert candidates[:2] == [supplied, supplied + "/Info"]
    urls = GSGlyphsInfo.findLocalGlyphInfoFolders_([supplied, supplied])
    assert [url.path() for url in urls] == [str(match), str(match)]
    manager = GSGlyphsInfo._from_index(GlyphInfoIndex())
    assert manager.loadLocalGlyphInfoFiles_error_(urls, None) is True
    assert manager.infoFromDataForName_("Discovered").name == "Discovered"
    assert manager.infoFromDataForName_("Never") is None
```

## Complete local construction and reload remain separate

These file/index/finalizer/discovery capabilities do not implement
`initWithLocalFile_`, `initWithLocalFile_forFont_` or complete `loadGlyphInfo`.
Plain construction/`init()` returns the shared manager; `alloc()` alone is an
uninitialized object, not an empty usable local manager. The owned seams above
do not authorize presenting a successful public local initializer.

The retained constructor contract includes sidebar setup, an operation queue,
glyph loading and a final queue wait. Reload ordering depends on the stored URL:
nil/global loading includes a Chinese intermediate barrier before later Hangul
work; nonnil local loading has no final barrier. Constructors add a final wait.
Thus neither universal synchronous reload nor universal absence of waits is
accurate. A local nonnil URL can still transitively initialize shared resources.

Reload replaces the row list while retaining name/Unicode maps; it does not
universally delete records absent from the next file set. Sidebar groups,
summary callbacks, iMatra and other private resources have independent lifecycle
requirements. A minimal custom file cannot stand in for those missing resources.
The full original script, native cache/lifetime/history and save/reopen workflows
stay open, alongside generated-reference, source-lock, site/archive/routes,
browser accessibility and publication gates.

## Read the source contract

The checkpoint's `glyphsapp/info_manager.py`, `glyphsapp/application.py`,
`glyphsapp/application_profiles.py`, `model/glyph_metadata.py`,
`model/stored_glyph_fields.py`, `model/info_records.py`, `model/custom_info.py`,
`model/custom_info_parser.py`, `model/info_finalize.py` and
`model/custom_info_discovery.py` define these bounded source operations.
The [description guide](glyport-descriptions.md),
[production guide](glyport-production.md) and [compound guide](glyport-compounds.md)
retain their field/selection contracts with current manager/identity corrections
and explicit owned fixtures where a complete metadata source is required.

Wrapper authority is the pinned public SDK source for
[Glyphs2](https://github.com/schriftgestalt/GlyphsSDK/blob/1c5a8639ba643dfd9d6379b8daad4173b67aab73/ObjectWrapper/GlyphsApp/__init__.py#L937),
[Glyphs3](https://github.com/schriftgestalt/GlyphsSDK/blob/569244a7181e08fc7c5230bcdfad6b9f7e5ea11f/ObjectWrapper/GlyphsApp/__init__.py#L1332)
and [Glyphs4](https://github.com/schriftgestalt/GlyphsSDK/blob/6483f93aa17a0917cc6ebe9abe71126509c3889c/ObjectWrapper/GlyphsApp/__init__.py#L2070),
plus the separately retained Glyphs4 wrapper/static loader audit. Source labels
do not prove every minor version or a current native runtime. Earlier tagged controls have current source-qualified fixtures and corrected
oracles where the selected-manager contract changed. Exact original code bodies
remain in external verification evidence and the retained predecessor history.
