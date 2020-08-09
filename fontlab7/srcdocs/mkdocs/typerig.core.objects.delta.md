

<a name="typerig.core.objects.delta"></a>

# `typerig.core.objects.delta`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.delta (<span class="info">version 0.10.4)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Delta (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li><li>typerig.core.func.transform</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></span>(<span class="bases">_abcoll.Sized, _abcoll.Iterable, _abcoll.Container</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.delta.html#DeltaArray">DeltaArray</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.delta.html#DeltaScale">DeltaScale</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="DeltaArray" href="#DeltaArray">class <span class="class-name">DeltaArray</span></a>(<a href="./_abcoll.html#Sequence">_abcoll.Sequence</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Objects ------------------------------------
# -- Interpolation ------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.delta.html#DeltaArray">DeltaArray</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="DeltaArray-__call__" href="#DeltaArray-__call__"><span class="function-name">__call__</span></a><span class="argspec">(self, global_time, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Linear interpolation (LERP) with optional extrapolation.
Interval (-inf) <-- (0 .. len(array)-1) --> (+inf) (supports negative indexing).</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__getitem__" href="#DeltaArray-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"># - Internals</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__hash__" href="#DeltaArray-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__init__" href="#DeltaArray-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__len__" href="#DeltaArray-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__repr__" href="#DeltaArray-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-mixer" href="#DeltaArray-mixer"><span class="function-name">mixer</span></a><span class="argspec">(self, global_time)</span></dt><dd>

<pre class="doc" markdown="0">Will return the proper coordinate values for the selected global time.</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-timer" href="#DeltaArray-timer"><span class="function-name">timer</span></a><span class="argspec">(self, global_time, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="DeltaArray-__contains__" href="#DeltaArray-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__iter__" href="#DeltaArray-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__reversed__" href="#DeltaArray-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-count" href="#DeltaArray-count"><span class="function-name">count</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#DeltaArray-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-index" href="#DeltaArray-index"><span class="function-name">index</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#DeltaArray-index">index</a>(value) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="DeltaArray-__subclasshook__" href="#DeltaArray-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl><dt><span class="other-name">__metaclass__</span> = &lt;class 'abc.ABCMeta'&gt;<dd>

<pre class="doc" markdown="0">Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="DeltaScale" href="#DeltaScale">class <span class="class-name">DeltaScale</span></a>(<a href="./_abcoll.html#Sequence">_abcoll.Sequence</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.delta.html#DeltaScale">DeltaScale</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="DeltaScale-__getitem__" href="#DeltaScale-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-__init__" href="#DeltaScale-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-__len__" href="#DeltaScale-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-__repr__" href="#DeltaScale-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Internals ----------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-dump" href="#DeltaScale-dump"><span class="function-name">dump</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - IO ---------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-load" href="#DeltaScale-load"><span class="function-name">load</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-scale_by_stem" href="#DeltaScale-scale_by_stem"><span class="function-name">scale_by_stem</span></a><span class="argspec">(self, stem, scale, comp, shift, italic_angle, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-scale_by_time" href="#DeltaScale-scale_by_time"><span class="function-name">scale_by_time</span></a><span class="argspec">(self, time, scale, comp, shift, italic_angle, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Process ----------------------------------</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>dim</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>
<dl><dt><span class="other-name">__setitem__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="DeltaScale-__contains__" href="#DeltaScale-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-__iter__" href="#DeltaScale-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-__reversed__" href="#DeltaScale-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-count" href="#DeltaScale-count"><span class="function-name">count</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#DeltaScale-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaScale-index" href="#DeltaScale-index"><span class="function-name">index</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#DeltaScale-index">index</a>(value) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="DeltaScale-__subclasshook__" href="#DeltaScale-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl><dt><span class="other-name">__metaclass__</span> = &lt;class 'abc.ABCMeta'&gt;<dd>

<pre class="doc" markdown="0">Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).</pre>

</dd></dl>
</dd></dl></div></div>


<a name="typerig.core.objects.delta.DeltaArray"></a>

## `DeltaArray`


<dt class="class"><h2><span class="class-name">typerig.core.objects.delta.DeltaArray</span> = <a name="typerig.core.objects.delta.DeltaArray" href="#typerig.core.objects.delta.DeltaArray">class DeltaArray</a>(<a href="./_abcoll.html#Sequence">_abcoll.Sequence</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Objects ------------------------------------
# -- Interpolation ------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.delta.html#DeltaArray">DeltaArray</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="DeltaArray-__call__" href="#DeltaArray-__call__"><span class="function-name">__call__</span></a><span class="argspec">(self, global_time, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Linear interpolation (LERP) with optional extrapolation.
Interval (-inf) <-- (0 .. len(array)-1) --> (+inf) (supports negative indexing).</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__getitem__" href="#DeltaArray-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"># - Internals</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__hash__" href="#DeltaArray-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__init__" href="#DeltaArray-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__len__" href="#DeltaArray-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__repr__" href="#DeltaArray-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-mixer" href="#DeltaArray-mixer"><span class="function-name">mixer</span></a><span class="argspec">(self, global_time)</span></dt><dd>

<pre class="doc" markdown="0">Will return the proper coordinate values for the selected global time.</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-timer" href="#DeltaArray-timer"><span class="function-name">timer</span></a><span class="argspec">(self, global_time, extrapolate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="DeltaArray-__contains__" href="#DeltaArray-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__iter__" href="#DeltaArray-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-__reversed__" href="#DeltaArray-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-count" href="#DeltaArray-count"><span class="function-name">count</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#typerig.core.objects.delta.DeltaArray-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="DeltaArray-index" href="#DeltaArray-index"><span class="function-name">index</span></a><span class="argspec">(self, value)</span></dt><dd>

<pre class="doc" markdown="0">S.<a href="#typerig.core.objects.delta.DeltaArray-index">index</a>(value) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="DeltaArray-__subclasshook__" href="#DeltaArray-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl><dt><span class="other-name">__metaclass__</span> = &lt;class 'abc.ABCMeta'&gt;<dd>

<pre class="doc" markdown="0">Metaclass for defining Abstract Base Classes (ABCs).

Use this metaclass to create an ABC.  An ABC can be subclassed
directly, and then acts as a mix-in class.  You can also register
unrelated concrete classes (even built-in classes) and unrelated
ABCs as 'virtual subclasses' -- these and their descendants will
be considered subclasses of the registering ABC by the built-in
issubclass() function, but the registering ABC won't show up in
their MRO (Method Resolution Order) nor will method
implementations defined by the registering ABC be callable (not
even via super()).</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.delta.DeltaArray.mixer"></a>

### `mixer`


<dl class="function"><dt><a name="-typerig.core.objects.delta.DeltaArray.mixer" href="#-typerig.core.objects.delta.DeltaArray.mixer"><span class="function-name">typerig.core.objects.delta.DeltaArray.mixer</span></a> = mixer<span class="argspec">(self, global_time)</span><span class="note"> unbound <a href="./typerig.core.objects.delta.html#DeltaArray">typerig.core.objects.delta.DeltaArray</a> method</span></dt><dd>

<pre class="doc" markdown="0">Will return the proper coordinate values for the selected global time.</pre>

</dd></dl>

