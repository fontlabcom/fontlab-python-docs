

<a name="fontlab.flNode"></a>

# `flNode`


<dt class="class"><h2><span class="class-name">fontlab.flNode</span> = <a name="fontlab.flNode" href="#fontlab.flNode">class flNode</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flNode representation

Constructors:
  flNode()
  flNode(Node) - make clone
  flNode(QPointF position[, string nodeType="on"[, int nodeKind=None]])
  flNode(double x, double y[, string nodeType="on"[, int nodeKind=None]])</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flNode-__delattr__" href="#flNode-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__eq__" href="#flNode-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__ge__" href="#flNode-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__getattribute__" href="#flNode-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__gt__" href="#flNode-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__init__" href="#flNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flNode-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__le__" href="#flNode-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__lt__" href="#flNode-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__ne__" href="#flNode-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__repr__" href="#flNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-__setattr__" href="#flNode-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flNode-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-angleTo" href="#flNode-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flNode-angleTo">angleTo</a>(QPointF p)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-applyTransform" href="#flNode-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-applyTransform">applyTransform</a>(QTransform)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-canBeHobby" href="#flNode-canBeHobby"><span class="function-name">canBeHobby</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-canBeHobby">canBeHobby</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-canBeSmooth" href="#flNode-canBeSmooth"><span class="function-name">canBeSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-canBeSmooth">canBeSmooth</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-canCollapse" href="#flNode-canCollapse"><span class="function-name">canCollapse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-canCollapse">canCollapse</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-canImprove" href="#flNode-canImprove"><span class="function-name">canImprove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-canImprove">canImprove</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-changed" href="#flNode-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-checkInitHistoryState" href="#flNode-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-checkVectors" href="#flNode-checkVectors"><span class="function-name">checkVectors</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-checkVectors">checkVectors</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-clearAboveHistory" href="#flNode-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-clearFlag" href="#flNode-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-clearFlags" href="#flNode-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-clearStored" href="#flNode-clearStored"><span class="function-name">clearStored</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-clearStored">clearStored</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-clone" href="#flNode-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-cloneMapped" href="#flNode-cloneMapped"><span class="function-name">cloneMapped</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flNode-cloneMapped">cloneMapped</a>(QTransform)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-collapseHandles" href="#flNode-collapseHandles"><span class="function-name">collapseHandles</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-collapseHandles">collapseHandles</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-convertToCurve" href="#flNode-convertToCurve"><span class="function-name">convertToCurve</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-convertToCurve">convertToCurve</a>([bool smooth = false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-convertToCurves" href="#flNode-convertToCurves"><span class="function-name">convertToCurves</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-convertToCurves">convertToCurves</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-convertToLine" href="#flNode-convertToLine"><span class="function-name">convertToLine</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-convertToLine">convertToLine</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-copyFrom" href="#flNode-copyFrom"><span class="function-name">copyFrom</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-copyFrom">copyFrom</a>(Node[, withSelected=False])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-createHistoryState" href="#flNode-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-currentHistoryState" href="#flNode-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-distanceTo" href="#flNode-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flNode-distanceTo">distanceTo</a>(Node/QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-flag" href="#flNode-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getLines" href="#flNode-getLines"><span class="function-name">getLines</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(QLineF, QLineF)/None <a href="#fontlab.flNode-getLines">getLines</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getOn" href="#flNode-getOn"><span class="function-name">getOn</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None <a href="#fontlab.flNode-getOn">getOn</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getProperties" href="#flNode-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getProperty" href="#flNode-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getPropertyFloat" href="#flNode-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-getPropertyInt" href="#flNode-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-hasHistoryState" href="#flNode-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-historyStates" href="#flNode-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-improve" href="#flNode-improve"><span class="function-name">improve</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-improve">improve</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-independedAll" href="#flNode-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-initialHistoryState" href="#flNode-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isCorner" href="#flNode-isCorner"><span class="function-name">isCorner</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isCorner">isCorner</a>([double a = 10.])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isCurve" href="#flNode-isCurve"><span class="function-name">isCurve</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isCurve">isCurve</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isEqual" href="#flNode-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isEqualTo" href="#flNode-isEqualTo"><span class="function-name">isEqualTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isEqualTo">isEqualTo</a>(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isExtreme" href="#flNode-isExtreme"><span class="function-name">isExtreme</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isExtreme">isExtreme</a>(bool x[, bool open = true[, double limit = 0]])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isFirst" href="#flNode-isFirst"><span class="function-name">isFirst</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isFirst">isFirst</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isG2" href="#flNode-isG2"><span class="function-name">isG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isG2">isG2</a>(double tolerance)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isInternal" href="#flNode-isInternal"><span class="function-name">isInternal</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isInternal">isInternal</a>(bool clockwise)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isInterpolated" href="#flNode-isInterpolated"><span class="function-name">isInterpolated</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isInterpolated">isInterpolated</a>(bool x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isLast" href="#flNode-isLast"><span class="function-name">isLast</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isLast">isLast</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isOff" href="#flNode-isOff"><span class="function-name">isOff</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isOff">isOff</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isOn" href="#flNode-isOn"><span class="function-name">isOn</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isOn">isOn</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-isSmartAngle" href="#flNode-isSmartAngle"><span class="function-name">isSmartAngle</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-isSmartAngle">isSmartAngle</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-makeStart" href="#flNode-makeStart"><span class="function-name">makeStart</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-makeStart">makeStart</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-moveBy" href="#flNode-moveBy"><span class="function-name">moveBy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-moveBy">moveBy</a>(float dx, float dy[, bool round=false]</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-nextNode" href="#flNode-nextNode"><span class="function-name">nextNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None <a href="#fontlab.flNode-nextNode">nextNode</a>([string nodeType= [, int searchDepth=1]])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-pointG2" href="#flNode-pointG2"><span class="function-name">pointG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/None <a href="#fontlab.flNode-pointG2">pointG2</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-prevNode" href="#flNode-prevNode"><span class="function-name">prevNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None <a href="#fontlab.flNode-prevNode">prevNode</a>([string nodeType= [, int searchDepth=1]])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-release" href="#flNode-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-remove" href="#flNode-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-removeChild" href="#flNode-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-removeProperty" href="#flNode-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-restoreCoordinates" href="#flNode-restoreCoordinates"><span class="function-name">restoreCoordinates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-restoreCoordinates">restoreCoordinates</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-restoreHistoryState" href="#flNode-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-rotateBy" href="#flNode-rotateBy"><span class="function-name">rotateBy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-rotateBy">rotateBy</a>(valueDegree[, QPointF origin=(0, 0)])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-round" href="#flNode-round"><span class="function-name">round</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-round">round</a>() - Round the node's coordinate</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-scaleBy" href="#flNode-scaleBy"><span class="function-name">scaleBy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-scaleBy">scaleBy</a>(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setExtraLast" href="#flNode-setExtraLast"><span class="function-name">setExtraLast</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setExtraLast">setExtraLast</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setFlag" href="#flNode-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setNextSmooth" href="#flNode-setNextSmooth"><span class="function-name">setNextSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setNextSmooth">setNextSmooth</a>(QPointF base)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setPrevSmooth" href="#flNode-setPrevSmooth"><span class="function-name">setPrevSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setPrevSmooth">setPrevSmooth</a>(QPointF base)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setProperty" href="#flNode-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setPropertyFloat" href="#flNode-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setPropertyInt" href="#flNode-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setSmartAngleEnbl" href="#flNode-setSmartAngleEnbl"><span class="function-name">setSmartAngleEnbl</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-setSmartAngleEnbl">setSmartAngleEnbl</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-setSmartSharp" href="#flNode-setSmartSharp"><span class="function-name">setSmartSharp</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-setSmartSharp">setSmartSharp</a>([double tension = 0.6])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-skewBy" href="#flNode-skewBy"><span class="function-name">skewBy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-skewBy">skewBy</a>(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-smartMove" href="#flNode-smartMove"><span class="function-name">smartMove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(uint) <a href="#fontlab.flNode-smartMove">smartMove</a>(offset)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-smartSetXY" href="#flNode-smartSetXY"><span class="function-name">smartSetXY</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-smartSetXY">smartSetXY</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-storeCoordinates" href="#flNode-storeCoordinates"><span class="function-name">storeCoordinates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-storeCoordinates">storeCoordinates</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-storeTestParameters" href="#flNode-storeTestParameters"><span class="function-name">storeTestParameters</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-storeTestParameters">storeTestParameters</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-tag" href="#flNode-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-transformBy" href="#flNode-transformBy"><span class="function-name">transformBy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-transformBy">transformBy</a>(QTransform tx[, QPointF origin=(0, 0)])</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-update" href="#flNode-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-update">update</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-updateG2" href="#flNode-updateG2"><span class="function-name">updateG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-updateG2">updateG2</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-updateSmooth" href="#flNode-updateSmooth"><span class="function-name">updateSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flNode-updateSmooth">updateSmooth</a>([bool extended_neibh=true])</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flNode-cloneObject" href="#flNode-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flNode-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-createObject" href="#flNode-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flNode-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-haveObject" href="#flNode-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flNode-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flNode-instanceType" href="#flNode-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flNode-instanceType">instanceType</a>();</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>angle</dt>
