---
this_file: src_docs/md/guide/glyport-layer-identities.md
---

# Preserve distinct foreground layers with repeated names

`glyph.layers` keeps declared master slots first, followed by other valid stored
foreground identities in native order. A repeated name does not merge records.
String lookup uses exact IDs; it does not add an ambiguous display-name alias.
Missing declared masters retain pending slots without creating native layers.

FontLab's `isMasterLayer` is name-derived and also recognizes interpolation and
bracket names. It is broader than a declared master slot. Current upstream source
shows that case-sensitive `findLayer(name)` selects the last matching stored
identity. Glyport uses that finder consistently, then assigns separate tokens to
the remaining foreground records. Its public `isMasterLayer` describes the
declared slot, not that broader native name classification.

These experiments run the actual backend, Model and layer proxies against owned
Python objects. Only the native boundary data and finder are invented; no
projection, lookup, cache or history algorithm is replaced. They make no FontLab,
Qt, framework, font, preference, selection or document calls. Run the visible setup
afresh before each tagged body.

## Prepare owned boundary objects

<!-- setup: glyport-owned-layer-identities -->
```python
from types import SimpleNamespace as NS
from fontlab_glyport.model import Model
from fontlab_glyport.model.fontlab_backend import FontLabBackend
from fontlab_glyport.errors import StaleNativeObject

class OwnedFont(dict):
    @property
    def glyphs(self):
        return list(self.values())

def owned_layer(identity, name, width):
    return NS(id=identity, name=name, isValid=True, isMasterLayer=True,
              isMaskLayer=False, isService=False, autoLayer=False,
              advanceWidth=width, shapes=[], anchors=[], guidelines=[])

def owned_scene():
    state = NS(epoch=0)
    regular = owned_layer(30, "Regular", 500)
    bold = owned_layer(40, "Bold", 802.5)
    other_regular = owned_layer(50, "Regular", 701.25)
    other_bold = owned_layer(60, "Bold", 903.75)
    service = owned_layer(70, "img", 1)
    service.isService = True
    glyph = NS(id=20, name="A", isValid=True,
               layers=[service, other_regular, bold, other_bold, regular],
               currentHistoryState=lambda: state.epoch)
    glyph.findLayer = lambda name: next(
        (layer for layer in reversed(glyph.layers) if layer.name == name), None)
    font_data = OwnedFont(A=NS(id=200, name="A", unicodes=(65,)))
    font_data.info = NS(familyName="Owned layer experiment")
    package = NS(id=10, fgId=100, isValid=True, masters=["Regular", "Bold"],
                 axes=[], upm=1000, fgPackage=font_data, glyphsCount=1,
                 currentHistoryState=lambda: state.epoch)
    package.findFgId = lambda identity: glyph if identity == 200 else None
    package.findName = lambda name: glyph if name == "A" else None
    backend = FontLabBackend(packages=[package])
    font = Model(backend).font
    return NS(state=state, backend=backend, font=font, proxy=font.glyphs[0],
              glyph=glyph, regular=regular, bold=bold,
              other_regular=other_regular, other_bold=other_bold)

def native_ids(scene, layers):
    return [scene.backend._object(layer.id).id for layer in layers]
```

`fgPackage` above is an ordinary field on an invented object. It does not read
the unsafe native getter on an unregistered FontLab package. All glyph/layer IDs
and widths are invented. These source experiments do not qualify imported roles.

## Retain every repeated-name identity

The finder selects stored30 for Regular and60 for Bold. Stored50 and40 remain
separate auxiliaries, even though every foreground's native master flag is true.

<!-- example: glyport-layer-repeated-names -->
```python
scene = owned_scene()
layers = list(scene.proxy.layers)
assert native_ids(scene, layers) == [30, 60, 50, 40]
assert [layer.name for layer in layers] == ["Regular", "Bold", "Regular", "Bold"]
assert [layer.width for layer in layers] == [500, 903.75, 701.25, 802.5]
assert [layer.isMasterLayer for layer in layers] == [True, True, False, False]
assert len({layer.layerId for layer in layers}) == 4
```

## Use IDs, not display names, for lookup

<!-- example: glyport-layer-id-lookup -->
```python
scene = owned_scene()
layers = list(scene.proxy.layers)
for layer in layers:
    assert scene.proxy.layers[layer.layerId] is layer
assert scene.proxy.layers[scene.font.masters[0].id] is layers[0]
assert scene.proxy.layers["Regular"] is None
assert scene.proxy.layers[-1] is layers[-1]
```

