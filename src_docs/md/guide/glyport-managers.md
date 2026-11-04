---
this_file: src_docs/md/guide/glyport-managers.md
---
# Select the metadata manager before reading Glyph Info

Use `glyph.glyphInfo` for metadata resolved through that glyph's parent font and
document. Use `Glyphs.glyphInfoForName(..., font=font)` or the Unicode method when
you explicitly choose a font. Omitting the font selects the shared manager; it
does not mean the current font. These routes return the selected manager's result.

This guide describes private Glyport source checkpoint
`5a54b4b681f3a5cf1d80830c57204c4b36e92711`. Matching Echopy producer
provenance is qualified separately from these authored source examples.
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

The connected source now implements the constructor/reload control paths over
explicit lawful dependencies. Public global record queries and complete local
resource initialization have different requirements, detailed below. Plain
construction/`init()` returns the shared manager; `alloc()` alone is uninitialized.
An owned index created with `_from_index` has no complete lifecycle resources.

## Construct and reload a local manager with explicit dependencies

Continue with [sidebar trees and document metadata](glyport-sidebar.md) for
defaults-backed visibility, dynamic category/filter trees, insertion and copy
identity, delayed counts, list expansion and actual document URL loading. Its
experiments reuse the exact setups below and keep FontLab adapters explicit.

The source checkpoint connects `initWithLocalFile_`,
`initWithLocalFile_forFont_`, `loadGlyphInfo` and their base-parser/sidebar helpers.
Public global queries can use the maintained public record index without these
dependencies. Complete local initialization needs an explicit lawful provider;
there is no default provider for private GlyphData, sidebar property lists,
iMatra resources, localization, images, predicates or operation queues. The
internal `using_info_provider` context supplies dependencies for source
qualification. It is not a supported native provider installer.

An allocated local receiver retains the exact URL object, creates its own queue,
sets that queue's concurrency limit, dispatches the sidebar before glyph loading,
then waits after successful loading. `None` is a global-load branch on that local
receiver; it does not turn the receiver into the shared manager. An existing
shared receiver retains its shared flag if explicitly reinitialized. The font
argument selects sidebar dispatch, including the empty icon-set branch; the
initializer does not establish document observation or a lasting font binding.

### Shared setup for the local examples

Run the following setup after **Prepare an owned graph**, then run each
`glyport-local-*` example separately. The verification runner executes both
exact setup blocks in a fresh namespace and directory for each tag. The
context temporarily isolates the process-wide shared pointer and resource caches,
and restores them in `finally`. Those assignments, `_lifecycle` inspection and
`InfoErrorSlot` are internal owned controls, not public application recipes.

Every resource below is invented. The scheduler runs queued callbacks in FIFO
order when explicitly waited. The actual Chinese generator runs all ten jobs
over its complete fixed ranges and four explicitly supplied invented banks;
the actual queued Hangul generator visits all 11,172 syllables. The base file
supplies owned Jamo and three syllable targets. Missing Unicode lookups can also
synthesize records through the manager's existing resolution rules.
Localization, nil collection handling, filesystem enumeration and empty image
directories have explicit fixture policies. This qualifies those algorithms,
that schedule and those inputs only; it supplies no proprietary embedded lists.

