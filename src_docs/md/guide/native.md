---
this_file: src_docs/md/guide/native.md
---
# Native scripting

Inside FontLab, `echopy.fontlab` delegates to the original `fontlab` objects;
`echopy.fontgate` and `echopy.fontpr` follow the same contract.

```python
from echopy import fontlab as fl

font = fl.CurrentFont()
glyph = fl.CurrentGlyph()
node = fl.flNode(120, 340)
```

Use [flNode][fontlab.flNode] and the complete class member indexes to inspect
captured signatures and enriched documentation. `Any` and variadic arguments
mark incomplete native signature information. They are not permission to pass
arbitrary objects; confirm an uncertain operation against the running host.

The optional [fontlabpr](../reference/fontlabpr.md) module was absent from the
captured host. Its absence is recorded rather than represented by invented APIs.

## Short imports

Fly provides seven lazy module aliases:

| Alias | Target |
| --- | --- |
| `fly.fl` | `echopy.fontlab` |
| `fly.fg` | `echopy.fontgate` |
| `fly.tr` | `typerig` |
| `fly.pr` | `echopy.fontpr` |
| `fly.qt` | native `PythonQt` |
| `fly.ap` | `fontlabapp` |
| `fly.qs` | `pythonqtside` |

They share the canonical module objects. Documentation names use the live API's
natural namespaces, while source and enrichment hashes retain provenance.

Outside FontLab, native construction and operations fail with `NativeUnavailable`.
Documentation builds read source and stubs without invoking these operations.


## Handle writer results and failures

A successful Python call does not prove that FontLab preserved every unrelated
part of a font. Keep the returned counters and warnings, and qualify edits with
Apply, Undo, Redo and saved-file reopen on owned copies before relying on a writer.
Do not convert an exception into a success message or automatically repeat a
failed edit: a partial write can already have changed the font.

The examples below use the development App contract verified in ordinary package
`0.2.26.dev158+g55fc09868`. This is a source/artifact checkpoint, not a published
release or native acceptance claim. Older installed App versions may still refuse
queued updates and may not accept the `disclosure` keyword.

### Queued updates are a warning

FontLab can retain glyph IDs in its process-wide update queue after opening an
editor or refreshing views. A later write may change those glyphs’ modification
dates. Ordinary App writers disclose this as `pending_updates` and `pending_note`
instead of refusing solely because the queue is nonempty. They do not clear the
queue or restore unrelated dates to conceal the change.

| Field | Meaning |
| --- | --- |
| `pending_updates` | Tuple of native glyph IDs captured before the write; these are not names or proof that those glyphs changed. |
| `pending_note` | Human-readable date caveat, or an empty string. |
| `undo_steps` | Raise Ascender’s completed changed occurrences, not a guarantee that a later Undo succeeded. |
| `nodes` | Raise Ascender’s counted node moves across its sequential occurrences. |
| `guides`, `layers` | Perpendicular Guides’ reported additions and affected-layer count. |

Use the stored note when formatting a result. Reading the native queue again can
observe different state and lose the warning that applied to this action.

<!-- example: writer-status -->
```python
from fontlabapp.edit_guards import append_note


def raise_status(result):
    text = (
        f"Moved {result['nodes']} nodes across {result['occurrences']} occurrences; "
        f"{result['undo_steps']} Undo steps."
    )
    return append_note(text, result)
```

This formatter runs outside FontLab with an ordinary result dictionary. The helper
appends a nonempty note once. A zero-move result is still a valid outcome: it does
not mean every selected node required an edit.

### Preserve warnings when Raise Ascender fails

`Backend.execute()` accepts an optional mutable `disclosure` dictionary. It resets
the dictionary at entry and fills it before history, so a caller can display the
queue warning even when no result is returned. A failure before queue sampling, or a no-op, leaves
an empty disclosure; this does not prove that the native queue is empty. Without a dictionary, the backend prints the warning itself.

This wrapper uses the formatter above. Defining it is safe outside FontLab;
calling it requires FontLab and can change the current font.

<!-- example: raise-caller -->
```python
from fontlabapp.edit_guards import append_note
from fontlabapp.raise_ascender_native import Backend


def raise_selected(amount="10", *, all_layers=False):
    disclosure = {"pending_updates": (), "pending_note": ""}
    try:
        result = Backend().execute(
            amount, all_layers, disclosure=disclosure
        )
    except Exception as error:
        print(append_note(f"Raise Ascender failed: {error}", disclosure))
        raise
    print(raise_status(result))
    return result
```

`all_layers=False` uses the selected occurrences. `True` uses every foreground
layer of the first selected glyph, including associated auxiliary layers; it is
not an all-font operation. The writer retains its bound-font, source-change,
automatic-dependent and history-scope checks. A queued-update warning does not
waive any of those checks.

