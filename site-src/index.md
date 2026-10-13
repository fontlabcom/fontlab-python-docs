---
this_file: site-src/index.md
---

<div class="api-hero" markdown="1">

<p class="api-kicker">FontLab · Python · Qt</p>

# Python, inside FontLab.

Work with native font objects, control a running FontLab from another Python
process, and build interfaces with the application's Qt runtime.

[Connect to FontLab](guide/install.md){ .md-button .md-button--primary }
[Browse the API](reference/index.md){ .md-button }

</div>

## Start outside the application

```python
from fontlab_remopy import FontLab

with FontLab() as app:
    print(app.output())
    print(app.eval("21 * 2"))
```

## Use the native objects inside FontLab

```python
from echopy import fontlab as fl

node = fl.flNode(120, 340)
node.x = 160
```

Echopy exposes the original native objects. This reference is built off-host
from Python source captured in FontLab and enriched with typing and documentation.
Unknown signatures remain explicit; PySide2 reference signatures describe an
upstream binding and may differ from PythonQt.

## Find the right surface

| Task | API |
| --- | --- |
| Edit fonts and outlines | [fontlab](reference/fontlab.md), [fontgate](reference/fontgate.md) |
| Use native command helpers | [fontpr](reference/fontpr.md) |
| Write native Qt interfaces | [PythonQt](reference/PythonQt.md) |
| Control FontLab remotely | [Remopy](reference/fontlab_remopy.md) |
| Access panels and draw | [Fontlabapp](reference/fontlabapp.md), [Grablab](reference/grablab.md) |
| Inspect Glyphs scripts/plugins | [Glyport](reference/fontlab_glyport.md) |

Glyphs runtime/GUI adaptation and full PySide2 app compatibility are being
implemented. Their guides distinguish current behavior from planned interfaces.
