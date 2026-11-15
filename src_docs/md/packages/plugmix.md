---
this_file: src_docs/md/packages/plugmix.md
---
# Plugmix

Plugmix v1.1.17 is an Extensions pack for App's `fontlabapp.plugins` core: 50 plugins,
with 39 reporters, five filters, four tools, one palette and one General plugin.
The separate `fontlab_plugmix` wheel remains a supported compatibility runtime;
it contains no Extensions bundles.

Both runtimes have five plugin kinds:
**reporters** (toggleable, read-only overlays on the Glyph window), **filters**
(undoable edits to selected glyphs), **palettes** (dockable panels), **tools**
(native FontLab tools) and **General** plugins (menu commands and font events).
Plugmix uses
FontLab's PythonQt and, on older builds, Fontlabapp's editor painters. It does not
use PySide2, and it does not emulate Glyphs.app.

## Install and start the Extensions pack

Use the released `fontlab-python-plugmix-extensions.zip` pack with
`fontlab-fontlabapp>=1.2.10` and `fontlab-fly>=1.3.0` in FontLab's Python 3.11 arm64
environment. Run App's `install.vfpy` first, then the Plugmix checkout's
`install.vfpy` from FontLab's Scripts panel with the App checkout beside it.
For a manual installation, prepare those packages and copy the pack's Extensions
contents into the FontLab user-data `Extensions/` folder. The pack's bundles live
under `Extensions/<kind>/`; installing the compatibility wheel does not install them.

The shipped `initScript-snippet.py` starts App through Fly. Its startup call is:

```python
from fly.ap.plugins import install
install()
```

Use the Reporters palette or **View > Reporters** to enable reporters.

<a id="the-scripts-folder"></a>

The only shipped menu script, `Scripts/Plugmix/Show Reporters.py`, opens that palette.
App owns bundle discovery, preferences, callbacks and native UI.
`fontlabapp.plugmix` is a deprecated alias retaining the same App objects; it is
distinct from the independent `fontlab_plugmix` compatibility runtime below.

App plugin classes use the `fontlabapp.plugmix` entry-point group. Compatibility
classes use `fontlab_plugmix.plugins`. The class bases and groups are not
interchangeable; Fly's `fly.ap.plugins` returns App's own classes.

!!! warning "Choose one runtime per session"
    App and the compatibility runtime both use `fontlab-plugmix.json` in FontLab's
    Data folder. Do not combine their startup installers in one FontLab session.
    Cross-runtime preference migration remains unqualified. Native palette/menu,
    drawing, teardown and writer-history acceptance still need the exact installed tuple.

## Retained compatibility runtime

The remaining API descriptions and examples use the supported
`fontlab_plugmix` compatibility package: 19 reporters, one filter, one palette,
one tool and one General plugin. They do not describe the 50 Extensions bundles.

### How it works

FontLab 9 builds with native canvas painters expose two Python hooks on the host
itself: a canvas painter (`flCanvas.appendPythonPainter`) and a workspace tool
(`flWorkspace.registerPythonTool`). See [Native Python hooks in
FontLab 9](../guide/native-hooks.md). Plugmix reporters build on the painter hook.

- **Registry.** Finds plugins of every kind, remembers your choices, and attaches
  or detaches them. Built-in plugins and plugins published through the
  `fontlab_plugmix.plugins` entry-point group are discovered the same way, and the
  kind comes from the class's base class. A plugin needs a unique `name` and a
  human-readable `title`; names are unique across kinds.
- **Native-painter backend.** When `flCanvas.appendPythonPainter` exists, Plugmix
  attaches one painter per Glyph window as it becomes active and registers each
  reporter on it. Reporters with `layer = "background"` paint under the glyph; the
  others paint over it. On older builds the backend falls back to Fontlabapp's
  `EditorPainters`, paints everything over the canvas and logs the background
  substitution once.
- **Coordinates.** A glyph point is mapped through the glyph's position in its text
  block, then the text block's placement, then `canvas.mapToViewportF` into
  viewport pixels.
- **Cost.** Each reporter reads the glyph again on every repaint. That is fine for
  the built-in set but adds up with many reporters enabled.

Plugins compute from immutable, plain-Python snapshots, so you can test them
without FontLab.

### Install

