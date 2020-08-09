

<a name="fontgate.fgCurve"></a>

# `fgCurve`


<dt class="class"><h2><span class="class-name">fontgate.fgCurve</span> = <a name="fontgate.fgCurve" href="#fontgate.fgCurve">class fgCurve</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Curve representation

Constructors:
  fgCurve() - default
  fgCurve(fgCurve) - copy
  fgCurve( [4 x fgPoint] )
  fgCurve( (q0, q1, q2, q3) )
  fgCurve( fgPoint, fgPoint )
  fgCurve( fgPoint, fgPoint, fgPoint )
  fgCurve( fgPoint, fgPoint, fgPoint, fgPoint )
  fgCurve( fgCurve, float t0, float t1 )</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgCurve-__cmp__" href="#fgCurve-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__delattr__" href="#fgCurve-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__getattribute__" href="#fgCurve-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__init__" href="#fgCurve-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__repr__" href="#fgCurve-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__setattr__" href="#fgCurve-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-__str__" href="#fgCurve-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgCurve-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-asDict" href="#fgCurve-asDict"><span class="function-name">asDict</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-asTuple" href="#fgCurve-asTuple"><span class="function-name">asTuple</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-bbox" href="#fgCurve-bbox"><span class="function-name">bbox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgCurve-bbox">bbox</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-check" href="#fgCurve-check"><span class="function-name">check</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgCurve-check">check</a>(float flatness, float length, float w0, float w1)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-coefficients" href="#fgCurve-coefficients"><span class="function-name">coefficients</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(fgPoint a, fgPoint b, fgPoint c, fgPoint d) <a href="#fontgate.fgCurve-coefficients">coefficients</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-curvature" href="#fgCurve-curvature"><span class="function-name">curvature</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgCurve-curvature">curvature</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-d1" href="#fgCurve-d1"><span class="function-name">d1</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgCurve-d1">d1</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-d2" href="#fgCurve-d2"><span class="function-name">d2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgCurve-d2">d2</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-direction" href="#fgCurve-direction"><span class="function-name">direction</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgCurve-direction">direction</a>(float time)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-eseg" href="#fgCurve-eseg"><span class="function-name">eseg</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve <a href="#fontgate.fgCurve-eseg">eseg</a>(float u)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-flat" href="#fgCurve-flat"><span class="function-name">flat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgCurve-flat">flat</a>(double parameter = almost_zero)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-getExtrema" href="#fgCurve-getExtrema"><span class="function-name">getExtrema</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgCurve-getExtrema">getExtrema</a>(bool h, [float] )</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-getInflection" href="#fgCurve-getInflection"><span class="function-name">getInflection</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgCurve-getInflection">getInflection</a>( [float] )</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-hasExtrema" href="#fgCurve-hasExtrema"><span class="function-name">hasExtrema</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgCurve-hasExtrema">hasExtrema</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-isConvex" href="#fgCurve-isConvex"><span class="function-name">isConvex</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgCurve-isConvex">isConvex</a>( [float area] )</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-len" href="#fgCurve-len"><span class="function-name">len</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgCurve-len">len</a>(int quality)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-maximumDeviation" href="#fgCurve-maximumDeviation"><span class="function-name">maximumDeviation</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgCurve-maximumDeviation">maximumDeviation</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-merge" href="#fgCurve-merge"><span class="function-name">merge</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgCurve-merge">merge</a>(fgCurve c)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-point" href="#fgCurve-point"><span class="function-name">point</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint <a href="#fontgate.fgCurve-point">point</a>(float time)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-quickLen" href="#fgCurve-quickLen"><span class="function-name">quickLen</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgCurve-quickLen">quickLen</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-render" href="#fgCurve-render"><span class="function-name">render</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgCurve-render">render</a>([fgPoint/fgPointU], int quality)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-seg" href="#fgCurve-seg"><span class="function-name">seg</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve <a href="#fontgate.fgCurve-seg">seg</a>(float stime, float etime)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-sseg" href="#fgCurve-sseg"><span class="function-name">sseg</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve <a href="#fontgate.fgCurve-sseg">sseg</a>(float u)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgCurve-time" href="#fgCurve-time"><span class="function-name">time</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgCurve-time">time</a>(fgPoint[, int quality[, [float min_dist] ]])</pre>

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
<dl class="descriptor"><dt>q2</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>q3</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgCurve-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgCurve.asDict"></a>