<!-- setup: glyport-local-lifecycle -->
```python
from contextlib import contextmanager
from types import SimpleNamespace
from fontlab_glyport.glyphsapp import GSGlyphsInfo
from fontlab_glyport.glyphsapp.info_runtime import (
    InfoErrorSlot, InfoNativeException, using_info_provider,
)
from fontlab_glyport.glyphsapp import info_sidebar_resources

class OwnedQueue:
    def __init__(self, events):
        self.events, self.pending = events, []
    def setMaxConcurrentOperationCount_(self, count):
        self.maxConcurrentOperationCount = count
    def addOperationWithBlock_(self, callback):
        self.pending.append(callback)
    def waitUntilAllOperationsAreFinished(self):
        self.events.append(("wait", self))
        while self.pending:
            self.pending.pop(0)()

class OwnedLifecycleProvider:
    def __init__(self, base, folder):
        self.base, self.folder, self.events, self.queues = base, folder, [], []
        self.arrays = {
            "defaultCategories": [{"name": "Owned category", "id": "Owned"}],
            "defaultLanguages": [], "StandardFilter": [],
        }
        self.dictionary = {"invented": "matra"}
        self.banks = (("2FF0",), ("20000",), ("20001",), ("20002",))
        self.bank_calls = []
    def new_queue(self):
        queue = OwnedQueue(self.events)
        self.queues.append(queue)
        return queue
    def active_processor_count(self):
        return 2
    def resource_url(self, name, extension):
        self.events.append(("resource", name, extension))
        return {"GlyphData": SimpleNamespace(path=lambda: str(self.base)),
                **{key: key for key in self.arrays},
                "iMatraPresCombination": "owned-matra"}[name]
    def load_array(self, url):
        return self.arrays[url]
    def load_dictionary(self, url):
        assert url == "owned-matra"
        return self.dictionary
    def localize(self, text):
        return text  # Explicit identity localization for these invented inputs.
    def compare(self, left, right):
        return (left > right) - (left < right)
    def distinct_values(self, rows, field):
        return list(dict.fromkeys(getattr(row, field) for row in rows
                                  if getattr(row, field) is not None))
    def application_support_paths(self):
        return []  # This fixture has no global support folders.
    def user_support_path(self):
        return str(self.folder / "owned-support")
    def directory_entries(self, path):
        return []  # Owned icon/group/filter directories are explicitly empty.
    def resolve_path(self, path):
        return path
    def load_property_list(self, path):
        assert path == self.user_support_path() + "/CustomFilter.plist"
        return [], None  # An empty primary filter suppresses StandardFilter.
    def draw_emoji_icon(self, width, height, flipped):
        assert (width, height, flipped) == (17, 17, True)
        return SimpleNamespace(setName_=lambda name: self.events.append(("image", name)))
    def chinese_codes(self, slot):
        self.bank_calls.append(slot)
        return self.banks[slot]
    def notify(self, manager, phase, key):
        self.events.append((phase, key))
    def add_observer(self, *arguments):
        self.events.append(("observer", arguments))
    def register_defaults(self, values):
        self.events.append(("defaults", values))
    def present_error(self, error):
        self.events.append(("error", error))
    def log(self, value):
        self.events.append(("log", value))

@contextmanager
def owned_lifecycle():
    from tempfile import TemporaryDirectory
    saved_shared = GSGlyphsInfo._shared
    saved_arrays = info_sidebar_resources._once_arrays
    GSGlyphsInfo._shared = None
    info_sidebar_resources._once_arrays = {}
    try:
        with TemporaryDirectory(dir=Path.cwd()) as temporary:
            folder = Path(temporary)
            base = folder / "base.xml"
            codes = [*range(0x1100, 0x1113), *range(0x1161, 0x1176),
                     *range(0x11A8, 0x11C3), 0xAC00, 0xAC01, 0xD7A3]
            base.write_text(
                '<glyph name="owned.base" unicode="0041" '
                'script="owned" subCategory="Base"/>' + "".join(
                    f'<glyph name="owned.{code:04X}" unicode="{code:04X}" '
                    'script="owned" category="Letter" subCategory="Other"/>'
                    for code in codes), encoding="utf-8")
            local = folder / "font"
            local.mkdir()
            data = local / "GlyphData.xml"
            data.write_text('<glyph name="owned.local" unicode="0042" '
                            'script="fleet" subCategory="Local"/>', encoding="utf-8")
            provider = OwnedLifecycleProvider(base, folder)
            url = SimpleNamespace(path=lambda: str(local))
            with using_info_provider(provider):
                yield provider, url, data
    finally:
        GSGlyphsInfo._shared = saved_shared
        info_sidebar_resources._once_arrays = saved_arrays
```