<dd>

<pre class="doc" markdown="0">angle</pre>

</dd>
</dl>
<dl class="descriptor"><dt>contour</dt>
<dd>

<pre class="doc" markdown="0">The parent Contour or None if not present</pre>

</dd>
</dl>
<dl class="descriptor"><dt>g2</dt>
<dd>

<pre class="doc" markdown="0">g2</pre>

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
<dl class="descriptor"><dt>hobby</dt>
<dd>

<pre class="doc" markdown="0">hobby</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>
<dl class="descriptor"><dt>index</dt>
<dd>

<pre class="doc" markdown="0">The index of the node in parent's contour (if present, otherwise -1)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolated</dt>
<dd>

<pre class="doc" markdown="0">interpolated</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolatedX</dt>
<dd>

<pre class="doc" markdown="0">interpolatedX</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolatedY</dt>
<dd>

<pre class="doc" markdown="0">interpolatedY</pre>

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
<dl class="descriptor"><dt>isSelectedAlone</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isTerminal</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>nodeState</dt>
<dd>

<pre class="doc" markdown="0">nodeState</pre>

</dd>
</dl>
<dl class="descriptor"><dt>position</dt>
<dd>

<pre class="doc" markdown="0">Coordinates of the node as QPointF</pre>

</dd>
</dl>
<dl class="descriptor"><dt>preview</dt>
<dd>

