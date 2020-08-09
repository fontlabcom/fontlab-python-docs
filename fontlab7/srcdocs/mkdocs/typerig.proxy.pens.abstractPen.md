

<a name="typerig.proxy.pens.abstractPen"></a>

# `typerig.proxy.pens.abstractPen`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.pens.html">pens</a>.abstractPen (<span class="info">version 0.0.1)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Pen (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2019-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">AbstractPen</a></span></li><li><span class="class-name"><a href="./typerig.proxy.pens.abstractPen.html#AbstractPointPen">AbstractPointPen</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="AbstractPen" href="#AbstractPen">class <span class="class-name">AbstractPen</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">AbstractPen as specified by FontTools (fontTools.pens.basePen.py)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="AbstractPen-addComponent" href="#AbstractPen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, glyphName, transformation)</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph. The 'transformation' argument must be a 6-tuple
containing an affine transformation, or a Transform <a href="./__builtin__.html#object">object</a> from the
fontTools.misc.transform module. More precisely: it should be a
sequence containing 6 numbers.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-closePath" href="#AbstractPen-closePath"><span class="function-name">closePath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Close the current sub path. You must call either pen.<a href="#AbstractPen-closePath">closePath</a>()
or pen.<a href="#AbstractPen-endPath">endPath</a>() after each sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-curveTo" href="#AbstractPen-curveTo"><span class="function-name">curveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0">Draw a cubic bezier with an arbitrary number of control points.

The last point specified is on-curve, all others are off-curve
(control) points. If the number of control points is > 2, the
segment is split into multiple bezier segments. This works
like this:

Let n be the number of control points (which is the number of
arguments to this call minus 1). If n==2, a plain vanilla cubic
bezier is drawn. If n==1, we fall back to a quadratic segment and
if n==0 we draw a straight line. It gets interesting when n>2:
n-1 PostScript-style cubic segments will be drawn as if it were
one curve. See decomposeSuperBezierSegment().

The conversion algorithm used for n>2 is inspired by NURB
splines, and is conceptually equivalent to the TrueType "implied
points" principle. See also decomposeQuadraticSegment().</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-endPath" href="#AbstractPen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path, but don't close it. You must call
either pen.<a href="#AbstractPen-closePath">closePath</a>() or pen.<a href="#AbstractPen-endPath">endPath</a>() after each sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-lineTo" href="#AbstractPen-lineTo"><span class="function-name">lineTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0">Draw a straight line from the current point to 'pt'.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-moveTo" href="#AbstractPen-moveTo"><span class="function-name">moveTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0">Begin a new sub path, set the current point to 'pt'. You must
end each sub path with a call to pen.<a href="#AbstractPen-closePath">closePath</a>() or pen.<a href="#AbstractPen-endPath">endPath</a>().</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-qCurveTo" href="#AbstractPen-qCurveTo"><span class="function-name">qCurveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0">Draw a whole string of quadratic curve segments.

The last point specified is on-curve, all others are off-curve
points.

This method implements TrueType-style curves, breaking up curves
using 'implied points': between each two consequtive off-curve points,
there is one implied point exactly in the middle between them. See
also decomposeQuadraticSegment().

