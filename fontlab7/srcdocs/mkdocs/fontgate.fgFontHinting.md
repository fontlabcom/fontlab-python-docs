

<a name="fontgate.fgFontHinting"></a>

# `fgFontHinting`


<dt class="class"><h2><span class="class-name">fontgate.fgFontHinting</span> = <a name="fontgate.fgFontHinting" href="#fontgate.fgFontHinting">class fgFontHinting</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Font Hinting data representation

Constructors:
  fgFontHinting() - default
  fgFontHinting(fgFontHinting) - copy</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgFontHinting-__cmp__" href="#fgFontHinting-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__delattr__" href="#fgFontHinting-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__getattribute__" href="#fgFontHinting-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__init__" href="#fgFontHinting-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__repr__" href="#fgFontHinting-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__setattr__" href="#fgFontHinting-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-__str__" href="#fgFontHinting-__str__"><span class="function-name">__str__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgFontHinting-__str__">__str__</a>() <==> str(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-generateStemsProgram" href="#fgFontHinting-generateStemsProgram"><span class="function-name">generateStemsProgram</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgFontHinting-generateStemsProgram">generateStemsProgram</a>(Position upm, bool keepValues)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getBlueValues" href="#fgFontHinting-getBlueValues"><span class="function-name">getBlueValues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) <a href="#fontgate.fgFontHinting-getBlueValues">getBlueValues</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getFamilyBlues" href="#fgFontHinting-getFamilyBlues"><span class="function-name">getFamilyBlues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) <a href="#fontgate.fgFontHinting-getFamilyBlues">getFamilyBlues</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getFamilyOtherBlues" href="#fgFontHinting-getFamilyOtherBlues"><span class="function-name">getFamilyOtherBlues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) <a href="#fontgate.fgFontHinting-getFamilyBlues">getFamilyBlues</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getOtherBlues" href="#fgFontHinting-getOtherBlues"><span class="function-name">getOtherBlues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) <a href="#fontgate.fgFontHinting-getOtherBlues">getOtherBlues</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getZone" href="#fgFontHinting-getZone"><span class="function-name">getZone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgZone/Nothing <a href="#fontgate.fgFontHinting-getZone">getZone</a>(int index, bool top)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgFontHinting-getZonesCount" href="#fgFontHinting-getZonesCount"><span class="function-name">getZonesCount</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgFontHinting-getZonesCount">getZonesCount</a>(bool top)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>blueFuzz</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>blueScale</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>blueShift</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>codePPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>cvt</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>dict</dt>
<dd>

<pre class="doc" markdown="0">( { string : int } )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>dropoutPPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyZones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>flex</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>forceBold</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>forceBoldTreshold</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fpgm</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>gasp</dt>
<dd>

<pre class="doc" markdown="0">( [ fgGaspRecord ] )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hdmx</dt>
<dd>

<pre class="doc" markdown="0">( [ int ] )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>maxp</dt>
<dd>

<pre class="doc" markdown="0">( fgMaxP )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>prep</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stemH</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stemSnapLimit</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stemV</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stemsH</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stemsV</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>t1stemsH</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>t1stemsV</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>t1zones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>vdmx</dt>
<dd>

<pre class="doc" markdown="0">( [ fgVdmxRecord ] )</pre>

</dd>
</dl>
<dl class="descriptor"><dt>zonePPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>zones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgFontHinting-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgFontHinting.blueFuzz"></a>

## `blueFuzz`


<dl class="descriptor"><dt>fontgate.fgFontHinting.blueFuzz</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.blueScale"></a>

## `blueScale`


<dl class="descriptor"><dt>fontgate.fgFontHinting.blueScale</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.blueShift"></a>

## `blueShift`


<dl class="descriptor"><dt>fontgate.fgFontHinting.blueShift</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.codePPM"></a>

## `codePPM`


<dl class="descriptor"><dt>fontgate.fgFontHinting.codePPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.cvt"></a>

## `cvt`


<dl class="descriptor"><dt>fontgate.fgFontHinting.cvt</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.dict"></a>

## `dict`


<dl class="descriptor"><dt>fontgate.fgFontHinting.dict</dt>
<dd>

<pre class="doc" markdown="0">( { string : int } )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.dropoutPPM"></a>

## `dropoutPPM`


<dl class="descriptor"><dt>fontgate.fgFontHinting.dropoutPPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.familyZones"></a>

## `familyZones`


<dl class="descriptor"><dt>fontgate.fgFontHinting.familyZones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.flex"></a>

## `flex`


<dl class="descriptor"><dt>fontgate.fgFontHinting.flex</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.forceBold"></a>

## `forceBold`


<dl class="descriptor"><dt>fontgate.fgFontHinting.forceBold</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.forceBoldTreshold"></a>

## `forceBoldTreshold`


<dl class="descriptor"><dt>fontgate.fgFontHinting.forceBoldTreshold</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.fpgm"></a>

