

<a name="typerig.proxy.objects.glyph"></a>

# `typerig.proxy.objects.glyph`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.glyph (<span class="info">version 0.26.9)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Glyph
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li><li>PythonQt</li><li>fontTools.pens.statisticsPen</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.glyph.html#eGlyph">eGlyph</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eGlyph" href="#eGlyph">class <span class="class-name">eGlyph</span></a>(<a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Glyph, adding some advanced functionality

Constructor:
        pGlyph() - default represents the current glyph and current font
        pGlyph(fgFont, fgGlyph)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.glyph.html#eGlyph">eGlyph</a></dd><dd><a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eGlyph-bindCompMetrics" href="#eGlyph-bindCompMetrics"><span class="function-name">bindCompMetrics</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, bindIndex<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Auto bind metrics to the base composite glyph or to specified shape index</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-blendLayers" href="#eGlyph-blendLayers"><span class="function-name">blendLayers</span></a><span class="argspec">(self, layerA, layerB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two layers at given times (anisotropic support).
Args:
        layerA (flLayer), layerB (flLayer): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-breakContour" href="#eGlyph-breakContour"><span class="function-name">breakContour</span></a><span class="argspec">(self, contourId, nodeId, layer<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and layer. Extrapolate line endings if needed.
Args:
        contourId (int): Contour Index
        nodeId (int): Node Index
        layer (int or str): Layer index or name, works with both
        expand (float): Will extrapolate the line endings at that given value

Returns:
        flContour</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyADVbyName" href="#eGlyph-copyADVbyName"><span class="function-name">copyADVbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy Advance width from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyLSBbyName" href="#eGlyph-copyLSBbyName"><span class="function-name">copyLSBbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyMetricsbyName" href="#eGlyph-copyMetricsbyName"><span class="function-name">copyMetricsbyName</span></a><span class="argspec">(self, metricTriple<span class="parameter-default">=(None, None, None)</span>, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=(0, 0, 0)</span>, adjustPercent<span class="parameter-default">=(100, 100, 100)</span>, adjustUnits<span class="parameter-default">=(0, 0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB, RSB and Advance width from glyphs specified by Glyph Name.

Args:
        metricTriple tuple(str): Names of source glyphs for (LSB, RSB, ADV)
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order tuple(bool): Use source LSB (0 False) or RSB (1 True). Flips the metric copied. (LSB, RSB, 0)
        adjustPercent tuple(int): Adjust the copied metric by percent (100 default) - (LSB, RSB, ADV)
        adjustUnits tuple(int): Adjust the copied metric by units (0 default) - (LSB, RSB, ADV)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyRSBbyName" href="#eGlyph-copyRSBbyName"><span class="function-name">copyRSBbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy RSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dropAnchor" href="#eGlyph-dropAnchor"><span class="function-name">dropAnchor</span></a><span class="argspec">(self, name, layer, coordTuple, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Drop anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dropGuide" href="#eGlyph-dropGuide"><span class="function-name">dropGuide</span></a><span class="argspec">(self, nodes<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, name<span class="parameter-default">='*DropGuideline'</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, flip<span class="parameter-default">=(1, 1)</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Build guideline trough *any two* given points or the *first two of the current selection*.

If *single point* is given will create a vertical guideline trough that point,
with guideline inclined according to the font's Italic Angle.

if process layers (pLayers) is None guideline will be created in all compatible layers,
otherwise the bool control tuple (active_layer (True or False), masters (True or False), masks (True or False), services (True or False)) is used. 
If all are set to False only the active layer is used.

Args:
        nodes (list(int)): List of node indexes
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        name (str): Name of the guideline to be build
        color (str): Color of the guideline according to QtCore colors
        style (str): Style of the guideline according to FontLab 6

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getAttachmentCenters" href="#eGlyph-getAttachmentCenters"><span class="function-name">getAttachmentCenters</span></a><span class="argspec">(self, layer, tolerance<span class="parameter-default">=5</span>, applyTransform<span class="parameter-default">=True</span>, getAll<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return X center of lowest, highest Y of [glyph] for [layer] within given [tolerance]
Note: Determine diacritic to glyph attachment positions (for anchor placement)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getNewBaseCoords" href="#eGlyph-getNewBaseCoords"><span class="function-name">getNewBaseCoords</span></a><span class="argspec">(self, layer, adjustTuple, alignTuple, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>, initPosTuple<span class="parameter-default">=(0.0, 0.0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Calculate Anchor base position
Args:
        layer (int or str): Layer index or name, works with both
        coordTuple (int/float, int/float): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int/float): Outline feature auto detection tolerance*
        initPosTuple (int/float, int/float): Itinital anchor position

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        x, y (int/float)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-lerpLayerFg" href="#eGlyph-lerpLayerFg"><span class="function-name">lerpLayerFg</span></a><span class="argspec">(self, l0_Name, l1_Name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-moveAnchor" href="#eGlyph-moveAnchor"><span class="function-name">moveAnchor</span></a><span class="argspec">(self, name, layer, coordTuple<span class="parameter-default">=(0, 0)</span>, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Move anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-reorder_shapes" href="#eGlyph-reorder_shapes"><span class="function-name">reorder_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mode<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Auto reorder shapes on given layer using criteria.
Args:
        layer (int or str): Layer index or name, works with both
        mode (bool, bool): Mode of shape reordering/sorting by (X, Y)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setStart" href="#eGlyph-setStart"><span class="function-name">setStart</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, control<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-splitContour" href="#eGlyph-splitContour"><span class="function-name">splitContour</span></a><span class="argspec">(self, scnPairs<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>, close<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and combinations of compatible layers. Extrapolate line endings and close contour if needed.

Args:
        scnPairs (list(tuple)): Shape-contour-node pairs for the selected nodes [(Shape Index, Contour Index, Node Index)..()]
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        expand (float): Will extrapolate the line endings at that given value
        close (bool): True = Close contour 

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-ungroup_all_shapes" href="#eGlyph-ungroup_all_shapes"><span class="function-name">ungroup_all_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, applyTransform<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Ungroup all shapes at given layer.
Args:
        layer (int or str): Layer index or name, works with both
        applyTransform (bool): Apply transformation at shape.

Returns:
        None</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></h4><dl class="function"><dt><a name="eGlyph-__init__" href="#eGlyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-__repr__" href="#eGlyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-activeGuides" href="#eGlyph-activeGuides"><span class="function-name">activeGuides</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-activeLayer" href="#eGlyph-activeLayer"><span class="function-name">activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addAnchor" href="#eGlyph-addAnchor"><span class="function-name">addAnchor</span></a><span class="argspec">(self, coordTuple, name, layer<span class="parameter-default">=None</span>, isAnchor<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Anchor at given layer.
Args:
        coordTuple (tuple(float,float)): Anchor coordinates X, Y
        name (str): Anchor name
        layer (int or str): Layer index or name. If None returns ActiveLayer
        isAnchor (bool): True creates a true flAnchor, False ? (flPinPoint)
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addComponents" href="#eGlyph-addComponents"><span class="function-name">addComponents</span></a><span class="argspec">(self, componentConfig, layer<span class="parameter-default">=None</span>, useAnchors<span class="parameter-default">=True</span>, colorize<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a components to given glyph layer.
Args:
        componentConfig (list(tuple(glyph_name (str), glyph_transform (QTransform), layer_pointer (str)))): List contianign component configuration.  
        layer (int or str): Layer index or name. If None returns ActiveLayer
        useAnchors (bool): Compose using anchors
        colorize (bool): Flag new glyphs
Returns:
        list(flShapes): List of components added</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addGuideline" href="#eGlyph-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, coordTuple, layer<span class="parameter-default">=None</span>, angle<span class="parameter-default">=0</span>, name<span class="parameter-default">=''</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Guideline at given layer
Args:
        coordTuple (tuple(float,float) or tuple(float,float,float,float)): Guideline coordinates X, Y and given angle or two node reference x1,y1 and x2,y2
        name (str): Anchor name
        angle (float): Incline of the guideline
        layer (int or str): Layer index or name. If None returns ActiveLayer                    
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addLayer" href="#eGlyph-addLayer"><span class="function-name">addLayer</span></a><span class="argspec">(self, layer, toBack<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a layer to glyph.
Args:
        layer (flLayer or fgLayer)
        toBack (bool): Send layer to back
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addShape" href="#eGlyph-addShape"><span class="function-name">addShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, clone<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape at given layer.
Args:
        shape (flShape): Shape to be added
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addShapeContainer" href="#eGlyph-addShapeContainer"><span class="function-name">addShapeContainer</span></a><span class="argspec">(self, shapeList, layer<span class="parameter-default">=None</span>, remove<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape container* at given layer.
A flShape containing all of the shapes given that
could be transformed to Shape-group or shape-filter.
Args:
        shapeList list(flShape): List if Shapes to be grouped.
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-anchors" href="#eGlyph-anchors"><span class="function-name">anchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of anchors (list[flAnchor]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-blendShapes" href="#eGlyph-blendShapes"><span class="function-name">blendShapes</span></a><span class="argspec">(self, shapeA, shapeB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two shapes at given times (anisotropic support).
Args:
        shapeA (flShape), shapeB (flShape): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        Native (interpolation engine dependent) or flShape (default)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-clearAnchors" href="#eGlyph-clearAnchors"><span class="function-name">clearAnchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all anchors at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-components" href="#eGlyph-components"><span class="function-name">components</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph components besides glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-containers" href="#eGlyph-containers"><span class="function-name">containers</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-contours" href="#eGlyph-contours"><span class="function-name">contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=True</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyLayer" href="#eGlyph-copyLayer"><span class="function-name">copyLayer</span></a><span class="argspec">(self, srcLayerName, dstLayerName, options<span class="parameter-default">={'adv': True, 'anc': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True}</span>, addLayer<span class="parameter-default">=False</span>, cleanDST<span class="parameter-default">=True</span>, toBack<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copies a layer within the glyph.
Args:
        srcLayerName, dstLayerName (string): Source and destination layer names
        options (dict): Copy Options as follows {'out': Outline, 'gui': Guidelines, 'anc': Anchors, 'lsb': LSB, 'adv': Advance, 'rsb': RSB, 'lnk': Linked metrics, 'ref': References}, addLayer=False):
        addLayer (bool): Create a new layer
        cleanDST (bool): Clean destination layer
        toBack (bool): Add layer to back of the layer stack
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-decompose" href="#eGlyph-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decompose all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dereference" href="#eGlyph-dereference"><span class="function-name">dereference</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all shape references but leave components.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-draw" href="#eGlyph-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-drawPoints" href="#eGlyph-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the PointPen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-duplicateLayer" href="#eGlyph-duplicateLayer"><span class="function-name">duplicateLayer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, newLayerName<span class="parameter-default">='New Layer'</span>, references<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a layer with new name and adds it to glyph's layers.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        toBack(bool): send to back
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-elements" href="#eGlyph-elements"><span class="function-name">elements</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph elements in glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_activeLayer" href="#eGlyph-fg_activeLayer"><span class="function-name">fg_activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_contours" href="#eGlyph-fg_contours"><span class="function-name">fg_contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_hasLayer" href="#eGlyph-fg_hasLayer"><span class="function-name">fg_hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_layer" href="#eGlyph-fg_layer"><span class="function-name">fg_layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns FontGate layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        fgLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_layers" href="#eGlyph-fg_layers"><span class="function-name">fg_layers</span></a><span class="argspec">(self, asDict<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FotnGate layers</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_nodes" href="#eGlyph-fg_nodes"><span class="function-name">fg_nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_shapes" href="#eGlyph-fg_shapes"><span class="function-name">fg_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findAnchor" href="#eGlyph-findAnchor"><span class="function-name">findAnchor</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findAnchorCoords" href="#eGlyph-findAnchorCoords"><span class="function-name">findAnchorCoords</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findNode" href="#eGlyph-findNode"><span class="function-name">findNode</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findNodeCoords" href="#eGlyph-findNodeCoords"><span class="function-name">findNodeCoords</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findShape" href="#eGlyph-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds shape by name on given layer
Args:
        shapeName (str): Shape name
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flShape or None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fontMetricsInfo" href="#eGlyph-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (<a href="./__builtin__.html#object">object</a>)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getAdvance" href="#eGlyph-getAdvance"><span class="function-name">getAdvance</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Advance Width at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getBounds" href="#eGlyph-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Glyph's Boundig Box at given layer (int or str). Returns QRectF.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getBuilders" href="#eGlyph-getBuilders"><span class="function-name">getBuilders</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, store<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getCompositionDict" href="#eGlyph-getCompositionDict"><span class="function-name">getCompositionDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return composition dict of a glyph. Elements!</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getCompositionNames" href="#eGlyph-getCompositionNames"><span class="function-name">getCompositionNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return name of glyph and the parts it is made of.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getElementNames" href="#eGlyph-getElementNames"><span class="function-name">getElementNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return names of elements references used in glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getLSB" href="#eGlyph-getLSB"><span class="function-name">getLSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Left Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getRSB" href="#eGlyph-getRSB"><span class="function-name">getRSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Right Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getSBeq" href="#eGlyph-getSBeq"><span class="function-name">getSBeq</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">GET LSB, RSB metric equations on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getSegment" href="#eGlyph-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns contour segment of the node specified at given layer
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        CurveEx</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getTags" href="#eGlyph-getTags"><span class="function-name">getTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Tags -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-guidelines" href="#eGlyph-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of guidelines (list[flGuideline]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-hasLayer" href="#eGlyph-hasLayer"><span class="function-name">hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-insertNodeAt" href="#eGlyph-insertNodeAt"><span class="function-name">insertNodeAt</span></a><span class="argspec">(self, cID, nID_time, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts node in contour at specified layer
Arg:
        cID (int): Contour Index
        nID_time (float): Node index + float time
        layer (int or str): Layer index or name. If None returns ActiveLayer

