

<a name="fontgate.fgPointU"></a>

# `fgPointU`


<dt class="class"><h2><span class="class-name">fontgate.fgPointU</span> = <a name="fontgate.fgPointU" href="#fontgate.fgPointU">class fgPointU</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">PointU representation

Constructors:
  fgPointU() - default
  fgPointU(fgPoint) - copy
  fgPointU(fgPointU) - copy
  fgPointU(fgPoint, float u)
  fgPointU(tuple(float x, float y, float u))
  fgPointU(float x, float y, float u)

Math Operations:
  fgPointU + fgPoint/fgPointU
  fgPointU - fgPoint/fgPointU
  fgPointU * fgPoint/fgPointU
  fgPointU * float - vector product
  fgPointU / float
  fgPointU << fgPointU - True if first point is less or equal to second
  fgPointU >> fgPointU - True if first point is greater or equal to second
  fgPointU ^ fgPointU - scalar product</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgPointU-__add__" href="#fgPointU-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__cmp__" href="#fgPointU-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__delattr__" href="#fgPointU-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__delitem__" href="#fgPointU-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__delslice__" href="#fgPointU-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__div__" href="#fgPointU-__div__"><span class="function-name">__div__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__div__">__div__</a>(y) <==> x/y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__eq__" href="#fgPointU-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__ge__" href="#fgPointU-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__getattribute__" href="#fgPointU-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__getitem__" href="#fgPointU-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__getslice__" href="#fgPointU-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__gt__" href="#fgPointU-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__init__" href="#fgPointU-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__le__" href="#fgPointU-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__len__" href="#fgPointU-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__len__">__len__</a>() <==> <a href="#fontgate.fgPointU-len">len</a>(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__lshift__" href="#fgPointU-__lshift__"><span class="function-name">__lshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__lshift__">__lshift__</a>(y) <==> x<<y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__lt__" href="#fgPointU-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__mul__" href="#fgPointU-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__ne__" href="#fgPointU-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__radd__" href="#fgPointU-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rdiv__" href="#fgPointU-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rdiv__">__rdiv__</a>(y) <==> y/x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__repr__" href="#fgPointU-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rlshift__" href="#fgPointU-__rlshift__"><span class="function-name">__rlshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rlshift__">__rlshift__</a>(y) <==> y<<x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rmul__" href="#fgPointU-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rrshift__" href="#fgPointU-__rrshift__"><span class="function-name">__rrshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rrshift__">__rrshift__</a>(y) <==> y>>x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rshift__" href="#fgPointU-__rshift__"><span class="function-name">__rshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rshift__">__rshift__</a>(y) <==> x>>y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rsub__" href="#fgPointU-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__rxor__" href="#fgPointU-__rxor__"><span class="function-name">__rxor__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__rxor__">__rxor__</a>(y) <==> y^x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__setattr__" href="#fgPointU-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__setitem__" href="#fgPointU-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__setslice__" href="#fgPointU-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__str__" href="#fgPointU-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__sub__" href="#fgPointU-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-__xor__" href="#fgPointU-__xor__"><span class="function-name">__xor__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPointU-__xor__">__xor__</a>(y) <==> x^y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-angleDiff" href="#fgPointU-angleDiff"><span class="function-name">angleDiff</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-angleDiff">angleDiff</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-angleSum" href="#fgPointU-angleSum"><span class="function-name">angleSum</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-angleSum">angleSum</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-asDict" href="#fgPointU-asDict"><span class="function-name">asDict</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-asTuple" href="#fgPointU-asTuple"><span class="function-name">asTuple</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-assign" href="#fgPointU-assign"><span class="function-name">assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPointU-assign">assign</a>(fgPointU) or <a href="#fontgate.fgPointU-assign">assign</a>(float x, float y, float u)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-clear" href="#fgPointU-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPointU-clear">clear</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-close_to" href="#fgPointU-close_to"><span class="function-name">close_to</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPointU-close_to">close_to</a>(fgPointU[, d=0.00001])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-collinear" href="#fgPointU-collinear"><span class="function-name">collinear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPointU-collinear">collinear</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-direction" href="#fgPointU-direction"><span class="function-name">direction</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-direction">direction</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-dist" href="#fgPointU-dist"><span class="function-name">dist</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-dist">dist</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-dist2" href="#fgPointU-dist2"><span class="function-name">dist2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-dist2">dist2</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-distance" href="#fgPointU-distance"><span class="function-name">distance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-distance">distance</a>(fgPoint[, horizontal=false]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-doubleScale" href="#fgPointU-doubleScale"><span class="function-name">doubleScale</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scale(fgPoint) or scale(float sx, float sy)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-flip" href="#fgPointU-flip"><span class="function-name">flip</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPointU-flip">flip</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-flipped" href="#fgPointU-flipped"><span class="function-name">flipped</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-flipped">flipped</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-ix" href="#fgPointU-ix"><span class="function-name">ix</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPointU-ix">ix</a>() - integer fast</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-iy" href="#fgPointU-iy"><span class="function-name">iy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPointU-iy">iy</a>() - integer fast</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-len" href="#fgPointU-len"><span class="function-name">len</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-len">len</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-len2" href="#fgPointU-len2"><span class="function-name">len2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-len2">len2</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-normal" href="#fgPointU-normal"><span class="function-name">normal</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-normal">normal</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-rotate" href="#fgPointU-rotate"><span class="function-name">rotate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-rotate">rotate</a>(fgPointU v, fgPoint c)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-round" href="#fgPointU-round"><span class="function-name">round</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-round">round</a>([doRound=true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-rx" href="#fgPointU-rx"><span class="function-name">rx</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPointU-rx">rx</a>() - integer rounded</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-ry" href="#fgPointU-ry"><span class="function-name">ry</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPointU-ry">ry</a>() - integer rounded</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-transform" href="#fgPointU-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPointU-transform">transform</a>(fgMatrix)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-transformed" href="#fgPointU-transformed"><span class="function-name">transformed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPointU-transformed">transformed</a>(fgMatrix)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-value" href="#fgPointU-value"><span class="function-name">value</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPointU-value">value</a>([horizontal=true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPointU-zero" href="#fgPointU-zero"><span class="function-name">zero</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPointU-zero">zero</a>()</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>u</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>x</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgPointU-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgPointU.angleDiff"></a>

