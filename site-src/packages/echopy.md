---
this_file: site-src/packages/echopy.md
---
# Echopy

Echopy gives FontLab's native API (`fontlab`, `fontgate`, `fontpr`, `PythonQt`) a
readable Python source form: classes, signatures, types and documentation that
editors, type checkers and this site can read. At run time it hands you the
original native objects, so nothing changes in behaviour.

This page describes Echopy v0.2.3.

## Install

Install the `fontlab-echopy` wheel into FontLab's Python folder (see
[Install into FontLab](index.md#install-into-fontlab)). Both import names,
`echopy` and `fontlab_echopy`, refer to the same modules.

## Quick start

```python
# Inside FontLab
from echopy import fontlab as fl, fontgate as fg, fontpr

node = fl.flNode(12, 34)        # the original native flNode
assert fl.flNode is __import__("fontlab").flNode
```

Outside FontLab the same imports load the declarations for documentation and
type checking; calling a native function or constructing a native class raises
`NativeUnavailable`.

## Examples

Inspect a declaration without FontLab:

```python
import inspect
from echopy import fontlab as fl

print(inspect.signature(fl.flNode.__init__))
```

Static shims describe modules that exist only at run time, for example the
`GlyphsApp` module Glyport builds for each Glyphs script:

```python
from fontlab_echopy import GlyphsApp   # declarations only; see GlyphsApp reference
```

## How it works and limits

- Small `.py` facades bind native symbols; full declarations live in `.pyi`
  sidecars, which keeps imports inside FontLab's five-second script deadline.
- Unknown native signatures stay explicit as `*args, **kwargs`; PySide2 reference
  signatures are labelled as upstream and may differ from PythonQt.
- `fontlabpr` is absent from FontLab 9.0.9780 and documented as absent.

Reference: [fontlab_echopy](../reference/fontlab_echopy.md), and the native
[fontlab](../reference/fontlab.md), [fontgate](../reference/fontgate.md),
[fontpr](../reference/fontpr.md) and [PythonQt](../reference/PythonQt.md) pages.
