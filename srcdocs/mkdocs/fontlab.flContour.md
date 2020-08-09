

<a name="fontlab.flContour"></a>

# `flContour`


<dt class="class"><h2><span class="class-name">fontlab.flContour</span> = <a name="fontlab.flContour" href="#fontlab.flContour">class flContour</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flContour representation

Constructors:
  flContour()
  flContour(flObject)
  flContour(flContour)
  flContour(fgContour)
  flContour(id)
  flContour(list(Node)[, bool closed=false])
  flContour(list(QPointF)[, flNode::NodeType=flNode::On[, bool closed=false]])
  flContour(QRectF)
  flContour(QLineF)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flContour-__delattr__" href="#flContour-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__eq__" href="#flContour-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__ge__" href="#flContour-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__getattribute__" href="#flContour-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__gt__" href="#flContour-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__init__" href="#flContour-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flContour-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__le__" href="#flContour-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__lt__" href="#flContour-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__ne__" href="#flContour-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__repr__" href="#flContour-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-__setattr__" href="#flContour-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flContour-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-add" href="#flContour-add"><span class="function-name">add</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-add">add</a>(flNode | QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-addInterval" href="#flContour-addInterval"><span class="function-name">addInterval</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-addInterval">addInterval</a>(Interval)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-addMarker" href="#flContour-addMarker"><span class="function-name">addMarker</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-addMarker">addMarker</a>( flContourMarker)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-addMarkers" href="#flContour-addMarkers"><span class="function-name">addMarkers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-addMarkers">addMarkers</a>( list(flContourMarker) )</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-append" href="#flContour-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-append">append</a>(list(flNode) | flContour)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-appendMapped" href="#flContour-appendMapped"><span class="function-name">appendMapped</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-appendMapped">appendMapped</a>(list(flNode) | flContour, QTransform)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-appendMarkers" href="#flContour-appendMarkers"><span class="function-name">appendMarkers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-appendMarkers">appendMarkers</a>(list(flContourMarker))</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-applyTransform" href="#flContour-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-applyTransform">applyTransform</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-assign" href="#flContour-assign"><span class="function-name">assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-assign">assign</a>(flContour | fgContour | list(flNode))</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-assignOwner" href="#flContour-assignOwner"><span class="function-name">assignOwner</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-assignOwner">assignOwner</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-at" href="#flContour-at"><span class="function-name">at</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-at">at</a>(int index)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-autoG2" href="#flContour-autoG2"><span class="function-name">autoG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-autoG2">autoG2</a>(float tolerance)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-beautify" href="#flContour-beautify"><span class="function-name">beautify</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-beautify">beautify</a>([int precision = 1])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-bindDependencies" href="#flContour-bindDependencies"><span class="function-name">bindDependencies</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-bindDependencies">bindDependencies</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-boundingBox" href="#flContour-boundingBox"><span class="function-name">boundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flContour-boundingBox">boundingBox</a>([QTransform])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-breakContour" href="#flContour-breakContour"><span class="function-name">breakContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flContour, flNode, flNode)/Nothing <a href="#fontlab.flContour-breakContour">breakContour</a>(flNode) | flContour/Nothing <a href="#fontlab.flContour-breakContour">breakContour</a>(int node_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-breakContourExpanded" href="#flContour-breakContourExpanded"><span class="function-name">breakContourExpanded</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour/Nothing <a href="#fontlab.flContour-breakContourExpanded">breakContourExpanded</a>(int node_ix | flNode [, float extrapolate_d]</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-calculate" href="#flContour-calculate"><span class="function-name">calculate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flContour-calculate">calculate</a>(float t[, QTransform tx])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-changed" href="#flContour-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-checkFa" href="#flContour-checkFa"><span class="function-name">checkFa</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(FaBasic) <a href="#fontlab.flContour-checkFa">checkFa</a>(list(int) tests)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-checkInitHistoryState" href="#flContour-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-checkSmooth" href="#flContour-checkSmooth"><span class="function-name">checkSmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-checkSmooth">checkSmooth</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearAboveHistory" href="#flContour-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearFlag" href="#flContour-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearFlags" href="#flContour-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearIntervals" href="#flContour-clearIntervals"><span class="function-name">clearIntervals</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearIntervals">clearIntervals</a>([uint key])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearMarkers" href="#flContour-clearMarkers"><span class="function-name">clearMarkers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearMarkers">clearMarkers</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clearNodes" href="#flContour-clearNodes"><span class="function-name">clearNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-clearNodes">clearNodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-clone" href="#flContour-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-cloneMapped" href="#flContour-cloneMapped"><span class="function-name">cloneMapped</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour <a href="#fontlab.flContour-cloneMapped">cloneMapped</a>(QTransform[, float ex_t0, float ex_t1])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-cloneMappedByT" href="#flContour-cloneMappedByT"><span class="function-name">cloneMappedByT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour <a href="#fontlab.flContour-cloneMappedByT">cloneMappedByT</a>(QTransform tx, float t0, float t1)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-cloneSelected" href="#flContour-cloneSelected"><span class="function-name">cloneSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flContour)/Nothing <a href="#fontlab.flContour-cloneSelected">cloneSelected</a>([QTransform, [bool ignore_alone=true]])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-compare" href="#flContour-compare"><span class="function-name">compare</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool result, QPointF offset) <a href="#fontlab.flContour-compare">compare</a>(flContour, float error)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-contains" href="#flContour-contains"><span class="function-name">contains</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-contains">contains</a>(flContour knife | QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertClToT" href="#flContour-convertClToT"><span class="function-name">convertClToT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-convertClToT">convertClToT</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertExToCl" href="#flContour-convertExToCl"><span class="function-name">convertExToCl</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-convertExToCl">convertExToCl</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertExToT" href="#flContour-convertExToT"><span class="function-name">convertExToT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-convertExToT">convertExToT</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertTTtoCurve" href="#flContour-convertTTtoCurve"><span class="function-name">convertTTtoCurve</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-convertTTtoCurve">convertTTtoCurve</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertToFgContour" href="#flContour-convertToFgContour"><span class="function-name">convertToFgContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour <a href="#fontlab.flContour-convertToFgContour">convertToFgContour</a>([QTransform tx])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertTtoCl" href="#flContour-convertTtoCl"><span class="function-name">convertTtoCl</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-convertTtoCl">convertTtoCl</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-convertTtoEx" href="#flContour-convertTtoEx"><span class="function-name">convertTtoEx</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-convertTtoEx">convertTtoEx</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-createHistoryState" href="#flContour-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-currentHistoryState" href="#flContour-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-curvature" href="#flContour-curvature"><span class="function-name">curvature</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float  <a href="#fontlab.flContour-curvature">curvature</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-derivative" href="#flContour-derivative"><span class="function-name">derivative</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flContour-derivative">derivative</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-distanceBetween" href="#flContour-distanceBetween"><span class="function-name">distanceBetween</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-distanceBetween">distanceBetween</a>(float t0, float t1[, float step =0.1])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-draw" href="#flContour-draw"><span class="function-name">draw</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-draw">draw</a>(pen) - Draw the contour’s outline data to the given type-pen</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-drawPoints" href="#flContour-drawPoints"><span class="function-name">drawPoints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-drawPoints">drawPoints</a>(point-pen) - Draw the contour’s outline data to the given type-point-pen</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-extrapolateFirst" href="#flContour-extrapolateFirst"><span class="function-name">extrapolateFirst</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-extrapolateFirst">extrapolateFirst</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-extrapolateLast" href="#flContour-extrapolateLast"><span class="function-name">extrapolateLast</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-extrapolateLast">extrapolateLast</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-fastAppend" href="#flContour-fastAppend"><span class="function-name">fastAppend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-fastAppend">fastAppend</a>( list(flNode) )</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-fastClone" href="#flContour-fastClone"><span class="function-name">fastClone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour <a href="#fontlab.flContour-fastClone">fastClone</a>(float ex_t0, float ex_t1)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-fastCloneByT" href="#flContour-fastCloneByT"><span class="function-name">fastCloneByT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour <a href="#fontlab.flContour-fastCloneByT">fastCloneByT</a>(float t0, float t1)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-find" href="#flContour-find"><span class="function-name">find</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-find">find</a>(QPointF, float, flNode::NodeType)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-findNearest" href="#flContour-findNearest"><span class="function-name">findNearest</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(float out_nearest_t, float dist)/Nothing <a href="#fontlab.flContour-findNearest">findNearest</a>(QPointF shape_p[, int orientation=0])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-findNearestNode" href="#flContour-findNearestNode"><span class="function-name">findNearestNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flNode, float new_maxd)/Nothing <a href="#fontlab.flContour-findNearestNode">findNearestNode</a>(QPointF p, flNode::NodeType node_type, float maxd)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-findNearestOn" href="#flContour-findNearestOn"><span class="function-name">findNearestOn</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float out_nearest_t/Nothing <a href="#fontlab.flContour-findNearestOn">findNearestOn</a>(QPointF  p, float base_t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-findNode" href="#flContour-findNode"><span class="function-name">findNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing <a href="#fontlab.flContour-findNode">findNode</a>(uint id | string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-flag" href="#flContour-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getBoundedT" href="#flContour-getBoundedT"><span class="function-name">getBoundedT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-getBoundedT">getBoundedT</a>(float param_t, float radius)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getChangesRect" href="#flContour-getChangesRect"><span class="function-name">getChangesRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flContour-getChangesRect">getChangesRect</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getFirstPoint" href="#flContour-getFirstPoint"><span class="function-name">getFirstPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing <a href="#fontlab.flContour-getFirstPoint">getFirstPoint</a>([int =0])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getIntervals" href="#flContour-getIntervals"><span class="function-name">getIntervals</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(Interval) <a href="#fontlab.flContour-getIntervals">getIntervals</a>(uint key)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getLastPoint" href="#flContour-getLastPoint"><span class="function-name">getLastPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing <a href="#fontlab.flContour-getLastPoint">getLastPoint</a>([int =0])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getLength" href="#flContour-getLength"><span class="function-name">getLength</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-getLength">getLength</a>([float t0, float t1,] int =10)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getLengthSquareBRect" href="#flContour-getLengthSquareBRect"><span class="function-name">getLengthSquareBRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(float square, float length, QRectF brect) <a href="#fontlab.flContour-getLengthSquareBRect">getLengthSquareBRect</a>(float t0, float t1[, int step=10])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getNext" href="#flContour-getNext"><span class="function-name">getNext</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing <a href="#fontlab.flContour-getNext">getNext</a>(index[, flNode::NodeType=flNode::On])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getNextT" href="#flContour-getNextT"><span class="function-name">getNextT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool, float) <a href="#fontlab.flContour-getNextT">getNextT</a>(float base_t, float offset)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getNodeAt" href="#flContour-getNodeAt"><span class="function-name">getNodeAt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing <a href="#fontlab.flContour-getNodeAt">getNodeAt</a>(int idx[, flNode::NodeType = flNode::AnyNodeMask])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getPoint" href="#flContour-getPoint"><span class="function-name">getPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing <a href="#fontlab.flContour-getPoint">getPoint</a>(int idx[, flNode::NodeType = flNode::On])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getPrev" href="#flContour-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing <a href="#fontlab.flContour-getPrev">getPrev</a>(index[, flNode::NodeType=flNode::On])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getPrevT" href="#flContour-getPrevT"><span class="function-name">getPrevT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool, float) <a href="#fontlab.flContour-getPrevT">getPrevT</a>(float base_t, float offset)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getProperties" href="#flContour-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getProperty" href="#flContour-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getPropertyFloat" href="#flContour-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getPropertyInt" href="#flContour-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getSegment" href="#flContour-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) <a href="#fontlab.flContour-getSegment">getSegment</a>(int i0, int i1, bool left)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getSelectedBoundingBox" href="#flContour-getSelectedBoundingBox"><span class="function-name">getSelectedBoundingBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flContour-getSelectedBoundingBox">getSelectedBoundingBox</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getSelectedNodes" href="#flContour-getSelectedNodes"><span class="function-name">getSelectedNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode)/Nothing <a href="#fontlab.flContour-getSelectedNodes">getSelectedNodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getSideOf" href="#flContour-getSideOf"><span class="function-name">getSideOf</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-getSideOf">getSideOf</a>(QPointF p)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getSquare" href="#flContour-getSquare"><span class="function-name">getSquare</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.flContour-getSquare">getSquare</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getT" href="#flContour-getT"><span class="function-name">getT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-getT">getT</a>(flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-getUpdateRect" href="#flContour-getUpdateRect"><span class="function-name">getUpdateRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flContour-getUpdateRect">getUpdateRect</a>(float ex_t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-hasHistoryState" href="#flContour-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-hasIntersPoints" href="#flContour-hasIntersPoints"><span class="function-name">hasIntersPoints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-hasIntersPoints">hasIntersPoints</a>(flContour)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-hasSelected" href="#flContour-hasSelected"><span class="function-name">hasSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-hasSelected">hasSelected</a>(SelectionMode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-historyStates" href="#flContour-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-improve" href="#flContour-improve"><span class="function-name">improve</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-improve">improve</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-indentParamT" href="#flContour-indentParamT"><span class="function-name">indentParamT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-indentParamT">indentParamT</a>(float base_t, float indent[, float step =0.1])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-independedAll" href="#flContour-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-initialHistoryState" href="#flContour-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-inkBox" href="#flContour-inkBox"><span class="function-name">inkBox</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF <a href="#fontlab.flContour-inkBox">inkBox</a>([QTransform tx])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-insert" href="#flContour-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-insert">insert</a>(index, flNode | list(flNode) )</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-insertNodeTo" href="#flContour-insertNodeTo"><span class="function-name">insertNodeTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-insertNodeTo">insertNodeTo</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-insertSafeNodeTo" href="#flContour-insertSafeNodeTo"><span class="function-name">insertSafeNodeTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-insertSafeNodeTo">insertSafeNodeTo</a>(float t, float dst)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-intervals" href="#flContour-intervals"><span class="function-name">intervals</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(Interval) <a href="#fontlab.flContour-intervals">intervals</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isAllNodesSelected" href="#flContour-isAllNodesSelected"><span class="function-name">isAllNodesSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-isAllNodesSelected">isAllNodesSelected</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isCompatible" href="#flContour-isCompatible"><span class="function-name">isCompatible</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-isCompatible">isCompatible</a>(flContour, bool strong)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isEqual" href="#flContour-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isFirst" href="#flContour-isFirst"><span class="function-name">isFirst</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-isFirst">isFirst</a>(flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isLast" href="#flContour-isLast"><span class="function-name">isLast</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-isLast">isLast</a>(flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-isSelected" href="#flContour-isSelected"><span class="function-name">isSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-isSelected">isSelected</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-mapParamT" href="#flContour-mapParamT"><span class="function-name">mapParamT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-mapParamT">mapParamT</a>(float, float, float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-markers" href="#flContour-markers"><span class="function-name">markers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flContourMarker) <a href="#fontlab.flContour-markers">markers</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-move" href="#flContour-move"><span class="function-name">move</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-move">move</a>(QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-nodes" href="#flContour-nodes"><span class="function-name">nodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) <a href="#fontlab.flContour-nodes">nodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-normalAt" href="#flContour-normalAt"><span class="function-name">normalAt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-normalAt">normalAt</a>(float t[, QTransform])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-normalPoint" href="#flContour-normalPoint"><span class="function-name">normalPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flContour-normalPoint">normalPoint</a>(float t, float length)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-normalizeExT" href="#flContour-normalizeExT"><span class="function-name">normalizeExT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-normalizeExT">normalizeExT</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-path" href="#flContour-path"><span class="function-name">path</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath <a href="#fontlab.flContour-path">path</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-pointInside" href="#flContour-pointInside"><span class="function-name">pointInside</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-pointInside">pointInside</a>(QPointF pt) - Bool indicating if the point pt in the black area of the contour</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-pointf" href="#flContour-pointf"><span class="function-name">pointf</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flContour-pointf">pointf</a>(int index)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-release" href="#flContour-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-remove" href="#flContour-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeAt" href="#flContour-removeAt"><span class="function-name">removeAt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeAt">removeAt</a>(int index)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeChild" href="#flContour-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeLast" href="#flContour-removeLast"><span class="function-name">removeLast</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeLast">removeLast</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeMarker" href="#flContour-removeMarker"><span class="function-name">removeMarker</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeMarker">removeMarker</a>( flContourMarker )</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeNodesBetween" href="#flContour-removeNodesBetween"><span class="function-name">removeNodesBetween</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeNodesBetween">removeNodesBetween</a>(flNode prev,  flNode next)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeOne" href="#flContour-removeOne"><span class="function-name">removeOne</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeOne">removeOne</a>(flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-removeProperty" href="#flContour-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-replace" href="#flContour-replace"><span class="function-name">replace</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-replace">replace</a>(flNode old_node, flNode new_node)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-restoreHistoryState" href="#flContour-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-reverse" href="#flContour-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-reverse">reverse</a>() - Reverse the direction of the contour</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-secondDerivative" href="#flContour-secondDerivative"><span class="function-name">secondDerivative</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF <a href="#fontlab.flContour-secondDerivative">secondDerivative</a>(float)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-segment" href="#flContour-segment"><span class="function-name">segment</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">CurveEx/Nothing <a href="#fontlab.flContour-segment">segment</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-segments" href="#flContour-segments"><span class="function-name">segments</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(CurveEx) <a href="#fontlab.flContour-segments">segments</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-selectedPath" href="#flContour-selectedPath"><span class="function-name">selectedPath</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath <a href="#fontlab.flContour-selectedPath">selectedPath</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-selectionChanged" href="#flContour-selectionChanged"><span class="function-name">selectionChanged</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-selectionChanged">selectionChanged</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setFlag" href="#flContour-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setNext" href="#flContour-setNext"><span class="function-name">setNext</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-setNext">setNext</a>(int, QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setPoint" href="#flContour-setPoint"><span class="function-name">setPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-setPoint">setPoint</a>(int index, QPointF p)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setPrev" href="#flContour-setPrev"><span class="function-name">setPrev</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode <a href="#fontlab.flContour-setPrev">setPrev</a>(int, QPointF)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setProperty" href="#flContour-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setPropertyFloat" href="#flContour-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setPropertyInt" href="#flContour-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setSelectedNodes" href="#flContour-setSelectedNodes"><span class="function-name">setSelectedNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-setSelectedNodes">setSelectedNodes</a>(bool)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-setStartPoint" href="#flContour-setStartPoint"><span class="function-name">setStartPoint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-setStartPoint">setStartPoint</a>(int i)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-simplify" href="#flContour-simplify"><span class="function-name">simplify</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-simplify">simplify</a>(float precision, bool lossy, bool extremes)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-tag" href="#flContour-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-takeNodes" href="#flContour-takeNodes"><span class="function-name">takeNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) <a href="#fontlab.flContour-takeNodes">takeNodes</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-tangent" href="#flContour-tangent"><span class="function-name">tangent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-tangent">tangent</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-toBeziers" href="#flContour-toBeziers"><span class="function-name">toBeziers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-toBeziers">toBeziers</a>(float tolerance)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-toSplines" href="#flContour-toSplines"><span class="function-name">toSplines</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-toSplines">toSplines</a>(float tolerance, bool short_splines)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-unselectAll" href="#flContour-unselectAll"><span class="function-name">unselectAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-unselectAll">unselectAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-unselectedPath" href="#flContour-unselectedPath"><span class="function-name">unselectedPath</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath <a href="#fontlab.flContour-unselectedPath">unselectedPath</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-update" href="#flContour-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-update">update</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-updateG2" href="#flContour-updateG2"><span class="function-name">updateG2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-updateG2">updateG2</a>(bool all_nodes)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-updateHobby" href="#flContour-updateHobby"><span class="function-name">updateHobby</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-updateHobby">updateHobby</a>(bool all_nodes)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-updateIndices" href="#flContour-updateIndices"><span class="function-name">updateIndices</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-updateIndices">updateIndices</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-validateExT" href="#flContour-validateExT"><span class="function-name">validateExT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_ex_t, bool) <a href="#fontlab.flContour-validateExT">validateExT</a>(float ex_t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-validateIndex" href="#flContour-validateIndex"><span class="function-name">validateIndex</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_inx, bool) <a href="#fontlab.flContour-validateIndex">validateIndex</a>(int inx)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-validateSmartR" href="#flContour-validateSmartR"><span class="function-name">validateSmartR</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_r, max_available_r, bool) <a href="#fontlab.flContour-validateSmartR">validateSmartR</a>(int node_ix, float r)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-validateT" href="#flContour-validateT"><span class="function-name">validateT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_t, bool) <a href="#fontlab.flContour-validateT">validateT</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-validatedT" href="#flContour-validatedT"><span class="function-name">validatedT</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float <a href="#fontlab.flContour-validatedT">validatedT</a>(float t)</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-verifySmooth" href="#flContour-verifySmooth"><span class="function-name">verifySmooth</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flContour-verifySmooth">verifySmooth</a>()</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flContour-cloneObject" href="#flContour-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flContour-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-createObject" href="#flContour-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flContour-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-haveObject" href="#flContour-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flContour-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flContour-instanceType" href="#flContour-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flContour-instanceType">instanceType</a>();</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>bounds</dt>
