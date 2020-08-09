

<a name="typerig.core.objects.point"></a>

# `typerig.core.objects.point`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.point (<span class="info">version 0.26.2)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Point (Object)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.point.html#Point">Point</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.point.html#Void">Void</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Point" href="#Point">class <span class="class-name">Point</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Point-__abs__" href="#Point-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__add__" href="#Point-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"># -- Operators</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__and__" href="#Point-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self & other: Used as for Scalar product</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__div__" href="#Point-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__init__" href="#Point-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__mul__" href="#Point-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__neg__" href="#Point-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__or__" href="#Point-__or__"><span class="function-name">__or__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self | other: Used as for Cross product</pre>

</dd></dl>
<dl><dt><a name="Point-__rdiv__" href="#Point-__rdiv__"><span class="function-name">__rdiv__</span></a> = <a href="#Point-__div__">__div__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-__repr__" href="#Point-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Point-__rmul__" href="#Point-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#Point-__mul__">__mul__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-__sub__" href="#Point-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Point-__truediv__" href="#Point-__truediv__"><span class="function-name">__truediv__</span></a> = <a href="#Point-__div__">__div__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-angle_to" href="#Point-angle_to"><span class="function-name">angle_to</span></a><span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-diff_to" href="#Point-diff_to"><span class="function-name">diff_to</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doFlip" href="#Point-doFlip"><span class="function-name">doFlip</span></a><span class="argspec">(self, sign<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doSwap" href="#Point-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doTransform" href="#Point-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_width" href="#Point-solve_width"><span class="function-name">solve_width</span></a><span class="argspec">(self, y<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_x" href="#Point-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_y" href="#Point-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

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
</dd>
<dt class="class"><h2><a name="Void" href="#Void">class <span class="class-name">Void</span></a>(<a href="./typerig.core.objects.point.html#Point">Point</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.point.html#Void">Void</a></dd><dd><a href="./typerig.core.objects.point.html#Point">Point</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Void-__init__" href="#Void-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.point.html#Point">Point</a></h4><dl class="function"><dt><a name="Void-__abs__" href="#Void-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__add__" href="#Void-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"># -- Operators</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__and__" href="#Void-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self & other: Used as for Scalar product</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__div__" href="#Void-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__mul__" href="#Void-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__neg__" href="#Void-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__or__" href="#Void-__or__"><span class="function-name">__or__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self | other: Used as for Cross product</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__rdiv__" href="#Void-__rdiv__"><span class="function-name">__rdiv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__repr__" href="#Void-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__rmul__" href="#Void-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__sub__" href="#Void-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-__truediv__" href="#Void-__truediv__"><span class="function-name">__truediv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-angle_to" href="#Void-angle_to"><span class="function-name">angle_to</span></a><span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-diff_to" href="#Void-diff_to"><span class="function-name">diff_to</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-doFlip" href="#Void-doFlip"><span class="function-name">doFlip</span></a><span class="argspec">(self, sign<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-doSwap" href="#Void-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-doTransform" href="#Void-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-solve_width" href="#Void-solve_width"><span class="function-name">solve_width</span></a><span class="argspec">(self, y<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>
<dl class="function"><dt><a name="Void-solve_x" href="#Void-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Void-solve_y" href="#Void-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.point.html#Point">Point</a></h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.core.objects.point.Point"></a>

## `Point`


<dt class="class"><h2><span class="class-name">typerig.core.objects.point.Point</span> = <a name="typerig.core.objects.point.Point" href="#typerig.core.objects.point.Point">class Point</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Point-__abs__" href="#Point-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__add__" href="#Point-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"># -- Operators</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__and__" href="#Point-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self & other: Used as for Scalar product</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__div__" href="#Point-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__init__" href="#Point-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__mul__" href="#Point-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__neg__" href="#Point-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__or__" href="#Point-__or__"><span class="function-name">__or__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self | other: Used as for Cross product</pre>

</dd></dl>
<dl><dt><a name="Point-__rdiv__" href="#Point-__rdiv__"><span class="function-name">__rdiv__</span></a> = <a href="#Point-__div__">__div__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-__repr__" href="#Point-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Point-__rmul__" href="#Point-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#Point-__mul__">__mul__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-__sub__" href="#Point-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="Point-__truediv__" href="#Point-__truediv__"><span class="function-name">__truediv__</span></a> = <a href="#Point-__div__">__div__</a><span class="argspec">(self, other)</span></dt></dl>
<dl class="function"><dt><a name="Point-angle_to" href="#Point-angle_to"><span class="function-name">angle_to</span></a><span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-diff_to" href="#Point-diff_to"><span class="function-name">diff_to</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doFlip" href="#Point-doFlip"><span class="function-name">doFlip</span></a><span class="argspec">(self, sign<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doSwap" href="#Point-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-doTransform" href="#Point-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_width" href="#Point-solve_width"><span class="function-name">solve_width</span></a><span class="argspec">(self, y<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_x" href="#Point-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Point-solve_y" href="#Point-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

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
</dd>


<a name="typerig.core.objects.point.Point.solve_width"></a>

### `solve_width`


<dl class="function"><dt><a name="-typerig.core.objects.point.Point.solve_width" href="#-typerig.core.objects.point.Point.solve_width"><span class="function-name">typerig.core.objects.point.Point.solve_width</span></a> = solve_width<span class="argspec">(self, y<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a> method</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>



<a name="typerig.core.objects.point.Point.angle_to"></a>

### `angle_to`


<dl class="function"><dt><a name="-typerig.core.objects.point.Point.angle_to" href="#-typerig.core.objects.point.Point.angle_to"><span class="function-name">typerig.core.objects.point.Point.angle_to</span></a> = angle_to<span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a> method</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>