!NOTE: FL6 treats contour insertions (as well as nodes) as float times along contour,
so inserting a node at .5 t between nodes with indexes 3 and 4 will be 3 (index) + 0.5 (time) = 3.5</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-insertNodesAt" href="#eGlyph-insertNodesAt"><span class="function-name">insertNodesAt</span></a><span class="argspec">(self, cID, nID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts a list of nodes to specified contour, starting at given index all on layer specified.
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-isCompatible" href="#eGlyph-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph is ready for interpolation - all master layers are compatible.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-isMixedReference" href="#eGlyph-isMixedReference"><span class="function-name">isMixedReference</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph has mixed references - components on some layers and referenced shapes on others</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-italicAngle" href="#eGlyph-italicAngle"><span class="function-name">italicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-layer" href="#eGlyph-layer"><span class="function-name">layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-layers" href="#eGlyph-layers"><span class="function-name">layers</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return all layers</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mLine" href="#eGlyph-mLine"><span class="function-name">mLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mapNodes2Times" href="#eGlyph-mapNodes2Times"><span class="function-name">mapNodes2Times</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Nodes at contour times for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Contour Time (int): Node Index (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mapTimes2Nodes" href="#eGlyph-mapTimes2Nodes"><span class="function-name">mapTimes2Nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Contour times at node indexes for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Node Index (int) : Contour Time (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mask" href="#eGlyph-mask"><span class="function-name">mask</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-masks" href="#eGlyph-masks"><span class="function-name">masks</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all mask layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-masters" href="#eGlyph-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all master layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-newAnchor" href="#eGlyph-newAnchor"><span class="function-name">newAnchor</span></a><span class="argspec">(self, coordTuple, name, anchorType<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Not working</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodes" href="#eGlyph-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer.
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodes4segments" href="#eGlyph-nodes4segments"><span class="function-name">nodes4segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments and their corresponding nodes at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        dict{time(int):(CurveEx, list[flNode]}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodesForIndices" href="#eGlyph-nodesForIndices"><span class="function-name">nodesForIndices</span></a><span class="argspec">(self, indices, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-noncomplex" href="#eGlyph-noncomplex"><span class="function-name">noncomplex</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph shapes that are not glyph references or components</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-object" href="#eGlyph-object"><span class="function-name">object</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeLayer" href="#eGlyph-removeLayer"><span class="function-name">removeLayer</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Removes a layer from glyph.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeNodeAt" href="#eGlyph-removeNodeAt"><span class="function-name">removeNodeAt</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a node from contour at layer specified.
Args:
        cID (int): Contour index
        nID (int): Index of Node to be removed
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeNodes" href="#eGlyph-removeNodes"><span class="function-name">removeNodes</span></a><span class="argspec">(self, cID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a list of nodes from contour at layer specified.
Args:
        cID (int): Contour index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeShape" href="#eGlyph-removeShape"><span class="function-name">removeShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, recursive<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a new shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
        recursive (bool): 
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-replaceShape" href="#eGlyph-replaceShape"><span class="function-name">replaceShape</span></a><span class="argspec">(self, old_shape, new_shape, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Repalce a shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-reportLayerComp" href="#eGlyph-reportLayerComp"><span class="function-name">reportLayerComp</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns a layer compatibility report</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-rotate" href="#eGlyph-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rotate outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-scale" href="#eGlyph-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Scale outline at given layer.
Args:
        sx (float), sy (float): delta (scaling) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-segments" href="#eGlyph-segments"><span class="function-name">segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selected" href="#eGlyph-selected"><span class="function-name">selected</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes indexes at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedAtContours" href="#eGlyph-selectedAtContours"><span class="function-name">selectedAtContours</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the contours they rest upon at current layer.
Args:
        index (bool): If True returns only indexes, False returns flContour, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(contourID, nodeID)..()] or 
        list[tuple(flContour, flNode)]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedAtShapes" href="#eGlyph-selectedAtShapes"><span class="function-name">selectedAtShapes</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, filterOn<span class="parameter-default">=False</span>, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the shapes they belong at current layer.
Args:
        index (bool): If True returns only indexes, False returns flShape, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(shapeID, nodeID)..()] or
        list[tuple(flShape, flNode)]

!TODO: Make it working with layers as <a href="#eGlyph-selectedAtContours">selectedAtContours</a>(). This is legacy mode so other scripts would work!</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedContours" href="#eGlyph-selectedContours"><span class="function-name">selectedContours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, allNodesSelected<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedCoords" href="#eGlyph-selectedCoords"><span class="function-name">selectedCoords</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, applyTransform<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the coordinates of all selected nodes at the current layer or other.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        filterOn (bool): Return only on-curve nodes
        applyTransform (bool) : Gets local shape transformation matrix and applies it to the node coordinates
Returns:
        list[QPointF]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodeIndices" href="#eGlyph-selectedNodeIndices"><span class="function-name">selectedNodeIndices</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodes" href="#eGlyph-selectedNodes"><span class="function-name">selectedNodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes at given layer.
Args:
        filterOn (bool): Return only on-curve nodes
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNode]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodesOnCanvas" href="#eGlyph-selectedNodesOnCanvas"><span class="function-name">selectedNodesOnCanvas</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Glyph Selection -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedSegments" href="#eGlyph-selectedSegments"><span class="function-name">selectedSegments</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns list of currently selected segments
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedShapeIndices" href="#eGlyph-selectedShapeIndices"><span class="function-name">selectedShapeIndices</span></a><span class="argspec">(self, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        select_all (bool): True all nodes on Shape should be selected. False any node will do.
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedShapes" href="#eGlyph-selectedShapes"><span class="function-name">selectedShapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes that have a node selected.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-services" href="#eGlyph-services"><span class="function-name">services</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all service layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setADVeq" href="#eGlyph-setADVeq"><span class="function-name">setADVeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set Advance width metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setAdvance" href="#eGlyph-setAdvance"><span class="function-name">setAdvance</span></a><span class="argspec">(self, newAdvance, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Advance Width (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setLSB" href="#eGlyph-setLSB"><span class="function-name">setLSB</span></a><span class="argspec">(self, newLSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Left Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setLSBeq" href="#eGlyph-setLSBeq"><span class="function-name">setLSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set LSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setMark" href="#eGlyph-setMark"><span class="function-name">setMark</span></a><span class="argspec">(self, mark_color, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setName" href="#eGlyph-setName"><span class="function-name">setName</span></a><span class="argspec">(self, glyph_name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setRSB" href="#eGlyph-setRSB"><span class="function-name">setRSB</span></a><span class="argspec">(self, newRSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Right Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setRSBeq" href="#eGlyph-setRSBeq"><span class="function-name">setRSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set RSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setTags" href="#eGlyph-setTags"><span class="function-name">setTags</span></a><span class="argspec">(self, tagList, append<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-shapes" href="#eGlyph-shapes"><span class="function-name">shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-shapes_data" href="#eGlyph-shapes_data"><span class="function-name">shapes_data</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all flShapeData objects at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapeData]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-slant" href="#eGlyph-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Slant outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-tag" href="#eGlyph-tag"><span class="function-name">tag</span></a><span class="argspec">(self, newTag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-translate" href="#eGlyph-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Translate (shift) outline at given layer.
Args:
        dx (float), dy (float): delta (shift) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-update" href="#eGlyph-update"><span class="function-name">update</span></a><span class="argspec">(self, fl<span class="parameter-default">=True</span>, fg<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates the glyph and sends notification to the editor.
Args:
        fl (bool): Update the flGlyph
        fg (bool): Update the fgGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-updateObject" href="#eGlyph-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-version" href="#eGlyph-version"><span class="function-name">version</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
</dl>
<dl class="descriptor"><dt>index</dt>
</dl>
<dl class="descriptor"><dt>mark</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>package</dt>
</dl>
<dl class="descriptor"><dt>tags</dt>
</dl>
<dl class="descriptor"><dt>unicode</dt>
</dl>
<dl class="descriptor"><dt>unicodes</dt>
</dl>
</dd>
<dt class="class"><h2><a name="pGlyph" href="#pGlyph">class <span class="class-name">pGlyph</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flGlyph and fgGlyph combined into single entity.

Constructor:
        pGlyph() : default represents the current glyph and current font
        pGlyph(flGlyph)
        pGlyph(fgFont, fgGlyph)

Methods:

Attributes:
        .parent (fgFont)
        .fg (fgGlyph)
        .fl (flGlyph)
        ...</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pGlyph-__init__" href="#pGlyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-__repr__" href="#pGlyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-activeGuides" href="#pGlyph-activeGuides"><span class="function-name">activeGuides</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-activeLayer" href="#pGlyph-activeLayer"><span class="function-name">activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addAnchor" href="#pGlyph-addAnchor"><span class="function-name">addAnchor</span></a><span class="argspec">(self, coordTuple, name, layer<span class="parameter-default">=None</span>, isAnchor<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Anchor at given layer.
Args:
        coordTuple (tuple(float,float)): Anchor coordinates X, Y
        name (str): Anchor name
        layer (int or str): Layer index or name. If None returns ActiveLayer
        isAnchor (bool): True creates a true flAnchor, False ? (flPinPoint)
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addComponents" href="#pGlyph-addComponents"><span class="function-name">addComponents</span></a><span class="argspec">(self, componentConfig, layer<span class="parameter-default">=None</span>, useAnchors<span class="parameter-default">=True</span>, colorize<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a components to given glyph layer.
Args:
        componentConfig (list(tuple(glyph_name (str), glyph_transform (QTransform), layer_pointer (str)))): List contianign component configuration.  
        layer (int or str): Layer index or name. If None returns ActiveLayer
        useAnchors (bool): Compose using anchors
        colorize (bool): Flag new glyphs
Returns:
        list(flShapes): List of components added</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addGuideline" href="#pGlyph-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, coordTuple, layer<span class="parameter-default">=None</span>, angle<span class="parameter-default">=0</span>, name<span class="parameter-default">=''</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Guideline at given layer
Args:
        coordTuple (tuple(float,float) or tuple(float,float,float,float)): Guideline coordinates X, Y and given angle or two node reference x1,y1 and x2,y2
        name (str): Anchor name
        angle (float): Incline of the guideline
        layer (int or str): Layer index or name. If None returns ActiveLayer                    
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addLayer" href="#pGlyph-addLayer"><span class="function-name">addLayer</span></a><span class="argspec">(self, layer, toBack<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a layer to glyph.
Args:
        layer (flLayer or fgLayer)
        toBack (bool): Send layer to back
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addShape" href="#pGlyph-addShape"><span class="function-name">addShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, clone<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape at given layer.
Args:
        shape (flShape): Shape to be added
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addShapeContainer" href="#pGlyph-addShapeContainer"><span class="function-name">addShapeContainer</span></a><span class="argspec">(self, shapeList, layer<span class="parameter-default">=None</span>, remove<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape container* at given layer.
A flShape containing all of the shapes given that
could be transformed to Shape-group or shape-filter.
Args:
        shapeList list(flShape): List if Shapes to be grouped.
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-anchors" href="#pGlyph-anchors"><span class="function-name">anchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of anchors (list[flAnchor]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-blendShapes" href="#pGlyph-blendShapes"><span class="function-name">blendShapes</span></a><span class="argspec">(self, shapeA, shapeB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two shapes at given times (anisotropic support).
Args:
        shapeA (flShape), shapeB (flShape): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        Native (interpolation engine dependent) or flShape (default)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-clearAnchors" href="#pGlyph-clearAnchors"><span class="function-name">clearAnchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all anchors at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-components" href="#pGlyph-components"><span class="function-name">components</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph components besides glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-containers" href="#pGlyph-containers"><span class="function-name">containers</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-contours" href="#pGlyph-contours"><span class="function-name">contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=True</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-copyLayer" href="#pGlyph-copyLayer"><span class="function-name">copyLayer</span></a><span class="argspec">(self, srcLayerName, dstLayerName, options<span class="parameter-default">={'adv': True, 'anc': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True}</span>, addLayer<span class="parameter-default">=False</span>, cleanDST<span class="parameter-default">=True</span>, toBack<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copies a layer within the glyph.