<pre class="doc" markdown="0">preview</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>scv</dt>
<dd>

<pre class="doc" markdown="0">scv</pre>

</dd>
</dl>
<dl class="descriptor"><dt>selected</dt>
<dd>

<pre class="doc" markdown="0">The selected flag</pre>

</dd>
</dl>
<dl class="descriptor"><dt>smartAngleR</dt>
<dd>

<pre class="doc" markdown="0">smartAngleR</pre>

</dd>
</dl>
<dl class="descriptor"><dt>smooth</dt>
<dd>

<pre class="doc" markdown="0">The smooth flag</pre>

</dd>
</dl>
<dl class="descriptor"><dt>state</dt>
<dd>

<pre class="doc" markdown="0">state</pre>

</dd>
</dl>
<dl class="descriptor"><dt>type</dt>
<dd>

<pre class="doc" markdown="0">The node type</pre>

</dd>
</dl>
<dl class="descriptor"><dt>x</dt>
<dd>

<pre class="doc" markdown="0">The x coordinate of the node</pre>

</dd>
</dl>
<dl class="descriptor"><dt>y</dt>
<dd>

<pre class="doc" markdown="0">The y coordinate of the node</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">NodeKind</span> = {'ExtraLast': 16384, 'First': 16, 'G2': 4096, 'Hobby': 8192, 'HotSpot': 2048, 'InterpolatedX': 256, 'InterpolatedY': 512, 'KindMask': 65535, 'None': 0, 'Preview': 64, ...}</dt></dl>
<dl><dt><span class="other-name">NodeType</span> = {'AnyNodeMask': 7, 'Curve': 4, 'Off': 2, 'On': 1}</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flNode-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flNode.angle"></a>

## `angle`


<dl class="descriptor"><dt>fontlab.flNode.angle</dt>
<dd>

<pre class="doc" markdown="0">angle</pre>

</dd>
</dl>



<a name="fontlab.flNode.angleTo"></a>

## `angleTo`


<dl class="function"><dt><a name="-fontlab.flNode.angleTo" href="#-fontlab.flNode.angleTo"><span class="function-name">fontlab.flNode.angleTo</span></a> = angleTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double angleTo(QPointF p)</pre>

</dd></dl>



<a name="fontlab.flNode.applyTransform"></a>

## `applyTransform`


<dl class="function"><dt><a name="-fontlab.flNode.applyTransform" href="#-fontlab.flNode.applyTransform"><span class="function-name">fontlab.flNode.applyTransform</span></a> = applyTransform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">applyTransform(QTransform)</pre>

</dd></dl>



<a name="fontlab.flNode.canBeHobby"></a>

## `canBeHobby`


<dl class="function"><dt><a name="-fontlab.flNode.canBeHobby" href="#-fontlab.flNode.canBeHobby"><span class="function-name">fontlab.flNode.canBeHobby</span></a> = canBeHobby<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool canBeHobby()</pre>

</dd></dl>



<a name="fontlab.flNode.canBeSmooth"></a>

## `canBeSmooth`


<dl class="function"><dt><a name="-fontlab.flNode.canBeSmooth" href="#-fontlab.flNode.canBeSmooth"><span class="function-name">fontlab.flNode.canBeSmooth</span></a> = canBeSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool canBeSmooth()</pre>

</dd></dl>



<a name="fontlab.flNode.canCollapse"></a>

## `canCollapse`


<dl class="function"><dt><a name="-fontlab.flNode.canCollapse" href="#-fontlab.flNode.canCollapse"><span class="function-name">fontlab.flNode.canCollapse</span></a> = canCollapse<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool canCollapse()</pre>

</dd></dl>



<a name="fontlab.flNode.canImprove"></a>

## `canImprove`


<dl class="function"><dt><a name="-fontlab.flNode.canImprove" href="#-fontlab.flNode.canImprove"><span class="function-name">fontlab.flNode.canImprove</span></a> = canImprove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool canImprove()</pre>

</dd></dl>



<a name="fontlab.flNode.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flNode.changed" href="#-fontlab.flNode.changed"><span class="function-name">fontlab.flNode.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flNode.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.checkInitHistoryState" href="#-fontlab.flNode.checkInitHistoryState"><span class="function-name">fontlab.flNode.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNode.checkVectors"></a>

## `checkVectors`


<dl class="function"><dt><a name="-fontlab.flNode.checkVectors" href="#-fontlab.flNode.checkVectors"><span class="function-name">fontlab.flNode.checkVectors</span></a> = checkVectors<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool checkVectors()</pre>

</dd></dl>



