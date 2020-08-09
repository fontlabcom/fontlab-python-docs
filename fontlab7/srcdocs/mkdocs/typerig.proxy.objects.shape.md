

<a name="typerig.proxy.objects.shape"></a>

# `typerig.proxy.objects.shape`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.shape (<span class="info">version 0.26.5)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Shape (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li><li>PythonQt</li><li>random</li><li>typerig.core.objects</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.shape.html#eShape">eShape</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eShape" href="#eShape">class <span class="class-name">eShape</span></a>(<a href="./typerig.proxy.objects.shape.html#pShape">pShape</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Shape, adding some advanced functionality.

Constructor:
        eShape(flShape)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.shape.html#eShape">eShape</a></dd><dd><a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eShape-alignTo" href="#eShape-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Args:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-asCoord" href="#eShape-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord <a href="./__builtin__.html#object">object</a> of the Bottom lest corner.</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-contourOrder" href="#eShape-contourOrder"><span class="function-name">contourOrder</span></a><span class="argspec">(self, order<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rearrange shape contours:
Args:
        order (tuple(Bool,Bool)): X (Left(True) to Right(False)) and Y (Bottom(True), Top(False)) order or None to sort on single coordinate.
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-getNext" href="#eShape-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-getPrev" href="#eShape-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-round" href="#eShape-round"><span class="function-name">round</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></h4><dl class="function"><dt><a name="eShape-__init__" href="#eShape-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, glyph<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-__repr__" href="#eShape-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-builder" href="#eShape-builder"><span class="function-name">builder</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeBuilder Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-container" href="#eShape-container"><span class="function-name">container</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns a list of flShape Objects that are contained within this shape.</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-contours" href="#eShape-contours"><span class="function-name">contours</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-copyBuilder" href="#eShape-copyBuilder"><span class="function-name">copyBuilder</span></a><span class="argspec">(self, source)</span></dt><dd>

<pre class="doc" markdown="0"># - Complex shapes, builders and etc. ---------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-data" href="#eShape-data"><span class="function-name">data</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeData Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-decompose" href="#eShape-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Position, composition ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-draw" href="#eShape-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goBackOf" href="#eShape-goBackOf"><span class="function-name">goBackOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goDown" href="#eShape-goDown"><span class="function-name">goDown</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goFrontOf" href="#eShape-goFrontOf"><span class="function-name">goFrontOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goLayerBack" href="#eShape-goLayerBack"><span class="function-name">goLayerBack</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goLayerFront" href="#eShape-goLayerFront"><span class="function-name">goLayerFront</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goUp" href="#eShape-goUp"><span class="function-name">goUp</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-info" href="#eShape-info"><span class="function-name">info</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeInfo Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-isChanged" href="#eShape-isChanged"><span class="function-name">isChanged</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-nodes" href="#eShape-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-reset_transform" href="#eShape-reset_transform"><span class="function-name">reset_transform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Transformation ----------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-rotate" href="#eShape-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-scale" href="#eShape-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-segments" href="#eShape-segments"><span class="function-name">segments</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Contours, Segmets, Nodes ------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-setName" href="#eShape-setName"><span class="function-name">setName</span></a><span class="argspec">(self, shape_name)</span></dt><dd>

<pre class="doc" markdown="0"># - Management ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-shear" href="#eShape-shear"><span class="function-name">shear</span></a><span class="argspec">(self, sh, sv, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-shift" href="#eShape-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-sortContours" href="#eShape-sortContours"><span class="function-name">sortContours</span></a><span class="argspec">(self, criteria<span class="parameter-default">='y'</span>, ascending<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-tag" href="#eShape-tag"><span class="function-name">tag</span></a><span class="argspec">(self, tagString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-update" href="#eShape-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
</dd>
<dt class="class"><h2><a name="pShape" href="#pShape">class <span class="class-name">pShape</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flShape, flShapeData and flShapeInfo objects

Constructor:
        pShape(flShape)

