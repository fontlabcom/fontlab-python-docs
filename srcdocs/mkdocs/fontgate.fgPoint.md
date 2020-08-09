

<a name="fontgate.fgPoint"></a>

# `fgPoint`


<dt class="class"><h2><span class="class-name">fontgate.fgPoint</span> = <a name="fontgate.fgPoint" href="#fontgate.fgPoint">class fgPoint</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Point representation

Constructors:
  fgPoint() - default
  fgPoint(fgPoint) - copy
  fgPoint(float x)
  fgPoint(tuple(float x, float y))
  fgPoint(float x, float y)

Math Operations:
  fgPoint + fgPoint
  fgPoint - fgPoint
  fgPoint * fgPoint
  fgPoint * float - vector product
  fgPoint / float
  fgPoint << fgPoint - True if first point is less or equal to second
  fgPoint >> fgPoint - True if first point is greater or equal to second
  fgPoint ^ fgPoint - scalar product</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgPoint-__add__" href="#fgPoint-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__cmp__" href="#fgPoint-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__delattr__" href="#fgPoint-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__delitem__" href="#fgPoint-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__delslice__" href="#fgPoint-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__div__" href="#fgPoint-__div__"><span class="function-name">__div__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__div__">__div__</a>(y) <==> x/y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__eq__" href="#fgPoint-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__ge__" href="#fgPoint-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__getattribute__" href="#fgPoint-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__getitem__" href="#fgPoint-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__getslice__" href="#fgPoint-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__gt__" href="#fgPoint-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__init__" href="#fgPoint-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__le__" href="#fgPoint-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__len__" href="#fgPoint-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__len__">__len__</a>() <==> <a href="#fontgate.fgPoint-len">len</a>(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__lshift__" href="#fgPoint-__lshift__"><span class="function-name">__lshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__lshift__">__lshift__</a>(y) <==> x<<y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__lt__" href="#fgPoint-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__mul__" href="#fgPoint-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__ne__" href="#fgPoint-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__radd__" href="#fgPoint-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rdiv__" href="#fgPoint-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rdiv__">__rdiv__</a>(y) <==> y/x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__repr__" href="#fgPoint-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rlshift__" href="#fgPoint-__rlshift__"><span class="function-name">__rlshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rlshift__">__rlshift__</a>(y) <==> y<<x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rmul__" href="#fgPoint-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rrshift__" href="#fgPoint-__rrshift__"><span class="function-name">__rrshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rrshift__">__rrshift__</a>(y) <==> y>>x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rshift__" href="#fgPoint-__rshift__"><span class="function-name">__rshift__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rshift__">__rshift__</a>(y) <==> x>>y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rsub__" href="#fgPoint-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__rxor__" href="#fgPoint-__rxor__"><span class="function-name">__rxor__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__rxor__">__rxor__</a>(y) <==> y^x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__setattr__" href="#fgPoint-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__setitem__" href="#fgPoint-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__setslice__" href="#fgPoint-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__str__" href="#fgPoint-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__sub__" href="#fgPoint-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-__xor__" href="#fgPoint-__xor__"><span class="function-name">__xor__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgPoint-__xor__">__xor__</a>(y) <==> x^y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-angleDiff" href="#fgPoint-angleDiff"><span class="function-name">angleDiff</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-angleDiff">angleDiff</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-angleSum" href="#fgPoint-angleSum"><span class="function-name">angleSum</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-angleSum">angleSum</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-asDict" href="#fgPoint-asDict"><span class="function-name">asDict</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-asTuple" href="#fgPoint-asTuple"><span class="function-name">asTuple</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-assign" href="#fgPoint-assign"><span class="function-name">assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPoint-assign">assign</a>(fgPoint) or <a href="#fontgate.fgPoint-assign">assign</a>(float x, float y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-clear" href="#fgPoint-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPoint-clear">clear</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-close_to" href="#fgPoint-close_to"><span class="function-name">close_to</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPoint-close_to">close_to</a>(fgPoint[, d=0.00001])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-collinear" href="#fgPoint-collinear"><span class="function-name">collinear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPoint-collinear">collinear</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-direction" href="#fgPoint-direction"><span class="function-name">direction</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-direction">direction</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-dist" href="#fgPoint-dist"><span class="function-name">dist</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-dist">dist</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-dist2" href="#fgPoint-dist2"><span class="function-name">dist2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-dist2">dist2</a>(fgPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-distance" href="#fgPoint-distance"><span class="function-name">distance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-distance">distance</a>(fgPoint[, horizontal=false]</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-doubleScale" href="#fgPoint-doubleScale"><span class="function-name">doubleScale</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scale(fgPoint) or scale(float sx, float sy)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-flip" href="#fgPoint-flip"><span class="function-name">flip</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPoint-flip">flip</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-flipped" href="#fgPoint-flipped"><span class="function-name">flipped</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-flipped">flipped</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-ix" href="#fgPoint-ix"><span class="function-name">ix</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPoint-ix">ix</a>() - integer fast</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-iy" href="#fgPoint-iy"><span class="function-name">iy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPoint-iy">iy</a>() - integer fast</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-len" href="#fgPoint-len"><span class="function-name">len</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-len">len</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-len2" href="#fgPoint-len2"><span class="function-name">len2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-len2">len2</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-normal" href="#fgPoint-normal"><span class="function-name">normal</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-normal">normal</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-rotate" href="#fgPoint-rotate"><span class="function-name">rotate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-rotate">rotate</a>(fgPoint v, fgPoint c)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-round" href="#fgPoint-round"><span class="function-name">round</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-round">round</a>([doRound=true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-rx" href="#fgPoint-rx"><span class="function-name">rx</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPoint-rx">rx</a>() - integer rounded</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-ry" href="#fgPoint-ry"><span class="function-name">ry</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgPoint-ry">ry</a>() - integer rounded</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-transform" href="#fgPoint-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgPoint-transform">transform</a>(fgMatrix)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-transformed" href="#fgPoint-transformed"><span class="function-name">transformed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgPoint-transformed">transformed</a>(fgMatrix)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-value" href="#fgPoint-value"><span class="function-name">value</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgPoint-value">value</a>([horizontal=true])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgPoint-zero" href="#fgPoint-zero"><span class="function-name">zero</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgPoint-zero">zero</a>()</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>x</dt>
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