<a name="fontlab.flNode.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flNode.clearAboveHistory" href="#-fontlab.flNode.clearAboveHistory"><span class="function-name">fontlab.flNode.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNode.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flNode.clearFlag" href="#-fontlab.flNode.clearFlag"><span class="function-name">fontlab.flNode.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flNode.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flNode.clearFlags" href="#-fontlab.flNode.clearFlags"><span class="function-name">fontlab.flNode.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flNode.clearStored"></a>

## `clearStored`


<dl class="function"><dt><a name="-fontlab.flNode.clearStored" href="#-fontlab.flNode.clearStored"><span class="function-name">fontlab.flNode.clearStored</span></a> = clearStored<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearStored()</pre>

</dd></dl>



<a name="fontlab.flNode.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flNode.clone" href="#-fontlab.flNode.clone"><span class="function-name">fontlab.flNode.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flNode.cloneMapped"></a>

## `cloneMapped`


<dl class="function"><dt><a name="-fontlab.flNode.cloneMapped" href="#-fontlab.flNode.cloneMapped"><span class="function-name">fontlab.flNode.cloneMapped</span></a> = cloneMapped<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode cloneMapped(QTransform)</pre>

</dd></dl>



<a name="fontlab.flNode.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flNode.cloneObject" href="#-fontlab.flNode.cloneObject"><span class="function-name">fontlab.flNode.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flNode.collapseHandles"></a>

## `collapseHandles`


<dl class="function"><dt><a name="-fontlab.flNode.collapseHandles" href="#-fontlab.flNode.collapseHandles"><span class="function-name">fontlab.flNode.collapseHandles</span></a> = collapseHandles<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool collapseHandles()</pre>

</dd></dl>



<a name="fontlab.flNode.contour"></a>

## `contour`


<dl class="descriptor"><dt>fontlab.flNode.contour</dt>
<dd>

<pre class="doc" markdown="0">The parent Contour or None if not present</pre>

</dd>
</dl>



<a name="fontlab.flNode.convertToCurve"></a>

## `convertToCurve`


<dl class="function"><dt><a name="-fontlab.flNode.convertToCurve" href="#-fontlab.flNode.convertToCurve"><span class="function-name">fontlab.flNode.convertToCurve</span></a> = convertToCurve<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool convertToCurve([bool smooth = false])</pre>

</dd></dl>



<a name="fontlab.flNode.convertToCurves"></a>

## `convertToCurves`


<dl class="function"><dt><a name="-fontlab.flNode.convertToCurves" href="#-fontlab.flNode.convertToCurves"><span class="function-name">fontlab.flNode.convertToCurves</span></a> = convertToCurves<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool convertToCurves()</pre>

</dd></dl>



<a name="fontlab.flNode.convertToLine"></a>

## `convertToLine`


<dl class="function"><dt><a name="-fontlab.flNode.convertToLine" href="#-fontlab.flNode.convertToLine"><span class="function-name">fontlab.flNode.convertToLine</span></a> = convertToLine<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool convertToLine()</pre>

</dd></dl>



<a name="fontlab.flNode.copyFrom"></a>

## `copyFrom`


<dl class="function"><dt><a name="-fontlab.flNode.copyFrom" href="#-fontlab.flNode.copyFrom"><span class="function-name">fontlab.flNode.copyFrom</span></a> = copyFrom<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">copyFrom(Node[, withSelected=False])</pre>

</dd></dl>



<a name="fontlab.flNode.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.createHistoryState" href="#-fontlab.flNode.createHistoryState"><span class="function-name">fontlab.flNode.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNode.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flNode.createObject" href="#-fontlab.flNode.createObject"><span class="function-name">fontlab.flNode.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flNode.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.currentHistoryState" href="#-fontlab.flNode.currentHistoryState"><span class="function-name">fontlab.flNode.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flNode.distanceTo"></a>

## `distanceTo`


<dl class="function"><dt><a name="-fontlab.flNode.distanceTo" href="#-fontlab.flNode.distanceTo"><span class="function-name">fontlab.flNode.distanceTo</span></a> = distanceTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double distanceTo(Node/QPointF)</pre>

</dd></dl>



<a name="fontlab.flNode.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flNode.flag" href="#-fontlab.flNode.flag"><span class="function-name">fontlab.flNode.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flNode.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flNode.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flNode.g2"></a>

## `g2`


<dl class="descriptor"><dt>fontlab.flNode.g2</dt>
<dd>

<pre class="doc" markdown="0">g2</pre>

</dd>
</dl>



<a name="fontlab.flNode.getLines"></a>

## `getLines`


<dl class="function"><dt><a name="-fontlab.flNode.getLines" href="#-fontlab.flNode.getLines"><span class="function-name">fontlab.flNode.getLines</span></a> = getLines<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(QLineF, QLineF)/None getLines()</pre>

</dd></dl>



<a name="fontlab.flNode.getOn"></a>

## `getOn`


<dl class="function"><dt><a name="-fontlab.flNode.getOn" href="#-fontlab.flNode.getOn"><span class="function-name">fontlab.flNode.getOn</span></a> = getOn<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None getOn()</pre>

</dd></dl>