<dd>

<pre class="doc" markdown="0">The bounds of the contour as tuple (xMin, yMin, xMax, yMax) or None</pre>

</dd>
</dl>
<dl class="descriptor"><dt>clockwise</dt>
<dd>

<pre class="doc" markdown="0">Bool indicating if the contour’s winding direction is clockwise</pre>

</dd>
</dl>
<dl class="descriptor"><dt>closed</dt>
<dd>

<pre class="doc" markdown="0">closed attribute</pre>

</dd>
</dl>
<dl class="descriptor"><dt>closedT0</dt>
<dd>

<pre class="doc" markdown="0">closedT0 attr</pre>

</dd>
</dl>
<dl class="descriptor"><dt>closedT1</dt>
<dd>

<pre class="doc" markdown="0">closedT1 attr</pre>

</dd>
</dl>
<dl class="descriptor"><dt>first</dt>
<dd>

<pre class="doc" markdown="0">first node</pre>

</dd>
</dl>
<dl class="descriptor"><dt>font</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent font</pre>

</dd>
</dl>
<dl class="descriptor"><dt>glyph</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent glyph</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasCorners</dt>
<dd>

<pre class="doc" markdown="0">hasCorners</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasSmartAngle</dt>
<dd>

<pre class="doc" markdown="0">hasSmartAngle</pre>

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
<dl class="descriptor"><dt>isComplete</dt>
<dd>

