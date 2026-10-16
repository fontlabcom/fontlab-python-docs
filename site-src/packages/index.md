---
this_file: site-src/packages/index.md
---
# Packages

FontLab 9 runs Python 3.11 with its own PythonQt (Qt 5). These packages extend
it. Each page below gives an overview, installation, a quick start, examples and
the current limits; the API reference links lead to every documented member.

| Package | Import | Use it to |
| --- | --- | --- |
| [Echopy](echopy.md) | `echopy`, `fontlab_echopy` | Read FontLab's native API as typed, documented Python |
| [Fly](fly.md) | `fly` | Import FontLab-related modules under short aliases |
| [Fontlabapp](fontlabapp.md) | `fontlabapp` | Drive menus, panels, preferences, windows and drawing overlays |
| [Remopy](remopy.md) | `fontlab_remopy` | Control a running FontLab from another Python process |
| [Grablab](grablab.md) | `grablab` | Capture panels, windows, menus and canvases as PNG, SVG or PDF |
| [Pythonqtside](pythonqtside.md) | `pythonqtside` | Run PySide2-style Qt code on FontLab's PythonQt |
| [Glyport](glyport.md) | `fontlab_glyport` | Run Glyphs scripts and plugins inside FontLab |
| [Fontport](fontport.md) | `fontlab_fontport` | Use FontParts, fontTools pens and ufoLib2 with FontLab fonts |
| [TypeRig](typerig.md) | `typerig` | Use the TypeRig glyph and outline library |
| [Aidus Code](aidus-code.md) | `fontlab_aidus_code` | Chat with an AI agent that inspects and edits fonts in FontLab |

## Install into FontLab

Download a reviewed wheel from the package's GitHub release, then install it
into FontLab 9's per-user Python folder with a Python 3.11 resolver:

```sh
uv pip install --python 3.11 \
  --target "$HOME/Library/Application Support/FontLab/FontLab 9/python/3.11/site-packages" \
  PATH_TO_WHEEL
```

### Editable install from a checkout

To work on a package, install its Git checkout in editable mode into FontLab's
per-user Python environment. When that folder is the `site-packages` of a virtual
environment (for example a link into `FontLab 9/.venv`), point `--python` at that
environment's interpreter; `--link-mode=copy` copies files from uv's cache instead
of linking them:

```sh
FL_PY="$HOME/Library/Application Support/FontLab/FontLab 9/.venv/bin/python"
uv pip install --python "$FL_PY" --link-mode=copy -e path/to/fontlab-glyport
uv pip install --python "$FL_PY" --link-mode=copy -e path/to/fontlab-fontport
```

Repeat for each checkout you develop
(Echopy, Fly, Fontlabapp, Grablab, Remopy, Aidus Code, Glyport, Fontport). Source
edits are live in FontLab once the package's modules are reloaded.

Restart FontLab, or remove the package's modules from `sys.modules`, to load a
new version: FontLab keeps imported modules between script runs. Packages with
compiled extensions must match FontLab's architecture (arm64 on Apple silicon).

Install packages that run outside FontLab (Remopy, the documentation tools,
TypeRig's core) into an ordinary environment with `uv pip install PATH_TO_WHEEL`.
Private repositories require authenticated GitHub access; keep credentials in your
GitHub tooling, never in scripts or URLs.

## How this reference is built

Every API page is generated without running FontLab:

- `fontlab`, `fontgate`, `fontpr` and `PythonQt` come from Echopy's captures of the
  live host (242,654 captured identities, each one documented).
- Modules that exist only while a Glyphs script runs (`GlyphsApp`, `vanilla`,
  `AppKit`, `Cocoa`, `Foundation`, `objc`), FontLab's menus and panels
  (`fontlabapp_shim`) and the Aidus tools (`aidus_code_tools`) come from Echopy
  shims generated from the providers FontLab scripts actually receive.
- The packages above are read from their source, never imported, so code that
  needs FontLab still documents completely. The build fails when any package
  renders no members or no documentation.
