

<a name="fontgate.fgVector"></a>

# `fgVector`


<dt class="class"><h2><span class="class-name">fontgate.fgVector</span> = <a name="fontgate.fgVector" href="#fontgate.fgVector">class fgVector</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Vector representation

Constructors:
  fgVector() - default
  fgVector(fgVector) - copy
  fgVector(fgPoint q0[, fgPoint q1]) - from one or two points
  fgVector(fgPoint, float l, float a)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgVector-__cmp__" href="#fgVector-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__delattr__" href="#fgVector-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__getattribute__" href="#fgVector-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__init__" href="#fgVector-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__repr__" href="#fgVector-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__setattr__" href="#fgVector-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-__str__" href="#fgVector-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgVector-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-angle" href="#fgVector-angle"><span class="function-name">angle</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgVector-angle">angle</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-angleTo" href="#fgVector-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgVector-angleTo">angleTo</a>(fgVector)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-asDict" href="#fgVector-asDict"><span class="function-name">asDict</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-asTuple" href="#fgVector-asTuple"><span class="function-name">asTuple</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-bbox" href="#fgVector-bbox"><span class="function-name">bbox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgVector-bbox">bbox</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-center" href="#fgVector-center"><span class="function-name">center</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgVector-center">center</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-delta" href="#fgVector-delta"><span class="function-name">delta</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgVector-delta">delta</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-direction" href="#fgVector-direction"><span class="function-name">direction</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgVector-direction">direction</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-equivalent" href="#fgVector-equivalent"><span class="function-name">equivalent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgVector-equivalent">equivalent</a>(fgVector)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-intersect" href="#fgVector-intersect"><span class="function-name">intersect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint/None <a href="#fontgate.fgVector-intersect">intersect</a>(fgVector) or (fgPoint, t)/None <a href="#fontgate.fgVector-intersect">intersect</a>(fgVector, bool get_t)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-intersectY" href="#fgVector-intersectY"><span class="function-name">intersectY</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float/None <a href="#fontgate.fgVector-intersectY">intersectY</a>(float pos)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-len" href="#fgVector-len"><span class="function-name">len</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgVector-len">len</a>() - distance between q0 and q1</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-parallel" href="#fgVector-parallel"><span class="function-name">parallel</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgVector-parallel">parallel</a>(fgVector)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-point" href="#fgVector-point"><span class="function-name">point</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgVector-point">point</a>(float time)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgVector-time" href="#fgVector-time"><span class="function-name">time</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgVector-time">time</a>(fgPoint)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>q0</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>q1</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgVector-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgVector.angle"></a>

## `angle`


<dl class="function"><dt><a name="-fontgate.fgVector.angle" href="#-fontgate.fgVector.angle"><span class="function-name">fontgate.fgVector.angle</span></a> = angle<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float angle()</pre>

</dd></dl>



<a name="fontgate.fgVector.angleTo"></a>

## `angleTo`


<dl class="function"><dt><a name="-fontgate.fgVector.angleTo" href="#-fontgate.fgVector.angleTo"><span class="function-name">fontgate.fgVector.angleTo</span></a> = angleTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float angleTo(fgVector)</pre>

</dd></dl>



<a name="fontgate.fgVector.asDict"></a>

## `asDict`


<dl class="function"><dt><a name="-fontgate.fgVector.asDict" href="#-fontgate.fgVector.asDict"><span class="function-name">fontgate.fgVector.asDict</span></a> = asDict<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>



<a name="fontgate.fgVector.asTuple"></a>

## `asTuple`


<dl class="function"><dt><a name="-fontgate.fgVector.asTuple" href="#-fontgate.fgVector.asTuple"><span class="function-name">fontgate.fgVector.asTuple</span></a> = asTuple<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>



<a name="fontgate.fgVector.bbox"></a>

## `bbox`


<dl class="function"><dt><a name="-fontgate.fgVector.bbox" href="#-fontgate.fgVector.bbox"><span class="function-name">fontgate.fgVector.bbox</span></a> = bbox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect bbox()</pre>

</dd></dl>



<a name="fontgate.fgVector.center"></a>

## `center`


<dl class="function"><dt><a name="-fontgate.fgVector.center" href="#-fontgate.fgVector.center"><span class="function-name">fontgate.fgVector.center</span></a> = center<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint center()</pre>

</dd></dl>



<a name="fontgate.fgVector.delta"></a>

## `delta`


<dl class="function"><dt><a name="-fontgate.fgVector.delta" href="#-fontgate.fgVector.delta"><span class="function-name">fontgate.fgVector.delta</span></a> = delta<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint delta()</pre>

</dd></dl>



<a name="fontgate.fgVector.direction"></a>

## `direction`


<dl class="function"><dt><a name="-fontgate.fgVector.direction" href="#-fontgate.fgVector.direction"><span class="function-name">fontgate.fgVector.direction</span></a> = direction<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint direction()</pre>

</dd></dl>



<a name="fontgate.fgVector.equivalent"></a>

## `equivalent`


<dl class="function"><dt><a name="-fontgate.fgVector.equivalent" href="#-fontgate.fgVector.equivalent"><span class="function-name">fontgate.fgVector.equivalent</span></a> = equivalent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool equivalent(fgVector)</pre>

</dd></dl>



<a name="fontgate.fgVector.intersect"></a>

## `intersect`


<dl class="function"><dt><a name="-fontgate.fgVector.intersect" href="#-fontgate.fgVector.intersect"><span class="function-name">fontgate.fgVector.intersect</span></a> = intersect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint/None intersect(fgVector) or (fgPoint, t)/None intersect(fgVector, bool get_t)</pre>

</dd></dl>



<a name="fontgate.fgVector.intersectY"></a>

## `intersectY`


<dl class="function"><dt><a name="-fontgate.fgVector.intersectY" href="#-fontgate.fgVector.intersectY"><span class="function-name">fontgate.fgVector.intersectY</span></a> = intersectY<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float/None intersectY(float pos)</pre>

</dd></dl>



<a name="fontgate.fgVector.len"></a>

## `len`


<dl class="function"><dt><a name="-fontgate.fgVector.len" href="#-fontgate.fgVector.len"><span class="function-name">fontgate.fgVector.len</span></a> = len<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len() - distance between q0 and q1</pre>

</dd></dl>



<a name="fontgate.fgVector.parallel"></a>

## `parallel`


<dl class="function"><dt><a name="-fontgate.fgVector.parallel" href="#-fontgate.fgVector.parallel"><span class="function-name">fontgate.fgVector.parallel</span></a> = parallel<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool parallel(fgVector)</pre>

</dd></dl>



<a name="fontgate.fgVector.point"></a>

## `point`


<dl class="function"><dt><a name="-fontgate.fgVector.point" href="#-fontgate.fgVector.point"><span class="function-name">fontgate.fgVector.point</span></a> = point<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint point(float time)</pre>

</dd></dl>



<a name="fontgate.fgVector.q0"></a>

## `q0`


<dl class="descriptor"><dt>fontgate.fgVector.q0</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgVector.q1"></a>

## `q1`


<dl class="descriptor"><dt>fontgate.fgVector.q1</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgVector.time"></a>

## `time`


<dl class="function"><dt><a name="-fontgate.fgVector.time" href="#-fontgate.fgVector.time"><span class="function-name">fontgate.fgVector.time</span></a> = time<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float time(fgPoint)</pre>

</dd></dl>

