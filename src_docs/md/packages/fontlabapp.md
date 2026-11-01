---
this_file: src_docs/md/packages/fontlabapp.md
---
# Fontlabapp

Fontlabapp is the Python layer for FontLab's application surface: menus and
actions, panels, preferences, versions and paths, Glyph and Preview windows,
drawing overlays, and docks, dialogs and widgets you create yourself.

This page describes Fontlabapp v0.2.4.

## Install

Install `fontlab-fontlabapp` into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab). Its utilities import
outside FontLab without loading native modules or creating preference files.

## Quick start

```python
# Inside FontLab
from fontlabapp import Application

app = Application(with_ui=True, with_preflib=False)
print(app.versions.app_version)

with app.control as fl:
    print(fl.fonts())
    fl.panel("preview").show()
    fl.preview.set_text("Hamburgefonts").set_font_size(48)
```

## Examples

Draw on the Glyph window without changing the font. The overlay is removed when
the context exits:

```python
from PythonQt import QtGui

with app.control as fl:
    glyph_window = fl.glyph_window()          # raises if no Glyph window is open

    def paint(painter):
        painter.setPen(QtGui.QColor("#008000"))
        painter.drawLine(30, 30, 100, 100)

    with glyph_window.draw(paint, coordinates="canvas") as overlay:
        overlay.raise_if_failed()
```

Create your own panel, modeless dialog or tool widget:

```python
def build(widget):
    layout = QtGui.QVBoxLayout(widget)
    layout.addWidget(QtGui.QLabel("My tool", widget))

with app.control as fl:
    panel = fl.create_panel("My panel", build, area="right")
    panel.close()
```

Edit vertical metrics or alignment zones on several masters as one Undo step:

```python
from fontlabapp import master_metrics, zone_native
from fontlabapp.scripting import current_package

package = current_package()                   # the current font, Font window active
master_metrics.write_master_metrics(
    package, {"Regular": {"xHeight": 500}, "Bold": {"capsHeight": 705}},
    title="Master Metrics",
)
zones = zone_native.backend()                 # the zone_editor.Backend for this font
```

These writers refuse before any history call when FontLab is not on the GUI thread,
when a Glyph window is the active editor, or when the font has an unknown field or
master. A failure during the write restores every written value and adds nothing to
Undo (`font_history.RolledBackError`). After Undo or Redo of such a step, FontLab
shows only some metric guidelines until the font is reopened (fl#8574); the saved
file is correct. `outline_extent.vertical_extent(layer)` measures glyph extents from
outline nodes, because `flLayer.boundingBox` can stay stale after scripted edits
(fl#8575).

The `fontlabapp_shim` reference lists FontLab's menus, actions and panels as
Python names (788 of 788 resolve in FontLab 9).

## FontUI: font and glyph browsers and editors

`fontlabapp.fontui` provides ready-made Qt tools that work on an explicit font
model (ufoLib2, defcon, or live FontParts objects from [Fontport](fontport.md)).
Install the extra that matches the tools you need:

| Extra | Adds |
| --- | --- |
| `fontlab-fontlabapp[fontui]` | `font_browser`, `glyph_browser`, `glyph_preview`, `features_editor`, `designspace_panel` |

The FontParts-bound editors moved to [Fontport](fontport.md#ui-editors):
`font_info_editor`, `groups_editor`, `kerning_editor`, `transform_editor`,
`batch_panel` and `glyph_sequence`. Import them from `fontlab_fontport.ui`. The
old `fontlabapp.fontui` names raise an `ImportError` that names the new home.

Each function returns a handle. Keep a reference to it, show its `.widget` and
call `.close()` when you are done. The browsers, preview and features editor
also have `.refresh()` for edits made elsewhere; `designspace_panel` does not:

```python
# Inside FontLab, with the fontui extra and ufoLib2 installed
from ufoLib2 import Font
from fontlabapp.fontui import font_browser

font = Font()                       # a detached demonstration model
font.info.familyName = "Browser demonstration"
glyph = font.newGlyph("A")
glyph.width = 600
pen = glyph.getPen()
pen.moveTo((50, 0)); pen.lineTo((300, 700)); pen.lineTo((550, 0)); pen.closePath()

browser = font_browser([font])      # keep this handle alive
browser.widget.resize(850, 1000)
browser.widget.show()
# ... later:
browser.close()
```

The features editor stages changes and applies them in one validated batch; a
model without a batch apply opens read-only.

While a script has unfinished point edits on a font, the controls that follow
FontLab changes skip that font's reload rather than discard the edits, and show
"A font has unfinished script edits; its view updates when the script finishes."
The view updates on the next change after the script completes.

## Limits

- `Application(with_preflib=False)` inspects the application without opening or
  saving the preference library.
- Native wrappers may be recreated on each access: compare fonts by native id,
  not with `is`.
- Created panels, dialogs and widgets own only themselves; close them when done.

Reference: [fontlabapp](../reference/fontlabapp.md),
[FontLab menus and panels](../reference/fontlabapp_shim.md).
