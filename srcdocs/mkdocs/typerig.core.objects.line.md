

<a name="typerig.core.objects.line"></a>

# `typerig.core.objects.line`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.line (<span class="info">version 0.26.1)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Line (Object)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2015-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.line.html#Line">Line</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.line.html#Vector">Vector</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Line" href="#Line">class <span class="class-name">Line</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Line-__add__" href="#Line-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__and__" href="#Line-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__div__" href="#Line-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__init__" href="#Line-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__mul__" href="#Line-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__repr__" href="#Line-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Line-__rmul__" href="#Line-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#Line-__mul__">__mul__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Line-__sub__" href="#Line-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doSwap" href="#Line-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doTransform" href="#Line-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-intersect_line" href="#Line-intersect_line"><span class="function-name">intersect_line</span></a><span class="argspec">(self, other_line)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp" href="#Line-lerp"><span class="function-name">lerp</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp_xy" href="#Line-lerp_xy"><span class="function-name">lerp_xy</span></a><span class="argspec">(self, time_x, time_y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-shift" href="#Line-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_point" href="#Line-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_slice" href="#Line-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_x" href="#Line-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_y" href="#Line-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

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
<dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>diff_x</dt>
</dl>
<dl class="descriptor"><dt>diff_y</dt>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>length</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd>
<dt class="class"><h2><a name="Vector" href="#Vector">class <span class="class-name">Vector</span></a>(<a href="./typerig.core.objects.line.html#Line">Line</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.line.html#Vector">Vector</a></dd><dd><a href="./typerig.core.objects.line.html#Line">Line</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Vector-__init__" href="#Vector-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__repr__" href="#Vector-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-getAngle" href="#Vector-getAngle"><span class="function-name">getAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-getSlope" href="#Vector-getSlope"><span class="function-name">getSlope</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Getters</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.line.html#Line">Line</a></h4><dl class="function"><dt><a name="Vector-__add__" href="#Vector-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__and__" href="#Vector-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__div__" href="#Vector-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__mul__" href="#Vector-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__rmul__" href="#Vector-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__sub__" href="#Vector-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-doSwap" href="#Vector-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-doTransform" href="#Vector-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-intersect_line" href="#Vector-intersect_line"><span class="function-name">intersect_line</span></a><span class="argspec">(self, other_line)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-lerp" href="#Vector-lerp"><span class="function-name">lerp</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-lerp_xy" href="#Vector-lerp_xy"><span class="function-name">lerp_xy</span></a><span class="argspec">(self, time_x, time_y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-shift" href="#Vector-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_point" href="#Vector-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_slice" href="#Vector-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_x" href="#Vector-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_y" href="#Vector-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.line.html#Line">Line</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>diff_x</dt>
</dl>
<dl class="descriptor"><dt>diff_y</dt>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>length</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd></dl></div></div>


<a name="typerig.core.objects.line.Line"></a>

## `Line`


<dt class="class"><h2><span class="class-name">typerig.core.objects.line.Line</span> = <a name="typerig.core.objects.line.Line" href="#typerig.core.objects.line.Line">class Line</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Line-__add__" href="#Line-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__and__" href="#Line-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__div__" href="#Line-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__init__" href="#Line-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__mul__" href="#Line-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__repr__" href="#Line-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Line-__rmul__" href="#Line-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#Line-__mul__">__mul__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Line-__sub__" href="#Line-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doSwap" href="#Line-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doTransform" href="#Line-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-intersect_line" href="#Line-intersect_line"><span class="function-name">intersect_line</span></a><span class="argspec">(self, other_line)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp" href="#Line-lerp"><span class="function-name">lerp</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp_xy" href="#Line-lerp_xy"><span class="function-name">lerp_xy</span></a><span class="argspec">(self, time_x, time_y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-shift" href="#Line-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_point" href="#Line-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_slice" href="#Line-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_x" href="#Line-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_y" href="#Line-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

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
<dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>diff_x</dt>
</dl>
<dl class="descriptor"><dt>diff_y</dt>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>length</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd>


<a name="typerig.core.objects.line.Line.y_intercept"></a>

### `y_intercept`


<dl class="descriptor"><dt>typerig.core.objects.line.Line.y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>



<a name="typerig.core.objects.line.Line.solve_y"></a>

### `solve_y`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.solve_y" href="#-typerig.core.objects.line.Line.solve_y"><span class="function-name">typerig.core.objects.line.Line.solve_y</span></a> = solve_y<span class="argspec">(self, x)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

</dd></dl>



<a name="typerig.core.objects.line.Line.solve_x"></a>

### `solve_x`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.solve_x" href="#-typerig.core.objects.line.Line.solve_x"><span class="function-name">typerig.core.objects.line.Line.solve_x</span></a> = solve_x<span class="argspec">(self, y)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>



<a name="typerig.core.objects.line.Line.solve_point"></a>

### `solve_point`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.solve_point" href="#-typerig.core.objects.line.Line.solve_point"><span class="function-name">typerig.core.objects.line.Line.solve_point</span></a> = solve_point<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>



<a name="typerig.core.objects.line.Line.solve_slice"></a>

### `solve_slice`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.solve_slice" href="#-typerig.core.objects.line.Line.solve_slice"><span class="function-name">typerig.core.objects.line.Line.solve_slice</span></a> = solve_slice<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>



<a name="typerig.core.objects.line.Line.intersect_line"></a>

### `intersect_line`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.intersect_line" href="#-typerig.core.objects.line.Line.intersect_line"><span class="function-name">typerig.core.objects.line.Line.intersect_line</span></a> = intersect_line<span class="argspec">(self, other_line)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>



<a name="typerig.core.objects.line.Line.shift"></a>

### `shift`


<dl class="function"><dt><a name="-typerig.core.objects.line.Line.shift" href="#-typerig.core.objects.line.Line.shift"><span class="function-name">typerig.core.objects.line.Line.shift</span></a> = shift<span class="argspec">(self, dx, dy)</span><span class="note"> unbound <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a> method</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>

