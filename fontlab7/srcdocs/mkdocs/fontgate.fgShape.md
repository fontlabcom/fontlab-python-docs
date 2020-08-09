

<a name="fontgate.fgShape"></a>

# `fgShape`


<dt class="class"><h2><span class="class-name">fontgate.fgShape</span> = <a name="fontgate.fgShape" href="#fontgate.fgShape">class fgShape</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Shape representation

Constructors:
  fgShape() - default
  fgShape(fgShape) - copy
  fgShape(fgShape, fgShape, float tx, float ty)
  fgShape(fgShape, fgShape, float tx, float ty, int blend_mode)

Math Operations:
  fgShape + fgShape
  fgShape - fgShape
  fgShape * float</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fgShape-__add__" href="#fgShape-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__cmp__" href="#fgShape-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__delattr__" href="#fgShape-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__getattribute__" href="#fgShape-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__init__" href="#fgShape-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__mul__" href="#fgShape-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__radd__" href="#fgShape-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__repr__" href="#fgShape-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__rmul__" href="#fgShape-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__rsub__" href="#fgShape-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__setattr__" href="#fgShape-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-__sub__" href="#fgShape-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontgate.fgShape-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-addContour" href="#fgShape-addContour"><span class="function-name">addContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour <a href="#fontgate.fgShape-addContour">addContour</a>(fgContour)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-addShape" href="#fgShape-addShape"><span class="function-name">addShape</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-addShape">addShape</a>(fgShape, int mode) ???</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-applyTransform" href="#fgShape-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-applyTransform">applyTransform</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-area" href="#fgShape-area"><span class="function-name">area</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontgate.fgShape-area">area</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-assignStyle" href="#fgShape-assignStyle"><span class="function-name">assignStyle</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-assignStyle">assignStyle</a>(fgShape)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-autoInterpolated" href="#fgShape-autoInterpolated"><span class="function-name">autoInterpolated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgShape-autoInterpolated">autoInterpolated</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-autoSmooth" href="#fgShape-autoSmooth"><span class="function-name">autoSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgShape-autoSmooth">autoSmooth</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-boundingBox" href="#fgShape-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect/Nothing <a href="#fontgate.fgShape-boundingBox">boundingBox</a>(fgMatrix[, bool prepareExport=false])</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-checkContours" href="#fgShape-checkContours"><span class="function-name">checkContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-checkContours">checkContours</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-containsOffPoint" href="#fgShape-containsOffPoint"><span class="function-name">containsOffPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgShape-containsOffPoint">containsOffPoint</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-countContours" href="#fgShape-countContours"><span class="function-name">countContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-countContours">countContours</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-countNodes" href="#fgShape-countNodes"><span class="function-name">countNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-countNodes">countNodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-excludeShape" href="#fgShape-excludeShape"><span class="function-name">excludeShape</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-excludeShape">excludeShape</a>(fgShape, int mode) ???</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-hasBody" href="#fgShape-hasBody"><span class="function-name">hasBody</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgShape-hasBody">hasBody</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-hasContours" href="#fgShape-hasContours"><span class="function-name">hasContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontgate.fgShape-hasContours">hasContours</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-isCompatible" href="#fgShape-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool/Nothing <a href="#fontgate.fgShape-isCompatible">isCompatible</a>(fgShape)</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-removeOverlap" href="#fgShape-removeOverlap"><span class="function-name">removeOverlap</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-removeOverlap">removeOverlap</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-reverse" href="#fgShape-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-reverse">reverse</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-sortContours" href="#fgShape-sortContours"><span class="function-name">sortContours</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-sortContours">sortContours</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-subtractShape" href="#fgShape-subtractShape"><span class="function-name">subtractShape</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontgate.fgShape-subtractShape">subtractShape</a>(fgShape, int mode) ???</pre>

</dd></dl>
<dl class="function"><dt><a name="fgShape-transform" href="#fgShape-transform"><span class="function-name">transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontgate.fgShape-transform">transform</a>(fgMatrix)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>angle</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>body</dt>
<dd>

<pre class="doc" markdown="0">(fgBrush)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>calligraphic</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>cap_type</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>contours</dt>
<dd>

<pre class="doc" markdown="0">(fgContours)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>join_type</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>matrix</dt>
<dd>

<pre class="doc" markdown="0">(fgMatrix)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">(string)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>opacity</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>pen</dt>
<dd>

<pre class="doc" markdown="0">(fgBrush)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>picture</dt>
<dd>

<pre class="doc" markdown="0">(fgBitmap)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>width</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontgate.fgShape-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontgate.fgShape.addContour"></a>

