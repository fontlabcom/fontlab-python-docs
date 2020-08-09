

<a name="FL.KerningPair"></a>

# `KerningPair`


<dt class="class"><h2><span class="class-name">FL.KerningPair</span> = <a name="FL.KerningPair" href="#FL.KerningPair">class KerningPair</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  KerningPair - class to represent kerning pair
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  KerningPair() - generic constructor, creates an empty KerningPair
  KerningPair(KerningPair) - copy constructor
  KerningPair(index) - creates a KerningPair to glyph referenced by index but zero value
  KerningPair(index, value) - creates a KerningPair to glyph referenced by index but and assigns value

ATTRIBUTES:
  parent (read-only) - KerningPair's parent object, Glyph
  key (integer) - index of right glyph of the pair
  value (integer) - value of the pair
  values [(integer)] - list of values for each master

OPERATIONS:

METHODS</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="KerningPair-__delattr__" href="#KerningPair-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.KerningPair-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="KerningPair-__getattribute__" href="#KerningPair-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.KerningPair-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="KerningPair-__init__" href="#KerningPair-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.KerningPair-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="KerningPair-__repr__" href="#KerningPair-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.KerningPair-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="KerningPair-__setattr__" href="#KerningPair-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.KerningPair-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.KerningPair-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
