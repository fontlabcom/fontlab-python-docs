---
this_file: src_docs/md/guide/original-node-actions.md
---

# Choose the original node-duplication scope explicitly

Scriptmix now exposes three distinct Node Duplicator actions. They use App's
guarded `node_duplicator_native.duplicate_selected_nodes` entry point, introduced
in the matching `0.2.26.dev333` artifact. Older rescued adapters lack that name.
Keep the separate **Node Duplicator** panel for its per-glyph reference selection,
preview and declared-master controls.

| Menu action in Contours | Source policy |
| --- | --- |
| Duplicate Nodes All Foreground Layers | Broadcast the first selected layer's on-curve indices to every stored foreground layer of each selected parent occurrence. |
| Duplicate Nodes Current Layer | Copy selected on-curves in the first selected layer only. |
| Duplicate Nodes with Two Handles | First selected layer only; insert two coincident controls and a copied curve endpoint per selected on-curve. |

The two-handle source's filename says “all masters”, but its body has no
all-master loop. The actions preserve that distinction. All-layer mode retains
auxiliary-layer identities and repeated parents; two layers with the same name
remain separate targets. Missing target path/node indices are reported.

These are immediate actions. Select nodes, activate the appropriate Font or
Glyph window, and run the chosen menu entry. A broadcast that includes owners
outside the active Glyph canvas is refused before staging; activate the Font
window for that edit. Queued glyph ids are disclosed without clearing them.
Automatic dependants, shared owners, hinted topology and unsupported generated
or control mappings have explicit refusals.

The following experiments execute the actual immutable App planning engine.
They use invented node/layer identities and metadata, with no FontLab, Qt,
framework, font, preference or document access. They do not establish native
selection projection, copy fidelity, history or saved-font acceptance.

## Prepare an owned source graph

Execute this setup afresh before each tagged experiment. Layers10/11 share one
parent;20/21 share another. The occurrence list selects the first parent twice.
Only node1 in the first selected layer supplies the reference selection.
The native adapter keeps display names separately from these stable identities.

<!-- setup: original-node-owned-source -->
```python
from dataclasses import replace
from fontlabapp.node_duplicator import Node, Path, Layer, Source, plan

def owned_source():
    def node(key):
        return Node(key, key + 0.125, key + 0.375, "line", 8,
                    f"node-{key}", (("corner_smooth", 0.375),))
    layers = tuple(
        Layer(key, glyph, (Path(key * 10, (node(a), node(a + 1)), False),))
        for key, glyph, a in [(10, 1, 1), (11, 1, 3), (20, 2, 5), (21, 2, 7)]
    )
    return Source(layers, (10, 11, 20), ((0, 1),), True)
```

## Replay each selected parent occurrence

Both foreground layers of the first parent receive two insertions. Both layers
of the second receive one, even though they have no independent selected node.
The source graph remains unchanged. History enrollment can deduplicate owners;
the operation program must retain repeated occurrences.

<!-- example: original-node-all-occurrences -->
```python
source = owned_source()
result = plan(source, "all")
assert result.inserted == 6
assert [len(layer.paths[0].nodes) for layer in result.layers] == [4, 4, 3, 3]
assert [len(layer.paths[0].nodes) for layer in source.layers] == [2, 2, 2, 2]
assert [operation.layer for operation in result.operations] == [10, 11, 10, 11, 20, 21]
assert result.skipped == ()
```

## Keep current-layer and handle semantics distinct

Current mode inserts one line copy. Handles mode inserts two fresh controls
and a curve endpoint copied from the target. The copied endpoint keeps its name,
coordinates and properties; the new controls do not pretend to be copies.
Only the first selected layer changes in either mode.

<!-- example: original-node-current-and-handles -->
```python
source = owned_source()
current, handles = plan(source, "current"), plan(source, "handles")
assert current.inserted == 1 and handles.inserted == 3
assert [len(layer.paths[0].nodes) for layer in current.layers] == [3, 2, 2, 2]
nodes = handles.layers[0].paths[0].nodes
assert [node.kind for node in nodes] == ["line", "off", "off", "curve", "line"]
original, copied = source.layers[0].paths[0].nodes[0], nodes[3]
assert (copied.x, copied.y, copied.name, copied.properties) == (
    original.x, original.y, original.name, original.properties
)
assert nodes[1].name == nodes[2].name == ""
assert nodes[1].properties == nodes[2].properties == ()
assert handles.layers[1:] == source.layers[1:]
```

## Report unavailable target indices

The original all-layer policy uses fixed reference indices. It does not require
every target to have identical topology. Here one target has no path and another
has too few nodes. Both skips retain their target identities and exact indices;
the native result window supplies captured glyph/layer names alongside them.

<!-- example: original-node-missing-targets -->
```python
source = owned_source()
layers = list(source.layers)
layers[2] = replace(layers[2], paths=())
short = replace(layers[3].paths[0], nodes=layers[3].paths[0].nodes[:1])
layers[3] = replace(layers[3], paths=(short,))
source = replace(source, layers=tuple(layers), selection=((0, 2),))
result = plan(source, "all")
assert result.inserted == 4
assert result.skipped == ((2, 20, 0, 1), (2, 21, 0, 1))
```

## Preserve the original empty-selection message rules

A visual selection can contain objects other than editable on-curves. All mode
asks for nodes when none are selected. Current mode uses the original truth of
the entire selection; handle mode has no corresponding message branch.
All three produce no insertions in this owned example.

<!-- example: original-node-empty-selection -->
```python
source = replace(owned_source(), selection=(), any_selection=True)
all_layers = plan(source, "all")
current = plan(source, "current")
handles = plan(source, "handles")
assert all_layers.inserted == current.inserted == handles.inserted == 0
assert all_layers.no_selection_message is True
assert current.no_selection_message is False
assert handles.no_selection_message is False
```

## Handle a partial failure without a blind retry

The native boundary captures and rechecks context before history, stages detached
copies and uses current history-scope guards. It checks copied metadata and exact
old-node state, and reports failed writes. Cleanup removes only exact owned new
identities while its deadline permits; it stops further mutations after expiry.

`WriteError.pending_nodes` retains owned contour/node handles for inspection.
`history_finalized` records whether the notification returned successfully; it
does not prove actual Undo/Redo or complete restoration. Inspect the affected
font and history before retrying. Do not clear native update queues, normalize
unrelated dates or discard a failed receipt to obtain a green result.

The result window uses the shared parent/priority/lifecycle helper. Owned Qt
tests cover parenting, the topmost flag, Close and reopen. Actual macOS FontLab
stacking and lifetime, four-font full preservation, Apply/Undo/Redo/save/reopen,
compiled binding behavior and release/promotion remain separate requirements.

These behavior-only rewrites credit Fernando Díaz and Reset Type Studio,
[Glyphs-Scripts](https://github.com/Reset-Type-Studio/Glyphs-Scripts), whose
retained README declares Apache-2.0. Original source identities stay separate
in Scriptmix's provenance/backlog; no original body is redistributed here.
