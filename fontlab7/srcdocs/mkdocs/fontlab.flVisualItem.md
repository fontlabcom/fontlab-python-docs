

<a name="fontlab.flVisualItem"></a>

# `flVisualItem`


<dt class="class"><h2><span class="class-name">fontlab.flVisualItem</span> = <a name="fontlab.flVisualItem" href="#fontlab.flVisualItem">class flVisualItem</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flVisualItem representation

Constructors:
  flVisualItem()
  flVisualItem(flVisualItem)
  flVisualItem(flObject)
  flVisualItem(objId id)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flVisualItem-__delattr__" href="#flVisualItem-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__eq__" href="#flVisualItem-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__ge__" href="#flVisualItem-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__getattribute__" href="#flVisualItem-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__gt__" href="#flVisualItem-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__init__" href="#flVisualItem-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flVisualItem-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__le__" href="#flVisualItem-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__lt__" href="#flVisualItem-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__ne__" href="#flVisualItem-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__repr__" href="#flVisualItem-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-__setattr__" href="#flVisualItem-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flVisualItem-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-acceptEvents" href="#flVisualItem-acceptEvents"><span class="function-name">acceptEvents</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flVisualItem-acceptEvents">acceptEvents</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-activateEditor" href="#flVisualItem-activateEditor"><span class="function-name">activateEditor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-activateEditor">activateEditor</a>(QPointF canvas_pos)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-addedToCanvas" href="#flVisualItem-addedToCanvas"><span class="function-name">addedToCanvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-addedToCanvas">addedToCanvas</a>(flCanvas)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-adjustCanvasPosition" href="#flVisualItem-adjustCanvasPosition"><span class="function-name">adjustCanvasPosition</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flVisualItem-adjustCanvasPosition">adjustCanvasPosition</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-adjustPosition" href="#flVisualItem-adjustPosition"><span class="function-name">adjustPosition</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | double <a href="#fontlab.flVisualItem-adjustPosition">adjustPosition</a>(QPointF | double)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-appendDecorator" href="#flVisualItem-appendDecorator"><span class="function-name">appendDecorator</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-appendDecorator">appendDecorator</a>(flVisualItem, DecoratorOrder)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-boundingRectOnCanvas" href="#flVisualItem-boundingRectOnCanvas"><span class="function-name">boundingRectOnCanvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flVisualItem-boundingRectOnCanvas">boundingRectOnCanvas</a>(</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-canvas" href="#flVisualItem-canvas"><span class="function-name">canvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flCanvas <a href="#fontlab.flVisualItem-canvas">canvas</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-changed" href="#flVisualItem-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-checkInitHistoryState" href="#flVisualItem-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clearAboveHistory" href="#flVisualItem-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clearDecorators" href="#flVisualItem-clearDecorators"><span class="function-name">clearDecorators</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-clearDecorators">clearDecorators</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clearFlag" href="#flVisualItem-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clearFlags" href="#flVisualItem-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clearItems" href="#flVisualItem-clearItems"><span class="function-name">clearItems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-clearItems">clearItems</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-clone" href="#flVisualItem-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-contain" href="#flVisualItem-contain"><span class="function-name">contain</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-contain">contain</a>(QPointF canvas_pos)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-containsItem" href="#flVisualItem-containsItem"><span class="function-name">containsItem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-containsItem">containsItem</a>(flVisualItem)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-createHistoryState" href="#flVisualItem-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-currentHistoryState" href="#flVisualItem-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-deactivateEditor" href="#flVisualItem-deactivateEditor"><span class="function-name">deactivateEditor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-deactivateEditor">deactivateEditor</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-distanceTo" href="#flVisualItem-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flVisualItem-distanceTo">distanceTo</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-flag" href="#flVisualItem-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-getProperties" href="#flVisualItem-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-getProperty" href="#flVisualItem-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-getPropertyFloat" href="#flVisualItem-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-getPropertyInt" href="#flVisualItem-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-hasHistoryState" href="#flVisualItem-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-haveCanvas" href="#flVisualItem-haveCanvas"><span class="function-name">haveCanvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-haveCanvas">haveCanvas</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-haveEditor" href="#flVisualItem-haveEditor"><span class="function-name">haveEditor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-haveEditor">haveEditor</a>(QPointF canvas_pos)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-hide" href="#flVisualItem-hide"><span class="function-name">hide</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-hide">hide</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-historyStates" href="#flVisualItem-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-independedAll" href="#flVisualItem-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-initialHistoryState" href="#flVisualItem-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-invselect" href="#flVisualItem-invselect"><span class="function-name">invselect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-invselect">invselect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-isEqual" href="#flVisualItem-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-isSelectable" href="#flVisualItem-isSelectable"><span class="function-name">isSelectable</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-isSelectable">isSelectable</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-isStableSelect" href="#flVisualItem-isStableSelect"><span class="function-name">isStableSelect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-isStableSelect">isStableSelect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-itemScale" href="#flVisualItem-itemScale"><span class="function-name">itemScale</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flVisualItem-itemScale">itemScale</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-mapCanvasDistanceToItem" href="#flVisualItem-mapCanvasDistanceToItem"><span class="function-name">mapCanvasDistanceToItem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flVisualItem-mapCanvasDistanceToItem">mapCanvasDistanceToItem</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-mapCanvasToItem" href="#flVisualItem-mapCanvasToItem"><span class="function-name">mapCanvasToItem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | QRectF <a href="#fontlab.flVisualItem-mapCanvasToItem">mapCanvasToItem</a>(QPointF | QRectF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-mapItemToCanvas" href="#flVisualItem-mapItemToCanvas"><span class="function-name">mapItemToCanvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | QRectF <a href="#fontlab.flVisualItem-mapItemToCanvas">mapItemToCanvas</a>(QPointF | QRectF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-metricStep" href="#flVisualItem-metricStep"><span class="function-name">metricStep</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flVisualItem-metricStep">metricStep</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-move" href="#flVisualItem-move"><span class="function-name">move</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-move">move</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-paint" href="#flVisualItem-paint"><span class="function-name">paint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-paint">paint</a>(QPainter*)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-preview" href="#flVisualItem-preview"><span class="function-name">preview</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-preview">preview</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-referencePoint" href="#flVisualItem-referencePoint"><span class="function-name">referencePoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flVisualItem-referencePoint">referencePoint</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-release" href="#flVisualItem-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-remove" href="#flVisualItem-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-removeChild" href="#flVisualItem-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-removeDecorator" href="#flVisualItem-removeDecorator"><span class="function-name">removeDecorator</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-removeDecorator">removeDecorator</a>(flVisualItem)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-removeItem" href="#flVisualItem-removeItem"><span class="function-name">removeItem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.flVisualItem-removeItem">removeItem</a>(flVisualItem)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-removeProperty" href="#flVisualItem-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-removedFromCanvas" href="#flVisualItem-removedFromCanvas"><span class="function-name">removedFromCanvas</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-removedFromCanvas">removedFromCanvas</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-restoreHistoryState" href="#flVisualItem-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-select" href="#flVisualItem-select"><span class="function-name">select</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-select">select</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-setFlag" href="#flVisualItem-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-setProperty" href="#flVisualItem-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-setPropertyFloat" href="#flVisualItem-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-setPropertyInt" href="#flVisualItem-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-show" href="#flVisualItem-show"><span class="function-name">show</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-show">show</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-tag" href="#flVisualItem-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-unselect" href="#flVisualItem-unselect"><span class="function-name">unselect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-unselect">unselect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-update" href="#flVisualItem-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flVisualItem-update">update</a>()</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flVisualItem-cloneObject" href="#flVisualItem-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flVisualItem-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-createObject" href="#flVisualItem-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flVisualItem-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-haveObject" href="#flVisualItem-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flVisualItem-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-instanceAcceptEvents" href="#flVisualItem-instanceAcceptEvents"><span class="function-name">instanceAcceptEvents</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flVisualItem-instanceAcceptEvents">instanceAcceptEvents</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flVisualItem-instanceType" href="#flVisualItem-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flVisualItem-instanceType">instanceType</a>();</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hovered</dt>
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
<dl class="descriptor"><dt>locked</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>opacity</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>owner</dt>
<dd>

