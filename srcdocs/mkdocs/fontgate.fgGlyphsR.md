

<a name="fontgate.fgGlyphsR"></a>

# `fgGlyphsR`


<dt class="class"><h2><span class="class-name">fontgate.fgGlyphsR</span> = <a name="fontgate.fgGlyphsR" href="#fontgate.fgGlyphsR">class fgGlyphsR</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">fgGlyphsR representation

Constructors:
  fgGlyphsR() - default
  fgGlyphsR(fgGlyphsR) - copy
  fgGlyphsR(fgGlyphs) - create from list(fgGlyph)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgGlyphsR-__cmp__" href="#fgGlyphsR-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__delattr__" href="#fgGlyphsR-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__getattribute__" href="#fgGlyphsR-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__init__" href="#fgGlyphsR-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__repr__" href="#fgGlyphsR-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__setattr__" href="#fgGlyphsR-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-__str__" href="#fgGlyphsR-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphsR-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-find" href="#fgGlyphsR-find"><span class="function-name">find</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph <a href="#fontgate.fgGlyphsR-find">find</a>(name|unicode)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-getStats" href="#fgGlyphsR-getStats"><span class="function-name">getStats</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(totalGlyphs, avgNodesCount, avgContoursCount) <a href="#fontgate.fgGlyphsR-getStats">getStats</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-glyph" href="#fgGlyphsR-glyph"><span class="function-name">glyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph <a href="#fontgate.fgGlyphsR-glyph">glyph</a>(int index)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-glyphByID" href="#fgGlyphsR-glyphByID"><span class="function-name">glyphByID</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph <a href="#fontgate.fgGlyphsR-glyphByID">glyphByID</a>(int ID)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-index" href="#fgGlyphsR-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgGlyphsR-index">index</a>(fgGlyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-indexByID" href="#fgGlyphsR-indexByID"><span class="function-name">indexByID</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgGlyphsR-index">index</a>(int ID)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphsR-rebuildUnicodeMap" href="#fgGlyphsR-rebuildUnicodeMap"><span class="function-name">rebuildUnicodeMap</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgGlyphsR-rebuildUnicodeMap">rebuildUnicodeMap</a>()</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgGlyphsR-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgGlyphsR.find"></a>

## `find`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.find" href="#-fontgate.fgGlyphsR.find"><span class="function-name">fontgate.fgGlyphsR.find</span></a> = find<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph find(name|unicode)</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.getStats"></a>

## `getStats`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.getStats" href="#-fontgate.fgGlyphsR.getStats"><span class="function-name">fontgate.fgGlyphsR.getStats</span></a> = getStats<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(totalGlyphs, avgNodesCount, avgContoursCount) getStats()</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.glyph"></a>

## `glyph`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.glyph" href="#-fontgate.fgGlyphsR.glyph"><span class="function-name">fontgate.fgGlyphsR.glyph</span></a> = glyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph glyph(int index)</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.glyphByID"></a>

## `glyphByID`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.glyphByID" href="#-fontgate.fgGlyphsR.glyphByID"><span class="function-name">fontgate.fgGlyphsR.glyphByID</span></a> = glyphByID<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph glyphByID(int ID)</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.index"></a>

## `index`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.index" href="#-fontgate.fgGlyphsR.index"><span class="function-name">fontgate.fgGlyphsR.index</span></a> = index<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int index(fgGlyph)</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.indexByID"></a>

## `indexByID`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.indexByID" href="#-fontgate.fgGlyphsR.indexByID"><span class="function-name">fontgate.fgGlyphsR.indexByID</span></a> = indexByID<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int index(int ID)</pre>

</dd></dl>



<a name="fontgate.fgGlyphsR.rebuildUnicodeMap"></a>

## `rebuildUnicodeMap`


<dl class="function"><dt><a name="-fontgate.fgGlyphsR.rebuildUnicodeMap" href="#-fontgate.fgGlyphsR.rebuildUnicodeMap"><span class="function-name">fontgate.fgGlyphsR.rebuildUnicodeMap</span></a> = rebuildUnicodeMap<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">rebuildUnicodeMap()</pre>

</dd></dl>

