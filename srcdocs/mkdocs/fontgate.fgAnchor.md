

<a name="fontgate.fgAnchor"></a>

# `fgAnchor`


<dt class="class"><h2><span class="class-name">fontgate.fgAnchor</span> = <a name="fontgate.fgAnchor" href="#fontgate.fgAnchor">class fgAnchor</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Anchor representation

Constructors:
  fgAnchor() - default
  fgAnchor(fgAnchor) - copy
  fgAnchor((x, y), 'name') - create with position=(x, y) and name='name'
  fgAnchor(x, y, 'name') - create with position=(x, y) and name='name'</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgAnchor-__cmp__" href="#fgAnchor-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__delattr__" href="#fgAnchor-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__getattribute__" href="#fgAnchor-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__init__" href="#fgAnchor-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__repr__" href="#fgAnchor-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__setattr__" href="#fgAnchor-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-__str__" href="#fgAnchor-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgAnchor-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-copy" href="#fgAnchor-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-copy">copy</a>(fgAnchor) - copy data from another fgAnchor object</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-draw" href="#fgAnchor-draw"><span class="function-name">draw</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-draw">draw</a>(penObject) - draw the object with a segment pen</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-drawPoints" href="#fgAnchor-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-drawPoints">drawPoints</a>(penObject) - draw the object with a point pen</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-move" href="#fgAnchor-move"><span class="function-name">move</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-move">move</a>(dx, dy) - move anchor by (dx, dy)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-round" href="#fgAnchor-round"><span class="function-name">round</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-round">round</a>() - round anchor coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-scale" href="#fgAnchor-scale"><span class="function-name">scale</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-scale">scale</a>((scale_x, scale_y)[, (center_x, center_y)]) - scale anchor by (scale_x, scale_y) with center=(center_x, center_y) or (0,0) if not defined</pre>

</dd></dl>
<dl class="function"><dt><a name="fgAnchor-transform" href="#fgAnchor-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgAnchor-transform">transform</a>(fgMatrix) - transform anchor coordinates by matrix</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>data</dt>
<dd>

<pre class="doc" markdown="0">(uint) - data</pre>

</dd>
</dl>
<dl class="descriptor"><dt>index</dt>
<dd>

<pre class="doc" markdown="0">(int) - index of object for owner's base layer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>mark</dt>
<dd>

<pre class="doc" markdown="0">(uint) - mark</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">(string) - name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>position</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint) - coordinates as fgPoint</pre>

</dd>
</dl>
<dl class="descriptor"><dt>x</dt>
<dd>

<pre class="doc" markdown="0">(int/double) - horizontal coordinate</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y</dt>
<dd>

<pre class="doc" markdown="0">(int/double) - vertical coordinate</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgAnchor-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgAnchor.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgAnchor.copy" href="#-fontgate.fgAnchor.copy"><span class="function-name">fontgate.fgAnchor.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">copy(fgAnchor) - copy data from another fgAnchor object</pre>

</dd></dl>



<a name="fontgate.fgAnchor.data"></a>

## `data`


<dl class="descriptor"><dt>fontgate.fgAnchor.data</dt>
<dd>

<pre class="doc" markdown="0">(uint) - data</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.draw"></a>

## `draw`


<dl class="function"><dt><a name="-fontgate.fgAnchor.draw" href="#-fontgate.fgAnchor.draw"><span class="function-name">fontgate.fgAnchor.draw</span></a> = draw<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">draw(penObject) - draw the object with a segment pen</pre>

</dd></dl>



<a name="fontgate.fgAnchor.drawPoints"></a>

## `drawPoints`


<dl class="function"><dt><a name="-fontgate.fgAnchor.drawPoints" href="#-fontgate.fgAnchor.drawPoints"><span class="function-name">fontgate.fgAnchor.drawPoints</span></a> = drawPoints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">drawPoints(penObject) - draw the object with a point pen</pre>

</dd></dl>



<a name="fontgate.fgAnchor.index"></a>

## `index`


<dl class="descriptor"><dt>fontgate.fgAnchor.index</dt>
<dd>

<pre class="doc" markdown="0">(int) - index of object for owner's base layer</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.mark"></a>

## `mark`


<dl class="descriptor"><dt>fontgate.fgAnchor.mark</dt>
<dd>

<pre class="doc" markdown="0">(uint) - mark</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.move"></a>

## `move`


<dl class="function"><dt><a name="-fontgate.fgAnchor.move" href="#-fontgate.fgAnchor.move"><span class="function-name">fontgate.fgAnchor.move</span></a> = move<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">move(dx, dy) - move anchor by (dx, dy)</pre>

</dd></dl>



<a name="fontgate.fgAnchor.name"></a>

## `name`


<dl class="descriptor"><dt>fontgate.fgAnchor.name</dt>
<dd>

<pre class="doc" markdown="0">(string) - name</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.position"></a>

## `position`


<dl class="descriptor"><dt>fontgate.fgAnchor.position</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint) - coordinates as fgPoint</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.round"></a>

## `round`


<dl class="function"><dt><a name="-fontgate.fgAnchor.round" href="#-fontgate.fgAnchor.round"><span class="function-name">fontgate.fgAnchor.round</span></a> = round<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">round() - round anchor coordinates</pre>

</dd></dl>



<a name="fontgate.fgAnchor.scale"></a>

## `scale`


<dl class="function"><dt><a name="-fontgate.fgAnchor.scale" href="#-fontgate.fgAnchor.scale"><span class="function-name">fontgate.fgAnchor.scale</span></a> = scale<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scale((scale_x, scale_y)[, (center_x, center_y)]) - scale anchor by (scale_x, scale_y) with center=(center_x, center_y) or (0,0) if not defined</pre>

</dd></dl>



<a name="fontgate.fgAnchor.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgAnchor.transform" href="#-fontgate.fgAnchor.transform"><span class="function-name">fontgate.fgAnchor.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix) - transform anchor coordinates by matrix</pre>

</dd></dl>



<a name="fontgate.fgAnchor.x"></a>

## `x`


<dl class="descriptor"><dt>fontgate.fgAnchor.x</dt>
<dd>

<pre class="doc" markdown="0">(int/double) - horizontal coordinate</pre>

</dd>
</dl>



<a name="fontgate.fgAnchor.y"></a>

## `y`


<dl class="descriptor"><dt>fontgate.fgAnchor.y</dt>
<dd>

<pre class="doc" markdown="0">(int/double) - vertical coordinate</pre>

</dd>
</dl>

