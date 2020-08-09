

<a name="typerig.proxy.pens.outlinePen"></a>

# `typerig.proxy.pens.outlinePen`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.pens.html">pens</a>.outlinePen (<span class="info">version 0.1.3)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0">#FLM: Refactor: Outline Pen
# MODULE: Typerig / Proxy / Pen / Outline Pen (Pen)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2019-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a></span>(<span class="bases">fontTools.pens.basePen.DecomposingPen</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.pens.outlinePen.html#OutlinePen">OutlinePen</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.pens.outlinePen.html#altPoint">altPoint</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="OutlinePen" href="#OutlinePen">class <span class="class-name">OutlinePen</span></a>(<a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">OutlinePen (protocol)
Adapted from: Frederik Berlaen's (Typemytype) outlinerRoboFontExtension
Original Source: https://github.com/typemytype/outlinerRoboFontExtension

Attribs:
- offset (float): Outline offset
- contrast (float): Outline Contrast
- contrastAngle (float): Outline contrast angle
- connection (string): Connection type - square; 
- cap (string): Cap type - round
- closeOpenPaths (bool): Close open paths
- optimizeCurve (bool): Optimize curve (adds an extra point of every curve at .5 time)
- filterDoubles (bool): Filter double nodes
- miterLimit (float): Sets miter limit

Returns:
- getGlyphs(): innerGlyph, outerGlyph, originalGlyph,(fgGlyph)
- getShapes():  innerShape, outerShape, originalShape (flShape)
- getContours(): innerContour, outerContour, originalContour (flShape)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.pens.outlinePen.html#OutlinePen">OutlinePen</a></dd><dd><a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a></dd><dd><a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></dd><dd><a href="./fontTools.pens.basePen.html#LoggingPen">fontTools.pens.basePen.LoggingPen</a></dd><dd><a href="./fontTools.misc.loggingTools.html#LogMixin">fontTools.misc.loggingTools.LogMixin</a></dd><dd><a href="./fontTools.pens.basePen.html#AbstractPen">fontTools.pens.basePen.AbstractPen</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="OutlinePen-__init__" href="#OutlinePen-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-buildCap" href="#OutlinePen-buildCap"><span class="function-name">buildCap</span></a><span class="argspec">(self, firstContour, lastContour)</span></dt><dd>

<pre class="doc" markdown="0"># - Line Caps --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-buildConnection" href="#OutlinePen-buildConnection"><span class="function-name">buildConnection</span></a><span class="argspec">(self, close<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># -- Connections --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capButt" href="#OutlinePen-capButt"><span class="function-name">capButt</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capRound" href="#OutlinePen-capRound"><span class="function-name">capRound</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capSquare" href="#OutlinePen-capSquare"><span class="function-name">capSquare</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionButt" href="#OutlinePen-connectionButt"><span class="function-name">connectionButt</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionInnerCorner" href="#OutlinePen-connectionInnerCorner"><span class="function-name">connectionInnerCorner</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionRound" href="#OutlinePen-connectionRound"><span class="function-name">connectionRound</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionSquare" href="#OutlinePen-connectionSquare"><span class="function-name">connectionSquare</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getGlyphs" href="#OutlinePen-getGlyphs"><span class="function-name">getGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Output -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getShapes" href="#OutlinePen-getShapes"><span class="function-name">getShapes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getThickness" href="#OutlinePen-getThickness"><span class="function-name">getThickness</span></a><span class="argspec">(self, angle)</span></dt><dd>

