

<a name="fontlab.flNodeInfo"></a>

# `flNodeInfo`


<dt class="class"><h2><span class="class-name">fontlab.flNodeInfo</span> = <a name="fontlab.flNodeInfo" href="#fontlab.flNodeInfo">class flNodeInfo</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flNodeInfo representation

Constructors:
  flNodeInfo()
  flNodeInfo(flObject)
  flNodeInfo(flNodeInfo)
  flNodeInfo(flNode, QTransform)
  flNodeInfo(flNode, flObject contour_info)
  flNodeInfo(flNode, flObject glyph_info, QTransform)
  flNodeInfo(flNode, flNodeInfo)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flNodeInfo-__delattr__" href="#flNodeInfo-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__eq__" href="#flNodeInfo-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__ge__" href="#flNodeInfo-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__getattribute__" href="#flNodeInfo-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__gt__" href="#flNodeInfo-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__init__" href="#flNodeInfo-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flNodeInfo-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__le__" href="#flNodeInfo-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__lt__" href="#flNodeInfo-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__ne__" href="#flNodeInfo-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__repr__" href="#flNodeInfo-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-__setattr__" href="#flNodeInfo-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNodeInfo-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-breakContourExpanded" href="#flNodeInfo-breakContourExpanded"><span class="function-name">breakContourExpanded</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNodeInfo-breakContourExpanded">breakContourExpanded</a>([double extrapolate_d=0.5])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-changed" href="#flNodeInfo-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-checkInitHistoryState" href="#flNodeInfo-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-clearAboveHistory" href="#flNodeInfo-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-clearFlag" href="#flNodeInfo-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-clearFlags" href="#flNodeInfo-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-clone" href="#flNodeInfo-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-combine" href="#flNodeInfo-combine"><span class="function-name">combine</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-combine">combine</a>(QTransform transform)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-contour" href="#flNodeInfo-contour"><span class="function-name">contour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour <a href="#fontlab.flNodeInfo-contour">contour</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-createHistoryState" href="#flNodeInfo-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-currentHistoryState" href="#flNodeInfo-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-flag" href="#flNodeInfo-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getGlyphPoint" href="#flNodeInfo-getGlyphPoint"><span class="function-name">getGlyphPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flNodeInfo-getGlyphPoint">getGlyphPoint</a>(bool round)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getMappedNeighborsRect" href="#flNodeInfo-getMappedNeighborsRect"><span class="function-name">getMappedNeighborsRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flNodeInfo-getMappedNeighborsRect">getMappedNeighborsRect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getMappedPoint" href="#flNodeInfo-getMappedPoint"><span class="function-name">getMappedPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flNodeInfo-getMappedPoint">getMappedPoint</a>([QPointF])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getProperties" href="#flNodeInfo-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getProperty" href="#flNodeInfo-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getPropertyFloat" href="#flNodeInfo-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getPropertyInt" href="#flNodeInfo-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-getUpdateCanvasRect" href="#flNodeInfo-getUpdateCanvasRect"><span class="function-name">getUpdateCanvasRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flNodeInfo-getUpdateCanvasRect">getUpdateCanvasRect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-hasHistoryState" href="#flNodeInfo-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-historyStates" href="#flNodeInfo-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-independedAll" href="#flNodeInfo-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-initialHistoryState" href="#flNodeInfo-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-isEqual" href="#flNodeInfo-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-isValid" href="#flNodeInfo-isValid"><span class="function-name">isValid</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNodeInfo-isValid">isValid</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-release" href="#flNodeInfo-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-remove" href="#flNodeInfo-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-removeChild" href="#flNodeInfo-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-removeProperty" href="#flNodeInfo-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-restoreHistoryState" href="#flNodeInfo-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setFlag" href="#flNodeInfo-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setGlyphPoint" href="#flNodeInfo-setGlyphPoint"><span class="function-name">setGlyphPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setGlyphPoint">setGlyphPoint</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setGlyphPointX" href="#flNodeInfo-setGlyphPointX"><span class="function-name">setGlyphPointX</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setGlyphPointX">setGlyphPointX</a>(double x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setGlyphPointY" href="#flNodeInfo-setGlyphPointY"><span class="function-name">setGlyphPointY</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setGlyphPointY">setGlyphPointY</a>(double y)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setProperty" href="#flNodeInfo-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setPropertyFloat" href="#flNodeInfo-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-setPropertyInt" href="#flNodeInfo-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-shape" href="#flNodeInfo-shape"><span class="function-name">shape</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShape <a href="#fontlab.flNodeInfo-shape">shape</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-shapeInfo" href="#flNodeInfo-shapeInfo"><span class="function-name">shapeInfo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShapeInfo <a href="#fontlab.flNodeInfo-shapeInfo">shapeInfo</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-tag" href="#flNodeInfo-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-toNodesInfo" href="#flNodeInfo-toNodesInfo"><span class="function-name">toNodesInfo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNodeInfo) <a href="#fontlab.flNodeInfo-toNodesInfo">toNodesInfo</a>(list(flNode))</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-update" href="#flNodeInfo-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNodeInfo-update">update</a>()</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flNodeInfo-cloneObject" href="#flNodeInfo-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flNodeInfo-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-createInstance" href="#flNodeInfo-createInstance"><span class="function-name">createInstance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNodeInfo <a href="#fontlab.flNodeInfo-createInstance">createInstance</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-createObject" href="#flNodeInfo-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flNodeInfo-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-haveObject" href="#flNodeInfo-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNodeInfo-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNodeInfo-instanceType" href="#flNodeInfo-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flNodeInfo-instanceType">instanceType</a>();</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>contourInfo</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>