Args:
        srcLayerName, dstLayerName (string): Source and destination layer names
        options (dict): Copy Options as follows {'out': Outline, 'gui': Guidelines, 'anc': Anchors, 'lsb': LSB, 'adv': Advance, 'rsb': RSB, 'lnk': Linked metrics, 'ref': References}, addLayer=False):
        addLayer (bool): Create a new layer
        cleanDST (bool): Clean destination layer
        toBack (bool): Add layer to back of the layer stack
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-decompose" href="#pGlyph-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decompose all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-dereference" href="#pGlyph-dereference"><span class="function-name">dereference</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all shape references but leave components.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-draw" href="#pGlyph-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-drawPoints" href="#pGlyph-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the PointPen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-duplicateLayer" href="#pGlyph-duplicateLayer"><span class="function-name">duplicateLayer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, newLayerName<span class="parameter-default">='New Layer'</span>, references<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a layer with new name and adds it to glyph's layers.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        toBack(bool): send to back
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-elements" href="#pGlyph-elements"><span class="function-name">elements</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph elements in glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_activeLayer" href="#pGlyph-fg_activeLayer"><span class="function-name">fg_activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_contours" href="#pGlyph-fg_contours"><span class="function-name">fg_contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_hasLayer" href="#pGlyph-fg_hasLayer"><span class="function-name">fg_hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_layer" href="#pGlyph-fg_layer"><span class="function-name">fg_layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns FontGate layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        fgLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_layers" href="#pGlyph-fg_layers"><span class="function-name">fg_layers</span></a><span class="argspec">(self, asDict<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FotnGate layers</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_nodes" href="#pGlyph-fg_nodes"><span class="function-name">fg_nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_shapes" href="#pGlyph-fg_shapes"><span class="function-name">fg_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findAnchor" href="#pGlyph-findAnchor"><span class="function-name">findAnchor</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findAnchorCoords" href="#pGlyph-findAnchorCoords"><span class="function-name">findAnchorCoords</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findNode" href="#pGlyph-findNode"><span class="function-name">findNode</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findNodeCoords" href="#pGlyph-findNodeCoords"><span class="function-name">findNodeCoords</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findShape" href="#pGlyph-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds shape by name on given layer
Args:
        shapeName (str): Shape name
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flShape or None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fontMetricsInfo" href="#pGlyph-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (<a href="./__builtin__.html#object">object</a>)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getAdvance" href="#pGlyph-getAdvance"><span class="function-name">getAdvance</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Advance Width at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getBounds" href="#pGlyph-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Glyph's Boundig Box at given layer (int or str). Returns QRectF.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getBuilders" href="#pGlyph-getBuilders"><span class="function-name">getBuilders</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, store<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getCompositionDict" href="#pGlyph-getCompositionDict"><span class="function-name">getCompositionDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return composition dict of a glyph. Elements!</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getCompositionNames" href="#pGlyph-getCompositionNames"><span class="function-name">getCompositionNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return name of glyph and the parts it is made of.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getElementNames" href="#pGlyph-getElementNames"><span class="function-name">getElementNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return names of elements references used in glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getLSB" href="#pGlyph-getLSB"><span class="function-name">getLSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Left Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getRSB" href="#pGlyph-getRSB"><span class="function-name">getRSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Right Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getSBeq" href="#pGlyph-getSBeq"><span class="function-name">getSBeq</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">GET LSB, RSB metric equations on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getSegment" href="#pGlyph-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns contour segment of the node specified at given layer
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        CurveEx</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getTags" href="#pGlyph-getTags"><span class="function-name">getTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Tags -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-guidelines" href="#pGlyph-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of guidelines (list[flGuideline]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-hasLayer" href="#pGlyph-hasLayer"><span class="function-name">hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-insertNodeAt" href="#pGlyph-insertNodeAt"><span class="function-name">insertNodeAt</span></a><span class="argspec">(self, cID, nID_time, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts node in contour at specified layer
Arg:
        cID (int): Contour Index
        nID_time (float): Node index + float time
        layer (int or str): Layer index or name. If None returns ActiveLayer

!NOTE: FL6 treats contour insertions (as well as nodes) as float times along contour,
so inserting a node at .5 t between nodes with indexes 3 and 4 will be 3 (index) + 0.5 (time) = 3.5</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-insertNodesAt" href="#pGlyph-insertNodesAt"><span class="function-name">insertNodesAt</span></a><span class="argspec">(self, cID, nID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts a list of nodes to specified contour, starting at given index all on layer specified.
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-isCompatible" href="#pGlyph-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph is ready for interpolation - all master layers are compatible.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-isMixedReference" href="#pGlyph-isMixedReference"><span class="function-name">isMixedReference</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph has mixed references - components on some layers and referenced shapes on others</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-italicAngle" href="#pGlyph-italicAngle"><span class="function-name">italicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-layer" href="#pGlyph-layer"><span class="function-name">layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-layers" href="#pGlyph-layers"><span class="function-name">layers</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return all layers</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mLine" href="#pGlyph-mLine"><span class="function-name">mLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mapNodes2Times" href="#pGlyph-mapNodes2Times"><span class="function-name">mapNodes2Times</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Nodes at contour times for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Contour Time (int): Node Index (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mapTimes2Nodes" href="#pGlyph-mapTimes2Nodes"><span class="function-name">mapTimes2Nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Contour times at node indexes for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Node Index (int) : Contour Time (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mask" href="#pGlyph-mask"><span class="function-name">mask</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-masks" href="#pGlyph-masks"><span class="function-name">masks</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all mask layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-masters" href="#pGlyph-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all master layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-newAnchor" href="#pGlyph-newAnchor"><span class="function-name">newAnchor</span></a><span class="argspec">(self, coordTuple, name, anchorType<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Not working</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodes" href="#pGlyph-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer.
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodes4segments" href="#pGlyph-nodes4segments"><span class="function-name">nodes4segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments and their corresponding nodes at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        dict{time(int):(CurveEx, list[flNode]}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodesForIndices" href="#pGlyph-nodesForIndices"><span class="function-name">nodesForIndices</span></a><span class="argspec">(self, indices, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-noncomplex" href="#pGlyph-noncomplex"><span class="function-name">noncomplex</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph shapes that are not glyph references or components</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-object" href="#pGlyph-object"><span class="function-name">object</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeLayer" href="#pGlyph-removeLayer"><span class="function-name">removeLayer</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Removes a layer from glyph.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeNodeAt" href="#pGlyph-removeNodeAt"><span class="function-name">removeNodeAt</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a node from contour at layer specified.
Args:
        cID (int): Contour index
        nID (int): Index of Node to be removed
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeNodes" href="#pGlyph-removeNodes"><span class="function-name">removeNodes</span></a><span class="argspec">(self, cID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a list of nodes from contour at layer specified.
Args:
        cID (int): Contour index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeShape" href="#pGlyph-removeShape"><span class="function-name">removeShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, recursive<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a new shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
        recursive (bool): 
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-replaceShape" href="#pGlyph-replaceShape"><span class="function-name">replaceShape</span></a><span class="argspec">(self, old_shape, new_shape, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Repalce a shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-reportLayerComp" href="#pGlyph-reportLayerComp"><span class="function-name">reportLayerComp</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns a layer compatibility report</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-rotate" href="#pGlyph-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rotate outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-scale" href="#pGlyph-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Scale outline at given layer.
Args:
        sx (float), sy (float): delta (scaling) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-segments" href="#pGlyph-segments"><span class="function-name">segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selected" href="#pGlyph-selected"><span class="function-name">selected</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes indexes at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedAtContours" href="#pGlyph-selectedAtContours"><span class="function-name">selectedAtContours</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the contours they rest upon at current layer.
Args:
        index (bool): If True returns only indexes, False returns flContour, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(contourID, nodeID)..()] or 
        list[tuple(flContour, flNode)]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedAtShapes" href="#pGlyph-selectedAtShapes"><span class="function-name">selectedAtShapes</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, filterOn<span class="parameter-default">=False</span>, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the shapes they belong at current layer.
Args:
        index (bool): If True returns only indexes, False returns flShape, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(shapeID, nodeID)..()] or
        list[tuple(flShape, flNode)]

!TODO: Make it working with layers as <a href="#pGlyph-selectedAtContours">selectedAtContours</a>(). This is legacy mode so other scripts would work!</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedContours" href="#pGlyph-selectedContours"><span class="function-name">selectedContours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, allNodesSelected<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedCoords" href="#pGlyph-selectedCoords"><span class="function-name">selectedCoords</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, applyTransform<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the coordinates of all selected nodes at the current layer or other.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        filterOn (bool): Return only on-curve nodes
        applyTransform (bool) : Gets local shape transformation matrix and applies it to the node coordinates
Returns:
        list[QPointF]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodeIndices" href="#pGlyph-selectedNodeIndices"><span class="function-name">selectedNodeIndices</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodes" href="#pGlyph-selectedNodes"><span class="function-name">selectedNodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes at given layer.
Args:
        filterOn (bool): Return only on-curve nodes
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNode]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodesOnCanvas" href="#pGlyph-selectedNodesOnCanvas"><span class="function-name">selectedNodesOnCanvas</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Glyph Selection -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedSegments" href="#pGlyph-selectedSegments"><span class="function-name">selectedSegments</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns list of currently selected segments
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedShapeIndices" href="#pGlyph-selectedShapeIndices"><span class="function-name">selectedShapeIndices</span></a><span class="argspec">(self, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        select_all (bool): True all nodes on Shape should be selected. False any node will do.
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedShapes" href="#pGlyph-selectedShapes"><span class="function-name">selectedShapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes that have a node selected.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-services" href="#pGlyph-services"><span class="function-name">services</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all service layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setADVeq" href="#pGlyph-setADVeq"><span class="function-name">setADVeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set Advance width metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setAdvance" href="#pGlyph-setAdvance"><span class="function-name">setAdvance</span></a><span class="argspec">(self, newAdvance, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Advance Width (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setLSB" href="#pGlyph-setLSB"><span class="function-name">setLSB</span></a><span class="argspec">(self, newLSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Left Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setLSBeq" href="#pGlyph-setLSBeq"><span class="function-name">setLSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set LSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setMark" href="#pGlyph-setMark"><span class="function-name">setMark</span></a><span class="argspec">(self, mark_color, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setName" href="#pGlyph-setName"><span class="function-name">setName</span></a><span class="argspec">(self, glyph_name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setRSB" href="#pGlyph-setRSB"><span class="function-name">setRSB</span></a><span class="argspec">(self, newRSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Right Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setRSBeq" href="#pGlyph-setRSBeq"><span class="function-name">setRSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set RSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setTags" href="#pGlyph-setTags"><span class="function-name">setTags</span></a><span class="argspec">(self, tagList, append<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-shapes" href="#pGlyph-shapes"><span class="function-name">shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-shapes_data" href="#pGlyph-shapes_data"><span class="function-name">shapes_data</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all flShapeData objects at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapeData]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-slant" href="#pGlyph-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Slant outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-tag" href="#pGlyph-tag"><span class="function-name">tag</span></a><span class="argspec">(self, newTag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-translate" href="#pGlyph-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Translate (shift) outline at given layer.
Args:
        dx (float), dy (float): delta (shift) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-update" href="#pGlyph-update"><span class="function-name">update</span></a><span class="argspec">(self, fl<span class="parameter-default">=True</span>, fg<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates the glyph and sends notification to the editor.
Args:
        fl (bool): Update the flGlyph
        fg (bool): Update the fgGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-updateObject" href="#pGlyph-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-version" href="#pGlyph-version"><span class="function-name">version</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
</dl>
<dl class="descriptor"><dt>index</dt>
</dl>
<dl class="descriptor"><dt>mark</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>package</dt>
</dl>
<dl class="descriptor"><dt>tags</dt>
</dl>
<dl class="descriptor"><dt>unicode</dt>
</dl>
<dl class="descriptor"><dt>unicodes</dt>
</dl>
</dd></dl></div></div>


<a name="typerig.proxy.objects.glyph.pGlyph"></a>

## `pGlyph`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.glyph.pGlyph</span> = <a name="typerig.proxy.objects.glyph.pGlyph" href="#typerig.proxy.objects.glyph.pGlyph">class pGlyph</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flGlyph and fgGlyph combined into single entity.

Constructor:
        pGlyph() : default represents the current glyph and current font
        pGlyph(flGlyph)
        pGlyph(fgFont, fgGlyph)

Methods:

Attributes:
        .parent (fgFont)
        .fg (fgGlyph)
        .fl (flGlyph)
        ...</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pGlyph-__init__" href="#pGlyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-__repr__" href="#pGlyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-activeGuides" href="#pGlyph-activeGuides"><span class="function-name">activeGuides</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-activeLayer" href="#pGlyph-activeLayer"><span class="function-name">activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addAnchor" href="#pGlyph-addAnchor"><span class="function-name">addAnchor</span></a><span class="argspec">(self, coordTuple, name, layer<span class="parameter-default">=None</span>, isAnchor<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Anchor at given layer.
Args:
        coordTuple (tuple(float,float)): Anchor coordinates X, Y
        name (str): Anchor name
        layer (int or str): Layer index or name. If None returns ActiveLayer
        isAnchor (bool): True creates a true flAnchor, False ? (flPinPoint)
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addComponents" href="#pGlyph-addComponents"><span class="function-name">addComponents</span></a><span class="argspec">(self, componentConfig, layer<span class="parameter-default">=None</span>, useAnchors<span class="parameter-default">=True</span>, colorize<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a components to given glyph layer.
Args:
        componentConfig (list(tuple(glyph_name (str), glyph_transform (QTransform), layer_pointer (str)))): List contianign component configuration.  
        layer (int or str): Layer index or name. If None returns ActiveLayer
        useAnchors (bool): Compose using anchors
        colorize (bool): Flag new glyphs
Returns:
        list(flShapes): List of components added</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addGuideline" href="#pGlyph-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, coordTuple, layer<span class="parameter-default">=None</span>, angle<span class="parameter-default">=0</span>, name<span class="parameter-default">=''</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Guideline at given layer
Args:
        coordTuple (tuple(float,float) or tuple(float,float,float,float)): Guideline coordinates X, Y and given angle or two node reference x1,y1 and x2,y2
        name (str): Anchor name
        angle (float): Incline of the guideline
        layer (int or str): Layer index or name. If None returns ActiveLayer                    
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addLayer" href="#pGlyph-addLayer"><span class="function-name">addLayer</span></a><span class="argspec">(self, layer, toBack<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a layer to glyph.
Args:
        layer (flLayer or fgLayer)
        toBack (bool): Send layer to back
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addShape" href="#pGlyph-addShape"><span class="function-name">addShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, clone<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape at given layer.
Args:
        shape (flShape): Shape to be added
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-addShapeContainer" href="#pGlyph-addShapeContainer"><span class="function-name">addShapeContainer</span></a><span class="argspec">(self, shapeList, layer<span class="parameter-default">=None</span>, remove<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape container* at given layer.
A flShape containing all of the shapes given that
could be transformed to Shape-group or shape-filter.
Args:
        shapeList list(flShape): List if Shapes to be grouped.
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-anchors" href="#pGlyph-anchors"><span class="function-name">anchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of anchors (list[flAnchor]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-blendShapes" href="#pGlyph-blendShapes"><span class="function-name">blendShapes</span></a><span class="argspec">(self, shapeA, shapeB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two shapes at given times (anisotropic support).
Args:
        shapeA (flShape), shapeB (flShape): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        Native (interpolation engine dependent) or flShape (default)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-clearAnchors" href="#pGlyph-clearAnchors"><span class="function-name">clearAnchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all anchors at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-components" href="#pGlyph-components"><span class="function-name">components</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph components besides glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-containers" href="#pGlyph-containers"><span class="function-name">containers</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-contours" href="#pGlyph-contours"><span class="function-name">contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=True</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-copyLayer" href="#pGlyph-copyLayer"><span class="function-name">copyLayer</span></a><span class="argspec">(self, srcLayerName, dstLayerName, options<span class="parameter-default">={'adv': True, 'anc': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True}</span>, addLayer<span class="parameter-default">=False</span>, cleanDST<span class="parameter-default">=True</span>, toBack<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copies a layer within the glyph.
