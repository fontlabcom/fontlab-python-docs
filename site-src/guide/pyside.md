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

[`pythonqtside.run_app(path, *, parent=None)`](../reference/pythonqtside/_app/members-001.md#pythonqtside._app.run_app)
runs a PySide2 source file and its supported local imports inside FontLab's
existing Qt application. It returns an
[`AppHandle`](../reference/pythonqtside/_app/AppHandle.md), retains execution
globals, routes supported imports without replacing the host's import state,
and tracks constructor-created Qt objects and connections for cleanup.
An optional `parent` must be a native QWidget. Call it on the host thread.

Run this from FontLab's scripting surface with your application's source path:

```python
from pythonqtside import run_app

app_handle = run_app("/path/to/my_app.py")
# Inspect app_handle.reports and app_handle.identity_report for routing details.
# Keep the handle while the window is in use; close it when finished.
app_handle.close()
```

`close()` disconnects tracked connections, stops owned work and schedules owned
object cleanup; repeated calls are safe. Inspect `cleanup_errors` for cleanup
failures. Objects returned by arbitrary APIs are borrowed, not automatically owned.

Dynamic exec/eval source, importlib imports, namespace packages and application
subclasses/settings are unsupported. Namespace routing and this implemented
runner do not establish full unchanged-app compatibility. Full acceptance still
requires real native windows, callbacks, responsiveness, cleanup and owned-font
editing/undo/save/reopen across the required application corpus.

Reuse FontLab's application and event loop. Do not load a second Qt runtime or
start a nested standalone application loop in the host.