<dl class="descriptor"><dt>dist</dt>
<dd>

<pre class="doc" markdown="0">double dist</pre>

</dd>
</dl>
<dl class="descriptor"><dt>glyphInfo</dt>
<dd>

<pre class="doc" markdown="0">flObject - glyph info</pre>

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
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>node</dt>
<dd>

<pre class="doc" markdown="0">flNode</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>transform</dt>
<dd>

<pre class="doc" markdown="0">transform matrix</pre>

</dd>
</dl>
<dl class="descriptor"><dt>type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flNodeInfo-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flNodeInfo.breakContourExpanded"></a>

## `breakContourExpanded`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.breakContourExpanded" href="#-fontlab.flNodeInfo.breakContourExpanded"><span class="function-name">fontlab.flNodeInfo.breakContourExpanded</span></a> = breakContourExpanded<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool breakContourExpanded([double extrapolate_d=0.5])</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.changed" href="#-fontlab.flNodeInfo.changed"><span class="function-name">fontlab.flNodeInfo.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.checkInitHistoryState" href="#-fontlab.flNodeInfo.checkInitHistoryState"><span class="function-name">fontlab.flNodeInfo.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.clearAboveHistory" href="#-fontlab.flNodeInfo.clearAboveHistory"><span class="function-name">fontlab.flNodeInfo.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.clearFlag" href="#-fontlab.flNodeInfo.clearFlag"><span class="function-name">fontlab.flNodeInfo.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.clearFlags" href="#-fontlab.flNodeInfo.clearFlags"><span class="function-name">fontlab.flNodeInfo.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.clone" href="#-fontlab.flNodeInfo.clone"><span class="function-name">fontlab.flNodeInfo.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.cloneObject" href="#-fontlab.flNodeInfo.cloneObject"><span class="function-name">fontlab.flNodeInfo.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.combine"></a>

## `combine`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.combine" href="#-fontlab.flNodeInfo.combine"><span class="function-name">fontlab.flNodeInfo.combine</span></a> = combine<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">combine(QTransform transform)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.contour"></a>

## `contour`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.contour" href="#-fontlab.flNodeInfo.contour"><span class="function-name">fontlab.flNodeInfo.contour</span></a> = contour<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour contour()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.contourInfo"></a>

## `contourInfo`