Install `fontlab-python-plugmix` and its `fontlab-fontlabapp` dependency into
FontLab's Python folder; see [Install into FontLab](index.md#install-into-fontlab).

Start Plugmix once per FontLab session from your own `initScript.py`:

```python
try:
    from fontlab_plugmix import install; install()
except Exception as error: print(f"Plugmix startup: {error}")
```

This is an explicit compatibility startup example. The shipped
`initScript-snippet.py` starts the App runtime instead; do not use both. Nothing
in the package edits FontLab's startup file.

For the compatibility runtime, `install()` adds menu entries and restores your choices:

| Kind | Where it appears |
| --- | --- |
| Reporter | One checkable **Plugmix: Show ...** action per reporter in the View menu. |
| Filter | **Plugmix: Delete Small Paths…** in the Glyph menu, opening a non-modal parameter dialog. |
| Palette | **Plugmix: Step and Repeat Panel** in the Window menu, checkable, hidden until shown. |
| Tool | **Plugmix: Tool Smart Select** in the Window menu, which registers a native tool when enabled. |
| General | **Plugmix: Zoom to Selection** in the View menu. |

Choices live in one JSON file in FontLab's `Data` folder, with these keys:
`enabled` (reporters), `enabled_filters`, `enabled_palettes`, `enabled_tools`,
`enabled_general` and `params` (last-used filter values). Older files with only
`enabled` still load, filters, tools and General plugins are enabled by default,
and `enabled_palettes` is written only after you choose a
visibility. Within this compatibility runtime, a selection saved under the former
name `nodes_outside_paths` restores as `offcurve_outside_bounds`.
`fontlab_plugmix.boot.uninstall()` removes the actions, overlays
and panels and keeps the saved choices.

### Reporters

Built-in reporters:

| Reporter | Overlay |
| --- | --- |
| Duplicate Anchor Rings | Rings around anchors less than one font unit apart. |
| Node Indexes | Contour index beside every on- and off-curve node. |
| Selected Node Coordinates | Coordinates beside selected nodes. |
| Two Point Distance | Segment, length and angle for exactly two selected nodes. |
| Off-curve Handles Outside Bounds (`offcurve_outside_bounds`) | Off-curve handles beyond the on-curve bounding rectangle. It tests bounds, not path containment. |
| Center Lines | Advance/2, x-height/2 and cap-height/2 lines. |
| Vertical Metrics | Labelled ascender, descender, x-height, cap-height and baseline. |
| Angled Handles | Rings on off-curve handles outside horizontal, vertical and italic axes. |
| Crosshair | Guides through selected nodes. |
| Tops and Bottoms | Rings and y labels at tied highest and lowest on-curve positions. |
| Segment Length | Straight and flattened curve lengths for selected segments. |
| Glyph Focus | Shade outside the advance box between descender and ascender. |
| Emphasise Selected Handles | Accent lines and rings for handles next to selected nodes. |
| Anchor Cloud | Names and positions of the current glyph's anchors. |
| RSB Line | Advance boundary plus RSB and LSB labels. |
| Unitizer | Vertical grid at UPM / 18 increments. |
| Nodes Close to Zones | Rings on on-curves near zone edges or metric heights. |
| Imprecise Italic Angle | Straight segments close to, but not exactly on, the master slant. |
| Smooth Node Angles | Handle-angle mismatch and handle-length ratio at smooth nodes. |

#### Write your own reporter

This example uses the compatibility runtime's `Mark` and `Reporter` classes.

```python
from fontlab_plugmix import Mark, Reporter


class Origin(Reporter):
    name = "origin"
    title = "Origin"

    def compute(self, snapshot):
        return [
            Mark("ring", ((0, 0),), diameter_px=12),
            Mark("text", ((6, 6),), text="origin", text_px=11),
        ]
```

`compute()` returns marks in font units. Mark kinds are `ring`, `line`, `polyline`,
`polygon` (with an RGBA `fill`) and `text`; stroke width, text size and ring
diameter are view pixels, so overlays keep their size while you zoom. Set
`layer = "background"` to paint under the glyph on builds with native painters.

Publish the class so Plugmix finds it. In your package's `pyproject.toml`:

```toml
[project.entry-points."fontlab_plugmix.plugins"]
origin = "my_package.reporters:Origin"
```

