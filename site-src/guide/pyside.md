---
this_file: site-src/guide/pyside.md
---
# PySide2 compatibility

FontLab supplies PythonQt and an existing Qt5 application. Pythonqtside provides
the QtCore/QtGui/QtWidgets namespace routing used by `fly.qs`.

```python
from pythonqtside import QtCore, QtWidgets
```

The PySide2 reference package does not support the captured Python3.11 host.
The expanded adapter will translate ordinary PySide2 app imports and binding
behavior onto PythonQt, including property getters, constructors, signals,
ownership, forms, models/views, painting, timers and processes.

The planned `pythonqtside.run_app()` is pending. Namespace routing alone is not
unchanged-app compatibility. Full acceptance requires real native windows,
callbacks, responsiveness, cleanup and owned-font editing/undo/save/reopen.

Reuse FontLab's application and event loop. Do not load a second Qt runtime or
start a nested standalone application loop in the host.