### Construct through the actual parser and sidebar paths

The nonnil local branch can initialize the shared manager transitively. This
example uses the real public constructor, base/custom loaders and sidebar builder;
it overrides none of them. The two queues and their completed jobs belong to
the invented sequential scheduler above. A successful constructor says nothing
about native resource availability.

<!-- example: glyport-local-connected-constructor -->
```python
with owned_lifecycle() as (provider, url, data):
    receiver = GSGlyphsInfo.alloc()
    manager = receiver.initWithLocalFile_(url)
    shared = GSGlyphsInfo.sharedManager()
    assert manager is receiver and manager is not shared
    assert manager._lifecycle.localURL is url and not manager._lifecycle.shared
    assert shared._lifecycle.shared and len(provider.queues) == 2
    assert all(queue.maxConcurrentOperationCount == 2 for queue in provider.queues)
    assert not any(queue.pending for queue in provider.queues)
    assert manager.infoFromDataForName_("owned.local").unicode == "0042"
    assert manager.infoFromDataForName_("owned.base") is shared.infoFromDataForName_("owned.base")
    state = manager._lifecycle
    assert state.allItem.identifier == "All"
    assert state.name2Group["Owned"].name == "Owned category"
    assert state.categoriesGroup.identifier == "CATEGORIES"
    assert state.filterGroups[0].identifier == "FILTERS"
    assert state.iMatraCombinations is provider.dictionary
    assert ("image", "GSEmojiIcon") in provider.events
```

### Reload retains maps while replacing the listed rows

`loadGlyphInfo()` resets the row/category arrays, keeps the name/Unicode maps and
queues a summary that reads the current rows when it executes. A custom override
can update an existing indexed record without relisting it. Only listed rows
receive fresh unsigned 32-bit indices and component finalization. Earlier views
can remain canonical and addressable even when absent from the new row list.

<!-- example: glyport-local-reload-identity -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(url)
    index = manager._index
    names, codes, old_rows = index.names, index.unicodes, index.records
    retained = manager.infoFromDataForName_("owned.local")
    data.write_text('<glyph name="owned.local" script="changed"/>', encoding="utf-8")
    manager.loadGlyphInfo()
    assert index.names is names and index.unicodes is codes
    assert index.records is not old_rows and index.records == []
    assert manager.infoFromDataForName_("owned.local") is retained
    assert retained.script == "changed" and retained.unicode == "0042"
    assert manager._lifecycle.queue.pending
    data.write_text('<glyph name="owned.new" script="fresh"/>', encoding="utf-8")
    manager.loadGlyphInfo()
    assert [row.name for row in index.records] == ["owned.new"]
    assert index.records[0].index == 0
    manager._lifecycle.queue.waitUntilAllOperationsAreFinished()
    assert "fresh" in manager._lifecycle.scriptIDs
    assert "changed" not in manager._lifecycle.scriptIDs
```

The local reload has no final barrier. Both queued summaries above see the latest
row list. Script IDs persist across reloads and shared IDs can be appended again;
do not interpret these arrays as a fresh deduplicated inventory of every map key.
Nil/global loading has a Chinese intermediate barrier before later Hangul work;
the constructor adds its final wait. Neither universal synchronous reload nor
universal absence of waits describes both branches.

### Keep base data distinct from custom overrides

The base scanner parses into independent containers before committing. It commits
names, encodings, rows and groups in order, with separate locks rather than an
atomic transaction. Empty destination containers can adopt parsed containers;
nonempty containers merge. Base rows establish description/group fields that
custom overrides do not merge. A malformed private parse leaves those manager
containers untouched; custom parsing can retain completed earlier rows on failure.
Neither scanner is a general XML normalizer or a proprietary GlyphData replacement.

<!-- example: glyport-local-base-custom-fields -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(url)
    base = data.parent / "base-owned.xml"
    base.write_text('<glyph name="owned.fields" unicode="0043" '
                    'description="Base description" group="Base group" '
                    'groupIdx="-3" script="owned"/>', encoding="utf-8")
    base_url = SimpleNamespace(path=lambda: str(base))
    sentinel = object()
    slot = InfoErrorSlot(sentinel)
    assert manager.loadGlyphDataFromURL_error_(base_url, slot)
    assert slot.value is sentinel
    view = manager.infoFromDataForName_("owned.fields")
    assert (view.desc, view.group, view.groupIdx) == ("Base description", "Base group", -3)
    override = data.parent / "override.xml"
    override.write_text('<glyph name="owned.fields" description="Ignored" '
                        'group="Ignored" script="changed"/>', encoding="utf-8")
    assert manager.loadCustomGlyphDataFromURL_error_(
        SimpleNamespace(path=lambda: str(override)), None)
    assert manager.infoFromDataForName_("owned.fields") is view
    assert (view.desc, view.group, view.groupIdx, view.script) == (
        "Base description", "Base group", -3, "changed")
```