<pre class="doc" markdown="0">isComplete</pre>

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
<dl class="descriptor"><dt>isTT</dt>
<dd>

<pre class="doc" markdown="0">is truetype</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>last</dt>
<dd>

<pre class="doc" markdown="0">last node</pre>

</dd>
</dl>
<dl class="descriptor"><dt>layer</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent layer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>nodesCount</dt>
<dd>

<pre class="doc" markdown="0">nodes count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>paramT0</dt>
<dd>

<pre class="doc" markdown="0">paramT0 attr</pre>

</dd>
</dl>
<dl class="descriptor"><dt>paramT1</dt>
<dd>

<pre class="doc" markdown="0">paramT1 attr</pre>

</dd>
</dl>
<dl class="descriptor"><dt>paramsClosed</dt>
<dd>

<pre class="doc" markdown="0">paramsClosed attribute</pre>

</dd>
</dl>
<dl class="descriptor"><dt>prevLast</dt>
<dd>

<pre class="doc" markdown="0">last but one node</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>reversed</dt>
<dd>

<pre class="doc" markdown="0">reversed</pre>

</dd>
</dl>
<dl class="descriptor"><dt>selection</dt>
<dd>

<pre class="doc" markdown="0">selection list (list<bool>)</pre>

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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">FigureType</span> = {'figureEllipse': 1, 'figureRectangle': 2}</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flContour-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flContour.add"></a>

## `add`


<dl class="function"><dt><a name="-fontlab.flContour.add" href="#-fontlab.flContour.add"><span class="function-name">fontlab.flContour.add</span></a> = add<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">add(flNode | QPointF)</pre>

</dd></dl>



<a name="fontlab.flContour.addInterval"></a>

## `addInterval`


<dl class="function"><dt><a name="-fontlab.flContour.addInterval" href="#-fontlab.flContour.addInterval"><span class="function-name">fontlab.flContour.addInterval</span></a> = addInterval<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">addInterval(Interval)</pre>

</dd></dl>



<a name="fontlab.flContour.addMarker"></a>

## `addMarker`


<dl class="function"><dt><a name="-fontlab.flContour.addMarker" href="#-fontlab.flContour.addMarker"><span class="function-name">fontlab.flContour.addMarker</span></a> = addMarker<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">addMarker( flContourMarker)</pre>

</dd></dl>



<a name="fontlab.flContour.addMarkers"></a>

## `addMarkers`


<dl class="function"><dt><a name="-fontlab.flContour.addMarkers" href="#-fontlab.flContour.addMarkers"><span class="function-name">fontlab.flContour.addMarkers</span></a> = addMarkers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">addMarkers( list(flContourMarker) )</pre>

</dd></dl>



<a name="fontlab.flContour.append"></a>

## `append`


<dl class="function"><dt><a name="-fontlab.flContour.append" href="#-fontlab.flContour.append"><span class="function-name">fontlab.flContour.append</span></a> = append<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">append(list(flNode) | flContour)</pre>

</dd></dl>



<a name="fontlab.flContour.appendMapped"></a>

## `appendMapped`


<dl class="function"><dt><a name="-fontlab.flContour.appendMapped" href="#-fontlab.flContour.appendMapped"><span class="function-name">fontlab.flContour.appendMapped</span></a> = appendMapped<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">appendMapped(list(flNode) | flContour, QTransform)</pre>

</dd></dl>



<a name="fontlab.flContour.appendMarkers"></a>

## `appendMarkers`


<dl class="function"><dt><a name="-fontlab.flContour.appendMarkers" href="#-fontlab.flContour.appendMarkers"><span class="function-name">fontlab.flContour.appendMarkers</span></a> = appendMarkers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">appendMarkers(list(flContourMarker))</pre>

</dd></dl>



<a name="fontlab.flContour.applyTransform"></a>

## `applyTransform`


<dl class="function"><dt><a name="-fontlab.flContour.applyTransform" href="#-fontlab.flContour.applyTransform"><span class="function-name">fontlab.flContour.applyTransform</span></a> = applyTransform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">applyTransform()</pre>

</dd></dl>



<a name="fontlab.flContour.assign"></a>

## `assign`


<dl class="function"><dt><a name="-fontlab.flContour.assign" href="#-fontlab.flContour.assign"><span class="function-name">fontlab.flContour.assign</span></a> = assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assign(flContour | fgContour | list(flNode))</pre>

</dd></dl>



<a name="fontlab.flContour.assignOwner"></a>

## `assignOwner`


<dl class="function"><dt><a name="-fontlab.flContour.assignOwner" href="#-fontlab.flContour.assignOwner"><span class="function-name">fontlab.flContour.assignOwner</span></a> = assignOwner<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assignOwner()</pre>

</dd></dl>



<a name="fontlab.flContour.at"></a>

## `at`


<dl class="function"><dt><a name="-fontlab.flContour.at" href="#-fontlab.flContour.at"><span class="function-name">fontlab.flContour.at</span></a> = at<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode at(int index)</pre>

</dd></dl>



<a name="fontlab.flContour.autoG2"></a>

## `autoG2`


<dl class="function"><dt><a name="-fontlab.flContour.autoG2" href="#-fontlab.flContour.autoG2"><span class="function-name">fontlab.flContour.autoG2</span></a> = autoG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">autoG2(float tolerance)</pre>

</dd></dl>



<a name="fontlab.flContour.beautify"></a>

## `beautify`


<dl class="function"><dt><a name="-fontlab.flContour.beautify" href="#-fontlab.flContour.beautify"><span class="function-name">fontlab.flContour.beautify</span></a> = beautify<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool beautify([int precision = 1])</pre>

</dd></dl>



<a name="fontlab.flContour.bindDependencies"></a>

## `bindDependencies`


<dl class="function"><dt><a name="-fontlab.flContour.bindDependencies" href="#-fontlab.flContour.bindDependencies"><span class="function-name">fontlab.flContour.bindDependencies</span></a> = bindDependencies<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bindDependencies()</pre>

</dd></dl>



<a name="fontlab.flContour.boundingBox"></a>

## `boundingBox`


<dl class="function"><dt><a name="-fontlab.flContour.boundingBox" href="#-fontlab.flContour.boundingBox"><span class="function-name">fontlab.flContour.boundingBox</span></a> = boundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF boundingBox([QTransform])</pre>

</dd></dl>



<a name="fontlab.flContour.bounds"></a>

## `bounds`


<dl class="descriptor"><dt>fontlab.flContour.bounds</dt>
<dd>

<pre class="doc" markdown="0">The bounds of the contour as tuple (xMin, yMin, xMax, yMax) or None</pre>

</dd>
</dl>



<a name="fontlab.flContour.breakContour"></a>

## `breakContour`


