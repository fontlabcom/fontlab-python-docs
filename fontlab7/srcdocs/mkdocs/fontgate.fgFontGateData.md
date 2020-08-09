

<a name="fontgate.fgFontGateData"></a>

# `fgFontGateData`


<dt class="class"><h2><span class="class-name">fontgate.fgFontGateData</span> = <a name="fontgate.fgFontGateData" href="#fontgate.fgFontGateData">class fgFontGateData</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">FontGateData representation

Constructors:
  fgFontGateData() - default
  fgFontGateData(fgFontGateData) - copy</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgFontGateData-OK" href="#fgFontGateData-OK"><span class="function-name">OK</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-OK">OK</a>() - return true if status is gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__cmp__" href="#fgFontGateData-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__delattr__" href="#fgFontGateData-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__getattribute__" href="#fgFontGateData-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__init__" href="#fgFontGateData-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__repr__" href="#fgFontGateData-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__setattr__" href="#fgFontGateData-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-__str__" href="#fgFontGateData-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontGateData-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-activeLayer" href="#fgFontGateData-activeLayer"><span class="function-name">activeLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer <a href="#fontgate.fgFontGateData-activeLayer">activeLayer</a>() - get active layer or Nothing if no layers exists</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-addContour" href="#fgFontGateData-addContour"><span class="function-name">addContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour <a href="#fontgate.fgFontGateData-addContour">addContour</a>(fgContour) - add contour into 'Body' layer</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-addShape" href="#fgFontGateData-addShape"><span class="function-name">addShape</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgShape <a href="#fontgate.fgFontGateData-addShape">addShape</a>(fgShape) - add shape into 'Body' layer</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-bad" href="#fgFontGateData-bad"><span class="function-name">bad</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-bad">bad</a>() - return true if status isn't gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-bodyLayer" href="#fgFontGateData-bodyLayer"><span class="function-name">bodyLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer <a href="#fontgate.fgFontGateData-bodyLayer">bodyLayer</a>() - get layer named 'Body', any existing non-service layer if not found or Nothing if no layers exists</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-bodyLayerStrict" href="#fgFontGateData-bodyLayerStrict"><span class="function-name">bodyLayerStrict</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer <a href="#fontgate.fgFontGateData-bodyLayerStrict">bodyLayerStrict</a>() - get layer named 'Body'. if it's not present, create it on the fly</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-boundingBox" href="#fgFontGateData-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgFontGateData-boundingBox">boundingBox</a>(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-checkContours" href="#fgFontGateData-checkContours"><span class="function-name">checkContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontGateData-checkContours">checkContours</a>() - ckeck for multi-segment contours and split it into one segment's contours</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-copy" href="#fgFontGateData-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontgate.fgFontGateData-copy">copy</a>() - create alone copy of data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-countNodesContours" href="#fgFontGateData-countNodesContours"><span class="function-name">countNodesContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(nodesCount, contoursCount) <a href="#fontgate.fgFontGateData-countNodesContours">countNodesContours</a>() - calculate stats for 'Body' layer if it present, return (0,0) otherwise</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-countPictures" href="#fgFontGateData-countPictures"><span class="function-name">countPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgFontGateData-countPictures">countPictures</a>() - return pictures count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-countShapes" href="#fgFontGateData-countShapes"><span class="function-name">countShapes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgFontGateData-countShapes">countShapes</a>() - return shapes count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-findLayer" href="#fgFontGateData-findLayer"><span class="function-name">findLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer <a href="#fontgate.fgFontGateData-findLayer">findLayer</a>('name') - get layer by name, return Nothing if no layer found</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-getFontGateData" href="#fgFontGateData-getFontGateData"><span class="function-name">getFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontgate.fgFontGateData-getFontGateData">getFontGateData</a>() - return self</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-getType" href="#fgFontGateData-getType"><span class="function-name">getType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontgate.fgFontGateData-getType">getType</a>() - return 'dtFontGate'</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-hasBody" href="#fgFontGateData-hasBody"><span class="function-name">hasBody</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-hasBody">hasBody</a>(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-hasColors" href="#fgFontGateData-hasColors"><span class="function-name">hasColors</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-hasColors">hasColors</a>() - return true if colors is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-hasHints" href="#fgFontGateData-hasHints"><span class="function-name">hasHints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-hasHints">hasHints</a>() - return true if hints is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-hasPictures" href="#fgFontGateData-hasPictures"><span class="function-name">hasPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-hasPictures">hasPictures</a>() - return true if pictures is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-maskLayer" href="#fgFontGateData-maskLayer"><span class="function-name">maskLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer <a href="#fontgate.fgFontGateData-maskLayer">maskLayer</a>(bool createIfMissing)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-modified" href="#fgFontGateData-modified"><span class="function-name">modified</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgFontGateData-modified">modified</a>() - return true if data was changed</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-resetBbox" href="#fgFontGateData-resetBbox"><span class="function-name">resetBbox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontGateData-resetBbox">resetBbox</a>() - reset bbox cache</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-setParent" href="#fgFontGateData-setParent"><span class="function-name">setParent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontGateData-setParent">setParent</a>(fgGlyph) - set parent glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-status" href="#fgFontGateData-status"><span class="function-name">status</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' <a href="#fontgate.fgFontGateData-status">status</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-transform" href="#fgFontGateData-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontGateData-transform">transform</a>(fgMatrix) - transform data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontGateData-updated" href="#fgFontGateData-updated"><span class="function-name">updated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontGateData-updated">updated</a>() - mark data as changed, reset internal caches</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>layers</dt>
