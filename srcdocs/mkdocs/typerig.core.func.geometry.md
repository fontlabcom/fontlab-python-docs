

<a name="typerig.core.func.geometry"></a>

# `typerig.core.func.geometry`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.func.html">func</a>.geometry (<span class="info">version 0.26.2)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Analytic geometry (Functions)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2015-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-ccw" href="#-ccw"><span class="function-name">ccw</span></a><span class="argspec">(A, B, C)</span></dt><dd>

<pre class="doc" markdown="0">Tests whether the turn formed by points A, B, and C is Counter clock wise (CCW)</pre>

</dd></dl>

<dl class="function"><dt><a name="-checkInnerOuter" href="#-checkInnerOuter"><span class="function-name">checkInnerOuter</span></a><span class="argspec">(firstAngle, lastAngle)</span></dt><dd>

<pre class="doc" markdown="0">Check if connection is inner or outer.
Adapted from RoboFont pens. (NOTE: To be deleted)</pre>

</dd></dl>

<dl class="function"><dt><a name="-checkSmooth" href="#-checkSmooth"><span class="function-name">checkSmooth</span></a><span class="argspec">(firstAngle, lastAngle, error<span class="parameter-default">=4</span>)</span></dt><dd>

<pre class="doc" markdown="0">Check if connection is smooth within error margin.
Adapted from RoboFont pens. (NOTE: To be deleted)</pre>

</dd></dl>

