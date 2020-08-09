

<a name="typerig.core.objects.transform"></a>

# `typerig.core.objects.transform`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.transform (<span class="info">version 0.26.0)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Transform (Object)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.transform.html#AdaptiveScale">AdaptiveScale</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.transform.html#Transform">Transform</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="AdaptiveScale" href="#AdaptiveScale">class <span class="class-name">AdaptiveScale</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># -- Adaptive scaling ------------------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="AdaptiveScale-__init__" href="#AdaptiveScale-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, point_arrays, stem_arrays)</span></dt><dd>

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
<dt class="class"><h2><a name="Transform" href="#Transform">class <span class="class-name">Transform</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Affine transformations (Object)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Transform-__cmp__" href="#Transform-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__getitem__" href="#Transform-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__getslice__" href="#Transform-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__hash__" href="#Transform-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__init__" href="#Transform-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, xx<span class="parameter-default">=1.0</span>, xy<span class="parameter-default">=0.0</span>, yx<span class="parameter-default">=0.0</span>, yy<span class="parameter-default">=1.0</span>, dx<span class="parameter-default">=0.0</span>, dy<span class="parameter-default">=0.0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__len__" href="#Transform-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__repr__" href="#Transform-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-applyTransformation" href="#Transform-applyTransformation"><span class="function-name">applyTransformation</span></a><span class="argspec">(self, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-inverse" href="#Transform-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-reverseTransform" href="#Transform-reverseTransform"><span class="function-name">reverseTransform</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-rotate" href="#Transform-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-scale" href="#Transform-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-shift" href="#Transform-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-skew" href="#Transform-skew"><span class="function-name">skew</span></a><span class="argspec">(self, ax, ay)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-transform" href="#Transform-transform"><span class="function-name">transform</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-translate" href="#Transform-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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


<a name="typerig.core.objects.transform.Transform"></a>

## `Transform`


<dt class="class"><h2><span class="class-name">typerig.core.objects.transform.Transform</span> = <a name="typerig.core.objects.transform.Transform" href="#typerig.core.objects.transform.Transform">class Transform</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Affine transformations (Object)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Transform-__cmp__" href="#Transform-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__getitem__" href="#Transform-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__getslice__" href="#Transform-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__hash__" href="#Transform-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__init__" href="#Transform-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, xx<span class="parameter-default">=1.0</span>, xy<span class="parameter-default">=0.0</span>, yx<span class="parameter-default">=0.0</span>, yy<span class="parameter-default">=1.0</span>, dx<span class="parameter-default">=0.0</span>, dy<span class="parameter-default">=0.0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__len__" href="#Transform-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-__repr__" href="#Transform-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-applyTransformation" href="#Transform-applyTransformation"><span class="function-name">applyTransformation</span></a><span class="argspec">(self, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-inverse" href="#Transform-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-reverseTransform" href="#Transform-reverseTransform"><span class="function-name">reverseTransform</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-rotate" href="#Transform-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, angle)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-scale" href="#Transform-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-shift" href="#Transform-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-skew" href="#Transform-skew"><span class="function-name">skew</span></a><span class="argspec">(self, ax, ay)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-transform" href="#Transform-transform"><span class="function-name">transform</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Transform-translate" href="#Transform-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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
