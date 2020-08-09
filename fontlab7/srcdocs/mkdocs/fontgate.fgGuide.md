

<a name="fontgate.fgGuide"></a>

# `fgGuide`


<dt class="class"><h2><span class="class-name">fontgate.fgGuide</span> = <a name="fontgate.fgGuide" href="#fontgate.fgGuide">class fgGuide</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Guide representation

Constructors:
  fgGuide() - default
  fgGuide(fgGuide) - copy
  fgGuide(float pos[, bool horizontal = false])
  fgGuide(fgPoint p0, fgPoint p1[, name=''[, horizonta=false[, color=fgColor]]])</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgGuide-__cmp__" href="#fgGuide-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-__delattr__" href="#fgGuide-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-__getattribute__" href="#fgGuide-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-__init__" href="#fgGuide-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-__repr__" href="#fgGuide-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-__setattr__" href="#fgGuide-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGuide-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGuide-copy" href="#fgGuide-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGuide <a href="#fontgate.fgGuide-copy">copy</a>() - copy object</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>color</dt>
<dd>

<pre class="doc" markdown="0">(fgColor)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>horizontal</dt>
<dd>

<pre class="doc" markdown="0">True if guide is horizontal</pre>

</dd>
</dl>
<dl class="descriptor"><dt>index</dt>
<dd>

<pre class="doc" markdown="0">(int) index in owner guides list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">(string) guide name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>p0</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>p1</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>position</dt>
<dd>

<pre class="doc" markdown="0">(int) y value of p0, p1 if guide is horizontal, x value - if vertical, none if guide nor horizontal/vertical</pre>

</dd>
</dl>
<dl class="descriptor"><dt>vertical</dt>
<dd>

<pre class="doc" markdown="0">True if guide is vertical</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgGuide-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgGuide.color"></a>

## `color`


<dl class="descriptor"><dt>fontgate.fgGuide.color</dt>
<dd>

<pre class="doc" markdown="0">(fgColor)</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgGuide.copy" href="#-fontgate.fgGuide.copy"><span class="function-name">fontgate.fgGuide.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGuide copy() - copy object</pre>

</dd></dl>



<a name="fontgate.fgGuide.horizontal"></a>

## `horizontal`


<dl class="descriptor"><dt>fontgate.fgGuide.horizontal</dt>
<dd>

<pre class="doc" markdown="0">True if guide is horizontal</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.index"></a>

## `index`


<dl class="descriptor"><dt>fontgate.fgGuide.index</dt>
<dd>

<pre class="doc" markdown="0">(int) index in owner guides list</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.name"></a>

## `name`


<dl class="descriptor"><dt>fontgate.fgGuide.name</dt>
<dd>

<pre class="doc" markdown="0">(string) guide name</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.p0"></a>

## `p0`


<dl class="descriptor"><dt>fontgate.fgGuide.p0</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.p1"></a>

## `p1`


<dl class="descriptor"><dt>fontgate.fgGuide.p1</dt>
<dd>

<pre class="doc" markdown="0">(fgPoint)</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.position"></a>

## `position`


<dl class="descriptor"><dt>fontgate.fgGuide.position</dt>
<dd>

<pre class="doc" markdown="0">(int) y value of p0, p1 if guide is horizontal, x value - if vertical, none if guide nor horizontal/vertical</pre>

</dd>
</dl>



<a name="fontgate.fgGuide.vertical"></a>

## `vertical`


<dl class="descriptor"><dt>fontgate.fgGuide.vertical</dt>
<dd>

<pre class="doc" markdown="0">True if guide is vertical</pre>

</dd>
</dl>