<dl class="descriptor"><dt>fontlab.flNodeInfo.contourInfo</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.createHistoryState" href="#-fontlab.flNodeInfo.createHistoryState"><span class="function-name">fontlab.flNodeInfo.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.createInstance"></a>

## `createInstance`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.createInstance" href="#-fontlab.flNodeInfo.createInstance"><span class="function-name">fontlab.flNodeInfo.createInstance</span></a> = createInstance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNodeInfo createInstance()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.createObject" href="#-fontlab.flNodeInfo.createObject"><span class="function-name">fontlab.flNodeInfo.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.currentHistoryState" href="#-fontlab.flNodeInfo.currentHistoryState"><span class="function-name">fontlab.flNodeInfo.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.dist"></a>

## `dist`


<dl class="descriptor"><dt>fontlab.flNodeInfo.dist</dt>
<dd>

<pre class="doc" markdown="0">double dist</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.flag" href="#-fontlab.flNodeInfo.flag"><span class="function-name">fontlab.flNodeInfo.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flNodeInfo.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flNodeInfo.getGlyphPoint"></a>

## `getGlyphPoint`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getGlyphPoint" href="#-fontlab.flNodeInfo.getGlyphPoint"><span class="function-name">fontlab.flNodeInfo.getGlyphPoint</span></a> = getGlyphPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF getGlyphPoint(bool round)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getMappedNeighborsRect"></a>

## `getMappedNeighborsRect`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getMappedNeighborsRect" href="#-fontlab.flNodeInfo.getMappedNeighborsRect"><span class="function-name">fontlab.flNodeInfo.getMappedNeighborsRect</span></a> = getMappedNeighborsRect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF getMappedNeighborsRect()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getMappedPoint"></a>

## `getMappedPoint`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getMappedPoint" href="#-fontlab.flNodeInfo.getMappedPoint"><span class="function-name">fontlab.flNodeInfo.getMappedPoint</span></a> = getMappedPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF getMappedPoint([QPointF])</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getProperties" href="#-fontlab.flNodeInfo.getProperties"><span class="function-name">fontlab.flNodeInfo.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getProperty" href="#-fontlab.flNodeInfo.getProperty"><span class="function-name">fontlab.flNodeInfo.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getPropertyFloat" href="#-fontlab.flNodeInfo.getPropertyFloat"><span class="function-name">fontlab.flNodeInfo.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getPropertyInt" href="#-fontlab.flNodeInfo.getPropertyInt"><span class="function-name">fontlab.flNodeInfo.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.getUpdateCanvasRect"></a>

## `getUpdateCanvasRect`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.getUpdateCanvasRect" href="#-fontlab.flNodeInfo.getUpdateCanvasRect"><span class="function-name">fontlab.flNodeInfo.getUpdateCanvasRect</span></a> = getUpdateCanvasRect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF getUpdateCanvasRect()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.glyphInfo"></a>

## `glyphInfo`


<dl class="descriptor"><dt>fontlab.flNodeInfo.glyphInfo</dt>
<dd>

<pre class="doc" markdown="0">flObject - glyph info</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flNodeInfo.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.hasHistoryState" href="#-fontlab.flNodeInfo.hasHistoryState"><span class="function-name">fontlab.flNodeInfo.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flNodeInfo.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.haveObject" href="#-fontlab.flNodeInfo.haveObject"><span class="function-name">fontlab.flNodeInfo.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.historyStates" href="#-fontlab.flNodeInfo.historyStates"><span class="function-name">fontlab.flNodeInfo.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flNodeInfo.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.independedAll" href="#-fontlab.flNodeInfo.independedAll"><span class="function-name">fontlab.flNodeInfo.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.initialHistoryState" href="#-fontlab.flNodeInfo.initialHistoryState"><span class="function-name">fontlab.flNodeInfo.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.instanceType" href="#-fontlab.flNodeInfo.instanceType"><span class="function-name">fontlab.flNodeInfo.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flNodeInfo.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.isEqual" href="#-fontlab.flNodeInfo.isEqual"><span class="function-name">fontlab.flNodeInfo.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flNodeInfo.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flNodeInfo.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flNodeInfo.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.isValid"></a>