<dl class="function"><dt><a name="-fontlab.flContour.breakContour" href="#-fontlab.flContour.breakContour"><span class="function-name">fontlab.flContour.breakContour</span></a> = breakContour<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flContour, flNode, flNode)/Nothing breakContour(flNode) | flContour/Nothing breakContour(int node_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.breakContourExpanded"></a>

## `breakContourExpanded`


<dl class="function"><dt><a name="-fontlab.flContour.breakContourExpanded" href="#-fontlab.flContour.breakContourExpanded"><span class="function-name">fontlab.flContour.breakContourExpanded</span></a> = breakContourExpanded<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour/Nothing breakContourExpanded(int node_ix | flNode [, float extrapolate_d]</pre>

</dd></dl>



<a name="fontlab.flContour.calculate"></a>

## `calculate`


<dl class="function"><dt><a name="-fontlab.flContour.calculate" href="#-fontlab.flContour.calculate"><span class="function-name">fontlab.flContour.calculate</span></a> = calculate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF calculate(float t[, QTransform tx])</pre>

</dd></dl>



<a name="fontlab.flContour.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flContour.changed" href="#-fontlab.flContour.changed"><span class="function-name">fontlab.flContour.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flContour.checkFa"></a>

## `checkFa`


<dl class="function"><dt><a name="-fontlab.flContour.checkFa" href="#-fontlab.flContour.checkFa"><span class="function-name">fontlab.flContour.checkFa</span></a> = checkFa<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(FaBasic) checkFa(list(int) tests)</pre>

</dd></dl>



<a name="fontlab.flContour.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.checkInitHistoryState" href="#-fontlab.flContour.checkInitHistoryState"><span class="function-name">fontlab.flContour.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.checkSmooth"></a>

## `checkSmooth`


<dl class="function"><dt><a name="-fontlab.flContour.checkSmooth" href="#-fontlab.flContour.checkSmooth"><span class="function-name">fontlab.flContour.checkSmooth</span></a> = checkSmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkSmooth()</pre>

</dd></dl>



<a name="fontlab.flContour.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flContour.clearAboveHistory" href="#-fontlab.flContour.clearAboveHistory"><span class="function-name">fontlab.flContour.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flContour.clearFlag" href="#-fontlab.flContour.clearFlag"><span class="function-name">fontlab.flContour.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flContour.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flContour.clearFlags" href="#-fontlab.flContour.clearFlags"><span class="function-name">fontlab.flContour.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flContour.clearIntervals"></a>

## `clearIntervals`


<dl class="function"><dt><a name="-fontlab.flContour.clearIntervals" href="#-fontlab.flContour.clearIntervals"><span class="function-name">fontlab.flContour.clearIntervals</span></a> = clearIntervals<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearIntervals([uint key])</pre>

</dd></dl>



<a name="fontlab.flContour.clearMarkers"></a>

## `clearMarkers`


<dl class="function"><dt><a name="-fontlab.flContour.clearMarkers" href="#-fontlab.flContour.clearMarkers"><span class="function-name">fontlab.flContour.clearMarkers</span></a> = clearMarkers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearMarkers()</pre>

</dd></dl>



<a name="fontlab.flContour.clearNodes"></a>

## `clearNodes`


<dl class="function"><dt><a name="-fontlab.flContour.clearNodes" href="#-fontlab.flContour.clearNodes"><span class="function-name">fontlab.flContour.clearNodes</span></a> = clearNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearNodes()</pre>

</dd></dl>



<a name="fontlab.flContour.clockwise"></a>

## `clockwise`


<dl class="descriptor"><dt>fontlab.flContour.clockwise</dt>
<dd>

<pre class="doc" markdown="0">Bool indicating if the contour’s winding direction is clockwise</pre>

</dd>
</dl>



<a name="fontlab.flContour.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flContour.clone" href="#-fontlab.flContour.clone"><span class="function-name">fontlab.flContour.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flContour.cloneMapped"></a>

## `cloneMapped`


<dl class="function"><dt><a name="-fontlab.flContour.cloneMapped" href="#-fontlab.flContour.cloneMapped"><span class="function-name">fontlab.flContour.cloneMapped</span></a> = cloneMapped<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour cloneMapped(QTransform[, float ex_t0, float ex_t1])</pre>

</dd></dl>



<a name="fontlab.flContour.cloneMappedByT"></a>

## `cloneMappedByT`


<dl class="function"><dt><a name="-fontlab.flContour.cloneMappedByT" href="#-fontlab.flContour.cloneMappedByT"><span class="function-name">fontlab.flContour.cloneMappedByT</span></a> = cloneMappedByT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour cloneMappedByT(QTransform tx, float t0, float t1)</pre>

</dd></dl>



<a name="fontlab.flContour.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flContour.cloneObject" href="#-fontlab.flContour.cloneObject"><span class="function-name">fontlab.flContour.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flContour.cloneSelected"></a>

## `cloneSelected`


<dl class="function"><dt><a name="-fontlab.flContour.cloneSelected" href="#-fontlab.flContour.cloneSelected"><span class="function-name">fontlab.flContour.cloneSelected</span></a> = cloneSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flContour)/Nothing cloneSelected([QTransform, [bool ignore_alone=true]])</pre>

</dd></dl>



<a name="fontlab.flContour.closed"></a>

## `closed`


<dl class="descriptor"><dt>fontlab.flContour.closed</dt>
<dd>

<pre class="doc" markdown="0">closed attribute</pre>

</dd>
</dl>



<a name="fontlab.flContour.closedT0"></a>

## `closedT0`


<dl class="descriptor"><dt>fontlab.flContour.closedT0</dt>
<dd>

<pre class="doc" markdown="0">closedT0 attr</pre>

</dd>
</dl>



<a name="fontlab.flContour.closedT1"></a>

## `closedT1`


<dl class="descriptor"><dt>fontlab.flContour.closedT1</dt>
<dd>

<pre class="doc" markdown="0">closedT1 attr</pre>

</dd>
</dl>



<a name="fontlab.flContour.compare"></a>

## `compare`


<dl class="function"><dt><a name="-fontlab.flContour.compare" href="#-fontlab.flContour.compare"><span class="function-name">fontlab.flContour.compare</span></a> = compare<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool result, QPointF offset) compare(flContour, float error)</pre>

</dd></dl>



<a name="fontlab.flContour.contains"></a>

## `contains`


<dl class="function"><dt><a name="-fontlab.flContour.contains" href="#-fontlab.flContour.contains"><span class="function-name">fontlab.flContour.contains</span></a> = contains<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool contains(flContour knife | QPointF)</pre>

</dd></dl>



<a name="fontlab.flContour.convertClToT"></a>

## `convertClToT`


<dl class="function"><dt><a name="-fontlab.flContour.convertClToT" href="#-fontlab.flContour.convertClToT"><span class="function-name">fontlab.flContour.convertClToT</span></a> = convertClToT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float convertClToT(float)</pre>

</dd></dl>



<a name="fontlab.flContour.convertExToCl"></a>

## `convertExToCl`


<dl class="function"><dt><a name="-fontlab.flContour.convertExToCl" href="#-fontlab.flContour.convertExToCl"><span class="function-name">fontlab.flContour.convertExToCl</span></a> = convertExToCl<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float convertExToCl(float)</pre>

</dd></dl>



<a name="fontlab.flContour.convertExToT"></a>

## `convertExToT`


<dl class="function"><dt><a name="-fontlab.flContour.convertExToT" href="#-fontlab.flContour.convertExToT"><span class="function-name">fontlab.flContour.convertExToT</span></a> = convertExToT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float convertExToT(float)</pre>

</dd></dl>



<a name="fontlab.flContour.convertToFgContour"></a>

## `convertToFgContour`


<dl class="function"><dt><a name="-fontlab.flContour.convertToFgContour" href="#-fontlab.flContour.convertToFgContour"><span class="function-name">fontlab.flContour.convertToFgContour</span></a> = convertToFgContour<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgContour convertToFgContour([QTransform tx])</pre>

</dd></dl>



<a name="fontlab.flContour.convertTtoCl"></a>

## `convertTtoCl`


<dl class="function"><dt><a name="-fontlab.flContour.convertTtoCl" href="#-fontlab.flContour.convertTtoCl"><span class="function-name">fontlab.flContour.convertTtoCl</span></a> = convertTtoCl<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float convertTtoCl(float)</pre>

</dd></dl>



<a name="fontlab.flContour.convertTtoEx"></a>

## `convertTtoEx`


<dl class="function"><dt><a name="-fontlab.flContour.convertTtoEx" href="#-fontlab.flContour.convertTtoEx"><span class="function-name">fontlab.flContour.convertTtoEx</span></a> = convertTtoEx<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float convertTtoEx(float)</pre>

</dd></dl>



<a name="fontlab.flContour.convertTTtoCurve"></a>

## `convertTTtoCurve`


<dl class="function"><dt><a name="-fontlab.flContour.convertTTtoCurve" href="#-fontlab.flContour.convertTTtoCurve"><span class="function-name">fontlab.flContour.convertTTtoCurve</span></a> = convertTTtoCurve<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">convertTTtoCurve()</pre>

</dd></dl>



<a name="fontlab.flContour.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.createHistoryState" href="#-fontlab.flContour.createHistoryState"><span class="function-name">fontlab.flContour.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flContour.createObject" href="#-fontlab.flContour.createObject"><span class="function-name">fontlab.flContour.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flContour.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.currentHistoryState" href="#-fontlab.flContour.currentHistoryState"><span class="function-name">fontlab.flContour.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flContour.curvature"></a>

## `curvature`


<dl class="function"><dt><a name="-fontlab.flContour.curvature" href="#-fontlab.flContour.curvature"><span class="function-name">fontlab.flContour.curvature</span></a> = curvature<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float  curvature(float)</pre>

</dd></dl>



<a name="fontlab.flContour.derivative"></a>

## `derivative`