Args:
        srcLayerName, dstLayerName (string): Source and destination layer names
        options (dict): Copy Options as follows {'out': Outline, 'gui': Guidelines, 'anc': Anchors, 'lsb': LSB, 'adv': Advance, 'rsb': RSB, 'lnk': Linked metrics, 'ref': References}, addLayer=False):
        addLayer (bool): Create a new layer
        cleanDST (bool): Clean destination layer
        toBack (bool): Add layer to back of the layer stack
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-decompose" href="#pGlyph-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decompose all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-dereference" href="#pGlyph-dereference"><span class="function-name">dereference</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all shape references but leave components.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-draw" href="#pGlyph-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-drawPoints" href="#pGlyph-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the PointPen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-duplicateLayer" href="#pGlyph-duplicateLayer"><span class="function-name">duplicateLayer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, newLayerName<span class="parameter-default">='New Layer'</span>, references<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a layer with new name and adds it to glyph's layers.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        toBack(bool): send to back
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-elements" href="#pGlyph-elements"><span class="function-name">elements</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph elements in glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_activeLayer" href="#pGlyph-fg_activeLayer"><span class="function-name">fg_activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_contours" href="#pGlyph-fg_contours"><span class="function-name">fg_contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_hasLayer" href="#pGlyph-fg_hasLayer"><span class="function-name">fg_hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_layer" href="#pGlyph-fg_layer"><span class="function-name">fg_layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns FontGate layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        fgLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_layers" href="#pGlyph-fg_layers"><span class="function-name">fg_layers</span></a><span class="argspec">(self, asDict<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FotnGate layers</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_nodes" href="#pGlyph-fg_nodes"><span class="function-name">fg_nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fg_shapes" href="#pGlyph-fg_shapes"><span class="function-name">fg_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findAnchor" href="#pGlyph-findAnchor"><span class="function-name">findAnchor</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findAnchorCoords" href="#pGlyph-findAnchorCoords"><span class="function-name">findAnchorCoords</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findNode" href="#pGlyph-findNode"><span class="function-name">findNode</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findNodeCoords" href="#pGlyph-findNodeCoords"><span class="function-name">findNodeCoords</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-findShape" href="#pGlyph-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds shape by name on given layer
Args:
        shapeName (str): Shape name
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flShape or None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-fontMetricsInfo" href="#pGlyph-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getAdvance" href="#pGlyph-getAdvance"><span class="function-name">getAdvance</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Advance Width at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getBounds" href="#pGlyph-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Glyph's Boundig Box at given layer (int or str). Returns QRectF.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getBuilders" href="#pGlyph-getBuilders"><span class="function-name">getBuilders</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, store<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getCompositionDict" href="#pGlyph-getCompositionDict"><span class="function-name">getCompositionDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return composition dict of a glyph. Elements!</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getCompositionNames" href="#pGlyph-getCompositionNames"><span class="function-name">getCompositionNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return name of glyph and the parts it is made of.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getElementNames" href="#pGlyph-getElementNames"><span class="function-name">getElementNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return names of elements references used in glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getLSB" href="#pGlyph-getLSB"><span class="function-name">getLSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Left Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getRSB" href="#pGlyph-getRSB"><span class="function-name">getRSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Right Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getSBeq" href="#pGlyph-getSBeq"><span class="function-name">getSBeq</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">GET LSB, RSB metric equations on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getSegment" href="#pGlyph-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns contour segment of the node specified at given layer
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        CurveEx</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-getTags" href="#pGlyph-getTags"><span class="function-name">getTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Tags -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-guidelines" href="#pGlyph-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of guidelines (list[flGuideline]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-hasLayer" href="#pGlyph-hasLayer"><span class="function-name">hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-insertNodeAt" href="#pGlyph-insertNodeAt"><span class="function-name">insertNodeAt</span></a><span class="argspec">(self, cID, nID_time, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts node in contour at specified layer
Arg:
        cID (int): Contour Index
        nID_time (float): Node index + float time
        layer (int or str): Layer index or name. If None returns ActiveLayer

!NOTE: FL6 treats contour insertions (as well as nodes) as float times along contour,
so inserting a node at .5 t between nodes with indexes 3 and 4 will be 3 (index) + 0.5 (time) = 3.5</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-insertNodesAt" href="#pGlyph-insertNodesAt"><span class="function-name">insertNodesAt</span></a><span class="argspec">(self, cID, nID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts a list of nodes to specified contour, starting at given index all on layer specified.
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-isCompatible" href="#pGlyph-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph is ready for interpolation - all master layers are compatible.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-isMixedReference" href="#pGlyph-isMixedReference"><span class="function-name">isMixedReference</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph has mixed references - components on some layers and referenced shapes on others</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-italicAngle" href="#pGlyph-italicAngle"><span class="function-name">italicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-layer" href="#pGlyph-layer"><span class="function-name">layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-layers" href="#pGlyph-layers"><span class="function-name">layers</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return all layers</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mLine" href="#pGlyph-mLine"><span class="function-name">mLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mapNodes2Times" href="#pGlyph-mapNodes2Times"><span class="function-name">mapNodes2Times</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Nodes at contour times for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Contour Time (int): Node Index (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mapTimes2Nodes" href="#pGlyph-mapTimes2Nodes"><span class="function-name">mapTimes2Nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Contour times at node indexes for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Node Index (int) : Contour Time (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-mask" href="#pGlyph-mask"><span class="function-name">mask</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-masks" href="#pGlyph-masks"><span class="function-name">masks</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all mask layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-masters" href="#pGlyph-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all master layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-newAnchor" href="#pGlyph-newAnchor"><span class="function-name">newAnchor</span></a><span class="argspec">(self, coordTuple, name, anchorType<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Not working</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodes" href="#pGlyph-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer.
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodes4segments" href="#pGlyph-nodes4segments"><span class="function-name">nodes4segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments and their corresponding nodes at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        dict{time(int):(CurveEx, list[flNode]}</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-nodesForIndices" href="#pGlyph-nodesForIndices"><span class="function-name">nodesForIndices</span></a><span class="argspec">(self, indices, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-noncomplex" href="#pGlyph-noncomplex"><span class="function-name">noncomplex</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph shapes that are not glyph references or components</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-object" href="#pGlyph-object"><span class="function-name">object</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeLayer" href="#pGlyph-removeLayer"><span class="function-name">removeLayer</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Removes a layer from glyph.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeNodeAt" href="#pGlyph-removeNodeAt"><span class="function-name">removeNodeAt</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a node from contour at layer specified.
Args:
        cID (int): Contour index
        nID (int): Index of Node to be removed
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeNodes" href="#pGlyph-removeNodes"><span class="function-name">removeNodes</span></a><span class="argspec">(self, cID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a list of nodes from contour at layer specified.
Args:
        cID (int): Contour index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-removeShape" href="#pGlyph-removeShape"><span class="function-name">removeShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, recursive<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a new shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
        recursive (bool): 
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-replaceShape" href="#pGlyph-replaceShape"><span class="function-name">replaceShape</span></a><span class="argspec">(self, old_shape, new_shape, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Repalce a shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-reportLayerComp" href="#pGlyph-reportLayerComp"><span class="function-name">reportLayerComp</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns a layer compatibility report</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-rotate" href="#pGlyph-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rotate outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-scale" href="#pGlyph-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Scale outline at given layer.
Args:
        sx (float), sy (float): delta (scaling) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-segments" href="#pGlyph-segments"><span class="function-name">segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selected" href="#pGlyph-selected"><span class="function-name">selected</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes indexes at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedAtContours" href="#pGlyph-selectedAtContours"><span class="function-name">selectedAtContours</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the contours they rest upon at current layer.
Args:
        index (bool): If True returns only indexes, False returns flContour, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(contourID, nodeID)..()] or 
        list[tuple(flContour, flNode)]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedAtShapes" href="#pGlyph-selectedAtShapes"><span class="function-name">selectedAtShapes</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, filterOn<span class="parameter-default">=False</span>, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the shapes they belong at current layer.
Args:
        index (bool): If True returns only indexes, False returns flShape, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(shapeID, nodeID)..()] or
        list[tuple(flShape, flNode)]

!TODO: Make it working with layers as <a href="#typerig.proxy.objects.glyph.pGlyph-selectedAtContours">selectedAtContours</a>(). This is legacy mode so other scripts would work!</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedContours" href="#pGlyph-selectedContours"><span class="function-name">selectedContours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, allNodesSelected<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedCoords" href="#pGlyph-selectedCoords"><span class="function-name">selectedCoords</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, applyTransform<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the coordinates of all selected nodes at the current layer or other.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        filterOn (bool): Return only on-curve nodes
        applyTransform (bool) : Gets local shape transformation matrix and applies it to the node coordinates
Returns:
        list[QPointF]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodeIndices" href="#pGlyph-selectedNodeIndices"><span class="function-name">selectedNodeIndices</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodes" href="#pGlyph-selectedNodes"><span class="function-name">selectedNodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes at given layer.
Args:
        filterOn (bool): Return only on-curve nodes
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNode]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedNodesOnCanvas" href="#pGlyph-selectedNodesOnCanvas"><span class="function-name">selectedNodesOnCanvas</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Glyph Selection -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedSegments" href="#pGlyph-selectedSegments"><span class="function-name">selectedSegments</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns list of currently selected segments
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedShapeIndices" href="#pGlyph-selectedShapeIndices"><span class="function-name">selectedShapeIndices</span></a><span class="argspec">(self, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        select_all (bool): True all nodes on Shape should be selected. False any node will do.
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-selectedShapes" href="#pGlyph-selectedShapes"><span class="function-name">selectedShapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes that have a node selected.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-services" href="#pGlyph-services"><span class="function-name">services</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all service layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setADVeq" href="#pGlyph-setADVeq"><span class="function-name">setADVeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set Advance width metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setAdvance" href="#pGlyph-setAdvance"><span class="function-name">setAdvance</span></a><span class="argspec">(self, newAdvance, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Advance Width (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setLSB" href="#pGlyph-setLSB"><span class="function-name">setLSB</span></a><span class="argspec">(self, newLSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Left Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setLSBeq" href="#pGlyph-setLSBeq"><span class="function-name">setLSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set LSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setMark" href="#pGlyph-setMark"><span class="function-name">setMark</span></a><span class="argspec">(self, mark_color, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setName" href="#pGlyph-setName"><span class="function-name">setName</span></a><span class="argspec">(self, glyph_name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setRSB" href="#pGlyph-setRSB"><span class="function-name">setRSB</span></a><span class="argspec">(self, newRSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Right Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setRSBeq" href="#pGlyph-setRSBeq"><span class="function-name">setRSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set RSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-setTags" href="#pGlyph-setTags"><span class="function-name">setTags</span></a><span class="argspec">(self, tagList, append<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-shapes" href="#pGlyph-shapes"><span class="function-name">shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-shapes_data" href="#pGlyph-shapes_data"><span class="function-name">shapes_data</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all flShapeData objects at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapeData]</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-slant" href="#pGlyph-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Slant outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-tag" href="#pGlyph-tag"><span class="function-name">tag</span></a><span class="argspec">(self, newTag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-translate" href="#pGlyph-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Translate (shift) outline at given layer.
Args:
        dx (float), dy (float): delta (shift) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-update" href="#pGlyph-update"><span class="function-name">update</span></a><span class="argspec">(self, fl<span class="parameter-default">=True</span>, fg<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates the glyph and sends notification to the editor.
Args:
        fl (bool): Update the flGlyph
        fg (bool): Update the fgGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-updateObject" href="#pGlyph-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="pGlyph-version" href="#pGlyph-version"><span class="function-name">version</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
</dl>
<dl class="descriptor"><dt>index</dt>
</dl>
<dl class="descriptor"><dt>mark</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>package</dt>
</dl>
<dl class="descriptor"><dt>tags</dt>
</dl>
<dl class="descriptor"><dt>unicode</dt>
</dl>
<dl class="descriptor"><dt>unicodes</dt>
</dl>
</dd>


<a name="typerig.proxy.objects.glyph.pGlyph.nodes"></a>

### `nodes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.nodes" href="#-typerig.proxy.objects.glyph.pGlyph.nodes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.nodes</span></a> = nodes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer.
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNodes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fg_nodes"></a>

### `fg_nodes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fg_nodes" href="#-typerig.proxy.objects.glyph.pGlyph.fg_nodes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fg_nodes</span></a> = fg_nodes<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgNodes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.contours"></a>

### `contours`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.contours" href="#-typerig.proxy.objects.glyph.pGlyph.contours"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.contours</span></a> = contours<span class="argspec">(self, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=True</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flContours]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fg_contours"></a>

### `fg_contours`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fg_contours" href="#-typerig.proxy.objects.glyph.pGlyph.fg_contours"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fg_contours</span></a> = fg_contours<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgContours]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.layers"></a>

### `layers`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.layers" href="#-typerig.proxy.objects.glyph.pGlyph.layers"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.layers</span></a> = layers<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all layers</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fg_layers"></a>

### `fg_layers`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fg_layers" href="#-typerig.proxy.objects.glyph.pGlyph.fg_layers"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fg_layers</span></a> = fg_layers<span class="argspec">(self, asDict<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all FotnGate layers</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.layer"></a>

