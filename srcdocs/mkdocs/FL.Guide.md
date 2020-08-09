

<a name="FL.Guide"></a>

# `Guide`


<dt class="class"><h2><span class="class-name">FL.Guide</span> = <a name="FL.Guide" href="#FL.Guide">class Guide</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Guide - class to represent guideline
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Guide() - generic constructor, creates a Guide with zero coordinates
  Guide(Guide) - copy constructor
  Guide(position) - creates a Guide and assigns position
  Guide(position, angle) - creates a Guide and assigns position and width values

ATTRIBUTES:
  parent (read-only) - Guide's parent object, Glyph
  position (integer) - position of the guideline
  width (integer) - width of the guideline
  angle (float) - angle of the guide (degrees)
  positions [(integer)] - list of positions for each master
  widths [(integer)] - list of widths for each master

OPERATIONS:

METHODS
  Transform(Matrix m) - applies Matrix transformation to the Guide (see Matrix().__doc__)
  TransformLayer(Matrix m, layernum) - applies Matrix transformation to the selected layer of the Guide</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Guide-Transform" href="#Guide-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-TransformLayer" href="#Guide-TransformLayer"><span class="function-name">TransformLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-__delattr__" href="#Guide-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Guide-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-__getattribute__" href="#Guide-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Guide-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-__init__" href="#Guide-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Guide-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-__repr__" href="#Guide-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Guide-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Guide-__setattr__" href="#Guide-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Guide-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Guide-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
