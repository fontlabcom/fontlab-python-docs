

<a name="fontgate.fgComponent"></a>

# `fgComponent`


<dt class="class"><h2><span class="class-name">fontgate.fgComponent</span> = <a name="fontgate.fgComponent" href="#fontgate.fgComponent">class fgComponent</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Component representation

Constructors:
  fgComponent() - default
  fgComponent(fgComponent) - copy
  fgComponent('name', fgMatrix) - by 'name' and transformation matrix fgMatrix</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgComponent-__cmp__" href="#fgComponent-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__delattr__" href="#fgComponent-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__getattribute__" href="#fgComponent-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__init__" href="#fgComponent-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__repr__" href="#fgComponent-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__setattr__" href="#fgComponent-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-__str__" href="#fgComponent-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgComponent-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-draw" href="#fgComponent-draw"><span class="function-name">draw</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgComponent-draw">draw</a>(pen object) - draw the object with a segment pen</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-drawPoints" href="#fgComponent-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgComponent-drawPoints">drawPoints</a>(pen object) - draw the object with a point pen</pre>

</dd></dl>
<dl class="function"><dt><a name="fgComponent-move" href="#fgComponent-move"><span class="function-name">move</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgComponent-move">move</a>(dx, dy) - move by float dx, dy value</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>baseGlyph</dt>
<dd>

<pre class="doc" markdown="0">(string) name of base glyph</pre>

</dd>
</dl>
<dl class="descriptor"><dt>box</dt>
<dd>

<pre class="doc" markdown="0">(fgRect) - bounding box</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasFullMatrix</dt>
<dd>

<pre class="doc" markdown="0"></pre>

</dd>
</dl>
<dl class="descriptor"><dt>index</dt>
<dd>

<pre class="doc" markdown="0">(int) component index in glyph's components list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>matrix</dt>
<dd>

<pre class="doc" markdown="0">(fgMatrix) - component transform matrix</pre>

</dd>
</dl>
<dl class="descriptor"><dt>offset</dt>
<dd>

<pre class="doc" markdown="0"></pre>

</dd>
</dl>
<dl class="descriptor"><dt>scale</dt>
<dd>

<pre class="doc" markdown="0"></pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgComponent-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgComponent.baseGlyph"></a>

## `baseGlyph`


<dl class="descriptor"><dt>fontgate.fgComponent.baseGlyph</dt>
<dd>

<pre class="doc" markdown="0">(string) name of base glyph</pre>

</dd>
</dl>



<a name="fontgate.fgComponent.box"></a>

## `box`


<dl class="descriptor"><dt>fontgate.fgComponent.box</dt>
<dd>

<pre class="doc" markdown="0">(fgRect) - bounding box</pre>

</dd>
</dl>



<a name="fontgate.fgComponent.draw"></a>

## `draw`


<dl class="function"><dt><a name="-fontgate.fgComponent.draw" href="#-fontgate.fgComponent.draw"><span class="function-name">fontgate.fgComponent.draw</span></a> = draw<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">draw(pen object) - draw the object with a segment pen</pre>

</dd></dl>



<a name="fontgate.fgComponent.drawPoints"></a>

## `drawPoints`


<dl class="function"><dt><a name="-fontgate.fgComponent.drawPoints" href="#-fontgate.fgComponent.drawPoints"><span class="function-name">fontgate.fgComponent.drawPoints</span></a> = drawPoints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">drawPoints(pen object) - draw the object with a point pen</pre>

</dd></dl>



<a name="fontgate.fgComponent.index"></a>

## `index`


<dl class="descriptor"><dt>fontgate.fgComponent.index</dt>
<dd>

<pre class="doc" markdown="0">(int) component index in glyph's components list</pre>

</dd>
</dl>



<a name="fontgate.fgComponent.matrix"></a>

## `matrix`


<dl class="descriptor"><dt>fontgate.fgComponent.matrix</dt>
<dd>

<pre class="doc" markdown="0">(fgMatrix) - component transform matrix</pre>

</dd>
</dl>



<a name="fontgate.fgComponent.move"></a>

## `move`


<dl class="function"><dt><a name="-fontgate.fgComponent.move" href="#-fontgate.fgComponent.move"><span class="function-name">fontgate.fgComponent.move</span></a> = move<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">move(dx, dy) - move by float dx, dy value</pre>

</dd></dl>

