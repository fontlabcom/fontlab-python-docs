

<a name="typerig.core.objects.cubicbezier"></a>

# `typerig.core.objects.cubicbezier`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.cubicbezier (<span class="info">version 0.26.6)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Cubic Bezier (Object)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2016-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.cubicbezier.html#CubicBezier">CubicBezier</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="CubicBezier" href="#CubicBezier">class <span class="class-name">CubicBezier</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CubicBezier-__init__" href="#CubicBezier-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-__repr__" href="#CubicBezier-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-asList" href="#CubicBezier-asList"><span class="function-name">asList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-doSwap" href="#CubicBezier-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-doTransform" href="#CubicBezier-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-get_handle_length" href="#CubicBezier-get_handle_length"><span class="function-name">get_handle_length</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns handle length and radii from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-lerp_first" href="#CubicBezier-lerp_first"><span class="function-name">lerp_first</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-lerp_last" href="#CubicBezier-lerp_last"><span class="function-name">lerp_last</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_curvature" href="#CubicBezier-solve_curvature"><span class="function-name">solve_curvature</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find Curvature of on-curve point at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_derivative" href="#CubicBezier-solve_derivative"><span class="function-name">solve_derivative</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns point of on-curve point at given time and vector of 1st and 2nd derivative.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_distance_end" href="#CubicBezier-solve_distance_end"><span class="function-name">solve_distance_end</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to end of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_distance_start" href="#CubicBezier-solve_distance_start"><span class="function-name">solve_distance_start</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to beginning of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_extremes" href="#CubicBezier-solve_extremes"><span class="function-name">solve_extremes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Finds curve extremes and returns [(extreme_01_x, extreme_01_y, extreme_01_t)...(extreme_n_x, extreme_n_y, extreme_n_t)]</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_handle_distance_from_base" href="#CubicBezier-solve_handle_distance_from_base"><span class="function-name">solve_handle_distance_from_base</span></a><span class="argspec">(self, ratio<span class="parameter-default">=(0.5, 0.5)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds new handle positions for given ratio from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_hobby" href="#CubicBezier-solve_hobby"><span class="function-name">solve_hobby</span></a><span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Calculates and applies John Hobby's mock-curvature-smoothness by given curvature - <a href="#CubicBezier-tuple">tuple</a>(float,float) or (float)
Based on Metapolator's Hobby Spline by Juraj Sukop, Lasse Fister, Simon Egli</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_hobby_curvature" href="#CubicBezier-solve_hobby_curvature"><span class="function-name">solve_hobby_curvature</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns current curvature coefficients (complex(alpha), complex(beta)) for 
both handles according to John Hobby's mock-curvature calculation</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_parallel" href="#CubicBezier-solve_parallel"><span class="function-name">solve_parallel</span></a><span class="argspec">(self, vector, fullOutput<span class="parameter-default">=False</span>)</span></dt><dd>

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
<dl class="function"><dt><a name="CubicBezier-solve_point" href="#CubicBezier-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on cubic bezier at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_proportional_handles" href="#CubicBezier-solve_proportional_handles"><span class="function-name">solve_proportional_handles</span></a><span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>)</span></dt><dd>

