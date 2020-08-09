

<a name="fontlab.flInstance"></a>

# `flInstance`


<dt class="class"><h2><span class="class-name">fontlab.flInstance</span> = <a name="fontlab.flInstance" href="#fontlab.flInstance">class flInstance</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flInstance representation

Constructors:
  flInstance()
  flInstance(string name, string tsn, flLocation location)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flInstance-__delattr__" href="#flInstance-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flInstance-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-__getattribute__" href="#flInstance-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flInstance-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-__init__" href="#flInstance-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flInstance-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-__repr__" href="#flInstance-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flInstance-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-__setattr__" href="#flInstance-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flInstance-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-autoSGN" href="#flInstance-autoSGN"><span class="function-name">autoSGN</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flInstance-autoSGN">autoSGN</a>(const string &tfn)</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-autoSLV" href="#flInstance-autoSLV"><span class="function-name">autoSLV</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flInstance-autoSLV">autoSLV</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-autoTSN" href="#flInstance-autoTSN"><span class="function-name">autoTSN</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flInstance-autoTSN">autoTSN</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flInstance-setSLV" href="#flInstance-setSLV"><span class="function-name">setSLV</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flInstance-setSLV">setSLV</a>(bool bold, bool italic)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>bold</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>exportable</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>italic</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>location</dt>
<dd>

<pre class="doc" markdown="0">flLocation</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>sgn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>slv</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tsn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>weight</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>weightValue</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>width</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flInstance-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.flInstance.autoSGN"></a>

## `autoSGN`


<dl class="function"><dt><a name="-fontlab.flInstance.autoSGN" href="#-fontlab.flInstance.autoSGN"><span class="function-name">fontlab.flInstance.autoSGN</span></a> = autoSGN<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string autoSGN(const string &tfn)</pre>

</dd></dl>



<a name="fontlab.flInstance.autoSLV"></a>

## `autoSLV`


<dl class="function"><dt><a name="-fontlab.flInstance.autoSLV" href="#-fontlab.flInstance.autoSLV"><span class="function-name">fontlab.flInstance.autoSLV</span></a> = autoSLV<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int autoSLV()</pre>

</dd></dl>



<a name="fontlab.flInstance.autoTSN"></a>

## `autoTSN`


<dl class="function"><dt><a name="-fontlab.flInstance.autoTSN" href="#-fontlab.flInstance.autoTSN"><span class="function-name">fontlab.flInstance.autoTSN</span></a> = autoTSN<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string autoTSN()</pre>

</dd></dl>



<a name="fontlab.flInstance.bold"></a>

## `bold`


<dl class="descriptor"><dt>fontlab.flInstance.bold</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flInstance.exportable"></a>

## `exportable`


<dl class="descriptor"><dt>fontlab.flInstance.exportable</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flInstance.italic"></a>

## `italic`


<dl class="descriptor"><dt>fontlab.flInstance.italic</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flInstance.location"></a>

## `location`


<dl class="descriptor"><dt>fontlab.flInstance.location</dt>
<dd>

<pre class="doc" markdown="0">flLocation</pre>

</dd>
</dl>



<a name="fontlab.flInstance.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flInstance.name</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flInstance.setSLV"></a>

## `setSLV`


<dl class="function"><dt><a name="-fontlab.flInstance.setSLV" href="#-fontlab.flInstance.setSLV"><span class="function-name">fontlab.flInstance.setSLV</span></a> = setSLV<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setSLV(bool bold, bool italic)</pre>

</dd></dl>



<a name="fontlab.flInstance.sgn"></a>

## `sgn`


<dl class="descriptor"><dt>fontlab.flInstance.sgn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flInstance.slv"></a>

## `slv`


<dl class="descriptor"><dt>fontlab.flInstance.slv</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flInstance.tsn"></a>

## `tsn`


<dl class="descriptor"><dt>fontlab.flInstance.tsn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flInstance.weight"></a>

## `weight`


<dl class="descriptor"><dt>fontlab.flInstance.weight</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flInstance.weightValue"></a>

## `weightValue`


<dl class="descriptor"><dt>fontlab.flInstance.weightValue</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flInstance.width"></a>

## `width`


<dl class="descriptor"><dt>fontlab.flInstance.width</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>

