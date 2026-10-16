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

## Limits

- `Application(with_preflib=False)` inspects the application without opening or
  saving the preference library.
- Native wrappers may be recreated on each access: compare fonts by native id,
  not with `is`.
- Created panels, dialogs and widgets own only themselves; close them when done.

Reference: [fontlabapp](../reference/fontlabapp.md),
[FontLab menus and panels](../reference/fontlabapp_shim.md).
