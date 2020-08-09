

<a name="fontlab.flGlyph"></a>

# `flGlyph`


<dt class="class"><h2><span class="class-name">fontlab.flGlyph</span> = <a name="fontlab.flGlyph" href="#fontlab.flGlyph">class flGlyph</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flGlyph representation

Constructors:
  flGlyph()
  flGlyph(flGlyph)
  flGlyph(flObject)
  flGlyph(fgGlyph, fgFont)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flGlyph-__delattr__" href="#flGlyph-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__eq__" href="#flGlyph-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__ge__" href="#flGlyph-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__getattribute__" href="#flGlyph-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__gt__" href="#flGlyph-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__init__" href="#flGlyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flGlyph-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__le__" href="#flGlyph-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__lt__" href="#flGlyph-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__ne__" href="#flGlyph-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__repr__" href="#flGlyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-__setattr__" href="#flGlyph-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flGlyph-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-addLayer" href="#flGlyph-addLayer"><span class="function-name">addLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-addLayer">addLayer</a>(flLayer[, bool back = false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-addLayers" href="#flGlyph-addLayers"><span class="function-name">addLayers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-addLayers">addLayers</a>(list(flLayer))</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-applyTransform" href="#flGlyph-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-applyTransform">applyTransform</a>([QTransform transform])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-assignFontGateData" href="#flGlyph-assignFontGateData"><span class="function-name">assignFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-assignFontGateData">assignFontGateData</a>(fgFontGateData, bool doGuide = true, bool doHints = true, bool doAnchors = true)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-bindDependencies" href="#flGlyph-bindDependencies"><span class="function-name">bindDependencies</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-bindDependencies">bindDependencies</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-changed" href="#flGlyph-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-checkInitHistoryState" href="#flGlyph-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-clearAboveHistory" href="#flGlyph-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-clearFlag" href="#flGlyph-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-clearFlags" href="#flGlyph-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-clone" href="#flGlyph-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-createHistoryState" href="#flGlyph-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-currentHistoryState" href="#flGlyph-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-deactivateAll" href="#flGlyph-deactivateAll"><span class="function-name">deactivateAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-deactivateAll">deactivateAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-ensureMaskLayer" href="#flGlyph-ensureMaskLayer"><span class="function-name">ensureMaskLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer <a href="#fontlab.flGlyph-ensureMaskLayer">ensureMaskLayer</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-fillFgData" href="#flGlyph-fillFgData"><span class="function-name">fillFgData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontlab.flGlyph-fillFgData">fillFgData</a>(bool doGuides, bool doHints)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-findLayer" href="#flGlyph-findLayer"><span class="function-name">findLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer <a href="#fontlab.flGlyph-findLayer">findLayer</a>(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-findLayerCreate" href="#flGlyph-findLayerCreate"><span class="function-name">findLayerCreate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer <a href="#fontlab.flGlyph-findLayerCreate">findLayerCreate</a>(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-findVerticalGuideline" href="#flGlyph-findVerticalGuideline"><span class="function-name">findVerticalGuideline</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double/Nothing <a href="#fontlab.flGlyph-findVerticalGuideline">findVerticalGuideline</a>(QString)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-flag" href="#flGlyph-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getAuditInfo" href="#flGlyph-getAuditInfo"><span class="function-name">getAuditInfo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flAuditInfo) <a href="#fontlab.flGlyph-getAuditInfo">getAuditInfo</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getFastFontGateData" href="#flGlyph-getFastFontGateData"><span class="function-name">getFastFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontlab.flGlyph-getFastFontGateData">getFastFontGateData</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getLSB" href="#flGlyph-getLSB"><span class="function-name">getLSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flGlyph-getLSB">getLSB</a>(QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getLayerByName" href="#flGlyph-getLayerByName"><span class="function-name">getLayerByName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer <a href="#fontlab.flGlyph-getLayerByName">getLayerByName</a>(QString[, bool create =false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getProperties" href="#flGlyph-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getProperty" href="#flGlyph-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getPropertyFloat" href="#flGlyph-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getPropertyInt" href="#flGlyph-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getRSB" href="#flGlyph-getRSB"><span class="function-name">getRSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flGlyph-getRSB">getRSB</a>(QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-getSB" href="#flGlyph-getSB"><span class="function-name">getSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(double l, double r) <a href="#fontlab.flGlyph-getSB">getSB</a>(QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-glyphName" href="#flGlyph-glyphName"><span class="function-name">glyphName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString <a href="#fontlab.flGlyph-glyphName">glyphName</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-hasFontAudit" href="#flGlyph-hasFontAudit"><span class="function-name">hasFontAudit</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-hasFontAudit">hasFontAudit</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-hasHistoryState" href="#flGlyph-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-haveSelected" href="#flGlyph-haveSelected"><span class="function-name">haveSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-haveSelected">haveSelected</a>(SelectionMode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-historyStates" href="#flGlyph-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-horzReflection" href="#flGlyph-horzReflection"><span class="function-name">horzReflection</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-horzReflection">horzReflection</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-independedAll" href="#flGlyph-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-initialHistoryState" href="#flGlyph-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-inkBox" href="#flGlyph-inkBox"><span class="function-name">inkBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flGlyph-inkBox">inkBox</a>([QTransform tx = QTransform()])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-isEqual" href="#flGlyph-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-isUnbindedDependecies" href="#flGlyph-isUnbindedDependecies"><span class="function-name">isUnbindedDependecies</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-isUnbindedDependecies">isUnbindedDependecies</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-issele" href="#flGlyph-issele"><span class="function-name">issele</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-issele">issele</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-measurementLine" href="#flGlyph-measurementLine"><span class="function-name">measurementLine</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double/Nothing <a href="#fontlab.flGlyph-measurementLine">measurementLine</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-prepareTransformationData" href="#flGlyph-prepareTransformationData"><span class="function-name">prepareTransformationData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-prepareTransformationData">prepareTransformationData</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-release" href="#flGlyph-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-remove" href="#flGlyph-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-removeChild" href="#flGlyph-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-removeEmptyShapes" href="#flGlyph-removeEmptyShapes"><span class="function-name">removeEmptyShapes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-removeEmptyShapes">removeEmptyShapes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-removeLayer" href="#flGlyph-removeLayer"><span class="function-name">removeLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-removeLayer">removeLayer</a>(flLayer)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-removeProperty" href="#flGlyph-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-resetInkBox" href="#flGlyph-resetInkBox"><span class="function-name">resetInkBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-resetInkBox">resetInkBox</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-resetTransformationData" href="#flGlyph-resetTransformationData"><span class="function-name">resetTransformationData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-resetTransformationData">resetTransformationData</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-restoreHistoryState" href="#flGlyph-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setAllShapesSelected" href="#flGlyph-setAllShapesSelected"><span class="function-name">setAllShapesSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setAllShapesSelected">setAllShapesSelected</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setFlag" href="#flGlyph-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setLSB" href="#flGlyph-setLSB"><span class="function-name">setLSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-setLSB">setLSB</a>(double v, bool move_guidelines, QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setLayers" href="#flGlyph-setLayers"><span class="function-name">setLayers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-setLayers">setLayers</a>(list(flLayer))</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setProperty" href="#flGlyph-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setPropertyFloat" href="#flGlyph-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setPropertyInt" href="#flGlyph-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setRSB" href="#flGlyph-setRSB"><span class="function-name">setRSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-setRSB">setRSB</a>(double v, QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setReflected" href="#flGlyph-setReflected"><span class="function-name">setReflected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-setReflected">setReflected</a>(bool, bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-setSB" href="#flGlyph-setSB"><span class="function-name">setSB</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-setSB">setSB</a>(double l, double r, bool move_guidelines, bool all_layers, QTransform tr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-tag" href="#flGlyph-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-unselectAllNodes" href="#flGlyph-unselectAllNodes"><span class="function-name">unselectAllNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-unselectAllNodes">unselectAllNodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-update" href="#flGlyph-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-update">update</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-updateActiveLayer" href="#flGlyph-updateActiveLayer"><span class="function-name">updateActiveLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer <a href="#fontlab.flGlyph-updateActiveLayer">updateActiveLayer</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-updateAudit" href="#flGlyph-updateAudit"><span class="function-name">updateAudit</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flGlyph-updateAudit">updateAudit</a>(list(int))</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-updateSidebearings" href="#flGlyph-updateSidebearings"><span class="function-name">updateSidebearings</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-updateSidebearings">updateSidebearings</a>(bool nofify)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-vertReflection" href="#flGlyph-vertReflection"><span class="function-name">vertReflection</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-vertReflection">vertReflection</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-virtualTags" href="#flGlyph-virtualTags"><span class="function-name">virtualTags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QSet<QString>/Nothing <a href="#fontlab.flGlyph-virtualTags">virtualTags</a>()</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flGlyph-clearUpdateFgGlyphs" href="#flGlyph-clearUpdateFgGlyphs"><span class="function-name">clearUpdateFgGlyphs</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-clearUpdateFgGlyphs">clearUpdateFgGlyphs</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-cloneObject" href="#flGlyph-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flGlyph-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-createInstance" href="#flGlyph-createInstance"><span class="function-name">createInstance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flGlyph-createInstance">createInstance</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-createObject" href="#flGlyph-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flGlyph-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-ensureFgData" href="#flGlyph-ensureFgData"><span class="function-name">ensureFgData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData <a href="#fontlab.flGlyph-ensureFgData">ensureFgData</a>(fgGlyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-hasInstance" href="#flGlyph-hasInstance"><span class="function-name">hasInstance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-hasInstance">hasInstance</a>(fgGlyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-haveObject" href="#flGlyph-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-instanceType" href="#flGlyph-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flGlyph-instanceType">instanceType</a>();</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-linkInstances" href="#flGlyph-linkInstances"><span class="function-name">linkInstances</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flGlyph-linkInstances">linkInstances</a>(flGlyph, fgGlyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-updateFgGlyph" href="#flGlyph-updateFgGlyph"><span class="function-name">updateFgGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flGlyph-updateFgGlyph">updateFgGlyph</a>(uint id)</pre>

