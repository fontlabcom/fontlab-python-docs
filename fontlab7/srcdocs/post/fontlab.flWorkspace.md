## Example

```python
import os.path
# Access the font-specific logic of FontLab 7 with
# the `fontlab` package
from fontlab import *
# Access the entire Qt application framework that powers
# FontLab 7 with the `PythonQt` package
# `PythonQt.QtGui` exposes the full Qt GUI toolkit to build
# simple and most complex UIs
from PythonQt import QtGui

# Checks if a `.vfc` file with the same file name as this
# script file exists in the same folder
loc = [os.path.dirname(__file__)] +     list(os.path.splitext(os.path.basename(__file__)))
fontPath = os.path.join(loc[0], loc[1] + '.vfc')
# If there is no such file, opens a file open dialog with
# `QtGui.QFileDialog`, so you can pick a font file or Cancel
if not os.path.exists(fontPath):
    fontPath = QtGui.QFileDialog.getOpenFileName(
        None, 'Choose font', loc[0], '')

# If there is a font file, export its instances as OTF
if fontPath:
    # `fontlab.flWorkspace` instance is the FontLab 7 app
    # seen as the font editor
    ws = flWorkspace.instance()
    # `.mainWindow` is the graphical interface of FontLab 7
    main = ws.mainWindow

    # `.loadFont` opens a file in the FontLab GUI
    main.loadFont(fontPath)

    # `.currentPackage` is the active `fontlab.flPackage`,
    # which is a font inside FontLab
    fp = ws.currentPackage

    # `fontlab.flPreferences` has the FL7 preferences
    # that hold numeric constants that represent values
    # in the Export Font As dialog settings
    pref = flPreferences()

    # New `fontlab.ExportControl` class corresponds to
    # the settings of File > Export Font As...
    ec = ExportControl()
    ec.profileName = "OpenType PS"
    ec.destinationMode = pref.DestinationFolder
    ec.conflictMode = pref.ConflictOverwrite
    ec.contentMode = pref.ContentInstances
    ec.destinationFolder = os.path.dirname(fontPath)
    ec.groupProfiles = False
    ec.groupFamily = True

    # `flWorkspace.exportFont` exports the `flPackage`
    # with `ExportControl` settings
    ws.exportFont(fp, ec)

# `QtGui.QApplication` instance is the FontLab 7 app
# seen as a graphical app that uses the Qt framework
qapp = QtGui.QApplication.instance()
# Quit the FontLab 7 app
qapp.quit()
```