

<a name="fontgate.fgNode"></a>

# `fgNode`


<dt class="class"><h2><span class="class-name">fontgate.fgNode</span> = <a name="fontgate.fgNode" href="#fontgate.fgNode">class fgNode</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Node representation

Constructors:
  fgNode() - default
  fgNode(fgNode) - copy
  fgNode('Move'/'On'/'Off'/'Curve', fgPoint[, smooth=false])
  fgNode('Move'/'On'/'Off'/'Curve', fgPoint, 'name'[, smooth=false])

Math operation:
  fgNode + fgNode
  fgNode - fgNode
  fgNode * float</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgNode-__add__" href="#fgNode-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__cmp__" href="#fgNode-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__delattr__" href="#fgNode-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__getattribute__" href="#fgNode-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__init__" href="#fgNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__mul__" href="#fgNode-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__radd__" href="#fgNode-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__repr__" href="#fgNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__rmul__" href="#fgNode-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__rsub__" href="#fgNode-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__setattr__" href="#fgNode-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-__sub__" href="#fgNode-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNode-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isG2" href="#fgNode-isG2"><span class="function-name">isG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isG2">isG2</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isInterpolatedX" href="#fgNode-isInterpolatedX"><span class="function-name">isInterpolatedX</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isInterpolatedX">isInterpolatedX</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isInterpolatedY" href="#fgNode-isInterpolatedY"><span class="function-name">isInterpolatedY</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isInterpolatedY">isInterpolatedY</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isOff" href="#fgNode-isOff"><span class="function-name">isOff</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isOff">isOff</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isOn" href="#fgNode-isOn"><span class="function-name">isOn</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isOn">isOn</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-isSelected" href="#fgNode-isSelected"><span class="function-name">isSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNode-isSelected">isSelected</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-setG2" href="#fgNode-setG2"><span class="function-name">setG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgNode-setG2">setG2</a>([true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-setInterpolatedX" href="#fgNode-setInterpolatedX"><span class="function-name">setInterpolatedX</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgNode-setInterpolatedX">setInterpolatedX</a>([true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-setInterpolatedY" href="#fgNode-setInterpolatedY"><span class="function-name">setInterpolatedY</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgNode-setInterpolatedY">setInterpolatedY</a>([true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-setSelected" href="#fgNode-setSelected"><span class="function-name">setSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgNode-setSelected">setSelected</a>([true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNode-transform" href="#fgNode-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgNode-transform">transform</a>(fgMatrix)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>flags</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>kind</dt>
<dd>

<pre class="doc" markdown="0">('Move'/'On'/'Off'/'Curve')</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">(string)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>point</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>smooth</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgNode-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgNode.flags"></a>

## `flags`


<dl class="descriptor"><dt>fontgate.fgNode.flags</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgNode.isG2"></a>

## `isG2`


<dl class="function"><dt><a name="-fontgate.fgNode.isG2" href="#-fontgate.fgNode.isG2"><span class="function-name">fontgate.fgNode.isG2</span></a> = isG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isG2()</pre>

</dd></dl>



<a name="fontgate.fgNode.isInterpolatedX"></a>

## `isInterpolatedX`


<dl class="function"><dt><a name="-fontgate.fgNode.isInterpolatedX" href="#-fontgate.fgNode.isInterpolatedX"><span class="function-name">fontgate.fgNode.isInterpolatedX</span></a> = isInterpolatedX<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isInterpolatedX()</pre>

</dd></dl>



<a name="fontgate.fgNode.isInterpolatedY"></a>

## `isInterpolatedY`


<dl class="function"><dt><a name="-fontgate.fgNode.isInterpolatedY" href="#-fontgate.fgNode.isInterpolatedY"><span class="function-name">fontgate.fgNode.isInterpolatedY</span></a> = isInterpolatedY<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isInterpolatedY()</pre>

</dd></dl>



<a name="fontgate.fgNode.isOff"></a>

## `isOff`


<dl class="function"><dt><a name="-fontgate.fgNode.isOff" href="#-fontgate.fgNode.isOff"><span class="function-name">fontgate.fgNode.isOff</span></a> = isOff<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isOff()</pre>

</dd></dl>



<a name="fontgate.fgNode.isOn"></a>

## `isOn`


<dl class="function"><dt><a name="-fontgate.fgNode.isOn" href="#-fontgate.fgNode.isOn"><span class="function-name">fontgate.fgNode.isOn</span></a> = isOn<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isOn()</pre>

</dd></dl>



<a name="fontgate.fgNode.isSelected"></a>

## `isSelected`


<dl class="function"><dt><a name="-fontgate.fgNode.isSelected" href="#-fontgate.fgNode.isSelected"><span class="function-name">fontgate.fgNode.isSelected</span></a> = isSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isSelected()</pre>

</dd></dl>



<a name="fontgate.fgNode.kind"></a>

## `kind`


<dl class="descriptor"><dt>fontgate.fgNode.kind</dt>
<dd>

<pre class="doc" markdown="0">('Move'/'On'/'Off'/'Curve')</pre>

</dd>
</dl>



<a name="fontgate.fgNode.name"></a>

## `name`


<dl class="descriptor"><dt>fontgate.fgNode.name</dt>
<dd>

<pre class="doc" markdown="0">(string)</pre>

</dd>
</dl>



<a name="fontgate.fgNode.point"></a>

## `point`


<dl class="descriptor"><dt>fontgate.fgNode.point</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgNode.setG2"></a>

## `setG2`


<dl class="function"><dt><a name="-fontgate.fgNode.setG2" href="#-fontgate.fgNode.setG2"><span class="function-name">fontgate.fgNode.setG2</span></a> = setG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setG2([true])</pre>

</dd></dl>



<a name="fontgate.fgNode.setInterpolatedX"></a>

## `setInterpolatedX`


<dl class="function"><dt><a name="-fontgate.fgNode.setInterpolatedX" href="#-fontgate.fgNode.setInterpolatedX"><span class="function-name">fontgate.fgNode.setInterpolatedX</span></a> = setInterpolatedX<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setInterpolatedX([true])</pre>

</dd></dl>



<a name="fontgate.fgNode.setInterpolatedY"></a>

## `setInterpolatedY`


<dl class="function"><dt><a name="-fontgate.fgNode.setInterpolatedY" href="#-fontgate.fgNode.setInterpolatedY"><span class="function-name">fontgate.fgNode.setInterpolatedY</span></a> = setInterpolatedY<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setInterpolatedY([true])</pre>

</dd></dl>



<a name="fontgate.fgNode.setSelected"></a>

## `setSelected`


<dl class="function"><dt><a name="-fontgate.fgNode.setSelected" href="#-fontgate.fgNode.setSelected"><span class="function-name">fontgate.fgNode.setSelected</span></a> = setSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setSelected([true])</pre>

</dd></dl>



<a name="fontgate.fgNode.smooth"></a>

## `smooth`


<dl class="descriptor"><dt>fontgate.fgNode.smooth</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>



<a name="fontgate.fgNode.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgNode.transform" href="#-fontgate.fgNode.transform"><span class="function-name">fontgate.fgNode.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix)</pre>

</dd></dl>

