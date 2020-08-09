

<a name="typerig.core.objects.utils"></a>

# `typerig.core.objects.utils`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.utils (<span class="info">version 0.26.0)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Utilities (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.utils.html#bounds">bounds</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.utils.html#geoAxis">geoAxis</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.utils.html#linAxis">linAxis</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.utils.html#fontFamilly">fontFamilly</a></span></li></ul><dl class="classes"><dt class="class"><h2><a name="bounds" href="#bounds">class <span class="class-name">bounds</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Bounding box object ----------------------------------</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="bounds-__init__" href="#bounds-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, tupleList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="bounds-recalc" href="#bounds-recalc"><span class="function-name">recalc</span></a><span class="argspec">(self, tupleList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="bounds-refresh" href="#bounds-refresh"><span class="function-name">refresh</span></a><span class="argspec">(self, tupleList)</span></dt><dd>

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
<dt class="class"><h2><a name="fontFamilly" href="#fontFamilly">class <span class="class-name">fontFamilly</span></a></h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Font familly class:
*   generates weight stems [.wt_stems] and MM weight instances [.wt_instances]
        using given masters/layers wt0, wt1, and number of weight members [wt_steps].
        Uses geometric growth (progression) algorithm to determine stem weight

*   generates MM width instances [.wd_instances] using given number
        of width members [wd_steps]. Uses linear growth.

*   generates all MM isntaces/vectors for instance generation [.instances]
---
ex: fontFamilyName = fontFamilly(wt0 = 56, wt1 = 178, wt_steps = 7, wd_steps = 3)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fontFamilly-__init__" href="#fontFamilly-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="fontFamilly-update" href="#fontFamilly-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="geoAxis" href="#geoAxis">class <span class="class-name">geoAxis</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A geometric series axis instance and stem calculator

Usage linAxis(masterDict, instanceCount), where:
*   masterDict = {min_axis_value:min_stem_width, max_axis_value:max_stem_width} ex: {0:50, 1000:750}
*   instanceCount = number of instances to be calculated</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="geoAxis-__init__" href="#geoAxis-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, masterDict, instanceCount)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="geoAxis-update" href="#geoAxis-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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
<dt class="class"><h2><a name="linAxis" href="#linAxis">class <span class="class-name">linAxis</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A linear series axis instance and stem calculator

Usage linAxis(masterDict, instanceCount), where:
*       masterDict = {min_axis_value:min_stem_width, max_axis_value:max_stem_width} ex: {0:50, 1000:750}
*       instanceCount = number of instances to be calculated</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="linAxis-__init__" href="#linAxis-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, masterDict, instanceCount)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="linAxis-update" href="#linAxis-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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


<a name="typerig.core.objects.utils.fontFamilly"></a>

## `fontFamilly`


<dt class="class"><h2><span class="class-name">typerig.core.objects.utils.fontFamilly</span> = <a name="typerig.core.objects.utils.fontFamilly" href="#typerig.core.objects.utils.fontFamilly">class fontFamilly</a></h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Font familly class:
*   generates weight stems [.wt_stems] and MM weight instances [.wt_instances]
        using given masters/layers wt0, wt1, and number of weight members [wt_steps].
        Uses geometric growth (progression) algorithm to determine stem weight

*   generates MM width instances [.wd_instances] using given number
        of width members [wd_steps]. Uses linear growth.

*   generates all MM isntaces/vectors for instance generation [.instances]
---
ex: fontFamilyName = fontFamilly(wt0 = 56, wt1 = 178, wt_steps = 7, wd_steps = 3)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fontFamilly-__init__" href="#fontFamilly-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="fontFamilly-update" href="#fontFamilly-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.utils.linAxis"></a>

## `linAxis`


<dt class="class"><h2><span class="class-name">typerig.core.objects.utils.linAxis</span> = <a name="typerig.core.objects.utils.linAxis" href="#typerig.core.objects.utils.linAxis">class linAxis</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A linear series axis instance and stem calculator

Usage linAxis(masterDict, instanceCount), where:
*       masterDict = {min_axis_value:min_stem_width, max_axis_value:max_stem_width} ex: {0:50, 1000:750}
*       instanceCount = number of instances to be calculated</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="linAxis-__init__" href="#linAxis-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, masterDict, instanceCount)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="linAxis-update" href="#linAxis-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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


<a name="typerig.core.objects.utils.geoAxis"></a>

## `geoAxis`


<dt class="class"><h2><span class="class-name">typerig.core.objects.utils.geoAxis</span> = <a name="typerig.core.objects.utils.geoAxis" href="#typerig.core.objects.utils.geoAxis">class geoAxis</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A geometric series axis instance and stem calculator

Usage linAxis(masterDict, instanceCount), where:
*   masterDict = {min_axis_value:min_stem_width, max_axis_value:max_stem_width} ex: {0:50, 1000:750}
*   instanceCount = number of instances to be calculated</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="geoAxis-__init__" href="#geoAxis-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, masterDict, instanceCount)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="geoAxis-update" href="#geoAxis-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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