To search by name, collect every match instead of building a name-keyed dict.
Master ordinals and IDs retain lazy direct lookup; auxiliary IDs and slices use
the complete catalogue. Tokens describe live session identities, not new
persistent native UUIDs.

## Repeated reads do not edit storage

<!-- example: glyport-layer-readonly-repeat -->
```python
scene = owned_scene()
before = tuple(scene.glyph.layers)
layers = list(scene.proxy.layers)
assert list(scene.proxy.layers) == layers
assert tuple(scene.glyph.layers) == before
assert not scene.backend._changed and not scene.backend._prepared
assert [layer.advanceWidth for layer in before] == [1, 701.25, 802.5, 903.75, 500]
```

## Preserve nondeclared interpolation records

<!-- example: glyport-layer-interpolating-foreground -->
```python
scene = owned_scene()
scene.other_regular.name = "Intermediate [500]"
layers = list(scene.proxy.layers)
assert native_ids(scene, layers) == [30, 60, 50, 40]
assert layers[2].name == "Intermediate [500]"
assert scene.other_regular.isMasterLayer and not layers[2].isMasterLayer
assert layers[2].associatedMasterId == scene.font.masters[0].id
```

Without explicit retained association metadata, an imported auxiliary uses the
existing first-master fallback. This does not infer full native interpolation
semantics from its name, nor authorize every generated/interpolating layer edit.

## Keep mask and service filtering

<!-- example: glyport-layer-protected-records -->
```python
for role in ("isMaskLayer", "isService"):
    scene = owned_scene()
    setattr(scene.other_regular, role, True)
    assert native_ids(scene, list(scene.proxy.layers)) == [30, 60, 40]
    assert not scene.backend._changed and not scene.backend._prepared
```

## Distinguish pending master slots from stored layers

<!-- example: glyport-layer-pending-master -->
```python
scene = owned_scene()
scene.glyph.layers.remove(scene.bold)
scene.glyph.layers.remove(scene.other_bold)
before = tuple(scene.glyph.layers)
layers = list(scene.proxy.layers)
assert len(layers) == 3 and layers[1].width == 0
assert layers[1].layerId == scene.font.masters[1].id
assert layers[2].width == 701.25
assert tuple(scene.glyph.layers) == before
```

The public collection includes logical pending slots. It is not a literal
stored-only iterator for the complete original Transform workflow. That workflow
still needs occurrence order, separate transform stages, full shape/component/
image/anchor/PS/TT payload behavior and native preservation/history proof.

## Rebind a retained identity after a history change

<!-- example: glyport-layer-history-wrapper -->
```python
scene = owned_scene()
auxiliary = list(scene.proxy.layers)[2]
old = scene.other_regular
replacement = NS(**vars(old))
replacement.advanceWidth = 888.25
scene.glyph.layers[scene.glyph.layers.index(old)] = replacement
old.isValid = False
scene.state.epoch += 1
assert auxiliary.width == 888.25
assert scene.backend._object(auxiliary.id) is replacement
assert scene.proxy.layers[auxiliary.layerId] is auxiliary
assert scene.proxy.layers[0].width == 500
```

The backend records the history marker when the handle is exposed. The epoch
change above is an invented boundary event; it does not simulate or prove actual
FontLab Undo/Redo. Native changes without observable history remain a limit.

## Retire an auxiliary that becomes the master winner

<!-- example: glyport-layer-slot-transition -->
```python
scene = owned_scene()
auxiliary = list(scene.proxy.layers)[2]
token = auxiliary.id
scene.glyph.layers.remove(scene.other_regular)
scene.glyph.layers.append(scene.other_regular)
scene.state.epoch += 1
try:
    auxiliary.width
except StaleNativeObject:
    pass
else:
    raise AssertionError("An old auxiliary must not silently alias a master slot")
assert not scene.backend.is_valid(token)
assert native_ids(scene, list(scene.proxy.layers)) == [50, 60, 40, 30]
```

Owned integration checks separately exercise exact-target duplicate-layer width
writes and automatic-layer refusal. Actual imported order/roles, all four owner
fonts, complete font/cache/date/lifetime preservation, Apply/Undo/Redo/save/reopen,
real TypeRig window priority and native binding behavior remain independent
acceptance requirements. Generated references, source locks, strict rendering,
browser/accessibility/archive/licence/publication remain under their existing gates.
