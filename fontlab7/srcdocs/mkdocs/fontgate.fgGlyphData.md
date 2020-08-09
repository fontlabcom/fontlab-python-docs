

<a name="fontgate.fgGlyphData"></a>

# `fgGlyphData`


<dt class="class"><h2><span class="class-name">fontgate.fgGlyphData</span> = <a name="fontgate.fgGlyphData" href="#fontgate.fgGlyphData">class fgGlyphData</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">GlyphData representation

Constructors:
  fgGlyphData() - default
  fgGlyphData(fgGlyphData) - copy</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgGlyphData-OK" href="#fgGlyphData-OK"><span class="function-name">OK</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-OK">OK</a>() - return true if status is gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__cmp__" href="#fgGlyphData-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__delattr__" href="#fgGlyphData-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__getattribute__" href="#fgGlyphData-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__init__" href="#fgGlyphData-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__repr__" href="#fgGlyphData-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-__setattr__" href="#fgGlyphData-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgGlyphData-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-bad" href="#fgGlyphData-bad"><span class="function-name">bad</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-bad">bad</a>() - return true if status isn't gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-boundingBox" href="#fgGlyphData-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgGlyphData-boundingBox">boundingBox</a>(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-copy" href="#fgGlyphData-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyphData <a href="#fontgate.fgGlyphData-copy">copy</a>() - create alone copy of data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-countPictures" href="#fgGlyphData-countPictures"><span class="function-name">countPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgGlyphData-countPictures">countPictures</a>() - return pictures count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-countShapes" href="#fgGlyphData-countShapes"><span class="function-name">countShapes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgGlyphData-countShapes">countShapes</a>() - return shapes count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-getFontGateData" href="#fgGlyphData-getFontGateData"><span class="function-name">getFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontgate.fgGlyphData-getFontGateData">getFontGateData</a>() - return Nothing</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-getType" href="#fgGlyphData-getType"><span class="function-name">getType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontgate.fgGlyphData-getType">getType</a>() - return 'dtTrueType'</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-hasBody" href="#fgGlyphData-hasBody"><span class="function-name">hasBody</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-hasBody">hasBody</a>(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-hasColors" href="#fgGlyphData-hasColors"><span class="function-name">hasColors</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-hasColors">hasColors</a>() - return true if colors is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-hasHints" href="#fgGlyphData-hasHints"><span class="function-name">hasHints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-hasHints">hasHints</a>() - return true if hints is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-hasPictures" href="#fgGlyphData-hasPictures"><span class="function-name">hasPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-hasPictures">hasPictures</a>() - return true if pictures is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-modified" href="#fgGlyphData-modified"><span class="function-name">modified</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgGlyphData-modified">modified</a>() - return true if data was changed</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-setParent" href="#fgGlyphData-setParent"><span class="function-name">setParent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgGlyphData-setParent">setParent</a>(fgGlyph) - set parent glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-status" href="#fgGlyphData-status"><span class="function-name">status</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' <a href="#fontgate.fgGlyphData-status">status</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-transform" href="#fgGlyphData-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgGlyphData-transform">transform</a>(fgMatrix) - transform data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgGlyphData-updated" href="#fgGlyphData-updated"><span class="function-name">updated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgGlyphData-updated">updated</a>() - mark data as changed, reset internal caches</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgGlyphData-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgGlyphData.bad"></a>

## `bad`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.bad" href="#-fontgate.fgGlyphData.bad"><span class="function-name">fontgate.fgGlyphData.bad</span></a> = bad<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool bad() - return true if status isn't gdsOK</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.boundingBox" href="#-fontgate.fgGlyphData.boundingBox"><span class="function-name">fontgate.fgGlyphData.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.copy" href="#-fontgate.fgGlyphData.copy"><span class="function-name">fontgate.fgGlyphData.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgGlyphData copy() - create alone copy of data</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.countPictures"></a>

## `countPictures`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.countPictures" href="#-fontgate.fgGlyphData.countPictures"><span class="function-name">fontgate.fgGlyphData.countPictures</span></a> = countPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countPictures() - return pictures count</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.countShapes"></a>

## `countShapes`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.countShapes" href="#-fontgate.fgGlyphData.countShapes"><span class="function-name">fontgate.fgGlyphData.countShapes</span></a> = countShapes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countShapes() - return shapes count</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.getFontGateData"></a>

## `getFontGateData`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.getFontGateData" href="#-fontgate.fgGlyphData.getFontGateData"><span class="function-name">fontgate.fgGlyphData.getFontGateData</span></a> = getFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData getFontGateData() - return Nothing</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.getType"></a>

## `getType`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.getType" href="#-fontgate.fgGlyphData.getType"><span class="function-name">fontgate.fgGlyphData.getType</span></a> = getType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getType() - return 'dtTrueType'</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.hasBody"></a>

## `hasBody`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.hasBody" href="#-fontgate.fgGlyphData.hasBody"><span class="function-name">fontgate.fgGlyphData.hasBody</span></a> = hasBody<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasBody(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.hasColors"></a>

## `hasColors`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.hasColors" href="#-fontgate.fgGlyphData.hasColors"><span class="function-name">fontgate.fgGlyphData.hasColors</span></a> = hasColors<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasColors() - return true if colors is present</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.hasHints"></a>

## `hasHints`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.hasHints" href="#-fontgate.fgGlyphData.hasHints"><span class="function-name">fontgate.fgGlyphData.hasHints</span></a> = hasHints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasHints() - return true if hints is present</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.hasPictures"></a>

## `hasPictures`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.hasPictures" href="#-fontgate.fgGlyphData.hasPictures"><span class="function-name">fontgate.fgGlyphData.hasPictures</span></a> = hasPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasPictures() - return true if pictures is present</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.modified"></a>

## `modified`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.modified" href="#-fontgate.fgGlyphData.modified"><span class="function-name">fontgate.fgGlyphData.modified</span></a> = modified<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool modified() - return true if data was changed</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.OK"></a>

## `OK`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.OK" href="#-fontgate.fgGlyphData.OK"><span class="function-name">fontgate.fgGlyphData.OK</span></a> = OK<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool OK() - return true if status is gdsOK</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.setParent"></a>

## `setParent`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.setParent" href="#-fontgate.fgGlyphData.setParent"><span class="function-name">fontgate.fgGlyphData.setParent</span></a> = setParent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setParent(fgGlyph) - set parent glyph</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.status"></a>

## `status`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.status" href="#-fontgate.fgGlyphData.status"><span class="function-name">fontgate.fgGlyphData.status</span></a> = status<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' status()</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.transform" href="#-fontgate.fgGlyphData.transform"><span class="function-name">fontgate.fgGlyphData.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix) - transform data</pre>

</dd></dl>



<a name="fontgate.fgGlyphData.updated"></a>

## `updated`


<dl class="function"><dt><a name="-fontgate.fgGlyphData.updated" href="#-fontgate.fgGlyphData.updated"><span class="function-name">fontgate.fgGlyphData.updated</span></a> = updated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updated() - mark data as changed, reset internal caches</pre>

</dd></dl>