### `layer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.layer" href="#-typerig.proxy.objects.glyph.pGlyph.layer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.layer</span></a> = layer<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flLayer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fg_layer"></a>

### `fg_layer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fg_layer" href="#-typerig.proxy.objects.glyph.pGlyph.fg_layer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fg_layer</span></a> = fg_layer<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns FontGate layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        fgLayer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.shapes"></a>

### `shapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.shapes" href="#-typerig.proxy.objects.glyph.pGlyph.shapes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.shapes</span></a> = shapes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getElementNames"></a>

### `getElementNames`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getElementNames" href="#-typerig.proxy.objects.glyph.pGlyph.getElementNames"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getElementNames</span></a> = getElementNames<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return names of elements references used in glyph.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.dereference"></a>

### `dereference`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.dereference" href="#-typerig.proxy.objects.glyph.pGlyph.dereference"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.dereference</span></a> = dereference<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Remove all shape references but leave components.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.containers"></a>

### `containers`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.containers" href="#-typerig.proxy.objects.glyph.pGlyph.containers"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.containers</span></a> = containers<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.decompose"></a>

### `decompose`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.decompose" href="#-typerig.proxy.objects.glyph.pGlyph.decompose"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.decompose</span></a> = decompose<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Decompose all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addShape"></a>

### `addShape`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addShape" href="#-typerig.proxy.objects.glyph.pGlyph.addShape"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addShape</span></a> = addShape<span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, clone<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape at given layer.
Args:
        shape (flShape): Shape to be added
Returns:
        flShape</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.replaceShape"></a>

### `replaceShape`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.replaceShape" href="#-typerig.proxy.objects.glyph.pGlyph.replaceShape"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.replaceShape</span></a> = replaceShape<span class="argspec">(self, old_shape, new_shape, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Repalce a shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.removeShape"></a>

### `removeShape`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.removeShape" href="#-typerig.proxy.objects.glyph.pGlyph.removeShape"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.removeShape</span></a> = removeShape<span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, recursive<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Remove a new shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
        recursive (bool): 
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addShapeContainer"></a>

### `addShapeContainer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addShapeContainer" href="#-typerig.proxy.objects.glyph.pGlyph.addShapeContainer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addShapeContainer</span></a> = addShapeContainer<span class="argspec">(self, shapeList, layer<span class="parameter-default">=None</span>, remove<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape container* at given layer.
A flShape containing all of the shapes given that
could be transformed to Shape-group or shape-filter.
Args:
        shapeList list(flShape): List if Shapes to be grouped.
Returns:
        flShape</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.findShape"></a>

### `findShape`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.findShape" href="#-typerig.proxy.objects.glyph.pGlyph.findShape"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.findShape</span></a> = findShape<span class="argspec">(self, shapeName, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Finds shape by name on given layer
Args:
        shapeName (str): Shape name
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flShape or None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.shapes_data"></a>

### `shapes_data`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.shapes_data" href="#-typerig.proxy.objects.glyph.pGlyph.shapes_data"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.shapes_data</span></a> = shapes_data<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all flShapeData objects at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapeData]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fg_shapes"></a>

### `fg_shapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fg_shapes" href="#-typerig.proxy.objects.glyph.pGlyph.fg_shapes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fg_shapes</span></a> = fg_shapes<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgShapes]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.elements"></a>

### `elements`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.elements" href="#-typerig.proxy.objects.glyph.pGlyph.elements"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.elements</span></a> = elements<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph elements in glyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.noncomplex"></a>

### `noncomplex`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.noncomplex" href="#-typerig.proxy.objects.glyph.pGlyph.noncomplex"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.noncomplex</span></a> = noncomplex<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph shapes that are not glyph references or components</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.components"></a>

### `components`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.components" href="#-typerig.proxy.objects.glyph.pGlyph.components"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.components</span></a> = components<span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph components besides glyph.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getCompositionNames"></a>

### `getCompositionNames`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getCompositionNames" href="#-typerig.proxy.objects.glyph.pGlyph.getCompositionNames"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getCompositionNames</span></a> = getCompositionNames<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return name of glyph and the parts it is made of.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getCompositionDict"></a>

### `getCompositionDict`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getCompositionDict" href="#-typerig.proxy.objects.glyph.pGlyph.getCompositionDict"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getCompositionDict</span></a> = getCompositionDict<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return composition dict of a glyph. Elements!</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addComponents"></a>

### `addComponents`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addComponents" href="#-typerig.proxy.objects.glyph.pGlyph.addComponents"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addComponents</span></a> = addComponents<span class="argspec">(self, componentConfig, layer<span class="parameter-default">=None</span>, useAnchors<span class="parameter-default">=True</span>, colorize<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a components to given glyph layer.
Args:
        componentConfig (list(tuple(glyph_name (str), glyph_transform (QTransform), layer_pointer (str)))): List contianign component configuration.  
        layer (int or str): Layer index or name. If None returns ActiveLayer
        useAnchors (bool): Compose using anchors
        colorize (bool): Flag new glyphs
Returns:
        list(flShapes): List of components added</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.masters"></a>

### `masters`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.masters" href="#-typerig.proxy.objects.glyph.pGlyph.masters"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.masters</span></a> = masters<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all master layers.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.masks"></a>

### `masks`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.masks" href="#-typerig.proxy.objects.glyph.pGlyph.masks"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.masks</span></a> = masks<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all mask layers.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.services"></a>

### `services`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.services" href="#-typerig.proxy.objects.glyph.pGlyph.services"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.services</span></a> = services<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all service layers.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addLayer"></a>

### `addLayer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addLayer" href="#-typerig.proxy.objects.glyph.pGlyph.addLayer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addLayer</span></a> = addLayer<span class="argspec">(self, layer, toBack<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a layer to glyph.
Args:
        layer (flLayer or fgLayer)
        toBack (bool): Send layer to back
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.removeLayer"></a>

### `removeLayer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.removeLayer" href="#-typerig.proxy.objects.glyph.pGlyph.removeLayer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.removeLayer</span></a> = removeLayer<span class="argspec">(self, layer)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Removes a layer from glyph.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.duplicateLayer"></a>

### `duplicateLayer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.duplicateLayer" href="#-typerig.proxy.objects.glyph.pGlyph.duplicateLayer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.duplicateLayer</span></a> = duplicateLayer<span class="argspec">(self, layer<span class="parameter-default">=None</span>, newLayerName<span class="parameter-default">='New Layer'</span>, references<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a layer with new name and adds it to glyph's layers.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        toBack(bool): send to back
Returns:
        flLayer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.copyLayer"></a>

### `copyLayer`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.copyLayer" href="#-typerig.proxy.objects.glyph.pGlyph.copyLayer"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.copyLayer</span></a> = copyLayer<span class="argspec">(self, srcLayerName, dstLayerName, options<span class="parameter-default">={'adv': True, 'anc': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True}</span>, addLayer<span class="parameter-default">=False</span>, cleanDST<span class="parameter-default">=True</span>, toBack<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Copies a layer within the glyph.
Args:
        srcLayerName, dstLayerName (string): Source and destination layer names
        options (dict): Copy Options as follows {'out': Outline, 'gui': Guidelines, 'anc': Anchors, 'lsb': LSB, 'adv': Advance, 'rsb': RSB, 'lnk': Linked metrics, 'ref': References}, addLayer=False):
        addLayer (bool): Create a new layer
        cleanDST (bool): Clean destination layer
        toBack (bool): Add layer to back of the layer stack
Returns:
        flLayer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.isCompatible"></a>

### `isCompatible`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.isCompatible" href="#-typerig.proxy.objects.glyph.pGlyph.isCompatible"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.isCompatible</span></a> = isCompatible<span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph is ready for interpolation - all master layers are compatible.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.isMixedReference"></a>

### `isMixedReference`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.isMixedReference" href="#-typerig.proxy.objects.glyph.pGlyph.isMixedReference"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.isMixedReference</span></a> = isMixedReference<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph has mixed references - components on some layers and referenced shapes on others</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.reportLayerComp"></a>

### `reportLayerComp`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.reportLayerComp" href="#-typerig.proxy.objects.glyph.pGlyph.reportLayerComp"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.reportLayerComp</span></a> = reportLayerComp<span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns a layer compatibility report</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.update"></a>

### `update`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.update" href="#-typerig.proxy.objects.glyph.pGlyph.update"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.update</span></a> = update<span class="argspec">(self, fl<span class="parameter-default">=True</span>, fg<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Updates the glyph and sends notification to the editor.
Args:
        fl (bool): Update the flGlyph
        fg (bool): Update the fgGlyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.updateObject"></a>

### `updateObject`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.updateObject" href="#-typerig.proxy.objects.glyph.pGlyph.updateObject"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.updateObject</span></a> = updateObject<span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedNodeIndices"></a>

### `selectedNodeIndices`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedNodeIndices" href="#-typerig.proxy.objects.glyph.pGlyph.selectedNodeIndices"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedNodeIndices</span></a> = selectedNodeIndices<span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selected"></a>

### `selected`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selected" href="#-typerig.proxy.objects.glyph.pGlyph.selected"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selected</span></a> = selected<span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes indexes at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedNodes"></a>

### `selectedNodes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedNodes" href="#-typerig.proxy.objects.glyph.pGlyph.selectedNodes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedNodes</span></a> = selectedNodes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes at given layer.
Args:
        filterOn (bool): Return only on-curve nodes
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNode]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedAtContours"></a>

### `selectedAtContours`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedAtContours" href="#-typerig.proxy.objects.glyph.pGlyph.selectedAtContours"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedAtContours</span></a> = selectedAtContours<span class="argspec">(self, index<span class="parameter-default">=True</span>, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the contours they rest upon at current layer.
Args:
        index (bool): If True returns only indexes, False returns flContour, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(contourID, nodeID)..()] or 
        list[tuple(flContour, flNode)]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedAtShapes"></a>

### `selectedAtShapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedAtShapes" href="#-typerig.proxy.objects.glyph.pGlyph.selectedAtShapes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedAtShapes</span></a> = selectedAtShapes<span class="argspec">(self, index<span class="parameter-default">=True</span>, filterOn<span class="parameter-default">=False</span>, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the shapes they belong at current layer.
Args:
        index (bool): If True returns only indexes, False returns flShape, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(shapeID, nodeID)..()] or
        list[tuple(flShape, flNode)]

!TODO: Make it working with layers as selectedAtContours(). This is legacy mode so other scripts would work!</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedShapeIndices"></a>

### `selectedShapeIndices`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedShapeIndices" href="#-typerig.proxy.objects.glyph.pGlyph.selectedShapeIndices"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedShapeIndices</span></a> = selectedShapeIndices<span class="argspec">(self, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        select_all (bool): True all nodes on Shape should be selected. False any node will do.
Returns:
        list[int]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedShapes"></a>

### `selectedShapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedShapes" href="#-typerig.proxy.objects.glyph.pGlyph.selectedShapes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedShapes</span></a> = selectedShapes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes that have a node selected.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedCoords"></a>

### `selectedCoords`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedCoords" href="#-typerig.proxy.objects.glyph.pGlyph.selectedCoords"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedCoords</span></a> = selectedCoords<span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, applyTransform<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return the coordinates of all selected nodes at the current layer or other.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        filterOn (bool): Return only on-curve nodes
        applyTransform (bool) : Gets local shape transformation matrix and applies it to the node coordinates
Returns:
        list[QPointF]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.selectedSegments"></a>

### `selectedSegments`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.selectedSegments" href="#-typerig.proxy.objects.glyph.pGlyph.selectedSegments"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.selectedSegments</span></a> = selectedSegments<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns list of currently selected segments
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.findNode"></a>

### `findNode`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.findNode" href="#-typerig.proxy.objects.glyph.pGlyph.findNode"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.findNode</span></a> = findNode<span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find node by name/tag</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.findNodeCoords"></a>

### `findNodeCoords`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.findNodeCoords" href="#-typerig.proxy.objects.glyph.pGlyph.findNodeCoords"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.findNodeCoords</span></a> = findNodeCoords<span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find node coordinates by name/tag</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.mapNodes2Times"></a>

### `mapNodes2Times`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.mapNodes2Times" href="#-typerig.proxy.objects.glyph.pGlyph.mapNodes2Times"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.mapNodes2Times</span></a> = mapNodes2Times<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Create map of Nodes at contour times for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Contour Time (int): Node Index (int) }}</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.mapTimes2Nodes"></a>

### `mapTimes2Nodes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.mapTimes2Nodes" href="#-typerig.proxy.objects.glyph.pGlyph.mapTimes2Nodes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.mapTimes2Nodes</span></a> = mapTimes2Nodes<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Create map of Contour times at node indexes for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Node Index (int) : Contour Time (int) }}</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getSegment"></a>

### `getSegment`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getSegment" href="#-typerig.proxy.objects.glyph.pGlyph.getSegment"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getSegment</span></a> = getSegment<span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns contour segment of the node specified at given layer
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        CurveEx</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.segments"></a>

### `segments`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.segments" href="#-typerig.proxy.objects.glyph.pGlyph.segments"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.segments</span></a> = segments<span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.nodes4segments"></a>

### `nodes4segments`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.nodes4segments" href="#-typerig.proxy.objects.glyph.pGlyph.nodes4segments"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.nodes4segments</span></a> = nodes4segments<span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments and their corresponding nodes at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        dict{time(int):(CurveEx, list[flNode]}</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.insertNodesAt"></a>

### `insertNodesAt`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.insertNodesAt" href="#-typerig.proxy.objects.glyph.pGlyph.insertNodesAt"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.insertNodesAt</span></a> = insertNodesAt<span class="argspec">(self, cID, nID, nodeList, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Inserts a list of nodes to specified contour, starting at given index all on layer specified.
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.removeNodes"></a>

### `removeNodes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.removeNodes" href="#-typerig.proxy.objects.glyph.pGlyph.removeNodes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.removeNodes</span></a> = removeNodes<span class="argspec">(self, cID, nodeList, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Removes a list of nodes from contour at layer specified.
Args:
        cID (int): Contour index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.insertNodeAt"></a>

