---
this_file: src_docs/md/packages/plugmix.md
---
# Plugmix

Plugmix is a package of native FontLab 9 plugins. It has three plugin kinds that
work today: **reporters** (toggleable, read-only overlays on the Glyph window),
**filters** (undoable edits to selected glyphs) and **palettes** (dockable
panels). Tool and General plugins are designed but not built. Plugmix uses
FontLab's PythonQt and, on older builds, Fontlabapp's editor painters. It does not
use PySide2, and it does not emulate Glyphs.app.

!!! note "Under revision"
    Plugmix is being revised. This page describes the stable concepts. Exact
    module names and defaults can still change.

## How it works

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

## Install

Install `fontlab-python-plugmix` and its `fontlab-fontlabapp` dependency into
FontLab's Python folder; see [Install into FontLab](index.md#install-into-fontlab).

Start Plugmix once per FontLab session from your own `initScript.py`:

```python
try:
    from fontlab_plugmix import install; install()
except Exception as error: print(f"Plugmix startup: {error}")
```

The package ships this snippet as `initScript-snippet.py`. Nothing in the package
edits a FontLab installation. Alternatively, run `Install Plugmix Menu.py` from
the Script menu.

`install()` adds menu entries and restores your choices:

| Kind | Where it appears |
| --- | --- |
| Reporter | One checkable **Plugmix: Show ...** action per reporter in the View menu. |
| Filter | **Plugmix: Delete Small Paths...** in the Glyph menu, opening a non-modal parameter dialog. |
| Palette | **Plugmix: Step and Repeat Panel** in the Window menu, checkable, hidden until shown. |

Choices live in one JSON file in FontLab's `Data` folder, with these keys:
`enabled` (reporters), `enabled_filters`, `enabled_palettes` and `params`
(last-used filter values). Older files with only `enabled` still load, filters are
enabled by default, and `enabled_palettes` is written only after you choose a
visibility. A selection saved under the former name `nodes_outside_paths`
restores as `offcurve_outside_bounds`. `uninstall()` removes the actions, overlays
and panels and keeps the saved choices.

## Reporters

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

### Write your own reporter

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

## Filters

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

## Palettes

A palette is a dockable panel. `Palette.build(ui)` creates controls once through
`PaletteUI`, `refresh(context)` runs when the active glyph, master, revision or node
selection changes, and `close()` releases resources. `PaletteUI` offers `label`,
`number`, `checkbox` and `button`, so palettes import no Qt. One timer serves all
visible palettes and stops when none are visible.

**Step and Repeat** (`step_and_repeat`) duplicates the selected contours of the
active glyph. `count` is the number of *additional* copies, and each copy is shifted
by another (`dx`, `dy`), so offsets accumulate. Apply is one Undo step.

## The Scripts folder

The repository's `Scripts/` folder holds ordinary FontLab menu scripts: one to
install the Plugmix menu, and one per reporter under `Scripts/Plugmix/Reports/`.
Copy them into FontLab's Scripts folder to run a reporter from the Script menu
instead of from the View menu.

## Limits

- Reporters are read-only. Filters and palettes edit only through Plugmix's shared
  outline writer.
- Painting runs inside FontLab's paint event on the GUI thread. Keep `compute()`
  quick.
- The palette refresh key reads the glyph modification timestamp and node
  selection; confirm that edits outside Plugmix advance it in your build.
- Native behaviour needs an in-app check: the test suite uses fake Qt and FontLab
  objects, and some newer reporters have offline coverage only.