<dd>

<pre class="doc" markdown="0">(fgLayers) layers list</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgFontGateData-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgFontGateData.activeLayer"></a>

## `activeLayer`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.activeLayer" href="#-fontgate.fgFontGateData.activeLayer"><span class="function-name">fontgate.fgFontGateData.activeLayer</span></a> = activeLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer activeLayer() - get active layer or Nothing if no layers exists</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.addContour"></a>

## `addContour`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.addContour" href="#-fontgate.fgFontGateData.addContour"><span class="function-name">fontgate.fgFontGateData.addContour</span></a> = addContour<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour addContour(fgContour) - add contour into 'Body' layer</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.addShape"></a>

## `addShape`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.addShape" href="#-fontgate.fgFontGateData.addShape"><span class="function-name">fontgate.fgFontGateData.addShape</span></a> = addShape<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgShape addShape(fgShape) - add shape into 'Body' layer</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.bad"></a>

## `bad`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.bad" href="#-fontgate.fgFontGateData.bad"><span class="function-name">fontgate.fgFontGateData.bad</span></a> = bad<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool bad() - return true if status isn't gdsOK</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.bodyLayer"></a>

## `bodyLayer`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.bodyLayer" href="#-fontgate.fgFontGateData.bodyLayer"><span class="function-name">fontgate.fgFontGateData.bodyLayer</span></a> = bodyLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer bodyLayer() - get layer named 'Body', any existing non-service layer if not found or Nothing if no layers exists</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.bodyLayerStrict"></a>

## `bodyLayerStrict`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.bodyLayerStrict" href="#-fontgate.fgFontGateData.bodyLayerStrict"><span class="function-name">fontgate.fgFontGateData.bodyLayerStrict</span></a> = bodyLayerStrict<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer bodyLayerStrict() - get layer named 'Body'. if it's not present, create it on the fly</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.boundingBox" href="#-fontgate.fgFontGateData.boundingBox"><span class="function-name">fontgate.fgFontGateData.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.checkContours"></a>

## `checkContours`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.checkContours" href="#-fontgate.fgFontGateData.checkContours"><span class="function-name">fontgate.fgFontGateData.checkContours</span></a> = checkContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkContours() - ckeck for multi-segment contours and split it into one segment's contours</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.copy" href="#-fontgate.fgFontGateData.copy"><span class="function-name">fontgate.fgFontGateData.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData copy() - create alone copy of data</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.countNodesContours"></a>

## `countNodesContours`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.countNodesContours" href="#-fontgate.fgFontGateData.countNodesContours"><span class="function-name">fontgate.fgFontGateData.countNodesContours</span></a> = countNodesContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(nodesCount, contoursCount) countNodesContours() - calculate stats for 'Body' layer if it present, return (0,0) otherwise</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.countPictures"></a>