## `asDict`


<dl class="function"><dt><a name="-fontgate.fgCurve.asDict" href="#-fontgate.fgCurve.asDict"><span class="function-name">fontgate.fgCurve.asDict</span></a> = asDict<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as dictionary</pre>

</dd></dl>



<a name="fontgate.fgCurve.asTuple"></a>

## `asTuple`


<dl class="function"><dt><a name="-fontgate.fgCurve.asTuple" href="#-fontgate.fgCurve.asTuple"><span class="function-name">fontgate.fgCurve.asTuple</span></a> = asTuple<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">represent object as tuple</pre>

</dd></dl>



<a name="fontgate.fgCurve.bbox"></a>

## `bbox`


<dl class="function"><dt><a name="-fontgate.fgCurve.bbox" href="#-fontgate.fgCurve.bbox"><span class="function-name">fontgate.fgCurve.bbox</span></a> = bbox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect bbox()</pre>

</dd></dl>



<a name="fontgate.fgCurve.check"></a>

## `check`


<dl class="function"><dt><a name="-fontgate.fgCurve.check" href="#-fontgate.fgCurve.check"><span class="function-name">fontgate.fgCurve.check</span></a> = check<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool check(float flatness, float length, float w0, float w1)</pre>

</dd></dl>



<a name="fontgate.fgCurve.coefficients"></a>

## `coefficients`


<dl class="function"><dt><a name="-fontgate.fgCurve.coefficients" href="#-fontgate.fgCurve.coefficients"><span class="function-name">fontgate.fgCurve.coefficients</span></a> = coefficients<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(fgPoint a, fgPoint b, fgPoint c, fgPoint d) coefficients()</pre>

</dd></dl>



<a name="fontgate.fgCurve.curvature"></a>

## `curvature`


<dl class="function"><dt><a name="-fontgate.fgCurve.curvature" href="#-fontgate.fgCurve.curvature"><span class="function-name">fontgate.fgCurve.curvature</span></a> = curvature<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float curvature(float t)</pre>

</dd></dl>



<a name="fontgate.fgCurve.d1"></a>

## `d1`


<dl class="function"><dt><a name="-fontgate.fgCurve.d1" href="#-fontgate.fgCurve.d1"><span class="function-name">fontgate.fgCurve.d1</span></a> = d1<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint d1(float t)</pre>

</dd></dl>



<a name="fontgate.fgCurve.d2"></a>

## `d2`


<dl class="function"><dt><a name="-fontgate.fgCurve.d2" href="#-fontgate.fgCurve.d2"><span class="function-name">fontgate.fgCurve.d2</span></a> = d2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint d2(float t)</pre>

</dd></dl>



<a name="fontgate.fgCurve.direction"></a>

## `direction`


<dl class="function"><dt><a name="-fontgate.fgCurve.direction" href="#-fontgate.fgCurve.direction"><span class="function-name">fontgate.fgCurve.direction</span></a> = direction<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint direction(float time)</pre>

</dd></dl>



<a name="fontgate.fgCurve.eseg"></a>

## `eseg`


<dl class="function"><dt><a name="-fontgate.fgCurve.eseg" href="#-fontgate.fgCurve.eseg"><span class="function-name">fontgate.fgCurve.eseg</span></a> = eseg<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve eseg(float u)</pre>

</dd></dl>



<a name="fontgate.fgCurve.flat"></a>

## `flat`


<dl class="function"><dt><a name="-fontgate.fgCurve.flat" href="#-fontgate.fgCurve.flat"><span class="function-name">fontgate.fgCurve.flat</span></a> = flat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool flat(double parameter = almost_zero)</pre>

</dd></dl>



<a name="fontgate.fgCurve.getExtrema"></a>

## `getExtrema`


<dl class="function"><dt><a name="-fontgate.fgCurve.getExtrema" href="#-fontgate.fgCurve.getExtrema"><span class="function-name">fontgate.fgCurve.getExtrema</span></a> = getExtrema<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int getExtrema(bool h, [float] )</pre>

</dd></dl>



<a name="fontgate.fgCurve.getInflection"></a>

## `getInflection`


<dl class="function"><dt><a name="-fontgate.fgCurve.getInflection" href="#-fontgate.fgCurve.getInflection"><span class="function-name">fontgate.fgCurve.getInflection</span></a> = getInflection<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int getInflection( [float] )</pre>