## `isValid`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.isValid" href="#-fontlab.flNodeInfo.isValid"><span class="function-name">fontlab.flNodeInfo.isValid</span></a> = isValid<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isValid()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flNodeInfo.name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.node"></a>

## `node`


<dl class="descriptor"><dt>fontlab.flNodeInfo.node</dt>
<dd>

<pre class="doc" markdown="0">flNode</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flNodeInfo.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.release" href="#-fontlab.flNodeInfo.release"><span class="function-name">fontlab.flNodeInfo.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.remove" href="#-fontlab.flNodeInfo.remove"><span class="function-name">fontlab.flNodeInfo.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.removeChild" href="#-fontlab.flNodeInfo.removeChild"><span class="function-name">fontlab.flNodeInfo.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.removeProperty" href="#-fontlab.flNodeInfo.removeProperty"><span class="function-name">fontlab.flNodeInfo.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.restoreHistoryState" href="#-fontlab.flNodeInfo.restoreHistoryState"><span class="function-name">fontlab.flNodeInfo.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setFlag" href="#-fontlab.flNodeInfo.setFlag"><span class="function-name">fontlab.flNodeInfo.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setGlyphPoint"></a>

## `setGlyphPoint`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setGlyphPoint" href="#-fontlab.flNodeInfo.setGlyphPoint"><span class="function-name">fontlab.flNodeInfo.setGlyphPoint</span></a> = setGlyphPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setGlyphPoint(QPointF)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setGlyphPointX"></a>

## `setGlyphPointX`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setGlyphPointX" href="#-fontlab.flNodeInfo.setGlyphPointX"><span class="function-name">fontlab.flNodeInfo.setGlyphPointX</span></a> = setGlyphPointX<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setGlyphPointX(double x)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setGlyphPointY"></a>

## `setGlyphPointY`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setGlyphPointY" href="#-fontlab.flNodeInfo.setGlyphPointY"><span class="function-name">fontlab.flNodeInfo.setGlyphPointY</span></a> = setGlyphPointY<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setGlyphPointY(double y)</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setProperty" href="#-fontlab.flNodeInfo.setProperty"><span class="function-name">fontlab.flNodeInfo.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setPropertyFloat" href="#-fontlab.flNodeInfo.setPropertyFloat"><span class="function-name">fontlab.flNodeInfo.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.setPropertyInt" href="#-fontlab.flNodeInfo.setPropertyInt"><span class="function-name">fontlab.flNodeInfo.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.shape"></a>

## `shape`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.shape" href="#-fontlab.flNodeInfo.shape"><span class="function-name">fontlab.flNodeInfo.shape</span></a> = shape<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShape shape()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.shapeInfo"></a>

## `shapeInfo`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.shapeInfo" href="#-fontlab.flNodeInfo.shapeInfo"><span class="function-name">fontlab.flNodeInfo.shapeInfo</span></a> = shapeInfo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShapeInfo shapeInfo()</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.tag" href="#-fontlab.flNodeInfo.tag"><span class="function-name">fontlab.flNodeInfo.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.toNodesInfo"></a>

## `toNodesInfo`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.toNodesInfo" href="#-fontlab.flNodeInfo.toNodesInfo"><span class="function-name">fontlab.flNodeInfo.toNodesInfo</span></a> = toNodesInfo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNodeInfo) toNodesInfo(list(flNode))</pre>

</dd></dl>



<a name="fontlab.flNodeInfo.transform"></a>

## `transform`


<dl class="descriptor"><dt>fontlab.flNodeInfo.transform</dt>
<dd>

<pre class="doc" markdown="0">transform matrix</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flNodeInfo.type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>



<a name="fontlab.flNodeInfo.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flNodeInfo.update" href="#-fontlab.flNodeInfo.update"><span class="function-name">fontlab.flNodeInfo.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>

