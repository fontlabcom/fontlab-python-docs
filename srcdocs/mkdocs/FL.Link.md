

<a name="FL.Link"></a>

# `Link`


<dt class="class"><h2><span class="class-name">FL.Link</span> = <a name="FL.Link" href="#FL.Link">class Link</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Link - class to represent link
===============================================

CONSTRUCTOR:
  Link() - generic constructor, creates a Link with zero coordinates
  Link(Link) - copy constructor
  Link(index1, index2) - creates a Link between nodes index1 and index2

ATTRIBUTES:
  parent (read-only) - Link's parent object, Glyph
  node1, node2 (integer) - indexes of the nodes that are linked

OPERATIONS:

METHODS
  ToHint() - transforms link to Hint (and returns it as a result) using parent as a source of node coordinates. Parent must exist</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Link-ToHint" href="#Link-ToHint"><span class="function-name">ToHint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Link-__delattr__" href="#Link-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Link-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Link-__getattribute__" href="#Link-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Link-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Link-__init__" href="#Link-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Link-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Link-__repr__" href="#Link-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Link-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Link-__setattr__" href="#Link-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Link-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Link-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