### `insertNodeAt`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.insertNodeAt" href="#-typerig.proxy.objects.glyph.pGlyph.insertNodeAt"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.insertNodeAt</span></a> = insertNodeAt<span class="argspec">(self, cID, nID_time, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Inserts node in contour at specified layer
Arg:
        cID (int): Contour Index
        nID_time (float): Node index + float time
        layer (int or str): Layer index or name. If None returns ActiveLayer

!NOTE: FL6 treats contour insertions (as well as nodes) as float times along contour,
so inserting a node at .5 t between nodes with indexes 3 and 4 will be 3 (index) + 0.5 (time) = 3.5</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.removeNodeAt"></a>

### `removeNodeAt`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.removeNodeAt" href="#-typerig.proxy.objects.glyph.pGlyph.removeNodeAt"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.removeNodeAt</span></a> = removeNodeAt<span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Removes a node from contour at layer specified.
Args:
        cID (int): Contour index
        nID (int): Index of Node to be removed
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.translate"></a>

### `translate`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.translate" href="#-typerig.proxy.objects.glyph.pGlyph.translate"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.translate</span></a> = translate<span class="argspec">(self, dx, dy, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Translate (shift) outline at given layer.
Args:
        dx (float), dy (float): delta (shift) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.scale"></a>

### `scale`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.scale" href="#-typerig.proxy.objects.glyph.pGlyph.scale"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.scale</span></a> = scale<span class="argspec">(self, sx, sy, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Scale outline at given layer.
Args:
        sx (float), sy (float): delta (scaling) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.slant"></a>

### `slant`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.slant" href="#-typerig.proxy.objects.glyph.pGlyph.slant"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.slant</span></a> = slant<span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Slant outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.rotate"></a>

### `rotate`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.rotate" href="#-typerig.proxy.objects.glyph.pGlyph.rotate"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.rotate</span></a> = rotate<span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Rotate outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.blendShapes"></a>

### `blendShapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.blendShapes" href="#-typerig.proxy.objects.glyph.pGlyph.blendShapes"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.blendShapes</span></a> = blendShapes<span class="argspec">(self, shapeA, shapeB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Blend two shapes at given times (anisotropic support).
Args:
        shapeA (flShape), shapeB (flShape): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        Native (interpolation engine dependent) or flShape (default)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getLSB"></a>

### `getLSB`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getLSB" href="#-typerig.proxy.objects.glyph.pGlyph.getLSB"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getLSB</span></a> = getLSB<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Get the Left Side-bearing at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getAdvance"></a>

### `getAdvance`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getAdvance" href="#-typerig.proxy.objects.glyph.pGlyph.getAdvance"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getAdvance</span></a> = getAdvance<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Get the Advance Width at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getRSB"></a>

### `getRSB`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getRSB" href="#-typerig.proxy.objects.glyph.pGlyph.getRSB"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getRSB</span></a> = getRSB<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Get the Right Side-bearing at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getBounds"></a>

### `getBounds`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getBounds" href="#-typerig.proxy.objects.glyph.pGlyph.getBounds"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getBounds</span></a> = getBounds<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Get Glyph's Boundig Box at given layer (int or str). Returns QRectF.</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setLSB"></a>

### `setLSB`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setLSB" href="#-typerig.proxy.objects.glyph.pGlyph.setLSB"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setLSB</span></a> = setLSB<span class="argspec">(self, newLSB, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set the Left Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setRSB"></a>

### `setRSB`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setRSB" href="#-typerig.proxy.objects.glyph.pGlyph.setRSB"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setRSB</span></a> = setRSB<span class="argspec">(self, newRSB, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set the Right Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setAdvance"></a>

### `setAdvance`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setAdvance" href="#-typerig.proxy.objects.glyph.pGlyph.setAdvance"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setAdvance</span></a> = setAdvance<span class="argspec">(self, newAdvance, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set the Advance Width (int) at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setLSBeq"></a>

### `setLSBeq`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setLSBeq" href="#-typerig.proxy.objects.glyph.pGlyph.setLSBeq"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setLSBeq</span></a> = setLSBeq<span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set LSB metric equation on given layer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setRSBeq"></a>

### `setRSBeq`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setRSBeq" href="#-typerig.proxy.objects.glyph.pGlyph.setRSBeq"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setRSBeq</span></a> = setRSBeq<span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set RSB metric equation on given layer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.setADVeq"></a>

### `setADVeq`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.setADVeq" href="#-typerig.proxy.objects.glyph.pGlyph.setADVeq"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.setADVeq</span></a> = setADVeq<span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Set Advance width metric equation on given layer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.getSBeq"></a>

### `getSBeq`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.getSBeq" href="#-typerig.proxy.objects.glyph.pGlyph.getSBeq"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.getSBeq</span></a> = getSBeq<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">GET LSB, RSB metric equations on given layer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.fontMetricsInfo"></a>

### `fontMetricsInfo`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.fontMetricsInfo" href="#-typerig.proxy.objects.glyph.pGlyph.fontMetricsInfo"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.fontMetricsInfo</span></a> = fontMetricsInfo<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.anchors"></a>

### `anchors`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.anchors" href="#-typerig.proxy.objects.glyph.pGlyph.anchors"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.anchors</span></a> = anchors<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return list of anchors (list[flAnchor]) at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addAnchor"></a>

### `addAnchor`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addAnchor" href="#-typerig.proxy.objects.glyph.pGlyph.addAnchor"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addAnchor</span></a> = addAnchor<span class="argspec">(self, coordTuple, name, layer<span class="parameter-default">=None</span>, isAnchor<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds named Anchor at given layer.
Args:
        coordTuple (tuple(float,float)): Anchor coordinates X, Y
        name (str): Anchor name
        layer (int or str): Layer index or name. If None returns ActiveLayer
        isAnchor (bool): True creates a true flAnchor, False ? (flPinPoint)
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.newAnchor"></a>

### `newAnchor`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.newAnchor" href="#-typerig.proxy.objects.glyph.pGlyph.newAnchor"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.newAnchor</span></a> = newAnchor<span class="argspec">(self, coordTuple, name, anchorType<span class="parameter-default">=1</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Not working</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.clearAnchors"></a>

### `clearAnchors`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.clearAnchors" href="#-typerig.proxy.objects.glyph.pGlyph.clearAnchors"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.clearAnchors</span></a> = clearAnchors<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Remove all anchors at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.findAnchor"></a>

### `findAnchor`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.findAnchor" href="#-typerig.proxy.objects.glyph.pGlyph.findAnchor"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.findAnchor</span></a> = findAnchor<span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find anchor by name/tag</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.findAnchorCoords"></a>

### `findAnchorCoords`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.findAnchorCoords" href="#-typerig.proxy.objects.glyph.pGlyph.findAnchorCoords"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.findAnchorCoords</span></a> = findAnchorCoords<span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find anchor coordinates by name/tag</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.guidelines"></a>

### `guidelines`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.guidelines" href="#-typerig.proxy.objects.glyph.pGlyph.guidelines"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.guidelines</span></a> = guidelines<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return list of guidelines (list[flGuideline]) at given layer (int or str)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.addGuideline"></a>

### `addGuideline`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.addGuideline" href="#-typerig.proxy.objects.glyph.pGlyph.addGuideline"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.addGuideline</span></a> = addGuideline<span class="argspec">(self, coordTuple, layer<span class="parameter-default">=None</span>, angle<span class="parameter-default">=0</span>, name<span class="parameter-default">=''</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds named Guideline at given layer
Args:
        coordTuple (tuple(float,float) or tuple(float,float,float,float)): Guideline coordinates X, Y and given angle or two node reference x1,y1 and x2,y2
        name (str): Anchor name
        angle (float): Incline of the guideline
        layer (int or str): Layer index or name. If None returns ActiveLayer                    
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.draw"></a>

### `draw`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.draw" href="#-typerig.proxy.objects.glyph.pGlyph.draw"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.draw</span></a> = draw<span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.pGlyph.drawPoints"></a>

### `drawPoints`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.pGlyph.drawPoints" href="#-typerig.proxy.objects.glyph.pGlyph.drawPoints"><span class="function-name">typerig.proxy.objects.glyph.pGlyph.drawPoints</span></a> = drawPoints<span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#pGlyph">typerig.proxy.objects.glyph.pGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the PointPen protocol</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph"></a>

## `eGlyph`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.glyph.eGlyph</span> = <a name="typerig.proxy.objects.glyph.eGlyph" href="#typerig.proxy.objects.glyph.eGlyph">class eGlyph</a>(<a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Glyph, adding some advanced functionality

Constructor:
        pGlyph() - default represents the current glyph and current font
        pGlyph(fgFont, fgGlyph)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.glyph.html#eGlyph">eGlyph</a></dd><dd><a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eGlyph-bindCompMetrics" href="#eGlyph-bindCompMetrics"><span class="function-name">bindCompMetrics</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, bindIndex<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Auto bind metrics to the base composite glyph or to specified shape index</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-blendLayers" href="#eGlyph-blendLayers"><span class="function-name">blendLayers</span></a><span class="argspec">(self, layerA, layerB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two layers at given times (anisotropic support).
Args:
        layerA (flLayer), layerB (flLayer): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-breakContour" href="#eGlyph-breakContour"><span class="function-name">breakContour</span></a><span class="argspec">(self, contourId, nodeId, layer<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and layer. Extrapolate line endings if needed.
Args:
        contourId (int): Contour Index
        nodeId (int): Node Index
        layer (int or str): Layer index or name, works with both
        expand (float): Will extrapolate the line endings at that given value

Returns:
        flContour</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyADVbyName" href="#eGlyph-copyADVbyName"><span class="function-name">copyADVbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy Advance width from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyLSBbyName" href="#eGlyph-copyLSBbyName"><span class="function-name">copyLSBbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyMetricsbyName" href="#eGlyph-copyMetricsbyName"><span class="function-name">copyMetricsbyName</span></a><span class="argspec">(self, metricTriple<span class="parameter-default">=(None, None, None)</span>, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=(0, 0, 0)</span>, adjustPercent<span class="parameter-default">=(100, 100, 100)</span>, adjustUnits<span class="parameter-default">=(0, 0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB, RSB and Advance width from glyphs specified by Glyph Name.

Args:
        metricTriple tuple(str): Names of source glyphs for (LSB, RSB, ADV)
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order tuple(bool): Use source LSB (0 False) or RSB (1 True). Flips the metric copied. (LSB, RSB, 0)
        adjustPercent tuple(int): Adjust the copied metric by percent (100 default) - (LSB, RSB, ADV)
        adjustUnits tuple(int): Adjust the copied metric by units (0 default) - (LSB, RSB, ADV)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyRSBbyName" href="#eGlyph-copyRSBbyName"><span class="function-name">copyRSBbyName</span></a><span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copy RSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dropAnchor" href="#eGlyph-dropAnchor"><span class="function-name">dropAnchor</span></a><span class="argspec">(self, name, layer, coordTuple, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Drop anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dropGuide" href="#eGlyph-dropGuide"><span class="function-name">dropGuide</span></a><span class="argspec">(self, nodes<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, name<span class="parameter-default">='*DropGuideline'</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, flip<span class="parameter-default">=(1, 1)</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Build guideline trough *any two* given points or the *first two of the current selection*.

If *single point* is given will create a vertical guideline trough that point,
with guideline inclined according to the font's Italic Angle.

if process layers (pLayers) is None guideline will be created in all compatible layers,
otherwise the bool control tuple (active_layer (True or False), masters (True or False), masks (True or False), services (True or False)) is used. 
If all are set to False only the active layer is used.

Args:
        nodes (list(int)): List of node indexes
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        name (str): Name of the guideline to be build
        color (str): Color of the guideline according to QtCore colors
        style (str): Style of the guideline according to FontLab 6

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getAttachmentCenters" href="#eGlyph-getAttachmentCenters"><span class="function-name">getAttachmentCenters</span></a><span class="argspec">(self, layer, tolerance<span class="parameter-default">=5</span>, applyTransform<span class="parameter-default">=True</span>, getAll<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return X center of lowest, highest Y of [glyph] for [layer] within given [tolerance]
Note: Determine diacritic to glyph attachment positions (for anchor placement)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getNewBaseCoords" href="#eGlyph-getNewBaseCoords"><span class="function-name">getNewBaseCoords</span></a><span class="argspec">(self, layer, adjustTuple, alignTuple, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>, initPosTuple<span class="parameter-default">=(0.0, 0.0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Calculate Anchor base position
Args:
        layer (int or str): Layer index or name, works with both
        coordTuple (int/float, int/float): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int/float): Outline feature auto detection tolerance*
        initPosTuple (int/float, int/float): Itinital anchor position

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        x, y (int/float)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-lerpLayerFg" href="#eGlyph-lerpLayerFg"><span class="function-name">lerpLayerFg</span></a><span class="argspec">(self, l0_Name, l1_Name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-moveAnchor" href="#eGlyph-moveAnchor"><span class="function-name">moveAnchor</span></a><span class="argspec">(self, name, layer, coordTuple<span class="parameter-default">=(0, 0)</span>, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Move anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-reorder_shapes" href="#eGlyph-reorder_shapes"><span class="function-name">reorder_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mode<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Auto reorder shapes on given layer using criteria.
Args:
        layer (int or str): Layer index or name, works with both
        mode (bool, bool): Mode of shape reordering/sorting by (X, Y)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setStart" href="#eGlyph-setStart"><span class="function-name">setStart</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, control<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-splitContour" href="#eGlyph-splitContour"><span class="function-name">splitContour</span></a><span class="argspec">(self, scnPairs<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>, close<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and combinations of compatible layers. Extrapolate line endings and close contour if needed.