## `addContour`


<dl class="function"><dt><a name="-fontgate.fgShape.addContour" href="#-fontgate.fgShape.addContour"><span class="function-name">fontgate.fgShape.addContour</span></a> = addContour<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour addContour(fgContour)</pre>

</dd></dl>



<a name="fontgate.fgShape.addShape"></a>

## `addShape`


<dl class="function"><dt><a name="-fontgate.fgShape.addShape" href="#-fontgate.fgShape.addShape"><span class="function-name">fontgate.fgShape.addShape</span></a> = addShape<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int addShape(fgShape, int mode) ???</pre>

</dd></dl>



<a name="fontgate.fgShape.angle"></a>

## `angle`


<dl class="descriptor"><dt>fontgate.fgShape.angle</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.applyTransform"></a>

## `applyTransform`


<dl class="function"><dt><a name="-fontgate.fgShape.applyTransform" href="#-fontgate.fgShape.applyTransform"><span class="function-name">fontgate.fgShape.applyTransform</span></a> = applyTransform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">applyTransform()</pre>

</dd></dl>



<a name="fontgate.fgShape.area"></a>

## `area`


<dl class="function"><dt><a name="-fontgate.fgShape.area" href="#-fontgate.fgShape.area"><span class="function-name">fontgate.fgShape.area</span></a> = area<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float area()</pre>

</dd></dl>



<a name="fontgate.fgShape.assignStyle"></a>

## `assignStyle`


<dl class="function"><dt><a name="-fontgate.fgShape.assignStyle" href="#-fontgate.fgShape.assignStyle"><span class="function-name">fontgate.fgShape.assignStyle</span></a> = assignStyle<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assignStyle(fgShape)</pre>

</dd></dl>



<a name="fontgate.fgShape.autoInterpolated"></a>

## `autoInterpolated`


<dl class="function"><dt><a name="-fontgate.fgShape.autoInterpolated" href="#-fontgate.fgShape.autoInterpolated"><span class="function-name">fontgate.fgShape.autoInterpolated</span></a> = autoInterpolated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool autoInterpolated()</pre>

</dd></dl>



<a name="fontgate.fgShape.autoSmooth"></a>

## `autoSmooth`


<dl class="function"><dt><a name="-fontgate.fgShape.autoSmooth" href="#-fontgate.fgShape.autoSmooth"><span class="function-name">fontgate.fgShape.autoSmooth</span></a> = autoSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool autoSmooth()</pre>

</dd></dl>



<a name="fontgate.fgShape.body"></a>

## `body`


<dl class="descriptor"><dt>fontgate.fgShape.body</dt>
<dd>

<pre class="doc" markdown="0">(fgBrush)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontgate.fgShape.boundingBox" href="#-fontgate.fgShape.boundingBox"><span class="function-name">fontgate.fgShape.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgRect/Nothing boundingBox(fgMatrix[, bool prepareExport=false])</pre>

</dd></dl>



<a name="fontgate.fgShape.calligraphic"></a>

## `calligraphic`


<dl class="descriptor"><dt>fontgate.fgShape.calligraphic</dt>
<dd>

<pre class="doc" markdown="0">(bool)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.cap_type"></a>

## `cap_type`


<dl class="descriptor"><dt>fontgate.fgShape.cap_type</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.checkContours"></a>

## `checkContours`


<dl class="function"><dt><a name="-fontgate.fgShape.checkContours" href="#-fontgate.fgShape.checkContours"><span class="function-name">fontgate.fgShape.checkContours</span></a> = checkContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkContours()</pre>

</dd></dl>



<a name="fontgate.fgShape.containsOffPoint"></a>

## `containsOffPoint`


<dl class="function"><dt><a name="-fontgate.fgShape.containsOffPoint" href="#-fontgate.fgShape.containsOffPoint"><span class="function-name">fontgate.fgShape.containsOffPoint</span></a> = containsOffPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool containsOffPoint()</pre>

</dd></dl>



<a name="fontgate.fgShape.contours"></a>

## `contours`


<dl class="descriptor"><dt>fontgate.fgShape.contours</dt>
<dd>

<pre class="doc" markdown="0">(fgContours)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.countContours"></a>

## `countContours`


<dl class="function"><dt><a name="-fontgate.fgShape.countContours" href="#-fontgate.fgShape.countContours"><span class="function-name">fontgate.fgShape.countContours</span></a> = countContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countContours()</pre>

</dd></dl>



<a name="fontgate.fgShape.countNodes"></a>

## `countNodes`