Attributes:
        .fl (flNode): Original flNode 
        .parent (flContour): parent contour
        .contour (flContour): parent contour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pShape-__init__" href="#pShape-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, glyph<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-__repr__" href="#pShape-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-builder" href="#pShape-builder"><span class="function-name">builder</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeBuilder Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-container" href="#pShape-container"><span class="function-name">container</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns a list of flShape Objects that are contained within this shape.</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-contours" href="#pShape-contours"><span class="function-name">contours</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-copyBuilder" href="#pShape-copyBuilder"><span class="function-name">copyBuilder</span></a><span class="argspec">(self, source)</span></dt><dd>

<pre class="doc" markdown="0"># - Complex shapes, builders and etc. ---------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-data" href="#pShape-data"><span class="function-name">data</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeData Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-decompose" href="#pShape-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Position, composition ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-draw" href="#pShape-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goBackOf" href="#pShape-goBackOf"><span class="function-name">goBackOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goDown" href="#pShape-goDown"><span class="function-name">goDown</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goFrontOf" href="#pShape-goFrontOf"><span class="function-name">goFrontOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goLayerBack" href="#pShape-goLayerBack"><span class="function-name">goLayerBack</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goLayerFront" href="#pShape-goLayerFront"><span class="function-name">goLayerFront</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goUp" href="#pShape-goUp"><span class="function-name">goUp</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-info" href="#pShape-info"><span class="function-name">info</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeInfo Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-isChanged" href="#pShape-isChanged"><span class="function-name">isChanged</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-nodes" href="#pShape-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-reset_transform" href="#pShape-reset_transform"><span class="function-name">reset_transform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Transformation ----------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-rotate" href="#pShape-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-scale" href="#pShape-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-segments" href="#pShape-segments"><span class="function-name">segments</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Contours, Segmets, Nodes ------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-setName" href="#pShape-setName"><span class="function-name">setName</span></a><span class="argspec">(self, shape_name)</span></dt><dd>

<pre class="doc" markdown="0"># - Management ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-shear" href="#pShape-shear"><span class="function-name">shear</span></a><span class="argspec">(self, sh, sv, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-shift" href="#pShape-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-sortContours" href="#pShape-sortContours"><span class="function-name">sortContours</span></a><span class="argspec">(self, criteria<span class="parameter-default">='y'</span>, ascending<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-tag" href="#pShape-tag"><span class="function-name">tag</span></a><span class="argspec">(self, tagString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-update" href="#pShape-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

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
</dd></dl></div></div>


<a name="typerig.proxy.objects.shape.pShape"></a>

## `pShape`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.shape.pShape</span> = <a name="typerig.proxy.objects.shape.pShape" href="#typerig.proxy.objects.shape.pShape">class pShape</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flShape, flShapeData and flShapeInfo objects

Constructor:
        pShape(flShape)

Attributes:
        .fl (flNode): Original flNode 
        .parent (flContour): parent contour
        .contour (flContour): parent contour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pShape-__init__" href="#pShape-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, glyph<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-__repr__" href="#pShape-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-builder" href="#pShape-builder"><span class="function-name">builder</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeBuilder Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-container" href="#pShape-container"><span class="function-name">container</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns a list of flShape Objects that are contained within this shape.</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-contours" href="#pShape-contours"><span class="function-name">contours</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-copyBuilder" href="#pShape-copyBuilder"><span class="function-name">copyBuilder</span></a><span class="argspec">(self, source)</span></dt><dd>