### Preserve caller error state and partial custom commits

`None` and the synthetic `objc.NULL` remain the supported public null arguments.
`InfoErrorSlot` is an internal explicit source analogue of an output slot, not an
arbitrary native pointer bridge. A successful load leaves its previous value
alone. A qualified failed parse writes its error (which can be nil). A false
loader result with a nonnil error is presented by `loadGlyphInfo`, which then
continues; an exception has a different control path.

<!-- example: glyport-local-error-slot-boundaries -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(url)
    old_names, old_codes, old_rows = manager._index.names, manager._index.unicodes, manager._index.records
    broken = data.parent / "broken-base.xml"
    broken.write_text('<glyph name="uncommitted"/><glyph name="broken" unicode="unfinished/>', encoding="utf-8")
    slot = InfoErrorSlot(object())
    assert not manager.loadGlyphDataFromURL_error_(SimpleNamespace(path=lambda: str(broken)), slot)
    assert slot.value is not None
    assert manager._index.names is old_names and manager._index.unicodes is old_codes
    assert manager._index.records is old_rows
    assert manager.infoFromDataForName_("uncommitted") is None
    broken.write_text('<glyph name="completed"/><glyph name="broken" unicode="unfinished/>', encoding="utf-8")
    later = data.parent / "later.xml"
    later.write_text('<glyph name="never"/>', encoding="utf-8")
    assert not manager.loadLocalGlyphInfoFiles_error_(
        [SimpleNamespace(path=lambda: str(broken)), SimpleNamespace(path=lambda: str(later))], slot)
    assert slot.value.code() == 0x2AE2
    assert manager.infoFromDataForName_("completed").name == "completed"
    assert manager.infoFromDataForName_("never") is None
```

### Recover only the marked component exception

The protected interval covers component finalization and Hangul enqueue.
`InfoNativeException` is the owned source analogue for that qualified native
exception boundary. Ordinary Python errors, dependency refusals, earlier loader
failures and deferred callback failures propagate. A constructor does not drain
pending work on an exceptional return. These subclasses inject failures at the
actual public dispatch boundary; they do not claim a complete alternate loader.

<!-- example: glyport-local-typed-component-recovery -->
```python
class MarkedFailure(GSGlyphsInfo):
    def updateComponentsInfos(self):
        raise InfoNativeException("owned component failure")

with owned_lifecycle() as (provider, url, data):
    manager = MarkedFailure.alloc().initWithLocalFile_(url)
    failures = [event[1] for event in provider.events if event[0] == "log"]
    assert any(isinstance(error, InfoNativeException) for error in failures)
    assert manager._lifecycle.iMatraCombinations is provider.dictionary
    assert not manager._lifecycle.queue.pending
    assert manager._index.records[0].index == 0
```

<!-- example: glyport-local-exception-keeps-pending -->
```python
class OrdinaryFailure(GSGlyphsInfo):
    def updateComponentsInfos(self):
        raise RuntimeError("owned ordinary failure")