## `angleDiff`


<dl class="function"><dt><a name="-fontgate.fgPointU.angleDiff" href="#-fontgate.fgPointU.angleDiff"><span class="function-name">fontgate.fgPointU.angleDiff</span></a> = angleDiff<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint angleDiff(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPointU.angleSum"></a>

## `angleSum`


<dl class="function"><dt><a name="-fontgate.fgPointU.angleSum" href="#-fontgate.fgPointU.angleSum"><span class="function-name">fontgate.fgPointU.angleSum</span></a> = angleSum<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint angleSum(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPointU.asDict"></a>

## `asDict`


<dl class="function"><dt><a name="-fontgate.fgPointU.asDict" href="#-fontgate.fgPointU.asDict"><span class="function-name">fontgate.fgPointU.asDict</span></a> = asDict<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>



<a name="fontgate.fgPointU.assign"></a>

## `assign`


<dl class="function"><dt><a name="-fontgate.fgPointU.assign" href="#-fontgate.fgPointU.assign"><span class="function-name">fontgate.fgPointU.assign</span></a> = assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assign(fgPointU) or assign(float x, float y, float u)</pre>

</dd></dl>



<a name="fontgate.fgPointU.asTuple"></a>

## `asTuple`


<dl class="function"><dt><a name="-fontgate.fgPointU.asTuple" href="#-fontgate.fgPointU.asTuple"><span class="function-name">fontgate.fgPointU.asTuple</span></a> = asTuple<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>



<a name="fontgate.fgPointU.clear"></a>

## `clear`


<dl class="function"><dt><a name="-fontgate.fgPointU.clear" href="#-fontgate.fgPointU.clear"><span class="function-name">fontgate.fgPointU.clear</span></a> = clear<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clear()</pre>

</dd></dl>



<a name="fontgate.fgPointU.close_to"></a>

## `close_to`


<dl class="function"><dt><a name="-fontgate.fgPointU.close_to" href="#-fontgate.fgPointU.close_to"><span class="function-name">fontgate.fgPointU.close_to</span></a> = close_to<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool close_to(fgPointU[, d=0.00001])</pre>

</dd></dl>



<a name="fontgate.fgPointU.collinear"></a>

## `collinear`


<dl class="function"><dt><a name="-fontgate.fgPointU.collinear" href="#-fontgate.fgPointU.collinear"><span class="function-name">fontgate.fgPointU.collinear</span></a> = collinear<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool collinear(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPointU.direction"></a>

## `direction`


<dl class="function"><dt><a name="-fontgate.fgPointU.direction" href="#-fontgate.fgPointU.direction"><span class="function-name">fontgate.fgPointU.direction</span></a> = direction<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint direction()</pre>

</dd></dl>



<a name="fontgate.fgPointU.dist"></a>

## `dist`


<dl class="function"><dt><a name="-fontgate.fgPointU.dist" href="#-fontgate.fgPointU.dist"><span class="function-name">fontgate.fgPointU.dist</span></a> = dist<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float dist(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPointU.dist2"></a>

## `dist2`


<dl class="function"><dt><a name="-fontgate.fgPointU.dist2" href="#-fontgate.fgPointU.dist2"><span class="function-name">fontgate.fgPointU.dist2</span></a> = dist2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float dist2(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPointU.distance"></a>

## `distance`


<dl class="function"><dt><a name="-fontgate.fgPointU.distance" href="#-fontgate.fgPointU.distance"><span class="function-name">fontgate.fgPointU.distance</span></a> = distance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float distance(fgPoint[, horizontal=false]</pre>

</dd></dl>



<a name="fontgate.fgPointU.doubleScale"></a>

## `doubleScale`


<dl class="function"><dt><a name="-fontgate.fgPointU.doubleScale" href="#-fontgate.fgPointU.doubleScale"><span class="function-name">fontgate.fgPointU.doubleScale</span></a> = doubleScale<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scale(fgPoint) or scale(float sx, float sy)</pre>

</dd></dl>



<a name="fontgate.fgPointU.flip"></a>

## `flip`


<dl class="function"><dt><a name="-fontgate.fgPointU.flip" href="#-fontgate.fgPointU.flip"><span class="function-name">fontgate.fgPointU.flip</span></a> = flip<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flip()</pre>

</dd></dl>



<a name="fontgate.fgPointU.flipped"></a>

## `flipped`


<dl class="function"><dt><a name="-fontgate.fgPointU.flipped" href="#-fontgate.fgPointU.flipped"><span class="function-name">fontgate.fgPointU.flipped</span></a> = flipped<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint flipped()</pre>

</dd></dl>



<a name="fontgate.fgPointU.ix"></a>

## `ix`


<dl class="function"><dt><a name="-fontgate.fgPointU.ix" href="#-fontgate.fgPointU.ix"><span class="function-name">fontgate.fgPointU.ix</span></a> = ix<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int ix() - integer fast</pre>

</dd></dl>



<a name="fontgate.fgPointU.iy"></a>

## `iy`


<dl class="function"><dt><a name="-fontgate.fgPointU.iy" href="#-fontgate.fgPointU.iy"><span class="function-name">fontgate.fgPointU.iy</span></a> = iy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int iy() - integer fast</pre>

</dd></dl>



<a name="fontgate.fgPointU.len"></a>

## `len`


<dl class="function"><dt><a name="-fontgate.fgPointU.len" href="#-fontgate.fgPointU.len"><span class="function-name">fontgate.fgPointU.len</span></a> = len<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len()</pre>

</dd></dl>



<a name="fontgate.fgPointU.len2"></a>

## `len2`


<dl class="function"><dt><a name="-fontgate.fgPointU.len2" href="#-fontgate.fgPointU.len2"><span class="function-name">fontgate.fgPointU.len2</span></a> = len2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len2()</pre>

</dd></dl>



<a name="fontgate.fgPointU.normal"></a>

## `normal`


<dl class="function"><dt><a name="-fontgate.fgPointU.normal" href="#-fontgate.fgPointU.normal"><span class="function-name">fontgate.fgPointU.normal</span></a> = normal<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint normal()</pre>

</dd></dl>



<a name="fontgate.fgPointU.rotate"></a>

## `rotate`


<dl class="function"><dt><a name="-fontgate.fgPointU.rotate" href="#-fontgate.fgPointU.rotate"><span class="function-name">fontgate.fgPointU.rotate</span></a> = rotate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint rotate(fgPointU v, fgPoint c)</pre>

</dd></dl>



<a name="fontgate.fgPointU.round"></a>

## `round`


<dl class="function"><dt><a name="-fontgate.fgPointU.round" href="#-fontgate.fgPointU.round"><span class="function-name">fontgate.fgPointU.round</span></a> = round<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint round([doRound=true])</pre>

</dd></dl>



<a name="fontgate.fgPointU.rx"></a>

## `rx`


<dl class="function"><dt><a name="-fontgate.fgPointU.rx" href="#-fontgate.fgPointU.rx"><span class="function-name">fontgate.fgPointU.rx</span></a> = rx<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int rx() - integer rounded</pre>

</dd></dl>



<a name="fontgate.fgPointU.ry"></a>

## `ry`


<dl class="function"><dt><a name="-fontgate.fgPointU.ry" href="#-fontgate.fgPointU.ry"><span class="function-name">fontgate.fgPointU.ry</span></a> = ry<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int ry() - integer rounded</pre>

</dd></dl>



<a name="fontgate.fgPointU.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgPointU.transform" href="#-fontgate.fgPointU.transform"><span class="function-name">fontgate.fgPointU.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix)</pre>

</dd></dl>



<a name="fontgate.fgPointU.transformed"></a>

## `transformed`


<dl class="function"><dt><a name="-fontgate.fgPointU.transformed" href="#-fontgate.fgPointU.transformed"><span class="function-name">fontgate.fgPointU.transformed</span></a> = transformed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint transformed(fgMatrix)</pre>

</dd></dl>



<a name="fontgate.fgPointU.u"></a>

## `u`


<dl class="descriptor"><dt>fontgate.fgPointU.u</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgPointU.value"></a>

## `value`


<dl class="function"><dt><a name="-fontgate.fgPointU.value" href="#-fontgate.fgPointU.value"><span class="function-name">fontgate.fgPointU.value</span></a> = value<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float value([horizontal=true])</pre>

</dd></dl>



<a name="fontgate.fgPointU.x"></a>

## `x`


<dl class="descriptor"><dt>fontgate.fgPointU.x</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgPointU.y"></a>

## `y`


<dl class="descriptor"><dt>fontgate.fgPointU.y</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgPointU.zero"></a>

## `zero`


<dl class="function"><dt><a name="-fontgate.fgPointU.zero" href="#-fontgate.fgPointU.zero"><span class="function-name">fontgate.fgPointU.zero</span></a> = zero<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool zero()</pre>

</dd></dl>

