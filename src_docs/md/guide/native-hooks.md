---
this_file: src_docs/md/guide/native-hooks.md
---
# Native Python hooks in FontLab 9

FontLab 9 lets Python draw on the Glyph canvas and register its own tools. Both
hooks live on the host objects, so you need no helper package to use them.
Plugmix and Glyport wrap them with friendlier APIs.

!!! warning "Host build"
    These methods exist only in FontLab 9 builds that include the Python
    scripting hooks. Check `hasattr(flCanvas, "appendPythonPainter")` before
    relying on them.

Everything here runs on the GUI thread. Calling a registration function from
another thread raises `RuntimeError`.

## Get the canvas

```python
from fontlab import flWorkspace

canvas = flWorkspace.instance().getActiveCanvas()   # a flCanvas, or nothing
```

`getActiveCanvas()` returns the canvas of the active window, or nothing when no
canvas is active.

## Draw with a canvas painter

```python
from fontlab import flCanvas
from PythonQt import QtCore, QtGui

def paint(painter, canvas):
    painter.setPen(QtGui.QColor("#d03030"))
    centre = canvas.mapToViewportF(QtCore.QPointF(0, 0))
    painter.drawEllipse(centre, 8, 8)

token = canvas.appendPythonPainter(paint, flCanvas.OverOwner)
# later
canvas.removePythonPainter(token)
```

`appendPythonPainter(callback, order=UnderOwner)` returns an integer token.
`removePythonPainter(token)` returns `True` when it removed the painter and
`False` when the token is unknown or belongs to another canvas.

**Callback signature.** `callback(painter, canvas)`. The painter is a `QPainter`;
the canvas is the `flCanvas` being painted.

**Order.** `flCanvas.UnderOwner` (`0`) paints before the item that owns the canvas
(the glyph); `flCanvas.OverOwner` (`1`) paints after it. Any other value raises
`ValueError`. The default is `UnderOwner`.

**Coordinates.** FontLab resets the painter's transform before each call, so you
draw in viewport pixels, with the origin at the viewport's top-left corner. To
place something at a canvas position, convert it first: `mapToViewportF` takes a
`QPointF` and returns a `QPointF`, or takes a `QLineF` and returns a `QLineF`.
`mapToViewport` is the integer form for `QPoint`, `QRectF` and `QPolygonF`. Pen
widths and text sizes stay in pixels, so they do not scale with zoom.

**Painter lifetime.** The painter is valid only during the callback. Do not store
it, and do not use it after the callback returns. FontLab saves the painter state
before calling you and restores it afterwards.

**Errors.** An exception in your callback is printed to the Python console and
does not stop the paint. Other painters still run.

**Scope and cleanup.** A painter belongs to one canvas, and FontLab discards it
when that canvas is destroyed. Painting does not nest: a callback that provokes
another paint pass during painting is skipped for that pass. Adding or removing a
painter asks the canvas to repaint.

## Register a tool

```python
from fontlab import flWorkspace

class Probe:
    def activate(self):
        print("probe on")

    def deactivate(self):
        print("probe off")

    def mousePressed(self, event, canvas):
        print(event.pos())
        return True          # handled

    def paint(self, painter, canvas):
        painter.drawText(10, 20, "Probe")

workspace = flWorkspace.instance()
token = workspace.registerPythonTool("Probe", None, Probe())
# later
workspace.unregisterPythonTool(token)
```

`registerPythonTool(name, icon, object)` returns an integer token. `name` must not
be empty. `icon` is a `QIcon` or `None`. `object` is any Python object; FontLab
looks up each method by name when the event happens, so implement only what you
need. The tool appears as a checkable action in the Tools list and in the toolbar.
`unregisterPythonTool(token)` removes those entries, deactivates the tool if it is
active, and returns `True` on success.

| Method | Arguments | Called when |
| --- | --- | --- |
| `activate`, `deactivate` | none | The tool becomes, or stops being, the main tool. |
| `mousePressed`, `mouseMoved`, `mouseReleased`, `mouseDoubleClicked` | `(event, canvas)` | A mouse event reaches a canvas of the tool's workspace. |
| `keyPressed`, `keyReleased` | `(event, canvas)` | A key event reaches such a canvas. |
| `paint` | `(painter, canvas)` | The canvas paints over the owner. Same rules as a canvas painter. |

**Events.** Mouse methods receive a `QMouseEvent`, key methods a `QKeyEvent`. Both
are valid only during the call. Return a true value to mark the event as handled;
FontLab then accepts it and stops normal processing. Return nothing to let FontLab
continue. FontLab offers a key press to `keyPressed` before it resolves
shortcuts, so a handled key beats a shortcut, and it reuses your answer for the
key press that follows.

**Active tool only.** Event methods and `paint` run only while your tool is the
active tool. `paint` always runs over the owner.

**Cleanup.** FontLab unregisters a workspace's tools when that workspace closes. A
callback may safely unregister its own tool.

## Choosing between the hooks

| Need | Hook |
| --- | --- |
| An overlay that is always on, in every tool | Canvas painter |
| An overlay or interaction that belongs to one tool | Tool `paint` and mouse methods |
| A menu or toolbar entry that takes over the canvas | Tool |

For ready-made reporters, filters and tools see [Plugmix](../packages/plugmix.md);
Glyport uses the same hooks for Glyphs reporters and tools. Fontlabapp's
`glyph_window.draw` overlay is a separate mechanism, not a wrapper for these hooks;
see [Fontlabapp](../packages/fontlabapp.md).
