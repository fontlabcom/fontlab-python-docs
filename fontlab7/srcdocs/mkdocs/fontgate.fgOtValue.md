

<a name="fontgate.fgOtValue"></a>

# `fgOtValue`


<dt class="class"><h2><span class="class-name">fontgate.fgOtValue</span> = <a name="fontgate.fgOtValue" href="#fontgate.fgOtValue">class fgOtValue</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">OT Value representation

Constructors:
  fgOtValue() - default
  fgOtValue(fgOtValue) - copy
  fgOtValue(float) - by float value
  fgOtValue(int/long) - by int/long value

Math operation:
  fgOtValue + fgOtValue
  fgOtValue - fgOtValue
  fgOtValue * float</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgOtValue-__add__" href="#fgOtValue-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__cmp__" href="#fgOtValue-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__delattr__" href="#fgOtValue-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__getattribute__" href="#fgOtValue-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__init__" href="#fgOtValue-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__mul__" href="#fgOtValue-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__radd__" href="#fgOtValue-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__repr__" href="#fgOtValue-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__rmul__" href="#fgOtValue-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__rsub__" href="#fgOtValue-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__setattr__" href="#fgOtValue-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__str__" href="#fgOtValue-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgOtValue-__sub__" href="#fgOtValue-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgOtValue-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>coordinate</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>deviceTable</dt>
<dd>

<pre class="doc" markdown="0">(fgDeviceRecords)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>point_index</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgOtValue-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgOtValue.coordinate"></a>

## `coordinate`


<dl class="descriptor"><dt>fontgate.fgOtValue.coordinate</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgOtValue.deviceTable"></a>

## `deviceTable`


<dl class="descriptor"><dt>fontgate.fgOtValue.deviceTable</dt>
<dd>

<pre class="doc" markdown="0">(fgDeviceRecords)</pre>

</dd>
</dl>



<a name="fontgate.fgOtValue.point_index"></a>

## `point_index`


<dl class="descriptor"><dt>fontgate.fgOtValue.point_index</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>