Args:
        scnPairs (list(tuple)): Shape-contour-node pairs for the selected nodes [(Shape Index, Contour Index, Node Index)..()]
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        expand (float): Will extrapolate the line endings at that given value
        close (bool): True = Close contour 

Return:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-ungroup_all_shapes" href="#eGlyph-ungroup_all_shapes"><span class="function-name">ungroup_all_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, applyTransform<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Ungroup all shapes at given layer.
Args:
        layer (int or str): Layer index or name, works with both
        applyTransform (bool): Apply transformation at shape.

Returns:
        None</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></h4><dl class="function"><dt><a name="eGlyph-__init__" href="#eGlyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-__repr__" href="#eGlyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-activeGuides" href="#eGlyph-activeGuides"><span class="function-name">activeGuides</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-activeLayer" href="#eGlyph-activeLayer"><span class="function-name">activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addAnchor" href="#eGlyph-addAnchor"><span class="function-name">addAnchor</span></a><span class="argspec">(self, coordTuple, name, layer<span class="parameter-default">=None</span>, isAnchor<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Anchor at given layer.
Args:
        coordTuple (tuple(float,float)): Anchor coordinates X, Y
        name (str): Anchor name
        layer (int or str): Layer index or name. If None returns ActiveLayer
        isAnchor (bool): True creates a true flAnchor, False ? (flPinPoint)
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addComponents" href="#eGlyph-addComponents"><span class="function-name">addComponents</span></a><span class="argspec">(self, componentConfig, layer<span class="parameter-default">=None</span>, useAnchors<span class="parameter-default">=True</span>, colorize<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a components to given glyph layer.
Args:
        componentConfig (list(tuple(glyph_name (str), glyph_transform (QTransform), layer_pointer (str)))): List contianign component configuration.  
        layer (int or str): Layer index or name. If None returns ActiveLayer
        useAnchors (bool): Compose using anchors
        colorize (bool): Flag new glyphs
Returns:
        list(flShapes): List of components added</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addGuideline" href="#eGlyph-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, coordTuple, layer<span class="parameter-default">=None</span>, angle<span class="parameter-default">=0</span>, name<span class="parameter-default">=''</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds named Guideline at given layer
Args:
        coordTuple (tuple(float,float) or tuple(float,float,float,float)): Guideline coordinates X, Y and given angle or two node reference x1,y1 and x2,y2
        name (str): Anchor name
        angle (float): Incline of the guideline
        layer (int or str): Layer index or name. If None returns ActiveLayer                    
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addLayer" href="#eGlyph-addLayer"><span class="function-name">addLayer</span></a><span class="argspec">(self, layer, toBack<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a layer to glyph.
Args:
        layer (flLayer or fgLayer)
        toBack (bool): Send layer to back
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addShape" href="#eGlyph-addShape"><span class="function-name">addShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, clone<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape at given layer.
Args:
        shape (flShape): Shape to be added
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-addShapeContainer" href="#eGlyph-addShapeContainer"><span class="function-name">addShapeContainer</span></a><span class="argspec">(self, shapeList, layer<span class="parameter-default">=None</span>, remove<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Add a new shape container* at given layer.
A flShape containing all of the shapes given that
could be transformed to Shape-group or shape-filter.
Args:
        shapeList list(flShape): List if Shapes to be grouped.
Returns:
        flShape</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-anchors" href="#eGlyph-anchors"><span class="function-name">anchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of anchors (list[flAnchor]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-blendShapes" href="#eGlyph-blendShapes"><span class="function-name">blendShapes</span></a><span class="argspec">(self, shapeA, shapeB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Blend two shapes at given times (anisotropic support).
Args:
        shapeA (flShape), shapeB (flShape): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        Native (interpolation engine dependent) or flShape (default)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-clearAnchors" href="#eGlyph-clearAnchors"><span class="function-name">clearAnchors</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all anchors at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-components" href="#eGlyph-components"><span class="function-name">components</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph components besides glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-containers" href="#eGlyph-containers"><span class="function-name">containers</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-contours" href="#eGlyph-contours"><span class="function-name">contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=True</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-copyLayer" href="#eGlyph-copyLayer"><span class="function-name">copyLayer</span></a><span class="argspec">(self, srcLayerName, dstLayerName, options<span class="parameter-default">={'adv': True, 'anc': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True}</span>, addLayer<span class="parameter-default">=False</span>, cleanDST<span class="parameter-default">=True</span>, toBack<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Copies a layer within the glyph.
Args:
        srcLayerName, dstLayerName (string): Source and destination layer names
        options (dict): Copy Options as follows {'out': Outline, 'gui': Guidelines, 'anc': Anchors, 'lsb': LSB, 'adv': Advance, 'rsb': RSB, 'lnk': Linked metrics, 'ref': References}, addLayer=False):
        addLayer (bool): Create a new layer
        cleanDST (bool): Clean destination layer
        toBack (bool): Add layer to back of the layer stack
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-decompose" href="#eGlyph-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decompose all complex shapes that contain other shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-dereference" href="#eGlyph-dereference"><span class="function-name">dereference</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove all shape references but leave components.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-draw" href="#eGlyph-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-drawPoints" href="#eGlyph-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(self, pen, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the PointPen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-duplicateLayer" href="#eGlyph-duplicateLayer"><span class="function-name">duplicateLayer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, newLayerName<span class="parameter-default">='New Layer'</span>, references<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a layer with new name and adds it to glyph's layers.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        toBack(bool): send to back
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-elements" href="#eGlyph-elements"><span class="function-name">elements</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph elements in glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_activeLayer" href="#eGlyph-fg_activeLayer"><span class="function-name">fg_activeLayer</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_contours" href="#eGlyph-fg_contours"><span class="function-name">fg_contours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate contours at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgContours]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_hasLayer" href="#eGlyph-fg_hasLayer"><span class="function-name">fg_hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_layer" href="#eGlyph-fg_layer"><span class="function-name">fg_layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns FontGate layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        fgLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_layers" href="#eGlyph-fg_layers"><span class="function-name">fg_layers</span></a><span class="argspec">(self, asDict<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FotnGate layers</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_nodes" href="#eGlyph-fg_nodes"><span class="function-name">fg_nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fg_shapes" href="#eGlyph-fg_shapes"><span class="function-name">fg_shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all FontGate shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[fgShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findAnchor" href="#eGlyph-findAnchor"><span class="function-name">findAnchor</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findAnchorCoords" href="#eGlyph-findAnchorCoords"><span class="function-name">findAnchorCoords</span></a><span class="argspec">(self, anchorName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find anchor coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findNode" href="#eGlyph-findNode"><span class="function-name">findNode</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findNodeCoords" href="#eGlyph-findNodeCoords"><span class="function-name">findNodeCoords</span></a><span class="argspec">(self, nodeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find node coordinates by name/tag</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-findShape" href="#eGlyph-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds shape by name on given layer
Args:
        shapeName (str): Shape name
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flShape or None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-fontMetricsInfo" href="#eGlyph-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getAdvance" href="#eGlyph-getAdvance"><span class="function-name">getAdvance</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Advance Width at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getBounds" href="#eGlyph-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Glyph's Boundig Box at given layer (int or str). Returns QRectF.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getBuilders" href="#eGlyph-getBuilders"><span class="function-name">getBuilders</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, store<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getCompositionDict" href="#eGlyph-getCompositionDict"><span class="function-name">getCompositionDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return composition dict of a glyph. Elements!</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getCompositionNames" href="#eGlyph-getCompositionNames"><span class="function-name">getCompositionNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return name of glyph and the parts it is made of.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getElementNames" href="#eGlyph-getElementNames"><span class="function-name">getElementNames</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return names of elements references used in glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getLSB" href="#eGlyph-getLSB"><span class="function-name">getLSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Left Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getRSB" href="#eGlyph-getRSB"><span class="function-name">getRSB</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get the Right Side-bearing at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getSBeq" href="#eGlyph-getSBeq"><span class="function-name">getSBeq</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">GET LSB, RSB metric equations on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getSegment" href="#eGlyph-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns contour segment of the node specified at given layer
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        CurveEx</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-getTags" href="#eGlyph-getTags"><span class="function-name">getTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Tags -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-guidelines" href="#eGlyph-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of guidelines (list[flGuideline]) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-hasLayer" href="#eGlyph-hasLayer"><span class="function-name">hasLayer</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-insertNodeAt" href="#eGlyph-insertNodeAt"><span class="function-name">insertNodeAt</span></a><span class="argspec">(self, cID, nID_time, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts node in contour at specified layer
Arg:
        cID (int): Contour Index
        nID_time (float): Node index + float time
        layer (int or str): Layer index or name. If None returns ActiveLayer

!NOTE: FL6 treats contour insertions (as well as nodes) as float times along contour,
so inserting a node at .5 t between nodes with indexes 3 and 4 will be 3 (index) + 0.5 (time) = 3.5</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-insertNodesAt" href="#eGlyph-insertNodesAt"><span class="function-name">insertNodesAt</span></a><span class="argspec">(self, cID, nID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Inserts a list of nodes to specified contour, starting at given index all on layer specified.
Args:
        cID (int): Contour index
        nID (int): Node of insertion index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-isCompatible" href="#eGlyph-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph is ready for interpolation - all master layers are compatible.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-isMixedReference" href="#eGlyph-isMixedReference"><span class="function-name">isMixedReference</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Test if glyph has mixed references - components on some layers and referenced shapes on others</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-italicAngle" href="#eGlyph-italicAngle"><span class="function-name">italicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-layer" href="#eGlyph-layer"><span class="function-name">layer</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns layer no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        flLayer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-layers" href="#eGlyph-layers"><span class="function-name">layers</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return all layers</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mLine" href="#eGlyph-mLine"><span class="function-name">mLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mapNodes2Times" href="#eGlyph-mapNodes2Times"><span class="function-name">mapNodes2Times</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Nodes at contour times for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Contour Time (int): Node Index (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mapTimes2Nodes" href="#eGlyph-mapTimes2Nodes"><span class="function-name">mapTimes2Nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Create map of Contour times at node indexes for every contour in given layer
Returns:
        dict{Contour index (int) : dict{Node Index (int) : Contour Time (int) }}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-mask" href="#eGlyph-mask"><span class="function-name">mask</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-masks" href="#eGlyph-masks"><span class="function-name">masks</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all mask layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-masters" href="#eGlyph-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all master layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-newAnchor" href="#eGlyph-newAnchor"><span class="function-name">newAnchor</span></a><span class="argspec">(self, coordTuple, name, anchorType<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Not working</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodes" href="#eGlyph-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all nodes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer.
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNodes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodes4segments" href="#eGlyph-nodes4segments"><span class="function-name">nodes4segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments and their corresponding nodes at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        dict{time(int):(CurveEx, list[flNode]}</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-nodesForIndices" href="#eGlyph-nodesForIndices"><span class="function-name">nodesForIndices</span></a><span class="argspec">(self, indices, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-noncomplex" href="#eGlyph-noncomplex"><span class="function-name">noncomplex</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all glyph shapes that are not glyph references or components</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-object" href="#eGlyph-object"><span class="function-name">object</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeLayer" href="#eGlyph-removeLayer"><span class="function-name">removeLayer</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Removes a layer from glyph.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeNodeAt" href="#eGlyph-removeNodeAt"><span class="function-name">removeNodeAt</span></a><span class="argspec">(self, cID, nID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a node from contour at layer specified.
Args:
        cID (int): Contour index
        nID (int): Index of Node to be removed
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeNodes" href="#eGlyph-removeNodes"><span class="function-name">removeNodes</span></a><span class="argspec">(self, cID, nodeList, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Removes a list of nodes from contour at layer specified.
Args:
        cID (int): Contour index
        nodeList (list): List of flNode objects
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-removeShape" href="#eGlyph-removeShape"><span class="function-name">removeShape</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, recursive<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a new shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
        recursive (bool): 
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-replaceShape" href="#eGlyph-replaceShape"><span class="function-name">replaceShape</span></a><span class="argspec">(self, old_shape, new_shape, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Repalce a shape at given layer.
Args:
        old_shape, new_shape (flShape): Shapes
        layer (str): Layer name
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-reportLayerComp" href="#eGlyph-reportLayerComp"><span class="function-name">reportLayerComp</span></a><span class="argspec">(self, strong<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns a layer compatibility report</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-rotate" href="#eGlyph-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rotate outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-scale" href="#eGlyph-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Scale outline at given layer.
Args:
        sx (float), sy (float): delta (scaling) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-segments" href="#eGlyph-segments"><span class="function-name">segments</span></a><span class="argspec">(self, cID, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all contour segments at given layer
Args:
        cID (int): Contour index
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selected" href="#eGlyph-selected"><span class="function-name">selected</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes indexes at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedAtContours" href="#eGlyph-selectedAtContours"><span class="function-name">selectedAtContours</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the contours they rest upon at current layer.
Args:
        index (bool): If True returns only indexes, False returns flContour, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(contourID, nodeID)..()] or 
        list[tuple(flContour, flNode)]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedAtShapes" href="#eGlyph-selectedAtShapes"><span class="function-name">selectedAtShapes</span></a><span class="argspec">(self, index<span class="parameter-default">=True</span>, filterOn<span class="parameter-default">=False</span>, layer<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes and the shapes they belong at current layer.
Args:
        index (bool): If True returns only indexes, False returns flShape, flNode
        filterOn (bool): Return only on-curve nodes
Returns:
        list[tuple(int, int)]: [(shapeID, nodeID)..()] or
        list[tuple(flShape, flNode)]

!TODO: Make it working with layers as <a href="#typerig.proxy.objects.glyph.eGlyph-selectedAtContours">selectedAtContours</a>(). This is legacy mode so other scripts would work!</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedContours" href="#eGlyph-selectedContours"><span class="function-name">selectedContours</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, allNodesSelected<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedCoords" href="#eGlyph-selectedCoords"><span class="function-name">selectedCoords</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, applyTransform<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the coordinates of all selected nodes at the current layer or other.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
        filterOn (bool): Return only on-curve nodes
        applyTransform (bool) : Gets local shape transformation matrix and applies it to the node coordinates
