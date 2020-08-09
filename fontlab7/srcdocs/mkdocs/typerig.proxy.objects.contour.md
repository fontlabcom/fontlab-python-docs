

<a name="typerig.proxy.objects.contour"></a>

# `typerig.proxy.objects.contour`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.contour (<span class="info">version 0.26.1)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Contour (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2019-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontlab</li><li>math</li><li>PythonQt</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.contour.html#eContour">eContour</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eContour" href="#eContour">class <span class="class-name">eContour</span></a>(<a href="./typerig.proxy.objects.contour.html#pContour">pContour</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Contour, adding some advanced functionality.

Constructor:
        eContour(flContour)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.contour.html#eContour">eContour</a></dd><dd><a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eContour-alignTo" href="#eContour-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-asCoord" href="#eContour-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord <a href="./__builtin__.html#object">object</a> of the Bottom lest corner.</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-getNext" href="#eContour-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-getPrev" href="#eContour-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></h4><dl class="function"><dt><a name="eContour-__init__" href="#eContour-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, contour)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-__repr__" href="#eContour-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-draw" href="#eContour-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isAllSelected" href="#eContour-isAllSelected"><span class="function-name">isAllSelected</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Is the whole contour selected</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isCCW" href="#eContour-isCCW"><span class="function-name">isCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isCW" href="#eContour-isCW"><span class="function-name">isCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-reverse" href="#eContour-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-rotate" href="#eContour-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-scale" href="#eContour-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-setCCW" href="#eContour-setCCW"><span class="function-name">setCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-setCW" href="#eContour-setCW"><span class="function-name">setCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-slant" href="#eContour-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-translate" href="#eContour-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></h4><dl class="descriptor"><dt>__dict__</dt>
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
<dt class="class"><h2><a name="pContour" href="#pContour">class <span class="class-name">pContour</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flContour object

Constructor:
        pContour(flContour)

Attributes:
        .fl (flContour): Original flContour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pContour-__init__" href="#pContour-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, contour)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-__repr__" href="#pContour-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-draw" href="#pContour-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isAllSelected" href="#pContour-isAllSelected"><span class="function-name">isAllSelected</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Is the whole contour selected</pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isCCW" href="#pContour-isCCW"><span class="function-name">isCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isCW" href="#pContour-isCW"><span class="function-name">isCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-reverse" href="#pContour-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-rotate" href="#pContour-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-scale" href="#pContour-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-setCCW" href="#pContour-setCCW"><span class="function-name">setCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-setCW" href="#pContour-setCW"><span class="function-name">setCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-slant" href="#pContour-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-translate" href="#pContour-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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


<a name="typerig.proxy.objects.contour.pContour"></a>

## `pContour`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.contour.pContour</span> = <a name="typerig.proxy.objects.contour.pContour" href="#typerig.proxy.objects.contour.pContour">class pContour</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flContour object

Constructor:
        pContour(flContour)

Attributes:
        .fl (flContour): Original flContour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pContour-__init__" href="#pContour-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, contour)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-__repr__" href="#pContour-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-draw" href="#pContour-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isAllSelected" href="#pContour-isAllSelected"><span class="function-name">isAllSelected</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Is the whole contour selected</pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isCCW" href="#pContour-isCCW"><span class="function-name">isCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-isCW" href="#pContour-isCW"><span class="function-name">isCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-reverse" href="#pContour-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-rotate" href="#pContour-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-scale" href="#pContour-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-setCCW" href="#pContour-setCCW"><span class="function-name">setCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-setCW" href="#pContour-setCW"><span class="function-name">setCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-slant" href="#pContour-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pContour-translate" href="#pContour-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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


<a name="typerig.proxy.objects.contour.pContour.isAllSelected"></a>

### `isAllSelected`


<dl class="function"><dt><a name="-typerig.proxy.objects.contour.pContour.isAllSelected" href="#-typerig.proxy.objects.contour.pContour.isAllSelected"><span class="function-name">typerig.proxy.objects.contour.pContour.isAllSelected</span></a> = isAllSelected<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.contour.html#pContour">typerig.proxy.objects.contour.pContour</a> method</span></dt><dd>

<pre class="doc" markdown="0">Is the whole contour selected</pre>

</dd></dl>



<a name="typerig.proxy.objects.contour.pContour.draw"></a>

### `draw`


<dl class="function"><dt><a name="-typerig.proxy.objects.contour.pContour.draw" href="#-typerig.proxy.objects.contour.pContour.draw"><span class="function-name">typerig.proxy.objects.contour.pContour.draw</span></a> = draw<span class="argspec">(self, pen, transform<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.contour.html#pContour">typerig.proxy.objects.contour.pContour</a> method</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>



<a name="typerig.proxy.objects.contour.eContour"></a>

## `eContour`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.contour.eContour</span> = <a name="typerig.proxy.objects.contour.eContour" href="#typerig.proxy.objects.contour.eContour">class eContour</a>(<a href="./typerig.proxy.objects.contour.html#pContour">pContour</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Contour, adding some advanced functionality.

Constructor:
        eContour(flContour)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.contour.html#eContour">eContour</a></dd><dd><a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eContour-alignTo" href="#eContour-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-asCoord" href="#eContour-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the Bottom lest corner.</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-getNext" href="#eContour-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-getPrev" href="#eContour-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></h4><dl class="function"><dt><a name="eContour-__init__" href="#eContour-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, contour)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-__repr__" href="#eContour-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-draw" href="#eContour-draw"><span class="function-name">draw</span></a><span class="argspec">(self, pen, transform<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Utilizes the Pen protocol</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isAllSelected" href="#eContour-isAllSelected"><span class="function-name">isAllSelected</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Is the whole contour selected</pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isCCW" href="#eContour-isCCW"><span class="function-name">isCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-isCW" href="#eContour-isCW"><span class="function-name">isCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-reverse" href="#eContour-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-rotate" href="#eContour-rotate"><span class="function-name">rotate</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-scale" href="#eContour-scale"><span class="function-name">scale</span></a><span class="argspec">(self, sx, sy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-setCCW" href="#eContour-setCCW"><span class="function-name">setCCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-setCW" href="#eContour-setCW"><span class="function-name">setCW</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-slant" href="#eContour-slant"><span class="function-name">slant</span></a><span class="argspec">(self, deg)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eContour-translate" href="#eContour-translate"><span class="function-name">translate</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.contour.html#pContour">pContour</a></h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.proxy.objects.contour.eContour.asCoord"></a>

### `asCoord`


<dl class="function"><dt><a name="-typerig.proxy.objects.contour.eContour.asCoord" href="#-typerig.proxy.objects.contour.eContour.asCoord"><span class="function-name">typerig.proxy.objects.contour.eContour.asCoord</span></a> = asCoord<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.contour.html#eContour">typerig.proxy.objects.contour.eContour</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the Bottom lest corner.</pre>

</dd></dl>



<a name="typerig.proxy.objects.contour.eContour.alignTo"></a>

### `alignTo`


<dl class="function"><dt><a name="-typerig.proxy.objects.contour.eContour.alignTo" href="#-typerig.proxy.objects.contour.eContour.alignTo"><span class="function-name">typerig.proxy.objects.contour.eContour.alignTo</span></a> = alignTo<span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.contour.html#eContour">typerig.proxy.objects.contour.eContour</a> method</span></dt><dd>

<pre class="doc" markdown="0">Align current contour.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>

