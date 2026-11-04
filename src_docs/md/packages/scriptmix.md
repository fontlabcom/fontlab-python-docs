---
this_file: src_docs/md/packages/scriptmix.md
---
# Scriptmix

Scriptmix (`fontlab-python-scriptmix`) is a menu collection of practical tools for
FontLab 9: metrics, names and anchors editors, component writers, master
navigation and layer copying, contour editing, kerning editors, proof texts,
reports and drawing panels. The tools inspect, proof and edit fonts through
FontLab's native APIs, PythonQt and Fontlabapp helpers.

Scriptmix is not an installable Python package. It is a set of scripts you copy
into FontLab; its `pyproject.toml` only configures documentation tools.

## Install

1. Install matching `fontlab-fly`, `fontlab-fontlabapp` and `fontlab-fontport` into
   FontLab's Python folder; see [Install into FontLab](index.md#install-into-fontlab).
   Some tools also need `fontTools`, and Glyphs-specific tools use Glyport.
2. Open FontLab's Scripts folder from the application.
3. Copy the category folders from the repository's `Scripts/` folder into it. Keep
   the layout `Scripts/<Category>/<Tool>.py`; FontLab accepts one category level.
4. Open a copy of a font, select the glyphs and master, and choose the tool from
   the Script menu. Each tool's docstring states its controls, scopes and refusals.

## Categories

Metrics, Names, Anchors, Components, Masters, Contours, Features, Font Info,
Guides, Kerning, Cleanup, Proof, Reports and Utilities. Each is a folder under
`Scripts/`.

## Examples

- **Metrics > Scale Advances** scales selected advances by a percentage, with a
  preview, keeping outlines centred.
- **Masters > Duplicate Current Layer** backs up the current master or all masters.
- **Names > Duplicate Unicodes** scans the font and lets you choose assignments to
  keep or remove.
- **Proof > Text Filter** simplifies proof text with persistent input and regex
  fields.

## Limits

Source tests do not establish correct Undo/Redo, saved font state or panel
lifetime inside FontLab; native acceptance is tracked separately in the
repository. Work on owned copies of fonts.

See the repository's README and porting backlog for the full tool list and
status. Where a task needs an interface or helper you write yourself, build it on
[Fontlabapp](fontlabapp.md).
