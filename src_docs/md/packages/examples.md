---
this_file: src_docs/md/packages/examples.md
---
# Examples

The Python examples (`fontlab-python-examples`) are one hundred menu scripts that
show useful Python and PythonQt workflows in FontLab 9: inspecting fonts, building
proofs, editing selected data and showing modeless panels. Each script states its
setup, scope and limits, and some change fonts, so read its Usage and Setup text
before you run it.

Like [Scriptmix](scriptmix.md), this is a script collection, not a runtime
package. The runtime code for the original Models, Forms and GetGo menus lives in
a separate package, `fontlab-python-lessons`, inside the repository.

## Install

1. Use FontLab 9 with its embedded Python 3.11 (arm64).
2. Install `fontlab-fly`, `fontlab-fontlabapp` and `fontlab-python-lessons` into
   FontLab's Python folder; see [Install into FontLab](index.md#install-into-fontlab).
   Add the Lessons `fonttools` extra for the pen and export lessons.
3. Copy the category folders from the repository's `Scripts/` folder into a FontLab
   Scripts location, keeping the one-level `Scripts/<Category>/<Tool>.py` layout.
4. Open an owned copy of a font and run a menu from its category.

Never start a second `QApplication` or install another Qt binding in FontLab.

## Examples

- **Tools > Kerning Copy Rules** turns `A|V A|W = T|o @ -5` into pairs, shows a
  preview, and applies them as one Undo step.
- **Contours > Node Table** lists the current layer's nodes and edits X and Y.
- **Dialogs > Glyph Batch Recipe Settings** builds a recipe that Glyph Proof Batch
  Wizard turns into proof text.

## Where the examples appear in this site

The [Examples](../examples/index.md) section of this site is generated from the
repository's retained catalogue. For the full menu map and status, see the
repository's README.
