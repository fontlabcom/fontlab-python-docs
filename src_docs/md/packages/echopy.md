---
this_file: src_docs/md/packages/echopy.md
---
# Echopy

Echopy makes FontLab's native Python API readable by editors, type checkers and
documentation tools. Inside FontLab, it returns the original native objects.
Outside FontLab, it provides declarations; it does not emulate the font editor.

Use `echopy` for short imports or `fontlab_echopy` for explicit package names.
Matching submodules imported through either name resolve to the same module
objects. The examples below use Python 3.11.

## Install and identify your copy

Install the `fontlab-echopy` wheel into the Python environment where you need
its declarations. For host use, follow [Install into FontLab](index.md#install-into-fontlab).
FontLab supplies the native modules; installing Echopy alone does not supply them.
Do not install PySide or create a second Qt application inside FontLab.

Run this outside FontLab to identify the installed distribution:

```python
# Outside FontLab
from importlib.metadata import version
import fontlab_echopy

print(version("fontlab-echopy"))
print(fontlab_echopy.__file__)
```

The package version identifies the installed declarations. It does not identify
the running FontLab build or prove that every declaration matches that build.
Keep the package version, native build and capture provenance together when
reporting a mismatch.

## Use the two import names

This check runs outside FontLab and does not construct native objects:

```python
# Outside FontLab
from echopy import fontlab as short_name
from fontlab_echopy import fontlab as long_name

assert short_name is long_name
print(short_name.__name__)
```

Inside FontLab, check native identity before relying on argument conversion or
`isinstance`. This snippet reads class objects only; it does not edit a font:

```python
# Inside FontLab; native execution required
import fontlab
from echopy import fontlab as fl

assert fl.flNode is fontlab.flNode
assert fl.flLayer is fontlab.flLayer
```

Echopy does not wrap each node or layer in a Python replacement class. Native
constructors, methods, errors and return values retain the host's behavior.
A declaration does not repair a host defect or add an unsupported overload.

## Read the full declarations offline

Small `.py` facades keep runtime imports inexpensive. Their adjacent `.pyi`
files hold the detailed declarations and docstrings. Inspecting an offline
placeholder with `inspect.signature` can show a generic signature; read the
sidecar when you need the recorded declaration.

Locate the FontLab sidecar without importing the native module:

```python
# Outside FontLab
from pathlib import Path
import fontlab_echopy

package = Path(fontlab_echopy.__file__).parent
sidecar = package / "fontlab.pyi"
assert sidecar.is_file()
print(sidecar.name)
```

Use Python's parser to extract one class and its documentation without executing
its declaration. This example prints the recorded `flNode` class:

```python
# Outside FontLab
import ast
from pathlib import Path
import fontlab_echopy

sidecar = Path(fontlab_echopy.__file__).parent / "fontlab.pyi"
source = sidecar.read_text(encoding="utf-8")
tree = ast.parse(source)
node = next(item for item in tree.body
            if isinstance(item, ast.ClassDef) and item.name == "flNode")
print(ast.get_docstring(node) or "No captured class documentation")
print(ast.get_source_segment(source, node))
```

The same approach applies to `fontgate.pyi` and `fontpr.pyi`. PythonQt declarations
use their package subdirectories. Read these files as text; do not execute them
to create native objects outside the host.

## Handle unavailable native operations

Offline imports support documentation and analysis. An attempted native operation
raises `NativeUnavailable` instead of returning a dummy object. This example
expects that refusal in a normal Python process without FontLab's native modules:

```python
# Outside FontLab
from echopy import fontlab as fl
from fontlab_echopy import NativeUnavailable

try:
    fl.flNode()
except NativeUnavailable:
    print("Run native operations inside FontLab")
else:
    raise AssertionError("This example requires an environment without FontLab")
```

Catch this exception at an application's boundary if host access is optional.
Do not catch every exception and present a failed native operation as success.
Inside FontLab, other exceptions can indicate invalid arguments or a host defect.

## Check capture provenance

Read the packaged provenance to see which capture and enrichment records produced
the declarations. The following prints its available top-level sections without
assuming that every release uses an identical metadata schema:

```python
# Outside FontLab
import json
from pathlib import Path
import fontlab_echopy

path = Path(fontlab_echopy.__file__).parent / "_provenance.json"
provenance = json.loads(path.read_text(encoding="utf-8"))
print(sorted(provenance))
```

A capture hash identifies input bytes, not complete behavioral coverage. Unknown
signatures remain explicit as `*args, **kwargs`. PySide2-derived signatures are
reference enrichment and may differ from FontLab's PythonQt bindings. Prefer a
measured call on the actual host when an overload or property is uncertain.

## Understand runtime shims

The `GlyphsApp`, `vanilla` and related shim declarations describe compatibility
modules supplied by other packages. They do not install Glyphs.app or turn an
offline process into a running Glyphs-compatible session. Glyport owns the
runtime providers used by adapted scripts.

Producer-derived shim freshness and native API fidelity are separate checks:

| Check | What it establishes |
| --- | --- |
| Regenerate shims against pinned producer files | Declarations match those producer inputs |
| Compare the generated files and provenance | The generated output is reproducible |
| Run offline tests | The tested Python behavior works outside FontLab |
| Run installed artifacts in FontLab | The exercised behavior works on that host build |

`fontlabapp_shim` has a separate App capture/generation route. Regenerating the
Glyport and Aidus shims does not refresh that capture or FontLab's native modules.

## Use PythonQt inside FontLab

FontLab's PythonQt exposes widgets through `QtGui`, not a `QtWidgets` namespace.
This native-only identity check does not create or show a widget:

```python
# Inside FontLab; native execution required
from PythonQt import QtGui as native_gui
from echopy.PythonQt import QtGui

assert QtGui.QWidget is native_gui.QWidget
```

Use the existing application and event loop. Do not construct `QApplication`,
start an application-wide `exec()`, or load another Qt runtime. For practical
panels, use the shared application helpers and retain their handles until close.
Do not probe every property on arbitrary native instances: some getters require
initialized native state and can crash the host. Class declarations and recorded
metadata are safer starting points for discovery.

## Verification boundaries

The offline examples can run in an ordinary Echopy installation. The two native
identity snippets require FontLab; compiling them is not native verification.
Neither example tests font edits, Undo/Redo, saving or reopening documents.

`fontlabpr` was absent in the recorded FontLab 9.0.9780 baseline. Treat that as a
build-specific observation, not a promise about every later release. Confirm
availability in the actual target host before designing a dependency on it.

Reference: [fontlab_echopy](../reference/fontlab_echopy.md), [fontlab](../reference/fontlab.md),
[fontgate](../reference/fontgate.md), [fontpr](../reference/fontpr.md),
[PythonQt](../reference/PythonQt.md), and [Glyport](glyport.md).
