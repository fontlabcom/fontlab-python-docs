

<a name="typerig.core.objects.atom"></a>

# `typerig.core.objects.atom`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.atom (<span class="info">version 0.0.2)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Atom (Objects)
# NOTE: Assorted atomic, generic objects
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2020             (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.atom.html#Linker">Linker</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.atom.html#Member">Member</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Linker" href="#Linker">class <span class="class-name">Linker</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Doubly-linked-list/node primitive.</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Linker-__add__" href="#Linker-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__init__" href="#Linker-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__iter__" href="#Linker-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__repr__" href="#Linker-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__sub__" href="#Linker-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-where" href="#Linker-where"><span class="function-name">where</span></a><span class="argspec">(self, search, value)</span></dt><dd>

<pre class="doc" markdown="0"># - Functions ------------------</pre>

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
<dt class="class"><h2><a name="Member" href="#Member">class <span class="class-name">Member</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Node primitive that is a member of a sequence.</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Member-__init__" href="#Member-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Member-__repr__" href="#Member-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

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
<dl class="descriptor"><dt>next</dt>
</dl>
<dl class="descriptor"><dt>prev</dt>
</dl>
</dd></dl></div></div>


<a name="typerig.core.objects.atom.Member"></a>

## `Member`


<dt class="class"><h2><span class="class-name">typerig.core.objects.atom.Member</span> = <a name="typerig.core.objects.atom.Member" href="#typerig.core.objects.atom.Member">class Member</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Node primitive that is a member of a sequence.</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Member-__init__" href="#Member-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Member-__repr__" href="#Member-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

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
<dl class="descriptor"><dt>next</dt>
</dl>
<dl class="descriptor"><dt>prev</dt>
</dl>
</dd>


<a name="typerig.core.objects.atom.Linker"></a>

## `Linker`


<dt class="class"><h2><span class="class-name">typerig.core.objects.atom.Linker</span> = <a name="typerig.core.objects.atom.Linker" href="#typerig.core.objects.atom.Linker">class Linker</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Doubly-linked-list/node primitive.</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Linker-__add__" href="#Linker-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__init__" href="#Linker-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, data, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__iter__" href="#Linker-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__repr__" href="#Linker-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-__sub__" href="#Linker-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Linker-where" href="#Linker-where"><span class="function-name">where</span></a><span class="argspec">(self, search, value)</span></dt><dd>

<pre class="doc" markdown="0"># - Functions ------------------</pre>

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
