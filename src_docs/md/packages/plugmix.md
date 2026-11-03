---
this_file: src_docs/md/packages/plugmix.md
---
# Plugmix

Plugmix is a package of native FontLab 9 plugins. Its first plugins are
reporters: toggleable, read-only overlays drawn on top of the Glyph window, such
as node indexes, duplicate anchors or vertical metrics. It uses FontLab's
PythonQt and Fontlabapp's editor painters. It does not use PySide2, and it does
not emulate Glyphs.app.

!!! note "Under revision"
    Plugmix is being revised. This page describes the stable concepts: the
    registry, the `Reporter` base class, the built-in reporters, the startup hook
    and the `Scripts/` folder. Exact module names and defaults can still change.

## How it works

FontLab 9 exposes two Python hooks on the host itself: a canvas painter
(`flCanvas.appendPythonPainter`) and a workspace tool
(`flWorkspace.registerPythonTool`). See [Native Python hooks in
FontLab 9](../guide/native-hooks.md). Plugmix builds on the painter hook.

- **Registry.** Finds reporters, remembers which ones you enabled, and attaches
  or detaches their painters. Built-in reporters and reporters published through
  the `fontlab_plugmix.plugins` entry-point group are discovered the same way. A
  reporter needs a unique `name` and a human-readable `title`.
- **Reporter base class.** A reporter has a pure `compute(snapshot)` method. It
  receives an immutable, plain-Python snapshot of one glyph and returns a list of
  `Mark` objects in font units. The base class does the drawing, converts
  coordinates, and keeps every error out of FontLab's paint event.
- **Mark kinds.** `ring`, `line`, `polyline` and `text`. Positions are glyph units.
  Stroke width, text size and ring diameter are view pixels, so overlays keep
  their size while you zoom.

Because `compute()` touches no FontLab object, you can test a reporter without
FontLab.

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

`install()` adds one checkable **Plugmix: Show ...** action per reporter to the
View menu and restores the reporters you left enabled. Your choice is saved in a
single JSON file in FontLab's `Data` folder. `uninstall()` removes the actions and
overlays and keeps the saved selection.

## Built-in reporters

| Reporter | Overlay |
| --- | --- |
| Duplicate Anchor Rings | Rings around anchors less than one font unit apart. |
| Node Indexes | Contour index beside each on-curve node. |
| Selected Node Coordinates | Coordinates beside selected nodes. |
| Two Point Distance | Segment, length and angle for exactly two selected nodes. |
| Nodes Outside Paths | Off-curve handles beyond the on-curve bounding rectangle. |
| Center Lines | Advance/2, x-height/2 and cap-height/2 lines. |
| Vertical Metrics | Labelled ascender, descender, x-height, cap-height and baseline. |

## Write your own reporter in 20 lines

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

Publish the class so Plugmix finds it. In your package's `pyproject.toml`:

```toml
[project.entry-points."fontlab_plugmix.plugins"]
origin = "my_package.reporters:Origin"
```

Reinstall your package and restart FontLab; the reporter appears in the View menu.
Test it without FontLab by calling `compute()` on a hand-built snapshot.

## The Scripts folder

The repository's `Scripts/` folder holds ordinary FontLab menu scripts: one to
install the Plugmix menu, and one per reporter under `Scripts/Plugmix/Reports/`.
Copy them into FontLab's Scripts folder to run a reporter from the Script menu
instead of from the View menu.

## Limits

- Reporters are read-only. They draw; they never edit the font.
- Painting runs inside FontLab's paint event on the GUI thread. Keep `compute()`
  quick.
- The test suite uses fake Qt and FontLab objects. Native behaviour still needs an
  in-app check.