Returns:
        list[QPointF]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodeIndices" href="#eGlyph-selectedNodeIndices"><span class="function-name">selectedNodeIndices</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        filterOn (bool): Return only on-curve nodes
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodes" href="#eGlyph-selectedNodes"><span class="function-name">selectedNodes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, filterOn<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all selected nodes at given layer.
Args:
        filterOn (bool): Return only on-curve nodes
        extend (class): A class construct with extended functionality to be applied on every node.
Returns:
        list[flNode]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedNodesOnCanvas" href="#eGlyph-selectedNodesOnCanvas"><span class="function-name">selectedNodesOnCanvas</span></a><span class="argspec">(self, filterOn<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Glyph Selection -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedSegments" href="#eGlyph-selectedSegments"><span class="function-name">selectedSegments</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns list of currently selected segments
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[CurveEx]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedShapeIndices" href="#eGlyph-selectedShapeIndices"><span class="function-name">selectedShapeIndices</span></a><span class="argspec">(self, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all indices of nodes selected at current layer.
Args:
        select_all (bool): True all nodes on Shape should be selected. False any node will do.
Returns:
        list[int]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-selectedShapes" href="#eGlyph-selectedShapes"><span class="function-name">selectedShapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, select_all<span class="parameter-default">=False</span>, deep<span class="parameter-default">=False</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes that have a node selected.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-services" href="#eGlyph-services"><span class="function-name">services</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns all service layers.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setADVeq" href="#eGlyph-setADVeq"><span class="function-name">setADVeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set Advance width metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setAdvance" href="#eGlyph-setAdvance"><span class="function-name">setAdvance</span></a><span class="argspec">(self, newAdvance, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Advance Width (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setLSB" href="#eGlyph-setLSB"><span class="function-name">setLSB</span></a><span class="argspec">(self, newLSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Left Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setLSBeq" href="#eGlyph-setLSBeq"><span class="function-name">setLSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set LSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setMark" href="#eGlyph-setMark"><span class="function-name">setMark</span></a><span class="argspec">(self, mark_color, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setName" href="#eGlyph-setName"><span class="function-name">setName</span></a><span class="argspec">(self, glyph_name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setRSB" href="#eGlyph-setRSB"><span class="function-name">setRSB</span></a><span class="argspec">(self, newRSB, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set the Right Side-bearing (int) at given layer (int or str)</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setRSBeq" href="#eGlyph-setRSBeq"><span class="function-name">setRSBeq</span></a><span class="argspec">(self, equationStr, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Set RSB metric equation on given layer</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-setTags" href="#eGlyph-setTags"><span class="function-name">setTags</span></a><span class="argspec">(self, tagList, append<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-shapes" href="#eGlyph-shapes"><span class="function-name">shapes</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all shapes at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapes]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-shapes_data" href="#eGlyph-shapes_data"><span class="function-name">shapes_data</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return all flShapeData objects at given layer.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        list[flShapeData]</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-slant" href="#eGlyph-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Slant outline at given layer.
Args:
        deg (float): degrees of slant
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-tag" href="#eGlyph-tag"><span class="function-name">tag</span></a><span class="argspec">(self, newTag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-translate" href="#eGlyph-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Translate (shift) outline at given layer.
Args:
        dx (float), dy (float): delta (shift) X, Y
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-update" href="#eGlyph-update"><span class="function-name">update</span></a><span class="argspec">(self, fl<span class="parameter-default">=True</span>, fg<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates the glyph and sends notification to the editor.
Args:
        fl (bool): Update the flGlyph
        fg (bool): Update the fgGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-updateObject" href="#eGlyph-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="eGlyph-version" href="#eGlyph-version"><span class="function-name">version</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.glyph.html#pGlyph">pGlyph</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
</dl>
<dl class="descriptor"><dt>index</dt>
</dl>
<dl class="descriptor"><dt>mark</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>package</dt>
</dl>
<dl class="descriptor"><dt>tags</dt>
</dl>
<dl class="descriptor"><dt>unicode</dt>
</dl>
<dl class="descriptor"><dt>unicodes</dt>
</dl>
</dd>


<a name="typerig.proxy.objects.glyph.eGlyph.breakContour"></a>

### `breakContour`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.breakContour" href="#-typerig.proxy.objects.glyph.eGlyph.breakContour"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.breakContour</span></a> = breakContour<span class="argspec">(self, contourId, nodeId, layer<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and layer. Extrapolate line endings if needed.
Args:
        contourId (int): Contour Index
        nodeId (int): Node Index
        layer (int or str): Layer index or name, works with both
        expand (float): Will extrapolate the line endings at that given value

Returns:
        flContour</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.splitContour"></a>

### `splitContour`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.splitContour" href="#-typerig.proxy.objects.glyph.eGlyph.splitContour"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.splitContour</span></a> = splitContour<span class="argspec">(self, scnPairs<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, expand<span class="parameter-default">=0</span>, close<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Split Contour at given node and combinations of compatible layers. Extrapolate line endings and close contour if needed.

Args:
        scnPairs (list(tuple)): Shape-contour-node pairs for the selected nodes [(Shape Index, Contour Index, Node Index)..()]
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        expand (float): Will extrapolate the line endings at that given value
        close (bool): True = Close contour 

Return:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.dropGuide"></a>

### `dropGuide`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.dropGuide" href="#-typerig.proxy.objects.glyph.eGlyph.dropGuide"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.dropGuide</span></a> = dropGuide<span class="argspec">(self, nodes<span class="parameter-default">=None</span>, layers<span class="parameter-default">=None</span>, name<span class="parameter-default">='*DropGuideline'</span>, tag<span class="parameter-default">=''</span>, color<span class="parameter-default">='darkMagenta'</span>, flip<span class="parameter-default">=(1, 1)</span>, style<span class="parameter-default">='gsGlyphGuideline'</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Build guideline trough *any two* given points or the *first two of the current selection*.

If *single point* is given will create a vertical guideline trough that point,
with guideline inclined according to the font's Italic Angle.

if process layers (pLayers) is None guideline will be created in all compatible layers,
otherwise the bool control tuple (active_layer (True or False), masters (True or False), masks (True or False), services (True or False)) is used. 
If all are set to False only the active layer is used.

Args:
        nodes (list(int)): List of node indexes
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        name (str): Name of the guideline to be build
        color (str): Color of the guideline according to QtCore colors
        style (str): Style of the guideline according to FontLab 6

Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.copyLSBbyName"></a>

### `copyLSBbyName`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.copyLSBbyName" href="#-typerig.proxy.objects.glyph.eGlyph.copyLSBbyName"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.copyLSBbyName</span></a> = copyLSBbyName<span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.copyRSBbyName"></a>

### `copyRSBbyName`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.copyRSBbyName" href="#-typerig.proxy.objects.glyph.eGlyph.copyRSBbyName"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.copyRSBbyName</span></a> = copyRSBbyName<span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=0</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Copy RSB from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order (bool or int): Use source LSB (0 False) or RSB (1 True). Flips the metric copied.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.copyADVbyName"></a>

### `copyADVbyName`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.copyADVbyName" href="#-typerig.proxy.objects.glyph.eGlyph.copyADVbyName"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.copyADVbyName</span></a> = copyADVbyName<span class="argspec">(self, glyphName, layers<span class="parameter-default">=None</span>, adjustPercent<span class="parameter-default">=100</span>, adjustUnits<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Copy Advance width from another glyph specified by Glyph Name.

Args:
        glyphName (str): Name of source glyph
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        adjustPercent (int): Adjust the copied metric by percent (100 default)
        adjustUnits (int): Adjust the copied metric by units (0 default)

Return:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.copyMetricsbyName"></a>

### `copyMetricsbyName`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.copyMetricsbyName" href="#-typerig.proxy.objects.glyph.eGlyph.copyMetricsbyName"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.copyMetricsbyName</span></a> = copyMetricsbyName<span class="argspec">(self, metricTriple<span class="parameter-default">=(None, None, None)</span>, layers<span class="parameter-default">=None</span>, order<span class="parameter-default">=(0, 0, 0)</span>, adjustPercent<span class="parameter-default">=(100, 100, 100)</span>, adjustUnits<span class="parameter-default">=(0, 0, 0)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Copy LSB, RSB and Advance width from glyphs specified by Glyph Name.

Args:
        metricTriple tuple(str): Names of source glyphs for (LSB, RSB, ADV)
        layers tuple(bool): Bool control tuple(active_layer, masters, masks, services). Note If all are set to False only the active layer is used.
        order tuple(bool): Use source LSB (0 False) or RSB (1 True). Flips the metric copied. (LSB, RSB, 0)
        adjustPercent tuple(int): Adjust the copied metric by percent (100 default) - (LSB, RSB, ADV)
        adjustUnits tuple(int): Adjust the copied metric by units (0 default) - (LSB, RSB, ADV)

Return:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.bindCompMetrics"></a>

### `bindCompMetrics`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.bindCompMetrics" href="#-typerig.proxy.objects.glyph.eGlyph.bindCompMetrics"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.bindCompMetrics</span></a> = bindCompMetrics<span class="argspec">(self, layer<span class="parameter-default">=None</span>, bindIndex<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Auto bind metrics to the base composite glyph or to specified shape index</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.blendLayers"></a>

### `blendLayers`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.blendLayers" href="#-typerig.proxy.objects.glyph.eGlyph.blendLayers"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.blendLayers</span></a> = blendLayers<span class="argspec">(self, layerA, layerB, blendTimes, outputFL<span class="parameter-default">=True</span>, blendMode<span class="parameter-default">=0</span>, engine<span class="parameter-default">='fg'</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Blend two layers at given times (anisotropic support).
Args:
        layerA (flLayer), layerB (flLayer): Shapes to be interpolated
        blendTimes (int or float or tuple(float, float)): (int) for percent 0%-100% or (float) time for both X,Y or tuple(float,float) times for anisotropic blending
        outputFL (bool): Return blend native format or flShape (default)
        blendMode (int): ?
        engine (str): 'fg' for FontGate (in-build).

Returns:
        flLayer</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.getAttachmentCenters"></a>

### `getAttachmentCenters`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.getAttachmentCenters" href="#-typerig.proxy.objects.glyph.eGlyph.getAttachmentCenters"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.getAttachmentCenters</span></a> = getAttachmentCenters<span class="argspec">(self, layer, tolerance<span class="parameter-default">=5</span>, applyTransform<span class="parameter-default">=True</span>, getAll<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return X center of lowest, highest Y of [glyph] for [layer] within given [tolerance]
Note: Determine diacritic to glyph attachment positions (for anchor placement)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.getNewBaseCoords"></a>

### `getNewBaseCoords`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.getNewBaseCoords" href="#-typerig.proxy.objects.glyph.eGlyph.getNewBaseCoords"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.getNewBaseCoords</span></a> = getNewBaseCoords<span class="argspec">(self, layer, adjustTuple, alignTuple, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>, initPosTuple<span class="parameter-default">=(0.0, 0.0)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Calculate Anchor base position
Args:
        layer (int or str): Layer index or name, works with both
        coordTuple (int/float, int/float): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int/float): Outline feature auto detection tolerance*
        initPosTuple (int/float, int/float): Itinital anchor position

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        x, y (int/float)</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.dropAnchor"></a>

### `dropAnchor`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.dropAnchor" href="#-typerig.proxy.objects.glyph.eGlyph.dropAnchor"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.dropAnchor</span></a> = dropAnchor<span class="argspec">(self, name, layer, coordTuple, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Drop anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.moveAnchor"></a>

### `moveAnchor`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.moveAnchor" href="#-typerig.proxy.objects.glyph.eGlyph.moveAnchor"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.moveAnchor</span></a> = moveAnchor<span class="argspec">(self, name, layer, coordTuple<span class="parameter-default">=(0, 0)</span>, alignTuple<span class="parameter-default">=(None, None)</span>, tolerance<span class="parameter-default">=5</span>, italic<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Move anchor at given layer
Args:
        name (str): Anchor Name
        layer (int or str): Layer index or name, works with both
        coordTuple (int, int): New anchor coordinates or auto aligment offsets*
        alignTuple (str,str): New anchor aligment*
        tolerance (int): Outline feature auto detection tolerance*

*Aligment rules: (width, height)
        - (None,None) - Uses coordinates given
        - width - (L) Left; (R) Right; (A) Auto Bottom with tolerance; (AT) Auto Top with tolerance; (C) Center;
        - height - (T) Top; (B) Bottom; (C) Center;
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.reorder_shapes"></a>

### `reorder_shapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.reorder_shapes" href="#-typerig.proxy.objects.glyph.eGlyph.reorder_shapes"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.reorder_shapes</span></a> = reorder_shapes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, mode<span class="parameter-default">=(0, 0)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Auto reorder shapes on given layer using criteria.
Args:
        layer (int or str): Layer index or name, works with both
        mode (bool, bool): Mode of shape reordering/sorting by (X, Y)

Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.glyph.eGlyph.ungroup_all_shapes"></a>

### `ungroup_all_shapes`


<dl class="function"><dt><a name="-typerig.proxy.objects.glyph.eGlyph.ungroup_all_shapes" href="#-typerig.proxy.objects.glyph.eGlyph.ungroup_all_shapes"><span class="function-name">typerig.proxy.objects.glyph.eGlyph.ungroup_all_shapes</span></a> = ungroup_all_shapes<span class="argspec">(self, layer<span class="parameter-default">=None</span>, applyTransform<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.glyph.html#eGlyph">typerig.proxy.objects.glyph.eGlyph</a> method</span></dt><dd>

<pre class="doc" markdown="0">Ungroup all shapes at given layer.
Args:
        layer (int or str): Layer index or name, works with both
        applyTransform (bool): Apply transformation at shape.

Returns:
        None</pre>

</dd></dl>

