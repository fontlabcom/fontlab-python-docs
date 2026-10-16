---
this_file: site-src/guide/ui.md
---
# Panels and drawing

Fontlabapp provides direct native panel/window discovery, Output text, Preview
and Glyph-window drawing, and owned custom widgets. Grablab exports actual
widgets to bitmaps and SVG.

```python
from fontlabapp import FontLab

with FontLab() as app:
    print(app.output())
    preview = app.preview
    windows = app.glyph_windows()
```

Inspect [the native FontLab controller][fontlabapp.controls.FontLab] for the
current API. A context closes only UI resources it owns. User-open documents
and unrelated widgets remain owned by the application.

PythonQt exposes several Qt properties as values, while PySide2 exposes methods:
`widget.width`, `line_edit.text`, and `scrollbar.maximum` are examples in the
captured host. Use the captured binding contract rather than blindly copying
upstream PySide2 calls. Qt5/PySide2 documentation is labeled in this reference.

Foreground overlays are useful for drawing over a view. Before/after-native-layer
reporter painting also requires actual native paint ordering, per-glyph item
transforms, clipping and callback-scoped painter lifetime. That expanded Glyport
integration is pending; a child overlay alone does not prove background painting.
