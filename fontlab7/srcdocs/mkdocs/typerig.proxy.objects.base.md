

<a name="typerig.proxy.objects.base"></a>

# `typerig.proxy.objects.base`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.base (<span class="info">version 0.26.0)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Base (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li><li>PythonQt</li><li>random</li><li>typerig.core.objects</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.base.html#Curve">Curve</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.base.html#Line">Line</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.line.html#Vector">typerig.core.objects.line.Vector</a></span>(<span class="bases">typerig.core.objects.line.Line</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.base.html#Vector">Vector</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.base.html#Coord">Coord</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="Coord" href="#Coord">class <span class="class-name">Coord</span></a>(<a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - FL Proxy model -------------------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.base.html#Coord">Coord</a></dd><dd><a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Coord-__init__" href="#Coord-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__repr__" href="#Coord-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-asQPoint" href="#Coord-asQPoint"><span class="function-name">asQPoint</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-asQPointF" href="#Coord-asQPointF"><span class="function-name">asQPointF</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></h4><dl class="function"><dt><a name="Coord-__abs__" href="#Coord-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__add__" href="#Coord-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"># -- Operators</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__and__" href="#Coord-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self & other: Used as for Scalar product</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__div__" href="#Coord-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__mul__" href="#Coord-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__neg__" href="#Coord-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__or__" href="#Coord-__or__"><span class="function-name">__or__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">self | other: Used as for Cross product</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__rdiv__" href="#Coord-__rdiv__"><span class="function-name">__rdiv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__rmul__" href="#Coord-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__sub__" href="#Coord-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-__truediv__" href="#Coord-__truediv__"><span class="function-name">__truediv__</span></a> = __div__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-angle_to" href="#Coord-angle_to"><span class="function-name">angle_to</span></a><span class="argspec">(self, other, add<span class="parameter-default">=90</span>)</span></dt><dd>

