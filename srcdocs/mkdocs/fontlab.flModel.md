

<a name="fontlab.flModel"></a>

# `flModel`


<dt class="class"><h2><span class="class-name">fontlab.flModel</span> = <a name="fontlab.flModel" href="#fontlab.flModel">class flModel</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flModel representation

Constructors:
None, static only methods</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flModel-__delattr__" href="#flModel-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flModel-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-__getattribute__" href="#flModel-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flModel-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-__init__" href="#flModel-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flModel-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-__repr__" href="#flModel-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flModel-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-__setattr__" href="#flModel-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flModel-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flModel-createObject" href="#flModel-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flModel-createObject">createObject</a>(int type)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-getClassMask" href="#flModel-getClassMask"><span class="function-name">getClassMask</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int  <a href="#fontlab.flModel-getClassMask">getClassMask</a>(int type)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-instance" href="#flModel-instance"><span class="function-name">instance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flModel <a href="#fontlab.flModel-instance">instance</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-isClassMask" href="#flModel-isClassMask"><span class="function-name">isClassMask</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flModel-isClassMask">isClassMask</a>(int type)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-notifyGlyphChanged" href="#flModel-notifyGlyphChanged"><span class="function-name">notifyGlyphChanged</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flModel-notifyGlyphChanged">notifyGlyphChanged</a>(unsigned long fg_glyphId)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-notifyGlyphUpdate" href="#flModel-notifyGlyphUpdate"><span class="function-name">notifyGlyphUpdate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flModel-notifyGlyphUpdate">notifyGlyphUpdate</a>(unsigned long fg_glyphId)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-notifyGlyphsChanged" href="#flModel-notifyGlyphsChanged"><span class="function-name">notifyGlyphsChanged</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flModel-notifyGlyphsChanged">notifyGlyphsChanged</a>(QSet<uint32_t> glyphs)</pre>

</dd></dl>
<dl class="function"><dt><a name="flModel-typeToStr" href="#flModel-typeToStr"><span class="function-name">typeToStr</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString <a href="#fontlab.flModel-typeToStr">typeToStr</a>(int type | flObject)</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">ModelType</span> = {'Anchor': 185, 'AnchorNode': 186, 'AnchorNodeToGuidelineCoords': 187, 'AutoShape': 55, 'Bezier': 48, 'Container': 8, 'Contour': 47, 'ContourInfo': 181, 'Controls': 14, 'Edge': 101, ...}</dt></dl>
<dl><dt><span class="other-name">ObjectParameter</span> = {'prmBrush': 2, 'prmPen': 3, 'prmStructure': 0, 'prmTransform': 1}</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flModel-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.flModel.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flModel.createObject" href="#-fontlab.flModel.createObject"><span class="function-name">fontlab.flModel.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int type)</pre>

</dd></dl>



<a name="fontlab.flModel.getClassMask"></a>

## `getClassMask`


<dl class="function"><dt><a name="-fontlab.flModel.getClassMask" href="#-fontlab.flModel.getClassMask"><span class="function-name">fontlab.flModel.getClassMask</span></a> = getClassMask<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int  getClassMask(int type)</pre>

</dd></dl>



<a name="fontlab.flModel.instance"></a>

## `instance`


<dl class="function"><dt><a name="-fontlab.flModel.instance" href="#-fontlab.flModel.instance"><span class="function-name">fontlab.flModel.instance</span></a> = instance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flModel instance()</pre>

</dd></dl>



<a name="fontlab.flModel.isClassMask"></a>

## `isClassMask`


<dl class="function"><dt><a name="-fontlab.flModel.isClassMask" href="#-fontlab.flModel.isClassMask"><span class="function-name">fontlab.flModel.isClassMask</span></a> = isClassMask<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isClassMask(int type)</pre>

</dd></dl>



<a name="fontlab.flModel.ModelType"></a>

## `ModelType`


<span class="other-name">fontlab.flModel.ModelType</span> = {'Anchor': 185, 'AnchorNode': 186, 'AnchorNodeToGuidelineCoords': 187, 'AutoShape': 55, 'Bezier': 48, 'Container': 8, 'Contour': 47, 'ContourInfo': 181, 'Controls': 14, 'Edge': 101, ...}


<a name="fontlab.flModel.notifyGlyphChanged"></a>

## `notifyGlyphChanged`


<dl class="function"><dt><a name="-fontlab.flModel.notifyGlyphChanged" href="#-fontlab.flModel.notifyGlyphChanged"><span class="function-name">fontlab.flModel.notifyGlyphChanged</span></a> = notifyGlyphChanged<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">notifyGlyphChanged(unsigned long fg_glyphId)</pre>

</dd></dl>



<a name="fontlab.flModel.notifyGlyphsChanged"></a>

## `notifyGlyphsChanged`


<dl class="function"><dt><a name="-fontlab.flModel.notifyGlyphsChanged" href="#-fontlab.flModel.notifyGlyphsChanged"><span class="function-name">fontlab.flModel.notifyGlyphsChanged</span></a> = notifyGlyphsChanged<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">notifyGlyphsChanged(QSet<uint32_t> glyphs)</pre>

</dd></dl>



<a name="fontlab.flModel.notifyGlyphUpdate"></a>

## `notifyGlyphUpdate`


<dl class="function"><dt><a name="-fontlab.flModel.notifyGlyphUpdate" href="#-fontlab.flModel.notifyGlyphUpdate"><span class="function-name">fontlab.flModel.notifyGlyphUpdate</span></a> = notifyGlyphUpdate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">notifyGlyphUpdate(unsigned long fg_glyphId)</pre>

</dd></dl>



<a name="fontlab.flModel.ObjectParameter"></a>

## `ObjectParameter`


<span class="other-name">fontlab.flModel.ObjectParameter</span> = {'prmBrush': 2, 'prmPen': 3, 'prmStructure': 0, 'prmTransform': 1}


<a name="fontlab.flModel.typeToStr"></a>

## `typeToStr`


<dl class="function"><dt><a name="-fontlab.flModel.typeToStr" href="#-fontlab.flModel.typeToStr"><span class="function-name">fontlab.flModel.typeToStr</span></a> = typeToStr<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString typeToStr(int type | flObject)</pre>

</dd></dl>

