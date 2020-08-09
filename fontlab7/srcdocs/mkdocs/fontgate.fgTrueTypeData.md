

<a name="fontgate.fgTrueTypeData"></a>

# `fgTrueTypeData`


<dt class="class"><h2><span class="class-name">fontgate.fgTrueTypeData</span> = <a name="fontgate.fgTrueTypeData" href="#fontgate.fgTrueTypeData">class fgTrueTypeData</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">TrueTypeData representation

Constructors:
  fgTrueTypeData() - default
  fgTrueTypeData(fgTrueTypeData) - copy</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgTrueTypeData-OK" href="#fgTrueTypeData-OK"><span class="function-name">OK</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-OK">OK</a>() - return true if status is gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__cmp__" href="#fgTrueTypeData-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__delattr__" href="#fgTrueTypeData-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__getattribute__" href="#fgTrueTypeData-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__init__" href="#fgTrueTypeData-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__repr__" href="#fgTrueTypeData-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-__setattr__" href="#fgTrueTypeData-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgTrueTypeData-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-bad" href="#fgTrueTypeData-bad"><span class="function-name">bad</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-bad">bad</a>() - return true if status isn't gdsOK</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-bottomSideBearing" href="#fgTrueTypeData-bottomSideBearing"><span class="function-name">bottomSideBearing</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgTrueTypeData-bottomSideBearing">bottomSideBearing</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-boundingBox" href="#fgTrueTypeData-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect <a href="#fontgate.fgTrueTypeData-boundingBox">boundingBox</a>(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-clearImports" href="#fgTrueTypeData-clearImports"><span class="function-name">clearImports</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgTrueTypeData-clearImports">clearImports</a>() - clear instructions and hdmx, set yPels = 1</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-copy" href="#fgTrueTypeData-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgTrueTypeData <a href="#fontgate.fgTrueTypeData-copy">copy</a>() - create alone copy of data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-countPictures" href="#fgTrueTypeData-countPictures"><span class="function-name">countPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgTrueTypeData-countPictures">countPictures</a>() - return pictures count</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-empty" href="#fgTrueTypeData-empty"><span class="function-name">empty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-empty">empty</a>() - return true if state == sEmpty or no endpoints present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-getFontGateData" href="#fgTrueTypeData-getFontGateData"><span class="function-name">getFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontgate.fgTrueTypeData-getFontGateData">getFontGateData</a>() - return Nothing</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-getType" href="#fgTrueTypeData-getType"><span class="function-name">getType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontgate.fgTrueTypeData-getType">getType</a>() - return 'dtTrueType'</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-hasBody" href="#fgTrueTypeData-hasBody"><span class="function-name">hasBody</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-hasBody">hasBody</a>(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-hasColors" href="#fgTrueTypeData-hasColors"><span class="function-name">hasColors</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-hasColors">hasColors</a>() - return true if colors is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-hasHints" href="#fgTrueTypeData-hasHints"><span class="function-name">hasHints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-hasHints">hasHints</a>() - return true if hints is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-hasPictures" href="#fgTrueTypeData-hasPictures"><span class="function-name">hasPictures</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-hasPictures">hasPictures</a>() - return true if pictures is present</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-modified" href="#fgTrueTypeData-modified"><span class="function-name">modified</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-modified">modified</a>() - return true if data was changed</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-rightSideBearing" href="#fgTrueTypeData-rightSideBearing"><span class="function-name">rightSideBearing</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgTrueTypeData-rightSideBearing">rightSideBearing</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-setParent" href="#fgTrueTypeData-setParent"><span class="function-name">setParent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgTrueTypeData-setParent">setParent</a>(fgGlyph) - set parent glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-status" href="#fgTrueTypeData-status"><span class="function-name">status</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' <a href="#fontgate.fgTrueTypeData-status">status</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-transform" href="#fgTrueTypeData-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgTrueTypeData-transform">transform</a>(fgMatrix) - transform data</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-updateBoundingBox" href="#fgTrueTypeData-updateBoundingBox"><span class="function-name">updateBoundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgTrueTypeData-updateBoundingBox">updateBoundingBox</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-updated" href="#fgTrueTypeData-updated"><span class="function-name">updated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgTrueTypeData-updated">updated</a>() - mark data as changed, reset internal caches</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-valid" href="#fgTrueTypeData-valid"><span class="function-name">valid</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgTrueTypeData-valid">valid</a>() - return true if state == sValid | sDecomposed</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-xExtent" href="#fgTrueTypeData-xExtent"><span class="function-name">xExtent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgTrueTypeData-xExtent">xExtent</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgTrueTypeData-yExtent" href="#fgTrueTypeData-yExtent"><span class="function-name">yExtent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgTrueTypeData-yExtent">yExtent</a>()</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>advanceHeight</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>advanceWidth</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>endpoint</dt>