<pre class="doc" markdown="0"># -- Thickness</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">magicCurve</span> = 0.5522847498</dt></dl>
<dl><dt><span class="other-name">pointClass</span> = &lt;class 'typerig.proxy.pens.outlinePen.altPoint'&gt;</dt></dl>

  <h4 class="head-methods">Methods from <a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a></h4><dl class="function"><dt><a name="OutlinePen-closePath" href="#OutlinePen-closePath"><span class="function-name">closePath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-curveTo" href="#OutlinePen-curveTo"><span class="function-name">curveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-endPath" href="#OutlinePen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-lineTo" href="#OutlinePen-lineTo"><span class="function-name">lineTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-moveTo" href="#OutlinePen-moveTo"><span class="function-name">moveTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-qCurveTo" href="#OutlinePen-qCurveTo"><span class="function-name">qCurveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></h4><dl class="function"><dt><a name="OutlinePen-addComponent" href="#OutlinePen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, glyphName, transformation)</span></dt><dd>

<pre class="doc" markdown="0">Transform the points of the base glyph and draw it onto self.</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></h4><dl><dt><span class="other-name">skipMissingComponents</span> = True</dt></dl>

  <h4 class="head-desc">Descriptors from <a href="./fontTools.misc.loggingTools.html#LogMixin">fontTools.misc.loggingTools.LogMixin</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>log</dt>