<dl class="function"><dt><a name="-fontlab.flContour.derivative" href="#-fontlab.flContour.derivative"><span class="function-name">fontlab.flContour.derivative</span></a> = derivative<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF derivative(float)</pre>

</dd></dl>



<a name="fontlab.flContour.distanceBetween"></a>

## `distanceBetween`


<dl class="function"><dt><a name="-fontlab.flContour.distanceBetween" href="#-fontlab.flContour.distanceBetween"><span class="function-name">fontlab.flContour.distanceBetween</span></a> = distanceBetween<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float distanceBetween(float t0, float t1[, float step =0.1])</pre>

</dd></dl>



<a name="fontlab.flContour.draw"></a>

## `draw`


<dl class="function"><dt><a name="-fontlab.flContour.draw" href="#-fontlab.flContour.draw"><span class="function-name">fontlab.flContour.draw</span></a> = draw<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">draw(pen) - Draw the contour’s outline data to the given type-pen</pre>

</dd></dl>



<a name="fontlab.flContour.drawPoints"></a>

## `drawPoints`


<dl class="function"><dt><a name="-fontlab.flContour.drawPoints" href="#-fontlab.flContour.drawPoints"><span class="function-name">fontlab.flContour.drawPoints</span></a> = drawPoints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">drawPoints(point-pen) - Draw the contour’s outline data to the given type-point-pen</pre>

</dd></dl>



<a name="fontlab.flContour.extrapolateFirst"></a>

## `extrapolateFirst`


<dl class="function"><dt><a name="-fontlab.flContour.extrapolateFirst" href="#-fontlab.flContour.extrapolateFirst"><span class="function-name">fontlab.flContour.extrapolateFirst</span></a> = extrapolateFirst<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">extrapolateFirst(float)</pre>

</dd></dl>



<a name="fontlab.flContour.extrapolateLast"></a>

## `extrapolateLast`


<dl class="function"><dt><a name="-fontlab.flContour.extrapolateLast" href="#-fontlab.flContour.extrapolateLast"><span class="function-name">fontlab.flContour.extrapolateLast</span></a> = extrapolateLast<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">extrapolateLast(float)</pre>

</dd></dl>



<a name="fontlab.flContour.fastAppend"></a>

## `fastAppend`


<dl class="function"><dt><a name="-fontlab.flContour.fastAppend" href="#-fontlab.flContour.fastAppend"><span class="function-name">fontlab.flContour.fastAppend</span></a> = fastAppend<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fastAppend( list(flNode) )</pre>

</dd></dl>



<a name="fontlab.flContour.fastClone"></a>

## `fastClone`


<dl class="function"><dt><a name="-fontlab.flContour.fastClone" href="#-fontlab.flContour.fastClone"><span class="function-name">fontlab.flContour.fastClone</span></a> = fastClone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour fastClone(float ex_t0, float ex_t1)</pre>

</dd></dl>



<a name="fontlab.flContour.fastCloneByT"></a>

## `fastCloneByT`


<dl class="function"><dt><a name="-fontlab.flContour.fastCloneByT" href="#-fontlab.flContour.fastCloneByT"><span class="function-name">fontlab.flContour.fastCloneByT</span></a> = fastCloneByT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flContour fastCloneByT(float t0, float t1)</pre>

</dd></dl>



<a name="fontlab.flContour.FigureType"></a>

## `FigureType`


<span class="other-name">fontlab.flContour.FigureType</span> = {'figureEllipse': 1, 'figureRectangle': 2}


<a name="fontlab.flContour.find"></a>

## `find`


<dl class="function"><dt><a name="-fontlab.flContour.find" href="#-fontlab.flContour.find"><span class="function-name">fontlab.flContour.find</span></a> = find<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode find(QPointF, float, flNode::NodeType)</pre>

</dd></dl>



<a name="fontlab.flContour.findNearest"></a>

## `findNearest`


<dl class="function"><dt><a name="-fontlab.flContour.findNearest" href="#-fontlab.flContour.findNearest"><span class="function-name">fontlab.flContour.findNearest</span></a> = findNearest<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(float out_nearest_t, float dist)/Nothing findNearest(QPointF shape_p[, int orientation=0])</pre>

</dd></dl>



<a name="fontlab.flContour.findNearestNode"></a>

## `findNearestNode`


<dl class="function"><dt><a name="-fontlab.flContour.findNearestNode" href="#-fontlab.flContour.findNearestNode"><span class="function-name">fontlab.flContour.findNearestNode</span></a> = findNearestNode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flNode, float new_maxd)/Nothing findNearestNode(QPointF p, flNode::NodeType node_type, float maxd)</pre>

</dd></dl>



<a name="fontlab.flContour.findNearestOn"></a>

## `findNearestOn`


<dl class="function"><dt><a name="-fontlab.flContour.findNearestOn" href="#-fontlab.flContour.findNearestOn"><span class="function-name">fontlab.flContour.findNearestOn</span></a> = findNearestOn<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float out_nearest_t/Nothing findNearestOn(QPointF  p, float base_t)</pre>

</dd></dl>



<a name="fontlab.flContour.findNode"></a>

## `findNode`


<dl class="function"><dt><a name="-fontlab.flContour.findNode" href="#-fontlab.flContour.findNode"><span class="function-name">fontlab.flContour.findNode</span></a> = findNode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing findNode(uint id | string name)</pre>

</dd></dl>



<a name="fontlab.flContour.first"></a>

## `first`


<dl class="descriptor"><dt>fontlab.flContour.first</dt>
<dd>

<pre class="doc" markdown="0">first node</pre>

</dd>
</dl>



<a name="fontlab.flContour.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flContour.flag" href="#-fontlab.flContour.flag"><span class="function-name">fontlab.flContour.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flContour.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flContour.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flContour.font"></a>

## `font`


<dl class="descriptor"><dt>fontlab.flContour.font</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent font</pre>

</dd>
</dl>



<a name="fontlab.flContour.getBoundedT"></a>

## `getBoundedT`


<dl class="function"><dt><a name="-fontlab.flContour.getBoundedT" href="#-fontlab.flContour.getBoundedT"><span class="function-name">fontlab.flContour.getBoundedT</span></a> = getBoundedT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float getBoundedT(float param_t, float radius)</pre>

</dd></dl>



<a name="fontlab.flContour.getChangesRect"></a>

## `getChangesRect`


<dl class="function"><dt><a name="-fontlab.flContour.getChangesRect" href="#-fontlab.flContour.getChangesRect"><span class="function-name">fontlab.flContour.getChangesRect</span></a> = getChangesRect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF getChangesRect()</pre>

</dd></dl>



<a name="fontlab.flContour.getFirstPoint"></a>

## `getFirstPoint`


<dl class="function"><dt><a name="-fontlab.flContour.getFirstPoint" href="#-fontlab.flContour.getFirstPoint"><span class="function-name">fontlab.flContour.getFirstPoint</span></a> = getFirstPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing getFirstPoint([int =0])</pre>

</dd></dl>



<a name="fontlab.flContour.getIntervals"></a>

## `getIntervals`


<dl class="function"><dt><a name="-fontlab.flContour.getIntervals" href="#-fontlab.flContour.getIntervals"><span class="function-name">fontlab.flContour.getIntervals</span></a> = getIntervals<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(Interval) getIntervals(uint key)</pre>

</dd></dl>



<a name="fontlab.flContour.getLastPoint"></a>

## `getLastPoint`


<dl class="function"><dt><a name="-fontlab.flContour.getLastPoint" href="#-fontlab.flContour.getLastPoint"><span class="function-name">fontlab.flContour.getLastPoint</span></a> = getLastPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing getLastPoint([int =0])</pre>

</dd></dl>



<a name="fontlab.flContour.getLength"></a>

## `getLength`


<dl class="function"><dt><a name="-fontlab.flContour.getLength" href="#-fontlab.flContour.getLength"><span class="function-name">fontlab.flContour.getLength</span></a> = getLength<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float getLength([float t0, float t1,] int =10)</pre>

</dd></dl>



<a name="fontlab.flContour.getLengthSquareBRect"></a>

## `getLengthSquareBRect`


<dl class="function"><dt><a name="-fontlab.flContour.getLengthSquareBRect" href="#-fontlab.flContour.getLengthSquareBRect"><span class="function-name">fontlab.flContour.getLengthSquareBRect</span></a> = getLengthSquareBRect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(float square, float length, QRectF brect) getLengthSquareBRect(float t0, float t1[, int step=10])</pre>

</dd></dl>



<a name="fontlab.flContour.getNext"></a>

## `getNext`


<dl class="function"><dt><a name="-fontlab.flContour.getNext" href="#-fontlab.flContour.getNext"><span class="function-name">fontlab.flContour.getNext</span></a> = getNext<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing getNext(index[, flNode::NodeType=flNode::On])</pre>

</dd></dl>



<a name="fontlab.flContour.getNextT"></a>

## `getNextT`


<dl class="function"><dt><a name="-fontlab.flContour.getNextT" href="#-fontlab.flContour.getNextT"><span class="function-name">fontlab.flContour.getNextT</span></a> = getNextT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool, float) getNextT(float base_t, float offset)</pre>

</dd></dl>



<a name="fontlab.flContour.getNodeAt"></a>

## `getNodeAt`


<dl class="function"><dt><a name="-fontlab.flContour.getNodeAt" href="#-fontlab.flContour.getNodeAt"><span class="function-name">fontlab.flContour.getNodeAt</span></a> = getNodeAt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing getNodeAt(int idx[, flNode::NodeType = flNode::AnyNodeMask])</pre>

</dd></dl>



<a name="fontlab.flContour.getPoint"></a>

## `getPoint`


<dl class="function"><dt><a name="-fontlab.flContour.getPoint" href="#-fontlab.flContour.getPoint"><span class="function-name">fontlab.flContour.getPoint</span></a> = getPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing getPoint(int idx[, flNode::NodeType = flNode::On])</pre>

