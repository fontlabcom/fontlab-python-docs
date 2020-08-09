

<a name="fontlab.fgSymbol"></a>

# `fgSymbol`


<dt class="class"><h2><span class="class-name">fontlab.fgSymbol</span> = <a name="fontlab.fgSymbol" href="#fontlab.fgSymbol">class fgSymbol</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">fgSymbol representation

Constructors:
  fgSymbol() - default
  fgSymbol(fgSymbol) - copy
  fgSymbol(unicode)
  fgSymbol('name')
  fgSymbol(id, fgFont)
  fgSymbol(glyph_id, package_id)
  fgSymbol(unicode, 'name', id)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgSymbol-__delattr__" href="#fgSymbol-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.fgSymbol-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-__getattribute__" href="#fgSymbol-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.fgSymbol-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-__init__" href="#fgSymbol-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.fgSymbol-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-__repr__" href="#fgSymbol-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.fgSymbol-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-__setattr__" href="#fgSymbol-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.fgSymbol-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-clear" href="#fgSymbol-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-clear">clear</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-clearData" href="#fgSymbol-clearData"><span class="function-name">clearData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-clearData">clearData</a>(DataCode)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-clearID" href="#fgSymbol-clearID"><span class="function-name">clearID</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-clearID">clearID</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-compare" href="#fgSymbol-compare"><span class="function-name">compare</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.fgSymbol-compare">compare</a>(fgSymbol)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-computeID" href="#fgSymbol-computeID"><span class="function-name">computeID</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.fgSymbol-computeID">computeID</a>(fgFont)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-containsData" href="#fgSymbol-containsData"><span class="function-name">containsData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.fgSymbol-containsData">containsData</a>(DataCode)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-data" href="#fgSymbol-data"><span class="function-name">data</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QVariant <a href="#fontlab.fgSymbol-data">data</a>(DataCode)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-glyph" href="#fgSymbol-glyph"><span class="function-name">glyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph <a href="#fontlab.fgSymbol-glyph">glyph</a>(fgFont, bool setId)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-init" href="#fgSymbol-init"><span class="function-name">init</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-init">init</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-setData" href="#fgSymbol-setData"><span class="function-name">setData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-setData">setData</a>(DataCode, QVariant d)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgSymbol-setSterile" href="#fgSymbol-setSterile"><span class="function-name">setSterile</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.fgSymbol-setSterile">setSterile</a>()</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>cr</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>empty</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>glyphIndex</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasName</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasUnicode</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
<dd>

<pre class="doc" markdown="0">unsigned long</pre>

</dd>
</dl>
<dl class="descriptor"><dt>layerName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ligatureIndex</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>pid</dt>
<dd>

<pre class="doc" markdown="0">unsigned long</pre>

</dd>
</dl>
<dl class="descriptor"><dt>space</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>unicode</dt>
<dd>

<pre class="doc" markdown="0">uint</pre>

</dd>
</dl>
<dl class="descriptor"><dt>unicodeEnsure</dt>
<dd>

<pre class="doc" markdown="0">uint</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">DataCode</span> = {'Active': 9, 'ColorMark': 10, 'DoFeatures': 6, 'DoLayout': 5, 'Features': 7, 'FontSize': 3, 'GlyphIndex': 0, 'LigatureIndex': 1, 'Locked': 2, 'PackageID': 4, ...}</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.fgSymbol-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.fgSymbol.clear"></a>

## `clear`


<dl class="function"><dt><a name="-fontlab.fgSymbol.clear" href="#-fontlab.fgSymbol.clear"><span class="function-name">fontlab.fgSymbol.clear</span></a> = clear<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clear()</pre>

</dd></dl>



<a name="fontlab.fgSymbol.clearData"></a>

## `clearData`


<dl class="function"><dt><a name="-fontlab.fgSymbol.clearData" href="#-fontlab.fgSymbol.clearData"><span class="function-name">fontlab.fgSymbol.clearData</span></a> = clearData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearData(DataCode)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.clearID"></a>

## `clearID`


<dl class="function"><dt><a name="-fontlab.fgSymbol.clearID" href="#-fontlab.fgSymbol.clearID"><span class="function-name">fontlab.fgSymbol.clearID</span></a> = clearID<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearID()</pre>

</dd></dl>



<a name="fontlab.fgSymbol.compare"></a>

## `compare`