with owned_lifecycle() as (provider, url, data):
    receiver = OrdinaryFailure.alloc()
    try:
        receiver.initWithLocalFile_(url)
    except RuntimeError as error:
        assert str(error) == "owned ordinary failure"
    else:
        raise AssertionError("Ordinary exceptions must propagate")
    queue = receiver._lifecycle.queue
    assert queue.pending and ("wait", queue) not in provider.events
    assert receiver._lifecycle.iMatraCombinations is None
    assert not any(event[0] == "log" and isinstance(event[1], RuntimeError)
                   for event in provider.events)
```

### Summaries use the receiver's current arrays and rows

The summary takes distinct script/subcategory values from current listed rows,
sorts new values with the supplied comparison policy, preserves existing repeats,
adds `Conjunct` after `Halfform` when present, and removes empty strings. Each
field reads the current rows separately. A nil field requires an explicit
collection policy; Python truthiness is not a substitute for Foundation KVC.

<!-- example: glyport-local-summary-current-rows -->
```python
from fontlab_glyport.glyphsapp.info_lifecycle import summarize

with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(url)
    state = manager._lifecycle
    state.scriptIDs = ["", "repeat", "repeat"]
    state.categories = ["", "Letter"]
    state.subCategories = ["Halfform", ""]
    state.index.records = [SimpleNamespace(script="zeta", subCategory="Wrong"),
                           SimpleNamespace(script="alpha", subCategory="Wrong2")]
    compare = provider.compare
    def replace_rows(left, right):
        state.index.records = [SimpleNamespace(script=None, subCategory="New")]
        return compare(left, right)
    provider.compare = replace_rows
    summarize(manager)
    assert state.scriptIDs == ["repeat", "repeat", "alpha", "zeta"]
    assert state.subCategories == ["Halfform", "Conjunct", "New"]
    assert state.categories == ["Letter"]
```

### Treat resource lifetimes and unsupported effects separately

Sidebar category/language arrays are cached process-wide on first access,
including a decoded nil result. Changing providers later does not refresh that
cache. Custom group files retain provider order; a bad property list stops its
folder after earlier mutations and schedules error presentation. An empty primary
filter array suppresses fallback; an unavailable primary can select the standard
resource. Extra filter headers retain filename titles, source paths and ordering.
Image type checks, decoding, registration and template marking remain explicit
dependencies. The fixture's empty image directories prove none of those native
effects, and its recorded emoji object proves only the provider call boundary.

Complete lawful default/private resources, predicates, images/counts,
observation lifetime, concurrency and document reload binding remain unqualified.
The following generation examples qualify actual algorithms over invented inputs;
they do not qualify the missing proprietary banks or native resource loading.
Python group-lock identity differs from the native current dictionary monitor; this sequential example does not establish concurrency parity.
Original font workflows, native history/lifetime/preservation/save/reopen,
ordinary installed tuples and complete consumers require independent evidence.
Generated reference, source-lock refresh, site/archive/routes, browser
accessibility and publication remain gated. The full issue remains active.

## Run complete generation over explicit owned inputs

Run each `glyport-generation-*` example after both setup blocks above, in a
fresh directory. The four banks are invented strings supplied by this guide.
They are not the missing proprietary lists. The underscored entry points and
record storage checks below are source-contract controls, not a native installer.

### Inspect every fixed Chinese range and profile lookup

The constructor runs the complete fixed ranges, which contain 38,206 positions,
and the four supplied bank entries. Prefix selection belongs to each range or
list primitive. `sortName` has its own prefix. Generated rows are locked Han
letters; each listed row receives its position as its index after generation.
The summary runs at the intermediate barrier before those rows are appended,
so its script list need not contain `han`.

<!-- example: glyport-generation-fixed-ranges-profiles -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    assert manager is not GSGlyphsInfo.sharedManager()
    assert len(manager._index.records) == 71 + 38206 + 4
    ranges = [(0x2E80, 0x2E99), (0x2E9B, 0x2EF3), (0x2F00, 0x2FD5),
              (0x3400, 0x57EE), (0x57EF, 0x7BDC), (0x7BDD, 0x9FFF),
              (0xF900, 0xFAD9), (0x30000, 0x3134A),
              (0x31350, 0x323AF), (0x2EBF0, 0x2EE5F)]
    for first, last in ranges:
        for scalar in range(first, last + 1):
            code = f"{scalar:04X}"
            row = manager._index.unicodes[code]
            assert row.name == ("uni" if first <= 0xFFFE else "u") + code
            assert row.sortName == ("uni0" if first <= 0xFFFE else "unj") + code
            assert row.script == "han" and row.category == "Letter" and row._locked
            assert manager._index.names[row.name] is row
    assert [row.index for row in manager._index.records] == list(range(38281))
    for gap in ("2E9A", "3134B", "3134F", "323B0", "2EE60"):
        assert manager.infoFromDataForUnicode_(gap) is None
    assert manager.infoFromDataForUnicode_("2E80").subCategory == "Radical"
    assert manager.infoFromDataForUnicode_("F900").subCategory == "Compatibility"
    for code, sort_name, subcategory in [("2FF0", "uni02FF0", "Compatibility"),
                                        ("20000", "unj20000", "Compatibility"),
                                        ("20001", "unj20001", None),
                                        ("20002", "unj20002", None)]:
        row = manager._index.unicodes[code]
        assert (row.sortName, row.subCategory) == (sort_name, subcategory)
    raw = manager.infoFromDataForUnicode_("30000")
    for profile in ("glyphs2", "glyphs3", "glyphs4"):
        app, font = owned_exports(manager, profile)
        assert app.Glyphs.glyphInfoForUnicode(0x30000, font=font) is raw
        assert app.Glyphs.glyphInfoForName("u30000", font=font) is raw
    assert provider.bank_calls[:4] == [0, 1, 2, 3]
    assert "han" not in manager._lifecycle.scriptIDs
```

