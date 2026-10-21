---
this_file: src_docs/md/packages/grablab.md
---
# Grablab

Grablab captures FontLab's interface for documentation and tests: panels, menus,
Glyph and Font windows, screens and widgets, as PNG, SVG or PDF with title and
description metadata.

## Install

Install `fontlab-grablab` together with `fontlab-fontlabapp` into FontLab's Python
folder; see [Install into FontLab](index.md#install-into-fontlab). Importing
`grablab` is host-free; capturing needs FontLab.

## Quick start

```python
# Inside FontLab
from grablab import Grab

capture = Grab(grab_canvas=False, grab_screens=False)
capture.newGrab()
paths = capture.grabPanel("elements")
print(paths)
```

## Examples

Capture a widget, including a Fontlabapp drawing overlay, as SVG and PNG:

```python
from pathlib import Path
from fontlabapp import Application
from grablab import Grab

app = Application()
folder = Path.home() / "Desktop" / "captures"
folder.mkdir(exist_ok=True)
grab = Grab(application=app, folder_base=folder)
with app.control as fl:
    grab.getWidgetSVG(fl.preview.widget, folder / "preview.svg")
```

## Limits

- Capture temporarily changes OpenGL, outline-thickness and pixel-rendering
  preferences and restores them afterwards, even on failure.
- OpenGL canvases have Qt framebuffer limits; the non-OpenGL Glyph view and
  Preview paths are verified.

Reference: [grablab](../reference/grablab.md).