<dl class="function"><dt><a name="-fontlab.fgSymbol.compare" href="#-fontlab.fgSymbol.compare"><span class="function-name">fontlab.fgSymbol.compare</span></a> = compare<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool compare(fgSymbol)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.computeID"></a>

## `computeID`


<dl class="function"><dt><a name="-fontlab.fgSymbol.computeID" href="#-fontlab.fgSymbol.computeID"><span class="function-name">fontlab.fgSymbol.computeID</span></a> = computeID<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool computeID(fgFont)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.containsData"></a>

## `containsData`


<dl class="function"><dt><a name="-fontlab.fgSymbol.containsData" href="#-fontlab.fgSymbol.containsData"><span class="function-name">fontlab.fgSymbol.containsData</span></a> = containsData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool containsData(DataCode)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.cr"></a>

## `cr`


<dl class="descriptor"><dt>fontlab.fgSymbol.cr</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.data"></a>

## `data`


<dl class="function"><dt><a name="-fontlab.fgSymbol.data" href="#-fontlab.fgSymbol.data"><span class="function-name">fontlab.fgSymbol.data</span></a> = data<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QVariant data(DataCode)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.DataCode"></a>

## `DataCode`


<span class="other-name">fontlab.fgSymbol.DataCode</span> = {'Active': 9, 'ColorMark': 10, 'DoFeatures': 6, 'DoLayout': 5, 'Features': 7, 'FontSize': 3, 'GlyphIndex': 0, 'LigatureIndex': 1, 'Locked': 2, 'PackageID': 4, ...}


<a name="fontlab.fgSymbol.empty"></a>

## `empty`


<dl class="descriptor"><dt>fontlab.fgSymbol.empty</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.glyph"></a>

## `glyph`


<dl class="function"><dt><a name="-fontlab.fgSymbol.glyph" href="#-fontlab.fgSymbol.glyph"><span class="function-name">fontlab.fgSymbol.glyph</span></a> = glyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyph glyph(fgFont, bool setId)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.glyphIndex"></a>

## `glyphIndex`


<dl class="descriptor"><dt>fontlab.fgSymbol.glyphIndex</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.hasName"></a>

## `hasName`


<dl class="descriptor"><dt>fontlab.fgSymbol.hasName</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.hasUnicode"></a>

## `hasUnicode`


<dl class="descriptor"><dt>fontlab.fgSymbol.hasUnicode</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.fgSymbol.id</dt>
<dd>

<pre class="doc" markdown="0">unsigned long</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.init"></a>

## `init`


<dl class="function"><dt><a name="-fontlab.fgSymbol.init" href="#-fontlab.fgSymbol.init"><span class="function-name">fontlab.fgSymbol.init</span></a> = init<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">init()</pre>

</dd></dl>



<a name="fontlab.fgSymbol.layerName"></a>

## `layerName`


<dl class="descriptor"><dt>fontlab.fgSymbol.layerName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.ligatureIndex"></a>

## `ligatureIndex`


<dl class="descriptor"><dt>fontlab.fgSymbol.ligatureIndex</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.fgSymbol.name</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.pid"></a>

## `pid`


<dl class="descriptor"><dt>fontlab.fgSymbol.pid</dt>
<dd>

<pre class="doc" markdown="0">unsigned long</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.setData"></a>

## `setData`


<dl class="function"><dt><a name="-fontlab.fgSymbol.setData" href="#-fontlab.fgSymbol.setData"><span class="function-name">fontlab.fgSymbol.setData</span></a> = setData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setData(DataCode, QVariant d)</pre>

</dd></dl>



<a name="fontlab.fgSymbol.setSterile"></a>

## `setSterile`


<dl class="function"><dt><a name="-fontlab.fgSymbol.setSterile" href="#-fontlab.fgSymbol.setSterile"><span class="function-name">fontlab.fgSymbol.setSterile</span></a> = setSterile<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setSterile()</pre>

</dd></dl>



<a name="fontlab.fgSymbol.space"></a>

## `space`


<dl class="descriptor"><dt>fontlab.fgSymbol.space</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.unicode"></a>

## `unicode`


<dl class="descriptor"><dt>fontlab.fgSymbol.unicode</dt>
<dd>

<pre class="doc" markdown="0">uint</pre>

</dd>
</dl>



<a name="fontlab.fgSymbol.unicodeEnsure"></a>

## `unicodeEnsure`


<dl class="descriptor"><dt>fontlab.fgSymbol.unicodeEnsure</dt>
<dd>

<pre class="doc" markdown="0">uint</pre>

</dd>
</dl>

