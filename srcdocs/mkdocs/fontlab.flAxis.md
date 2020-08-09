

<a name="fontlab.flAxis"></a>

# `flAxis`


<dt class="class"><h2><span class="class-name">fontlab.flAxis</span> = <a name="fontlab.flAxis" href="#fontlab.flAxis">class flAxis</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flAxis representation

Constructors:
  flAxis() - default
  flAxis(string name)
  flAxis(string name, string tag, string short_name)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flAxis-__delattr__" href="#flAxis-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flAxis-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-__getattribute__" href="#flAxis-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flAxis-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-__init__" href="#flAxis-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flAxis-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-__repr__" href="#flAxis-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flAxis-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-__setattr__" href="#flAxis-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flAxis-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-checkValue" href="#flAxis-checkValue"><span class="function-name">checkValue</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-checkValue">checkValue</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-getRange" href="#flAxis-getRange"><span class="function-name">getRange</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-getRange">getRange</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-instanceIndex" href="#flAxis-instanceIndex"><span class="function-name">instanceIndex</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flAxis-instanceIndex">instanceIndex</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-instances2map" href="#flAxis-instances2map"><span class="function-name">instances2map</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-instances2map">instances2map</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-instances2string" href="#flAxis-instances2string"><span class="function-name">instances2string</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flAxis-instances2string">instances2string</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-map2instances" href="#flAxis-map2instances"><span class="function-name">map2instances</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-map2instances">map2instances</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-mappedValue" href="#flAxis-mappedValue"><span class="function-name">mappedValue</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-mappedValue">mappedValue</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-normalize" href="#flAxis-normalize"><span class="function-name">normalize</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-normalize">normalize</a>(double userValue)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-onEdge" href="#flAxis-onEdge"><span class="function-name">onEdge</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-onEdge">onEdge</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-string2instances" href="#flAxis-string2instances"><span class="function-name">string2instances</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-string2instances">string2instances</a>(string s)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-styleName" href="#flAxis-styleName"><span class="function-name">styleName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flAxis-styleName">styleName</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-styleValue" href="#flAxis-styleValue"><span class="function-name">styleValue</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-styleValue">styleValue</a>(string style_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-updateInstances" href="#flAxis-updateInstances"><span class="function-name">updateInstances</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flAxis-updateInstances">updateInstances</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-updateShortName" href="#flAxis-updateShortName"><span class="function-name">updateShortName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flAxis-updateShortName">updateShortName</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-updateTag" href="#flAxis-updateTag"><span class="function-name">updateTag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flAxis-updateTag">updateTag</a>()</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flAxis-isWeight" href="#flAxis-isWeight"><span class="function-name">isWeight</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-isWeight">isWeight</a>(string s)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-isWidth" href="#flAxis-isWidth"><span class="function-name">isWidth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flAxis-isWidth">isWidth</a>(string s)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-locationName" href="#flAxis-locationName"><span class="function-name">locationName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString <a href="#fontlab.flAxis-locationName">locationName</a>(QList<flAxis> axes, flLocation location)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-valueWeight" href="#flAxis-valueWeight"><span class="function-name">valueWeight</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-valueWeight">valueWeight</a>(flLocation location, double value)</pre>

</dd></dl>
<dl class="function"><dt><a name="flAxis-valueWidth" href="#flAxis-valueWidth"><span class="function-name">valueWidth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flAxis-valueWidth">valueWidth</a>(flLocation location, double value)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>default</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>designDef</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>designMax</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>designMin</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hidden</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>map</dt>
<dd>

<pre class="doc" markdown="0">QMap<double,double></pre>

</dd>
</dl>
<dl class="descriptor"><dt>maximum</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>minimal</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>playRange</dt>
<dd>

<pre class="doc" markdown="0">(double, double)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>shortName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tag</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flAxis-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.flAxis.checkValue"></a>

## `checkValue`


<dl class="function"><dt><a name="-fontlab.flAxis.checkValue" href="#-fontlab.flAxis.checkValue"><span class="function-name">fontlab.flAxis.checkValue</span></a> = checkValue<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double checkValue(double v)</pre>

