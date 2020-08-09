
# FontLab 7 Python API

Version: 2020-08-09

The Python API for FontLab 7 consists of 4 packages:

- [`typerig`](typerig.md)
- [`fontlab`](fontlab.md)
- [`fontgate`](fontgate.md)
- [`FL`](FL.md)

You can also use the [`PythonQt`](PythonQt.md) package to interact with the OS and build GUIs.

## `typerig`

TypeRig is a Python library and set of tools for FontLab 7. It is developed by Vassil Kateliev. TypeRig provides several plugins that extend the functionality of FontLab, see [documentation](https://kateliev.github.io/TypeRig/). But it also comes with a `typerig` package that provides a simplified, alternative “pythonic” API to FontLab. TypeRig is written in Python.

To use the `typerig` package, run FontLab 7, choose _Scripts > Update / Install Scripts_. Click _OK_ in the dialog, wait until the installation completes. When you see the TypeRig is up-to-date dialog, click _OK_ and restart FontLab 7.

## `fontlab` and `fontgate`

The `fontlab` package exposes most or all of the FontLab 7 GUI and high-level font-related objects. The `fontgate` package exposes more technical aspects of fonts, and does not include GUI functionality.

Some functionality is in `fontgate`, some in `fontlab`, but `typerig` abstracts and combines both packages. Both `fontgate` and `fontlab` are “bindings”, i.e. they’re not true Python packages, but instead interfaces that you can use from within Python.

- [`fontlab`](fontlab.md): the API docs for the `fontlab` package
- [`fontgate`](fontgate.md): the API docs for the `fontgate` package


## `FL`

The `FL` package exposes a legacy API that is largely compatible with the old FontLab Studio 5 Python API. However, we no longer actively develop it, and it’s only useful for very simple scripts.

- [`FL`](FL.md): the API docs for the `FL` package

## `PythonQt`

FontLab uses Qt, a cross-platform set of APIs for user interface development and interaction with the operating system. Qt provides a unified API whether you use macOS or Windows. The `PythonQt` package exposes the entire Qt API to Python.

- [`PythonQt`](PythonQt.md): FontLab’s API docs for the `PythonQt` package
- [official PythonQt](https://mevislab.github.io/pythonqt/): the official documentation of PythonQt
- [PySide2 by Qt](https://doc.qt.io/qtforpython/index.html): documentation of `PySide2`, which is an alternative Qt-Python bridge. The documentation is useful in exploring what you can do with Qt. Some details differ between PySide2 and PythonQt, so always check PythonQt documentation.
