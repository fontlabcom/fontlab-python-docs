---
this_file: site-src/packages/fontlabapp.md
---
# Fontlabapp

Fontlabapp is the Python layer for FontLab's application surface: menus and
actions, panels, preferences, versions and paths, Glyph and Preview windows,
drawing overlays, and docks, dialogs and widgets you create yourself.

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

The `fontlabapp_shim` reference lists FontLab's menus, actions and panels as
Python names (788 of 788 resolve in FontLab 9).

## FontUI: font and glyph browsers and editors

`fontlabapp.fontui` provides ready-made Qt tools that work on an explicit font
model (ufoLib2, defcon, or live FontParts objects from [Fontport](fontport.md)).
Install the extra that matches the tools you need:

| Extra | Adds |
| --- | --- |
| `fontlab-fontlabapp[fontui]` | `font_browser`, `glyph_browser`, `glyph_preview` |
| `fontlab-fontlabapp[fontsequence]` | `glyph_sequence` |
| `fontlab-fontlabapp[fontedit]` | `font_info_editor`, `groups_editor`, `kerning_editor`, `features_editor`, `designspace_panel`, `transform_editor`, `batch_panel` |

Each function returns a handle. Keep a reference to it, show its `.widget`,
call `.refresh()` after edits made elsewhere and `.close()` when you are done:

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

Editors stage changes and apply them in one validated batch; a model without a
batch apply opens read-only. `batch_panel` runs work in a separate Python 3.11+
process so FontLab stays responsive.

## Limits

- `Application(with_preflib=False)` inspects the application without opening or
  saving the preference library.
- Native wrappers may be recreated on each access: compare fonts by native id,
  not with `is`.
- Created panels, dialogs and widgets own only themselves; close them when done.

Reference: [fontlabapp](../reference/fontlabapp.md),
[FontLab menus and panels](../reference/fontlabapp_shim.md).