On failure, the wrapper preserves the original exception and its Undo guidance.
In a dialog, put the same formatted text in an owned status label instead of
printing it. Keep the disclosure dictionary for that action only; do not reuse a
previous action’s warning after a no-op or an early failure.

### Perpendicular Guides uses the same warning

`fontlabapp.perpendicular_guides.run()` plans guides for the first selected layer.
When the sampled queue is nonempty, it prints the warning before a possible append.
On success it returns `guides`,
`layers`, `messages`, `pending_updates` and `pending_note`. The warning
is already printed; callers need not print it a second time. A no-op reports zero
counts and empty disclosure without querying the queue. Source changes,
automatic layers or affected automatic dependants still cause refusal.

If an append partially fails, no success dictionary is returned. The warning has
already been printed and the append-failure exception directs the user to inspect
Edit > Undo. Notification/finalization errors can also propagate; do not infer
rollback from an exception. No queue clearing, automatic retry or global Undo
belongs in a caller’s error handler.

### Preview complete background removal

The background tools remove entire background layer objects, including their
stored payload. They do not merely erase contours. Use **Clear All Layer Backgrounds** or **Clear Master Backgrounds** for a panel with a preview and
an explicit Apply action. The programmatic equivalent below also separates
inspection from the write.

`masters=False` includes mapped backgrounds of all foreground layers in the
current font, including auxiliary layers. `masters=True` restricts the plan to
master foreground layers. Neither scope means selected glyphs only. A background
shared by a master and an excluded auxiliary layer is refused in master-only
mode; silently deleting it would change the excluded layer too.

Defining these functions makes no edit. Call `preview_backgrounds()` in FontLab,
inspect the printed glyph/background names, then explicitly pass its returned
value to `clear_previewed_backgrounds()`. Pass `masters=True` to preview the
master-only scope. A preview is bound to its original font and scope: the writer
rechecks it before history and refuses stale facts rather than silently rescanning
and applying a different plan.

<!-- example: background-caller -->
```python
from fontlabapp.background_clear import plan as background_plan
from fontlabapp.background_clear_native import Backend as BackgroundBackend
from fontlabapp.edit_guards import append_note


def preview_backgrounds(*, masters=False):
    backend = BackgroundBackend()
    source = backend.capture()
    if source is None:
        raise ValueError("Open a font before previewing backgrounds.")
    for removal in background_plan(source, masters):
        print(f"{removal.glyph}: {removal.mask_name}")
    return backend, source, masters


def clear_previewed_backgrounds(preview):
    backend, source, masters = preview
    disclosure = {"pending_updates": (), "pending_note": ""}
    try:
        result = backend.apply(source, masters, disclosure=disclosure)
    except BaseException as error:
        # Report the action's warning, then propagate interruptions unchanged.
        print(append_note(f"Background clearing failed: {error}", disclosure))
        raise
    print(append_note(
        f"Removed {result['backgrounds']} backgrounds from "
        f"{result['layers']} foreground layers in {result['glyphs']} glyphs.",
        result,
    ))
    return result
```

`backgrounds` counts confirmed object removals; `layers` counts the affected
foreground layers, which can differ when backgrounds are shared. `glyphs` counts
owner glyphs. A no-op returns zero counts and empty disclosure without sampling
the native queue. A nonempty warning is reported once by this wrapper; the supplied
dictionary prevents the backend from printing it separately.

Active or locked backgrounds, invalid ownership/mapping, affected automatic
layers or automatic dependants, and unsupported history scope can still cause
refusal. Queue disclosure does not waive these guards. A refused domain remains
an incomplete compatibility boundary, not proof of equivalent original behavior.

A failure after an attempted removal may leave changes in the font. Ordinary
partial-write errors report attempted and confirmed removal counts and direct
the user to Undo. Interruptions stop further removals, attempt remaining date
updates and notification, then propagate the original interruption with recovery
notes. The wrapper preserves those notes by re-raising the same exception.
Neither cleanup nor an exception proves rollback, successful Undo, or that native
cleanup finished within a deadline. Do not automatically retry the operation.

### Verification boundary

The Raise Ascender formatter and caller are checked against the ordinary App artifact. Formatting
uses the actual shared helper; wrapper success/no-op/failure tests substitute the
native backend. Those tests prove message composition, disclosure forwarding and
exception propagation. They do not prove FontLab editing, native window behavior,
whole-font preservation or successful Undo/Redo. The writer’s artifact tests and
its dedicated native qualification are separate requirements.

The background example is also executed verbatim against the installed App
backend and planner. Owned native doubles cover master/auxiliary scope, stale
previews, no-op, partial removal and interruption. The backend itself is not
replaced. These checks still do not exercise FontLab's compiled object model,
native history, saved files, rendered documentation or publication.