<pre class="doc" markdown="0">T.<a href="#fontgate.fgPoint-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgPoint.angleDiff"></a>

## `angleDiff`


<dl class="function"><dt><a name="-fontgate.fgPoint.angleDiff" href="#-fontgate.fgPoint.angleDiff"><span class="function-name">fontgate.fgPoint.angleDiff</span></a> = angleDiff<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint angleDiff(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPoint.angleSum"></a>

## `angleSum`


<dl class="function"><dt><a name="-fontgate.fgPoint.angleSum" href="#-fontgate.fgPoint.angleSum"><span class="function-name">fontgate.fgPoint.angleSum</span></a> = angleSum<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint angleSum(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPoint.asDict"></a>

## `asDict`


<dl class="function"><dt><a name="-fontgate.fgPoint.asDict" href="#-fontgate.fgPoint.asDict"><span class="function-name">fontgate.fgPoint.asDict</span></a> = asDict<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>



<a name="fontgate.fgPoint.assign"></a>

## `assign`


<dl class="function"><dt><a name="-fontgate.fgPoint.assign" href="#-fontgate.fgPoint.assign"><span class="function-name">fontgate.fgPoint.assign</span></a> = assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assign(fgPoint) or assign(float x, float y)</pre>

</dd></dl>



<a name="fontgate.fgPoint.asTuple"></a>

## `asTuple`


<dl class="function"><dt><a name="-fontgate.fgPoint.asTuple" href="#-fontgate.fgPoint.asTuple"><span class="function-name">fontgate.fgPoint.asTuple</span></a> = asTuple<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>



<a name="fontgate.fgPoint.clear"></a>

## `clear`


<dl class="function"><dt><a name="-fontgate.fgPoint.clear" href="#-fontgate.fgPoint.clear"><span class="function-name">fontgate.fgPoint.clear</span></a> = clear<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clear()</pre>

</dd></dl>



<a name="fontgate.fgPoint.close_to"></a>

## `close_to`


<dl class="function"><dt><a name="-fontgate.fgPoint.close_to" href="#-fontgate.fgPoint.close_to"><span class="function-name">fontgate.fgPoint.close_to</span></a> = close_to<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool close_to(fgPoint[, d=0.00001])</pre>

</dd></dl>



<a name="fontgate.fgPoint.collinear"></a>

## `collinear`


<dl class="function"><dt><a name="-fontgate.fgPoint.collinear" href="#-fontgate.fgPoint.collinear"><span class="function-name">fontgate.fgPoint.collinear</span></a> = collinear<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool collinear(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPoint.direction"></a>

## `direction`


<dl class="function"><dt><a name="-fontgate.fgPoint.direction" href="#-fontgate.fgPoint.direction"><span class="function-name">fontgate.fgPoint.direction</span></a> = direction<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint direction()</pre>

</dd></dl>



<a name="fontgate.fgPoint.dist"></a>

## `dist`


<dl class="function"><dt><a name="-fontgate.fgPoint.dist" href="#-fontgate.fgPoint.dist"><span class="function-name">fontgate.fgPoint.dist</span></a> = dist<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float dist(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPoint.dist2"></a>

## `dist2`


<dl class="function"><dt><a name="-fontgate.fgPoint.dist2" href="#-fontgate.fgPoint.dist2"><span class="function-name">fontgate.fgPoint.dist2</span></a> = dist2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float dist2(fgPoint)</pre>

</dd></dl>



<a name="fontgate.fgPoint.distance"></a>

## `distance`


<dl class="function"><dt><a name="-fontgate.fgPoint.distance" href="#-fontgate.fgPoint.distance"><span class="function-name">fontgate.fgPoint.distance</span></a> = distance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float distance(fgPoint[, horizontal=false]</pre>

</dd></dl>



<a name="fontgate.fgPoint.doubleScale"></a>

## `doubleScale`


<dl class="function"><dt><a name="-fontgate.fgPoint.doubleScale" href="#-fontgate.fgPoint.doubleScale"><span class="function-name">fontgate.fgPoint.doubleScale</span></a> = doubleScale<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scale(fgPoint) or scale(float sx, float sy)</pre>

</dd></dl>



<a name="fontgate.fgPoint.flip"></a>

## `flip`


<dl class="function"><dt><a name="-fontgate.fgPoint.flip" href="#-fontgate.fgPoint.flip"><span class="function-name">fontgate.fgPoint.flip</span></a> = flip<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flip()</pre>

</dd></dl>



<a name="fontgate.fgPoint.flipped"></a>

## `flipped`


<dl class="function"><dt><a name="-fontgate.fgPoint.flipped" href="#-fontgate.fgPoint.flipped"><span class="function-name">fontgate.fgPoint.flipped</span></a> = flipped<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint flipped()</pre>

</dd></dl>



<a name="fontgate.fgPoint.ix"></a>

## `ix`


<dl class="function"><dt><a name="-fontgate.fgPoint.ix" href="#-fontgate.fgPoint.ix"><span class="function-name">fontgate.fgPoint.ix</span></a> = ix<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int ix() - integer fast</pre>

</dd></dl>



<a name="fontgate.fgPoint.iy"></a>

## `iy`


<dl class="function"><dt><a name="-fontgate.fgPoint.iy" href="#-fontgate.fgPoint.iy"><span class="function-name">fontgate.fgPoint.iy</span></a> = iy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int iy() - integer fast</pre>

</dd></dl>



<a name="fontgate.fgPoint.len"></a>

## `len`


<dl class="function"><dt><a name="-fontgate.fgPoint.len" href="#-fontgate.fgPoint.len"><span class="function-name">fontgate.fgPoint.len</span></a> = len<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len()</pre>

</dd></dl>



<a name="fontgate.fgPoint.len2"></a>

## `len2`


<dl class="function"><dt><a name="-fontgate.fgPoint.len2" href="#-fontgate.fgPoint.len2"><span class="function-name">fontgate.fgPoint.len2</span></a> = len2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len2()</pre>

</dd></dl>



<a name="fontgate.fgPoint.normal"></a>

## `normal`


<dl class="function"><dt><a name="-fontgate.fgPoint.normal" href="#-fontgate.fgPoint.normal"><span class="function-name">fontgate.fgPoint.normal</span></a> = normal<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint normal()</pre>

</dd></dl>



<a name="fontgate.fgPoint.rotate"></a>

## `rotate`


<dl class="function"><dt><a name="-fontgate.fgPoint.rotate" href="#-fontgate.fgPoint.rotate"><span class="function-name">fontgate.fgPoint.rotate</span></a> = rotate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint rotate(fgPoint v, fgPoint c)</pre>

</dd></dl>



<a name="fontgate.fgPoint.round"></a>

## `round`


<dl class="function"><dt><a name="-fontgate.fgPoint.round" href="#-fontgate.fgPoint.round"><span class="function-name">fontgate.fgPoint.round</span></a> = round<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint round([doRound=true])</pre>

</dd></dl>



<a name="fontgate.fgPoint.rx"></a>

## `rx`


<dl class="function"><dt><a name="-fontgate.fgPoint.rx" href="#-fontgate.fgPoint.rx"><span class="function-name">fontgate.fgPoint.rx</span></a> = rx<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int rx() - integer rounded</pre>

</dd></dl>



<a name="fontgate.fgPoint.ry"></a>

## `ry`


<dl class="function"><dt><a name="-fontgate.fgPoint.ry" href="#-fontgate.fgPoint.ry"><span class="function-name">fontgate.fgPoint.ry</span></a> = ry<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int ry() - integer rounded</pre>

</dd></dl>



<a name="fontgate.fgPoint.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgPoint.transform" href="#-fontgate.fgPoint.transform"><span class="function-name">fontgate.fgPoint.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix)</pre>

</dd></dl>



<a name="fontgate.fgPoint.transformed"></a>

## `transformed`


<dl class="function"><dt><a name="-fontgate.fgPoint.transformed" href="#-fontgate.fgPoint.transformed"><span class="function-name">fontgate.fgPoint.transformed</span></a> = transformed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint transformed(fgMatrix)</pre>

</dd></dl>



<a name="fontgate.fgPoint.value"></a>

## `value`


<dl class="function"><dt><a name="-fontgate.fgPoint.value" href="#-fontgate.fgPoint.value"><span class="function-name">fontgate.fgPoint.value</span></a> = value<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float value([horizontal=true])</pre>

</dd></dl>



<a name="fontgate.fgPoint.x"></a>

## `x`


<dl class="descriptor"><dt>fontgate.fgPoint.x</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgPoint.y"></a>

## `y`


<dl class="descriptor"><dt>fontgate.fgPoint.y</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgPoint.zero"></a>

## `zero`


<dl class="function"><dt><a name="-fontgate.fgPoint.zero" href="#-fontgate.fgPoint.zero"><span class="function-name">fontgate.fgPoint.zero</span></a> = zero<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool zero()</pre>

</dd></dl>