</dd></dl>
<dl class="function"><dt><a name="flGlyph-updatedFgGlyphs" href="#flGlyph-updatedFgGlyphs"><span class="function-name">updatedFgGlyphs</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(uint32_t) <a href="#fontlab.flGlyph-updatedFgGlyphs">updatedFgGlyphs</a>()</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>activeLayer</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>advanceWidth</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ascender</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>bodyLayer</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>bodyRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>boundingBox</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>descender</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fgGlyph</dt>
<dd>

<pre class="doc" markdown="0">fgGlyph</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fgGlyphId</dt>
<dd>

<pre class="doc" markdown="0">FgTypeId</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fgPackage</dt>
<dd>

<pre class="doc" markdown="0">fgFont</pre>

</dd>
</dl>
<dl class="descriptor"><dt>getStateObject</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>
<dl class="descriptor"><dt>glyphRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasBody</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>lastModified</dt>
<dd>

<pre class="doc" markdown="0">QDateTime</pre>

</dd>
</dl>
<dl class="descriptor"><dt>layers</dt>
<dd>

<pre class="doc" markdown="0">list(flLayer)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>leftMetric</dt>
<dd>

<pre class="doc" markdown="0">QPointF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>mark</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>metricsLeft</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>metricsRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>metricsRight</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>metricsWidth</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>nodesCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>note</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>
<dl class="descriptor"><dt>package</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>rightMetric</dt>
<dd>