## `fpgm`


<dl class="descriptor"><dt>fontgate.fgFontHinting.fpgm</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.gasp"></a>

## `gasp`


<dl class="descriptor"><dt>fontgate.fgFontHinting.gasp</dt>
<dd>

<pre class="doc" markdown="0">( [ fgGaspRecord ] )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.generateStemsProgram"></a>

## `generateStemsProgram`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.generateStemsProgram" href="#-fontgate.fgFontHinting.generateStemsProgram"><span class="function-name">fontgate.fgFontHinting.generateStemsProgram</span></a> = generateStemsProgram<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">generateStemsProgram(Position upm, bool keepValues)</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getBlueValues"></a>

## `getBlueValues`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getBlueValues" href="#-fontgate.fgFontHinting.getBlueValues"><span class="function-name">fontgate.fgFontHinting.getBlueValues</span></a> = getBlueValues<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) getBlueValues()</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getFamilyBlues"></a>

## `getFamilyBlues`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getFamilyBlues" href="#-fontgate.fgFontHinting.getFamilyBlues"><span class="function-name">fontgate.fgFontHinting.getFamilyBlues</span></a> = getFamilyBlues<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) getFamilyBlues()</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getFamilyOtherBlues"></a>

## `getFamilyOtherBlues`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getFamilyOtherBlues" href="#-fontgate.fgFontHinting.getFamilyOtherBlues"><span class="function-name">fontgate.fgFontHinting.getFamilyOtherBlues</span></a> = getFamilyOtherBlues<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) getFamilyBlues()</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getOtherBlues"></a>

## `getOtherBlues`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getOtherBlues" href="#-fontgate.fgFontHinting.getOtherBlues"><span class="function-name">fontgate.fgFontHinting.getOtherBlues</span></a> = getOtherBlues<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( float ) getOtherBlues()</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getZone"></a>

## `getZone`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getZone" href="#-fontgate.fgFontHinting.getZone"><span class="function-name">fontgate.fgFontHinting.getZone</span></a> = getZone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgZone/Nothing getZone(int index, bool top)</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.getZonesCount"></a>

## `getZonesCount`


<dl class="function"><dt><a name="-fontgate.fgFontHinting.getZonesCount" href="#-fontgate.fgFontHinting.getZonesCount"><span class="function-name">fontgate.fgFontHinting.getZonesCount</span></a> = getZonesCount<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int getZonesCount(bool top)</pre>

</dd></dl>



<a name="fontgate.fgFontHinting.hdmx"></a>

## `hdmx`


<dl class="descriptor"><dt>fontgate.fgFontHinting.hdmx</dt>
<dd>

<pre class="doc" markdown="0">( [ int ] )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.maxp"></a>

## `maxp`


<dl class="descriptor"><dt>fontgate.fgFontHinting.maxp</dt>
<dd>

<pre class="doc" markdown="0">( fgMaxP )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.prep"></a>

## `prep`


<dl class="descriptor"><dt>fontgate.fgFontHinting.prep</dt>
<dd>

<pre class="doc" markdown="0">( bytesarray )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.stemH"></a>

## `stemH`


<dl class="descriptor"><dt>fontgate.fgFontHinting.stemH</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.stemsH"></a>

## `stemsH`


<dl class="descriptor"><dt>fontgate.fgFontHinting.stemsH</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.stemSnapLimit"></a>

## `stemSnapLimit`


<dl class="descriptor"><dt>fontgate.fgFontHinting.stemSnapLimit</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.stemsV"></a>

## `stemsV`


<dl class="descriptor"><dt>fontgate.fgFontHinting.stemsV</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.stemV"></a>

## `stemV`


<dl class="descriptor"><dt>fontgate.fgFontHinting.stemV</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.t1stemsH"></a>

## `t1stemsH`


<dl class="descriptor"><dt>fontgate.fgFontHinting.t1stemsH</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.t1stemsV"></a>

## `t1stemsV`


<dl class="descriptor"><dt>fontgate.fgFontHinting.t1stemsV</dt>
<dd>

<pre class="doc" markdown="0">(fgStems)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.t1zones"></a>

## `t1zones`


<dl class="descriptor"><dt>fontgate.fgFontHinting.t1zones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.vdmx"></a>

## `vdmx`


<dl class="descriptor"><dt>fontgate.fgFontHinting.vdmx</dt>
<dd>

<pre class="doc" markdown="0">( [ fgVdmxRecord ] )</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.zonePPM"></a>

## `zonePPM`


<dl class="descriptor"><dt>fontgate.fgFontHinting.zonePPM</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgFontHinting.zones"></a>

## `zones`


<dl class="descriptor"><dt>fontgate.fgFontHinting.zones</dt>
<dd>

<pre class="doc" markdown="0">(fgZones)</pre>

</dd>
</dl>