<pre class="doc" markdown="0">flVisualItem</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>selected</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>transform</dt>
<dd>

<pre class="doc" markdown="0">QTransform</pre>

</dd>
</dl>
<dl class="descriptor"><dt>type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>
<dl class="descriptor"><dt>visible</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">Listeners</span> = {'ClickListener': 8, 'DragListener': 4, 'HoverListener': 1, 'MoveListener': 2}</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flVisualItem-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flVisualItem.acceptEvents"></a>

## `acceptEvents`


<dl class="function"><dt><a name="-fontlab.flVisualItem.acceptEvents" href="#-fontlab.flVisualItem.acceptEvents"><span class="function-name">fontlab.flVisualItem.acceptEvents</span></a> = acceptEvents<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int acceptEvents()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.activateEditor"></a>

## `activateEditor`


<dl class="function"><dt><a name="-fontlab.flVisualItem.activateEditor" href="#-fontlab.flVisualItem.activateEditor"><span class="function-name">fontlab.flVisualItem.activateEditor</span></a> = activateEditor<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void activateEditor(QPointF canvas_pos)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.addedToCanvas"></a>

## `addedToCanvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.addedToCanvas" href="#-fontlab.flVisualItem.addedToCanvas"><span class="function-name">fontlab.flVisualItem.addedToCanvas</span></a> = addedToCanvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void addedToCanvas(flCanvas)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.adjustCanvasPosition"></a>