</dd></dl>



<a name="fontlab.flAxis.default"></a>

## `default`


<dl class="descriptor"><dt>fontlab.flAxis.default</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.designDef"></a>

## `designDef`


<dl class="descriptor"><dt>fontlab.flAxis.designDef</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.designMax"></a>

## `designMax`


<dl class="descriptor"><dt>fontlab.flAxis.designMax</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.designMin"></a>

## `designMin`


<dl class="descriptor"><dt>fontlab.flAxis.designMin</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.getRange"></a>

## `getRange`


<dl class="function"><dt><a name="-fontlab.flAxis.getRange" href="#-fontlab.flAxis.getRange"><span class="function-name">fontlab.flAxis.getRange</span></a> = getRange<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double getRange()</pre>

</dd></dl>



<a name="fontlab.flAxis.hidden"></a>

## `hidden`


<dl class="descriptor"><dt>fontlab.flAxis.hidden</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flAxis.instanceIndex"></a>

## `instanceIndex`


<dl class="function"><dt><a name="-fontlab.flAxis.instanceIndex" href="#-fontlab.flAxis.instanceIndex"><span class="function-name">fontlab.flAxis.instanceIndex</span></a> = instanceIndex<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceIndex(double v)</pre>

</dd></dl>



<a name="fontlab.flAxis.instances2map"></a>

## `instances2map`


<dl class="function"><dt><a name="-fontlab.flAxis.instances2map" href="#-fontlab.flAxis.instances2map"><span class="function-name">fontlab.flAxis.instances2map</span></a> = instances2map<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool instances2map()</pre>

</dd></dl>



<a name="fontlab.flAxis.instances2string"></a>

## `instances2string`


<dl class="function"><dt><a name="-fontlab.flAxis.instances2string" href="#-fontlab.flAxis.instances2string"><span class="function-name">fontlab.flAxis.instances2string</span></a> = instances2string<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string instances2string()</pre>

</dd></dl>



<a name="fontlab.flAxis.isWeight"></a>

## `isWeight`


<dl class="function"><dt><a name="-fontlab.flAxis.isWeight" href="#-fontlab.flAxis.isWeight"><span class="function-name">fontlab.flAxis.isWeight</span></a> = isWeight<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isWeight(string s)</pre>

</dd></dl>



<a name="fontlab.flAxis.isWidth"></a>

## `isWidth`


<dl class="function"><dt><a name="-fontlab.flAxis.isWidth" href="#-fontlab.flAxis.isWidth"><span class="function-name">fontlab.flAxis.isWidth</span></a> = isWidth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isWidth(string s)</pre>

</dd></dl>



<a name="fontlab.flAxis.locationName"></a>

## `locationName`


<dl class="function"><dt><a name="-fontlab.flAxis.locationName" href="#-fontlab.flAxis.locationName"><span class="function-name">fontlab.flAxis.locationName</span></a> = locationName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString locationName(QList<flAxis> axes, flLocation location)</pre>

</dd></dl>



<a name="fontlab.flAxis.map"></a>

## `map`


<dl class="descriptor"><dt>fontlab.flAxis.map</dt>
<dd>

<pre class="doc" markdown="0">QMap<double,double></pre>

</dd>
</dl>



<a name="fontlab.flAxis.map2instances"></a>

## `map2instances`


<dl class="function"><dt><a name="-fontlab.flAxis.map2instances" href="#-fontlab.flAxis.map2instances"><span class="function-name">fontlab.flAxis.map2instances</span></a> = map2instances<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool map2instances()</pre>

</dd></dl>



<a name="fontlab.flAxis.mappedValue"></a>

## `mappedValue`


<dl class="function"><dt><a name="-fontlab.flAxis.mappedValue" href="#-fontlab.flAxis.mappedValue"><span class="function-name">fontlab.flAxis.mappedValue</span></a> = mappedValue<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double mappedValue(double v)</pre>

</dd></dl>



<a name="fontlab.flAxis.maximum"></a>

## `maximum`


<dl class="descriptor"><dt>fontlab.flAxis.maximum</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.minimal"></a>

