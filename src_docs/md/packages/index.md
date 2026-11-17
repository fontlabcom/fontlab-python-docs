---
this_file: src_docs/md/packages/index.md
---
# Packages

FontLab 9 runs Python 3.11 with its own PythonQt (Qt 5). These packages extend
it. [Ecosystem and package boundaries](ecosystem.md) explains which package owns
what. Each page below gives an overview, installation, a quick start, examples and
the current limits; the API reference links lead to every documented member.

| Package | Import | Use it to |
| --- | --- | --- |
| [Instamix](instamix.md) | `fontlab_instamix` | Bootstrap and install distributions, scripts and extensions |
| [Echopy](echopy.md) | `echopy`, `fontlab_echopy` | Read FontLab's native API as typed, documented Python |
| [Fly](fly.md) | `fly` | Import FontLab-related modules under short aliases |
| [Fontlabapp](fontlabapp.md) | `fontlabapp` | Drive menus, panels, preferences, windows and drawing overlays |
| [Remopy](remopy.md) | `fontlab_remopy` | Control a running FontLab from another Python process |
| [Grablab](grablab.md) | `grablab` | Capture panels, windows, menus and canvases as PNG, SVG or PDF |
| [Pythonqtside](pythonqtside.md) | `pythonqtside` | Run PySide2-style Qt code on FontLab's PythonQt |
| [Glyport](glyport.md) | `fontlab_glyport` | Run Glyphs scripts and plugins inside FontLab |
| [Fontport](fontport.md) | `fontlab_fontport` | Use FontParts, fontTools pens and ufoLib2 with FontLab fonts |
| [Pens](pens.md) | `fontlab_pens` | Draw, measure, transform and reverse outlines with the fontTools pen protocol and no dependencies |
| [TypeRig](typerig.md) | `typerig` | Use the TypeRig glyph and outline library |
| [Aidus Agentus](aidus-agentus.md) | `fontlab_aidus_agentus` | Chat with an AI agent that inspects and edits fonts in FontLab |
| [Scriptmix](scriptmix.md) | scripts | Copy practical menu tools into FontLab's Scripts folder |
| [Examples](examples.md) | scripts | Separate site with PythonQt example scripts |
| [Instamix](instamix.md) | `fontlab_instamix` | Install extensions, scripts and Python packages into FontLab |
| [Plugmix](plugmix.md) | `fontlab_plugmix` | Add reporters, filters, palettes, tools and General plugins |

## Install into FontLab

Start with [Instamix 1.0.9 or newer](instamix.md), then use the reviewed project
installer or extension manifest. It provisions uv and a matching shared Python
environment; distribution requirements can be installed from FontLab with
`fontlab_instamix.install_packages(...)`. Read [Install and connect](../guide/install.md)
for the current bootstrap, data-folder rules and GitHub release inputs.

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
(Echopy, Fly, Fontlabapp, Grablab, Remopy, Aidus Agentus, Instamix, Plugmix, Glyport, Fontport). Source
edits are live in FontLab once the package's modules are reloaded.

FontLab keeps imported modules between script runs. An install refreshes import
caches but does not reload those modules; follow the package's documented reload
or restart procedure before using a new version. Do not remove loaded binary
modules from `sys.modules` as a generic update method. Packages with
compiled extensions must match FontLab's architecture (arm64 on Apple silicon).

Install packages that run outside FontLab (Remopy, the documentation tools,
TypeRig's core) into an ordinary environment with `uv pip install PATH_TO_WHEEL`.
Private repositories require authenticated GitHub access; keep credentials in your
GitHub tooling, never in scripts or URLs.

## How this reference is built

Every API page is generated without running FontLab:

- `fontlab`, `fontgate`, `fontpr` and `PythonQt` come from Echopy's captures of the
  live host (242,654 captured identities, each one documented).
- Echopy shims only `fontlab`, `fontgate`, `fontpr`, `FL` and `PythonQt`.
  The Glyphs.app emulation modules (`GlyphsApp`, `vanilla`, `AppKit`, `Cocoa`,
  `Foundation`, `objc`) live in Glyport, FontLab's menu and panel names live in
  Fontlabapp, and the Aidus tools belong to Aidus Agentus. Each is documented from
  its own package source.
- The packages above are read from their source, never imported, so code that
  needs FontLab still documents completely. The build fails when any package
  renders no members or no documentation.