<dd>

<pre class="doc" markdown="0">([int])</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hdmx</dt>
<dd>

<pre class="doc" markdown="0">(fgHdmx)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>instructions</dt>
<dd>

<pre class="doc" markdown="0">(fgBuffer)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>leftSideBearing</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>points</dt>
<dd>

<pre class="doc" markdown="0">(fgTrueTypePoints)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>pointsMap</dt>
<dd>

<pre class="doc" markdown="0">({ 'name': int value })</pre>

</dd>
</dl>
<dl class="descriptor"><dt>topSideBearing</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>xMax</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>xMin</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>yMax</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>yMin</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>yPels</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgTrueTypeData-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgTrueTypeData.advanceHeight"></a>

## `advanceHeight`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.advanceHeight</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.advanceWidth"></a>

## `advanceWidth`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.advanceWidth</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.bad"></a>

## `bad`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.bad" href="#-fontgate.fgTrueTypeData.bad"><span class="function-name">fontgate.fgTrueTypeData.bad</span></a> = bad<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool bad() - return true if status isn't gdsOK</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.bottomSideBearing"></a>

## `bottomSideBearing`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.bottomSideBearing" href="#-fontgate.fgTrueTypeData.bottomSideBearing"><span class="function-name">fontgate.fgTrueTypeData.bottomSideBearing</span></a> = bottomSideBearing<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int bottomSideBearing()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.boundingBox" href="#-fontgate.fgTrueTypeData.boundingBox"><span class="function-name">fontgate.fgTrueTypeData.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect boundingBox(fgGlyphsR, fgMatrix, bool prepareExport) - calculate bounding box</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.clearImports"></a>

## `clearImports`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.clearImports" href="#-fontgate.fgTrueTypeData.clearImports"><span class="function-name">fontgate.fgTrueTypeData.clearImports</span></a> = clearImports<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearImports() - clear instructions and hdmx, set yPels = 1</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.copy"></a>

## `copy`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.copy" href="#-fontgate.fgTrueTypeData.copy"><span class="function-name">fontgate.fgTrueTypeData.copy</span></a> = copy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgTrueTypeData copy() - create alone copy of data</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.countPictures"></a>

## `countPictures`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.countPictures" href="#-fontgate.fgTrueTypeData.countPictures"><span class="function-name">fontgate.fgTrueTypeData.countPictures</span></a> = countPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countPictures() - return pictures count</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.empty"></a>

## `empty`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.empty" href="#-fontgate.fgTrueTypeData.empty"><span class="function-name">fontgate.fgTrueTypeData.empty</span></a> = empty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool empty() - return true if state == sEmpty or no endpoints present</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.endpoint"></a>

## `endpoint`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.endpoint</dt>
<dd>

<pre class="doc" markdown="0">([int])</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.getFontGateData"></a>

## `getFontGateData`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.getFontGateData" href="#-fontgate.fgTrueTypeData.getFontGateData"><span class="function-name">fontgate.fgTrueTypeData.getFontGateData</span></a> = getFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData getFontGateData() - return Nothing</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.getType"></a>

## `getType`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.getType" href="#-fontgate.fgTrueTypeData.getType"><span class="function-name">fontgate.fgTrueTypeData.getType</span></a> = getType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getType() - return 'dtTrueType'</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.hasBody"></a>

## `hasBody`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.hasBody" href="#-fontgate.fgTrueTypeData.hasBody"><span class="function-name">fontgate.fgTrueTypeData.hasBody</span></a> = hasBody<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasBody(bool prepareExport) - return true if non-empty body layer is present</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.hasColors"></a>

## `hasColors`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.hasColors" href="#-fontgate.fgTrueTypeData.hasColors"><span class="function-name">fontgate.fgTrueTypeData.hasColors</span></a> = hasColors<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasColors() - return true if colors is present</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.hasHints"></a>

