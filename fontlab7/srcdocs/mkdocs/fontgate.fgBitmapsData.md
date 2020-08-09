

<a name="fontgate.fgBitmapsData"></a>

# `fgBitmapsData`


<dt class="class"><h2><span class="class-name">fontgate.fgBitmapsData</span> = <a name="fontgate.fgBitmapsData" href="#fontgate.fgBitmapsData">class fgBitmapsData</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">BitmapsData representation

Constructors:
  fgBitmapsData() - default
  fgBitmapsData(fgBitmapsData) - copy</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgBitmapsData-OK" href="#fgBitmapsData-OK"><span class="function-name">OK</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-OK">OK</a>() - return true if status is gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__cmp__" href="#fgBitmapsData-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__delattr__" href="#fgBitmapsData-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__getattribute__" href="#fgBitmapsData-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__init__" href="#fgBitmapsData-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__repr__" href="#fgBitmapsData-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__setattr__" href="#fgBitmapsData-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-__str__" href="#fgBitmapsData-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgBitmapsData-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-bad" href="#fgBitmapsData-bad"><span class="function-name">bad</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-bad">bad</a>() - return true if status isn't gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-boundingBox" href="#fgBitmapsData-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgBitmapsData-boundingBox">boundingBox</a>(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-copy" href="#fgBitmapsData-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgBitmapsData <a href="#fontgate.fgBitmapsData-copy">copy</a>() - create alone copy of data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-countPictures" href="#fgBitmapsData-countPictures"><span class="function-name">countPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgBitmapsData-countPictures">countPictures</a>() - return pictures count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-getFontGateData" href="#fgBitmapsData-getFontGateData"><span class="function-name">getFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgBitmapsData-getFontGateData">getFontGateData</a>() always return 0</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-getType" href="#fgBitmapsData-getType"><span class="function-name">getType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontgate.fgBitmapsData-getType">getType</a>() - return 'dtBitmaps'</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-hasBody" href="#fgBitmapsData-hasBody"><span class="function-name">hasBody</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-hasBody">hasBody</a>(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-hasColors" href="#fgBitmapsData-hasColors"><span class="function-name">hasColors</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-hasColors">hasColors</a>() - return true if colors is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-hasHints" href="#fgBitmapsData-hasHints"><span class="function-name">hasHints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-hasHints">hasHints</a>() - return true if hints is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-hasPictures" href="#fgBitmapsData-hasPictures"><span class="function-name">hasPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-hasPictures">hasPictures</a>() - return true if pictures is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-modified" href="#fgBitmapsData-modified"><span class="function-name">modified</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgBitmapsData-modified">modified</a>() - always return false</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-setParent" href="#fgBitmapsData-setParent"><span class="function-name">setParent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgBitmapsData-setParent">setParent</a>(fgGlyph) - set parent glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-status" href="#fgBitmapsData-status"><span class="function-name">status</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' <a href="#fontgate.fgBitmapsData-status">status</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-transform" href="#fgBitmapsData-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgBitmapsData-transform">transform</a>(fgMatrix) - transform data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgBitmapsData-updated" href="#fgBitmapsData-updated"><span class="function-name">updated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgBitmapsData-updated">updated</a>() - mark data as changed, reset internal caches</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>bitmaps</dt>
<dd>

<pre class="doc" markdown="0">(fgBitmaps) - list of fgRendered objects</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgBitmapsData-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgBitmapsData.bad"></a>

## `bad`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.bad" href="#-fontgate.fgBitmapsData.bad"><span class="function-name">fontgate.fgBitmapsData.bad</span></a> = bad<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool bad() - return true if status isn't gdsOK</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.bitmaps"></a>

## `bitmaps`


<dl class="descriptor"><dt>fontgate.fgBitmapsData.bitmaps</dt>
<dd>

<pre class="doc" markdown="0">(fgBitmaps) - list of fgRendered objects</pre>

</dd>
</dl>



<a name="fontgate.fgBitmapsData.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.boundingBox" href="#-fontgate.fgBitmapsData.boundingBox"><span class="function-name">fontgate.fgBitmapsData.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.copy" href="#-fontgate.fgBitmapsData.copy"><span class="function-name">fontgate.fgBitmapsData.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgBitmapsData copy() - create alone copy of data</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.countPictures"></a>

## `countPictures`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.countPictures" href="#-fontgate.fgBitmapsData.countPictures"><span class="function-name">fontgate.fgBitmapsData.countPictures</span></a> = countPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countPictures() - return pictures count</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.getFontGateData"></a>

## `getFontGateData`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.getFontGateData" href="#-fontgate.fgBitmapsData.getFontGateData"><span class="function-name">fontgate.fgBitmapsData.getFontGateData</span></a> = getFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getFontGateData() always return 0</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.getType"></a>

## `getType`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.getType" href="#-fontgate.fgBitmapsData.getType"><span class="function-name">fontgate.fgBitmapsData.getType</span></a> = getType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getType() - return 'dtBitmaps'</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.hasBody"></a>

## `hasBody`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.hasBody" href="#-fontgate.fgBitmapsData.hasBody"><span class="function-name">fontgate.fgBitmapsData.hasBody</span></a> = hasBody<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasBody(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.hasColors"></a>

## `hasColors`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.hasColors" href="#-fontgate.fgBitmapsData.hasColors"><span class="function-name">fontgate.fgBitmapsData.hasColors</span></a> = hasColors<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasColors() - return true if colors is present</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.hasHints"></a>

## `hasHints`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.hasHints" href="#-fontgate.fgBitmapsData.hasHints"><span class="function-name">fontgate.fgBitmapsData.hasHints</span></a> = hasHints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasHints() - return true if hints is present</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.hasPictures"></a>

## `hasPictures`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.hasPictures" href="#-fontgate.fgBitmapsData.hasPictures"><span class="function-name">fontgate.fgBitmapsData.hasPictures</span></a> = hasPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasPictures() - return true if pictures is present</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.modified"></a>

## `modified`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.modified" href="#-fontgate.fgBitmapsData.modified"><span class="function-name">fontgate.fgBitmapsData.modified</span></a> = modified<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool modified() - always return false</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.OK"></a>

## `OK`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.OK" href="#-fontgate.fgBitmapsData.OK"><span class="function-name">fontgate.fgBitmapsData.OK</span></a> = OK<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool OK() - return true if status is gdsOK</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.setParent"></a>

## `setParent`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.setParent" href="#-fontgate.fgBitmapsData.setParent"><span class="function-name">fontgate.fgBitmapsData.setParent</span></a> = setParent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setParent(fgGlyph) - set parent glyph</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.status"></a>

## `status`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.status" href="#-fontgate.fgBitmapsData.status"><span class="function-name">fontgate.fgBitmapsData.status</span></a> = status<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' status()</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.transform" href="#-fontgate.fgBitmapsData.transform"><span class="function-name">fontgate.fgBitmapsData.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix) - transform data</pre>

</dd></dl>



<a name="fontgate.fgBitmapsData.updated"></a>

## `updated`


<dl class="function"><dt><a name="-fontgate.fgBitmapsData.updated" href="#-fontgate.fgBitmapsData.updated"><span class="function-name">fontgate.fgBitmapsData.updated</span></a> = updated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updated() - mark data as changed, reset internal caches</pre>

</dd></dl>

