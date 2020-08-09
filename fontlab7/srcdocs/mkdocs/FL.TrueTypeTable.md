

<a name="FL.TrueTypeTable"></a>

# `TrueTypeTable`


<dt class="class"><h2><span class="class-name">FL.TrueTypeTable</span> = <a name="FL.TrueTypeTable" href="#FL.TrueTypeTable">class TrueTypeTable</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  TrueTypeTable - class to represent custom OpenType table
===============================================

CONSTRUCTOR:
  TrueTypeTable() - generic constructor, creates an empty TrueTypeTable record
  TrueTypeTable(TrueTypeTable) - copy constructor
  TrueTypeTable(string tag) - creates table, assigns 'tag' and empty value
  TrueTypeTable(string tag, string value) - creates TrueType table and assigns values to both attributes
  TrueTypeTable(string tag, string value, integer valuelen) - creates TrueType table and assigns values to both attributes. 'value' may include zeroes

ATTRIBUTES:
  parent (read-only) - parent object, Font
  tag (string) - TrueType table's tag
  value (string) - TrueType table's value

OPERATIONS:

METHODS</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="TrueTypeTable-__delattr__" href="#TrueTypeTable-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.TrueTypeTable-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="TrueTypeTable-__getattribute__" href="#TrueTypeTable-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.TrueTypeTable-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="TrueTypeTable-__init__" href="#TrueTypeTable-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.TrueTypeTable-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="TrueTypeTable-__repr__" href="#TrueTypeTable-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.TrueTypeTable-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="TrueTypeTable-__setattr__" href="#TrueTypeTable-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.TrueTypeTable-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.TrueTypeTable-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
