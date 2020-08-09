

<a name="typerig.core.base.message"></a>

# `typerig.core.base.message`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.base.html">base</a>.message (<span class="info">version 0.0.2)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Base / Messages (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2020             (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>os</li><li>warnings</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></span>(<span class="bases">exceptions.Warning</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.base.message.html#ContourWarning">ContourWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#FileImportWarning">FileImportWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#FileOpenWarning">FileOpenWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#FileSaveWarning">FileSaveWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#FontWarning">FontWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#GlyphWarning">GlyphWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#JSONimportWarning">JSONimportWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#LayerWarning">LayerWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#NAMdataMissing">NAMdataMissing</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#NAMimportWarning">NAMimportWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#NodeWarning">NodeWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#SVGimportWarning">SVGimportWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#TXTimportWarning">TXTimportWarning</a></span></li><li><span class="class-name"><a href="./typerig.core.base.message.html#VFJimportWarning">VFJimportWarning</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="ContourWarning" href="#ContourWarning">class <span class="class-name">ContourWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#ContourWarning">ContourWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="ContourWarning-__init__" href="#ContourWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#ContourWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="ContourWarning-__delattr__" href="#ContourWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__getattribute__" href="#ContourWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__getitem__" href="#ContourWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__getslice__" href="#ContourWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__reduce__" href="#ContourWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__repr__" href="#ContourWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__setattr__" href="#ContourWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__setstate__" href="#ContourWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__str__" href="#ContourWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#ContourWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="ContourWarning-__unicode__" href="#ContourWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="FileImportWarning" href="#FileImportWarning">class <span class="class-name">FileImportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#FileImportWarning">FileImportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="FileImportWarning-__init__" href="#FileImportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FileImportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="FileImportWarning-__delattr__" href="#FileImportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__getattribute__" href="#FileImportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__getitem__" href="#FileImportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__getslice__" href="#FileImportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__reduce__" href="#FileImportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__repr__" href="#FileImportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__setattr__" href="#FileImportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__setstate__" href="#FileImportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__str__" href="#FileImportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileImportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileImportWarning-__unicode__" href="#FileImportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="FileOpenWarning" href="#FileOpenWarning">class <span class="class-name">FileOpenWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#FileOpenWarning">FileOpenWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="FileOpenWarning-__init__" href="#FileOpenWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FileOpenWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="FileOpenWarning-__delattr__" href="#FileOpenWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__getattribute__" href="#FileOpenWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__getitem__" href="#FileOpenWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__getslice__" href="#FileOpenWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__reduce__" href="#FileOpenWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__repr__" href="#FileOpenWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__setattr__" href="#FileOpenWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__setstate__" href="#FileOpenWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__str__" href="#FileOpenWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileOpenWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileOpenWarning-__unicode__" href="#FileOpenWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="FileSaveWarning" href="#FileSaveWarning">class <span class="class-name">FileSaveWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># -- IO Related ---------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#FileSaveWarning">FileSaveWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="FileSaveWarning-__init__" href="#FileSaveWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FileSaveWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="FileSaveWarning-__delattr__" href="#FileSaveWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__getattribute__" href="#FileSaveWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__getitem__" href="#FileSaveWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__getslice__" href="#FileSaveWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__reduce__" href="#FileSaveWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__repr__" href="#FileSaveWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__setattr__" href="#FileSaveWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__setstate__" href="#FileSaveWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__str__" href="#FileSaveWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FileSaveWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FileSaveWarning-__unicode__" href="#FileSaveWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="FontWarning" href="#FontWarning">class <span class="class-name">FontWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#FontWarning">FontWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="FontWarning-__init__" href="#FontWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FontWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="FontWarning-__delattr__" href="#FontWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__getattribute__" href="#FontWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__getitem__" href="#FontWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__getslice__" href="#FontWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__reduce__" href="#FontWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__repr__" href="#FontWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__setattr__" href="#FontWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__setstate__" href="#FontWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__str__" href="#FontWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FontWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="FontWarning-__unicode__" href="#FontWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="GlyphWarning" href="#GlyphWarning">class <span class="class-name">GlyphWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#GlyphWarning">GlyphWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="GlyphWarning-__init__" href="#GlyphWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#GlyphWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="GlyphWarning-__delattr__" href="#GlyphWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__getattribute__" href="#GlyphWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__getitem__" href="#GlyphWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__getslice__" href="#GlyphWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__reduce__" href="#GlyphWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__repr__" href="#GlyphWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__setattr__" href="#GlyphWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__setstate__" href="#GlyphWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__str__" href="#GlyphWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#GlyphWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="GlyphWarning-__unicode__" href="#GlyphWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="JSONimportWarning" href="#JSONimportWarning">class <span class="class-name">JSONimportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#JSONimportWarning">JSONimportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="JSONimportWarning-__init__" href="#JSONimportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#JSONimportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="JSONimportWarning-__delattr__" href="#JSONimportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__getattribute__" href="#JSONimportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__getitem__" href="#JSONimportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__getslice__" href="#JSONimportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__reduce__" href="#JSONimportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__repr__" href="#JSONimportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__setattr__" href="#JSONimportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__setstate__" href="#JSONimportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__str__" href="#JSONimportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#JSONimportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="JSONimportWarning-__unicode__" href="#JSONimportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="LayerWarning" href="#LayerWarning">class <span class="class-name">LayerWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#LayerWarning">LayerWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="LayerWarning-__init__" href="#LayerWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#LayerWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="LayerWarning-__delattr__" href="#LayerWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__getattribute__" href="#LayerWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__getitem__" href="#LayerWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__getslice__" href="#LayerWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__reduce__" href="#LayerWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__repr__" href="#LayerWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__setattr__" href="#LayerWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__setstate__" href="#LayerWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__str__" href="#LayerWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LayerWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="LayerWarning-__unicode__" href="#LayerWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="NAMdataMissing" href="#NAMdataMissing">class <span class="class-name">NAMdataMissing</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#NAMdataMissing">NAMdataMissing</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="NAMdataMissing-__init__" href="#NAMdataMissing-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#NAMdataMissing-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="NAMdataMissing-__delattr__" href="#NAMdataMissing-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__getattribute__" href="#NAMdataMissing-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__getitem__" href="#NAMdataMissing-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__getslice__" href="#NAMdataMissing-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__reduce__" href="#NAMdataMissing-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__repr__" href="#NAMdataMissing-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__setattr__" href="#NAMdataMissing-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__setstate__" href="#NAMdataMissing-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__str__" href="#NAMdataMissing-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMdataMissing-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMdataMissing-__unicode__" href="#NAMdataMissing-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="NAMimportWarning" href="#NAMimportWarning">class <span class="class-name">NAMimportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#NAMimportWarning">NAMimportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="NAMimportWarning-__init__" href="#NAMimportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#NAMimportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="NAMimportWarning-__delattr__" href="#NAMimportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__getattribute__" href="#NAMimportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__getitem__" href="#NAMimportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__getslice__" href="#NAMimportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__reduce__" href="#NAMimportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__repr__" href="#NAMimportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__setattr__" href="#NAMimportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__setstate__" href="#NAMimportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__str__" href="#NAMimportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NAMimportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NAMimportWarning-__unicode__" href="#NAMimportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="NodeWarning" href="#NodeWarning">class <span class="class-name">NodeWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Warnings -------------------------
# -- Font related --------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#NodeWarning">NodeWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="NodeWarning-__init__" href="#NodeWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#NodeWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="NodeWarning-__delattr__" href="#NodeWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__getattribute__" href="#NodeWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__getitem__" href="#NodeWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__getslice__" href="#NodeWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__reduce__" href="#NodeWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__repr__" href="#NodeWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__setattr__" href="#NodeWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__setstate__" href="#NodeWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__str__" href="#NodeWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#NodeWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="NodeWarning-__unicode__" href="#NodeWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="SVGimportWarning" href="#SVGimportWarning">class <span class="class-name">SVGimportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#SVGimportWarning">SVGimportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="SVGimportWarning-__init__" href="#SVGimportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#SVGimportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="SVGimportWarning-__delattr__" href="#SVGimportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__getattribute__" href="#SVGimportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__getitem__" href="#SVGimportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__getslice__" href="#SVGimportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__reduce__" href="#SVGimportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__repr__" href="#SVGimportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__setattr__" href="#SVGimportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__setstate__" href="#SVGimportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__str__" href="#SVGimportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#SVGimportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="SVGimportWarning-__unicode__" href="#SVGimportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="TXTimportWarning" href="#TXTimportWarning">class <span class="class-name">TXTimportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#TXTimportWarning">TXTimportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="TXTimportWarning-__init__" href="#TXTimportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#TXTimportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="TXTimportWarning-__delattr__" href="#TXTimportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__getattribute__" href="#TXTimportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__getitem__" href="#TXTimportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__getslice__" href="#TXTimportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__reduce__" href="#TXTimportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__repr__" href="#TXTimportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__setattr__" href="#TXTimportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__setstate__" href="#TXTimportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__str__" href="#TXTimportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#TXTimportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="TXTimportWarning-__unicode__" href="#TXTimportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd>
<dt class="class"><h2><a name="VFJimportWarning" href="#VFJimportWarning">class <span class="class-name">VFJimportWarning</span></a>(<a href="./exceptions.html#UserWarning">exceptions.UserWarning</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.base.message.html#VFJimportWarning">VFJimportWarning</a></dd><dd><a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></dd><dd><a href="./exceptions.html#Warning">exceptions.Warning</a></dd><dd><a href="./exceptions.html#Exception">exceptions.Exception</a></dd><dd><a href="./exceptions.html#BaseException">exceptions.BaseException</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl class="function"><dt><a name="VFJimportWarning-__init__" href="#VFJimportWarning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./exceptions.html#UserWarning">exceptions.UserWarning</a></h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#VFJimportWarning-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="function"><dt><a name="VFJimportWarning-__delattr__" href="#VFJimportWarning-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__getattribute__" href="#VFJimportWarning-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__getitem__" href="#VFJimportWarning-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__getslice__" href="#VFJimportWarning-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__reduce__" href="#VFJimportWarning-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__repr__" href="#VFJimportWarning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__setattr__" href="#VFJimportWarning-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__setstate__" href="#VFJimportWarning-__setstate__"><span class="function-name">__setstate__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__str__" href="#VFJimportWarning-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#VFJimportWarning-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="VFJimportWarning-__unicode__" href="#VFJimportWarning-__unicode__"><span class="function-name">__unicode__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./exceptions.html#BaseException">exceptions.BaseException</a></h4><dl class="descriptor"><dt>__dict__</dt>
</dl>
<dl class="descriptor"><dt>args</dt>
</dl>
<dl class="descriptor"><dt>message</dt>
</dl>
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-output" href="#-output"><span class="function-name">output</span></a><span class="argspec">(msg_type, app_name, message)</span></dt><dd>

<pre class="doc" markdown="0"># - Functions ------------------------</pre>

</dd></dl>

<dl class="function"><dt><a name="-warning_custom" href="#-warning_custom"><span class="function-name">warning_custom</span></a><span class="argspec">(message, category, filename, lineno, file<span class="parameter-default">=None</span>, line<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
</dl></div></div>
