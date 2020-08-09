

<a name="typerig.proxy.objects.curve"></a>

# `typerig.proxy.objects.curve`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.curve (<span class="info">version 0.3.7)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Curve (Objects)
# ----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li><li>PythonQt</li><li>random</li><li>typerig.core.objects</li><li>warnings</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.curve.html#eCurveEx">eCurveEx</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eCurveEx" href="#eCurveEx">class <span class="class-name">eCurveEx</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of flCurveEx, adding some advanced functionality

Constructor:
        eCurveEx(flCurveEx, list[flNode])
        eCurveEx(list[flNode])
        eCurveEx(flContour, time (int))
        ...</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eCurveEx-__init__" href="#eCurveEx-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-__repr__" href="#eCurveEx-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basic functionality ----------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqHobbySpline" href="#eCurveEx-eqHobbySpline"><span class="function-name">eqHobbySpline</span></a><span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqProportionalHandles" href="#eCurveEx-eqProportionalHandles"><span class="function-name">eqProportionalHandles</span></a><span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqRatioHandles" href="#eCurveEx-eqRatioHandles"><span class="function-name">eqRatioHandles</span></a><span class="argspec">(self, ratio<span class="parameter-default">=0.3</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqTunni" href="#eCurveEx-eqTunni"><span class="function-name">eqTunni</span></a><span class="argspec">(self, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Curve optimization ----------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-updateCurve" href="#eCurveEx-updateCurve"><span class="function-name">updateCurve</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-updateNodes" href="#eCurveEx-updateNodes"><span class="function-name">updateNodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
</dd></dl></div></div>


<a name="typerig.proxy.objects.curve.eCurveEx"></a>

## `eCurveEx`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.curve.eCurveEx</span> = <a name="typerig.proxy.objects.curve.eCurveEx" href="#typerig.proxy.objects.curve.eCurveEx">class eCurveEx</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of flCurveEx, adding some advanced functionality

Constructor:
        eCurveEx(flCurveEx, list[flNode])
        eCurveEx(list[flNode])
        eCurveEx(flContour, time (int))
        ...</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eCurveEx-__init__" href="#eCurveEx-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *argv)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-__repr__" href="#eCurveEx-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basic functionality ----------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqHobbySpline" href="#eCurveEx-eqHobbySpline"><span class="function-name">eqHobbySpline</span></a><span class="argspec">(self, curvature<span class="parameter-default">=(0.9, 0.9)</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqProportionalHandles" href="#eCurveEx-eqProportionalHandles"><span class="function-name">eqProportionalHandles</span></a><span class="argspec">(self, proportion<span class="parameter-default">=0.3</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqRatioHandles" href="#eCurveEx-eqRatioHandles"><span class="function-name">eqRatioHandles</span></a><span class="argspec">(self, ratio<span class="parameter-default">=0.3</span>, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-eqTunni" href="#eCurveEx-eqTunni"><span class="function-name">eqTunni</span></a><span class="argspec">(self, apply<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Curve optimization ----------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-updateCurve" href="#eCurveEx-updateCurve"><span class="function-name">updateCurve</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eCurveEx-updateNodes" href="#eCurveEx-updateNodes"><span class="function-name">updateNodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
</dd>