The last argument (normally the on-curve point) may be None.
This is to support contours that have NO on-curve points (a rarely
seen feature of TrueType outlines).</pre>

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
<dt class="class"><h2><a name="AbstractPointPen" href="#AbstractPointPen">class <span class="class-name">AbstractPointPen</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Baseclass for all PointPens as specified by FontTools (fontTools.pens.pointPen.py)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="AbstractPointPen-addComponent" href="#AbstractPointPen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, baseGlyphName, transformation, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-addPoint" href="#AbstractPointPen-addPoint"><span class="function-name">addPoint</span></a><span class="argspec">(self, pt, segmentType<span class="parameter-default">=None</span>, smooth<span class="parameter-default">=False</span>, name<span class="parameter-default">=None</span>, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Add a point to the current sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-beginPath" href="#AbstractPointPen-beginPath"><span class="function-name">beginPath</span></a><span class="argspec">(self, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Start a new sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-endPath" href="#AbstractPointPen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path.</pre>

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


<a name="typerig.proxy.pens.abstractPen.AbstractPen"></a>

## `AbstractPen`


<dt class="class"><h2><span class="class-name">typerig.proxy.pens.abstractPen.AbstractPen</span> = <a name="typerig.proxy.pens.abstractPen.AbstractPen" href="#typerig.proxy.pens.abstractPen.AbstractPen">class AbstractPen</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">AbstractPen as specified by FontTools (fontTools.pens.basePen.py)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="AbstractPen-addComponent" href="#AbstractPen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, glyphName, transformation)</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph. The 'transformation' argument must be a 6-tuple
containing an affine transformation, or a Transform object from the
fontTools.misc.transform module. More precisely: it should be a
sequence containing 6 numbers.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-closePath" href="#AbstractPen-closePath"><span class="function-name">closePath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Close the current sub path. You must call either pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-closePath">closePath</a>()
or pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-endPath">endPath</a>() after each sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-curveTo" href="#AbstractPen-curveTo"><span class="function-name">curveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0">Draw a cubic bezier with an arbitrary number of control points.

The last point specified is on-curve, all others are off-curve
(control) points. If the number of control points is > 2, the
segment is split into multiple bezier segments. This works
like this:

Let n be the number of control points (which is the number of
arguments to this call minus 1). If n==2, a plain vanilla cubic
bezier is drawn. If n==1, we fall back to a quadratic segment and
if n==0 we draw a straight line. It gets interesting when n>2:
n-1 PostScript-style cubic segments will be drawn as if it were
one curve. See decomposeSuperBezierSegment().

The conversion algorithm used for n>2 is inspired by NURB
splines, and is conceptually equivalent to the TrueType "implied
points" principle. See also decomposeQuadraticSegment().</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-endPath" href="#AbstractPen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path, but don't close it. You must call
either pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-closePath">closePath</a>() or pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-endPath">endPath</a>() after each sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-lineTo" href="#AbstractPen-lineTo"><span class="function-name">lineTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0">Draw a straight line from the current point to 'pt'.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-moveTo" href="#AbstractPen-moveTo"><span class="function-name">moveTo</span></a><span class="argspec">(self, pt)</span></dt><dd>

<pre class="doc" markdown="0">Begin a new sub path, set the current point to 'pt'. You must
end each sub path with a call to pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-closePath">closePath</a>() or pen.<a href="#typerig.proxy.pens.abstractPen.AbstractPen-endPath">endPath</a>().</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPen-qCurveTo" href="#AbstractPen-qCurveTo"><span class="function-name">qCurveTo</span></a><span class="argspec">(self, *points)</span></dt><dd>

<pre class="doc" markdown="0">Draw a whole string of quadratic curve segments.

The last point specified is on-curve, all others are off-curve
points.

This method implements TrueType-style curves, breaking up curves
using 'implied points': between each two consequtive off-curve points,
there is one implied point exactly in the middle between them. See
also decomposeQuadraticSegment().

The last argument (normally the on-curve point) may be None.
This is to support contours that have NO on-curve points (a rarely
seen feature of TrueType outlines).</pre>

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


<a name="typerig.proxy.pens.abstractPen.AbstractPen.moveTo"></a>

### `moveTo`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.moveTo" href="#-typerig.proxy.pens.abstractPen.AbstractPen.moveTo"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.moveTo</span></a> = moveTo<span class="argspec">(self, pt)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Begin a new sub path, set the current point to 'pt'. You must
end each sub path with a call to pen.closePath() or pen.endPath().</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.lineTo"></a>

### `lineTo`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.lineTo" href="#-typerig.proxy.pens.abstractPen.AbstractPen.lineTo"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.lineTo</span></a> = lineTo<span class="argspec">(self, pt)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Draw a straight line from the current point to 'pt'.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.curveTo"></a>

### `curveTo`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.curveTo" href="#-typerig.proxy.pens.abstractPen.AbstractPen.curveTo"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.curveTo</span></a> = curveTo<span class="argspec">(self, *points)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Draw a cubic bezier with an arbitrary number of control points.

The last point specified is on-curve, all others are off-curve
(control) points. If the number of control points is > 2, the
segment is split into multiple bezier segments. This works
like this:

Let n be the number of control points (which is the number of
arguments to this call minus 1). If n==2, a plain vanilla cubic
bezier is drawn. If n==1, we fall back to a quadratic segment and
if n==0 we draw a straight line. It gets interesting when n>2:
n-1 PostScript-style cubic segments will be drawn as if it were
one curve. See decomposeSuperBezierSegment().

The conversion algorithm used for n>2 is inspired by NURB
splines, and is conceptually equivalent to the TrueType "implied
points" principle. See also decomposeQuadraticSegment().</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.qCurveTo"></a>

### `qCurveTo`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.qCurveTo" href="#-typerig.proxy.pens.abstractPen.AbstractPen.qCurveTo"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.qCurveTo</span></a> = qCurveTo<span class="argspec">(self, *points)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Draw a whole string of quadratic curve segments.

The last point specified is on-curve, all others are off-curve
points.

This method implements TrueType-style curves, breaking up curves
using 'implied points': between each two consequtive off-curve points,
there is one implied point exactly in the middle between them. See
also decomposeQuadraticSegment().

The last argument (normally the on-curve point) may be None.
This is to support contours that have NO on-curve points (a rarely
seen feature of TrueType outlines).</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.closePath"></a>

### `closePath`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.closePath" href="#-typerig.proxy.pens.abstractPen.AbstractPen.closePath"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.closePath</span></a> = closePath<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Close the current sub path. You must call either pen.closePath()
or pen.endPath() after each sub path.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.endPath"></a>

### `endPath`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.endPath" href="#-typerig.proxy.pens.abstractPen.AbstractPen.endPath"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.endPath</span></a> = endPath<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path, but don't close it. You must call
either pen.closePath() or pen.endPath() after each sub path.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPen.addComponent"></a>

### `addComponent`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPen.addComponent" href="#-typerig.proxy.pens.abstractPen.AbstractPen.addComponent"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPen.addComponent</span></a> = addComponent<span class="argspec">(self, glyphName, transformation)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPen">typerig.proxy.pens.abstractPen.AbstractPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph. The 'transformation' argument must be a 6-tuple
containing an affine transformation, or a Transform object from the
fontTools.misc.transform module. More precisely: it should be a
sequence containing 6 numbers.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPointPen"></a>

## `AbstractPointPen`


<dt class="class"><h2><span class="class-name">typerig.proxy.pens.abstractPen.AbstractPointPen</span> = <a name="typerig.proxy.pens.abstractPen.AbstractPointPen" href="#typerig.proxy.pens.abstractPen.AbstractPointPen">class AbstractPointPen</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Baseclass for all PointPens as specified by FontTools (fontTools.pens.pointPen.py)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="AbstractPointPen-addComponent" href="#AbstractPointPen-addComponent"><span class="function-name">addComponent</span></a><span class="argspec">(self, baseGlyphName, transformation, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-addPoint" href="#AbstractPointPen-addPoint"><span class="function-name">addPoint</span></a><span class="argspec">(self, pt, segmentType<span class="parameter-default">=None</span>, smooth<span class="parameter-default">=False</span>, name<span class="parameter-default">=None</span>, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Add a point to the current sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-beginPath" href="#AbstractPointPen-beginPath"><span class="function-name">beginPath</span></a><span class="argspec">(self, identifier<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0">Start a new sub path.</pre>

</dd></dl>
<dl class="function"><dt><a name="AbstractPointPen-endPath" href="#AbstractPointPen-endPath"><span class="function-name">endPath</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path.</pre>

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


<a name="typerig.proxy.pens.abstractPen.AbstractPointPen.beginPath"></a>

### `beginPath`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPointPen.beginPath" href="#-typerig.proxy.pens.abstractPen.AbstractPointPen.beginPath"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPointPen.beginPath</span></a> = beginPath<span class="argspec">(self, identifier<span class="parameter-default">=None</span>, **kwargs)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPointPen">typerig.proxy.pens.abstractPen.AbstractPointPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Start a new sub path.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPointPen.endPath"></a>

### `endPath`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPointPen.endPath" href="#-typerig.proxy.pens.abstractPen.AbstractPointPen.endPath"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPointPen.endPath</span></a> = endPath<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPointPen">typerig.proxy.pens.abstractPen.AbstractPointPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">End the current sub path.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPointPen.addPoint"></a>

### `addPoint`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPointPen.addPoint" href="#-typerig.proxy.pens.abstractPen.AbstractPointPen.addPoint"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPointPen.addPoint</span></a> = addPoint<span class="argspec">(self, pt, segmentType<span class="parameter-default">=None</span>, smooth<span class="parameter-default">=False</span>, name<span class="parameter-default">=None</span>, identifier<span class="parameter-default">=None</span>, **kwargs)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPointPen">typerig.proxy.pens.abstractPen.AbstractPointPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Add a point to the current sub path.</pre>

</dd></dl>



<a name="typerig.proxy.pens.abstractPen.AbstractPointPen.addComponent"></a>

### `addComponent`


<dl class="function"><dt><a name="-typerig.proxy.pens.abstractPen.AbstractPointPen.addComponent" href="#-typerig.proxy.pens.abstractPen.AbstractPointPen.addComponent"><span class="function-name">typerig.proxy.pens.abstractPen.AbstractPointPen.addComponent</span></a> = addComponent<span class="argspec">(self, baseGlyphName, transformation, identifier<span class="parameter-default">=None</span>, **kwargs)</span><span class="note"> unbound <a href="./typerig.proxy.pens.abstractPen.html#AbstractPointPen">typerig.proxy.pens.abstractPen.AbstractPointPen</a> method</span></dt><dd>

<pre class="doc" markdown="0">Add a sub glyph.</pre>

</dd></dl>