## `minimal`


<dl class="descriptor"><dt>fontlab.flAxis.minimal</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flAxis.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flAxis.name</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flAxis.normalize"></a>

## `normalize`


<dl class="function"><dt><a name="-fontlab.flAxis.normalize" href="#-fontlab.flAxis.normalize"><span class="function-name">fontlab.flAxis.normalize</span></a> = normalize<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double normalize(double userValue)</pre>

</dd></dl>



<a name="fontlab.flAxis.onEdge"></a>

## `onEdge`


<dl class="function"><dt><a name="-fontlab.flAxis.onEdge" href="#-fontlab.flAxis.onEdge"><span class="function-name">fontlab.flAxis.onEdge</span></a> = onEdge<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool onEdge(double v)</pre>

</dd></dl>



<a name="fontlab.flAxis.playRange"></a>

## `playRange`


<dl class="descriptor"><dt>fontlab.flAxis.playRange</dt>
<dd>

<pre class="doc" markdown="0">(double, double)</pre>

</dd>
</dl>



<a name="fontlab.flAxis.shortName"></a>

## `shortName`


<dl class="descriptor"><dt>fontlab.flAxis.shortName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flAxis.string2instances"></a>

## `string2instances`


<dl class="function"><dt><a name="-fontlab.flAxis.string2instances" href="#-fontlab.flAxis.string2instances"><span class="function-name">fontlab.flAxis.string2instances</span></a> = string2instances<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool string2instances(string s)</pre>

</dd></dl>



<a name="fontlab.flAxis.styleName"></a>

## `styleName`


<dl class="function"><dt><a name="-fontlab.flAxis.styleName" href="#-fontlab.flAxis.styleName"><span class="function-name">fontlab.flAxis.styleName</span></a> = styleName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string styleName(double v)</pre>

</dd></dl>



<a name="fontlab.flAxis.styleValue"></a>

## `styleValue`


<dl class="function"><dt><a name="-fontlab.flAxis.styleValue" href="#-fontlab.flAxis.styleValue"><span class="function-name">fontlab.flAxis.styleValue</span></a> = styleValue<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double styleValue(string style_name)</pre>

</dd></dl>



<a name="fontlab.flAxis.tag"></a>

## `tag`


<dl class="descriptor"><dt>fontlab.flAxis.tag</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flAxis.updateInstances"></a>

## `updateInstances`


<dl class="function"><dt><a name="-fontlab.flAxis.updateInstances" href="#-fontlab.flAxis.updateInstances"><span class="function-name">fontlab.flAxis.updateInstances</span></a> = updateInstances<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void updateInstances()</pre>

</dd></dl>



<a name="fontlab.flAxis.updateShortName"></a>

## `updateShortName`


<dl class="function"><dt><a name="-fontlab.flAxis.updateShortName" href="#-fontlab.flAxis.updateShortName"><span class="function-name">fontlab.flAxis.updateShortName</span></a> = updateShortName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void updateShortName()</pre>

</dd></dl>



<a name="fontlab.flAxis.updateTag"></a>

## `updateTag`


<dl class="function"><dt><a name="-fontlab.flAxis.updateTag" href="#-fontlab.flAxis.updateTag"><span class="function-name">fontlab.flAxis.updateTag</span></a> = updateTag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void updateTag()</pre>

</dd></dl>



<a name="fontlab.flAxis.valueWeight"></a>

## `valueWeight`


<dl class="function"><dt><a name="-fontlab.flAxis.valueWeight" href="#-fontlab.flAxis.valueWeight"><span class="function-name">fontlab.flAxis.valueWeight</span></a> = valueWeight<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double valueWeight(flLocation location, double value)</pre>

</dd></dl>



<a name="fontlab.flAxis.valueWidth"></a>

## `valueWidth`


<dl class="function"><dt><a name="-fontlab.flAxis.valueWidth" href="#-fontlab.flAxis.valueWidth"><span class="function-name">fontlab.flAxis.valueWidth</span></a> = valueWidth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double valueWidth(flLocation location, double value)</pre>

</dd></dl>

