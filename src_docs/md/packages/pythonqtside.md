---
this_file: src_docs/md/packages/pythonqtside.md
---
# Pythonqtside

Pythonqtside lets code written for PySide2 (`QtCore`, `QtGui`, `QtWidgets`, …)
run on FontLab's built-in PythonQt. It routes each PySide2 name to the native
class and adapts the differences that matter in practice: keyword arguments,
property getters, overloads and protected event handlers. It never loads a
second Qt binding or creates a `QApplication`.

## Install

Install `pythonqtside` (it depends on Echopy) into FontLab's Python folder; see
[Install into FontLab](index.md#install-into-fontlab).

## Quick start

```python
# Inside FontLab
from pythonqtside import QtCore, QtGui, QtWidgets

widget = QtWidgets.QWidget()          # the original native QWidget
layout = QtWidgets.QVBoxLayout(widget)
layout.addWidget(QtWidgets.QLabel("Hello from PySide2-style code"))
widget.show()
```

## Examples

Port an existing PySide2 tool by changing only its import:

```python
# from PySide2 import QtCore, QtWidgets
from pythonqtside import QtCore, QtWidgets
```

Available namespaces: `QtCore`, `QtGui`, `QtWidgets`, `QtNetwork`, `QtOpenGL`,
`QtSvg`, `QtUiTools`, `QtXmlPatterns` and the combined `Qt`.

## Limits

- Use FontLab's running application; do not call `QApplication.exec()`.
- Names alone do not guarantee identical behaviour: enum conversion, ownership and
  some overloads differ from PySide2. See the [PySide2 guide](../guide/pyside.md).
- Qt 6 / PySide6 is not supported (FontLab 9 uses Qt 5).

Reference: [pythonqtside](../reference/pythonqtside.md).