<pre class="doc" markdown="0">QPointF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tags</dt>
<dd>

<pre class="doc" markdown="0">QStringList</pre>

</dd>
</dl>
<dl class="descriptor"><dt>type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flGlyph-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flGlyph.activeLayer"></a>

## `activeLayer`


<dl class="descriptor"><dt>fontlab.flGlyph.activeLayer</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.addLayer"></a>

## `addLayer`


<dl class="function"><dt><a name="-fontlab.flGlyph.addLayer" href="#-fontlab.flGlyph.addLayer"><span class="function-name">fontlab.flGlyph.addLayer</span></a> = addLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void addLayer(flLayer[, bool back = false])</pre>

</dd></dl>



<a name="fontlab.flGlyph.addLayers"></a>

## `addLayers`


<dl class="function"><dt><a name="-fontlab.flGlyph.addLayers" href="#-fontlab.flGlyph.addLayers"><span class="function-name">fontlab.flGlyph.addLayers</span></a> = addLayers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void addLayers(list(flLayer))</pre>

</dd></dl>



<a name="fontlab.flGlyph.advanceWidth"></a>

## `advanceWidth`


<dl class="descriptor"><dt>fontlab.flGlyph.advanceWidth</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.applyTransform"></a>

## `applyTransform`


<dl class="function"><dt><a name="-fontlab.flGlyph.applyTransform" href="#-fontlab.flGlyph.applyTransform"><span class="function-name">fontlab.flGlyph.applyTransform</span></a> = applyTransform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">applyTransform([QTransform transform])</pre>

</dd></dl>



<a name="fontlab.flGlyph.ascender"></a>

## `ascender`


<dl class="descriptor"><dt>fontlab.flGlyph.ascender</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.assignFontGateData"></a>

## `assignFontGateData`


<dl class="function"><dt><a name="-fontlab.flGlyph.assignFontGateData" href="#-fontlab.flGlyph.assignFontGateData"><span class="function-name">fontlab.flGlyph.assignFontGateData</span></a> = assignFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void assignFontGateData(fgFontGateData, bool doGuide = true, bool doHints = true, bool doAnchors = true)</pre>

</dd></dl>



<a name="fontlab.flGlyph.bindDependencies"></a>

## `bindDependencies`


<dl class="function"><dt><a name="-fontlab.flGlyph.bindDependencies" href="#-fontlab.flGlyph.bindDependencies"><span class="function-name">fontlab.flGlyph.bindDependencies</span></a> = bindDependencies<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bindDependencies()</pre>

</dd></dl>



<a name="fontlab.flGlyph.bodyLayer"></a>

## `bodyLayer`


<dl class="descriptor"><dt>fontlab.flGlyph.bodyLayer</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.bodyRect"></a>

## `bodyRect`


<dl class="descriptor"><dt>fontlab.flGlyph.bodyRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.boundingBox"></a>

## `boundingBox`