<a name="fontlab.flNode.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flNode.getProperties" href="#-fontlab.flNode.getProperties"><span class="function-name">fontlab.flNode.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flNode.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flNode.getProperty" href="#-fontlab.flNode.getProperty"><span class="function-name">fontlab.flNode.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flNode.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flNode.getPropertyFloat" href="#-fontlab.flNode.getPropertyFloat"><span class="function-name">fontlab.flNode.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNode.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flNode.getPropertyInt" href="#-fontlab.flNode.getPropertyInt"><span class="function-name">fontlab.flNode.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNode.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flNode.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.hasHistoryState" href="#-fontlab.flNode.hasHistoryState"><span class="function-name">fontlab.flNode.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNode.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flNode.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flNode.haveObject" href="#-fontlab.flNode.haveObject"><span class="function-name">fontlab.flNode.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flNode.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flNode.historyStates" href="#-fontlab.flNode.historyStates"><span class="function-name">fontlab.flNode.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flNode.hobby"></a>

## `hobby`


<dl class="descriptor"><dt>fontlab.flNode.hobby</dt>
<dd>

<pre class="doc" markdown="0">hobby</pre>

</dd>
</dl>



<a name="fontlab.flNode.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flNode.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flNode.improve"></a>

## `improve`


<dl class="function"><dt><a name="-fontlab.flNode.improve" href="#-fontlab.flNode.improve"><span class="function-name">fontlab.flNode.improve</span></a> = improve<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool improve()</pre>

</dd></dl>



<a name="fontlab.flNode.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flNode.independedAll" href="#-fontlab.flNode.independedAll"><span class="function-name">fontlab.flNode.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flNode.index"></a>

## `index`


<dl class="descriptor"><dt>fontlab.flNode.index</dt>
<dd>

<pre class="doc" markdown="0">The index of the node in parent's contour (if present, otherwise -1)</pre>

</dd>
</dl>



<a name="fontlab.flNode.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.initialHistoryState" href="#-fontlab.flNode.initialHistoryState"><span class="function-name">fontlab.flNode.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flNode.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flNode.instanceType" href="#-fontlab.flNode.instanceType"><span class="function-name">fontlab.flNode.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flNode.interpolated"></a>

## `interpolated`


<dl class="descriptor"><dt>fontlab.flNode.interpolated</dt>
<dd>

<pre class="doc" markdown="0">interpolated</pre>

</dd>
</dl>



<a name="fontlab.flNode.interpolatedX"></a>

## `interpolatedX`


<dl class="descriptor"><dt>fontlab.flNode.interpolatedX</dt>
<dd>

<pre class="doc" markdown="0">interpolatedX</pre>

</dd>
</dl>



<a name="fontlab.flNode.interpolatedY"></a>

## `interpolatedY`


<dl class="descriptor"><dt>fontlab.flNode.interpolatedY</dt>
<dd>

<pre class="doc" markdown="0">interpolatedY</pre>

</dd>
</dl>



<a name="fontlab.flNode.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flNode.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isCorner"></a>

## `isCorner`


<dl class="function"><dt><a name="-fontlab.flNode.isCorner" href="#-fontlab.flNode.isCorner"><span class="function-name">fontlab.flNode.isCorner</span></a> = isCorner<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isCorner([double a = 10.])</pre>

</dd></dl>



<a name="fontlab.flNode.isCurve"></a>

## `isCurve`


<dl class="function"><dt><a name="-fontlab.flNode.isCurve" href="#-fontlab.flNode.isCurve"><span class="function-name">fontlab.flNode.isCurve</span></a> = isCurve<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isCurve()</pre>

</dd></dl>



<a name="fontlab.flNode.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flNode.isEqual" href="#-fontlab.flNode.isEqual"><span class="function-name">fontlab.flNode.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flNode.isEqualTo"></a>

## `isEqualTo`


<dl class="function"><dt><a name="-fontlab.flNode.isEqualTo" href="#-fontlab.flNode.isEqualTo"><span class="function-name">fontlab.flNode.isEqualTo</span></a> = isEqualTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isEqualTo(Node[, tolerance=0.1[, offset=QPointF(0, 0)]])</pre>

</dd></dl>



<a name="fontlab.flNode.isExtreme"></a>

## `isExtreme`


<dl class="function"><dt><a name="-fontlab.flNode.isExtreme" href="#-fontlab.flNode.isExtreme"><span class="function-name">fontlab.flNode.isExtreme</span></a> = isExtreme<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isExtreme(bool x[, bool open = true[, double limit = 0]])</pre>

</dd></dl>



<a name="fontlab.flNode.isFirst"></a>

## `isFirst`


<dl class="function"><dt><a name="-fontlab.flNode.isFirst" href="#-fontlab.flNode.isFirst"><span class="function-name">fontlab.flNode.isFirst</span></a> = isFirst<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isFirst()</pre>

</dd></dl>



<a name="fontlab.flNode.isG2"></a>

## `isG2`


<dl class="function"><dt><a name="-fontlab.flNode.isG2" href="#-fontlab.flNode.isG2"><span class="function-name">fontlab.flNode.isG2</span></a> = isG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isG2(double tolerance)</pre>