## `hasHints`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.hasHints" href="#-fontgate.fgTrueTypeData.hasHints"><span class="function-name">fontgate.fgTrueTypeData.hasHints</span></a> = hasHints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasHints() - return true if hints is present</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.hasPictures"></a>

## `hasPictures`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.hasPictures" href="#-fontgate.fgTrueTypeData.hasPictures"><span class="function-name">fontgate.fgTrueTypeData.hasPictures</span></a> = hasPictures<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasPictures() - return true if pictures is present</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.hdmx"></a>

## `hdmx`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.hdmx</dt>
<dd>

<pre class="doc" markdown="0">(fgHdmx)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.instructions"></a>

## `instructions`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.instructions</dt>
<dd>

<pre class="doc" markdown="0">(fgBuffer)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.leftSideBearing"></a>

## `leftSideBearing`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.leftSideBearing</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.modified"></a>

## `modified`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.modified" href="#-fontgate.fgTrueTypeData.modified"><span class="function-name">fontgate.fgTrueTypeData.modified</span></a> = modified<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool modified() - return true if data was changed</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.OK"></a>

## `OK`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.OK" href="#-fontgate.fgTrueTypeData.OK"><span class="function-name">fontgate.fgTrueTypeData.OK</span></a> = OK<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool OK() - return true if status is gdsOK</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.points"></a>

## `points`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.points</dt>
<dd>

<pre class="doc" markdown="0">(fgTrueTypePoints)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.pointsMap"></a>

## `pointsMap`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.pointsMap</dt>
<dd>

<pre class="doc" markdown="0">({ 'name': int value })</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.rightSideBearing"></a>

## `rightSideBearing`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.rightSideBearing" href="#-fontgate.fgTrueTypeData.rightSideBearing"><span class="function-name">fontgate.fgTrueTypeData.rightSideBearing</span></a> = rightSideBearing<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int rightSideBearing()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.setParent"></a>

## `setParent`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.setParent" href="#-fontgate.fgTrueTypeData.setParent"><span class="function-name">fontgate.fgTrueTypeData.setParent</span></a> = setParent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setParent(fgGlyph) - set parent glyph</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.status"></a>

## `status`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.status" href="#-fontgate.fgTrueTypeData.status"><span class="function-name">fontgate.fgTrueTypeData.status</span></a> = status<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">'gdsOK'/'gdsInvalid' status()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.topSideBearing"></a>

## `topSideBearing`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.topSideBearing</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.transform" href="#-fontgate.fgTrueTypeData.transform"><span class="function-name">fontgate.fgTrueTypeData.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix) - transform data</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.updateBoundingBox"></a>

## `updateBoundingBox`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.updateBoundingBox" href="#-fontgate.fgTrueTypeData.updateBoundingBox"><span class="function-name">fontgate.fgTrueTypeData.updateBoundingBox</span></a> = updateBoundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateBoundingBox()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.updated"></a>

## `updated`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.updated" href="#-fontgate.fgTrueTypeData.updated"><span class="function-name">fontgate.fgTrueTypeData.updated</span></a> = updated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updated() - mark data as changed, reset internal caches</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.valid"></a>

## `valid`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.valid" href="#-fontgate.fgTrueTypeData.valid"><span class="function-name">fontgate.fgTrueTypeData.valid</span></a> = valid<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool valid() - return true if state == sValid | sDecomposed</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.xExtent"></a>

## `xExtent`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.xExtent" href="#-fontgate.fgTrueTypeData.xExtent"><span class="function-name">fontgate.fgTrueTypeData.xExtent</span></a> = xExtent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int xExtent()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.xMax"></a>

## `xMax`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.xMax</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.xMin"></a>

## `xMin`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.xMin</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.yExtent"></a>

## `yExtent`


<dl class="function"><dt><a name="-fontgate.fgTrueTypeData.yExtent" href="#-fontgate.fgTrueTypeData.yExtent"><span class="function-name">fontgate.fgTrueTypeData.yExtent</span></a> = yExtent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int yExtent()</pre>

</dd></dl>



<a name="fontgate.fgTrueTypeData.yMax"></a>

## `yMax`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.yMax</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.yMin"></a>

## `yMin`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.yMin</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgTrueTypeData.yPels"></a>

## `yPels`


<dl class="descriptor"><dt>fontgate.fgTrueTypeData.yPels</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>