<dl class="descriptor"><dt>fontlab.flGlyph.boundingBox</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flGlyph.changed" href="#-fontlab.flGlyph.changed"><span class="function-name">fontlab.flGlyph.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flGlyph.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.checkInitHistoryState" href="#-fontlab.flGlyph.checkInitHistoryState"><span class="function-name">fontlab.flGlyph.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flGlyph.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flGlyph.clearAboveHistory" href="#-fontlab.flGlyph.clearAboveHistory"><span class="function-name">fontlab.flGlyph.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flGlyph.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flGlyph.clearFlag" href="#-fontlab.flGlyph.clearFlag"><span class="function-name">fontlab.flGlyph.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flGlyph.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flGlyph.clearFlags" href="#-fontlab.flGlyph.clearFlags"><span class="function-name">fontlab.flGlyph.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flGlyph.clearUpdateFgGlyphs"></a>

## `clearUpdateFgGlyphs`


<dl class="function"><dt><a name="-fontlab.flGlyph.clearUpdateFgGlyphs" href="#-fontlab.flGlyph.clearUpdateFgGlyphs"><span class="function-name">fontlab.flGlyph.clearUpdateFgGlyphs</span></a> = clearUpdateFgGlyphs<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearUpdateFgGlyphs()</pre>

</dd></dl>



<a name="fontlab.flGlyph.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flGlyph.clone" href="#-fontlab.flGlyph.clone"><span class="function-name">fontlab.flGlyph.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flGlyph.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flGlyph.cloneObject" href="#-fontlab.flGlyph.cloneObject"><span class="function-name">fontlab.flGlyph.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flGlyph.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.createHistoryState" href="#-fontlab.flGlyph.createHistoryState"><span class="function-name">fontlab.flGlyph.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flGlyph.createInstance"></a>

## `createInstance`


<dl class="function"><dt><a name="-fontlab.flGlyph.createInstance" href="#-fontlab.flGlyph.createInstance"><span class="function-name">fontlab.flGlyph.createInstance</span></a> = createInstance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph createInstance()</pre>

</dd></dl>



<a name="fontlab.flGlyph.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flGlyph.createObject" href="#-fontlab.flGlyph.createObject"><span class="function-name">fontlab.flGlyph.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flGlyph.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.currentHistoryState" href="#-fontlab.flGlyph.currentHistoryState"><span class="function-name">fontlab.flGlyph.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flGlyph.deactivateAll"></a>

## `deactivateAll`


<dl class="function"><dt><a name="-fontlab.flGlyph.deactivateAll" href="#-fontlab.flGlyph.deactivateAll"><span class="function-name">fontlab.flGlyph.deactivateAll</span></a> = deactivateAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">deactivateAll()</pre>

</dd></dl>



<a name="fontlab.flGlyph.descender"></a>

## `descender`


<dl class="descriptor"><dt>fontlab.flGlyph.descender</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.ensureFgData"></a>

## `ensureFgData`


<dl class="function"><dt><a name="-fontlab.flGlyph.ensureFgData" href="#-fontlab.flGlyph.ensureFgData"><span class="function-name">fontlab.flGlyph.ensureFgData</span></a> = ensureFgData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData ensureFgData(fgGlyph)</pre>

</dd></dl>



<a name="fontlab.flGlyph.ensureMaskLayer"></a>

## `ensureMaskLayer`


<dl class="function"><dt><a name="-fontlab.flGlyph.ensureMaskLayer" href="#-fontlab.flGlyph.ensureMaskLayer"><span class="function-name">fontlab.flGlyph.ensureMaskLayer</span></a> = ensureMaskLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer ensureMaskLayer()</pre>

</dd></dl>



<a name="fontlab.flGlyph.fgGlyph"></a>

## `fgGlyph`


<dl class="descriptor"><dt>fontlab.flGlyph.fgGlyph</dt>
<dd>

<pre class="doc" markdown="0">fgGlyph</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.fgGlyphId"></a>

## `fgGlyphId`


<dl class="descriptor"><dt>fontlab.flGlyph.fgGlyphId</dt>
<dd>

<pre class="doc" markdown="0">FgTypeId</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.fgPackage"></a>

## `fgPackage`


<dl class="descriptor"><dt>fontlab.flGlyph.fgPackage</dt>
<dd>

<pre class="doc" markdown="0">fgFont</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.fillFgData"></a>

## `fillFgData`


<dl class="function"><dt><a name="-fontlab.flGlyph.fillFgData" href="#-fontlab.flGlyph.fillFgData"><span class="function-name">fontlab.flGlyph.fillFgData</span></a> = fillFgData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData fillFgData(bool doGuides, bool doHints)</pre>

</dd></dl>



<a name="fontlab.flGlyph.findLayer"></a>

## `findLayer`