<dl class="function"><dt><a name="-fontgate.fgShape.countNodes" href="#-fontgate.fgShape.countNodes"><span class="function-name">fontgate.fgShape.countNodes</span></a> = countNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int countNodes()</pre>

</dd></dl>



<a name="fontgate.fgShape.excludeShape"></a>

## `excludeShape`


<dl class="function"><dt><a name="-fontgate.fgShape.excludeShape" href="#-fontgate.fgShape.excludeShape"><span class="function-name">fontgate.fgShape.excludeShape</span></a> = excludeShape<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int excludeShape(fgShape, int mode) ???</pre>

</dd></dl>



<a name="fontgate.fgShape.hasBody"></a>

## `hasBody`


<dl class="function"><dt><a name="-fontgate.fgShape.hasBody" href="#-fontgate.fgShape.hasBody"><span class="function-name">fontgate.fgShape.hasBody</span></a> = hasBody<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasBody()</pre>

</dd></dl>



<a name="fontgate.fgShape.hasContours"></a>

## `hasContours`


<dl class="function"><dt><a name="-fontgate.fgShape.hasContours" href="#-fontgate.fgShape.hasContours"><span class="function-name">fontgate.fgShape.hasContours</span></a> = hasContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasContours()</pre>

</dd></dl>



<a name="fontgate.fgShape.isCompatible"></a>

## `isCompatible`


<dl class="function"><dt><a name="-fontgate.fgShape.isCompatible" href="#-fontgate.fgShape.isCompatible"><span class="function-name">fontgate.fgShape.isCompatible</span></a> = isCompatible<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool/Nothing isCompatible(fgShape)</pre>

</dd></dl>



<a name="fontgate.fgShape.join_type"></a>

## `join_type`


<dl class="descriptor"><dt>fontgate.fgShape.join_type</dt>
<dd>

<pre class="doc" markdown="0">(int)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.matrix"></a>

## `matrix`


<dl class="descriptor"><dt>fontgate.fgShape.matrix</dt>
<dd>

<pre class="doc" markdown="0">(fgMatrix)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.name"></a>

## `name`


<dl class="descriptor"><dt>fontgate.fgShape.name</dt>
<dd>

<pre class="doc" markdown="0">(string)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.opacity"></a>

## `opacity`


<dl class="descriptor"><dt>fontgate.fgShape.opacity</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.pen"></a>

## `pen`


<dl class="descriptor"><dt>fontgate.fgShape.pen</dt>
<dd>

<pre class="doc" markdown="0">(fgBrush)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.picture"></a>

## `picture`


<dl class="descriptor"><dt>fontgate.fgShape.picture</dt>
<dd>

<pre class="doc" markdown="0">(fgBitmap)</pre>

</dd>
</dl>



<a name="fontgate.fgShape.removeOverlap"></a>

## `removeOverlap`


<dl class="function"><dt><a name="-fontgate.fgShape.removeOverlap" href="#-fontgate.fgShape.removeOverlap"><span class="function-name">fontgate.fgShape.removeOverlap</span></a> = removeOverlap<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int removeOverlap()</pre>

</dd></dl>



<a name="fontgate.fgShape.reverse"></a>

## `reverse`


<dl class="function"><dt><a name="-fontgate.fgShape.reverse" href="#-fontgate.fgShape.reverse"><span class="function-name">fontgate.fgShape.reverse</span></a> = reverse<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">reverse()</pre>

</dd></dl>



<a name="fontgate.fgShape.sortContours"></a>

## `sortContours`


<dl class="function"><dt><a name="-fontgate.fgShape.sortContours" href="#-fontgate.fgShape.sortContours"><span class="function-name">fontgate.fgShape.sortContours</span></a> = sortContours<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">sortContours()</pre>

</dd></dl>



<a name="fontgate.fgShape.subtractShape"></a>

## `subtractShape`


<dl class="function"><dt><a name="-fontgate.fgShape.subtractShape" href="#-fontgate.fgShape.subtractShape"><span class="function-name">fontgate.fgShape.subtractShape</span></a> = subtractShape<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int subtractShape(fgShape, int mode) ???</pre>

</dd></dl>



<a name="fontgate.fgShape.transform"></a>

## `transform`


<dl class="function"><dt><a name="-fontgate.fgShape.transform" href="#-fontgate.fgShape.transform"><span class="function-name">fontgate.fgShape.transform</span></a> = transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transform(fgMatrix)</pre>

</dd></dl>



<a name="fontgate.fgShape.width"></a>

## `width`


<dl class="descriptor"><dt>fontgate.fgShape.width</dt>
<dd>

<pre class="doc" markdown="0">(float)</pre>

</dd>
</dl>

