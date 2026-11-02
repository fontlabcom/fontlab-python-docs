---
this_file: src_docs/md/guide/glyport-sidebar.md
---

# Understand sidebar trees and document metadata

The [manager state, ranks and placeholder-font experiments](glyport-manager-state.md)
show raw container identity, retained rank caches, debug/shared construction,
observer cleanup and source-derived font/error control flow over visible owned
primitives. Actual native fonts/defaults/resources remain separately qualified.


A sidebar tree is a view of current font data, saved visibility preferences and
filter resources. Its rows also hold mutable parent, count and scheduling state.
These experiments show which objects survive each operation, when work actually
runs, and what remains after a failure. They use the current Glyport algorithms
over invented inputs. They do not open a font or contact FontLab.

The described bodies are pinned to Glyport source checkpoint
`788959172108d684bf84816d53aeca2d392eba6f`. Matching ordinary installations and
native behavior require their own verification.

Start with [metadata managers and execution profiles](glyport-managers.md) for
record lookup and complete local loading. The examples here complement that
guide: filtering a row is different from expanding its name list, and counting
it is different again from publishing the result.

## Prepare the experiments

Run the [owned graph setup](glyport-managers.md#prepare-an-owned-graph), followed
by the `glyport-local-lifecycle` setup in
[connected local initialization](glyport-managers.md#construct-and-reload-a-local-manager-with-explicit-dependencies).
Then run the following sidebar setup and the document setup below. For every
tagged experiment, execute all four setup blocks in that order in a fresh
namespace, then execute that single example body. Examples do not depend on
earlier example mutations.

`GSGlyphsInfo` and `GSDocument` are actual exported classes. `SidebarItem` and
`InfoState` are implementation surfaces used explicitly for source experiments.
Attaching an `InfoState` below exercises selected dynamic operations without
pretending to initialize complete resources. The document experiment instead
calls the actual initializer, parsers, sidebar builder and queued summaries.

The provider supplies individual primitives: defaults, a comparison function,
predicate objects and count results, field access, record allocation/copy/name
assignment, alerts and dispatch. It never implements tree filtering, name-list
expansion, count precedence, Smallcaps processing or publication. Its localization
is deliberately identity localization; its comparator deliberately sorts in
reverse order. Empty folders and nil-array no-op handling are explicit fixture
choices. None establishes a native Foundation policy.

<!-- setup: glyport-owned-sidebar -->
```python
import copy
import gc
from contextlib import contextmanager
from types import SimpleNamespace
from fontlab_glyport.errors import UnsupportedCapability
from fontlab_glyport.glyphsapp import GSDocument, GSGlyphsInfo
from fontlab_glyport.glyphsapp.info_runtime import (
    InfoNativeException, InfoState, using_info_provider,
)
from fontlab_glyport.glyphsapp.info_sidebar import SidebarItem
from fontlab_glyport.glyphsapp import info_sidebar_dynamic

class SidebarPrimitives:
    def __init__(self):
        self.events, self.pending, self.main, self.defaults = [], [], [], {}
        self.mapping, self.category_rows, self.filter_rows = {}, [], []
        self.predicate_counts, self.filtered = {}, {}
    def localize(self, text):
        return text
    def compare(self, left, right):
        return (right > left) - (right < left)
    def defaults_bool_for_key(self, key):
        self.events.append(("defaults-read", key))
        return self.defaults.get(key, False)
    def defaults_set_bool_for_key(self, value, key):
        self.defaults[key] = value
    def set_from_array(self, values):
        self.events.append(("script-set", tuple(values)))
        if None in values:
            raise ValueError("owned set rejects nil")
        return set(values)
    def compile_predicate(self, text, *arguments):
        self.events.append(("compile", text, arguments))
        if text == "owned bad filter":
            raise InfoNativeException("owned compilation failure")
        return SimpleNamespace(predicateFormat=text, arguments=arguments)
    def schedule_count_update(self, item, delay):
        self.events.append(("schedule", delay))
        self.pending.append(item._run_count_update)
    def dispatch_main(self, callback):
        self.main.append(callback)
    def notify(self, item, phase, key):
        self.events.append((phase, key, item.count, item.shallHaveCount))
    def resource_url(self, name, extension):
        self.events.append(("resource", name, extension))
        return name
    def load_dictionary(self, url):
        assert url == "category2Icon"
        return self.mapping
    def load_array(self, url):
        return self.category_rows if url == "defaultCategories" else self.filter_rows
    def user_support_path(self):
        return "owned-support"
    def application_support_paths(self):
        return []
    def load_property_list(self, path):
        assert path == "owned-support/CustomFilter.plist"
        return self.filter_rows, None
    def array_add_objects(self, destination, values):
        assert values is None
        self.events.append(("owned-nil-array",))
    def sidebar_info_value(self, row, field):
        return None if row is None else getattr(row, field)
    def sidebar_new_info(self):
        return record(None)
    def sidebar_copy_info(self, row):
        self.events.append(("copy", row.name))
        return copy.copy(row)
    def sidebar_set_info_name(self, row, name):
        row.name = name
    def sidebar_hex_to_int(self, code):
        return int(code, 16)
    def sidebar_font_all_glyphs(self, font):
        return font.glyphs
    def sidebar_count_infos(self, font, infos):
        self.events.append(("infos-count", tuple(row.name for row in infos)))
        return sum(row.name in font.names for row in infos)
    def sidebar_count_codes(self, font, codes):
        self.events.append(("codes-count", font.label))
        return sum(code in font.codes for code in codes)
    def count_matching_predicate(self, glyphs, predicate):
        self.events.append(("predicate-count", predicate.predicateFormat))
        answer = self.predicate_counts[predicate.predicateFormat]
        if isinstance(answer, Exception):
            raise answer
        return answer
    def filter_using_predicate(self, glyphs, predicate):
        answer = self.filtered[predicate.predicateFormat]
        if isinstance(answer, Exception):
            raise answer
        return answer
    def show_modal_alert(self, message):
        self.events.append(("modal", message))
    def show_exception_alert(self, error):
        self.events.append(("alert", str(error)))
    def present_error(self, error):
        self.events.append(("error", error.code()))
    def log(self, message):
        self.events.append(("log", str(message)))

def row(provider, identifier, *, predicate=None, coverage=None):
    item = SidebarItem()
    item._provider = provider
    item.setName_(identifier)
    item.setIdentifier_(identifier)
    item.setPredicate_(predicate)
    # Raw storage deliberately avoids scheduling; examples call setters explicitly.
    item.coverage = coverage
    return item

def dynamic_manager(provider):
    manager = GSGlyphsInfo.alloc()
    manager._lifecycle = InfoState(provider, None)
    state = manager._lifecycle
    state.name2Group, state.sidebarCategories = {}, []
    state.categories, state.subCategories, state.scriptIDs = [], [], []
    return manager, state

class GlyphRows(list):
    def __init__(self, provider, rows=(), scripts=(), counts=None):
        super().__init__(rows)
        self.provider, self.scripts = provider, scripts
        self.counts = {} if counts is None else counts
    def valueForKey_(self, key):
        assert key == "script"
        return self.scripts
    def countOfObjectsWithOptions_matchingPredicate_(self, options, predicate):
        self.provider.events.append(("general-count", options, predicate.predicateFormat))
        return self.counts[predicate.predicateFormat]

class OwnedFont:
    def __init__(self, provider, *, label="font", rows=(), scripts=(), counts=None,
                 types=(0, 0), tags=((),), manager=None, names=(), codes=()):
        self.provider, self.label, self.manager = provider, label, manager
        self.glyphs = GlyphRows(provider, rows, scripts, counts)
        self.types, self.tags = iter(types), iter(tags)
        self.names, self.codes = set(names), set(codes)
    def lockReadGlyphs(self):
        self.provider.events.append(("lock",))
    def unlockReadGlyphs(self):
        self.provider.events.append(("unlock",))
    def fontType(self):
        value = next(self.types)
        self.provider.events.append(("fontType", value))
        return value
    @property
    def allTags(self):
        value = next(self.tags)
        self.provider.events.append(("tags", value))
        return value
    def glyphsInfo(self):
        return self.manager
    def _check(self):
        pass

def record(name, code=None, *, locked=False, kind=0):
    return SimpleNamespace(name=name, unicode=code, locked=locked, type=kind)

class Lookup:
    # Individual owned lookup primitives; SidebarItem performs the expansion.
    def __init__(self, names=None, codes=None):
        self.names, self.codes = names or {}, codes or {}
    def glyphInfoForName_(self, name):
        return self.names.get(name)
    def glyphInfoForUnicode_(self, code):
        return self.codes.get(code)

def drain(callbacks):
    while callbacks:
        callbacks.pop(0)()

@contextmanager
def fresh_category_cache():
    # Isolate only this process's implementation cache, then restore exact objects.
    saved = (info_sidebar_dynamic._mapping_ready,
             info_sidebar_dynamic._category_mapping,
             info_sidebar_resources._once_arrays)
    info_sidebar_dynamic._mapping_ready = False
    info_sidebar_dynamic._category_mapping = None
    info_sidebar_resources._once_arrays = {}
    try:
        yield
    finally:
        (info_sidebar_dynamic._mapping_ready,
         info_sidebar_dynamic._category_mapping,
         info_sidebar_resources._once_arrays) = saved
```

The private cache assignments are process isolation for owned experiments. They
are not a supported runtime refresh API. Never use them to invalidate a running
application's resources.

## Visibility and projected trees

### Read the current preference key

Hidden state reads the defaults provider on every access, using the current row
identifier. A missing provider is a capability error, rather than a hidden or
visible default. This makes a renamed identifier a different preference key.

<!-- example: glyport-sidebar-hidden-defaults -->
```python
p = SidebarPrimitives()
item = row(p, "OwnedGreek")
assert item.hidden is False
item.setHidden_(True)
assert p.defaults == {"GSSidebarItemHidden_OwnedGreek": True}
p.defaults[item.hiddenKey()] = False
assert item.hidden is False
item.setIdentifier_(None)
assert item.hiddenKey() == "GSSidebarItemHidden_(null)"
item.setHidden_(True)
assert item.hidden is True
try:
    _ = SidebarItem().hidden
except UnsupportedCapability as error:
    assert "defaults_bool_for_key" in str(error)
else:
    raise AssertionError("Missing defaults must refuse")
```

### Distinguish the UTF16 shortcut from general counting

Filtering first locks the font, reads the script collection and constructs the
owned set, even for an empty group. Hidden rows with no predicate disappear.
The exact `script == ` prefix takes the UTF16 range `(11, length - 12)` unless
the format contains the exact string ` OR `. It does not parse a predicate
grammar. The emoji below occupies two UTF16 units; lowercase `or` still takes
the shortcut. General counts use option `1` inside their own lock/unlock pair.

<!-- example: glyport-sidebar-predicate-paths -->
```python
p = SidebarPrimitives()
manager, state = dynamic_manager(p)
for pattern, scripts, counts, expected, general in [
    ('script == "😀"', ["😀"], {}, True, False),
    ('script == "latin" OR name == "A"', [],
     {'script == "latin" OR name == "A"': 2}, True, True),
    ('script == "latin" or name == "A"', ["latin"], {}, False, False),
]:
    item = row(p, "Owned", predicate=p.compile_predicate(pattern))
    item.setHidden_(True)
    group = row(p, "Group")
    group.setSubItems_([item])
    p.events.clear()
    answer = manager.filterGroup_forFont_(
        group, OwnedFont(p, scripts=scripts, counts=counts))
    assert answer is (group if expected else None)
    assert any(e[0] == "general-count" for e in p.events) is general
    assert sum(e == ("lock",) for e in p.events) == (2 if general else 1)
    assert sum(e == ("unlock",) for e in p.events) == (2 if general else 1)
item.setPredicate_(p.compile_predicate("script == "))
try:
    manager.filterGroup_forFont_(group, OwnedFont(p))
except ValueError as error:
    assert "UTF-16 range" in str(error)
else:
    raise AssertionError("Malformed exact shortcut must retain its range failure")
```

### Keep original child identities when projecting

A partial projection allocates a plain `SidebarItem`, transfers selected fields
through their setters and reparents the retained original children. It does not
copy them. Setting transferred list coverage schedules a count; transferring
codes or the old badge is not part of this projection. The original group still
contains the same child whose parent now points to the projection.

<!-- example: glyport-sidebar-projection-identity -->
```python
p = SidebarPrimitives()
manager, state = dynamic_manager(p)
old = row(p, "Original", coverage=["A"])
kept, removed = row(p, "Kept"), row(p, "Removed")
removed.setHidden_(True)
old.setSubItems_([kept, removed])
old.codes, old.badgeString, old.editable = ["0041"], "old badge", True
projected = manager.filterGroup_forFont_(old, OwnedFont(p))
assert type(projected) is SidebarItem and projected is not old
assert projected.subItems == [kept] and projected.subItems[0] is kept
assert old.subItems == [kept, removed]
assert kept.parent is projected and removed.parent is old
assert projected.coverage is old.coverage
assert projected.codes is None and projected.badgeString is None
assert projected.editable is False and projected.isCalculating()
assert p.events[-1] == ("schedule", 10_000_000)
drain(p.pending)  # No current font: update does no work and calculating stays set.
assert projected.isCalculating() and not p.main
```

## Order, categories and current resource reads

### Retain encounter order and sort only subcategories

Category order follows the font's first encounters. Missing categories form the
`Other` group, with an explicit NULL predicate. Only subcategories use the supplied
comparison primitive. The mapping changes icon names; no mapping entry leaves
the category name as the icon name. No native image is loaded here.

<!-- example: glyport-sidebar-category-order -->
```python
p = SidebarPrimitives()
manager, state = dynamic_manager(p)
font = OwnedFont(p, rows=[
    SimpleNamespace(category="Mark", subCategory="Below"),
    SimpleNamespace(category=None, subCategory=""),
    SimpleNamespace(category="Mark", subCategory="Above"),
    SimpleNamespace(category="Letter", subCategory=None),
])
groups = manager.categoriesFromFont_categoryToIconMapping_(font, {"Mark": "OwnedIcon"})
assert [g.identifier for g in groups] == ["Mark", "Other", "Letter"]
assert [g.iconName for g in groups] == ["OwnedIcon", "Other", "Letter"]
assert [g.identifier for g in groups[0].subItems] == ["Below", "Above"]
assert groups[0].subItems[0].parent is groups[0]
assert groups[1].predicate.predicateFormat == "category == NULL"
assert groups[1].subItems is None
assert all(g.cellType == "ImageTextCell" for g in groups)
```

### Share the first category mapping object

The first receiver supplies default category overrides. Its dictionary object,
including a nil result, becomes the process-once result. Later receivers and
providers cannot refresh it merely by calling the method again. Mutations to
that same returned dictionary remain visible. The isolated cache context keeps
these experiments from contaminating other source examples.

<!-- example: glyport-sidebar-once-mapping -->
```python
first, later = SidebarPrimitives(), SidebarPrimitives()
first.mapping = {"Mark": "base", "Retained": "keep"}
first.category_rows = [{"name": "Mark", "icon": "override"}]
later.mapping = {"Mark": "later"}
with fresh_category_cache():
    with using_info_provider(first):
        mapping = GSGlyphsInfo.categoryToIconMapping()
    assert mapping is first.mapping
    assert mapping == {"Mark": "override", "Retained": "keep"}
    mapping["OwnedNew"] = "new"
    with using_info_provider(later):
        assert GSGlyphsInfo.categoryToIconMapping() is mapping
    assert later.events == [] and mapping["OwnedNew"] == "new"
with fresh_category_cache():
    first.mapping = None
    with using_info_provider(first):
        assert GSGlyphsInfo.categoryToIconMapping() is None
    with using_info_provider(later):
        assert GSGlyphsInfo.categoryToIconMapping() is None
```

### Resolve an icon once per row

Image lookup tries the original name, compact name and their `Template` forms,
then system symbols. A successful image is cached on the row. Changing the
stored icon name alone does not clear that image. These owned image objects
are plain tokens; no image registry or native UI is consulted.

<!-- example: glyport-sidebar-icon-cache -->
```python
p = SidebarPrimitives()
image, calls = object(), []
def image_named(name):
    calls.append(name)
    return image if name == "OwnedIconTemplate" else None
p.image_named = image_named
item = row(p, "Icon")
item.setIconName_("Owned Icon")
assert item.icon is image
assert calls == ["Owned Icon", "OwnedIcon", "Owned IconTemplate", "OwnedIconTemplate"]
item.setIconName_("Changed")
assert item.icon is image and len(calls) == 4
```

### Observe repeated tree reads and tag coverage

The builder reads `fontType()` twice and, for a nonempty first tag result, reads
`allTags` again for coverage. It does not cache a final tree. These intentionally
changing primitives make the repeated reads observable: the first type creates
categories; the second type still includes languages. Tags take the second
coverage object and schedule actual count work. Prefix construction stops at the
first nil item, while later languages/tags/filters can still be appended.

<!-- example: glyport-sidebar-current-tree -->
```python
p = SidebarPrimitives()
manager, state = dynamic_manager(p)
state.allItem = row(p, "All")
state.languagesGroup = row(p, "LANGUAGES")
language = row(p, "OwnedLanguage")
state.languagesGroup.setSubItems_([language])
custom = row(p, "OwnedFilter")
state.filterGroups = [custom]
coverage = ["second tag"]
font = OwnedFont(p, types=(3, 0), tags=(["first tag"], coverage), rows=[
    SimpleNamespace(category="Letter", subCategory=None),
])
with fresh_category_cache():
    tree = manager.glyphGroupsTreeForFont_(font)
assert [g.identifier for g in tree] == ["All", "CATEGORIES", "LANGUAGES", "TAGS", "OwnedFilter"]
assert tree[2] is state.languagesGroup and tree[-1] is custom
assert tree[3].coverage is coverage and tree[3].cellType == "TagsCell"
assert [e for e in p.events if e[0] == "fontType"] == [("fontType", 3), ("fontType", 0)]
assert [e[1] for e in p.events if e[0] == "tags"] == [["first tag"], coverage]
state.allItem = None
state.filterGroups = None
again = manager.glyphGroupsTreeForFont_(OwnedFont(p))
assert again == [state.languagesGroup]
assert p.events[-1] == ("owned-nil-array",)
```

### Reload filters without inventing rollback

The reload method replaces filter storage only after its actual loader returns.
An exception leaves the old array in place. Successful processing still uses the
persistent name map: duplicate identifiers do not replace the first map identity,
although new filter rows are returned. The example invokes the real file-list
loader and group processor, with only the property-list read supplied.

<!-- example: glyport-sidebar-filter-reload -->
```python
p = SidebarPrimitives()
manager, state = dynamic_manager(p)
p.filter_rows = [{"name": "Owned first", "id": "same"}]
manager.reloadCustomFilterGroup()
old = manager.filterGroups()
mapped = state.name2Group["same"]
original_read = p.load_property_list
def broken_read(path):
    raise OSError("owned unreadable filter")
p.load_property_list = broken_read
try:
    manager.reloadCustomFilterGroup()
except OSError as error:
    assert str(error) == "owned unreadable filter"
else:
    raise AssertionError("Read failure must propagate")
assert manager.filterGroups() is old
p.load_property_list = original_read
p.filter_rows = [{"name": "Owned second", "id": "same"}]
assert manager.reloadCustomFilterGroup() is None
assert manager.filterGroups() is not old
new = manager.filterGroups()[0].subItems[0]
assert new.name == "Owned second" and new is not mapped
assert state.name2Group["same"] is mapped
assert new.parent is manager.filterGroups()[0]
```

## Row insertion, copying and delayed work

### Preserve shallow fields and child ownership

Copying retains coverage and infos by identity while recursively copying children.
Normal count values reset; the `shallHaveCount == -2` sentinel preserves counts
and badge. Bulk insertion outside the current array bounds inserts at zero.
Removing a child removes duplicate occurrences but retains its old parent field.

<!-- example: glyport-sidebar-copy-insert -->
```python
p = SidebarPrimitives()
parent = row(p, "Parent", coverage=["A"])
a, b, c = row(p, "A"), row(p, "B"), row(p, "C")
children = [a]
parent.setSubItems_(children)
parent.insertObject_inSubItemsAtIndex_(b, 1)
parent.insertSubItems_atIndex_([c, b], 100)
assert parent.subItems is children and children == [c, b, a, b]
parent.removeSubItemsObject_(b)
assert children == [c, a] and b.parent is parent
parent.infos, parent.count, parent.shallHaveCount = [record("A")], 1, 2
parent.badgeString = "1/2"
duplicate = parent.copyWithZone_(None)
assert duplicate.coverage is parent.coverage and duplicate.infos is parent.infos
assert duplicate.subItems[0] is not c and duplicate.subItems[0].parent is duplicate
assert c.parent is parent
assert (duplicate.count, duplicate.shallHaveCount, duplicate.badgeString) == (-1, -1, None)
parent.shallHaveCount = -2
preserved = parent.copyWithZone_(None)
assert (preserved.count, preserved.shallHaveCount, preserved.badgeString) == (1, -2, "1/2")
nil_array = row(p, "Nil array")
nil_array.insertObject_inSubItemsAtIndex_(b, 500)
assert nil_array.subItems is None and b.parent is nil_array
```

### Resolve the weak font when the callback runs

Setting a font expands its current manager's name list and schedules a delayed
count, then forwards to children. A second assignment while calculating changes
the weak reference without adding a second count request. The scheduled body
reads that current reference, so it counts the second font. A collected font
becomes nil; nil-font count work does not clear calculating state.

<!-- example: glyport-sidebar-weak-delayed -->
```python
p = SidebarPrimitives()
item = row(p, "Codes")
item.codes = ["0041", "0042"]
first = OwnedFont(p, label="first", codes=["0041"])
second = OwnedFont(p, label="second", codes=["0041", "0042"])
item.setFont_(first)
item.setFont_(second)
assert len(p.pending) == 1 and item.font is second
drain(p.pending)
assert ("codes-count", "second") in p.events
assert item.count == -1 and len(p.main) == 2
drain(p.main)
assert (item.count, item.shallHaveCount, item.badgeString) == (2, 2, "✓")
assert not item.isCalculating()
item.setFont_(first)
del first
gc.collect()
assert item.font is None
drain(p.pending)
assert item.isCalculating() and not p.main
```

## Name lists and count publication

### Expand inclusive ranges without deduplicating

Both range endpoints are looked up by name, then every code is looked up in the
current Unicode index. Repeated rows remain repeated. A reversed range is
consumed without output. Missing endpoint Unicode falls back to the whole name
token and the new-record primitive. A nil record inside a valid range raises,
preserving old infos and original coverage.

<!-- example: glyport-sidebar-expand-ranges -->
```python
p = SidebarPrimitives()
a, b, c = record("A", "0041"), record("B", "0042"), record("C", "0043")
lookup = Lookup({"A": a, "C": c}, {"0041": a, "0042": b, "0043": c})
item = row(p, "Range", coverage=["A:C", "A", "C:A", "missing:end"])
original = item.coverage
item.expandNameList_(lookup)
assert item.coverage is original
assert item.infos[:4] == [a, b, c, a]
assert item.infos[4].name == "missing:end"
old = item.infos
lookup.codes.pop("0042")
item.coverage = ["A:C"]
try:
    item.expandNameList_(lookup)
except InfoNativeException as error:
    assert "range contains nil" in str(error)
else:
    raise AssertionError("A nil range member must fail")
assert item.infos is old and item.coverage == ["A:C"]
```

### Copy locked aliases and retain the original enumerator

An ASCII-leading multi-unit alias with a different stored name is renamed.
Locked records are copied first; unlocked records are renamed in place. These
are explicit owned record fields, not inferred proprietary metadata. A malformed
list member clears stored coverage and warns once per item name, but expansion
continues over the original array. Later valid members are still included.

<!-- example: glyport-sidebar-alias-collision -->
```python
p = SidebarPrimitives()
locked, mutable = record("canonical", locked=True), record("mutable")
lookup = Lookup({"Alias": locked, "MutableAlias": mutable})
item = row(p, "Owned malformed list", coverage=["Alias", 123, "MutableAlias", "Alias"])
item.expandNameList_(lookup)
assert item.coverage is None
assert [r.name for r in item.infos] == ["Alias", "MutableAlias", "Alias"]
assert item.infos[0] is not locked and locked.name == "canonical"
assert item.infos[1] is mutable and mutable.name == "MutableAlias"
assert item.infos[2] is not item.infos[0]
assert sum(e[0] == "modal" for e in p.events) == 1
item.coverage = [False, "Alias"]
item.expandNameList_(lookup)
assert sum(e[0] == "modal" for e in p.events) == 1
assert len(item.infos) == 1 and item.infos[0].name == "Alias"
```

### Separate calculation from main-thread publication

Nonempty infos take precedence over predicate and codes. Expected count includes
only infos with type zero. Calculation enqueues a working checkmark, then a
publication callback. Until those callbacks run, stored count fields are unchanged.
Only changed tuples emit `hasShallHaveCount` notifications. Repeating a successful
publication still clears calculating and updates the badge.

<!-- example: glyport-sidebar-count-publication -->
```python
p = SidebarPrimitives()
item = row(p, "Count", predicate=p.compile_predicate("must not count"))
item.infos = [record("A"), record("B", kind=1), record("C")]
item.codes = ["ignored"]
font = OwnedFont(p, names=["A", "C"])
item.setIsCalculating_(True)
item.updateCount_(font)
assert (item.count, item.shallHaveCount, item.badgeString) == (-1, -1, None)
assert len(p.main) == 2 and not any(e[0] == "predicate-count" for e in p.events)
p.main.pop(0)()
assert item.badgeString == "✓" and item.count == -1
p.main.pop(0)()
assert (item.count, item.shallHaveCount, item.badgeString) == (2, 2, "✓")
notifications = [e for e in p.events if e[0] in ("will", "did")]
assert notifications == [("will", "hasShallHaveCount", -1, -1),
                         ("did", "hasShallHaveCount", 2, 2)]
item.setIsCalculating_(True)
item._publish_count(2, 2)
assert not item.isCalculating()
assert [e for e in p.events if e[0] in ("will", "did")] == notifications
```

### Follow Smallcaps success and partial failure

The exact case-two predicate supplies the expected source count; `.sc` lookup
retains available records. The case-three predicate supplies the actual count.
The resulting list is assigned to `infos`, while `missingInfos` remains intact.
A marked exception in the second filter keeps the newly computed expected count
but leaves old infos and the base count in place. Ordinary Python errors are not
swallowed by this marked native-exception analogue.

<!-- example: glyport-sidebar-smallcaps -->
```python
p = SidebarPrimitives()
item = row(p, "Smallcaps")
item.codes = ["0041"]
sentinel = item.missingInfos = [record("untouched")]
source_pattern = "(case == 2) AND NOT (name contains '.0') AND (export == True)"
p.filtered[source_pattern] = [record("a"), record("b")]
p.filtered["case == 3"] = [record("a.sc")]
sc = record("a.sc")
font = OwnedFont(p, manager=Lookup({"a.sc": sc}), names=["a.sc"], codes=["0041"])
item.updateCount_(font)
drain(p.main)
assert (item.count, item.shallHaveCount, item.badgeString) == (1, 2, "1/2")
assert item.infos == [sc] and item.infos[0] is sc
assert item.missingInfos is sentinel
old_infos = item.infos
p.filtered["case == 3"] = InfoNativeException("owned second filter failure")
item.updateCount_(font)
drain(p.main)
assert (item.count, item.shallHaveCount) == (1, 2)
assert item.infos is old_infos and item.missingInfos is sentinel
assert any(e[0] == "log" and "second filter failure" in e[1] for e in p.events)
assert old_infos == [sc]
```

### Initialize the independent sidebar queue explicitly

Calling this selector is an explicit source experiment. Python does not invoke
Objective-C automatic class initialization. For five active processors, the
retained float32 half-count and nearest-away rounding yield three workers, with
QoS 17. A second call retains the first queue object. This queue is independent
of a manager's queue and does not itself replace the delayed scheduler primitive.

<!-- example: glyport-sidebar-queue-initialize -->
```python
from fontlab_glyport.glyphsapp import info_sidebar_support

class CountQueue:
    def setMaxConcurrentOperationCount_(self, count):
        self.limit = count
    def setQualityOfService_(self, quality):
        self.quality = quality

p = SidebarPrimitives()
queue = CountQueue()
allocations = []
def new_queue():
    allocations.append(queue)
    return queue
p.new_queue = new_queue
p.active_processor_count = lambda: 5
saved = info_sidebar_support._queue_initialized, info_sidebar_support._sidebar_queue
try:
    info_sidebar_support._queue_initialized = False
    info_sidebar_support._sidebar_queue = None
    with using_info_provider(p):
        SidebarItem.initialize()
        SidebarItem.initialize()
    assert allocations == [queue]
    assert (queue.limit, queue.quality) == (3, 17)
    assert info_sidebar_support._sidebar_queue is queue
finally:
    (info_sidebar_support._queue_initialized,
     info_sidebar_support._sidebar_queue) = saved
```

### Keep compilation and count errors distinct

The format setter catches only marked compilation failures, queues an alert and
retains the previous predicate. It does not assign `predicateFormat`, create the
constructor's fallback predicate or force a stop badge. Marked count failures
instead report error 992 and publish `(-2, -2)`. They deduplicate by the current
predicate format; an ordinary error still propagates before publication.

<!-- example: glyport-sidebar-predicate-failures -->
```python
p = SidebarPrimitives()
item = row(p, "Owned count failure")
item.setPredicateFormat_("owned prior")
prior = item.predicate
item.setPredicateFormat_("owned bad filter")
assert item.predicate is prior and item.predicateFormat is None
assert item.count == -1 and len(p.main) == 1
drain(p.main)
assert p.events[-1] == ("alert", "owned compilation failure")
p.predicate_counts["owned prior"] = InfoNativeException("owned count failure")
item.updateCount_(OwnedFont(p))
drain(p.main)
assert (item.count, item.shallHaveCount, item.badgeString) == (-2, -2, None)
assert ("error", 992) in p.events
p.predicate_counts["owned prior"] = ValueError("ordinary error")
try:
    item.updateCount_(OwnedFont(p))
except ValueError as error:
    assert str(error) == "ordinary error"
else:
    raise AssertionError("Unmarked errors must propagate")
assert len(p.main) == 1  # The working badge was already queued before failure.
drain(p.main)
```

## Documents: real local loading and explicit missing adapters

The document calls its file primitives rather than treating a path string as an
NSDocument. The following setup supplies URL selectors and a superclass file
setter only. Optional observer methods on the owned subclass record their order;
they do not watch the filesystem. All font data lives in a temporary owned tree.

<!-- setup: glyport-owned-document -->
```python
class OwnedURL:
    def __init__(self, name, parent=None):
        self.name, self.parent = name, parent
    def path(self):
        return self.name
    def URLByDeletingLastPathComponent(self):
        return self.parent
    def isEqual_(self, other):
        return isinstance(other, OwnedURL) and self.name == other.name

class FilePrimitives:
    def __init__(self, url, kind="com.schriftgestaltung.glyphs"):
        self.url, self.kind, self.events = url, kind, []
    def file_url(self, document):
        return self.url
    def set_file_url(self, document, url):
        self.events.append("super-set-url")
        self.url = url
    def file_type(self, document):
        return self.kind

class OwnedDocument(GSDocument):
    def stopObservingFile(self):
        self._file_primitives.events.append("stop")
    def startObservingFile(self):
        self._file_primitives.events.append("start")
    def updateFileObservers(self):
        self._file_primitives.events.append("update")
```

### Load the parent folder through the actual constructor

The document computes the parent URL before entering its manager lock. It keeps
the old local manager until the new initializer returns. This example runs the
actual sidebar initialization, local XML parsing, shared-manager fallback and
queue drain through the earlier complete lifecycle fixture. The first load's
temporary rows are real parsed invented data, rather than a fabricated manager
return. An equal URL calls only the superclass setter; a changed URL calls stop,
superclass setter, conditional start, update and then actual loading. The new
invalid XML experiment keeps the source's non-atomic loaded state and reported
error; it does not invent an exception or rollback.

<!-- example: glyport-sidebar-document-loading -->
```python
with owned_lifecycle() as (provider, folder_url, data):
    font = OwnedFont(SidebarPrimitives(), types=(0, 0, 0))
    file_url = OwnedURL(str(data.parent / "Owned.glyphs"), folder_url)
    document = OwnedDocument(font)
    files = document._file_primitives = FilePrimitives(file_url)
    assert document.loadCustomGlyphsData() is True
    local = document.glyphsInfo()
    assert local._lifecycle.localURL is folder_url
    assert local.glyphInfoForName_("owned.local").unicode == "0042"
    assert local.allItem().identifier == "All"
    assert local.categoriesGroup().subItems[0].identifier == "Owned"
    assert not local._lifecycle.queue.pending
    assert document.valueForKey_("glyphsInfo") is local
    document.setFileURL_(OwnedURL(file_url.name, folder_url))
    assert files.events == ["super-set-url"] and document.glyphsInfo() is local
    changed = OwnedURL(str(data.parent / "Other.glyphs"), folder_url)
    document.setFileURL_(changed)
    assert files.events == ["super-set-url", "stop", "super-set-url", "start", "update"]
    replacement = document.glyphsInfo()
    assert replacement is not local
    assert replacement.glyphInfoForName_("owned.local").unicode == "0042"
    data.write_text("<glyph broken", encoding="utf-8")
    assert document.loadCustomGlyphsData() is True
    assert document.glyphsInfo() is not replacement
    assert any(event[0] == "error" for event in provider.events)
    files.url = None
    assert document.loadCustomGlyphsData() is True
    assert document._local_glyph_info is None
```

### Refuse unqualified file and font-type dependencies

The four monitored types are Glyphs, UFO, Glyphs package and icon set. Other types
do not start an observer. Missing observer selectors take the source's optional
branches; that does not install a monitor. Missing file primitives refuse.
Likewise the current FontLab `GSFont` has no qualified `fontType()` mapping for
these algorithms: ordinary model access must not silently assume type zero.

<!-- example: glyport-sidebar-document-refusals -->
```python
manager, canonical = owned_manager()
exports, font = owned_exports(manager)
assert type(font.parent) is GSDocument
document = GSDocument(font)
assert document.shouldMonitorFile_("com.schriftgestaltung.glyphs")
assert document.shouldMonitorFile_("org.unifiedfontobject.ufo")
assert document.shouldMonitorFile_("com.glyphsapp.glyphspackage")
assert document.shouldMonitorFile_("com.glyphsapp.iconset")
assert not document.shouldMonitorFile_("owned.unmonitored")
try:
    document.loadCustomGlyphsData()
except UnsupportedCapability as error:
    assert "fileURL" in str(error)
else:
    raise AssertionError("An unqualified document URL must refuse")
document._file_primitives = FilePrimitives(None, "owned.unmonitored")
assert document.loadCustomGlyphsData() is True
try:
    font.fontType()
except UnsupportedCapability as error:
    assert "fontType" in str(error)
else:
    raise AssertionError("FontLab fontType needs a qualified adapter")
```

## Carry the result to a real integration

These are source-contract experiments, not native FontLab acceptance. A usable
FontLab adapter must qualify `GSFont.fontType`, lock/KVC/current glyph collection
access, file URL/type/superclass setter behavior and file observers. Sidebar
defaults, real predicate compilation/evaluation, lawful category/filter/icon
resources, image lookup, localization, record fields and count operations also
need concrete adapters. Scheduling must execute the real callbacks with the
appropriate queue/main-thread semantics; recording callback counts alone does
not complete that work.

Python weak references, locks and lists do not prove Cocoa weak references,
NSArray mutation/zone behavior, KVO delivery or process-once exception behavior.
Explicit `SidebarItem.initialize()` is separate from Objective-C automatic class
initialization. The owned nil-array policy above must never become an assertion
that every native array accepts nil. Projection and count failures retain the
source's partial state; a cleanup or rollback policy needs its own evidence.

The reusable verification runner executes every tagged experiment from a fresh
namespace with the exact published setup. It also runs the prior 99 active
examples independently and checks loaded provider origins. Installed mode allows
no source override and requires the active ordinary installation prefix. Matching
wheel/sdist payloads, complete consumers, actual FontLab behavior, original font
workflows, generated reference/rendered pages and publication remain separate
acceptance steps. The retained native/UI examples remain held and unchanged.