<pre class="doc" markdown="0">Equalizes handle length to given float(proportion)</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_slice" href="#CubicBezier-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns two segments representing cubic bezier sliced at given time. 
Output: list [(Start), (Start_BCP_out), (Slice_BCP_in), (Slice), (Slice_BCP_out), (End_BCP_in), (End)] of tuples (x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_tunni" href="#CubicBezier-solve_tunni"><span class="function-name">solve_tunni</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Make proportional handles keeping curvature and on-curve point positions 
Based on modified Andres Torresi implementation of Eduardo Tunni's method for control points</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
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
</dd></dl></div></div>


<a name="typerig.core.objects.cubicbezier.CubicBezier"></a>

## `CubicBezier`


<dt class="class"><h2><span class="class-name">typerig.core.objects.cubicbezier.CubicBezier</span> = <a name="typerig.core.objects.cubicbezier.CubicBezier" href="#typerig.core.objects.cubicbezier.CubicBezier">class CubicBezier</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes -----------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="CubicBezier-__init__" href="#CubicBezier-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-__repr__" href="#CubicBezier-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-asList" href="#CubicBezier-asList"><span class="function-name">asList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># -- Modifiers</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-doSwap" href="#CubicBezier-doSwap"><span class="function-name">doSwap</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-doTransform" href="#CubicBezier-doTransform"><span class="function-name">doTransform</span></a><span class="argspec">(self, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-get_handle_length" href="#CubicBezier-get_handle_length"><span class="function-name">get_handle_length</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns handle length and radii from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-lerp_first" href="#CubicBezier-lerp_first"><span class="function-name">lerp_first</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-lerp_last" href="#CubicBezier-lerp_last"><span class="function-name">lerp_last</span></a><span class="argspec">(self, shift)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_curvature" href="#CubicBezier-solve_curvature"><span class="function-name">solve_curvature</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find Curvature of on-curve point at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_derivative" href="#CubicBezier-solve_derivative"><span class="function-name">solve_derivative</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns point of on-curve point at given time and vector of 1st and 2nd derivative.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_distance_end" href="#CubicBezier-solve_distance_end"><span class="function-name">solve_distance_end</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to end of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_distance_start" href="#CubicBezier-solve_distance_start"><span class="function-name">solve_distance_start</span></a><span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to beginning of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_extremes" href="#CubicBezier-solve_extremes"><span class="function-name">solve_extremes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Finds curve extremes and returns [(extreme_01_x, extreme_01_y, extreme_01_t)...(extreme_n_x, extreme_n_y, extreme_n_t)]</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_handle_distance_from_base" href="#CubicBezier-solve_handle_distance_from_base"><span class="function-name">solve_handle_distance_from_base</span></a><span class="argspec">(self, ratio<span class="parameter-default">=(0.5, 0.5)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Finds new handle positions for given ratio from base points.</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_hobby" href="#CubicBezier-solve_hobby"><span class="function-name">solve_hobby</span></a><span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Calculates and applies John Hobby's mock-curvature-smoothness by given curvature - <a href="#typerig.core.objects.cubicbezier.CubicBezier-tuple">tuple</a>(float,float) or (float)
Based on Metapolator's Hobby Spline by Juraj Sukop, Lasse Fister, Simon Egli</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_hobby_curvature" href="#CubicBezier-solve_hobby_curvature"><span class="function-name">solve_hobby_curvature</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns current curvature coefficients (complex(alpha), complex(beta)) for 
both handles according to John Hobby's mock-curvature calculation</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_parallel" href="#CubicBezier-solve_parallel"><span class="function-name">solve_parallel</span></a><span class="argspec">(self, vector, fullOutput<span class="parameter-default">=False</span>)</span></dt><dd>

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
<dl class="function"><dt><a name="CubicBezier-solve_point" href="#CubicBezier-solve_point"><span class="function-name">solve_point</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Find point on cubic bezier at given time</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_proportional_handles" href="#CubicBezier-solve_proportional_handles"><span class="function-name">solve_proportional_handles</span></a><span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>)</span></dt><dd>

<pre class="doc" markdown="0">Equalizes handle length to given float(proportion)</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_slice" href="#CubicBezier-solve_slice"><span class="function-name">solve_slice</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0">Returns two segments representing cubic bezier sliced at given time. 
Output: list [(Start), (Start_BCP_out), (Slice_BCP_in), (Slice), (Slice_BCP_out), (End_BCP_in), (End)] of tuples (x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="CubicBezier-solve_tunni" href="#CubicBezier-solve_tunni"><span class="function-name">solve_tunni</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Make proportional handles keeping curvature and on-curve point positions 
Based on modified Andres Torresi implementation of Eduardo Tunni's method for control points</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_point"></a>

### `solve_point`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_point" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_point"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_point</span></a> = solve_point<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find point on cubic bezier at given time</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_derivative"></a>

### `solve_derivative`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_derivative" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_derivative"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_derivative</span></a> = solve_derivative<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns point of on-curve point at given time and vector of 1st and 2nd derivative.</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_curvature"></a>

### `solve_curvature`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_curvature" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_curvature"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_curvature</span></a> = solve_curvature<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Find Curvature of on-curve point at given time</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_slice"></a>

### `solve_slice`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_slice" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_slice"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_slice</span></a> = solve_slice<span class="argspec">(self, time)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns two segments representing cubic bezier sliced at given time. 
Output: list [(Start), (Start_BCP_out), (Slice_BCP_in), (Slice), (Slice_BCP_out), (End_BCP_in), (End)] of tuples (x,y)</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_distance_start"></a>

### `solve_distance_start`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_distance_start" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_distance_start"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_distance_start</span></a> = solve_distance_start<span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to beginning of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_distance_end"></a>

### `solve_distance_end`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_distance_end" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_distance_end"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_distance_end</span></a> = solve_distance_end<span class="argspec">(self, distance, timeStep<span class="parameter-default">=0.01</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns time at which the given distance to end of bezier is met. 
Probing is executed withing timeStep in range from 0 to 1. The finer the step the preciser the results.</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_extremes"></a>

### `solve_extremes`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_extremes" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_extremes"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_extremes</span></a> = solve_extremes<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Finds curve extremes and returns [(extreme_01_x, extreme_01_y, extreme_01_t)...(extreme_n_x, extreme_n_y, extreme_n_t)]</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_parallel"></a>

### `solve_parallel`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_parallel" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_parallel"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_parallel</span></a> = solve_parallel<span class="argspec">(self, vector, fullOutput<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

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



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_proportional_handles"></a>

### `solve_proportional_handles`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_proportional_handles" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_proportional_handles"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_proportional_handles</span></a> = solve_proportional_handles<span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Equalizes handle length to given float(proportion)</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_handle_distance_from_base"></a>

### `solve_handle_distance_from_base`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_handle_distance_from_base" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_handle_distance_from_base"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_handle_distance_from_base</span></a> = solve_handle_distance_from_base<span class="argspec">(self, ratio<span class="parameter-default">=(0.5, 0.5)</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Finds new handle positions for given ratio from base points.</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.get_handle_length"></a>

### `get_handle_length`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.get_handle_length" href="#-typerig.core.objects.cubicbezier.CubicBezier.get_handle_length"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.get_handle_length</span></a> = get_handle_length<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns handle length and radii from base points.</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_hobby"></a>

### `solve_hobby`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_hobby" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_hobby"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_hobby</span></a> = solve_hobby<span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Calculates and applies John Hobby's mock-curvature-smoothness by given curvature - tuple(float,float) or (float)
Based on Metapolator's Hobby Spline by Juraj Sukop, Lasse Fister, Simon Egli</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_hobby_curvature"></a>

### `solve_hobby_curvature`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_hobby_curvature" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_hobby_curvature"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_hobby_curvature</span></a> = solve_hobby_curvature<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns current curvature coefficients (complex(alpha), complex(beta)) for 
both handles according to John Hobby's mock-curvature calculation</pre>

</dd></dl>



<a name="typerig.core.objects.cubicbezier.CubicBezier.solve_tunni"></a>

### `solve_tunni`


<dl class="function"><dt><a name="-typerig.core.objects.cubicbezier.CubicBezier.solve_tunni" href="#-typerig.core.objects.cubicbezier.CubicBezier.solve_tunni"><span class="function-name">typerig.core.objects.cubicbezier.CubicBezier.solve_tunni</span></a> = solve_tunni<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.cubicbezier.html#CubicBezier">typerig.core.objects.cubicbezier.CubicBezier</a> method</span></dt><dd>

<pre class="doc" markdown="0">Make proportional handles keeping curvature and on-curve point positions 
Based on modified Andres Torresi implementation of Eduardo Tunni's method for control points</pre>

</dd></dl>

