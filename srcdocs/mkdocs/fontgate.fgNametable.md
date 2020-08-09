

<a name="fontgate.fgNametable"></a>

# `fgNametable`


<dt class="class"><h2><span class="class-name">fontgate.fgNametable</span> = <a name="fontgate.fgNametable" href="#fontgate.fgNametable">class fgNametable</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">NameTable - unicode->name translation and vice versa</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgNametable-__delattr__" href="#fgNametable-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNametable-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-__getattribute__" href="#fgNametable-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNametable-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-__init__" href="#fgNametable-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNametable-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-__repr__" href="#fgNametable-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNametable-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-__setattr__" href="#fgNametable-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgNametable-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-easyCompare" href="#fgNametable-easyCompare"><span class="function-name">easyCompare</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNametable-easyCompare">easyCompare</a>('name0', 'name1')</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-getAlternativeNames" href="#fgNametable-getAlternativeNames"><span class="function-name">getAlternativeNames</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( 'altGlyphName' ) <a href="#fontgate.fgNametable-getAlternativeNames">getAlternativeNames</a>('glyphName')</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-load" href="#fgNametable-load"><span class="function-name">load</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgNametable-load">load</a>(string path_to_file)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-name" href="#fgNametable-name"><span class="function-name">name</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'glyphName' <a href="#fontgate.fgNametable-name">name</a>(int unicode)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgNametable-unc" href="#fgNametable-unc"><span class="function-name">unc</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgNametable-unc">unc</a>('glyphName')</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>loaded</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgNametable-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgNametable.easyCompare"></a>

## `easyCompare`


<dl class="function"><dt><a name="-fontgate.fgNametable.easyCompare" href="#-fontgate.fgNametable.easyCompare"><span class="function-name">fontgate.fgNametable.easyCompare</span></a> = easyCompare<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool easyCompare('name0', 'name1')</pre>

</dd></dl>



<a name="fontgate.fgNametable.getAlternativeNames"></a>

## `getAlternativeNames`


<dl class="function"><dt><a name="-fontgate.fgNametable.getAlternativeNames" href="#-fontgate.fgNametable.getAlternativeNames"><span class="function-name">fontgate.fgNametable.getAlternativeNames</span></a> = getAlternativeNames<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( 'altGlyphName' ) getAlternativeNames('glyphName')</pre>

</dd></dl>



<a name="fontgate.fgNametable.load"></a>

## `load`


<dl class="function"><dt><a name="-fontgate.fgNametable.load" href="#-fontgate.fgNametable.load"><span class="function-name">fontgate.fgNametable.load</span></a> = load<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool load(string path_to_file)</pre>

</dd></dl>



<a name="fontgate.fgNametable.loaded"></a>

## `loaded`


<dl class="descriptor"><dt>fontgate.fgNametable.loaded</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>



<a name="fontgate.fgNametable.name"></a>

## `name`


<dl class="function"><dt><a name="-fontgate.fgNametable.name" href="#-fontgate.fgNametable.name"><span class="function-name">fontgate.fgNametable.name</span></a> = name<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'glyphName' name(int unicode)</pre>

</dd></dl>



<a name="fontgate.fgNametable.unc"></a>

## `unc`


<dl class="function"><dt><a name="-fontgate.fgNametable.unc" href="#-fontgate.fgNametable.unc"><span class="function-name">fontgate.fgNametable.unc</span></a> = unc<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int unc('glyphName')</pre>

</dd></dl>