<pre class="doc" markdown="0"># - Complex shapes, builders and etc. ---------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-data" href="#pShape-data"><span class="function-name">data</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeData Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-decompose" href="#pShape-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Position, composition ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-draw" href="#pShape-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goBackOf" href="#pShape-goBackOf"><span class="function-name">goBackOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goDown" href="#pShape-goDown"><span class="function-name">goDown</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goFrontOf" href="#pShape-goFrontOf"><span class="function-name">goFrontOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goLayerBack" href="#pShape-goLayerBack"><span class="function-name">goLayerBack</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goLayerFront" href="#pShape-goLayerFront"><span class="function-name">goLayerFront</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-goUp" href="#pShape-goUp"><span class="function-name">goUp</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-info" href="#pShape-info"><span class="function-name">info</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeInfo Object</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-isChanged" href="#pShape-isChanged"><span class="function-name">isChanged</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-nodes" href="#pShape-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-reset_transform" href="#pShape-reset_transform"><span class="function-name">reset_transform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Transformation ----------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-rotate" href="#pShape-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-scale" href="#pShape-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-segments" href="#pShape-segments"><span class="function-name">segments</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Contours, Segmets, Nodes ------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-setName" href="#pShape-setName"><span class="function-name">setName</span></a><span class="argspec">(self, shape_name)</span></dt><dd>

<pre class="doc" markdown="0"># - Management ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-shear" href="#pShape-shear"><span class="function-name">shear</span></a><span class="argspec">(self, sh, sv, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-shift" href="#pShape-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-sortContours" href="#pShape-sortContours"><span class="function-name">sortContours</span></a><span class="argspec">(self, criteria<span class="parameter-default">='y'</span>, ascending<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-tag" href="#pShape-tag"><span class="function-name">tag</span></a><span class="argspec">(self, tagString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pShape-update" href="#pShape-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

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
</dd>


<a name="typerig.proxy.objects.shape.pShape.data"></a>

### `data`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.pShape.data" href="#-typerig.proxy.objects.shape.pShape.data"><span class="function-name">typerig.proxy.objects.shape.pShape.data</span></a> = data<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#pShape">typerig.proxy.objects.shape.pShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeData Object</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.pShape.info"></a>

### `info`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.pShape.info" href="#-typerig.proxy.objects.shape.pShape.info"><span class="function-name">typerig.proxy.objects.shape.pShape.info</span></a> = info<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#pShape">typerig.proxy.objects.shape.pShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeInfo Object</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.pShape.builder"></a>

### `builder`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.pShape.builder" href="#-typerig.proxy.objects.shape.pShape.builder"><span class="function-name">typerig.proxy.objects.shape.pShape.builder</span></a> = builder<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#pShape">typerig.proxy.objects.shape.pShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeBuilder Object</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.pShape.container"></a>

### `container`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.pShape.container" href="#-typerig.proxy.objects.shape.pShape.container"><span class="function-name">typerig.proxy.objects.shape.pShape.container</span></a> = container<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#pShape">typerig.proxy.objects.shape.pShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns a list of flShape Objects that are contained within this shape.</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.pShape.draw"></a>

### `draw`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.pShape.draw" href="#-typerig.proxy.objects.shape.pShape.draw"><span class="function-name">typerig.proxy.objects.shape.pShape.draw</span></a> = draw<span class="argspec">(self, pen)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#pShape">typerig.proxy.objects.shape.pShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.eShape"></a>

## `eShape`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.shape.eShape</span> = <a name="typerig.proxy.objects.shape.eShape" href="#typerig.proxy.objects.shape.eShape">class eShape</a>(<a href="./typerig.proxy.objects.shape.html#pShape">pShape</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Shape, adding some advanced functionality.

Constructor:
        eShape(flShape)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.shape.html#eShape">eShape</a></dd><dd><a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eShape-alignTo" href="#eShape-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Args:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-asCoord" href="#eShape-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the Bottom lest corner.</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-contourOrder" href="#eShape-contourOrder"><span class="function-name">contourOrder</span></a><span class="argspec">(self, order<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rearrange shape contours:
Args:
        order (tuple(Bool,Bool)): X (Left(True) to Right(False)) and Y (Bottom(True), Top(False)) order or None to sort on single coordinate.
Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-getNext" href="#eShape-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-getPrev" href="#eShape-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-round" href="#eShape-round"><span class="function-name">round</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></h4><dl class="function"><dt><a name="eShape-__init__" href="#eShape-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, shape, layer<span class="parameter-default">=None</span>, glyph<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-__repr__" href="#eShape-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-builder" href="#eShape-builder"><span class="function-name">builder</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeBuilder Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-container" href="#eShape-container"><span class="function-name">container</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns a list of flShape Objects that are contained within this shape.</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-contours" href="#eShape-contours"><span class="function-name">contours</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-copyBuilder" href="#eShape-copyBuilder"><span class="function-name">copyBuilder</span></a><span class="argspec">(self, source)</span></dt><dd>

<pre class="doc" markdown="0"># - Complex shapes, builders and etc. ---------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-data" href="#eShape-data"><span class="function-name">data</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeData Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-decompose" href="#eShape-decompose"><span class="function-name">decompose</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Position, composition ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-draw" href="#eShape-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goBackOf" href="#eShape-goBackOf"><span class="function-name">goBackOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goDown" href="#eShape-goDown"><span class="function-name">goDown</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goFrontOf" href="#eShape-goFrontOf"><span class="function-name">goFrontOf</span></a><span class="argspec">(self, flShape)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goLayerBack" href="#eShape-goLayerBack"><span class="function-name">goLayerBack</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goLayerFront" href="#eShape-goLayerFront"><span class="function-name">goLayerFront</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-goUp" href="#eShape-goUp"><span class="function-name">goUp</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-info" href="#eShape-info"><span class="function-name">info</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return flShapeInfo Object</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-isChanged" href="#eShape-isChanged"><span class="function-name">isChanged</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-nodes" href="#eShape-nodes"><span class="function-name">nodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-reset_transform" href="#eShape-reset_transform"><span class="function-name">reset_transform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Transformation ----------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-rotate" href="#eShape-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-scale" href="#eShape-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-segments" href="#eShape-segments"><span class="function-name">segments</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Contours, Segmets, Nodes ------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-setName" href="#eShape-setName"><span class="function-name">setName</span></a><span class="argspec">(self, shape_name)</span></dt><dd>

<pre class="doc" markdown="0"># - Management ---------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-shear" href="#eShape-shear"><span class="function-name">shear</span></a><span class="argspec">(self, sh, sv, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-shift" href="#eShape-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy, reset<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-sortContours" href="#eShape-sortContours"><span class="function-name">sortContours</span></a><span class="argspec">(self, criteria<span class="parameter-default">='y'</span>, ascending<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-tag" href="#eShape-tag"><span class="function-name">tag</span></a><span class="argspec">(self, tagString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eShape-update" href="#eShape-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.shape.html#pShape">pShape</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
</dd>


<a name="typerig.proxy.objects.shape.eShape.asCoord"></a>

### `asCoord`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.eShape.asCoord" href="#-typerig.proxy.objects.shape.eShape.asCoord"><span class="function-name">typerig.proxy.objects.shape.eShape.asCoord</span></a> = asCoord<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#eShape">typerig.proxy.objects.shape.eShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the Bottom lest corner.</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.eShape.contourOrder"></a>

### `contourOrder`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.eShape.contourOrder" href="#-typerig.proxy.objects.shape.eShape.contourOrder"><span class="function-name">typerig.proxy.objects.shape.eShape.contourOrder</span></a> = contourOrder<span class="argspec">(self, order<span class="parameter-default">=(True, True)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#eShape">typerig.proxy.objects.shape.eShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Rearrange shape contours:
Args:
        order (tuple(Bool,Bool)): X (Left(True) to Right(False)) and Y (Bottom(True), Top(False)) order or None to sort on single coordinate.
Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.shape.eShape.alignTo"></a>

### `alignTo`


<dl class="function"><dt><a name="-typerig.proxy.objects.shape.eShape.alignTo" href="#-typerig.proxy.objects.shape.eShape.alignTo"><span class="function-name">typerig.proxy.objects.shape.eShape.alignTo</span></a> = alignTo<span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.shape.html#eShape">typerig.proxy.objects.shape.eShape</a> method</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Args:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>