</dd></dl>



<a name="fontlab.flNode.isInternal"></a>

## `isInternal`


<dl class="function"><dt><a name="-fontlab.flNode.isInternal" href="#-fontlab.flNode.isInternal"><span class="function-name">fontlab.flNode.isInternal</span></a> = isInternal<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isInternal(bool clockwise)</pre>

</dd></dl>



<a name="fontlab.flNode.isInterpolated"></a>

## `isInterpolated`


<dl class="function"><dt><a name="-fontlab.flNode.isInterpolated" href="#-fontlab.flNode.isInterpolated"><span class="function-name">fontlab.flNode.isInterpolated</span></a> = isInterpolated<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isInterpolated(bool x)</pre>

</dd></dl>



<a name="fontlab.flNode.isLast"></a>

## `isLast`


<dl class="function"><dt><a name="-fontlab.flNode.isLast" href="#-fontlab.flNode.isLast"><span class="function-name">fontlab.flNode.isLast</span></a> = isLast<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isLast()</pre>

</dd></dl>



<a name="fontlab.flNode.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flNode.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isOff"></a>

## `isOff`


<dl class="function"><dt><a name="-fontlab.flNode.isOff" href="#-fontlab.flNode.isOff"><span class="function-name">fontlab.flNode.isOff</span></a> = isOff<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isOff()</pre>

</dd></dl>



<a name="fontlab.flNode.isOn"></a>

## `isOn`


<dl class="function"><dt><a name="-fontlab.flNode.isOn" href="#-fontlab.flNode.isOn"><span class="function-name">fontlab.flNode.isOn</span></a> = isOn<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isOn()</pre>

</dd></dl>



<a name="fontlab.flNode.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flNode.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flNode.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isSelectedAlone"></a>

## `isSelectedAlone`


<dl class="descriptor"><dt>fontlab.flNode.isSelectedAlone</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isSmartAngle"></a>

## `isSmartAngle`


<dl class="function"><dt><a name="-fontlab.flNode.isSmartAngle" href="#-fontlab.flNode.isSmartAngle"><span class="function-name">fontlab.flNode.isSmartAngle</span></a> = isSmartAngle<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isSmartAngle()</pre>

</dd></dl>



<a name="fontlab.flNode.isTerminal"></a>

## `isTerminal`


<dl class="descriptor"><dt>fontlab.flNode.isTerminal</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.isValid"></a>

## `isValid`


<dl class="descriptor"><dt>fontlab.flNode.isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flNode.makeStart"></a>

## `makeStart`


<dl class="function"><dt><a name="-fontlab.flNode.makeStart" href="#-fontlab.flNode.makeStart"><span class="function-name">fontlab.flNode.makeStart</span></a> = makeStart<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool makeStart()</pre>

</dd></dl>



<a name="fontlab.flNode.moveBy"></a>

## `moveBy`


<dl class="function"><dt><a name="-fontlab.flNode.moveBy" href="#-fontlab.flNode.moveBy"><span class="function-name">fontlab.flNode.moveBy</span></a> = moveBy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">moveBy(float dx, float dy[, bool round=false]</pre>

</dd></dl>



<a name="fontlab.flNode.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flNode.name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>



<a name="fontlab.flNode.nextNode"></a>

## `nextNode`


<dl class="function"><dt><a name="-fontlab.flNode.nextNode" href="#-fontlab.flNode.nextNode"><span class="function-name">fontlab.flNode.nextNode</span></a> = nextNode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None nextNode([string nodeType= [, int searchDepth=1]])</pre>

</dd></dl>



<a name="fontlab.flNode.NodeKind"></a>

## `NodeKind`


<span class="other-name">fontlab.flNode.NodeKind</span> = {'ExtraLast': 16384, 'First': 16, 'G2': 4096, 'Hobby': 8192, 'HotSpot': 2048, 'InterpolatedX': 256, 'InterpolatedY': 512, 'KindMask': 65535, 'None': 0, 'Preview': 64, ...}


<a name="fontlab.flNode.nodeState"></a>

## `nodeState`


<dl class="descriptor"><dt>fontlab.flNode.nodeState</dt>
<dd>

<pre class="doc" markdown="0">nodeState</pre>

</dd>
</dl>



<a name="fontlab.flNode.NodeType"></a>

## `NodeType`


<span class="other-name">fontlab.flNode.NodeType</span> = {'AnyNodeMask': 7, 'Curve': 4, 'Off': 2, 'On': 1}


<a name="fontlab.flNode.pointG2"></a>

## `pointG2`


<dl class="function"><dt><a name="-fontlab.flNode.pointG2" href="#-fontlab.flNode.pointG2"><span class="function-name">fontlab.flNode.pointG2</span></a> = pointG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/None pointG2()</pre>

</dd></dl>



<a name="fontlab.flNode.position"></a>

## `position`


<dl class="descriptor"><dt>fontlab.flNode.position</dt>
<dd>

<pre class="doc" markdown="0">Coordinates of the node as QPointF</pre>

</dd>
</dl>



<a name="fontlab.flNode.preview"></a>

## `preview`


