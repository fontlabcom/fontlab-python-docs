---
this_file: src_docs/md/guide/owned-window-recovery.md
---

# Keep tool windows usable and recoverable

Keep the returned owner until its window has closed successfully. A failed Close
must leave a reachable window and its exact signal records available for retry.
This guide describes the dialog-ownership App candidate; it is not a released
minimum version or evidence of native FontLab stacking.

## Open a dock inside FontLab

Use FontLab's existing application and PythonQt. This example belongs inside
FontLab; do not install PySide6 there or start another application event loop.

```python
from fly import fl, qt
import fly.ap.widgets as widgets

def build(content):
    layout = qt.QtGui.QVBoxLayout(content)
    layout.addWidget(qt.QtGui.QLabel("Inspect the current font here.", content))

owned_panel = widgets.create_panel(fl.MainWindow(), "Inspection", build, "right")
# Keep owned_panel. When finished, retain it if close returns False or raises.
accepted = owned_panel.close()
```

The Unicode Issues Dock uses this same factory. A hidden MainWindow produces a
floating dock. Later undocking also requests the TypeRig-style priority hint;
the dock keeps its parent, area, content and native window type. Common Glyphs
applies priority inside its existing bounded display/recovery path. Plugin panels
and filter dialogs request priority through `OwnedMenus.tool_window`; their shell
is disposable, while the supplied plugin content remains caller-owned.

The generic script launcher retains an exact candidate when flags, show or raise
fails. A later launch closes that candidate before constructing its replacement.
It also preserves an old owner whose Close refuses or raises. Some panels have a
stronger, dedicated failed-owner fence; preserve that panel's recovery protocol.

## Run these standalone experiments separately

The following setup is for a separate Python 3.11 process with App's test extra.
It uses actual Qt widgets and the actual App helpers over an injected binding
namespace. It never contacts FontLab, reads a font or proves macOS host stacking.
Run the setup afresh for each experiment; retain the QApplication for the process.

<!-- setup: owned-window-qt -->
```python
import os
import sys
assert not {"fontlab", "FL", "PythonQt"}.intersection(sys.modules)
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from contextlib import contextmanager
from types import SimpleNamespace
from unittest.mock import patch
from PySide6 import QtCore, QtWidgets
from shiboken6 import isValid
import fontlabapp.widgets as widgets

APP = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
BINDING = SimpleNamespace(QtGui=QtWidgets, QtCore=QtCore)

def drain():
    APP.processEvents()
    QtCore.QCoreApplication.sendPostedEvents(None, QtCore.QEvent.DeferredDelete)
    APP.processEvents()

@contextmanager
def sandbox(binding=BINDING, parent_type=QtWidgets.QMainWindow):
    parent = parent_type()
    try:
        with patch.object(widgets, "_native", lambda name: binding):
            yield parent
    finally:
        if isValid(parent):
            parent.deleteLater()
        drain()
```

### A hidden host still exposes an owned dock

<!-- example: hidden-parent-floating-dock -->
```python
with sandbox() as parent:
    owned = widgets.create_panel(parent, "Report", None, "right")
    dock, content = owned.widget, owned.content
    assert dock.parentWidget() is parent and dock.widget() is content
    assert dock.isFloating() and dock.isVisible()
    assert dock.windowFlags() & QtCore.Qt.WindowStaysOnTopHint
    assert parent.dockWidgetArea(dock) == QtCore.Qt.RightDockWidgetArea
    assert owned.close() is True
    drain()
    assert owned.closed and not isValid(dock)
```

### Docking stays available when the host is visible

<!-- example: later-undocking-keeps-priority -->
```python
with sandbox() as parent:
    parent.show()
    owned = widgets.create_panel(parent, "Report", None, "left")
    dock = owned.widget
    assert not dock.isFloating()
    dock.setFloating(True)
    assert dock.isFloating() and dock.isVisible()
    assert dock.windowFlags() & QtCore.Qt.WindowStaysOnTopHint
    dock.setFloating(False)
    assert not dock.isFloating() and dock.widget() is owned.content
    assert owned.close()
```

### A refused Close keeps its visible owner

<!-- example: refused-close-retries -->
```python
class Draft(QtWidgets.QDialog):
    allow_close = False
    def closeEvent(self, event):
        event.accept() if self.allow_close else event.ignore()

with sandbox() as parent:
    dialog = Draft(parent)
    owned = widgets.OwnedWidget(dialog, dialog)
    dialog.show()
    assert owned.close() is False
    assert not owned.closed and owned.widget is dialog and dialog.isVisible()
    dialog.allow_close = True
    assert owned.close() is True
    drain()
    assert owned.closed and not isValid(dialog)
```

### Unregistration failure retains the unfinished stage

<!-- example: dock-removal-failure-retries -->
```python
class Host(QtWidgets.QMainWindow):
    fail_removal = True
    def removeDockWidget(self, dock):
        if self.fail_removal:
            raise RuntimeError("owned removal failed")
        QtWidgets.QMainWindow.removeDockWidget(self, dock)

with sandbox(parent_type=Host) as parent:
    owned = widgets.create_panel(parent, "Report", None, "right")
    dock = owned.widget
    try:
        owned.close()
    except RuntimeError as error:
        assert str(error) == "owned removal failed"
    else:
        raise AssertionError("The removal failure was hidden")
    assert owned.widget is dock and not owned.closed and isValid(dock)
    parent.fail_removal = False
    assert owned.close()
    drain()
    assert not isValid(dock)
```

### Keep both setup and cleanup errors

<!-- example: failed-factory-exposes-recovery-owner -->
```python
class Refusing(QtWidgets.QDialog):
    allow_close = False
    def closeEvent(self, event):
        event.accept() if self.allow_close else event.ignore()

binding = SimpleNamespace(QtGui=SimpleNamespace(QDialog=Refusing), QtCore=QtCore)
with sandbox(binding) as parent:
    original = ValueError("report setup failed")
    def fail(content):
        raise original
    try:
        widgets.create_dialog(parent, "Report", fail)
    except ExceptionGroup as failure:
        assert failure.exceptions[0] is original
        recovery = failure.owner
        assert not recovery.closed and isinstance(recovery.widget, Refusing)
        recovery.widget.allow_close = True
        assert recovery.close()
    else:
        raise AssertionError("Refused cleanup lost its recovery owner")
```

### Parent destruction clears references without another Close

<!-- example: parent-death-releases-refused-owner -->
```python
class Refusing(QtWidgets.QDialog):
    def closeEvent(self, event):
        event.ignore()

with sandbox() as parent:
    dialog = Refusing(parent)
    owned = widgets.OwnedWidget(dialog, dialog)
    assert owned.close() is False
    parent.deleteLater()
    drain()
    assert not isValid(dialog) and owned.closed
    assert owned.widget is None and owned.content is None
    assert owned.close() is True
```

Real FontLab acceptance still needs the installed candidate, observed host build,
Font/Glyph-window switching, foreground/background applications, Close/reopen,
parent destruction and all four named fonts' complete preservation/history tests.
Qt flags, a passing standalone experiment and source coverage do not establish
those results. Generated API reference, source-lock and publication remain held.