</dd></dl>



<a name="fontlab.flContour.getPrev"></a>

## `getPrev`


<dl class="function"><dt><a name="-fontlab.flContour.getPrev" href="#-fontlab.flContour.getPrev"><span class="function-name">fontlab.flContour.getPrev</span></a> = getPrev<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode/Nothing getPrev(index[, flNode::NodeType=flNode::On])</pre>

</dd></dl>



<a name="fontlab.flContour.getPrevT"></a>

## `getPrevT`


<dl class="function"><dt><a name="-fontlab.flContour.getPrevT" href="#-fontlab.flContour.getPrevT"><span class="function-name">fontlab.flContour.getPrevT</span></a> = getPrevT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(bool, float) getPrevT(float base_t, float offset)</pre>

</dd></dl>



<a name="fontlab.flContour.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flContour.getProperties" href="#-fontlab.flContour.getProperties"><span class="function-name">fontlab.flContour.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flContour.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flContour.getProperty" href="#-fontlab.flContour.getProperty"><span class="function-name">fontlab.flContour.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flContour.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flContour.getPropertyFloat" href="#-fontlab.flContour.getPropertyFloat"><span class="function-name">fontlab.flContour.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flContour.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flContour.getPropertyInt" href="#-fontlab.flContour.getPropertyInt"><span class="function-name">fontlab.flContour.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flContour.getSegment"></a>

## `getSegment`


<dl class="function"><dt><a name="-fontlab.flContour.getSegment" href="#-fontlab.flContour.getSegment"><span class="function-name">fontlab.flContour.getSegment</span></a> = getSegment<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) getSegment(int i0, int i1, bool left)</pre>

</dd></dl>



<a name="fontlab.flContour.getSelectedBoundingBox"></a>

## `getSelectedBoundingBox`


<dl class="function"><dt><a name="-fontlab.flContour.getSelectedBoundingBox" href="#-fontlab.flContour.getSelectedBoundingBox"><span class="function-name">fontlab.flContour.getSelectedBoundingBox</span></a> = getSelectedBoundingBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF getSelectedBoundingBox()</pre>

</dd></dl>



<a name="fontlab.flContour.getSelectedNodes"></a>

## `getSelectedNodes`


<dl class="function"><dt><a name="-fontlab.flContour.getSelectedNodes" href="#-fontlab.flContour.getSelectedNodes"><span class="function-name">fontlab.flContour.getSelectedNodes</span></a> = getSelectedNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode)/Nothing getSelectedNodes()</pre>

</dd></dl>



<a name="fontlab.flContour.getSideOf"></a>

## `getSideOf`


<dl class="function"><dt><a name="-fontlab.flContour.getSideOf" href="#-fontlab.flContour.getSideOf"><span class="function-name">fontlab.flContour.getSideOf</span></a> = getSideOf<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float getSideOf(QPointF p)</pre>

</dd></dl>



<a name="fontlab.flContour.getSquare"></a>

## `getSquare`


<dl class="function"><dt><a name="-fontlab.flContour.getSquare" href="#-fontlab.flContour.getSquare"><span class="function-name">fontlab.flContour.getSquare</span></a> = getSquare<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double getSquare()</pre>

</dd></dl>



<a name="fontlab.flContour.getT"></a>

## `getT`


<dl class="function"><dt><a name="-fontlab.flContour.getT" href="#-fontlab.flContour.getT"><span class="function-name">fontlab.flContour.getT</span></a> = getT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float getT(flNode)</pre>

</dd></dl>



<a name="fontlab.flContour.getUpdateRect"></a>

## `getUpdateRect`


<dl class="function"><dt><a name="-fontlab.flContour.getUpdateRect" href="#-fontlab.flContour.getUpdateRect"><span class="function-name">fontlab.flContour.getUpdateRect</span></a> = getUpdateRect<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF getUpdateRect(float ex_t)</pre>

</dd></dl>



<a name="fontlab.flContour.glyph"></a>

## `glyph`


<dl class="descriptor"><dt>fontlab.flContour.glyph</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent glyph</pre>

</dd>
</dl>



<a name="fontlab.flContour.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flContour.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.hasCorners"></a>

## `hasCorners`


<dl class="descriptor"><dt>fontlab.flContour.hasCorners</dt>
<dd>

<pre class="doc" markdown="0">hasCorners</pre>

</dd>
</dl>



<a name="fontlab.flContour.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.hasHistoryState" href="#-fontlab.flContour.hasHistoryState"><span class="function-name">fontlab.flContour.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flContour.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.hasIntersPoints"></a>

## `hasIntersPoints`


<dl class="function"><dt><a name="-fontlab.flContour.hasIntersPoints" href="#-fontlab.flContour.hasIntersPoints"><span class="function-name">fontlab.flContour.hasIntersPoints</span></a> = hasIntersPoints<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasIntersPoints(flContour)</pre>

</dd></dl>



<a name="fontlab.flContour.hasSelected"></a>

## `hasSelected`


<dl class="function"><dt><a name="-fontlab.flContour.hasSelected" href="#-fontlab.flContour.hasSelected"><span class="function-name">fontlab.flContour.hasSelected</span></a> = hasSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasSelected(SelectionMode)</pre>

</dd></dl>



<a name="fontlab.flContour.hasSmartAngle"></a>

## `hasSmartAngle`


<dl class="descriptor"><dt>fontlab.flContour.hasSmartAngle</dt>
<dd>

<pre class="doc" markdown="0">hasSmartAngle</pre>

</dd>
</dl>



<a name="fontlab.flContour.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flContour.haveObject" href="#-fontlab.flContour.haveObject"><span class="function-name">fontlab.flContour.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flContour.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flContour.historyStates" href="#-fontlab.flContour.historyStates"><span class="function-name">fontlab.flContour.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flContour.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flContour.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flContour.improve"></a>

## `improve`


<dl class="function"><dt><a name="-fontlab.flContour.improve" href="#-fontlab.flContour.improve"><span class="function-name">fontlab.flContour.improve</span></a> = improve<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool improve()</pre>

</dd></dl>



<a name="fontlab.flContour.indentParamT"></a>

## `indentParamT`


<dl class="function"><dt><a name="-fontlab.flContour.indentParamT" href="#-fontlab.flContour.indentParamT"><span class="function-name">fontlab.flContour.indentParamT</span></a> = indentParamT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float indentParamT(float base_t, float indent[, float step =0.1])</pre>

</dd></dl>



<a name="fontlab.flContour.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flContour.independedAll" href="#-fontlab.flContour.independedAll"><span class="function-name">fontlab.flContour.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flContour.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.initialHistoryState" href="#-fontlab.flContour.initialHistoryState"><span class="function-name">fontlab.flContour.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flContour.inkBox"></a>

## `inkBox`


<dl class="function"><dt><a name="-fontlab.flContour.inkBox" href="#-fontlab.flContour.inkBox"><span class="function-name">fontlab.flContour.inkBox</span></a> = inkBox<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QRectF inkBox([QTransform tx])</pre>

</dd></dl>



<a name="fontlab.flContour.insert"></a>

## `insert`


<dl class="function"><dt><a name="-fontlab.flContour.insert" href="#-fontlab.flContour.insert"><span class="function-name">fontlab.flContour.insert</span></a> = insert<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">insert(index, flNode | list(flNode) )</pre>

</dd></dl>



<a name="fontlab.flContour.insertNodeTo"></a>

## `insertNodeTo`


<dl class="function"><dt><a name="-fontlab.flContour.insertNodeTo" href="#-fontlab.flContour.insertNodeTo"><span class="function-name">fontlab.flContour.insertNodeTo</span></a> = insertNodeTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode insertNodeTo(float t)</pre>

</dd></dl>



<a name="fontlab.flContour.insertSafeNodeTo"></a>

## `insertSafeNodeTo`


<dl class="function"><dt><a name="-fontlab.flContour.insertSafeNodeTo" href="#-fontlab.flContour.insertSafeNodeTo"><span class="function-name">fontlab.flContour.insertSafeNodeTo</span></a> = insertSafeNodeTo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode insertSafeNodeTo(float t, float dst)</pre>

</dd></dl>



<a name="fontlab.flContour.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flContour.instanceType" href="#-fontlab.flContour.instanceType"><span class="function-name">fontlab.flContour.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flContour.intervals"></a>

## `intervals`


<dl class="function"><dt><a name="-fontlab.flContour.intervals" href="#-fontlab.flContour.intervals"><span class="function-name">fontlab.flContour.intervals</span></a> = intervals<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(Interval) intervals()</pre>

</dd></dl>



<a name="fontlab.flContour.isAllNodesSelected"></a>

## `isAllNodesSelected`


<dl class="function"><dt><a name="-fontlab.flContour.isAllNodesSelected" href="#-fontlab.flContour.isAllNodesSelected"><span class="function-name">fontlab.flContour.isAllNodesSelected</span></a> = isAllNodesSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isAllNodesSelected()</pre>

</dd></dl>



<a name="fontlab.flContour.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flContour.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.isCompatible"></a>

## `isCompatible`


<dl class="function"><dt><a name="-fontlab.flContour.isCompatible" href="#-fontlab.flContour.isCompatible"><span class="function-name">fontlab.flContour.isCompatible</span></a> = isCompatible<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isCompatible(flContour, bool strong)</pre>

</dd></dl>



<a name="fontlab.flContour.isComplete"></a>

## `isComplete`


<dl class="descriptor"><dt>fontlab.flContour.isComplete</dt>
<dd>

<pre class="doc" markdown="0">isComplete</pre>

</dd>
</dl>



<a name="fontlab.flContour.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flContour.isEqual" href="#-fontlab.flContour.isEqual"><span class="function-name">fontlab.flContour.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flContour.isFirst"></a>

## `isFirst`