## `adjustCanvasPosition`


<dl class="function"><dt><a name="-fontlab.flVisualItem.adjustCanvasPosition" href="#-fontlab.flVisualItem.adjustCanvasPosition"><span class="function-name">fontlab.flVisualItem.adjustCanvasPosition</span></a> = adjustCanvasPosition<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF adjustCanvasPosition(QPointF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.adjustPosition"></a>

## `adjustPosition`


<dl class="function"><dt><a name="-fontlab.flVisualItem.adjustPosition" href="#-fontlab.flVisualItem.adjustPosition"><span class="function-name">fontlab.flVisualItem.adjustPosition</span></a> = adjustPosition<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | double adjustPosition(QPointF | double)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.appendDecorator"></a>

## `appendDecorator`


<dl class="function"><dt><a name="-fontlab.flVisualItem.appendDecorator" href="#-fontlab.flVisualItem.appendDecorator"><span class="function-name">fontlab.flVisualItem.appendDecorator</span></a> = appendDecorator<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void appendDecorator(flVisualItem, DecoratorOrder)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.boundingRectOnCanvas"></a>

## `boundingRectOnCanvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.boundingRectOnCanvas" href="#-fontlab.flVisualItem.boundingRectOnCanvas"><span class="function-name">fontlab.flVisualItem.boundingRectOnCanvas</span></a> = boundingRectOnCanvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF boundingRectOnCanvas(</pre>

</dd></dl>



<a name="fontlab.flVisualItem.canvas"></a>

## `canvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.canvas" href="#-fontlab.flVisualItem.canvas"><span class="function-name">fontlab.flVisualItem.canvas</span></a> = canvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flCanvas canvas()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flVisualItem.changed" href="#-fontlab.flVisualItem.changed"><span class="function-name">fontlab.flVisualItem.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.checkInitHistoryState" href="#-fontlab.flVisualItem.checkInitHistoryState"><span class="function-name">fontlab.flVisualItem.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clearAboveHistory" href="#-fontlab.flVisualItem.clearAboveHistory"><span class="function-name">fontlab.flVisualItem.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clearDecorators"></a>

## `clearDecorators`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clearDecorators" href="#-fontlab.flVisualItem.clearDecorators"><span class="function-name">fontlab.flVisualItem.clearDecorators</span></a> = clearDecorators<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearDecorators()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clearFlag" href="#-fontlab.flVisualItem.clearFlag"><span class="function-name">fontlab.flVisualItem.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clearFlags" href="#-fontlab.flVisualItem.clearFlags"><span class="function-name">fontlab.flVisualItem.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clearItems"></a>

## `clearItems`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clearItems" href="#-fontlab.flVisualItem.clearItems"><span class="function-name">fontlab.flVisualItem.clearItems</span></a> = clearItems<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearItems()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flVisualItem.clone" href="#-fontlab.flVisualItem.clone"><span class="function-name">fontlab.flVisualItem.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flVisualItem.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flVisualItem.cloneObject" href="#-fontlab.flVisualItem.cloneObject"><span class="function-name">fontlab.flVisualItem.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flVisualItem.contain"></a>

## `contain`


<dl class="function"><dt><a name="-fontlab.flVisualItem.contain" href="#-fontlab.flVisualItem.contain"><span class="function-name">fontlab.flVisualItem.contain</span></a> = contain<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool contain(QPointF canvas_pos)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.containsItem"></a>

## `containsItem`


<dl class="function"><dt><a name="-fontlab.flVisualItem.containsItem" href="#-fontlab.flVisualItem.containsItem"><span class="function-name">fontlab.flVisualItem.containsItem</span></a> = containsItem<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool containsItem(flVisualItem)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.createHistoryState" href="#-fontlab.flVisualItem.createHistoryState"><span class="function-name">fontlab.flVisualItem.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flVisualItem.createObject" href="#-fontlab.flVisualItem.createObject"><span class="function-name">fontlab.flVisualItem.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flVisualItem.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.currentHistoryState" href="#-fontlab.flVisualItem.currentHistoryState"><span class="function-name">fontlab.flVisualItem.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.deactivateEditor"></a>

## `deactivateEditor`


<dl class="function"><dt><a name="-fontlab.flVisualItem.deactivateEditor" href="#-fontlab.flVisualItem.deactivateEditor"><span class="function-name">fontlab.flVisualItem.deactivateEditor</span></a> = deactivateEditor<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">deactivateEditor()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.distanceTo"></a>

## `distanceTo`


<dl class="function"><dt><a name="-fontlab.flVisualItem.distanceTo" href="#-fontlab.flVisualItem.distanceTo"><span class="function-name">fontlab.flVisualItem.distanceTo</span></a> = distanceTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double distanceTo(QPointF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flVisualItem.flag" href="#-fontlab.flVisualItem.flag"><span class="function-name">fontlab.flVisualItem.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flVisualItem.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flVisualItem.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flVisualItem.getProperties" href="#-fontlab.flVisualItem.getProperties"><span class="function-name">fontlab.flVisualItem.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flVisualItem.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flVisualItem.getProperty" href="#-fontlab.flVisualItem.getProperty"><span class="function-name">fontlab.flVisualItem.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flVisualItem.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flVisualItem.getPropertyFloat" href="#-fontlab.flVisualItem.getPropertyFloat"><span class="function-name">fontlab.flVisualItem.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flVisualItem.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flVisualItem.getPropertyInt" href="#-fontlab.flVisualItem.getPropertyInt"><span class="function-name">fontlab.flVisualItem.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flVisualItem.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flVisualItem.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.hasHistoryState" href="#-fontlab.flVisualItem.hasHistoryState"><span class="function-name">fontlab.flVisualItem.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flVisualItem.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.haveCanvas"></a>

## `haveCanvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.haveCanvas" href="#-fontlab.flVisualItem.haveCanvas"><span class="function-name">fontlab.flVisualItem.haveCanvas</span></a> = haveCanvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveCanvas()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.haveEditor"></a>

## `haveEditor`


<dl class="function"><dt><a name="-fontlab.flVisualItem.haveEditor" href="#-fontlab.flVisualItem.haveEditor"><span class="function-name">fontlab.flVisualItem.haveEditor</span></a> = haveEditor<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveEditor(QPointF canvas_pos)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flVisualItem.haveObject" href="#-fontlab.flVisualItem.haveObject"><span class="function-name">fontlab.flVisualItem.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flVisualItem.hide"></a>

## `hide`


<dl class="function"><dt><a name="-fontlab.flVisualItem.hide" href="#-fontlab.flVisualItem.hide"><span class="function-name">fontlab.flVisualItem.hide</span></a> = hide<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hide()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flVisualItem.historyStates" href="#-fontlab.flVisualItem.historyStates"><span class="function-name">fontlab.flVisualItem.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.hovered"></a>

## `hovered`


<dl class="descriptor"><dt>fontlab.flVisualItem.hovered</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flVisualItem.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flVisualItem.independedAll" href="#-fontlab.flVisualItem.independedAll"><span class="function-name">fontlab.flVisualItem.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.initialHistoryState" href="#-fontlab.flVisualItem.initialHistoryState"><span class="function-name">fontlab.flVisualItem.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.instanceAcceptEvents"></a>

## `instanceAcceptEvents`


<dl class="function"><dt><a name="-fontlab.flVisualItem.instanceAcceptEvents" href="#-fontlab.flVisualItem.instanceAcceptEvents"><span class="function-name">fontlab.flVisualItem.instanceAcceptEvents</span></a> = instanceAcceptEvents<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceAcceptEvents()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flVisualItem.instanceType" href="#-fontlab.flVisualItem.instanceType"><span class="function-name">fontlab.flVisualItem.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flVisualItem.invselect"></a>

## `invselect`


<dl class="function"><dt><a name="-fontlab.flVisualItem.invselect" href="#-fontlab.flVisualItem.invselect"><span class="function-name">fontlab.flVisualItem.invselect</span></a> = invselect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">invselect()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flVisualItem.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flVisualItem.isEqual" href="#-fontlab.flVisualItem.isEqual"><span class="function-name">fontlab.flVisualItem.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flVisualItem.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flVisualItem.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flVisualItem.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.isSelectable"></a>

## `isSelectable`


<dl class="function"><dt><a name="-fontlab.flVisualItem.isSelectable" href="#-fontlab.flVisualItem.isSelectable"><span class="function-name">fontlab.flVisualItem.isSelectable</span></a> = isSelectable<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isSelectable()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.isStableSelect"></a>

## `isStableSelect`


<dl class="function"><dt><a name="-fontlab.flVisualItem.isStableSelect" href="#-fontlab.flVisualItem.isStableSelect"><span class="function-name">fontlab.flVisualItem.isStableSelect</span></a> = isStableSelect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isStableSelect()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.isValid"></a>

## `isValid`


<dl class="descriptor"><dt>fontlab.flVisualItem.isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.itemScale"></a>

## `itemScale`


<dl class="function"><dt><a name="-fontlab.flVisualItem.itemScale" href="#-fontlab.flVisualItem.itemScale"><span class="function-name">fontlab.flVisualItem.itemScale</span></a> = itemScale<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double itemScale()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.Listeners"></a>

## `Listeners`


<span class="other-name">fontlab.flVisualItem.Listeners</span> = {'ClickListener': 8, 'DragListener': 4, 'HoverListener': 1, 'MoveListener': 2}


<a name="fontlab.flVisualItem.locked"></a>

## `locked`


<dl class="descriptor"><dt>fontlab.flVisualItem.locked</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.mapCanvasDistanceToItem"></a>

## `mapCanvasDistanceToItem`


<dl class="function"><dt><a name="-fontlab.flVisualItem.mapCanvasDistanceToItem" href="#-fontlab.flVisualItem.mapCanvasDistanceToItem"><span class="function-name">fontlab.flVisualItem.mapCanvasDistanceToItem</span></a> = mapCanvasDistanceToItem<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF mapCanvasDistanceToItem(QPointF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.mapCanvasToItem"></a>

## `mapCanvasToItem`


<dl class="function"><dt><a name="-fontlab.flVisualItem.mapCanvasToItem" href="#-fontlab.flVisualItem.mapCanvasToItem"><span class="function-name">fontlab.flVisualItem.mapCanvasToItem</span></a> = mapCanvasToItem<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | QRectF mapCanvasToItem(QPointF | QRectF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.mapItemToCanvas"></a>

## `mapItemToCanvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.mapItemToCanvas" href="#-fontlab.flVisualItem.mapItemToCanvas"><span class="function-name">fontlab.flVisualItem.mapItemToCanvas</span></a> = mapItemToCanvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF | QRectF mapItemToCanvas(QPointF | QRectF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.metricStep"></a>

## `metricStep`


<dl class="function"><dt><a name="-fontlab.flVisualItem.metricStep" href="#-fontlab.flVisualItem.metricStep"><span class="function-name">fontlab.flVisualItem.metricStep</span></a> = metricStep<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double metricStep()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.move"></a>

## `move`


<dl class="function"><dt><a name="-fontlab.flVisualItem.move" href="#-fontlab.flVisualItem.move"><span class="function-name">fontlab.flVisualItem.move</span></a> = move<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void move(QPointF)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flVisualItem.name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.opacity"></a>

## `opacity`


<dl class="descriptor"><dt>fontlab.flVisualItem.opacity</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.owner"></a>

## `owner`


<dl class="descriptor"><dt>fontlab.flVisualItem.owner</dt>
<dd>

<pre class="doc" markdown="0">flVisualItem</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.paint"></a>

## `paint`


<dl class="function"><dt><a name="-fontlab.flVisualItem.paint" href="#-fontlab.flVisualItem.paint"><span class="function-name">fontlab.flVisualItem.paint</span></a> = paint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void paint(QPainter*)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.preview"></a>

## `preview`


<dl class="function"><dt><a name="-fontlab.flVisualItem.preview" href="#-fontlab.flVisualItem.preview"><span class="function-name">fontlab.flVisualItem.preview</span></a> = preview<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">preview()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flVisualItem.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.referencePoint"></a>

## `referencePoint`


<dl class="function"><dt><a name="-fontlab.flVisualItem.referencePoint" href="#-fontlab.flVisualItem.referencePoint"><span class="function-name">fontlab.flVisualItem.referencePoint</span></a> = referencePoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF referencePoint()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flVisualItem.release" href="#-fontlab.flVisualItem.release"><span class="function-name">fontlab.flVisualItem.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flVisualItem.remove" href="#-fontlab.flVisualItem.remove"><span class="function-name">fontlab.flVisualItem.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flVisualItem.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flVisualItem.removeChild" href="#-fontlab.flVisualItem.removeChild"><span class="function-name">fontlab.flVisualItem.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.removeDecorator"></a>

## `removeDecorator`


<dl class="function"><dt><a name="-fontlab.flVisualItem.removeDecorator" href="#-fontlab.flVisualItem.removeDecorator"><span class="function-name">fontlab.flVisualItem.removeDecorator</span></a> = removeDecorator<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void removeDecorator(flVisualItem)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.removedFromCanvas"></a>

## `removedFromCanvas`


<dl class="function"><dt><a name="-fontlab.flVisualItem.removedFromCanvas" href="#-fontlab.flVisualItem.removedFromCanvas"><span class="function-name">fontlab.flVisualItem.removedFromCanvas</span></a> = removedFromCanvas<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removedFromCanvas()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.removeItem"></a>

## `removeItem`


<dl class="function"><dt><a name="-fontlab.flVisualItem.removeItem" href="#-fontlab.flVisualItem.removeItem"><span class="function-name">fontlab.flVisualItem.removeItem</span></a> = removeItem<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void removeItem(flVisualItem)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flVisualItem.removeProperty" href="#-fontlab.flVisualItem.removeProperty"><span class="function-name">fontlab.flVisualItem.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flVisualItem.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flVisualItem.restoreHistoryState" href="#-fontlab.flVisualItem.restoreHistoryState"><span class="function-name">fontlab.flVisualItem.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flVisualItem.select"></a>

## `select`


<dl class="function"><dt><a name="-fontlab.flVisualItem.select" href="#-fontlab.flVisualItem.select"><span class="function-name">fontlab.flVisualItem.select</span></a> = select<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">select()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.selected"></a>

## `selected`


<dl class="descriptor"><dt>fontlab.flVisualItem.selected</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flVisualItem.setFlag" href="#-fontlab.flVisualItem.setFlag"><span class="function-name">fontlab.flVisualItem.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flVisualItem.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flVisualItem.setProperty" href="#-fontlab.flVisualItem.setProperty"><span class="function-name">fontlab.flVisualItem.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flVisualItem.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flVisualItem.setPropertyFloat" href="#-fontlab.flVisualItem.setPropertyFloat"><span class="function-name">fontlab.flVisualItem.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flVisualItem.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flVisualItem.setPropertyInt" href="#-fontlab.flVisualItem.setPropertyInt"><span class="function-name">fontlab.flVisualItem.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flVisualItem.show"></a>

## `show`


<dl class="function"><dt><a name="-fontlab.flVisualItem.show" href="#-fontlab.flVisualItem.show"><span class="function-name">fontlab.flVisualItem.show</span></a> = show<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">show()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flVisualItem.tag" href="#-fontlab.flVisualItem.tag"><span class="function-name">fontlab.flVisualItem.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flVisualItem.transform"></a>

## `transform`


<dl class="descriptor"><dt>fontlab.flVisualItem.transform</dt>
<dd>

<pre class="doc" markdown="0">QTransform</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flVisualItem.type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>



<a name="fontlab.flVisualItem.unselect"></a>

## `unselect`


<dl class="function"><dt><a name="-fontlab.flVisualItem.unselect" href="#-fontlab.flVisualItem.unselect"><span class="function-name">fontlab.flVisualItem.unselect</span></a> = unselect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">unselect()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flVisualItem.update" href="#-fontlab.flVisualItem.update"><span class="function-name">fontlab.flVisualItem.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>



<a name="fontlab.flVisualItem.visible"></a>

## `visible`


<dl class="descriptor"><dt>fontlab.flVisualItem.visible</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>

