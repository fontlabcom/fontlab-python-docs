

<a name="FL.Anchor"></a>

# `Anchor`


<dt class="class"><h2><span class="class-name">FL.Anchor</span> = <a name="FL.Anchor" href="#FL.Anchor">class Anchor</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Anchor - class to represent Anchor point
===============================================
Integer values are accepted as coordinates

CONSTRUCTOR:
  Anchor() - generic constructor, creates an Anchor with zero coordinates and empty name
  Anchor(Anchor) - copy constructor
  Anchor(string name, integer x, integer y) - creates an Anchor and assigns name and coordinates.

ATTRIBUTES:
  parent (read-only) - anchor's parent object, Glyph
  name (string) - anchor's name as a string
  x (integer) - horizontal position of the anchor
  y (integer) - vertical position of the anchor
  p (Point) - position of the anchor as a Point object

OPERATIONS:

METHODS
  Transform(Matrix m) - applies Matrix transformation to the Anchor(see Matrix().__doc__)
  Layer(int layer_index) - returns position for the "layer_index" master
  SetLayer(int layer_index, Point position) - sets "position" position for the "layer_index" master</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Anchor-Layer" href="#Anchor-Layer"><span class="function-name">Layer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-SetLayer" href="#Anchor-SetLayer"><span class="function-name">SetLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-Transform" href="#Anchor-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-__delattr__" href="#Anchor-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Anchor-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-__getattribute__" href="#Anchor-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Anchor-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-__init__" href="#Anchor-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Anchor-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-__repr__" href="#Anchor-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Anchor-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Anchor-__setattr__" href="#Anchor-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Anchor-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Anchor-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