### Distinguish name collisions from Unicode identity

The generation jobs consult the captured Unicode map before committing their
new rows. A pre-existing encoding suppresses a generated row. A pre-existing
name with another encoding does not. The final name map can therefore select
a new row while the old encoding still selects the original row. Repeated bank
entries remain distinct listed records; the last commit wins in both maps.

<!-- example: glyport-generation-collisions -->
```python
with owned_lifecycle() as (provider, url, data):
    provider.base.write_text(provider.base.read_text() +
        '<glyph name="uni2FF0" unicode="E000" script="owned" subCategory="Other"/>')
    provider.banks = (("2FF0", "2FF0", "0041"), ("20000",), ("20000",), ("20002",))
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    old = manager.infoFromDataForUnicode_("E000")
    current = manager.infoFromDataForName_("uni2FF0")
    assert old.name == current.name and old is not current
    assert old.unicode == "E000" and current.unicode == "2FF0"
    duplicates = [row for row in manager._index.records if row.unicode == "2FF0"]
    assert len(duplicates) == 2 and duplicates[0] is not duplicates[1]
    assert current._resolved_record is duplicates[-1]
    assert manager.infoFromDataForUnicode_("2FF0") is current
    assert manager.infoFromDataForUnicode_("0041").name == "owned.base"
    assert not any(row.name == "uni0041" for row in manager._index.records)
    repeated = [row for row in manager._index.records if row.unicode == "20000"]
    assert len(repeated) == 2 and repeated[0] is not repeated[1]
    assert manager._index.unicodes["20000"] is repeated[-1]
    assert manager._index.names["u20000"] is repeated[-1]
```

### Keep chunk completion order visible

Each Chinese callback collects a whole chunk before publishing it. The final
listed order follows callback completion order, and the commit uses the captured
name and Unicode maps. This invented reverse scheduler runs every callback and
all fixed ranges, but finishes the last submitted job first. It demonstrates a
second permitted order; it does not model concurrent native queue timing.