Reinstall your package and restart FontLab; the reporter appears in the View menu.

### Filters

A filter computes a proposed edit for one layer from a frozen snapshot and typed
values, and Plugmix applies the result to the selected glyphs as one Undo step.

- `Param(key, label, kind, default, minimum=None, maximum=None, choices=())`
  declares a dialog field. `kind` is `"float"`, `"int"`, `"bool"` or `"choice"`;
  values outside the declared domain are rejected.
- `LayerEdit(contours=None, advance=None, anchors=None)` holds replacement values;
  `None` leaves that part of the layer alone.
- `Filter.compute(snapshot, values)` returns a `LayerEdit`. `Filter.validate(values)`
  fills defaults and rejects unknown or invalid parameters.

```python
from fontlab_plugmix.filter import Filter, LayerEdit


class DropOpenPaths(Filter):
    name = "drop_open_paths"
    title = "Drop Open Paths"
    params = ()

    def compute(self, snapshot, values):
        kept = tuple(c for c in snapshot.contours if c.closed)
        return LayerEdit(contours=kept)
```

The writer currently supports contour deletion. It skips shared or transformed
outlines and automatic layers per glyph and still edits the other selected glyphs.

**Delete Small Paths** (`delete_small_paths`, one parameter `threshold`, default
400 font units squared) deletes a closed contour when its area, measured on the
flattened curves, is strictly below the threshold. A contour whose flattened
bounding-box area is below the threshold is treated the same way. Open paths always
stay, and a contour exactly at the threshold stays.

### Palettes

A palette is a dockable panel. `Palette.build(ui)` creates controls once through
`PaletteUI`, `refresh(context)` runs when the active glyph, master, revision or node
selection changes, and `close()` releases resources. `PaletteUI` offers `label`,
`number`, `checkbox` and `button`, so palettes import no Qt. One timer serves all
visible palettes and stops when none are visible.

**Step and Repeat** (`step_and_repeat`) duplicates the selected contours of the
active glyph. `count` is the number of *additional* copies, and each copy is shifted
by another (`dx`, `dy`), so offsets accumulate. Apply is one Undo step. It works
on the current master layer only: when the Glyph window shows another layer, Apply
refuses with a status message instead of writing to the master.

### Tools

A tool becomes a native FontLab tool through `flWorkspace.registerPythonTool`.
`Tool.activate(ctx)` and `deactivate()` bracket its use; `press`, `move`, `release`,
`double_click`, `key_down` and `key_up` each take a `ToolEvent` and return `True`
when they handled it; `marks(glyph)` returns overlay marks drawn only while the
tool is active. `ToolContext` offers `snapshot()`, `select(indices, toggle=False)`,
`edit(plan_fn, title)` and `redraw()`. Viewport events are mapped through
FontLab's pan and zoom and the glyph's text-block transforms.

**Smart Select** drags a rectangle and selects whole contours touched by any node;
Shift toggles those contours. It is selection-only and never changes outline
geometry. It omits the source plugin's double-click containment and native move
handling.

### General plugins

A General plugin is a menu command with optional font events. `General.start(ctx)`
and `stop()` bracket its life, `run()` handles the command, and
`on_font_opened(font_id)` and `on_font_closed(font_id)` report fonts by the stable
`flPackage.fgId`, the id that MCP, Remopy and Fontport use. `GeneralContext`
offers `notify`, `snapshot`, `edit`, `timer` and `zoom_selected`. Plugmix owns the
extra actions and timers a General plugin creates and removes them on
`uninstall()`. General font watchers share the palettes' 250 ms timer.

**Zoom to Selection** fits the active glyph's selected nodes in the canvas with a
margin. It omits the source plugin's delayed viewport adjustment. Shortcut
conflicts are reported, not overridden. Shortcut handling and keyboard cursor
mapping still need an in-app recheck.

### Limits

- Reporters are read-only. Filters, palettes and tools edit only through Plugmix's
  shared outline writer.
- Painting runs inside FontLab's paint event on the GUI thread. Keep `compute()`
  quick.
- The palette refresh key reads the glyph modification timestamp and node
  selection; confirm that edits outside Plugmix advance it in your build.
- Native behaviour needs an in-app check: the test suite uses fake Qt and FontLab
  objects, and some newer reporters have offline coverage only.