## `countPictures`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.countPictures" href="#-fontgate.fgFontGateData.countPictures"><span class="function-name">fontgate.fgFontGateData.countPictures</span></a> = countPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countPictures() - return pictures count</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.countShapes"></a>

## `countShapes`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.countShapes" href="#-fontgate.fgFontGateData.countShapes"><span class="function-name">fontgate.fgFontGateData.countShapes</span></a> = countShapes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countShapes() - return shapes count</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.findLayer"></a>

## `findLayer`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.findLayer" href="#-fontgate.fgFontGateData.findLayer"><span class="function-name">fontgate.fgFontGateData.findLayer</span></a> = findLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer findLayer('name') - get layer by name, return Nothing if no layer found</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.getFontGateData"></a>

## `getFontGateData`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.getFontGateData" href="#-fontgate.fgFontGateData.getFontGateData"><span class="function-name">fontgate.fgFontGateData.getFontGateData</span></a> = getFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData getFontGateData() - return self</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.getType"></a>

## `getType`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.getType" href="#-fontgate.fgFontGateData.getType"><span class="function-name">fontgate.fgFontGateData.getType</span></a> = getType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getType() - return 'dtFontGate'</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.hasBody"></a>

## `hasBody`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.hasBody" href="#-fontgate.fgFontGateData.hasBody"><span class="function-name">fontgate.fgFontGateData.hasBody</span></a> = hasBody<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasBody(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.hasColors"></a>

## `hasColors`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.hasColors" href="#-fontgate.fgFontGateData.hasColors"><span class="function-name">fontgate.fgFontGateData.hasColors</span></a> = hasColors<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasColors() - return true if colors is present</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.hasHints"></a>

## `hasHints`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.hasHints" href="#-fontgate.fgFontGateData.hasHints"><span class="function-name">fontgate.fgFontGateData.hasHints</span></a> = hasHints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasHints() - return true if hints is present</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.hasPictures"></a>

## `hasPictures`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.hasPictures" href="#-fontgate.fgFontGateData.hasPictures"><span class="function-name">fontgate.fgFontGateData.hasPictures</span></a> = hasPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasPictures() - return true if pictures is present</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.layers"></a>

## `layers`


<dl class="descriptor"><dt>fontgate.fgFontGateData.layers</dt>
<dd>

<pre class="doc" markdown="0">(fgLayers) layers list</pre>

</dd>
</dl>



<a name="fontgate.fgFontGateData.maskLayer"></a>

## `maskLayer`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.maskLayer" href="#-fontgate.fgFontGateData.maskLayer"><span class="function-name">fontgate.fgFontGateData.maskLayer</span></a> = maskLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgLayer maskLayer(bool createIfMissing)</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.modified"></a>

## `modified`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.modified" href="#-fontgate.fgFontGateData.modified"><span class="function-name">fontgate.fgFontGateData.modified</span></a> = modified<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool modified() - return true if data was changed</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.OK"></a>

## `OK`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.OK" href="#-fontgate.fgFontGateData.OK"><span class="function-name">fontgate.fgFontGateData.OK</span></a> = OK<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool OK() - return true if status is gdsOK</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.resetBbox"></a>

## `resetBbox`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.resetBbox" href="#-fontgate.fgFontGateData.resetBbox"><span class="function-name">fontgate.fgFontGateData.resetBbox</span></a> = resetBbox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">resetBbox() - reset bbox cache</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.setParent"></a>

## `setParent`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.setParent" href="#-fontgate.fgFontGateData.setParent"><span class="function-name">fontgate.fgFontGateData.setParent</span></a> = setParent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setParent(fgGlyph) - set parent glyph</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.status"></a>

## `status`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.status" href="#-fontgate.fgFontGateData.status"><span class="function-name">fontgate.fgFontGateData.status</span></a> = status<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' status()</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.transform" href="#-fontgate.fgFontGateData.transform"><span class="function-name">fontgate.fgFontGateData.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix) - transform data</pre>

</dd></dl>



<a name="fontgate.fgFontGateData.updated"></a>

## `updated`


<dl class="function"><dt><a name="-fontgate.fgFontGateData.updated" href="#-fontgate.fgFontGateData.updated"><span class="function-name">fontgate.fgFontGateData.updated</span></a> = updated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updated() - mark data as changed, reset internal caches</pre>

</dd></dl>

