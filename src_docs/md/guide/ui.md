---
this_file: src_docs/md/guide/ui.md
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


## Keep an owned dialog alive until cleanup

A modeless dialog returns control immediately. Retain it, connect only callbacks
you own, and disconnect those callbacks before deleting the widget. Closing a
window, pressing Escape, and replacing a previously opened tool must all reach
the same cleanup path. A parent alone does not prove signal cleanup.

The App's script-dialog helpers provide this ownership pattern. The completion
owner routes `finished` through Close, including Escape/reject. Retain it under
`_completion_lifetime`: `close_script_dialog` uses that attribute when it stops
terminal callbacks. Do not add a second `reject()` override that calls `close()`.

<!-- example: owned-dialog -->
```python
from PythonQt import QtGui
import fontlabapp.script_completion as script_completion
import fontlabapp.scripting as scripting

class ExampleDialog(QtGui.QDialog):
    KEY = "example_owned_dialog"

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self._connections = []
        self.setWindowTitle("Owned example")
        layout = QtGui.QVBoxLayout(self)
        self.status = QtGui.QLabel("Close this panel or press Escape", self)
        layout.addWidget(self.status)
        button = QtGui.QPushButton("Close", self)
        layout.addWidget(button)
        scripting.connect_guarded(self, button.clicked, lambda *_: self.close())
        self._completion_lifetime = script_completion.install(self, self.KEY)

    def closeEvent(self, event):
        scripting.close_script_dialog(self, event, self.KEY)

panel = scripting.show_script_dialog(ExampleDialog, ExampleDialog.KEY)
```

The lambda discards the Boolean signal argument before calling argumentless
`close()`; PythonQt does not reliably trim native slot arguments.

Run this inside FontLab with a matching App installation. It creates only an
owned dialog; it does not edit a font. Do not construct `QApplication`, start an
application-wide event loop, or load PySide/PyQt binaries inside FontLab. The
standalone Qt checks for this example use a substitute main-window owner; they
do not prove native PythonQt behavior.

`show_script_dialog` retains one panel per key and adds the priority hint while
preserving its other flags. That is a modeless-panel policy, not proof that every
file chooser or macOS native sheet needs the same flags.

## Keep tool settings separate from chooser settings

Use an explicit file when testing a tool's own settings. This example writes a
single value in a temporary INI file, synchronizes it, and reopens the same file.
It never changes the process-wide default format or settings paths.

<!-- example: owned-settings -->
```python
from pathlib import Path
from tempfile import TemporaryDirectory
from PythonQt import QtCore

with TemporaryDirectory(prefix="fontlab-settings-example-") as directory:
    path = str(Path(directory) / "tool.ini")
    settings = QtCore.QSettings(path, QtCore.QSettings.IniFormat)
    settings.setFallbacksEnabled(False)
    settings.setValue("family", 2)
    settings.sync()
    assert settings.status() == QtCore.QSettings.NoError
    reopened = QtCore.QSettings(path, QtCore.QSettings.IniFormat)
    reopened.setFallbacksEnabled(False)
    assert int(reopened.value("family")) == 2
    del reopened, settings
```

For a tool that remembers window placement, use `saveGeometry()` and
`restoreGeometry()` rather than parsing coordinates yourself. Restore after all
controls exist and before the first show. Missing geometry keeps the layout's
defaults; a false restore result or malformed value needs a usable fallback.
Save before Close cleanup, and run cleanup in `finally` even if persistence
fails. Do not call widget methods from its `destroyed` callback. Qt documents
screen correction and the restore result in
[QWidget::restoreGeometry](https://doc.qt.io/qt-5/qwidget.html#restoreGeometry).

A settings error recorded on a panel that is about to be deleted is not the same
as a message the user can see. Choose a reporting surface deliberately if the
saved state is important; do not prevent cleanup merely to retain that message.

### QFileDialog has its own persistent state

The INI example isolates only the settings objects it constructs. It does not
redirect `QFileDialog`'s internal settings.

In upstream Qt **5.15.2**, file-dialog save/restore uses
`QSettings(UserScope, "QtProject")`. That scoped constructor selects
`NativeFormat` explicitly, so `setDefaultFormat(IniFormat)` does not change it.
On macOS, `setPath(NativeFormat, ...)` also does not redirect the native store.
Cancellation and destruction can still persist chooser state. A fresh process
isolates the in-memory last-visited directory but not the persistent store.
These are source findings, not verification of FontLab's compiled Qt build.
See [QFileDialog settings](https://github.com/qt/qtbase/blob/v5.15.2/src/widgets/dialogs/qfiledialog.cpp#L2921)
and [the scoped QSettings constructor](https://github.com/qt/qtbase/blob/v5.15.2/src/corelib/io/qsettings.cpp#L2575).

`DontUseNativeDialog` selects a widget chooser; it does not disable those
settings reads/writes. In that source version the Cocoa helper also refuses
native display when `WindowStaysOnTopHint` is present. Adding the flag can
therefore change which chooser implementation runs. See
[QCocoaFileDialogHelper::show](https://github.com/qt/qtbase/blob/v5.15.2/src/plugins/platforms/cocoa/qcocoafiledialoghelper.mm#L689).

For chooser tests, use a disposable OS account or VM whose preferences are owned
by the test. Keep the exact `open()` behavior: on macOS, conversion to a sheet
can replace flags set earlier, and rejection restores prior modality. Compare
complete flags, parent, modality, selected-file callbacks and cleanup across
repeated opens. A plain `QDialog` experiment, offscreen platform, alternate
working directory, or changed default settings format does not establish
`QFileDialog` isolation or native acceptance.