</dl>
</dd>
<dt class="class"><h2><a name="altPoint" href="#altPoint">class <span class="class-name">altPoint</span></a>(<a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes ------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.pens.outlinePen.html#altPoint">altPoint</a></dd><dd><a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="altPoint-__eq__" href="#altPoint-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, p)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__getitem__" href="#altPoint-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__init__" href="#altPoint-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, x, y<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__iter__" href="#altPoint-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__ne__" href="#altPoint-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, p)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>fgPoint</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></h4><dl class="function"><dt><a name="altPoint-__abs__" href="#altPoint-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__add__" href="#altPoint-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"># -- Operators</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__and__" href="#altPoint-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self & other: Used as for Scalar product</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__div__" href="#altPoint-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__mul__" href="#altPoint-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__neg__" href="#altPoint-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__or__" href="#altPoint-__or__"><span class="function-name">__or__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self | other: Used as for Cross product</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__rdiv__" href="#altPoint-__rdiv__"><span class="function-name">__rdiv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__repr__" href="#altPoint-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__rmul__" href="#altPoint-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__sub__" href="#altPoint-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-__truediv__" href="#altPoint-__truediv__"><span class="function-name">__truediv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-angle_to" href="#altPoint-angle_to"><span class="function-name">angle_to</span></a><span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-diff_to" href="#altPoint-diff_to"><span class="function-name">diff_to</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-doFlip" href="#altPoint-doFlip"><span class="function-name">doFlip</span></a><span class="argspec">(self, sign<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-doSwap" href="#altPoint-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-doTransform" href="#altPoint-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-solve_width" href="#altPoint-solve_width"><span class="function-name">solve_width</span></a><span class="argspec">(self, y<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-solve_x" href="#altPoint-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="altPoint-solve_y" href="#altPoint-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>magnitude</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>swap</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>unit</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
</dl>
</dd></dl></div></div>


<a name="typerig.proxy.pens.outlinePen.OutlinePen"></a>

## `OutlinePen`


<dt class="class"><h2><span class="class-name">typerig.proxy.pens.outlinePen.OutlinePen</span> = <a name="typerig.proxy.pens.outlinePen.OutlinePen" href="#typerig.proxy.pens.outlinePen.OutlinePen">class OutlinePen</a>(<a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">OutlinePen (protocol)
Adapted from: Frederik Berlaen's (Typemytype) outlinerRoboFontExtension
Original Source: https://github.com/typemytype/outlinerRoboFontExtension

Attribs:
- offset (float): Outline offset
- contrast (float): Outline Contrast
- contrastAngle (float): Outline contrast angle
- connection (string): Connection type - square; 
- cap (string): Cap type - round
- closeOpenPaths (bool): Close open paths
- optimizeCurve (bool): Optimize curve (adds an extra point of every curve at .5 time)
- filterDoubles (bool): Filter double nodes
- miterLimit (float): Sets miter limit

Returns:
- getGlyphs(): innerGlyph, outerGlyph, originalGlyph,(fgGlyph)
- getShapes():  innerShape, outerShape, originalShape (flShape)
- getContours(): innerContour, outerContour, originalContour (flShape)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.pens.outlinePen.html#OutlinePen">OutlinePen</a></dd><dd><a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a></dd><dd><a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></dd><dd><a href="./fontTools.pens.basePen.html#LoggingPen">fontTools.pens.basePen.LoggingPen</a></dd><dd><a href="./fontTools.misc.loggingTools.html#LogMixin">fontTools.misc.loggingTools.LogMixin</a></dd><dd><a href="./fontTools.pens.basePen.html#AbstractPen">fontTools.pens.basePen.AbstractPen</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="OutlinePen-__init__" href="#OutlinePen-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-buildCap" href="#OutlinePen-buildCap"><span class="function-name">buildCap</span></a><span class="argspec">(self, firstContour, lastContour)</span></dt><dd>

<pre class="doc" markdown="0"># - Line Caps --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-buildConnection" href="#OutlinePen-buildConnection"><span class="function-name">buildConnection</span></a><span class="argspec">(self, close<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># -- Connections --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capButt" href="#OutlinePen-capButt"><span class="function-name">capButt</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capRound" href="#OutlinePen-capRound"><span class="function-name">capRound</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-capSquare" href="#OutlinePen-capSquare"><span class="function-name">capSquare</span></a><span class="argspec">(self, firstContour, lastContour, first, last, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionButt" href="#OutlinePen-connectionButt"><span class="function-name">connectionButt</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionInnerCorner" href="#OutlinePen-connectionInnerCorner"><span class="function-name">connectionInnerCorner</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionRound" href="#OutlinePen-connectionRound"><span class="function-name">connectionRound</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-connectionSquare" href="#OutlinePen-connectionSquare"><span class="function-name">connectionSquare</span></a><span class="argspec">(self, first, last, pen, close)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getGlyphs" href="#OutlinePen-getGlyphs"><span class="function-name">getGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Output -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getShapes" href="#OutlinePen-getShapes"><span class="function-name">getShapes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-getThickness" href="#OutlinePen-getThickness"><span class="function-name">getThickness</span></a><span class="argspec">(self, angle)</span></dt><dd>

<pre class="doc" markdown="0"># -- Thickness</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">magicCurve</span> = 0.5522847498</dt></dl>
<dl><dt><span class="other-name">pointClass</span> = &lt;class 'typerig.proxy.pens.outlinePen.altPoint'&gt;</dt></dl>

  <h4 class="head-methods">Methods from <a href="./fontTools.pens.basePen.html#BasePen">fontTools.pens.basePen.BasePen</a></h4><dl class="function"><dt><a name="OutlinePen-closePath" href="#OutlinePen-closePath"><span class="function-name">closePath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-curveTo" href="#OutlinePen-curveTo"><span class="function-name">curveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-endPath" href="#OutlinePen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-lineTo" href="#OutlinePen-lineTo"><span class="function-name">lineTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-moveTo" href="#OutlinePen-moveTo"><span class="function-name">moveTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="OutlinePen-qCurveTo" href="#OutlinePen-qCurveTo"><span class="function-name">qCurveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></h4><dl class="function"><dt><a name="OutlinePen-addComponent" href="#OutlinePen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, glyphName, transformation)</span></dt><dd>

<pre class="doc" markdown="0">Transform the points of the base glyph and draw it onto self.</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./fontTools.pens.basePen.html#DecomposingPen">fontTools.pens.basePen.DecomposingPen</a></h4><dl><dt><span class="other-name">skipMissingComponents</span> = True</dt></dl>

  <h4 class="head-desc">Descriptors from <a href="./fontTools.misc.loggingTools.html#LogMixin">fontTools.misc.loggingTools.LogMixin</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>log</dt>
</dl>
</dd>


<a name="typerig.proxy.pens.outlinePen.OutlinePen.magicCurve"></a>

### `magicCurve`


<span class="other-name">typerig.proxy.pens.outlinePen.OutlinePen.magicCurve</span> = 0.5522847498