<dl class="descriptor"><dt>fontlab.flNode.preview</dt>
<dd>

<pre class="doc" markdown="0">preview</pre>

</dd>
</dl>



<a name="fontlab.flNode.prevNode"></a>

## `prevNode`


<dl class="function"><dt><a name="-fontlab.flNode.prevNode" href="#-fontlab.flNode.prevNode"><span class="function-name">fontlab.flNode.prevNode</span></a> = prevNode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Node/None prevNode([string nodeType= [, int searchDepth=1]])</pre>

</dd></dl>



<a name="fontlab.flNode.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flNode.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flNode.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flNode.release" href="#-fontlab.flNode.release"><span class="function-name">fontlab.flNode.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flNode.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flNode.remove" href="#-fontlab.flNode.remove"><span class="function-name">fontlab.flNode.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flNode.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flNode.removeChild" href="#-fontlab.flNode.removeChild"><span class="function-name">fontlab.flNode.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flNode.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flNode.removeProperty" href="#-fontlab.flNode.removeProperty"><span class="function-name">fontlab.flNode.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flNode.restoreCoordinates"></a>

## `restoreCoordinates`


<dl class="function"><dt><a name="-fontlab.flNode.restoreCoordinates" href="#-fontlab.flNode.restoreCoordinates"><span class="function-name">fontlab.flNode.restoreCoordinates</span></a> = restoreCoordinates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreCoordinates()</pre>

</dd></dl>



<a name="fontlab.flNode.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flNode.restoreHistoryState" href="#-fontlab.flNode.restoreHistoryState"><span class="function-name">fontlab.flNode.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flNode.rotateBy"></a>

## `rotateBy`


<dl class="function"><dt><a name="-fontlab.flNode.rotateBy" href="#-fontlab.flNode.rotateBy"><span class="function-name">fontlab.flNode.rotateBy</span></a> = rotateBy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">rotateBy(valueDegree[, QPointF origin=(0, 0)])</pre>

</dd></dl>



<a name="fontlab.flNode.round"></a>

## `round`


<dl class="function"><dt><a name="-fontlab.flNode.round" href="#-fontlab.flNode.round"><span class="function-name">fontlab.flNode.round</span></a> = round<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">round() - Round the node's coordinate</pre>

</dd></dl>



<a name="fontlab.flNode.scaleBy"></a>

## `scaleBy`


<dl class="function"><dt><a name="-fontlab.flNode.scaleBy" href="#-fontlab.flNode.scaleBy"><span class="function-name">fontlab.flNode.scaleBy</span></a> = scaleBy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">scaleBy(valueXY | (valueX, valueY)[, QPointF origin=(0, 0)])</pre>

</dd></dl>



<a name="fontlab.flNode.scv"></a>

## `scv`


<dl class="descriptor"><dt>fontlab.flNode.scv</dt>
<dd>

<pre class="doc" markdown="0">scv</pre>

</dd>
</dl>



<a name="fontlab.flNode.selected"></a>

## `selected`


<dl class="descriptor"><dt>fontlab.flNode.selected</dt>
<dd>

<pre class="doc" markdown="0">The selected flag</pre>

</dd>
</dl>



<a name="fontlab.flNode.setExtraLast"></a>

## `setExtraLast`


<dl class="function"><dt><a name="-fontlab.flNode.setExtraLast" href="#-fontlab.flNode.setExtraLast"><span class="function-name">fontlab.flNode.setExtraLast</span></a> = setExtraLast<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setExtraLast(bool)</pre>

</dd></dl>



<a name="fontlab.flNode.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flNode.setFlag" href="#-fontlab.flNode.setFlag"><span class="function-name">fontlab.flNode.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flNode.setNextSmooth"></a>

## `setNextSmooth`


<dl class="function"><dt><a name="-fontlab.flNode.setNextSmooth" href="#-fontlab.flNode.setNextSmooth"><span class="function-name">fontlab.flNode.setNextSmooth</span></a> = setNextSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setNextSmooth(QPointF base)</pre>

</dd></dl>



<a name="fontlab.flNode.setPrevSmooth"></a>

## `setPrevSmooth`


<dl class="function"><dt><a name="-fontlab.flNode.setPrevSmooth" href="#-fontlab.flNode.setPrevSmooth"><span class="function-name">fontlab.flNode.setPrevSmooth</span></a> = setPrevSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPrevSmooth(QPointF base)</pre>

</dd></dl>



<a name="fontlab.flNode.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flNode.setProperty" href="#-fontlab.flNode.setProperty"><span class="function-name">fontlab.flNode.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flNode.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flNode.setPropertyFloat" href="#-fontlab.flNode.setPropertyFloat"><span class="function-name">fontlab.flNode.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNode.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flNode.setPropertyInt" href="#-fontlab.flNode.setPropertyInt"><span class="function-name">fontlab.flNode.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flNode.setSmartAngleEnbl"></a>

## `setSmartAngleEnbl`


<dl class="function"><dt><a name="-fontlab.flNode.setSmartAngleEnbl" href="#-fontlab.flNode.setSmartAngleEnbl"><span class="function-name">fontlab.flNode.setSmartAngleEnbl</span></a> = setSmartAngleEnbl<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setSmartAngleEnbl(bool)</pre>

