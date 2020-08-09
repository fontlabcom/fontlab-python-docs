

<a name="typerig.core.func.transform"></a>

# `typerig.core.func.transform`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.func.html">func</a>.transform (<span class="info">version 0.26.1)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Transform (Functions)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li></ul></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-adaptive_scale" href="#-adaptive_scale"><span class="function-name">adaptive_scale</span></a><span class="argspec">(v, s, d, t, c, i, st)</span></dt><dd>

<pre class="doc" markdown="0">Perform adaptive scaling by keeping the stem/stroke weights
Args:
        v(t0, t1) -> tuple((float, float), (float, float)) : Joined coordinates for both weights
        s(sx, sy) -> tuple((float, float) : Scale factors (X, Y)
        d(dx, dy) -> tuple((float, float) : Translate values (X, Y) 
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        c(cx, cy) -> tuple((float, float) : Compensation factor 0.0 (no compensation) to 1.0 (full compensation) (X,Y)
        i -> (radians) : Angle of sharing (for italic designs)  
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        tuple(float, float): Transformed coordinate data</pre>

</dd></dl>

<dl class="function"><dt><a name="-adaptive_scale_array" href="#-adaptive_scale_array"><span class="function-name">adaptive_scale_array</span></a><span class="argspec">(a, s, d, t, c, i, st)</span></dt><dd>

<pre class="doc" markdown="0">Perform adaptive scaling by keeping the stem/stroke weights
Args:
        a(t0, t1) -> list(tuple(float, float), (float, float)) : Joined coordinate arrays for both weights
        s(sx, sy) -> tuple((float, float) : Scale factors (X, Y)
        d(dx, dy) -> tuple((float, float) : Translate values (X, Y) 
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        c(cx, cy) -> tuple((float, float) : Compensation factor 0.0 (no compensation) to 1.0 (full compensation) (X,Y)
        i -> (radians) : Angle of sharing (for italic designs)  
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        list(tuple(float, float)): Transformed coordinate data</pre>

</dd></dl>

<dl class="function"><dt><a name="-adjuster" href="#-adjuster"><span class="function-name">adjuster</span></a><span class="argspec">(v, w, h, t, d, st)</span></dt><dd>

<pre class="doc" markdown="0">Readjust scale factor based on interpolation time
Args:
        v(t0, t1) -> list(tuple((float, float), (float, float))...) : Joined coordinate arrays for both weights
        w, h -> Float: Target Width and Height
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        d(dx, dy) -> tuple((float, float) : Translation X, Y
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        tuple(float, float): Readjusted scale factors</pre>

</dd></dl>

<dl class="function"><dt><a name="-compensator" href="#-compensator"><span class="function-name">compensator</span></a><span class="argspec">(sf, cf, st0, st1)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-lerp" href="#-lerp"><span class="function-name">lerp</span></a><span class="argspec">(t0, t1, t)</span></dt><dd>

<pre class="doc" markdown="0"># - Functions ---------------------------</pre>

</dd></dl>

<dl class="function"><dt><a name="-timer" href="#-timer"><span class="function-name">timer</span></a><span class="argspec">(sw_c, sw_0, sw_1, fix_boundry<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Interpolation time for stem value withing given interval.
Args:
        sw_c -> Float : Target stem value
        sw_0, sw_1 -> Float : Stem values
Returns:
        t -> Float : Interpolation time</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.func.transform.timer"></a>

## `timer`


<dl class="function"><dt><a name="-typerig.core.func.transform.timer" href="#-typerig.core.func.transform.timer"><span class="function-name">typerig.core.func.transform.timer</span></a> = timer<span class="argspec">(sw_c, sw_0, sw_1, fix_boundry<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Get Interpolation time for stem value withing given interval.
Args:
        sw_c -> Float : Target stem value
        sw_0, sw_1 -> Float : Stem values
Returns:
        t -> Float : Interpolation time</pre>

</dd></dl>



<a name="typerig.core.func.transform.adjuster"></a>

## `adjuster`


<dl class="function"><dt><a name="-typerig.core.func.transform.adjuster" href="#-typerig.core.func.transform.adjuster"><span class="function-name">typerig.core.func.transform.adjuster</span></a> = adjuster<span class="argspec">(v, w, h, t, d, st)</span></dt><dd>

<pre class="doc" markdown="0">Readjust scale factor based on interpolation time
Args:
        v(t0, t1) -> list(tuple((float, float), (float, float))...) : Joined coordinate arrays for both weights
        w, h -> Float: Target Width and Height
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        d(dx, dy) -> tuple((float, float) : Translation X, Y
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        tuple(float, float): Readjusted scale factors</pre>

</dd></dl>



<a name="typerig.core.func.transform.adaptive_scale"></a>

## `adaptive_scale`


<dl class="function"><dt><a name="-typerig.core.func.transform.adaptive_scale" href="#-typerig.core.func.transform.adaptive_scale"><span class="function-name">typerig.core.func.transform.adaptive_scale</span></a> = adaptive_scale<span class="argspec">(v, s, d, t, c, i, st)</span></dt><dd>

<pre class="doc" markdown="0">Perform adaptive scaling by keeping the stem/stroke weights
Args:
        v(t0, t1) -> tuple((float, float), (float, float)) : Joined coordinates for both weights
        s(sx, sy) -> tuple((float, float) : Scale factors (X, Y)
        d(dx, dy) -> tuple((float, float) : Translate values (X, Y) 
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        c(cx, cy) -> tuple((float, float) : Compensation factor 0.0 (no compensation) to 1.0 (full compensation) (X,Y)
        i -> (radians) : Angle of sharing (for italic designs)  
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        tuple(float, float): Transformed coordinate data</pre>

</dd></dl>



<a name="typerig.core.func.transform.adaptive_scale_array"></a>

## `adaptive_scale_array`


<dl class="function"><dt><a name="-typerig.core.func.transform.adaptive_scale_array" href="#-typerig.core.func.transform.adaptive_scale_array"><span class="function-name">typerig.core.func.transform.adaptive_scale_array</span></a> = adaptive_scale_array<span class="argspec">(a, s, d, t, c, i, st)</span></dt><dd>

<pre class="doc" markdown="0">Perform adaptive scaling by keeping the stem/stroke weights
Args:
        a(t0, t1) -> list(tuple(float, float), (float, float)) : Joined coordinate arrays for both weights
        s(sx, sy) -> tuple((float, float) : Scale factors (X, Y)
        d(dx, dy) -> tuple((float, float) : Translate values (X, Y) 
        t(tx, ty) -> tuple((float, float) : Interpolation times (anisotropic X, Y) 
        c(cx, cy) -> tuple((float, float) : Compensation factor 0.0 (no compensation) to 1.0 (full compensation) (X,Y)
        i -> (radians) : Angle of sharing (for italic designs)  
        st(stx0, stx1, sty0, sty1) -> tuple((float, float, float, float) : Stems widths for weights t0, t1

Returns:
        list(tuple(float, float)): Transformed coordinate data</pre>

</dd></dl>

