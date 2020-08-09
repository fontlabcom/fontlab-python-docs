

<a name="FL.Hint"></a>

# `Hint`


<dt class="class"><h2><span class="class-name">FL.Hint</span> = <a name="FL.Hint" href="#FL.Hint">class Hint</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Hint - class to represent hint
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Hint() - generic constructor, creates a Hint with zero coordinates
  Hint(Hint) - copy constructor
  Hint(position, width) - creates a Hint and assigns position and width values

ATTRIBUTES:
  parent (read-only) - Hint's parent object, Glyph
  position (integer) - position of the hint
  width (integer) - width of the hint
  positions [(integer)] - list of positions for each master
  widths [(integer)] - list of widths for each master

OPERATIONS:

METHODS
  ToLink() - transforms hint to Link (and returns it as a result) using parent as a source of node coordinates. Parent must exist
  Transform(Matrix m) - applies Matrix transformation to the Hint (see Matrix().__doc__)
  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Hint</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Hint-ToLink" href="#Hint-ToLink"><span class="function-name">ToLink</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-Transform" href="#Hint-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-TransformLayer" href="#Hint-TransformLayer"><span class="function-name">TransformLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-__delattr__" href="#Hint-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Hint-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-__getattribute__" href="#Hint-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Hint-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-__init__" href="#Hint-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Hint-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-__repr__" href="#Hint-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Hint-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Hint-__setattr__" href="#Hint-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Hint-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Hint-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
