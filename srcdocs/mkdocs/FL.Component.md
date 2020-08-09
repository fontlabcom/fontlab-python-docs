

<a name="FL.Component"></a>

# `Component`


<dt class="class"><h2><span class="class-name">FL.Component</span> = <a name="FL.Component" href="#FL.Component">class Component</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Component - class to represent glyph component
===============================================
Components are defined by the glyph index which they reference, shift of components origin point and scale factor of a component
scale is measured in relation to 1.0, so 100% scale is 1.0 and 60% - 0.6
This class is Multiple Master - compatible

CONSTRUCTOR:
  Component() - generic constructor, creates an empty Component
  Component(Component) - copy constructor
  Component(index) - creates component referencing glyph index with zero shift and 100% scale
  Component(index, Point(integer) delta) - creates component referencing glyph index with delta shift and 100% scale
  Component(index, Point(integer) delta, Point(float) scale) - creates component referencing glyph index with delta shift and scale factor defined by scale

ATTRIBUTES:
  parent (read-only) - parent object, Glyph
  index (integer) - referencing glyph index
  delta (Point(integer)) - shift value
  scale (Point(float)) - scale factor
  deltas [(Point(integer))]- list of shift values for each master
  scales [(Point(float))] - list of scale values for each master

OPERATIONS:

METHODS
  Get() | (Font f) - creates a glyph from component applying delta and scale transformations. Font parameter is not needed when component has a parent
  Paste() - appends component to a parent glyph as a set of outlines. Component must have a parent</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Component-Get" href="#Component-Get"><span class="function-name">Get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Component-Paste" href="#Component-Paste"><span class="function-name">Paste</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Component-__delattr__" href="#Component-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Component-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Component-__getattribute__" href="#Component-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Component-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Component-__init__" href="#Component-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Component-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Component-__repr__" href="#Component-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Component-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Component-__setattr__" href="#Component-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Component-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Component-transform" href="#Component-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Component-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