<!-- example: glyport-generation-chunk-completion -->
```python
class ReverseQueue(OwnedQueue):
    def waitUntilAllOperationsAreFinished(self):
        self.events.append(("wait", self))
        while self.pending:
            self.pending.pop()()

with owned_lifecycle() as (provider, url, data):
    def reverse_queue():
        queue = ReverseQueue(provider.events)
        provider.queues.append(queue)
        return queue
    provider.new_queue = reverse_queue
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    rows = manager._index.records
    assert len(rows) == 38281
    assert rows[71].name == "u2EBF0" and rows[-1].name == "uni2FD5"
    assert manager._index.unicodes["2EBF0"] is rows[71]
    assert manager._index.names["uni2FD5"] is rows[-1]
    assert all(row.index == position for position, row in enumerate(rows))
    assert manager._index.unicodes["AC00"]._component_records == (
        manager._index.unicodes["1100"], manager._index.unicodes["1161"])
    assert not manager._lifecycle.queue.pending
```

### Match actual Hangul target and Jamo identities

The queued operation visits every syllable from `AC00` through `D7A3`. For each
one it looks up the target, leading Jamo, vowel Jamo and optional trailing Jamo,
in that order. This example checks the three supplied syllable targets against
Unicode NFD and checks their exact component-record identities. It exercises the
complete operation even though the fixture stores only three syllable targets.
Unicode NFD supplies an independent scalar oracle, not a proprietary recipe bank.

<!-- example: glyport-generation-hangul-tuples -->
```python
import unicodedata

with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    for code in (0xAC00, 0xAC01, 0xD7A3):
        target = manager._index.unicodes[f"{code:04X}"]
        expected = tuple(manager._index.unicodes[f"{ord(part):04X}"]
                         for part in unicodedata.normalize("NFD", chr(code)))
        assert len(expected) == (2 if code == 0xAC00 else 3)
        assert target._component_records == expected
        assert all(actual is wanted for actual, wanted in zip(target._component_records, expected))
        assert target._locked and target.baseString == chr(code)
        view = manager.infoFromDataForUnicode_(f"{code:04X}")
        assert all(part._resolved_record is raw for part, raw in zip(view.components, expected))
    assert not manager._lifecycle.queue.pending
```

### Preserve locks and caches when replacing component storage

The generated-component adapter replaces the raw component tuple, clears its
old name list and removes only the `components` unavailable-field marker. It
does not rerun general component finalization or rebuild unrelated caches.
The following snapshot checks every existing raw field by identity.

<!-- example: glyport-generation-storage-preservation -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    raw = manager._index.unicodes["AC00"]
    raw.baseString, raw.unicharString = "keep base", "keep cached text"
    raw._component_names = ["old names"]
    raw._unavailable_fields = frozenset({"components", "owned unknown"})
    before = vars(raw).copy()
    manager._addHangulGlyphInfos()
    assert raw._component_names is before["_component_names"]
    manager._lifecycle.queue.waitUntilAllOperationsAreFinished()
    assert raw._component_records == (manager._index.unicodes["1100"], manager._index.unicodes["1161"])
    assert raw._component_names is None
    assert raw._unavailable_fields == frozenset({"owned unknown"})
    for field in before.keys() - {"_component_records", "_component_names", "_unavailable_fields"}:
        assert vars(raw)[field] is before[field], field
```

### Resolve the current Unicode map after enqueue

Enqueuing captures the manager, not a frozen index snapshot. Replacing a target
or Jamo in its Unicode map before execution changes the later component links.
These direct map assignments are owned source controls; production callers
should use their qualified loading path.

<!-- example: glyport-generation-hangul-current-index -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    old = manager._index.unicodes["AC00"]
    retained = old._component_records
    manager._addHangulGlyphInfos()
    target, vowel = new_record("owned.new.target"), new_record("owned.new.vowel")
    add_unicode(target, "AC00")
    add_unicode(vowel, "1161")
    manager._index.unicodes["AC00"] = target
    manager._index.unicodes["1161"] = vowel
    assert target._component_records is None
    manager._lifecycle.queue.waitUntilAllOperationsAreFinished()
    assert target._component_records == (manager._index.unicodes["1100"], vowel)
    assert target._component_records[1] is vowel
    assert old._component_records is retained
    assert manager.infoFromDataForName_("owned.AC00")._resolved_record is old
    assert manager.infoFromDataForUnicode_("AC00")._resolved_record is target
```