</dd></dl>



<a name="fontlab.flNode.setSmartSharp"></a>

## `setSmartSharp`


<dl class="function"><dt><a name="-fontlab.flNode.setSmartSharp" href="#-fontlab.flNode.setSmartSharp"><span class="function-name">fontlab.flNode.setSmartSharp</span></a> = setSmartSharp<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setSmartSharp([double tension = 0.6])</pre>

</dd></dl>



<a name="fontlab.flNode.skewBy"></a>

## `skewBy`


<dl class="function"><dt><a name="-fontlab.flNode.skewBy" href="#-fontlab.flNode.skewBy"><span class="function-name">fontlab.flNode.skewBy</span></a> = skewBy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">skewBy(valueDegreeX | (valueDegreX, valueDegreY)[, QPointF origin=(0, 0)])</pre>

</dd></dl>



<a name="fontlab.flNode.smartAngleR"></a>

## `smartAngleR`


<dl class="descriptor"><dt>fontlab.flNode.smartAngleR</dt>
<dd>

<pre class="doc" markdown="0">smartAngleR</pre>

</dd>
</dl>



<a name="fontlab.flNode.smartMove"></a>

## `smartMove`


<dl class="function"><dt><a name="-fontlab.flNode.smartMove" href="#-fontlab.flNode.smartMove"><span class="function-name">fontlab.flNode.smartMove</span></a> = smartMove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(uint) smartMove(offset)</pre>

</dd></dl>



<a name="fontlab.flNode.smartSetXY"></a>

## `smartSetXY`


<dl class="function"><dt><a name="-fontlab.flNode.smartSetXY" href="#-fontlab.flNode.smartSetXY"><span class="function-name">fontlab.flNode.smartSetXY</span></a> = smartSetXY<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">smartSetXY(QPointF)</pre>

</dd></dl>



<a name="fontlab.flNode.smooth"></a>

## `smooth`


<dl class="descriptor"><dt>fontlab.flNode.smooth</dt>
<dd>

<pre class="doc" markdown="0">The smooth flag</pre>

</dd>
</dl>



<a name="fontlab.flNode.state"></a>

## `state`


<dl class="descriptor"><dt>fontlab.flNode.state</dt>
<dd>

<pre class="doc" markdown="0">state</pre>

</dd>
</dl>



<a name="fontlab.flNode.storeCoordinates"></a>

## `storeCoordinates`


<dl class="function"><dt><a name="-fontlab.flNode.storeCoordinates" href="#-fontlab.flNode.storeCoordinates"><span class="function-name">fontlab.flNode.storeCoordinates</span></a> = storeCoordinates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">storeCoordinates()</pre>

</dd></dl>



<a name="fontlab.flNode.storeTestParameters"></a>

## `storeTestParameters`


<dl class="function"><dt><a name="-fontlab.flNode.storeTestParameters" href="#-fontlab.flNode.storeTestParameters"><span class="function-name">fontlab.flNode.storeTestParameters</span></a> = storeTestParameters<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">storeTestParameters()</pre>

</dd></dl>



<a name="fontlab.flNode.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flNode.tag" href="#-fontlab.flNode.tag"><span class="function-name">fontlab.flNode.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flNode.transformBy"></a>

## `transformBy`


<dl class="function"><dt><a name="-fontlab.flNode.transformBy" href="#-fontlab.flNode.transformBy"><span class="function-name">fontlab.flNode.transformBy</span></a> = transformBy<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">transformBy(QTransform tx[, QPointF origin=(0, 0)])</pre>

</dd></dl>



<a name="fontlab.flNode.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flNode.type</dt>
<dd>

<pre class="doc" markdown="0">The node type</pre>

</dd>
</dl>



<a name="fontlab.flNode.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flNode.update" href="#-fontlab.flNode.update"><span class="function-name">fontlab.flNode.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>



<a name="fontlab.flNode.updateG2"></a>

## `updateG2`


<dl class="function"><dt><a name="-fontlab.flNode.updateG2" href="#-fontlab.flNode.updateG2"><span class="function-name">fontlab.flNode.updateG2</span></a> = updateG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool updateG2()</pre>

</dd></dl>



<a name="fontlab.flNode.updateSmooth"></a>

## `updateSmooth`


<dl class="function"><dt><a name="-fontlab.flNode.updateSmooth" href="#-fontlab.flNode.updateSmooth"><span class="function-name">fontlab.flNode.updateSmooth</span></a> = updateSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateSmooth([bool extended_neibh=true])</pre>

</dd></dl>



<a name="fontlab.flNode.x"></a>

## `x`


<dl class="descriptor"><dt>fontlab.flNode.x</dt>
<dd>

<pre class="doc" markdown="0">The x coordinate of the node</pre>

</dd>
</dl>



<a name="fontlab.flNode.y"></a>

## `y`


<dl class="descriptor"><dt>fontlab.flNode.y</dt>
<dd>

<pre class="doc" markdown="0">The y coordinate of the node</pre>

</dd>
</dl>