<dl class="function"><dt><a name="-get_angle" href="#-get_angle"><span class="function-name">get_angle</span></a><span class="argspec">(x, y, degrees<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return angle for given X,Y displacement from origin</pre>

</dd></dl>

<dl class="function"><dt><a name="-intersect" href="#-intersect"><span class="function-name">intersect</span></a><span class="argspec">(A, B, C, D)</span></dt><dd>

<pre class="doc" markdown="0">Tests whether A,B and C,D intersect</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_angle" href="#-line_angle"><span class="function-name">line_angle</span></a><span class="argspec">(p0, p1, degrees<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find angle between two points forming a line
Args: 
        p0, p1 -> tuple(x, y);
        degrees -> bool
                
Returns:
        radians or degrees</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_intersect" href="#-line_intersect"><span class="function-name">line_intersect</span></a><span class="argspec">(a0, a1, b0, b1)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection between two lines
Args: 
        a0, a1, b0, b1 -> tuple(x, y); 
Returns:
        intersect node -> tuple(x,y)</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_slope" href="#-line_slope"><span class="function-name">line_slope</span></a><span class="argspec">(p0, p1)</span></dt><dd>

<pre class="doc" markdown="0">Find slope between two points forming a line
Args: 
        p0, p1 -> tuple(x, y)
                
Returns:
        float or NAN</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_solve_x" href="#-line_solve_x"><span class="function-name">line_solve_x</span></a><span class="argspec">(p0, p1, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate by given Y.</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_solve_y" href="#-line_solve_y"><span class="function-name">line_solve_y</span></a><span class="argspec">(p0, p1, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate by given X.</pre>

</dd></dl>

<dl class="function"><dt><a name="-line_y_intercept" href="#-line_y_intercept"><span class="function-name">line_y_intercept</span></a><span class="argspec">(p0, p1)</span></dt><dd>

<pre class="doc" markdown="0">Find Y intercept of line equation for line formed by two points
Args: 
        p0, p1 -> tuple(x, y)

Returns:
        intercept node -> tuple(x,y)</pre>

</dd></dl>

<dl class="function"><dt><a name="-point_in_polygon" href="#-point_in_polygon"><span class="function-name">point_in_polygon</span></a><span class="argspec">(point, polygon)</span></dt><dd>

<pre class="doc" markdown="0">Point in Polygon test
Args: 
        point -> tuple(x, y); 
        polygon -> tuple(tuple(x0, y1)...tuple(xn, yn));

Returns:
        Bool</pre>

</dd></dl>

<dl class="function"><dt><a name="-point_in_triangle" href="#-point_in_triangle"><span class="function-name">point_in_triangle</span></a><span class="argspec">(point, triangle)</span></dt><dd>

<pre class="doc" markdown="0">Point in triangle test
Args: 
        point -> tuple(x, y); 
        triangle -> tuple(tuple(x0, y0), tuple(x1, y1), tuple(x2, y2))

Returns:
        Bool</pre>

</dd></dl>

<dl class="function"><dt><a name="-point_rotate" href="#-point_rotate"><span class="function-name">point_rotate</span></a><span class="argspec">(center, point, angle)</span></dt><dd>

<pre class="doc" markdown="0">Rotate point around center point with angle (in degrees)
Args: 
        center, point -> tuple(x, y); 
        angle -> float;

Returns:
        new point coordinates -> tuple(x,y)</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.func.geometry.get_angle"></a>

## `get_angle`


<dl class="function"><dt><a name="-typerig.core.func.geometry.get_angle" href="#-typerig.core.func.geometry.get_angle"><span class="function-name">typerig.core.func.geometry.get_angle</span></a> = get_angle<span class="argspec">(x, y, degrees<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return angle for given X,Y displacement from origin</pre>

</dd></dl>



<a name="typerig.core.func.geometry.ccw"></a>

## `ccw`


<dl class="function"><dt><a name="-typerig.core.func.geometry.ccw" href="#-typerig.core.func.geometry.ccw"><span class="function-name">typerig.core.func.geometry.ccw</span></a> = ccw<span class="argspec">(A, B, C)</span></dt><dd>

<pre class="doc" markdown="0">Tests whether the turn formed by points A, B, and C is Counter clock wise (CCW)</pre>

</dd></dl>



<a name="typerig.core.func.geometry.intersect"></a>

## `intersect`


<dl class="function"><dt><a name="-typerig.core.func.geometry.intersect" href="#-typerig.core.func.geometry.intersect"><span class="function-name">typerig.core.func.geometry.intersect</span></a> = intersect<span class="argspec">(A, B, C, D)</span></dt><dd>

<pre class="doc" markdown="0">Tests whether A,B and C,D intersect</pre>

</dd></dl>



<a name="typerig.core.func.geometry.point_in_triangle"></a>

## `point_in_triangle`


<dl class="function"><dt><a name="-typerig.core.func.geometry.point_in_triangle" href="#-typerig.core.func.geometry.point_in_triangle"><span class="function-name">typerig.core.func.geometry.point_in_triangle</span></a> = point_in_triangle<span class="argspec">(point, triangle)</span></dt><dd>

<pre class="doc" markdown="0">Point in triangle test
Args: 
        point -> tuple(x, y); 
        triangle -> tuple(tuple(x0, y0), tuple(x1, y1), tuple(x2, y2))

Returns:
        Bool</pre>

</dd></dl>



<a name="typerig.core.func.geometry.point_in_polygon"></a>

## `point_in_polygon`


<dl class="function"><dt><a name="-typerig.core.func.geometry.point_in_polygon" href="#-typerig.core.func.geometry.point_in_polygon"><span class="function-name">typerig.core.func.geometry.point_in_polygon</span></a> = point_in_polygon<span class="argspec">(point, polygon)</span></dt><dd>

<pre class="doc" markdown="0">Point in Polygon test
Args: 
        point -> tuple(x, y); 
        polygon -> tuple(tuple(x0, y1)...tuple(xn, yn));

Returns:
        Bool</pre>

</dd></dl>



<a name="typerig.core.func.geometry.point_rotate"></a>

## `point_rotate`


<dl class="function"><dt><a name="-typerig.core.func.geometry.point_rotate" href="#-typerig.core.func.geometry.point_rotate"><span class="function-name">typerig.core.func.geometry.point_rotate</span></a> = point_rotate<span class="argspec">(center, point, angle)</span></dt><dd>

<pre class="doc" markdown="0">Rotate point around center point with angle (in degrees)
Args: 
        center, point -> tuple(x, y); 
        angle -> float;

Returns:
        new point coordinates -> tuple(x,y)</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_slope"></a>

## `line_slope`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_slope" href="#-typerig.core.func.geometry.line_slope"><span class="function-name">typerig.core.func.geometry.line_slope</span></a> = line_slope<span class="argspec">(p0, p1)</span></dt><dd>

<pre class="doc" markdown="0">Find slope between two points forming a line
Args: 
        p0, p1 -> tuple(x, y)
                
Returns:
        float or NAN</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_angle"></a>

## `line_angle`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_angle" href="#-typerig.core.func.geometry.line_angle"><span class="function-name">typerig.core.func.geometry.line_angle</span></a> = line_angle<span class="argspec">(p0, p1, degrees<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Find angle between two points forming a line
Args: 
        p0, p1 -> tuple(x, y);
        degrees -> bool
                
Returns:
        radians or degrees</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_y_intercept"></a>

## `line_y_intercept`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_y_intercept" href="#-typerig.core.func.geometry.line_y_intercept"><span class="function-name">typerig.core.func.geometry.line_y_intercept</span></a> = line_y_intercept<span class="argspec">(p0, p1)</span></dt><dd>

<pre class="doc" markdown="0">Find Y intercept of line equation for line formed by two points
Args: 
        p0, p1 -> tuple(x, y)

Returns:
        intercept node -> tuple(x,y)</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_solve_y"></a>

## `line_solve_y`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_solve_y" href="#-typerig.core.func.geometry.line_solve_y"><span class="function-name">typerig.core.func.geometry.line_solve_y</span></a> = line_solve_y<span class="argspec">(p0, p1, x)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for Y coordinate by given X.</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_solve_x"></a>

## `line_solve_x`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_solve_x" href="#-typerig.core.func.geometry.line_solve_x"><span class="function-name">typerig.core.func.geometry.line_solve_x</span></a> = line_solve_x<span class="argspec">(p0, p1, y)</span></dt><dd>

<pre class="doc" markdown="0">Solve line equation for X coordinate by given Y.</pre>

</dd></dl>



<a name="typerig.core.func.geometry.line_intersect"></a>

## `line_intersect`


<dl class="function"><dt><a name="-typerig.core.func.geometry.line_intersect" href="#-typerig.core.func.geometry.line_intersect"><span class="function-name">typerig.core.func.geometry.line_intersect</span></a> = line_intersect<span class="argspec">(a0, a1, b0, b1)</span></dt><dd>

<pre class="doc" markdown="0">Find intersection between two lines
Args: 
        a0, a1, b0, b1 -> tuple(x, y); 
Returns:
        intersect node -> tuple(x,y)</pre>

</dd></dl>



<a name="typerig.core.func.geometry.checkSmooth"></a>

## `checkSmooth`


<dl class="function"><dt><a name="-typerig.core.func.geometry.checkSmooth" href="#-typerig.core.func.geometry.checkSmooth"><span class="function-name">typerig.core.func.geometry.checkSmooth</span></a> = checkSmooth<span class="argspec">(firstAngle, lastAngle, error<span class="parameter-default">=4</span>)</span></dt><dd>

<pre class="doc" markdown="0">Check if connection is smooth within error margin.
Adapted from RoboFont pens. (NOTE: To be deleted)</pre>

</dd></dl>



<a name="typerig.core.func.geometry.checkInnerOuter"></a>

## `checkInnerOuter`


<dl class="function"><dt><a name="-typerig.core.func.geometry.checkInnerOuter" href="#-typerig.core.func.geometry.checkInnerOuter"><span class="function-name">typerig.core.func.geometry.checkInnerOuter</span></a> = checkInnerOuter<span class="argspec">(firstAngle, lastAngle)</span></dt><dd>

<pre class="doc" markdown="0">Check if connection is inner or outer.
Adapted from RoboFont pens. (NOTE: To be deleted)</pre>

</dd></dl>