<dl class="function"><dt><a name="-fontlab.flContour.isFirst" href="#-fontlab.flContour.isFirst"><span class="function-name">fontlab.flContour.isFirst</span></a> = isFirst<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isFirst(flNode)</pre>

</dd></dl>



<a name="fontlab.flContour.isLast"></a>

## `isLast`


<dl class="function"><dt><a name="-fontlab.flContour.isLast" href="#-fontlab.flContour.isLast"><span class="function-name">fontlab.flContour.isLast</span></a> = isLast<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isLast(flNode)</pre>

</dd></dl>



<a name="fontlab.flContour.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flContour.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flContour.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flContour.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.isSelected"></a>

## `isSelected`


<dl class="function"><dt><a name="-fontlab.flContour.isSelected" href="#-fontlab.flContour.isSelected"><span class="function-name">fontlab.flContour.isSelected</span></a> = isSelected<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isSelected(float)</pre>

</dd></dl>



<a name="fontlab.flContour.isTT"></a>

## `isTT`


<dl class="descriptor"><dt>fontlab.flContour.isTT</dt>
<dd>

<pre class="doc" markdown="0">is truetype</pre>

</dd>
</dl>



<a name="fontlab.flContour.isValid"></a>

## `isValid`


<dl class="descriptor"><dt>fontlab.flContour.isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flContour.last"></a>

## `last`


<dl class="descriptor"><dt>fontlab.flContour.last</dt>
<dd>

<pre class="doc" markdown="0">last node</pre>

</dd>
</dl>



<a name="fontlab.flContour.layer"></a>

## `layer`


<dl class="descriptor"><dt>fontlab.flContour.layer</dt>
<dd>

<pre class="doc" markdown="0">The contour’s parent layer</pre>

</dd>
</dl>



<a name="fontlab.flContour.mapParamT"></a>

## `mapParamT`


<dl class="function"><dt><a name="-fontlab.flContour.mapParamT" href="#-fontlab.flContour.mapParamT"><span class="function-name">fontlab.flContour.mapParamT</span></a> = mapParamT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float mapParamT(float, float, float)</pre>

</dd></dl>



<a name="fontlab.flContour.markers"></a>

## `markers`


<dl class="function"><dt><a name="-fontlab.flContour.markers" href="#-fontlab.flContour.markers"><span class="function-name">fontlab.flContour.markers</span></a> = markers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flContourMarker) markers()</pre>

</dd></dl>



<a name="fontlab.flContour.move"></a>

## `move`


<dl class="function"><dt><a name="-fontlab.flContour.move" href="#-fontlab.flContour.move"><span class="function-name">fontlab.flContour.move</span></a> = move<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">move(QPointF)</pre>

</dd></dl>



<a name="fontlab.flContour.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flContour.name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>



<a name="fontlab.flContour.nodes"></a>

## `nodes`


<dl class="function"><dt><a name="-fontlab.flContour.nodes" href="#-fontlab.flContour.nodes"><span class="function-name">fontlab.flContour.nodes</span></a> = nodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) nodes()</pre>

</dd></dl>



<a name="fontlab.flContour.nodesCount"></a>

## `nodesCount`


<dl class="descriptor"><dt>fontlab.flContour.nodesCount</dt>
<dd>

<pre class="doc" markdown="0">nodes count</pre>

</dd>
</dl>



<a name="fontlab.flContour.normalAt"></a>

## `normalAt`


<dl class="function"><dt><a name="-fontlab.flContour.normalAt" href="#-fontlab.flContour.normalAt"><span class="function-name">fontlab.flContour.normalAt</span></a> = normalAt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float normalAt(float t[, QTransform])</pre>

</dd></dl>



<a name="fontlab.flContour.normalizeExT"></a>

## `normalizeExT`


<dl class="function"><dt><a name="-fontlab.flContour.normalizeExT" href="#-fontlab.flContour.normalizeExT"><span class="function-name">fontlab.flContour.normalizeExT</span></a> = normalizeExT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float normalizeExT(float)</pre>

</dd></dl>



<a name="fontlab.flContour.normalPoint"></a>

## `normalPoint`


<dl class="function"><dt><a name="-fontlab.flContour.normalPoint" href="#-fontlab.flContour.normalPoint"><span class="function-name">fontlab.flContour.normalPoint</span></a> = normalPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF normalPoint(float t, float length)</pre>

</dd></dl>



<a name="fontlab.flContour.paramsClosed"></a>

## `paramsClosed`


<dl class="descriptor"><dt>fontlab.flContour.paramsClosed</dt>
<dd>

<pre class="doc" markdown="0">paramsClosed attribute</pre>

</dd>
</dl>



<a name="fontlab.flContour.paramT0"></a>

## `paramT0`


<dl class="descriptor"><dt>fontlab.flContour.paramT0</dt>
<dd>

<pre class="doc" markdown="0">paramT0 attr</pre>

</dd>
</dl>



<a name="fontlab.flContour.paramT1"></a>

## `paramT1`


<dl class="descriptor"><dt>fontlab.flContour.paramT1</dt>
<dd>

<pre class="doc" markdown="0">paramT1 attr</pre>

</dd>
</dl>



<a name="fontlab.flContour.path"></a>

## `path`


<dl class="function"><dt><a name="-fontlab.flContour.path" href="#-fontlab.flContour.path"><span class="function-name">fontlab.flContour.path</span></a> = path<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath path()</pre>

</dd></dl>



<a name="fontlab.flContour.pointf"></a>

## `pointf`


<dl class="function"><dt><a name="-fontlab.flContour.pointf" href="#-fontlab.flContour.pointf"><span class="function-name">fontlab.flContour.pointf</span></a> = pointf<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF pointf(int index)</pre>

</dd></dl>



<a name="fontlab.flContour.pointInside"></a>

## `pointInside`


<dl class="function"><dt><a name="-fontlab.flContour.pointInside" href="#-fontlab.flContour.pointInside"><span class="function-name">fontlab.flContour.pointInside</span></a> = pointInside<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">pointInside(QPointF pt) - Bool indicating if the point pt in the black area of the contour</pre>

</dd></dl>



<a name="fontlab.flContour.prevLast"></a>

## `prevLast`


<dl class="descriptor"><dt>fontlab.flContour.prevLast</dt>
<dd>

<pre class="doc" markdown="0">last but one node</pre>

</dd>
</dl>



<a name="fontlab.flContour.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flContour.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flContour.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flContour.release" href="#-fontlab.flContour.release"><span class="function-name">fontlab.flContour.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flContour.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flContour.remove" href="#-fontlab.flContour.remove"><span class="function-name">fontlab.flContour.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flContour.removeAt"></a>

## `removeAt`


<dl class="function"><dt><a name="-fontlab.flContour.removeAt" href="#-fontlab.flContour.removeAt"><span class="function-name">fontlab.flContour.removeAt</span></a> = removeAt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeAt(int index)</pre>

</dd></dl>



<a name="fontlab.flContour.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flContour.removeChild" href="#-fontlab.flContour.removeChild"><span class="function-name">fontlab.flContour.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flContour.removeLast"></a>

## `removeLast`


<dl class="function"><dt><a name="-fontlab.flContour.removeLast" href="#-fontlab.flContour.removeLast"><span class="function-name">fontlab.flContour.removeLast</span></a> = removeLast<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeLast()</pre>

</dd></dl>



<a name="fontlab.flContour.removeMarker"></a>

## `removeMarker`


<dl class="function"><dt><a name="-fontlab.flContour.removeMarker" href="#-fontlab.flContour.removeMarker"><span class="function-name">fontlab.flContour.removeMarker</span></a> = removeMarker<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeMarker( flContourMarker )</pre>

</dd></dl>



<a name="fontlab.flContour.removeNodesBetween"></a>

## `removeNodesBetween`


<dl class="function"><dt><a name="-fontlab.flContour.removeNodesBetween" href="#-fontlab.flContour.removeNodesBetween"><span class="function-name">fontlab.flContour.removeNodesBetween</span></a> = removeNodesBetween<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeNodesBetween(flNode prev,  flNode next)</pre>

</dd></dl>



<a name="fontlab.flContour.removeOne"></a>

## `removeOne`


<dl class="function"><dt><a name="-fontlab.flContour.removeOne" href="#-fontlab.flContour.removeOne"><span class="function-name">fontlab.flContour.removeOne</span></a> = removeOne<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeOne(flNode)</pre>

</dd></dl>



<a name="fontlab.flContour.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flContour.removeProperty" href="#-fontlab.flContour.removeProperty"><span class="function-name">fontlab.flContour.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flContour.replace"></a>

## `replace`


<dl class="function"><dt><a name="-fontlab.flContour.replace" href="#-fontlab.flContour.replace"><span class="function-name">fontlab.flContour.replace</span></a> = replace<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">replace(flNode old_node, flNode new_node)</pre>

</dd></dl>



<a name="fontlab.flContour.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flContour.restoreHistoryState" href="#-fontlab.flContour.restoreHistoryState"><span class="function-name">fontlab.flContour.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flContour.reverse"></a>

## `reverse`


<dl class="function"><dt><a name="-fontlab.flContour.reverse" href="#-fontlab.flContour.reverse"><span class="function-name">fontlab.flContour.reverse</span></a> = reverse<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">reverse() - Reverse the direction of the contour</pre>

</dd></dl>



<a name="fontlab.flContour.reversed"></a>

## `reversed`


<dl class="descriptor"><dt>fontlab.flContour.reversed</dt>
<dd>

<pre class="doc" markdown="0">reversed</pre>

</dd>
</dl>



<a name="fontlab.flContour.secondDerivative"></a>

## `secondDerivative`


<dl class="function"><dt><a name="-fontlab.flContour.secondDerivative" href="#-fontlab.flContour.secondDerivative"><span class="function-name">fontlab.flContour.secondDerivative</span></a> = secondDerivative<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF secondDerivative(float)</pre>

</dd></dl>



