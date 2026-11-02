---
this_file: src_docs/md/guide/glyport-manager-state.md
---

# Keep manager state, ranks and placeholder fonts distinct

A glyph-info manager holds several graphs at once: raw records and indexes,
sidebar groups, lazy rank caches, a work queue and observer state. A new list
does not necessarily mean a new index, and changing a list does not necessarily
invalidate its cached order. These experiments show the actual source-derived
behavior and its failure boundaries.

The described implementation is pinned to Glyport
`5e04d1168b4e33823bed4940fce308637f8abadd`. It has source and package-archive
verification. Matching Echopy declarations, ordinary installations and native
FontLab workflows require their own verification.

Start with [metadata managers and execution profiles](glyport-managers.md) for
lookup and complete local initialization, then
[sidebar trees and document metadata](glyport-sidebar.md) for projected groups,
counts and URL loading. This page covers raw accessor identity, retained rank
caches, debug/shared construction, observation, placeholder fonts and recovery.

## Prepare three visible setups

For each tagged experiment, use a fresh namespace. Execute the
[owned graph setup](glyport-managers.md#prepare-an-owned-graph), then the
`glyport-local-lifecycle` setup in
[connected local initialization](glyport-managers.md#construct-and-reload-a-local-manager-with-explicit-dependencies),
then the setup below, and finally that single experiment. Do not carry a prior
experiment's globals or mutations into the next one.

The examples call the actual exported `GSGlyphsInfo` class. Attaching
`InfoState` is an explicit implementation-level source experiment, not complete
resource initialization. The two shared-constructor examples instead run the
actual parser/sidebar/lifecycle and queued algorithms with the existing visible
invented lifecycle provider.

The following provider supplies individual operations only. It does not build
rank caches, implement manager initialization, parse glyph data, choose a font,
manage the global placeholder cache or perform error recovery. Its dictionaries
and font tokens are owned Python models. The CF callback names are adapter
contracts; they are not native pointers. No font file, framework, defaults
database, application or workspace is accessed.

<!-- setup: glyport-owned-manager-state -->
```python
from contextlib import contextmanager
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSGlyphsInfo
from fontlab_glyport.glyphsapp.info_runtime import (
    InfoErrorSlot, InfoState, using_info_provider,
)
from fontlab_glyport.glyphsapp import info_manager_observation

OBSERVER_KEY = "values.GSScriptToPlaceholderFontPath"

class ManagerQueue:
    def __init__(self, provider):
        self.provider, self.maximum, self.pending = provider, None, []
    def setMaxConcurrentOperationCount_(self, value):
        self.provider.events.append(("limit", value))
        self.maximum = value
    def addOperationWithBlock_(self, callback):
        self.pending.append(callback)
    def waitUntilAllOperationsAreFinished(self):
        self.provider.events.append(("wait", self))
        while self.pending:
            self.pending.pop(0)()

class ManagerPrimitives:
    def __init__(self, label="owned"):
        self.label, self.events, self.queues = label, [], []
        self.cpu_count, self.rows, self.font_files = 7, [], {}
        self.fail_store = False
    def new_queue(self):
        self.events.append(("new-queue",))
        queue = ManagerQueue(self)
        self.queues.append(queue)
        return queue
    def active_processor_count(self):
        self.events.append(("processors",))
        if isinstance(self.cpu_count, Exception):
            raise self.cpu_count
        return self.cpu_count
    def defaults_object_for_key(self, key):
        assert key == "GSScriptToPlaceholderFontPath"
        self.events.append(("defaults", key))
        return self.rows
    def cf_dictionary_create_mutable(self, allocator, capacity, keys, values):
        assert allocator is None
        assert keys == "kCFTypeDictionaryKeyCallBacks"
        assert values == "kCFTypeDictionaryValueCallBacks"
        self.events.append(("dictionary", capacity))
        return {}
    def cg_font_with_file_path(self, path):
        self.events.append(("load-font", path))
        value = self.font_files.get(path)
        if isinstance(value, Exception):
            raise value
        return value
    def cf_dictionary_set_value(self, dictionary, key, value):
        self.events.append(("store-font", key, value))
        if self.fail_store:
            raise RuntimeError("owned store failure")
        dictionary[key] = value
    def cf_release(self, value):
        self.events.append(("release", value))
    def cf_dictionary_get_value(self, dictionary, key):
        self.events.append(("lookup", key))
        return None if dictionary is None else dictionary.get(key)
    def ct_font_create_with_graphics_font(self, font, size, matrix, attributes):
        assert matrix is None and attributes is None
        self.events.append(("sized-font", font, size))
        return SimpleNamespace(graphics=font, size=size, provider=self.label)
    def add_observer(self, receiver, key, options, context):
        self.events.append(("add-observer", receiver, key, options, context))
    def remove_observer(self, receiver, key):
        self.events.append(("remove-observer", receiver, key))
    def super_dealloc(self, receiver):
        self.events.append(("super-dealloc", receiver))
    def present_error(self, error):
        self.events.append(("present-error", error))
        return False
    def select_file_in_viewer(self, path, root):
        self.events.append(("reveal-file", path, root))
        return False

def owned_state_manager(provider=None):
    provider = ManagerPrimitives() if provider is None else provider
    manager = GSGlyphsInfo.alloc()
    state = manager._lifecycle = InfoState(provider, None)
    manager._fixed_index = state.index
    return manager, state

@contextmanager
def owned_placeholder_cache():
    saved = info_manager_observation._script_to_placeholder_font_cache
    info_manager_observation._script_to_placeholder_font_cache = None
    try:
        yield
    finally:
        info_manager_observation._script_to_placeholder_font_cache = saved

@contextmanager
def owned_shared_pointer(value):
    saved = GSGlyphsInfo._shared
    GSGlyphsInfo._shared = value
    try:
        yield
    finally:
        GSGlyphsInfo._shared = saved
```

The two context managers isolate this process's owned source experiments and
restore the exact previous objects. Assigning these private globals is not a
supported application cache-refresh or singleton-management API. Explicit
`dealloc` examples record a superclass primitive; they do not destroy a native
object. Do not call these model helpers or manual destruction experiments on
FontLab's live native objects.

## Inspect the current graph without making a copy

### Read the raw containers

These getters return exact current storage. A read through `name2Info` sees
later mutations to that same dictionary; it does not build a detached snapshot.

<!-- example: glyport-manager-raw-identity -->
```python
manager, state = owned_state_manager()
row = SimpleNamespace(name="owned.raw")
rows, names, codes = [row], {"owned.raw": row}, {"0041": row}
state.index.records, state.index.names, state.index.unicodes = rows, names, codes
state.scriptIDs, state.sidebarCategories = ["owned"], ["Letter"]
state.categories, state.subCategories = ["Mark"], ["Above"]
state.iMatraCombinations = {"owned": "combination"}
assert manager.glyphInfos() is rows
assert manager.name2Info() is names and manager.unicode2Info() is codes
assert manager.scriptIDs() is state.scriptIDs
assert manager.sidebarCategories() is state.sidebarCategories
assert manager.categories() is state.categories
assert manager.subCategories() is state.subCategories
assert manager.iMatraCombinations() is state.iMatraCombinations
names["owned.alias"] = row
assert manager.name2Info()["owned.alias"] is row
```

### Store the supplied object, including nil

The list and group setters neither copy nor normalize. Each getter returns the
identical assigned object. Python `None` represents the owned model's nil.

<!-- example: glyport-manager-setter-identity -->
```python
manager, state = owned_state_manager()
pairs = [
    (manager.setGlyphInfos_, manager.glyphInfos),
    (manager.setLanguagesGroup_, manager.languagesGroup),
    (manager.setCategoriesGroup_, manager.categoriesGroup),
    (manager.setAllItem_, manager.allItem),
    (manager.setFilterGroups_, manager.filterGroups),
]
for setter, getter in pairs:
    supplied = ["owned"]
    setter(supplied)
    assert getter() is supplied
    supplied.append("later")
    assert getter() == ["owned", "later"]
    setter(None)
    assert getter() is None
assert state.index.records is None
```

### Distinguish a nil category from missing initialized state

A nil category returns nil before checking the manager lifecycle. A real
category reads the current subcategory-order dictionary and returns its value
without copying it.

<!-- example: glyport-manager-subcategory-identity -->
```python
uninitialized = GSGlyphsInfo.alloc()
assert uninitialized._subcategoriesForSidebarCategory_(None) is None
manager, state = owned_state_manager()
values = ["Above", "Below"]
state.subCategoryOrder = {"Mark": values}
assert manager._subcategoriesForSidebarCategory_("Mark") is values
assert manager._subcategoriesForSidebarCategory_("Letter") is None
state.subCategoryOrder = None
assert manager._subcategoriesForSidebarCategory_("Mark") is None
```

## Use the correct order source

### Script ranks use the current script list when first built

Repeated keys overwrite earlier positions. A missing key returns the retained
NSNotFound value, `2**63 - 1`, rather than `-1` or a new appended rank.

<!-- example: glyport-manager-script-ranks -->
```python
manager, state = owned_state_manager()
state.scriptIDs = ["latin", "owned", "latin"]
assert state.scriptOrder is None
assert manager.indexOfObjectInScripts_("owned") == 1
assert manager.indexOfObjectInScripts_("latin") == 2
assert manager.indexOfObjectInScripts_("absent") == 2**63 - 1
assert list(state.scriptOrder) == ["latin", "owned"]
```

### Category ranks use sidebarCategories, then four terminal names

The generic category list is a different field. After enumerating sidebar
categories, the algorithm assigns Icon, SF-Symbol, Private Use and Corner
successive terminal positions. Their exact spellings matter.

<!-- example: glyport-manager-category-ranks -->
```python
manager, state = owned_state_manager()
state.categories = ["Wrong list"]
state.sidebarCategories = ["Mark", "Icon", "Letter", "Mark"]
assert manager.indexOfObjectInCategories_("Mark") == 3
assert manager.indexOfObjectInCategories_("Letter") == 2
assert manager.indexOfObjectInCategories_("Wrong list") == 2**63 - 1
assert [manager.indexOfObjectInCategories_(key) for key in
        ["Icon", "SF-Symbol", "Private Use", "Corner"]] == [4, 5, 6, 7]
assert manager.indexOfObjectInCategories_("PrivateUse") == 2**63 - 1
```

### Mutating a list does not refresh an already built rank cache

No rank invalidation is implied by a raw list change or group setter. This is
useful when diagnosing a view whose raw category list and cached order disagree.
The experiment observes that state; it does not recommend assigning private
cache fields in an application.

<!-- example: glyport-manager-retained-ranks -->
```python
manager, state = owned_state_manager()
state.scriptIDs, state.sidebarCategories = ["latin"], ["Letter"]
assert manager.indexOfObjectInScripts_("latin") == 0
assert manager.indexOfObjectInCategories_("Letter") == 0
script_cache, category_cache = state.scriptOrder, state.categoryOrder
state.scriptIDs[:] = ["owned"]
state.sidebarCategories[:] = ["Mark"]
manager.setCategoriesGroup_(["different group"])
assert manager.indexOfObjectInScripts_("latin") == 0
assert manager.indexOfObjectInScripts_("owned") == 2**63 - 1
assert manager.indexOfObjectInCategories_("Letter") == 0
assert manager.indexOfObjectInCategories_("Mark") == 2**63 - 1
assert state.scriptOrder is script_cache and state.categoryOrder is category_cache
```

The source checks for nil before synchronizing, then builds unconditionally
inside the manager monitor. It publishes the cache before enumeration. Lookup
locks the captured cache object but reads the current field. Owned RLocks and
dictionaries do not establish Foundation key copying, fast-enumeration mutation
counters, exception ABI or native concurrency. Stored ranks use signed 32-bit
arithmetic and are returned as unsigned 64-bit values.

## Debug initialization is a smaller operation

### Allocate a queue and group dictionary, leaving raw indexes nil

`initDebug` creates a queue, queries the current active processor count,
configures the then-current queue, then replaces name2Group. It does not load
glyph data, create sidebar groups or register an observer. name2Group is not
name2Info.

<!-- example: glyport-manager-debug-initial -->
```python
provider, manager = ManagerPrimitives(), GSGlyphsInfo.alloc()
with using_info_provider(provider):
    assert manager.initDebug() is manager
state = manager._lifecycle
assert state.queue is provider.queues[0] and state.queue.maximum == 7
assert state.name2Group == {} and state.index.names is None
assert state.index.records is None and state.index.unicodes is None
assert state.scriptIDs is None and state.categoriesGroup is None
assert state.observer_flag == 0 and state.localURL is None and not state.shared
assert provider.events == [("new-queue",), ("processors",), ("limit", 7)]
```

### Reinitialize without clearing unrelated state

Only the queue and group dictionary are replaced. Existing raw containers,
local URL, rank cache and observer flag survive. Changing the explicit provider
changes the primitives used by later source operations.

<!-- example: glyport-manager-debug-reinitialize -->
```python
old_provider, provider = ManagerPrimitives("first"), ManagerPrimitives("second")
manager, state = owned_state_manager(old_provider)
url, old_groups = object(), {"old": object()}
state.localURL, state.name2Group, state.observer_flag = url, old_groups, 3
rows, names, codes = state.index.records, state.index.names, state.index.unicodes
state.scriptIDs = ["latin"]
assert manager.indexOfObjectInScripts_("latin") == 0
cache = state.scriptOrder
with using_info_provider(provider):
    manager.initDebug()
first_queue, first_groups = state.queue, state.name2Group
provider.cpu_count = 3
with using_info_provider(provider):
    manager.initDebug()
assert manager._lifecycle is state and state.localURL is url
assert state.provider is provider and state.observer_flag == 3
assert state.index.records is rows and state.index.names is names
assert state.index.unicodes is codes and state.scriptOrder is cache
assert state.queue is not first_queue and state.queue.maximum == 3
assert state.name2Group is not first_groups and state.name2Group is not old_groups
```

### Let the real base parser adopt initially nil containers

This runs the actual base scanner and commit logic. It does not supply a
precomputed parsed result. The parser installs its row/name/Unicode containers
while retaining the group dictionary created by debug initialization.

<!-- example: glyport-manager-debug-base-adoption -->
```python
provider, manager = ManagerPrimitives(), GSGlyphsInfo.alloc()
with using_info_provider(provider):
    manager.initDebug()
groups = manager._lifecycle.name2Group
with TemporaryDirectory(dir=Path.cwd()) as temporary:
    source = Path(temporary) / "OwnedGlyphData.xml"
    source.write_text('<glyph name="owned.debug" unicode="0041" '
                      'category="Letter" script="latin"/>', encoding="utf-8")
    url = SimpleNamespace(path=lambda: str(source))
    assert manager.loadGlyphDataFromURL_error_(url, None) is True
row = manager.glyphInfos()[0]
assert manager.name2Info()["owned.debug"] is row
assert manager.unicode2Info()["0041"] is row
assert manager.infoFromDataForName_("owned.debug") is manager.infoFromDataForUnicode_("0041")
assert manager._lifecycle.name2Group is groups
assert len(provider.queues) == 1 and provider.queues[0].maximum == 7
```

### Separate missing-file false/nil from an actual parse error

A normal open failure returns false with a nil error. A qualified malformed
attribute returns false with an error. Neither commits raw containers. Unknown
native row-prefix/recovery behavior can still refuse as an unsupported
capability; an arbitrary malformed string is not evidence of an ordinary
parser error.

<!-- example: glyport-manager-debug-base-failure -->
```python
provider, manager = ManagerPrimitives(), GSGlyphsInfo.alloc()
with using_info_provider(provider):
    manager.initDebug()
groups = manager._lifecycle.name2Group
with TemporaryDirectory(dir=Path.cwd()) as temporary:
    folder = Path(temporary)
    missing = SimpleNamespace(path=lambda: str(folder / "absent.xml"))
    slot = InfoErrorSlot()
    assert manager.loadGlyphDataFromURL_error_(missing, slot) is False
    assert slot.value is None
    malformed = folder / "OwnedMalformed.xml"
    malformed.write_text("<glyph name=/>", encoding="utf-8")
    bad = SimpleNamespace(path=lambda: str(malformed))
    assert manager.loadGlyphDataFromURL_error_(bad, slot) is False
    assert slot.value is not None
assert manager.glyphInfos() is None and manager.name2Info() is None
assert manager.unicode2Info() is None and manager._lifecycle.name2Group is groups
```

### Preserve the partial queue when a primitive fails

A processor-count failure occurs after queue assignment and before group
replacement. A missing queue primitive is an explicit capability gap, not a
successful empty initialization.

<!-- example: glyport-manager-debug-partial-failure -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
groups = state.name2Group = {"keep": object()}
provider.cpu_count = RuntimeError("owned processor failure")
with using_info_provider(provider):
    try:
        manager.initDebug()
    except RuntimeError as error:
        assert str(error) == "owned processor failure"
    else:
        raise AssertionError("The failing primitive must propagate")
assert state.queue is provider.queues[0] and state.queue.maximum is None
assert state.name2Group is groups
other = GSGlyphsInfo.alloc()
with using_info_provider(object()):
    try:
        other.initDebug()
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphsInfo.provider.new_queue"
    else:
        raise AssertionError("Missing queue allocation must refuse")
assert other._lifecycle.queue is None and other._lifecycle.name2Group is None
```

## Shared construction and observer lifetime

### Run actual loading before registering the shared observer

This example executes the actual shared constructor, parser, sidebar builder,
complete fixed generation algorithms over the four visible invented banks and
queued summaries/linking from the earlier lifecycle setup. Only the individual
resource/queue primitives come from that setup. Observer registration follows
the final queue drain.

<!-- example: glyport-manager-shared-drain-register -->
```python
with owned_lifecycle() as (provider, url, data):
    manager = GSGlyphsInfo.sharedManager()
    state = manager._lifecycle
    assert GSGlyphsInfo._shared is manager and state.shared
    assert state.observer_flag == 1
    assert manager.name2Info()["owned.base"] is state.index.names["owned.base"]
    assert manager.categoriesGroup() is state.categoriesGroup
    assert manager.glyphInfos() is state.index.records
    assert provider.bank_calls == [0, 1, 2, 3]
    assert len(manager.glyphInfos()) == 38281
    assert [row.index for row in manager.glyphInfos()] == list(range(38281))
    assert manager.infoFromDataForUnicode_("30000").script == "han"
    assert all(not queue.pending for queue in provider.queues)
    assert provider.events[-1] == (
        "observer", (manager, OBSERVER_KEY, 0, None))
    assert provider.events[-2][0] == "wait"
```

### Retain an existing local URL and the observer flag's low bit

Reinitializing an allocated local-state receiver through plain init retains its
URL and state identity. Flag3 already has the low bit set, so registration is
skipped. Exact-1 removal is a different condition, shown next.

<!-- example: glyport-manager-shared-existing-state -->
```python
with owned_lifecycle() as (provider, url, data):
    manager, state = owned_state_manager(provider)
    state.localURL, state.observer_flag = url, 3
    groups = state.name2Group = {}
    assert manager.init() is manager
    assert manager._lifecycle is state and state.localURL is url and state.shared
    assert state.name2Group is groups and state.observer_flag == 3
    assert manager.name2Info()["owned.local"].name == "owned.local"
    assert not any(event[0] == "observer" for event in provider.events)
    assert all(not queue.pending for queue in provider.queues)
```

### Remove the current global shared receiver, then dispatch superclass cleanup

The source removes only when the original receiver flag equals exactly1.
It removes the current global shared receiver, which need not be the original
receiver. Every successful path then sends the explicit superclass primitive.
The fixture records this dispatch without performing native destruction.

<!-- example: glyport-manager-dealloc-current-shared -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
current = object()
state.observer_flag = 1
with owned_shared_pointer(current):
    assert manager.dealloc() is None
assert provider.events == [
    ("remove-observer", current, OBSERVER_KEY),
    ("super-dealloc", manager),
]
assert state.observer_flag == 0
provider.events.clear()
state.observer_flag = 3
with owned_shared_pointer(current):
    manager.dealloc()
assert provider.events == [("super-dealloc", manager)]
assert state.observer_flag == 3
```

### A failed removal neither clears the flag nor destroys the receiver

Failure order matters for recovery. The superclass primitive must not run after
a failing observer-removal primitive; unrelated state remains available.

<!-- example: glyport-manager-dealloc-failure -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
state.observer_flag = 1
groups = state.categoriesGroup = ["owned"]
def fail_remove(receiver, key):
    provider.events.append(("remove-failed", receiver, key))
    raise RuntimeError("owned removal failure")
provider.remove_observer = fail_remove
with owned_shared_pointer(manager):
    try:
        manager.dealloc()
    except RuntimeError as error:
        assert str(error) == "owned removal failure"
    else:
        raise AssertionError("Failed removal must propagate")
assert provider.events == [("remove-failed", manager, OBSERVER_KEY)]
assert state.observer_flag == 1 and state.categoriesGroup is groups
```

## Treat placeholder fonts as an explicit primitive contract

### Last successful duplicate wins; nil loads do not replace it

`fontForScript_size_` is a **class selector**. A first cache miss reads defaults,
creates and publishes a CF dictionary, then loads rows in order. Each nonnil
graphics font is stored before its release. Missing files leave prior successful
entries intact. The result below is an owned sized-font token.

<!-- example: glyport-manager-font-duplicates -->
```python
provider = ManagerPrimitives()
first, second = object(), object()
provider.rows = [
    ["latin", "first"], ["latin", "missing"],
    ["latin", "second"], ["greek", "also-missing"],
]
provider.font_files = {"first": first, "second": second}
with owned_placeholder_cache(), using_info_provider(provider):
    answer = GSGlyphsInfo.fontForScript_size_("latin", 13.5)
    assert answer.graphics is second and answer.size == 13.5
    assert GSGlyphsInfo.fontForScript_size_("greek", 9) is None
    cache = info_manager_observation._script_to_placeholder_font_cache
    assert cache == {"latin": second}
assert [event for event in provider.events if event[0] == "release"] == [
    ("release", first), ("release", second)]
assert [event[1] for event in provider.events if event[0] == "load-font"] == [
    "first", "missing", "second", "also-missing"]
```

### Keep a published partial cache after a later load fails

There is no retry or rollback hidden inside the class selector. A later lookup
uses the surviving nonnil cache; merely fixing the provider input does not
restart enumeration.

<!-- example: glyport-manager-font-partial-cache -->
```python
provider, font = ManagerPrimitives(), object()
provider.rows = [["latin", "first"], ["greek", "broken"]]
provider.font_files = {"first": font, "broken": RuntimeError("owned font failure")}
with owned_placeholder_cache(), using_info_provider(provider):
    try:
        GSGlyphsInfo.fontForScript_size_("latin", 10)
    except RuntimeError as error:
        assert str(error) == "owned font failure"
    else:
        raise AssertionError("A later failing font load must propagate")
    cache = info_manager_observation._script_to_placeholder_font_cache
    assert cache == {"latin": font}
    provider.font_files["broken"] = object()
    assert GSGlyphsInfo.fontForScript_size_("greek", 11) is None
    assert GSGlyphsInfo.fontForScript_size_("latin", 12).graphics is font
    assert info_manager_observation._script_to_placeholder_font_cache is cache
assert sum(event[0] == "load-font" for event in provider.events) == 2
```

### Invalidation drops the pointer without releasing the dictionary

The next class lookup rebuilds. The source invalidator performs no CFRelease of
the old dictionary or its values. The earlier per-font releases remain recorded;
there is no invented extra ownership operation.

<!-- example: glyport-manager-font-invalidate -->
```python
provider, first, second = ManagerPrimitives(), object(), object()
provider.rows, provider.font_files = [["latin", "first"]], {"first": first}
manager, state = owned_state_manager(provider)
with owned_placeholder_cache(), using_info_provider(provider):
    assert GSGlyphsInfo.fontForScript_size_("latin", 10).graphics is first
    old_cache = info_manager_observation._script_to_placeholder_font_cache
    events = list(provider.events)
    manager.setNeedsUpdateScriptToFontCache()
    assert info_manager_observation._script_to_placeholder_font_cache is None
    assert provider.events == events
    provider.rows, provider.font_files = [["latin", "second"]], {"second": second}
    assert GSGlyphsInfo.fontForScript_size_("latin", 20).graphics is second
    assert info_manager_observation._script_to_placeholder_font_cache is not old_cache
assert [event for event in provider.events if event[0] == "release"] == [
    ("release", first), ("release", second)]
```

### Missing primitives are capability gaps even when inputs look empty

An explicit empty list is a fixture choice; it does not authorize a missing
defaults or CF primitive to succeed. No framework is imported to fill that gap.

<!-- example: glyport-manager-font-missing-primitive -->
```python
with owned_placeholder_cache(), using_info_provider(object()):
    try:
        GSGlyphsInfo.fontForScript_size_("latin", 10)
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphsInfo.provider.defaults_object_for_key"
    else:
        raise AssertionError("Missing defaults primitive must refuse")
    assert info_manager_observation._script_to_placeholder_font_cache is None
with using_info_provider(None):
    try:
        GSGlyphsInfo.fontForScript_size_("latin", 10)
    except UnsupportedCapability as error:
        assert error.capability == "GSGlyphsInfo.initialization.provider"
    else:
        raise AssertionError("The class selector needs an explicit current provider")
```

### Resolve the current provider on every class call

The cache is global across subclasses, but lookup and sized-font creation use
the provider current at that call. A populated cache does not retain the first
call's provider as an implicit default.

<!-- example: glyport-manager-font-current-provider -->
```python
first, second, font = ManagerPrimitives("first"), ManagerPrimitives("second"), object()
first.rows, first.font_files = [["latin", "owned"]], {"owned": font}
class AnotherManager(GSGlyphsInfo):
    pass
with owned_placeholder_cache():
    with using_info_provider(first):
        assert GSGlyphsInfo.fontForScript_size_("latin", 8).provider == "first"
    with using_info_provider(second):
        answer = AnotherManager.fontForScript_size_("latin", 21)
        assert answer.graphics is font and answer.provider == "second"
        assert answer.size == 21
assert second.events == [("lookup", "latin"), ("sized-font", font, 21)]
```

### Observe only the exact retained key

An unrelated or differently capitalized key leaves the pointer alone. The exact
key dispatches the overridable invalidation selector and performs no font load.

<!-- example: glyport-manager-observer-key -->
```python
provider, font = ManagerPrimitives(), object()
provider.rows, provider.font_files = [["latin", "owned"]], {"owned": font}
manager, state = owned_state_manager(provider)
with owned_placeholder_cache(), using_info_provider(provider):
    GSGlyphsInfo.fontForScript_size_("latin", 10)
    cache = info_manager_observation._script_to_placeholder_font_cache
    before = list(provider.events)
    for key in [None, "GSScriptToPlaceholderFontPath", OBSERVER_KEY.lower()]:
        manager.observeValueForKeyPath_ofObject_change_context_(key, object(), {}, None)
        assert info_manager_observation._script_to_placeholder_font_cache is cache
    manager.observeValueForKeyPath_ofObject_change_context_(OBSERVER_KEY, None, None, None)
    assert info_manager_observation._script_to_placeholder_font_cache is None
    assert provider.events == before
```

The cache deliberately follows the retained unsynchronized publication and
current-global-field reads. These serial examples do not establish native race,
CF retain/release, font decoding, key equality, defaults or fast-enumeration
semantics. A production adapter must supply and qualify those individual
operations; an owned Python token is not a usable native font.

## Preserve error and recovery order

### Present the retained domain, code and message fields

`reportInfoError` constructs the source English fields and ignores the
presentation return value. The error below is an owned InfoError subclass;
native NSError identity and localization remain unqualified.

<!-- example: glyport-manager-error-presentation -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
assert manager.reportInfoError() is None
label, error = provider.events[0]
assert label == "present-error"
assert error.domain() == "GSGlyphsDomain" and error.code() == 1
assert error.localizedDescription() == "There was a problem loading glyph data"
assert error.localizedRecoverySuggestion() == (
    "Please make sure the app is not damaged and maybe re-download it.")
assert error.userInfo()["NSLocalizedDescription"] == error.localizedDescription()
```

### Reveal a path only for the retained codes and option1

The workspace primitive receives FilePath and an empty root string. A false
primitive result is ignored; the manager still returns true after that call.
Other options do not read userInfo or require a reveal primitive.

<!-- example: glyport-manager-recovery-options -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
for code in [0x2AE2, 0x8702]:
    error = SimpleNamespace(code=lambda: code, userInfo=lambda: {"FilePath": "owned.font"})
    assert manager.attemptRecoveryFromError_optionIndex_(error, 1) is True
assert provider.events == [("reveal-file", "owned.font", "")] * 2
provider.events.clear()
def unexpected_info():
    raise AssertionError("Unrelated options must not read userInfo")
for code, option in [(0x2AE2, 0), (0x8702, 2), (17, 1)]:
    error = SimpleNamespace(code=lambda: code, userInfo=unexpected_info)
    assert manager.attemptRecoveryFromError_optionIndex_(error, option) is True
assert provider.events == []
assert GSGlyphsInfo.alloc().attemptRecoveryFromError_optionIndex_(None, 1) is True
```

### Keep both error-code reads in their original order

For a first code other than0x2ae2, the source reads code again before checking the
option. A dynamic error can therefore select0x8702 on the second read. This
experiment exposes that order instead of caching or normalizing the first code.

<!-- example: glyport-manager-recovery-repeated-code -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
events, codes = [], iter([0, 0x8702])
def code():
    value = next(codes)
    events.append(("code", value))
    return value
def info():
    events.append(("userInfo",))
    return {"FilePath": "owned.second"}
error = SimpleNamespace(code=code, userInfo=info)
assert manager.attemptRecoveryFromError_optionIndex_(error, 1) is True
assert events == [("code", 0), ("code", 0x8702), ("userInfo",)]
assert provider.events == [("reveal-file", "owned.second", "")]
events.clear()
codes = iter([0, 0x8702])
assert manager.attemptRecoveryFromError_optionIndex_(error, 0) is True
assert events == [("code", 0), ("code", 0x8702)]
```

### Forward nil paths and propagate a failing reveal

The source does not replace missing FilePath with the current document or a
working directory. A failing workspace primitive propagates before a successful
return. No real file-viewer action occurs in this owned experiment.

<!-- example: glyport-manager-recovery-nil-failure -->
```python
provider = ManagerPrimitives()
manager, state = owned_state_manager(provider)
error = SimpleNamespace(code=lambda: 0x2AE2, userInfo=lambda: None)
assert manager.attemptRecoveryFromError_optionIndex_(error, 1) is True
assert provider.events == [("reveal-file", None, "")]
def fail_reveal(path, root):
    provider.events.append(("reveal-failed", path, root))
    raise RuntimeError("owned viewer failure")
provider.select_file_in_viewer = fail_reveal
try:
    manager.attemptRecoveryFromError_optionIndex_(error, 1)
except RuntimeError as caught:
    assert str(caught) == "owned viewer failure"
else:
    raise AssertionError("A failing reveal must propagate before return")
assert provider.events[-1] == ("reveal-failed", None, "")
```

## What these experiments establish

The examples exercise the installed package's actual source-derived algorithms
with visible invented inputs. They distinguish raw/current objects, retained
caches, class-versus-instance dispatch, queue completion, observer conditions,
partial failure and explicit primitive effects. The ordinary-prefix runner
checks package origins and forbids source overrides in installed mode.

They do not establish actual default/private resources, Foundation ownership,
NSNumber/key/fast-enumeration or exception ABI, NSObject substitution/dispatch-once
semantics, native fonts/destruction/concurrency, native document observers or the
original four-font editor workflows. Source, ordinary artifacts, native
preservation/Undo/Redo/save-reopen and publication remain separate gates.
