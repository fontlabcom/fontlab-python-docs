

<a name="typerig.core.objects.collection"></a>

# `typerig.core.objects.collection`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.collection (<span class="info">version 0.28.6)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Collection (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>json</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></span>(<span class="bases">_abcoll.Mapping</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#biDict">biDict</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.collection.html#extBiDict">extBiDict</a></span></li></ul></li></ul></li><li><span class="class-name"><a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a></span>(<span class="bases">_abcoll.Sequence</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#dimList">dimList</a></span></li></ul></li></ul></li><li><span class="class-name"><a href="./collections.html#defaultdict">collections.defaultdict</a></span>(<span class="bases">__builtin__.dict</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#attribdict">attribdict</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.collection.html#treeDict">treeDict</a></span></li></ul></li><li><span class="class-name"><a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#vfj_decoder">vfj_decoder</a></span></li></ul></li><li><span class="class-name"><a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.collection.html#vfj_encoder">vfj_encoder</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="CustomDict" href="#CustomDict">class <span class="class-name">CustomDict</span></a>(<a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A more or less complete user-defined wrapper around dictionary objects.
Adapted from Source: https://github.com/enthought/Python-2.7.3/blob/master/Lib/self.__class__.py</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CustomDict-__cmp__" href="#CustomDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__contains__" href="#CustomDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__delitem__" href="#CustomDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__getitem__" href="#CustomDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__init__" href="#CustomDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__iter__" href="#CustomDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__len__" href="#CustomDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__repr__" href="#CustomDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__setitem__" href="#CustomDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-clear" href="#CustomDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-copy" href="#CustomDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-get" href="#CustomDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-has_key" href="#CustomDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-items" href="#CustomDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-iteritems" href="#CustomDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-iterkeys" href="#CustomDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-itervalues" href="#CustomDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-keys" href="#CustomDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-pop" href="#CustomDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-popitem" href="#CustomDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-setdefault" href="#CustomDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-update" href="#CustomDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-values" href="#CustomDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods </h4><dl class="function"><dt><a name="CustomDict-fromkeys" href="#CustomDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>
<dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="CustomDict-__eq__" href="#CustomDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__ne__" href="#CustomDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="CustomDict-__subclasshook__" href="#CustomDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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
<dt class="class"><h2><a name="CustomList" href="#CustomList">class <span class="class-name">CustomList</span></a>(<a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A more or less complete user-defined wrapper around list objects.
Adapted from Source: https://github.com/enthought/Python-2.7.3/blob/master/Lib/UserList.py</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></dd><dd><a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CustomList-__add__" href="#CustomList-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__cmp__" href="#CustomList-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__contains__" href="#CustomList-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__delitem__" href="#CustomList-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__delslice__" href="#CustomList-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__eq__" href="#CustomList-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__ge__" href="#CustomList-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__getitem__" href="#CustomList-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__getslice__" href="#CustomList-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__gt__" href="#CustomList-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__iadd__" href="#CustomList-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__imul__" href="#CustomList-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__init__" href="#CustomList-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, initlist<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__le__" href="#CustomList-__le__"><span class="function-name">__le__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__len__" href="#CustomList-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__lt__" href="#CustomList-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__mul__" href="#CustomList-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__ne__" href="#CustomList-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__radd__" href="#CustomList-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__repr__" href="#CustomList-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="CustomList-__rmul__" href="#CustomList-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#CustomList-__mul__">__mul__</a><span class="argspec">(self, n)</span></dt></dl>
<dl class="function"><dt><a name="CustomList-__setitem__" href="#CustomList-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__setslice__" href="#CustomList-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(self, i, j, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-append" href="#CustomList-append"><span class="function-name">append</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-count" href="#CustomList-count"><span class="function-name">count</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-extend" href="#CustomList-extend"><span class="function-name">extend</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-index" href="#CustomList-index"><span class="function-name">index</span></a><span class="argspec">(self, item, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-insert" href="#CustomList-insert"><span class="function-name">insert</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-pop" href="#CustomList-pop"><span class="function-name">pop</span></a><span class="argspec">(self, i<span class="parameter-default">=-1</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-remove" href="#CustomList-remove"><span class="function-name">remove</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-reverse" href="#CustomList-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-sort" href="#CustomList-sort"><span class="function-name">sort</span></a><span class="argspec">(self, *args, **kwds)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>
<dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="CustomList-__iter__" href="#CustomList-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__reversed__" href="#CustomList-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="CustomList-__subclasshook__" href="#CustomList-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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
<dt class="class"><h2><a name="attribdict" href="#attribdict">class <span class="class-name">attribdict</span></a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes.</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#attribdict">attribdict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="attribdict-__delattr__" href="#attribdict-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__getattribute__" href="#attribdict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__hash__" href="#attribdict-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__init__" href="#attribdict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__repr__" href="#attribdict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__setattr__" href="#attribdict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-contains" href="#attribdict-contains"><span class="function-name">contains</span></a><span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Does the object contain ANY value or nested object with given name (search)

Attributes:
        search (Str): Search string
        search_type (type) : Value type

Returns:
        Bool</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-dir" href="#attribdict-dir"><span class="function-name">dir</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-extract" href="#attribdict-extract"><span class="function-name">extract</span></a><span class="argspec">(self, search)</span></dt><dd>

<pre class="doc" markdown="0">Pull all values of specified key (search)

Attributes:
        search (Str): Search string

Returns:
        generator</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-factory" href="#attribdict-factory"><span class="function-name">factory</span></a><span class="argspec">(self, factory_type)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-lock" href="#attribdict-lock"><span class="function-name">lock</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-where" href="#attribdict-where"><span class="function-name">where</span></a><span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Pull all objects that contain values of specified search.

Attributes:
        search (Str): Search string
        search_type (type) : Value type
Returns:
        generator</pre>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="attribdict-__copy__" href="#attribdict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__missing__" href="#attribdict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#attribdict-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#attribdict-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__reduce__" href="#attribdict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-copy" href="#attribdict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="attribdict-__cmp__" href="#attribdict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__contains__" href="#attribdict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__delitem__" href="#attribdict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__eq__" href="#attribdict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__ge__" href="#attribdict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__getitem__" href="#attribdict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__gt__" href="#attribdict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__iter__" href="#attribdict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__le__" href="#attribdict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__len__" href="#attribdict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__lt__" href="#attribdict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__ne__" href="#attribdict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__setitem__" href="#attribdict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#attribdict-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__sizeof__" href="#attribdict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-clear" href="#attribdict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-fromkeys" href="#attribdict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#attribdict-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-get" href="#attribdict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-has_key" href="#attribdict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-items" href="#attribdict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-iteritems" href="#attribdict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-iterkeys" href="#attribdict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-itervalues" href="#attribdict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-keys" href="#attribdict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-pop" href="#attribdict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-popitem" href="#attribdict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-setdefault" href="#attribdict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-setdefault">setdefault</a>(k[,d]) -> D.<a href="#attribdict-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-update" href="#attribdict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#attribdict-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#attribdict-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-values" href="#attribdict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewitems" href="#attribdict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewkeys" href="#attribdict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewvalues" href="#attribdict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#attribdict-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#attribdict-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="biDict" href="#biDict">class <span class="class-name">biDict</span></a>(<a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Bi-directioanl dictionary partly based on Basj answer st:
https://stackoverflow.com/questions/3318625/efficient-bidirectional-hash-table-in-python</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#biDict">biDict</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="biDict-__delitem__" href="#biDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__init__" href="#biDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__setitem__" href="#biDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="biDict-__cmp__" href="#biDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__contains__" href="#biDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__getitem__" href="#biDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__iter__" href="#biDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__len__" href="#biDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__repr__" href="#biDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-clear" href="#biDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-copy" href="#biDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-get" href="#biDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-has_key" href="#biDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-items" href="#biDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-iteritems" href="#biDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-iterkeys" href="#biDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-itervalues" href="#biDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-keys" href="#biDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-pop" href="#biDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-popitem" href="#biDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-setdefault" href="#biDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-update" href="#biDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-values" href="#biDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="biDict-fromkeys" href="#biDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="biDict-__eq__" href="#biDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__ne__" href="#biDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="biDict-__subclasshook__" href="#biDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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
<dt class="class"><h2><a name="dimList" href="#dimList">class <span class="class-name">dimList</span></a>(<a href="./typerig.core.objects.collection.html#CustomList">CustomList</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Custom list object that supports multiple dimensions
Example: 
        a = dimList([[[1, 2, 3, 4], ['a', 'b', 'c', 'd']], [[5, 6, 7, 8], ['e', 'f', 'g', 'h']]])
        print(a[0,1,2])</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#dimList">dimList</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></dd><dd><a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="dimList-__getitem__" href="#dimList-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__init__" href="#dimList-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__setitem__" href="#dimList-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>dim</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></h4><dl class="function"><dt><a name="dimList-__add__" href="#dimList-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__cmp__" href="#dimList-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__contains__" href="#dimList-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__delitem__" href="#dimList-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__delslice__" href="#dimList-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__eq__" href="#dimList-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__ge__" href="#dimList-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__getslice__" href="#dimList-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__gt__" href="#dimList-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__iadd__" href="#dimList-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__imul__" href="#dimList-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__le__" href="#dimList-__le__"><span class="function-name">__le__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__len__" href="#dimList-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__lt__" href="#dimList-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__mul__" href="#dimList-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__ne__" href="#dimList-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__radd__" href="#dimList-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__repr__" href="#dimList-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__rmul__" href="#dimList-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__setslice__" href="#dimList-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(self, i, j, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-append" href="#dimList-append"><span class="function-name">append</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-count" href="#dimList-count"><span class="function-name">count</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-extend" href="#dimList-extend"><span class="function-name">extend</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-index" href="#dimList-index"><span class="function-name">index</span></a><span class="argspec">(self, item, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-insert" href="#dimList-insert"><span class="function-name">insert</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-pop" href="#dimList-pop"><span class="function-name">pop</span></a><span class="argspec">(self, i<span class="parameter-default">=-1</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-remove" href="#dimList-remove"><span class="function-name">remove</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-reverse" href="#dimList-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-sort" href="#dimList-sort"><span class="function-name">sort</span></a><span class="argspec">(self, *args, **kwds)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="dimList-__iter__" href="#dimList-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__reversed__" href="#dimList-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="dimList-__subclasshook__" href="#dimList-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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
<dt class="class"><h2><a name="extBiDict" href="#extBiDict">class <span class="class-name">extBiDict</span></a>(<a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Bi-directioanl dictionary with lists for values</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#extBiDict">extBiDict</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="extBiDict-__delitem__" href="#extBiDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__init__" href="#extBiDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__setitem__" href="#extBiDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="extBiDict-__cmp__" href="#extBiDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__contains__" href="#extBiDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__getitem__" href="#extBiDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__iter__" href="#extBiDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__len__" href="#extBiDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__repr__" href="#extBiDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-clear" href="#extBiDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-copy" href="#extBiDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-get" href="#extBiDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-has_key" href="#extBiDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-items" href="#extBiDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-iteritems" href="#extBiDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-iterkeys" href="#extBiDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-itervalues" href="#extBiDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-keys" href="#extBiDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-pop" href="#extBiDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-popitem" href="#extBiDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-setdefault" href="#extBiDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-update" href="#extBiDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-values" href="#extBiDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="extBiDict-fromkeys" href="#extBiDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="extBiDict-__eq__" href="#extBiDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__ne__" href="#extBiDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="extBiDict-__subclasshook__" href="#extBiDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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
<dt class="class"><h2><span class="class-name">jsontree</span> = <a name="jsontree" href="#jsontree">class treeDict</a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes. Light Version
----
Adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#treeDict">treeDict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="treeDict-__getattribute__" href="#treeDict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__init__" href="#treeDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__repr__" href="#treeDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setattr__" href="#treeDict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="treeDict-__copy__" href="#treeDict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__missing__" href="#treeDict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#jsontree-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#jsontree-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__reduce__" href="#treeDict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-copy" href="#treeDict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="treeDict-__cmp__" href="#treeDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__contains__" href="#treeDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__delitem__" href="#treeDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__eq__" href="#treeDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ge__" href="#treeDict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__getitem__" href="#treeDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__gt__" href="#treeDict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__iter__" href="#treeDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__le__" href="#treeDict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__len__" href="#treeDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__lt__" href="#treeDict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ne__" href="#treeDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setitem__" href="#treeDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#jsontree-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__sizeof__" href="#treeDict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-clear" href="#treeDict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-fromkeys" href="#treeDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#jsontree-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-get" href="#treeDict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-has_key" href="#treeDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-items" href="#treeDict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iteritems" href="#treeDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iterkeys" href="#treeDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-itervalues" href="#treeDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-keys" href="#treeDict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-pop" href="#treeDict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-popitem" href="#treeDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-setdefault" href="#treeDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-setdefault">setdefault</a>(k[,d]) -> D.<a href="#jsontree-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-update" href="#treeDict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#jsontree-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#jsontree-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-values" href="#treeDict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewitems" href="#treeDict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewkeys" href="#treeDict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewvalues" href="#treeDict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#jsontree-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#jsontree-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="treeDict" href="#treeDict">class <span class="class-name">treeDict</span></a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes. Light Version
----
Adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#treeDict">treeDict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="treeDict-__getattribute__" href="#treeDict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__init__" href="#treeDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__repr__" href="#treeDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setattr__" href="#treeDict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="treeDict-__copy__" href="#treeDict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__missing__" href="#treeDict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#treeDict-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#treeDict-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__reduce__" href="#treeDict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-copy" href="#treeDict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="treeDict-__cmp__" href="#treeDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__contains__" href="#treeDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__delitem__" href="#treeDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__eq__" href="#treeDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ge__" href="#treeDict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__getitem__" href="#treeDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__gt__" href="#treeDict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__iter__" href="#treeDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__le__" href="#treeDict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__len__" href="#treeDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__lt__" href="#treeDict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ne__" href="#treeDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setitem__" href="#treeDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#treeDict-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__sizeof__" href="#treeDict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-clear" href="#treeDict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-fromkeys" href="#treeDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#treeDict-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-get" href="#treeDict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-has_key" href="#treeDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-items" href="#treeDict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iteritems" href="#treeDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iterkeys" href="#treeDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-itervalues" href="#treeDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-keys" href="#treeDict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-pop" href="#treeDict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-popitem" href="#treeDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-setdefault" href="#treeDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-setdefault">setdefault</a>(k[,d]) -> D.<a href="#treeDict-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-update" href="#treeDict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#treeDict-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#treeDict-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-values" href="#treeDict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewitems" href="#treeDict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewkeys" href="#treeDict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewvalues" href="#treeDict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#treeDict-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#treeDict-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="vfj_decoder" href="#vfj_decoder">class <span class="class-name">vfj_decoder</span></a>(<a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">VFJ (JSON) decoder class for deserializing to a jsontree object structure.
----
Parts adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#vfj_decoder">vfj_decoder</a></dd><dd><a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="vfj_decoder-__init__" href="#vfj_decoder-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></h4><dl class="function"><dt><a name="vfj_decoder-decode" href="#vfj_decoder-decode"><span class="function-name">decode</span></a><span class="argspec">(self, s, _w<span class="parameter-default">=&lt;built-in method match of _sre.SRE_Pattern object&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the Python representation of ``s`` (a ``str`` or ``unicode``
instance containing a JSON document)</pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_decoder-raw_decode" href="#vfj_decoder-raw_decode"><span class="function-name">raw_decode</span></a><span class="argspec">(self, s, idx<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decode a JSON document from ``s`` (a ``str`` or ``unicode``
beginning with a JSON document) and return a 2-tuple of the Python
representation and the index in ``s`` where the document ended.

This can be used to decode a JSON document from a string that may
have extraneous data at the end.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></h4><dl class="descriptor"><dt>__dict__</dt>
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
<dt class="class"><h2><a name="vfj_encoder" href="#vfj_encoder">class <span class="class-name">vfj_encoder</span></a>(<a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">VFJ (JSON) encoder class that serializes out jsontree object structures.
----
Parts adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#vfj_encoder">vfj_encoder</a></dd><dd><a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="vfj_encoder-__init__" href="#vfj_encoder-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_encoder-default" href="#vfj_encoder-default"><span class="function-name">default</span></a><span class="argspec">(self, obj)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl class="function"><dt><a name="vfj_encoder-encode" href="#vfj_encoder-encode"><span class="function-name">encode</span></a><span class="argspec">(self, o)</span></dt><dd>

<pre class="doc" markdown="0">Return a JSON string representation of a Python data structure.

>>> <a href="./json.encoder.html#JSONEncoder">JSONEncoder</a>().<a href="#vfj_encoder-encode">encode</a>({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'</pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_encoder-iterencode" href="#vfj_encoder-iterencode"><span class="function-name">iterencode</span></a><span class="argspec">(self, o, _one_shot<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Encode the given object and yield each string
representation as available.

For example::

    for chunk in <a href="./json.encoder.html#JSONEncoder">JSONEncoder</a>().<a href="#vfj_encoder-iterencode">iterencode</a>(bigobject):
        mysocket.write(chunk)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl><dt><span class="other-name">item_separator</span> = ', '</dt></dl>
<dl><dt><span class="other-name">key_separator</span> = ': '</dt></dl>
</dd></dl></div></div>


<a name="typerig.core.objects.collection.CustomList"></a>

## `CustomList`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.CustomList</span> = <a name="typerig.core.objects.collection.CustomList" href="#typerig.core.objects.collection.CustomList">class CustomList</a>(<a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A more or less complete user-defined wrapper around list objects.
Adapted from Source: https://github.com/enthought/Python-2.7.3/blob/master/Lib/UserList.py</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></dd><dd><a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CustomList-__add__" href="#CustomList-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__cmp__" href="#CustomList-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__contains__" href="#CustomList-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__delitem__" href="#CustomList-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__delslice__" href="#CustomList-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__eq__" href="#CustomList-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__ge__" href="#CustomList-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__getitem__" href="#CustomList-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__getslice__" href="#CustomList-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__gt__" href="#CustomList-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__iadd__" href="#CustomList-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__imul__" href="#CustomList-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__init__" href="#CustomList-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, initlist<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__le__" href="#CustomList-__le__"><span class="function-name">__le__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__len__" href="#CustomList-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__lt__" href="#CustomList-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__mul__" href="#CustomList-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__ne__" href="#CustomList-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__radd__" href="#CustomList-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__repr__" href="#CustomList-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl><dt><a name="CustomList-__rmul__" href="#CustomList-__rmul__"><span class="function-name">__rmul__</span></a> = <a href="#CustomList-__mul__">__mul__</a><span class="argspec">(self, n)</span></dt></dl>
<dl class="function"><dt><a name="CustomList-__setitem__" href="#CustomList-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__setslice__" href="#CustomList-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(self, i, j, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-append" href="#CustomList-append"><span class="function-name">append</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-count" href="#CustomList-count"><span class="function-name">count</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-extend" href="#CustomList-extend"><span class="function-name">extend</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-index" href="#CustomList-index"><span class="function-name">index</span></a><span class="argspec">(self, item, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-insert" href="#CustomList-insert"><span class="function-name">insert</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-pop" href="#CustomList-pop"><span class="function-name">pop</span></a><span class="argspec">(self, i<span class="parameter-default">=-1</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-remove" href="#CustomList-remove"><span class="function-name">remove</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-reverse" href="#CustomList-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-sort" href="#CustomList-sort"><span class="function-name">sort</span></a><span class="argspec">(self, *args, **kwds)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>
<dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="CustomList-__iter__" href="#CustomList-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomList-__reversed__" href="#CustomList-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="CustomList-__subclasshook__" href="#CustomList-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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


<a name="typerig.core.objects.collection.dimList"></a>

## `dimList`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.dimList</span> = <a name="typerig.core.objects.collection.dimList" href="#typerig.core.objects.collection.dimList">class dimList</a>(<a href="./typerig.core.objects.collection.html#CustomList">CustomList</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Custom list object that supports multiple dimensions
Example: 
        a = dimList([[[1, 2, 3, 4], ['a', 'b', 'c', 'd']], [[5, 6, 7, 8], ['e', 'f', 'g', 'h']]])
        print(a[0,1,2])</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#dimList">dimList</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></dd><dd><a href="./_abcoll.html#MutableSequence">_abcoll.MutableSequence</a></dd><dd><a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="dimList-__getitem__" href="#dimList-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__init__" href="#dimList-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__setitem__" href="#dimList-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>dim</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></h4><dl class="function"><dt><a name="dimList-__add__" href="#dimList-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__cmp__" href="#dimList-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__contains__" href="#dimList-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__delitem__" href="#dimList-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, i)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__delslice__" href="#dimList-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__eq__" href="#dimList-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__ge__" href="#dimList-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__getslice__" href="#dimList-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__gt__" href="#dimList-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__iadd__" href="#dimList-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__imul__" href="#dimList-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__le__" href="#dimList-__le__"><span class="function-name">__le__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__len__" href="#dimList-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__lt__" href="#dimList-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__mul__" href="#dimList-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__ne__" href="#dimList-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__radd__" href="#dimList-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__repr__" href="#dimList-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__rmul__" href="#dimList-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, n)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__setslice__" href="#dimList-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(self, i, j, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-append" href="#dimList-append"><span class="function-name">append</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-count" href="#dimList-count"><span class="function-name">count</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-extend" href="#dimList-extend"><span class="function-name">extend</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-index" href="#dimList-index"><span class="function-name">index</span></a><span class="argspec">(self, item, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-insert" href="#dimList-insert"><span class="function-name">insert</span></a><span class="argspec">(self, i, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-pop" href="#dimList-pop"><span class="function-name">pop</span></a><span class="argspec">(self, i<span class="parameter-default">=-1</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-remove" href="#dimList-remove"><span class="function-name">remove</span></a><span class="argspec">(self, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-reverse" href="#dimList-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-sort" href="#dimList-sort"><span class="function-name">sort</span></a><span class="argspec">(self, *args, **kwds)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomList">CustomList</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Sequence">_abcoll.Sequence</a></h4><dl class="function"><dt><a name="dimList-__iter__" href="#dimList-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="dimList-__reversed__" href="#dimList-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="dimList-__subclasshook__" href="#dimList-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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


<a name="typerig.core.objects.collection.CustomDict"></a>

## `CustomDict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.CustomDict</span> = <a name="typerig.core.objects.collection.CustomDict" href="#typerig.core.objects.collection.CustomDict">class CustomDict</a>(<a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A more or less complete user-defined wrapper around dictionary objects.
Adapted from Source: https://github.com/enthought/Python-2.7.3/blob/master/Lib/self.__class__.py</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CustomDict-__cmp__" href="#CustomDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__contains__" href="#CustomDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__delitem__" href="#CustomDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__getitem__" href="#CustomDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__init__" href="#CustomDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__iter__" href="#CustomDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__len__" href="#CustomDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__repr__" href="#CustomDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__setitem__" href="#CustomDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, item)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-clear" href="#CustomDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-copy" href="#CustomDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-get" href="#CustomDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-has_key" href="#CustomDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-items" href="#CustomDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-iteritems" href="#CustomDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-iterkeys" href="#CustomDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-itervalues" href="#CustomDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-keys" href="#CustomDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-pop" href="#CustomDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-popitem" href="#CustomDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-setdefault" href="#CustomDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-update" href="#CustomDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-values" href="#CustomDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods </h4><dl class="function"><dt><a name="CustomDict-fromkeys" href="#CustomDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>
<dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="CustomDict-__eq__" href="#CustomDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CustomDict-__ne__" href="#CustomDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="CustomDict-__subclasshook__" href="#CustomDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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


<a name="typerig.core.objects.collection.biDict"></a>

## `biDict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.biDict</span> = <a name="typerig.core.objects.collection.biDict" href="#typerig.core.objects.collection.biDict">class biDict</a>(<a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Bi-directioanl dictionary partly based on Basj answer st:
https://stackoverflow.com/questions/3318625/efficient-bidirectional-hash-table-in-python</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#biDict">biDict</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="biDict-__delitem__" href="#biDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__init__" href="#biDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__setitem__" href="#biDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="biDict-__cmp__" href="#biDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__contains__" href="#biDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__getitem__" href="#biDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__iter__" href="#biDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__len__" href="#biDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__repr__" href="#biDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-clear" href="#biDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-copy" href="#biDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-get" href="#biDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-has_key" href="#biDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-items" href="#biDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-iteritems" href="#biDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-iterkeys" href="#biDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-itervalues" href="#biDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-keys" href="#biDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-pop" href="#biDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-popitem" href="#biDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-setdefault" href="#biDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-update" href="#biDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-values" href="#biDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="biDict-fromkeys" href="#biDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="biDict-__eq__" href="#biDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="biDict-__ne__" href="#biDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="biDict-__subclasshook__" href="#biDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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


<a name="typerig.core.objects.collection.extBiDict"></a>

## `extBiDict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.extBiDict</span> = <a name="typerig.core.objects.collection.extBiDict" href="#typerig.core.objects.collection.extBiDict">class extBiDict</a>(<a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Bi-directioanl dictionary with lists for values</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#extBiDict">extBiDict</a></dd><dd><a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></dd><dd><a href="./_abcoll.html#MutableMapping">_abcoll.MutableMapping</a></dd><dd><a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></dd><dd><a href="./_abcoll.html#Sized">_abcoll.Sized</a></dd><dd><a href="./_abcoll.html#Iterable">_abcoll.Iterable</a></dd><dd><a href="./_abcoll.html#Container">_abcoll.Container</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="extBiDict-__delitem__" href="#extBiDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__init__" href="#extBiDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__setitem__" href="#extBiDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, key, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__abstractmethods__</span> = frozenset([])</dt></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="extBiDict-__cmp__" href="#extBiDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(self, dict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__contains__" href="#extBiDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__getitem__" href="#extBiDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__iter__" href="#extBiDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__len__" href="#extBiDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__repr__" href="#extBiDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-clear" href="#extBiDict-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-copy" href="#extBiDict-copy"><span class="function-name">copy</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-get" href="#extBiDict-get"><span class="function-name">get</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-has_key" href="#extBiDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-items" href="#extBiDict-items"><span class="function-name">items</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-iteritems" href="#extBiDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-iterkeys" href="#extBiDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-itervalues" href="#extBiDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-keys" href="#extBiDict-keys"><span class="function-name">keys</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-pop" href="#extBiDict-pop"><span class="function-name">pop</span></a><span class="argspec">(self, key, *args)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-popitem" href="#extBiDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-setdefault" href="#extBiDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(self, key, failobj<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-update" href="#extBiDict-update"><span class="function-name">update</span></a><span class="argspec">(self, dict<span class="parameter-default">=None</span>, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-values" href="#extBiDict-values"><span class="function-name">values</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl class="function"><dt><a name="extBiDict-fromkeys" href="#extBiDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(cls, iterable, value<span class="parameter-default">=None</span>)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.collection.html#CustomDict">CustomDict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>

  <h4 class="head-methods">Methods from <a href="./_abcoll.html#Mapping">_abcoll.Mapping</a></h4><dl class="function"><dt><a name="extBiDict-__eq__" href="#extBiDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="extBiDict-__ne__" href="#extBiDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-class-methods">Class methods from <a href="./_abcoll.html#Sized">_abcoll.Sized</a></h4><dl class="function"><dt><a name="extBiDict-__subclasshook__" href="#extBiDict-__subclasshook__"><span class="function-name">__subclasshook__</span></a><span class="argspec">(cls, C)</span><span class="note"> from <a href="./abc.html#ABCMeta">abc.ABCMeta</a></span></dt><dd>

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


<a name="typerig.core.objects.collection.attribdict"></a>

## `attribdict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.attribdict</span> = <a name="typerig.core.objects.collection.attribdict" href="#typerig.core.objects.collection.attribdict">class attribdict</a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes.</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#attribdict">attribdict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="attribdict-__delattr__" href="#attribdict-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__getattribute__" href="#attribdict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__hash__" href="#attribdict-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__init__" href="#attribdict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__repr__" href="#attribdict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__setattr__" href="#attribdict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-contains" href="#attribdict-contains"><span class="function-name">contains</span></a><span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Does the object contain ANY value or nested object with given name (search)

Attributes:
        search (Str): Search string
        search_type (type) : Value type

Returns:
        Bool</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-dir" href="#attribdict-dir"><span class="function-name">dir</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-extract" href="#attribdict-extract"><span class="function-name">extract</span></a><span class="argspec">(self, search)</span></dt><dd>

<pre class="doc" markdown="0">Pull all values of specified key (search)

Attributes:
        search (Str): Search string

Returns:
        generator</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-factory" href="#attribdict-factory"><span class="function-name">factory</span></a><span class="argspec">(self, factory_type)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-lock" href="#attribdict-lock"><span class="function-name">lock</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-where" href="#attribdict-where"><span class="function-name">where</span></a><span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Pull all objects that contain values of specified search.

Attributes:
        search (Str): Search string
        search_type (type) : Value type
Returns:
        generator</pre>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="attribdict-__copy__" href="#attribdict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__missing__" href="#attribdict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#typerig.core.objects.collection.attribdict-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#typerig.core.objects.collection.attribdict-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__reduce__" href="#attribdict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-copy" href="#attribdict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="attribdict-__cmp__" href="#attribdict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__contains__" href="#attribdict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__delitem__" href="#attribdict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__eq__" href="#attribdict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__ge__" href="#attribdict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__getitem__" href="#attribdict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__gt__" href="#attribdict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__iter__" href="#attribdict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__le__" href="#attribdict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__len__" href="#attribdict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__lt__" href="#attribdict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__ne__" href="#attribdict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__setitem__" href="#attribdict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.attribdict-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-__sizeof__" href="#attribdict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-clear" href="#attribdict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-fromkeys" href="#attribdict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#typerig.core.objects.collection.attribdict-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-get" href="#attribdict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-has_key" href="#attribdict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-items" href="#attribdict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-iteritems" href="#attribdict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-iterkeys" href="#attribdict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-itervalues" href="#attribdict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-keys" href="#attribdict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-pop" href="#attribdict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-popitem" href="#attribdict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-setdefault" href="#attribdict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-setdefault">setdefault</a>(k[,d]) -> D.<a href="#typerig.core.objects.collection.attribdict-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-update" href="#attribdict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#typerig.core.objects.collection.attribdict-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#typerig.core.objects.collection.attribdict-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-values" href="#attribdict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewitems" href="#attribdict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewkeys" href="#attribdict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="attribdict-viewvalues" href="#attribdict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.attribdict-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.collection.attribdict-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.collection.attribdict.extract"></a>

### `extract`


<dl class="function"><dt><a name="-typerig.core.objects.collection.attribdict.extract" href="#-typerig.core.objects.collection.attribdict.extract"><span class="function-name">typerig.core.objects.collection.attribdict.extract</span></a> = extract<span class="argspec">(self, search)</span><span class="note"> unbound <a href="./typerig.core.objects.collection.html#attribdict">typerig.core.objects.collection.attribdict</a> method</span></dt><dd>

<pre class="doc" markdown="0">Pull all values of specified key (search)

Attributes:
        search (Str): Search string

Returns:
        generator</pre>

</dd></dl>



<a name="typerig.core.objects.collection.attribdict.where"></a>

### `where`


<dl class="function"><dt><a name="-typerig.core.objects.collection.attribdict.where" href="#-typerig.core.objects.collection.attribdict.where"><span class="function-name">typerig.core.objects.collection.attribdict.where</span></a> = where<span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.collection.html#attribdict">typerig.core.objects.collection.attribdict</a> method</span></dt><dd>

<pre class="doc" markdown="0">Pull all objects that contain values of specified search.

Attributes:
        search (Str): Search string
        search_type (type) : Value type
Returns:
        generator</pre>

</dd></dl>



<a name="typerig.core.objects.collection.attribdict.contains"></a>

### `contains`


<dl class="function"><dt><a name="-typerig.core.objects.collection.attribdict.contains" href="#-typerig.core.objects.collection.attribdict.contains"><span class="function-name">typerig.core.objects.collection.attribdict.contains</span></a> = contains<span class="argspec">(self, search, search_type<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.collection.html#attribdict">typerig.core.objects.collection.attribdict</a> method</span></dt><dd>

<pre class="doc" markdown="0">Does the object contain ANY value or nested object with given name (search)

Attributes:
        search (Str): Search string
        search_type (type) : Value type

Returns:
        Bool</pre>

</dd></dl>



<a name="typerig.core.objects.collection.treeDict"></a>

## `treeDict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.treeDict</span> = <a name="typerig.core.objects.collection.treeDict" href="#typerig.core.objects.collection.treeDict">class treeDict</a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes. Light Version
----
Adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#treeDict">treeDict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="treeDict-__getattribute__" href="#treeDict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__init__" href="#treeDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__repr__" href="#treeDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setattr__" href="#treeDict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="treeDict-__copy__" href="#treeDict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__missing__" href="#treeDict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#typerig.core.objects.collection.treeDict-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#typerig.core.objects.collection.treeDict-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__reduce__" href="#treeDict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-copy" href="#treeDict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="treeDict-__cmp__" href="#treeDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__contains__" href="#treeDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__delitem__" href="#treeDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__eq__" href="#treeDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ge__" href="#treeDict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__getitem__" href="#treeDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__gt__" href="#treeDict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__iter__" href="#treeDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__le__" href="#treeDict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__len__" href="#treeDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__lt__" href="#treeDict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ne__" href="#treeDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setitem__" href="#treeDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.treeDict-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__sizeof__" href="#treeDict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-clear" href="#treeDict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-fromkeys" href="#treeDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#typerig.core.objects.collection.treeDict-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-get" href="#treeDict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-has_key" href="#treeDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-items" href="#treeDict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iteritems" href="#treeDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iterkeys" href="#treeDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-itervalues" href="#treeDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-keys" href="#treeDict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-pop" href="#treeDict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-popitem" href="#treeDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-setdefault" href="#treeDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-setdefault">setdefault</a>(k[,d]) -> D.<a href="#typerig.core.objects.collection.treeDict-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-update" href="#treeDict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#typerig.core.objects.collection.treeDict-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#typerig.core.objects.collection.treeDict-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-values" href="#treeDict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewitems" href="#treeDict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewkeys" href="#treeDict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewvalues" href="#treeDict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.treeDict-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.collection.treeDict-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.collection.jsontree"></a>

## `treeDict`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.jsontree</span> = <a name="typerig.core.objects.collection.jsontree" href="#typerig.core.objects.collection.jsontree">class treeDict</a>(<a href="./collections.html#defaultdict">collections.defaultdict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Default dictionary where keys can be accessed as attributes. Light Version
----
Adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#treeDict">treeDict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="treeDict-__getattribute__" href="#treeDict-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__init__" href="#treeDict-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__repr__" href="#treeDict-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setattr__" href="#treeDict-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

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

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="treeDict-__copy__" href="#treeDict-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__missing__" href="#treeDict-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#typerig.core.objects.collection.jsontree-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#typerig.core.objects.collection.jsontree-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__reduce__" href="#treeDict-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-copy" href="#treeDict-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="treeDict-__cmp__" href="#treeDict-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__contains__" href="#treeDict-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__delitem__" href="#treeDict-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__eq__" href="#treeDict-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ge__" href="#treeDict-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__getitem__" href="#treeDict-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__gt__" href="#treeDict-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__iter__" href="#treeDict-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__le__" href="#treeDict-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__len__" href="#treeDict-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__lt__" href="#treeDict-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__ne__" href="#treeDict-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__setitem__" href="#treeDict-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.collection.jsontree-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-__sizeof__" href="#treeDict-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-clear" href="#treeDict-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-fromkeys" href="#treeDict-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#typerig.core.objects.collection.jsontree-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-get" href="#treeDict-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-has_key" href="#treeDict-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-items" href="#treeDict-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iteritems" href="#treeDict-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-iterkeys" href="#treeDict-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-itervalues" href="#treeDict-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-keys" href="#treeDict-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-pop" href="#treeDict-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-popitem" href="#treeDict-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-setdefault" href="#treeDict-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-setdefault">setdefault</a>(k[,d]) -> D.<a href="#typerig.core.objects.collection.jsontree-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-update" href="#treeDict-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#typerig.core.objects.collection.jsontree-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#typerig.core.objects.collection.jsontree-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-values" href="#treeDict-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewitems" href="#treeDict-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-viewitems">viewitems</a>() -> a set-like object providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewkeys" href="#treeDict-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-viewkeys">viewkeys</a>() -> a set-like object providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="treeDict-viewvalues" href="#treeDict-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#typerig.core.objects.collection.jsontree-viewvalues">viewvalues</a>() -> an object providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.collection.jsontree-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.collection.vfj_decoder"></a>

## `vfj_decoder`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.vfj_decoder</span> = <a name="typerig.core.objects.collection.vfj_decoder" href="#typerig.core.objects.collection.vfj_decoder">class vfj_decoder</a>(<a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">VFJ (JSON) decoder class for deserializing to a jsontree object structure.
----
Parts adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#vfj_decoder">vfj_decoder</a></dd><dd><a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="vfj_decoder-__init__" href="#vfj_decoder-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></h4><dl class="function"><dt><a name="vfj_decoder-decode" href="#vfj_decoder-decode"><span class="function-name">decode</span></a><span class="argspec">(self, s, _w<span class="parameter-default">=&lt;built-in method match of _sre.SRE_Pattern object&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the Python representation of ``s`` (a ``str`` or ``unicode``
instance containing a JSON document)</pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_decoder-raw_decode" href="#vfj_decoder-raw_decode"><span class="function-name">raw_decode</span></a><span class="argspec">(self, s, idx<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Decode a JSON document from ``s`` (a ``str`` or ``unicode``
beginning with a JSON document) and return a 2-tuple of the Python
representation and the index in ``s`` where the document ended.

This can be used to decode a JSON document from a string that may
have extraneous data at the end.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./json.decoder.html#JSONDecoder">json.decoder.JSONDecoder</a></h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.core.objects.collection.vfj_encoder"></a>

## `vfj_encoder`


<dt class="class"><h2><span class="class-name">typerig.core.objects.collection.vfj_encoder</span> = <a name="typerig.core.objects.collection.vfj_encoder" href="#typerig.core.objects.collection.vfj_encoder">class vfj_encoder</a>(<a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">VFJ (JSON) encoder class that serializes out jsontree object structures.
----
Parts adapted from JsonTree by Doug Napoleone: https://github.com/dougn/jsontree</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.collection.html#vfj_encoder">vfj_encoder</a></dd><dd><a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="vfj_encoder-__init__" href="#vfj_encoder-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwdargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_encoder-default" href="#vfj_encoder-default"><span class="function-name">default</span></a><span class="argspec">(self, obj)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl class="function"><dt><a name="vfj_encoder-encode" href="#vfj_encoder-encode"><span class="function-name">encode</span></a><span class="argspec">(self, o)</span></dt><dd>

<pre class="doc" markdown="0">Return a JSON string representation of a Python data structure.

>>> JSONEncoder().<a href="#typerig.core.objects.collection.vfj_encoder-encode">encode</a>({"foo": ["bar", "baz"]})
'{"foo": ["bar", "baz"]}'</pre>

</dd></dl>
<dl class="function"><dt><a name="vfj_encoder-iterencode" href="#vfj_encoder-iterencode"><span class="function-name">iterencode</span></a><span class="argspec">(self, o, _one_shot<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Encode the given object and yield each string
representation as available.

For example::

    for chunk in JSONEncoder().<a href="#typerig.core.objects.collection.vfj_encoder-iterencode">iterencode</a>(bigobject):
        mysocket.write(chunk)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./json.encoder.html#JSONEncoder">json.encoder.JSONEncoder</a></h4><dl><dt><span class="other-name">item_separator</span> = ', '</dt></dl>
<dl><dt><span class="other-name">key_separator</span> = ': '</dt></dl>
</dd>