<a name="fontlab.flContour.segment"></a>

## `segment`


<dl class="function"><dt><a name="-fontlab.flContour.segment" href="#-fontlab.flContour.segment"><span class="function-name">fontlab.flContour.segment</span></a> = segment<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">CurveEx/Nothing segment(float t)</pre>

</dd></dl>



<a name="fontlab.flContour.segments"></a>

## `segments`


<dl class="function"><dt><a name="-fontlab.flContour.segments" href="#-fontlab.flContour.segments"><span class="function-name">fontlab.flContour.segments</span></a> = segments<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(CurveEx) segments()</pre>

</dd></dl>



<a name="fontlab.flContour.selectedPath"></a>

## `selectedPath`


<dl class="function"><dt><a name="-fontlab.flContour.selectedPath" href="#-fontlab.flContour.selectedPath"><span class="function-name">fontlab.flContour.selectedPath</span></a> = selectedPath<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath selectedPath()</pre>

</dd></dl>



<a name="fontlab.flContour.selection"></a>

## `selection`


<dl class="descriptor"><dt>fontlab.flContour.selection</dt>
<dd>

<pre class="doc" markdown="0">selection list (list<bool>)</pre>

</dd>
</dl>



<a name="fontlab.flContour.selectionChanged"></a>

## `selectionChanged`


<dl class="function"><dt><a name="-fontlab.flContour.selectionChanged" href="#-fontlab.flContour.selectionChanged"><span class="function-name">fontlab.flContour.selectionChanged</span></a> = selectionChanged<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">selectionChanged()</pre>

</dd></dl>



<a name="fontlab.flContour.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flContour.setFlag" href="#-fontlab.flContour.setFlag"><span class="function-name">fontlab.flContour.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flContour.setNext"></a>

## `setNext`


<dl class="function"><dt><a name="-fontlab.flContour.setNext" href="#-fontlab.flContour.setNext"><span class="function-name">fontlab.flContour.setNext</span></a> = setNext<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode setNext(int, QPointF)</pre>

</dd></dl>



<a name="fontlab.flContour.setPoint"></a>

## `setPoint`


<dl class="function"><dt><a name="-fontlab.flContour.setPoint" href="#-fontlab.flContour.setPoint"><span class="function-name">fontlab.flContour.setPoint</span></a> = setPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode setPoint(int index, QPointF p)</pre>

</dd></dl>



<a name="fontlab.flContour.setPrev"></a>

## `setPrev`


<dl class="function"><dt><a name="-fontlab.flContour.setPrev" href="#-fontlab.flContour.setPrev"><span class="function-name">fontlab.flContour.setPrev</span></a> = setPrev<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flNode setPrev(int, QPointF)</pre>

</dd></dl>



<a name="fontlab.flContour.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flContour.setProperty" href="#-fontlab.flContour.setProperty"><span class="function-name">fontlab.flContour.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flContour.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flContour.setPropertyFloat" href="#-fontlab.flContour.setPropertyFloat"><span class="function-name">fontlab.flContour.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flContour.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flContour.setPropertyInt" href="#-fontlab.flContour.setPropertyInt"><span class="function-name">fontlab.flContour.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flContour.setSelectedNodes"></a>

## `setSelectedNodes`


<dl class="function"><dt><a name="-fontlab.flContour.setSelectedNodes" href="#-fontlab.flContour.setSelectedNodes"><span class="function-name">fontlab.flContour.setSelectedNodes</span></a> = setSelectedNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setSelectedNodes(bool)</pre>

</dd></dl>



<a name="fontlab.flContour.setStartPoint"></a>

## `setStartPoint`


<dl class="function"><dt><a name="-fontlab.flContour.setStartPoint" href="#-fontlab.flContour.setStartPoint"><span class="function-name">fontlab.flContour.setStartPoint</span></a> = setStartPoint<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool setStartPoint(int i)</pre>

</dd></dl>



<a name="fontlab.flContour.simplify"></a>

## `simplify`


<dl class="function"><dt><a name="-fontlab.flContour.simplify" href="#-fontlab.flContour.simplify"><span class="function-name">fontlab.flContour.simplify</span></a> = simplify<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">simplify(float precision, bool lossy, bool extremes)</pre>

</dd></dl>



<a name="fontlab.flContour.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flContour.tag" href="#-fontlab.flContour.tag"><span class="function-name">fontlab.flContour.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flContour.takeNodes"></a>

## `takeNodes`


<dl class="function"><dt><a name="-fontlab.flContour.takeNodes" href="#-fontlab.flContour.takeNodes"><span class="function-name">fontlab.flContour.takeNodes</span></a> = takeNodes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flNode) takeNodes()</pre>

</dd></dl>



<a name="fontlab.flContour.tangent"></a>

## `tangent`


<dl class="function"><dt><a name="-fontlab.flContour.tangent" href="#-fontlab.flContour.tangent"><span class="function-name">fontlab.flContour.tangent</span></a> = tangent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float tangent(float t)</pre>

</dd></dl>



<a name="fontlab.flContour.toBeziers"></a>

## `toBeziers`


<dl class="function"><dt><a name="-fontlab.flContour.toBeziers" href="#-fontlab.flContour.toBeziers"><span class="function-name">fontlab.flContour.toBeziers</span></a> = toBeziers<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">toBeziers(float tolerance)</pre>

</dd></dl>



<a name="fontlab.flContour.toSplines"></a>

## `toSplines`


<dl class="function"><dt><a name="-fontlab.flContour.toSplines" href="#-fontlab.flContour.toSplines"><span class="function-name">fontlab.flContour.toSplines</span></a> = toSplines<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">toSplines(float tolerance, bool short_splines)</pre>

</dd></dl>



<a name="fontlab.flContour.transform"></a>

## `transform`


<dl class="descriptor"><dt>fontlab.flContour.transform</dt>
<dd>

<pre class="doc" markdown="0">transform matrix</pre>

</dd>
</dl>



<a name="fontlab.flContour.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flContour.type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>



<a name="fontlab.flContour.unselectAll"></a>

## `unselectAll`


<dl class="function"><dt><a name="-fontlab.flContour.unselectAll" href="#-fontlab.flContour.unselectAll"><span class="function-name">fontlab.flContour.unselectAll</span></a> = unselectAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">unselectAll()</pre>

</dd></dl>



<a name="fontlab.flContour.unselectedPath"></a>

## `unselectedPath`


<dl class="function"><dt><a name="-fontlab.flContour.unselectedPath" href="#-fontlab.flContour.unselectedPath"><span class="function-name">fontlab.flContour.unselectedPath</span></a> = unselectedPath<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPainterPath unselectedPath()</pre>

</dd></dl>



<a name="fontlab.flContour.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flContour.update" href="#-fontlab.flContour.update"><span class="function-name">fontlab.flContour.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>



<a name="fontlab.flContour.updateG2"></a>

## `updateG2`


<dl class="function"><dt><a name="-fontlab.flContour.updateG2" href="#-fontlab.flContour.updateG2"><span class="function-name">fontlab.flContour.updateG2</span></a> = updateG2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateG2(bool all_nodes)</pre>

</dd></dl>



<a name="fontlab.flContour.updateHobby"></a>

## `updateHobby`


<dl class="function"><dt><a name="-fontlab.flContour.updateHobby" href="#-fontlab.flContour.updateHobby"><span class="function-name">fontlab.flContour.updateHobby</span></a> = updateHobby<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateHobby(bool all_nodes)</pre>

</dd></dl>



<a name="fontlab.flContour.updateIndices"></a>

## `updateIndices`


<dl class="function"><dt><a name="-fontlab.flContour.updateIndices" href="#-fontlab.flContour.updateIndices"><span class="function-name">fontlab.flContour.updateIndices</span></a> = updateIndices<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateIndices()</pre>

</dd></dl>



<a name="fontlab.flContour.validatedT"></a>

## `validatedT`


<dl class="function"><dt><a name="-fontlab.flContour.validatedT" href="#-fontlab.flContour.validatedT"><span class="function-name">fontlab.flContour.validatedT</span></a> = validatedT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">float validatedT(float t)</pre>

</dd></dl>



<a name="fontlab.flContour.validateExT"></a>

## `validateExT`


<dl class="function"><dt><a name="-fontlab.flContour.validateExT" href="#-fontlab.flContour.validateExT"><span class="function-name">fontlab.flContour.validateExT</span></a> = validateExT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_ex_t, bool) validateExT(float ex_t)</pre>

</dd></dl>



<a name="fontlab.flContour.validateIndex"></a>

## `validateIndex`


<dl class="function"><dt><a name="-fontlab.flContour.validateIndex" href="#-fontlab.flContour.validateIndex"><span class="function-name">fontlab.flContour.validateIndex</span></a> = validateIndex<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_inx, bool) validateIndex(int inx)</pre>

</dd></dl>



<a name="fontlab.flContour.validateSmartR"></a>

## `validateSmartR`


<dl class="function"><dt><a name="-fontlab.flContour.validateSmartR" href="#-fontlab.flContour.validateSmartR"><span class="function-name">fontlab.flContour.validateSmartR</span></a> = validateSmartR<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_r, max_available_r, bool) validateSmartR(int node_ix, float r)</pre>

</dd></dl>



<a name="fontlab.flContour.validateT"></a>

## `validateT`


<dl class="function"><dt><a name="-fontlab.flContour.validateT" href="#-fontlab.flContour.validateT"><span class="function-name">fontlab.flContour.validateT</span></a> = validateT<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(new_t, bool) validateT(float t)</pre>

</dd></dl>



<a name="fontlab.flContour.verifySmooth"></a>

## `verifySmooth`


<dl class="function"><dt><a name="-fontlab.flContour.verifySmooth" href="#-fontlab.flContour.verifySmooth"><span class="function-name">fontlab.flContour.verifySmooth</span></a> = verifySmooth<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">verifySmooth()</pre>

</dd></dl>