<pre class="doc" markdown="0">Angle to another point in radians</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-diff_to" href="#Coord-diff_to"><span class="function-name">diff_to</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-doFlip" href="#Coord-doFlip"><span class="function-name">doFlip</span></a><span class="argspec">(self, sign<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-doSwap" href="#Coord-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-doTransform" href="#Coord-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-solve_width" href="#Coord-solve_width"><span class="function-name">solve_width</span></a><span class="argspec">(self, y<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get width - find adjacent X by opposite Y</pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-solve_x" href="#Coord-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Coord-solve_y" href="#Coord-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.point.html#Point">typerig.core.objects.point.Point</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>magnitude</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>swap</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>unit</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
</dl>
</dd>
<dt class="class"><h2><a name="Curve" href="#Curve">class <span class="class-name">Curve</span></a>(<a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.base.html#Curve">Curve</a></dd><dd><a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Curve-__init__" href="#Curve-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a></h4><dl class="function"><dt><a name="Curve-__repr__" href="#Curve-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-asList" href="#Curve-asList"><span class="function-name">asList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-doSwap" href="#Curve-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-doTransform" href="#Curve-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-get_handle_length" href="#Curve-get_handle_length"><span class="function-name">get_handle_length</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns handle length and radii from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-lerp_first" href="#Curve-lerp_first"><span class="function-name">lerp_first</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-lerp_last" href="#Curve-lerp_last"><span class="function-name">lerp_last</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_curvature" href="#Curve-solve_curvature"><span class="function-name">solve_curvature</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find Curvature of on-curve point at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_derivative" href="#Curve-solve_derivative"><span class="function-name">solve_derivative</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns point of on-curve point at given time and vector of 1st and 2nd derivative.</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_distance_end" href="#Curve-solve_distance_end"><span class="function-name">solve_distance_end</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to end of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_distance_start" href="#Curve-solve_distance_start"><span class="function-name">solve_distance_start</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to beginning of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_extremes" href="#Curve-solve_extremes"><span class="function-name">solve_extremes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Finds curve extremes and returns [(extreme_01_x, extreme_01_y, extreme_01_t)...(extreme_n_x, extreme_n_y, extreme_n_t)]</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_handle_distance_from_base" href="#Curve-solve_handle_distance_from_base"><span class="function-name">solve_handle_distance_from_base</span></a><span class="argspec">(self, ratio<span class="parameter-default">=(0.5, 0.5)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds new handle positions for given ratio from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_hobby" href="#Curve-solve_hobby"><span class="function-name">solve_hobby</span></a><span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Calculates and applies John Hobby's mock-curvature-smoothness by given curvature - <a href="#Curve-tuple">tuple</a>(float,float) or (float)
Based on Metapolator's Hobby Spline by Juraj Sukop, Lasse Fister, Simon Egli</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_hobby_curvature" href="#Curve-solve_hobby_curvature"><span class="function-name">solve_hobby_curvature</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns current curvature coefficients (complex(alpha), complex(beta)) for 
both handles according to John Hobby's mock-curvature calculation</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_parallel" href="#Curve-solve_parallel"><span class="function-name">solve_parallel</span></a><span class="argspec">(self, vector, fullOutput<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds the t value along a cubic Bezier where a tangent (1st derivative) is parallel with the direction vector.
vector: a pair of values representing the direction of interest (magnitude is ignored).
returns 0.0 <= t <= 1.0 or None

# Solving the dot product of cubic beziers first derivate to the vector given B'(t) x V. Two vectors are perpendicular if their dot product is zero. 
# So if you could find the (1) perpendicular of V it will be collinear == tangent of the curve so the equation to be solved is:
# B'(t) x V(x,y) = 0; -(a*t^2 + b*t + c)*x + (g*t^2 + h*t + i)*y = 0 solved for t, where a,b,c are coefs for X and g,h,i for Y B'(t) derivate of curve
# 
# Inspired by answer given by 'unutbu' on the stackoverflow question: <a href="http://stackoverflow.com/questions/20825173/how-to-find-a-point-if-any-on-quadratic-bezier-with-a-given-tangent-direction" target="_blank" rel="noreferrer noopener">http://stackoverflow.com/questions/20825173/how-to-find-a-point-if-any-on-quadratic-bezier-with-a-given-tangent-direction</a>
# Recoded and recalculated for qubic beziers. Used 'Rearrange It' app at <a href="http://www.wolframalpha.com/widgets/view.jsp?id=4be4308d0f9d17d1da68eea39de9b2ce" target="_blank" rel="noreferrer noopener">http://www.wolframalpha.com/widgets/view.jsp?id=4be4308d0f9d17d1da68eea39de9b2ce</a> was invaluable.
#
# DOTO: Fix calculation optimization error - will yield false positive result in cases #1 and #2 if vector is 45 degrees</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_point" href="#Curve-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on cubic bezier at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_proportional_handles" href="#Curve-solve_proportional_handles"><span class="function-name">solve_proportional_handles</span></a><span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>)</span></dt><dd>

<pre class="doc" markdown="0">Equalizes handle length to given float(proportion)</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_slice" href="#Curve-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns two segments representing cubic bezier sliced at given time. 
Output: list [(Start), (Start_BCP_out), (Slice_BCP_in), (Slice), (Slice_BCP_out), (End_BCP_in), (End)] of tuples (x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="Curve-solve_tunni" href="#Curve-solve_tunni"><span class="function-name">solve_tunni</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Make proportional handles keeping curvature and on-curve point positions 
Based on modified Andres Torresi implementation of Eduardo Tunni's method for control points</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>line</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd>
<dt class="class"><h2><a name="Line" href="#Line">class <span class="class-name">Line</span></a>(<a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.base.html#Line">Line</a></dd><dd><a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Line-__init__" href="#Line-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-asQLineF" href="#Line-asQLineF"><span class="function-name">asQLineF</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-asQPoint" href="#Line-asQPoint"><span class="function-name">asQPoint</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></h4><dl class="function"><dt><a name="Line-__add__" href="#Line-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__and__" href="#Line-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__div__" href="#Line-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__mul__" href="#Line-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__repr__" href="#Line-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__rmul__" href="#Line-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-__sub__" href="#Line-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doSwap" href="#Line-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-doTransform" href="#Line-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-intersect_line" href="#Line-intersect_line"><span class="function-name">intersect_line</span></a><span class="argspec">(self, other_line)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp" href="#Line-lerp"><span class="function-name">lerp</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-lerp_xy" href="#Line-lerp_xy"><span class="function-name">lerp_xy</span></a><span class="argspec">(self, time_x, time_y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Line-shift" href="#Line-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_point" href="#Line-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_slice" href="#Line-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_x" href="#Line-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>
<dl class="function"><dt><a name="Line-solve_y" href="#Line-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>diff_x</dt>
</dl>
<dl class="descriptor"><dt>diff_y</dt>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>length</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd>
<dt class="class"><h2><a name="Vector" href="#Vector">class <span class="class-name">Vector</span></a>(<a href="./typerig.core.objects.line.html#Vector">typerig.core.objects.line.Vector</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.base.html#Vector">Vector</a></dd><dd><a href="./typerig.core.objects.line.html#Vector">typerig.core.objects.line.Vector</a></dd><dd><a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Vector-__init__" href="#Vector-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-asQLineF" href="#Vector-asQLineF"><span class="function-name">asQLineF</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-asQPoint" href="#Vector-asQPoint"><span class="function-name">asQPoint</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.line.html#Vector">typerig.core.objects.line.Vector</a></h4><dl class="function"><dt><a name="Vector-__repr__" href="#Vector-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-getAngle" href="#Vector-getAngle"><span class="function-name">getAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-getSlope" href="#Vector-getSlope"><span class="function-name">getSlope</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Getters</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.line.html#Vector">typerig.core.objects.line.Vector</a></h4><dl class="descriptor"><dt>angle</dt>
</dl>
<dl class="descriptor"><dt>slope</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></h4><dl class="function"><dt><a name="Vector-__add__" href="#Vector-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__and__" href="#Vector-__and__"><span class="function-name">__and__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__div__" href="#Vector-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__mul__" href="#Vector-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__rmul__" href="#Vector-__rmul__"><span class="function-name">__rmul__</span></a> = __mul__<span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-__sub__" href="#Vector-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-doSwap" href="#Vector-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-doTransform" href="#Vector-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-intersect_line" href="#Vector-intersect_line"><span class="function-name">intersect_line</span></a><span class="argspec">(self, other_line)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection point (X, Y) for two lines.
Returns (None, None) if lines do not intersect.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-lerp" href="#Vector-lerp"><span class="function-name">lerp</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-lerp_xy" href="#Vector-lerp_xy"><span class="function-name">lerp_xy</span></a><span class="argspec">(self, time_x, time_y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-shift" href="#Vector-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0">Shift coordinates by dx, dy</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_point" href="#Vector-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on the line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_slice" href="#Vector-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Slice line at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_x" href="#Vector-solve_x"><span class="function-name">solve_x</span></a><span class="argspec">(self, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vector-solve_y" href="#Vector-solve_y"><span class="function-name">solve_y</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.line.html#Line">typerig.core.objects.line.Line</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>diff_x</dt>
</dl>
<dl class="descriptor"><dt>diff_y</dt>
</dl>
<dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>length</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>tuple</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x_max</dt>
</dl>
<dl class="descriptor"><dt>y_intercept</dt>
<dd>

<pre class="doc" markdown="0">Get the Y intercept of a line segment</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y_max</dt>
</dl>
</dd></dl></div></div>