<dl class="function"><dt><a name="-fontlab.flGlyph.findLayer" href="#-fontlab.flGlyph.findLayer"><span class="function-name">fontlab.flGlyph.findLayer</span></a> = findLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer findLayer(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>



<a name="fontlab.flGlyph.findLayerCreate"></a>

## `findLayerCreate`


<dl class="function"><dt><a name="-fontlab.flGlyph.findLayerCreate" href="#-fontlab.flGlyph.findLayerCreate"><span class="function-name">fontlab.flGlyph.findLayerCreate</span></a> = findLayerCreate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer findLayerCreate(QString name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>



<a name="fontlab.flGlyph.findVerticalGuideline"></a>

## `findVerticalGuideline`


<dl class="function"><dt><a name="-fontlab.flGlyph.findVerticalGuideline" href="#-fontlab.flGlyph.findVerticalGuideline"><span class="function-name">fontlab.flGlyph.findVerticalGuideline</span></a> = findVerticalGuideline<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double/Nothing findVerticalGuideline(QString)</pre>

</dd></dl>



<a name="fontlab.flGlyph.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flGlyph.flag" href="#-fontlab.flGlyph.flag"><span class="function-name">fontlab.flGlyph.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flGlyph.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flGlyph.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flGlyph.getAuditInfo"></a>

## `getAuditInfo`


<dl class="function"><dt><a name="-fontlab.flGlyph.getAuditInfo" href="#-fontlab.flGlyph.getAuditInfo"><span class="function-name">fontlab.flGlyph.getAuditInfo</span></a> = getAuditInfo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flAuditInfo) getAuditInfo()</pre>

</dd></dl>



<a name="fontlab.flGlyph.getFastFontGateData"></a>

## `getFastFontGateData`


<dl class="function"><dt><a name="-fontlab.flGlyph.getFastFontGateData" href="#-fontlab.flGlyph.getFastFontGateData"><span class="function-name">fontlab.flGlyph.getFastFontGateData</span></a> = getFastFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgFontGateData getFastFontGateData()</pre>

</dd></dl>



<a name="fontlab.flGlyph.getLayerByName"></a>

## `getLayerByName`


<dl class="function"><dt><a name="-fontlab.flGlyph.getLayerByName" href="#-fontlab.flGlyph.getLayerByName"><span class="function-name">fontlab.flGlyph.getLayerByName</span></a> = getLayerByName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer getLayerByName(QString[, bool create =false])</pre>

</dd></dl>



<a name="fontlab.flGlyph.getLSB"></a>

## `getLSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.getLSB" href="#-fontlab.flGlyph.getLSB"><span class="function-name">fontlab.flGlyph.getLSB</span></a> = getLSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double getLSB(QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flGlyph.getProperties" href="#-fontlab.flGlyph.getProperties"><span class="function-name">fontlab.flGlyph.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flGlyph.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flGlyph.getProperty" href="#-fontlab.flGlyph.getProperty"><span class="function-name">fontlab.flGlyph.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flGlyph.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flGlyph.getPropertyFloat" href="#-fontlab.flGlyph.getPropertyFloat"><span class="function-name">fontlab.flGlyph.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flGlyph.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flGlyph.getPropertyInt" href="#-fontlab.flGlyph.getPropertyInt"><span class="function-name">fontlab.flGlyph.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flGlyph.getRSB"></a>

## `getRSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.getRSB" href="#-fontlab.flGlyph.getRSB"><span class="function-name">fontlab.flGlyph.getRSB</span></a> = getRSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double getRSB(QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.getSB"></a>

## `getSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.getSB" href="#-fontlab.flGlyph.getSB"><span class="function-name">fontlab.flGlyph.getSB</span></a> = getSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(double l, double r) getSB(QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.getStateObject"></a>

## `getStateObject`


<dl class="descriptor"><dt>fontlab.flGlyph.getStateObject</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.glyphName"></a>

## `glyphName`


<dl class="function"><dt><a name="-fontlab.flGlyph.glyphName" href="#-fontlab.flGlyph.glyphName"><span class="function-name">fontlab.flGlyph.glyphName</span></a> = glyphName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QString glyphName()</pre>

</dd></dl>



<a name="fontlab.flGlyph.glyphRect"></a>

## `glyphRect`


<dl class="descriptor"><dt>fontlab.flGlyph.glyphRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.hasBody"></a>

## `hasBody`


<dl class="descriptor"><dt>fontlab.flGlyph.hasBody</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flGlyph.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.hasFontAudit"></a>

## `hasFontAudit`


<dl class="function"><dt><a name="-fontlab.flGlyph.hasFontAudit" href="#-fontlab.flGlyph.hasFontAudit"><span class="function-name">fontlab.flGlyph.hasFontAudit</span></a> = hasFontAudit<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasFontAudit()</pre>

</dd></dl>



<a name="fontlab.flGlyph.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.hasHistoryState" href="#-fontlab.flGlyph.hasHistoryState"><span class="function-name">fontlab.flGlyph.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flGlyph.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flGlyph.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.hasInstance"></a>

## `hasInstance`


<dl class="function"><dt><a name="-fontlab.flGlyph.hasInstance" href="#-fontlab.flGlyph.hasInstance"><span class="function-name">fontlab.flGlyph.hasInstance</span></a> = hasInstance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasInstance(fgGlyph)</pre>

</dd></dl>



<a name="fontlab.flGlyph.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flGlyph.haveObject" href="#-fontlab.flGlyph.haveObject"><span class="function-name">fontlab.flGlyph.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flGlyph.haveSelected"></a>

## `haveSelected`


<dl class="function"><dt><a name="-fontlab.flGlyph.haveSelected" href="#-fontlab.flGlyph.haveSelected"><span class="function-name">fontlab.flGlyph.haveSelected</span></a> = haveSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveSelected(SelectionMode)</pre>

</dd></dl>



<a name="fontlab.flGlyph.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flGlyph.historyStates" href="#-fontlab.flGlyph.historyStates"><span class="function-name">fontlab.flGlyph.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flGlyph.horzReflection"></a>

## `horzReflection`


<dl class="function"><dt><a name="-fontlab.flGlyph.horzReflection" href="#-fontlab.flGlyph.horzReflection"><span class="function-name">fontlab.flGlyph.horzReflection</span></a> = horzReflection<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool horzReflection()</pre>

</dd></dl>



<a name="fontlab.flGlyph.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flGlyph.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flGlyph.independedAll" href="#-fontlab.flGlyph.independedAll"><span class="function-name">fontlab.flGlyph.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flGlyph.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.initialHistoryState" href="#-fontlab.flGlyph.initialHistoryState"><span class="function-name">fontlab.flGlyph.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flGlyph.inkBox"></a>

## `inkBox`


<dl class="function"><dt><a name="-fontlab.flGlyph.inkBox" href="#-fontlab.flGlyph.inkBox"><span class="function-name">fontlab.flGlyph.inkBox</span></a> = inkBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF inkBox([QTransform tx = QTransform()])</pre>

</dd></dl>



<a name="fontlab.flGlyph.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flGlyph.instanceType" href="#-fontlab.flGlyph.instanceType"><span class="function-name">fontlab.flGlyph.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flGlyph.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flGlyph.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flGlyph.isEqual" href="#-fontlab.flGlyph.isEqual"><span class="function-name">fontlab.flGlyph.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flGlyph.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flGlyph.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flGlyph.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flGlyph.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.issele"></a>

## `issele`


<dl class="function"><dt><a name="-fontlab.flGlyph.issele" href="#-fontlab.flGlyph.issele"><span class="function-name">fontlab.flGlyph.issele</span></a> = issele<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void issele(bool)</pre>

</dd></dl>



<a name="fontlab.flGlyph.isUnbindedDependecies"></a>

## `isUnbindedDependecies`


<dl class="function"><dt><a name="-fontlab.flGlyph.isUnbindedDependecies" href="#-fontlab.flGlyph.isUnbindedDependecies"><span class="function-name">fontlab.flGlyph.isUnbindedDependecies</span></a> = isUnbindedDependecies<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isUnbindedDependecies()</pre>

</dd></dl>



<a name="fontlab.flGlyph.isValid"></a>

## `isValid`


<dl class="descriptor"><dt>fontlab.flGlyph.isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.lastModified"></a>

## `lastModified`


<dl class="descriptor"><dt>fontlab.flGlyph.lastModified</dt>
<dd>

<pre class="doc" markdown="0">QDateTime</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.layers"></a>

## `layers`


<dl class="descriptor"><dt>fontlab.flGlyph.layers</dt>
<dd>

<pre class="doc" markdown="0">list(flLayer)</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.leftMetric"></a>

## `leftMetric`


<dl class="descriptor"><dt>fontlab.flGlyph.leftMetric</dt>
<dd>

<pre class="doc" markdown="0">QPointF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.linkInstances"></a>

## `linkInstances`


<dl class="function"><dt><a name="-fontlab.flGlyph.linkInstances" href="#-fontlab.flGlyph.linkInstances"><span class="function-name">fontlab.flGlyph.linkInstances</span></a> = linkInstances<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool linkInstances(flGlyph, fgGlyph)</pre>

</dd></dl>



<a name="fontlab.flGlyph.mark"></a>

## `mark`


<dl class="descriptor"><dt>fontlab.flGlyph.mark</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.measurementLine"></a>

## `measurementLine`


<dl class="function"><dt><a name="-fontlab.flGlyph.measurementLine" href="#-fontlab.flGlyph.measurementLine"><span class="function-name">fontlab.flGlyph.measurementLine</span></a> = measurementLine<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double/Nothing measurementLine()</pre>

</dd></dl>



<a name="fontlab.flGlyph.metricsLeft"></a>

## `metricsLeft`


<dl class="descriptor"><dt>fontlab.flGlyph.metricsLeft</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.metricsRect"></a>

## `metricsRect`


<dl class="descriptor"><dt>fontlab.flGlyph.metricsRect</dt>
<dd>

<pre class="doc" markdown="0">QRectF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.metricsRight"></a>

## `metricsRight`


<dl class="descriptor"><dt>fontlab.flGlyph.metricsRight</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.metricsWidth"></a>

## `metricsWidth`


<dl class="descriptor"><dt>fontlab.flGlyph.metricsWidth</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flGlyph.name</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.nodesCount"></a>

## `nodesCount`


<dl class="descriptor"><dt>fontlab.flGlyph.nodesCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.note"></a>

## `note`


<dl class="descriptor"><dt>fontlab.flGlyph.note</dt>
<dd>

<pre class="doc" markdown="0">QString</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.package"></a>

## `package`


<dl class="descriptor"><dt>fontlab.flGlyph.package</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.prepareTransformationData"></a>

## `prepareTransformationData`


<dl class="function"><dt><a name="-fontlab.flGlyph.prepareTransformationData" href="#-fontlab.flGlyph.prepareTransformationData"><span class="function-name">fontlab.flGlyph.prepareTransformationData</span></a> = prepareTransformationData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">prepareTransformationData()</pre>

</dd></dl>



<a name="fontlab.flGlyph.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flGlyph.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flGlyph.release" href="#-fontlab.flGlyph.release"><span class="function-name">fontlab.flGlyph.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flGlyph.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flGlyph.remove" href="#-fontlab.flGlyph.remove"><span class="function-name">fontlab.flGlyph.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flGlyph.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flGlyph.removeChild" href="#-fontlab.flGlyph.removeChild"><span class="function-name">fontlab.flGlyph.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flGlyph.removeEmptyShapes"></a>

## `removeEmptyShapes`


<dl class="function"><dt><a name="-fontlab.flGlyph.removeEmptyShapes" href="#-fontlab.flGlyph.removeEmptyShapes"><span class="function-name">fontlab.flGlyph.removeEmptyShapes</span></a> = removeEmptyShapes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeEmptyShapes()</pre>

</dd></dl>



<a name="fontlab.flGlyph.removeLayer"></a>

## `removeLayer`


<dl class="function"><dt><a name="-fontlab.flGlyph.removeLayer" href="#-fontlab.flGlyph.removeLayer"><span class="function-name">fontlab.flGlyph.removeLayer</span></a> = removeLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void removeLayer(flLayer)</pre>

</dd></dl>



<a name="fontlab.flGlyph.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flGlyph.removeProperty" href="#-fontlab.flGlyph.removeProperty"><span class="function-name">fontlab.flGlyph.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flGlyph.resetInkBox"></a>

## `resetInkBox`


<dl class="function"><dt><a name="-fontlab.flGlyph.resetInkBox" href="#-fontlab.flGlyph.resetInkBox"><span class="function-name">fontlab.flGlyph.resetInkBox</span></a> = resetInkBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">resetInkBox()</pre>

</dd></dl>



<a name="fontlab.flGlyph.resetTransformationData"></a>

## `resetTransformationData`


<dl class="function"><dt><a name="-fontlab.flGlyph.resetTransformationData" href="#-fontlab.flGlyph.resetTransformationData"><span class="function-name">fontlab.flGlyph.resetTransformationData</span></a> = resetTransformationData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">resetTransformationData()</pre>

</dd></dl>



<a name="fontlab.flGlyph.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flGlyph.restoreHistoryState" href="#-fontlab.flGlyph.restoreHistoryState"><span class="function-name">fontlab.flGlyph.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flGlyph.rightMetric"></a>

## `rightMetric`


<dl class="descriptor"><dt>fontlab.flGlyph.rightMetric</dt>
<dd>

<pre class="doc" markdown="0">QPointF</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.setAllShapesSelected"></a>

## `setAllShapesSelected`


<dl class="function"><dt><a name="-fontlab.flGlyph.setAllShapesSelected" href="#-fontlab.flGlyph.setAllShapesSelected"><span class="function-name">fontlab.flGlyph.setAllShapesSelected</span></a> = setAllShapesSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setAllShapesSelected(bool)</pre>

</dd></dl>



<a name="fontlab.flGlyph.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flGlyph.setFlag" href="#-fontlab.flGlyph.setFlag"><span class="function-name">fontlab.flGlyph.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flGlyph.setLayers"></a>

## `setLayers`


<dl class="function"><dt><a name="-fontlab.flGlyph.setLayers" href="#-fontlab.flGlyph.setLayers"><span class="function-name">fontlab.flGlyph.setLayers</span></a> = setLayers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void setLayers(list(flLayer))</pre>

</dd></dl>



<a name="fontlab.flGlyph.setLSB"></a>

## `setLSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.setLSB" href="#-fontlab.flGlyph.setLSB"><span class="function-name">fontlab.flGlyph.setLSB</span></a> = setLSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setLSB(double v, bool move_guidelines, QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flGlyph.setProperty" href="#-fontlab.flGlyph.setProperty"><span class="function-name">fontlab.flGlyph.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flGlyph.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flGlyph.setPropertyFloat" href="#-fontlab.flGlyph.setPropertyFloat"><span class="function-name">fontlab.flGlyph.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flGlyph.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flGlyph.setPropertyInt" href="#-fontlab.flGlyph.setPropertyInt"><span class="function-name">fontlab.flGlyph.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flGlyph.setReflected"></a>

## `setReflected`


<dl class="function"><dt><a name="-fontlab.flGlyph.setReflected" href="#-fontlab.flGlyph.setReflected"><span class="function-name">fontlab.flGlyph.setReflected</span></a> = setReflected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setReflected(bool, bool)</pre>

</dd></dl>



<a name="fontlab.flGlyph.setRSB"></a>

## `setRSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.setRSB" href="#-fontlab.flGlyph.setRSB"><span class="function-name">fontlab.flGlyph.setRSB</span></a> = setRSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setRSB(double v, QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.setSB"></a>

## `setSB`


<dl class="function"><dt><a name="-fontlab.flGlyph.setSB" href="#-fontlab.flGlyph.setSB"><span class="function-name">fontlab.flGlyph.setSB</span></a> = setSB<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setSB(double l, double r, bool move_guidelines, bool all_layers, QTransform tr)</pre>

</dd></dl>



<a name="fontlab.flGlyph.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flGlyph.tag" href="#-fontlab.flGlyph.tag"><span class="function-name">fontlab.flGlyph.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flGlyph.tags"></a>

## `tags`


<dl class="descriptor"><dt>fontlab.flGlyph.tags</dt>
<dd>

<pre class="doc" markdown="0">QStringList</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flGlyph.type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>



<a name="fontlab.flGlyph.unselectAllNodes"></a>

## `unselectAllNodes`


<dl class="function"><dt><a name="-fontlab.flGlyph.unselectAllNodes" href="#-fontlab.flGlyph.unselectAllNodes"><span class="function-name">fontlab.flGlyph.unselectAllNodes</span></a> = unselectAllNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">unselectAllNodes()</pre>

</dd></dl>



<a name="fontlab.flGlyph.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flGlyph.update" href="#-fontlab.flGlyph.update"><span class="function-name">fontlab.flGlyph.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>



<a name="fontlab.flGlyph.updateActiveLayer"></a>

## `updateActiveLayer`


<dl class="function"><dt><a name="-fontlab.flGlyph.updateActiveLayer" href="#-fontlab.flGlyph.updateActiveLayer"><span class="function-name">fontlab.flGlyph.updateActiveLayer</span></a> = updateActiveLayer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLayer updateActiveLayer(bool)</pre>

</dd></dl>



<a name="fontlab.flGlyph.updateAudit"></a>

## `updateAudit`


<dl class="function"><dt><a name="-fontlab.flGlyph.updateAudit" href="#-fontlab.flGlyph.updateAudit"><span class="function-name">fontlab.flGlyph.updateAudit</span></a> = updateAudit<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void updateAudit(list(int))</pre>

</dd></dl>



<a name="fontlab.flGlyph.updatedFgGlyphs"></a>

## `updatedFgGlyphs`


<dl class="function"><dt><a name="-fontlab.flGlyph.updatedFgGlyphs" href="#-fontlab.flGlyph.updatedFgGlyphs"><span class="function-name">fontlab.flGlyph.updatedFgGlyphs</span></a> = updatedFgGlyphs<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(uint32_t) updatedFgGlyphs()</pre>

</dd></dl>



<a name="fontlab.flGlyph.updateFgGlyph"></a>

## `updateFgGlyph`


<dl class="function"><dt><a name="-fontlab.flGlyph.updateFgGlyph" href="#-fontlab.flGlyph.updateFgGlyph"><span class="function-name">fontlab.flGlyph.updateFgGlyph</span></a> = updateFgGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateFgGlyph(uint id)</pre>

</dd></dl>



<a name="fontlab.flGlyph.updateSidebearings"></a>

## `updateSidebearings`


<dl class="function"><dt><a name="-fontlab.flGlyph.updateSidebearings" href="#-fontlab.flGlyph.updateSidebearings"><span class="function-name">fontlab.flGlyph.updateSidebearings</span></a> = updateSidebearings<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool updateSidebearings(bool nofify)</pre>

</dd></dl>



<a name="fontlab.flGlyph.vertReflection"></a>

## `vertReflection`


<dl class="function"><dt><a name="-fontlab.flGlyph.vertReflection" href="#-fontlab.flGlyph.vertReflection"><span class="function-name">fontlab.flGlyph.vertReflection</span></a> = vertReflection<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool vertReflection()</pre>

</dd></dl>



<a name="fontlab.flGlyph.virtualTags"></a>

## `virtualTags`


<dl class="function"><dt><a name="-fontlab.flGlyph.virtualTags" href="#-fontlab.flGlyph.virtualTags"><span class="function-name">fontlab.flGlyph.virtualTags</span></a> = virtualTags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QSet<QString>/Nothing virtualTags()</pre>

</dd></dl>