</dd></dl>



<a name="fontgate.fgCurve.hasExtrema"></a>

## `hasExtrema`


<dl class="function"><dt><a name="-fontgate.fgCurve.hasExtrema" href="#-fontgate.fgCurve.hasExtrema"><span class="function-name">fontgate.fgCurve.hasExtrema</span></a> = hasExtrema<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasExtrema()</pre>

</dd></dl>



<a name="fontgate.fgCurve.isConvex"></a>

## `isConvex`


<dl class="function"><dt><a name="-fontgate.fgCurve.isConvex" href="#-fontgate.fgCurve.isConvex"><span class="function-name">fontgate.fgCurve.isConvex</span></a> = isConvex<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isConvex( [float area] )</pre>

</dd></dl>



<a name="fontgate.fgCurve.len"></a>

## `len`


<dl class="function"><dt><a name="-fontgate.fgCurve.len" href="#-fontgate.fgCurve.len"><span class="function-name">fontgate.fgCurve.len</span></a> = len<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float len(int quality)</pre>

</dd></dl>



<a name="fontgate.fgCurve.maximumDeviation"></a>

## `maximumDeviation`


<dl class="function"><dt><a name="-fontgate.fgCurve.maximumDeviation" href="#-fontgate.fgCurve.maximumDeviation"><span class="function-name">fontgate.fgCurve.maximumDeviation</span></a> = maximumDeviation<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float maximumDeviation()</pre>

</dd></dl>



<a name="fontgate.fgCurve.merge"></a>

## `merge`


<dl class="function"><dt><a name="-fontgate.fgCurve.merge" href="#-fontgate.fgCurve.merge"><span class="function-name">fontgate.fgCurve.merge</span></a> = merge<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool merge(fgCurve c)</pre>

</dd></dl>



<a name="fontgate.fgCurve.point"></a>

## `point`


<dl class="function"><dt><a name="-fontgate.fgCurve.point" href="#-fontgate.fgCurve.point"><span class="function-name">fontgate.fgCurve.point</span></a> = point<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgPoint point(float time)</pre>

</dd></dl>



<a name="fontgate.fgCurve.q0"></a>

## `q0`


<dl class="descriptor"><dt>fontgate.fgCurve.q0</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgCurve.q1"></a>

## `q1`


<dl class="descriptor"><dt>fontgate.fgCurve.q1</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgCurve.q2"></a>

## `q2`


<dl class="descriptor"><dt>fontgate.fgCurve.q2</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgCurve.q3"></a>

## `q3`


<dl class="descriptor"><dt>fontgate.fgCurve.q3</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgCurve.quickLen"></a>

## `quickLen`


<dl class="function"><dt><a name="-fontgate.fgCurve.quickLen" href="#-fontgate.fgCurve.quickLen"><span class="function-name">fontgate.fgCurve.quickLen</span></a> = quickLen<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float quickLen()</pre>

</dd></dl>



<a name="fontgate.fgCurve.render"></a>

## `render`


<dl class="function"><dt><a name="-fontgate.fgCurve.render" href="#-fontgate.fgCurve.render"><span class="function-name">fontgate.fgCurve.render</span></a> = render<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int render([fgPoint/fgPointU], int quality)</pre>

</dd></dl>



<a name="fontgate.fgCurve.seg"></a>

## `seg`


<dl class="function"><dt><a name="-fontgate.fgCurve.seg" href="#-fontgate.fgCurve.seg"><span class="function-name">fontgate.fgCurve.seg</span></a> = seg<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve seg(float stime, float etime)</pre>

</dd></dl>



<a name="fontgate.fgCurve.sseg"></a>

## `sseg`


<dl class="function"><dt><a name="-fontgate.fgCurve.sseg" href="#-fontgate.fgCurve.sseg"><span class="function-name">fontgate.fgCurve.sseg</span></a> = sseg<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgCurve sseg(float u)</pre>

</dd></dl>



<a name="fontgate.fgCurve.time"></a>

## `time`


<dl class="function"><dt><a name="-fontgate.fgCurve.time" href="#-fontgate.fgCurve.time"><span class="function-name">fontgate.fgCurve.time</span></a> = time<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float time(fgPoint[, int quality[, [float min_dist] ]])</pre>

</dd></dl>