### Retain partial writes and pending work on deferred failure

The following subclass explicitly injects a missing Jamo lookup. A real lookup
may synthesize a result, so deleting a raw map key alone does not establish a nil
lookup. The full queued operation completes `AC00`, then fails while constructing
the `AC01` component tuple. Its error escapes the wait; the earlier assignment
and the unrelated later queue entry remain. The constructor's protected enqueue
interval does not catch an error raised by a later callback.

<!-- example: glyport-generation-hangul-missing-queued -->
```python
class MissingTrailing(GSGlyphsInfo):
    def glyphInfoForUnicode_(self, code):
        return None if code == "11A8" else super().glyphInfoForUnicode_(code)

with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.alloc().initWithLocalFile_(None)
    receiver = MissingTrailing._from_index(manager._index)
    receiver._lifecycle = manager._lifecycle
    target = manager._index.unicodes["AC00"]
    target._component_records = None
    receiver._addHangulGlyphInfos()
    marker = []
    receiver._lifecycle.queue.addOperationWithBlock_(lambda: marker.append("later"))
    try:
        receiver._lifecycle.queue.waitUntilAllOperationsAreFinished()
    except InfoNativeException as error:
        assert "AC01" in str(error) and "nil" in str(error)
    else:
        raise AssertionError("Missing Jamo must refuse the deferred tuple")
    assert target._component_records == (manager._index.unicodes["1100"], manager._index.unicodes["1161"])
    assert len(receiver._lifecycle.queue.pending) == 1 and marker == []
```

### Refuse an unavailable Chinese bank explicitly

The full generator requires each of four lawful lists or tuples of strings.
An absent bank is a dependency refusal; it does not become an empty successful
callback. The constructor below fails during the Chinese intermediate barrier.
It does not append any partially collected Chinese rows or drain the remaining
jobs on unwind. The supplied base rows remain and later work stays queued.

<!-- example: glyport-generation-missing-bank -->
```python
from fontlab_glyport.errors import UnsupportedCapability

with owned_lifecycle() as (provider, url, data):
    provider.chinese_codes = lambda slot: None if slot == 2 else provider.banks[slot]
    receiver = GSGlyphsInfo.alloc()
    try:
        receiver.initWithLocalFile_(None)
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphsInfo.provider.chinese_codes"
    else:
        raise AssertionError("Missing lawful bank must refuse initialization")
    assert len(receiver._index.records) == 71
    assert "2E80" not in receiver._index.unicodes
    assert receiver._lifecycle.queue.pending
    assert receiver._lifecycle.iMatraCombinations is None
```

## Read the source contract

The checkpoint's `glyphsapp/info_manager.py`, `glyphsapp/application.py`,
`glyphsapp/application_profiles.py`, `model/glyph_metadata.py`,
`model/stored_glyph_fields.py`, `model/info_records.py`, `model/custom_info.py`,
`model/custom_info_parser.py`, `model/info_finalize.py` and
`model/custom_info_discovery.py` define these bounded source operations.
The connected lifecycle also uses `glyphsapp/info_lifecycle.py`,
`info_runtime.py`, `info_shared.py`, `info_sidebar.py`,
`info_sidebar_resources.py`, `info_filters.py`, `info_images.py` and
`model/base_info_parser.py`, plus the complete-generation implementations
`info_chinese.py`, `info_hangul.py`, `info_generated.py` and `model/info_hex.py`.
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
