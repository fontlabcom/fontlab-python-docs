

<a name="typerig.proxy.objects.node"></a>

# `typerig.proxy.objects.node`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.node (<span class="info">version 0.26.3)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Node (Obejcts)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>math</li><li>PythonQt</li><li>random</li><li>typerig.core.objects</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.node.html#pNode">pNode</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.node.html#eNode">eNode</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.node.html#eNodesContainer">eNodesContainer</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eNode" href="#eNode">class <span class="class-name">eNode</span></a>(<a href="./typerig.proxy.objects.node.html#pNode">pNode</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Node, adding some advanced functionality

Constructor:
        eNode(flNode)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.node.html#eNode">eNode</a></dd><dd><a href="./typerig.proxy.objects.node.html#pNode">pNode</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eNode-alignTo" href="#eNode-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current node to a node or line given.
Arguments:
        entity (flNode, <a href="#pNode">pNode</a>, <a href="#eNode">eNode</a> or Line)
        align (tuple(Align_X (bool), Align_Y (bool))</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-asCoord" href="#eNode-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord <a href="./__builtin__.html#object">object</a> of the node.</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerMitre" href="#eNode-cornerMitre"><span class="function-name">cornerMitre</span></a><span class="argspec">(self, mitreSize<span class="parameter-default">=5</span>, isRadius<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Corner operations ---------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerRound" href="#eNode-cornerRound"><span class="function-name">cornerRound</span></a><span class="argspec">(self, size<span class="parameter-default">=5</span>, proportion<span class="parameter-default">=None</span>, curvature<span class="parameter-default">=None</span>, isRadius<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerTrap" href="#eNode-cornerTrap"><span class="function-name">cornerTrap</span></a><span class="argspec">(self, aperture<span class="parameter-default">=10</span>, depth<span class="parameter-default">=20</span>, trap<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given aperture.

Arguments:
        aperture (float): Width of the traps mouth (opening);
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom.

Returns:
        tuple(flNode, flNode, flNode, flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerTrapInc" href="#eNode-cornerTrapInc"><span class="function-name">cornerTrapInc</span></a><span class="argspec">(self, incision<span class="parameter-default">=10</span>, depth<span class="parameter-default">=50</span>, trap<span class="parameter-default">=2</span>, smooth<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given incision into the glyph flesh.

Arguments:
        incision (float): How much to cut into glyphs flesh based from that corner inward;
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom;
        smooth (bool): Creates a smooth trap.

Returns:
        tuple(flNode, flNode, flNode, flNode) four base (ON) nodes of the trap.</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffTo" href="#eNode-diffTo"><span class="function-name">diffTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffToNext" href="#eNode-diffToNext"><span class="function-name">diffToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffToPrev" href="#eNode-diffToPrev"><span class="function-name">diffToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNextLine" href="#eNode-getNextLine"><span class="function-name">getNextLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrevLine" href="#eNode-getPrevLine"><span class="function-name">getPrevLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-interpShift" href="#eNode-interpShift"><span class="function-name">interpShift</span></a><span class="argspec">(self, shift_x, shift_y)</span></dt><dd>

<pre class="doc" markdown="0">Interpolated move aka Interpolated Nudge.

Arguments:
        shift_x, shift_y (float)</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarReloc" href="#eNode-polarReloc"><span class="function-name">polarReloc</span></a><span class="argspec">(self, angle, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarRelocFromPrev" href="#eNode-polarRelocFromPrev"><span class="function-name">polarRelocFromPrev</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarTo" href="#eNode-polarTo"><span class="function-name">polarTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarToNext" href="#eNode-polarToNext"><span class="function-name">polarToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarToPrev" href="#eNode-polarToPrev"><span class="function-name">polarToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shiftFromNext" href="#eNode-shiftFromNext"><span class="function-name">shiftFromNext</span></a><span class="argspec">(self, diffX, diffY)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shiftFromPrev" href="#eNode-shiftFromPrev"><span class="function-name">shiftFromPrev</span></a><span class="argspec">(self, diffX, diffY)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-slantShift" href="#eNode-slantShift"><span class="function-name">slantShift</span></a><span class="argspec">(self, shift_x, shift_y, angle)</span></dt><dd>

<pre class="doc" markdown="0">Slanted move - move a node (in inclined space) according to Y coordinate slanted at given angle.

Arguments:
        shift_x, shift_y (float)
        angle (float): Angle in degrees</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartPolarReloc" href="#eNode-smartPolarReloc"><span class="function-name">smartPolarReloc</span></a><span class="argspec">(self, angle, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.node.html#pNode">pNode</a></h4><dl class="function"><dt><a name="eNode-__init__" href="#eNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-__repr__" href="#eNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleTo" href="#eNode-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleToNext" href="#eNode-angleToNext"><span class="function-name">angleToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleToPrev" href="#eNode-angleToPrev"><span class="function-name">angleToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-delSmartAngle" href="#eNode-delSmartAngle"><span class="function-name">delSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceTo" href="#eNode-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceToNext" href="#eNode-distanceToNext"><span class="function-name">distanceToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceToPrev" href="#eNode-distanceToPrev"><span class="function-name">distanceToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getContour" href="#eNode-getContour"><span class="function-name">getContour</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getMaxY" href="#eNode-getMaxY"><span class="function-name">getMaxY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getMinY" href="#eNode-getMinY"><span class="function-name">getMinY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNext" href="#eNode-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNextOn" href="#eNode-getNextOn"><span class="function-name">getNextOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getOn" href="#eNode-getOn"><span class="function-name">getOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrev" href="#eNode-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrevOn" href="#eNode-getPrevOn"><span class="function-name">getPrevOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSegment" href="#eNode-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSegmentNodes" href="#eNode-getSegmentNodes"><span class="function-name">getSegmentNodes</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSmartAngle" href="#eNode-getSmartAngle"><span class="function-name">getSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Effects --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSmartAngleRadius" href="#eNode-getSmartAngleRadius"><span class="function-name">getSmartAngleRadius</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getTime" href="#eNode-getTime"><span class="function-name">getTime</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertAfter" href="#eNode-insertAfter"><span class="function-name">insertAfter</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertAfterDist" href="#eNode-insertAfterDist"><span class="function-name">insertAfterDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertBefore" href="#eNode-insertBefore"><span class="function-name">insertBefore</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertBeforeDist" href="#eNode-insertBeforeDist"><span class="function-name">insertBeforeDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-reloc" href="#eNode-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-remove" href="#eNode-remove"><span class="function-name">remove</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-setSmartAngle" href="#eNode-setSmartAngle"><span class="function-name">setSmartAngle</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-setSmartAngleRadius" href="#eNode-setSmartAngleRadius"><span class="function-name">setSmartAngleRadius</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shift" href="#eNode-shift"><span class="function-name">shift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartReloc" href="#eNode-smartReloc"><span class="function-name">smartReloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node and adjacent BCPs to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartShift" href="#eNode-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node and adjacent BCPs by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-update" href="#eNode-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.node.html#pNode">pNode</a></h4><dl class="descriptor"><dt>__dict__</dt>
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
<dt class="class"><h2><a name="eNodesContainer" href="#eNodesContainer">class <span class="class-name">eNodesContainer</span></a>(<a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of Abstract nodes container

Constructor:
        eNodesContainer(list(flNode))</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.node.html#eNodesContainer">eNodesContainer</a></dd><dd><a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eNodesContainer-alignTo" href="#eNodesContainer-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align Abstract nodes container to.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></h4><dl class="function"><dt><a name="eNodesContainer-__delitem__" href="#eNodesContainer-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__getitem__" href="#eNodesContainer-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__hash__" href="#eNodesContainer-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__init__" href="#eNodesContainer-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, nodeList, extend<span class="parameter-default">=&lt;class 'typerig.proxy.objects.node.pNode'&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__len__" href="#eNodesContainer-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__repr__" href="#eNodesContainer-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__setitem__" href="#eNodesContainer-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-append" href="#eNodesContainer-append"><span class="function-name">append</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-applyTransform" href="#eNodesContainer-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-clone" href="#eNodesContainer-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-cloneTransform" href="#eNodesContainer-cloneTransform"><span class="function-name">cloneTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getBounds" href="#eNodesContainer-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getCoord" href="#eNodesContainer-getCoord"><span class="function-name">getCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getPosition" href="#eNodesContainer-getPosition"><span class="function-name">getPosition</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-insert" href="#eNodesContainer-insert"><span class="function-name">insert</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-reverse" href="#eNodesContainer-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-shift" href="#eNodesContainer-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-smartShift" href="#eNodesContainer-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></h4><dl class="descriptor"><dt>__dict__</dt>
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
<dt class="class"><h2><a name="pNode" href="#pNode">class <span class="class-name">pNode</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flNode object

Constructor:
        pNode(flNode)

Attributes:
        .fl (flNode): Original flNode 
        .parent (flContour): parent contour
        .contour (flContour): parent contour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pNode-__init__" href="#pNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-__repr__" href="#pNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleTo" href="#pNode-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleToNext" href="#pNode-angleToNext"><span class="function-name">angleToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleToPrev" href="#pNode-angleToPrev"><span class="function-name">angleToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-delSmartAngle" href="#pNode-delSmartAngle"><span class="function-name">delSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceTo" href="#pNode-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceToNext" href="#pNode-distanceToNext"><span class="function-name">distanceToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceToPrev" href="#pNode-distanceToPrev"><span class="function-name">distanceToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getContour" href="#pNode-getContour"><span class="function-name">getContour</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getMaxY" href="#pNode-getMaxY"><span class="function-name">getMaxY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getMinY" href="#pNode-getMinY"><span class="function-name">getMinY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getNext" href="#pNode-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getNextOn" href="#pNode-getNextOn"><span class="function-name">getNextOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getOn" href="#pNode-getOn"><span class="function-name">getOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getPrev" href="#pNode-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getPrevOn" href="#pNode-getPrevOn"><span class="function-name">getPrevOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSegment" href="#pNode-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSegmentNodes" href="#pNode-getSegmentNodes"><span class="function-name">getSegmentNodes</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSmartAngle" href="#pNode-getSmartAngle"><span class="function-name">getSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Effects --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSmartAngleRadius" href="#pNode-getSmartAngleRadius"><span class="function-name">getSmartAngleRadius</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getTime" href="#pNode-getTime"><span class="function-name">getTime</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertAfter" href="#pNode-insertAfter"><span class="function-name">insertAfter</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertAfterDist" href="#pNode-insertAfterDist"><span class="function-name">insertAfterDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertBefore" href="#pNode-insertBefore"><span class="function-name">insertBefore</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertBeforeDist" href="#pNode-insertBeforeDist"><span class="function-name">insertBeforeDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-reloc" href="#pNode-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-remove" href="#pNode-remove"><span class="function-name">remove</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-setSmartAngle" href="#pNode-setSmartAngle"><span class="function-name">setSmartAngle</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-setSmartAngleRadius" href="#pNode-setSmartAngleRadius"><span class="function-name">setSmartAngleRadius</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-shift" href="#pNode-shift"><span class="function-name">shift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-smartReloc" href="#pNode-smartReloc"><span class="function-name">smartReloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node and adjacent BCPs to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-smartShift" href="#pNode-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node and adjacent BCPs by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-update" href="#pNode-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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
<dt class="class"><h2><a name="pNodesContainer" href="#pNodesContainer">class <span class="class-name">pNodesContainer</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Abstract nodes container

Constructor:
        pNodesContainer(list(flNode))

Attributes:</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pNodesContainer-__delitem__" href="#pNodesContainer-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__getitem__" href="#pNodesContainer-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__hash__" href="#pNodesContainer-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__init__" href="#pNodesContainer-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, nodeList, extend<span class="parameter-default">=&lt;class 'typerig.proxy.objects.node.pNode'&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__len__" href="#pNodesContainer-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__repr__" href="#pNodesContainer-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__setitem__" href="#pNodesContainer-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-append" href="#pNodesContainer-append"><span class="function-name">append</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-applyTransform" href="#pNodesContainer-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-clone" href="#pNodesContainer-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-cloneTransform" href="#pNodesContainer-cloneTransform"><span class="function-name">cloneTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getBounds" href="#pNodesContainer-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getCoord" href="#pNodesContainer-getCoord"><span class="function-name">getCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getPosition" href="#pNodesContainer-getPosition"><span class="function-name">getPosition</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-insert" href="#pNodesContainer-insert"><span class="function-name">insert</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-reverse" href="#pNodesContainer-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-shift" href="#pNodesContainer-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-smartShift" href="#pNodesContainer-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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


<a name="typerig.proxy.objects.node.pNode"></a>

## `pNode`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.node.pNode</span> = <a name="typerig.proxy.objects.node.pNode" href="#typerig.proxy.objects.node.pNode">class pNode</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flNode object

Constructor:
        pNode(flNode)

Attributes:
        .fl (flNode): Original flNode 
        .parent (flContour): parent contour
        .contour (flContour): parent contour</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pNode-__init__" href="#pNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-__repr__" href="#pNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleTo" href="#pNode-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleToNext" href="#pNode-angleToNext"><span class="function-name">angleToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-angleToPrev" href="#pNode-angleToPrev"><span class="function-name">angleToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-delSmartAngle" href="#pNode-delSmartAngle"><span class="function-name">delSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceTo" href="#pNode-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceToNext" href="#pNode-distanceToNext"><span class="function-name">distanceToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-distanceToPrev" href="#pNode-distanceToPrev"><span class="function-name">distanceToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getContour" href="#pNode-getContour"><span class="function-name">getContour</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getMaxY" href="#pNode-getMaxY"><span class="function-name">getMaxY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getMinY" href="#pNode-getMinY"><span class="function-name">getMinY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getNext" href="#pNode-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getNextOn" href="#pNode-getNextOn"><span class="function-name">getNextOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getOn" href="#pNode-getOn"><span class="function-name">getOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getPrev" href="#pNode-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getPrevOn" href="#pNode-getPrevOn"><span class="function-name">getPrevOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSegment" href="#pNode-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSegmentNodes" href="#pNode-getSegmentNodes"><span class="function-name">getSegmentNodes</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSmartAngle" href="#pNode-getSmartAngle"><span class="function-name">getSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Effects --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getSmartAngleRadius" href="#pNode-getSmartAngleRadius"><span class="function-name">getSmartAngleRadius</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-getTime" href="#pNode-getTime"><span class="function-name">getTime</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertAfter" href="#pNode-insertAfter"><span class="function-name">insertAfter</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertAfterDist" href="#pNode-insertAfterDist"><span class="function-name">insertAfterDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertBefore" href="#pNode-insertBefore"><span class="function-name">insertBefore</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-insertBeforeDist" href="#pNode-insertBeforeDist"><span class="function-name">insertBeforeDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-reloc" href="#pNode-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-remove" href="#pNode-remove"><span class="function-name">remove</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-setSmartAngle" href="#pNode-setSmartAngle"><span class="function-name">setSmartAngle</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-setSmartAngleRadius" href="#pNode-setSmartAngleRadius"><span class="function-name">setSmartAngleRadius</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-shift" href="#pNode-shift"><span class="function-name">shift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-smartReloc" href="#pNode-smartReloc"><span class="function-name">smartReloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node and adjacent BCPs to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-smartShift" href="#pNode-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node and adjacent BCPs by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="pNode-update" href="#pNode-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

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


<a name="typerig.proxy.objects.node.pNode.reloc"></a>

### `reloc`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.pNode.reloc" href="#-typerig.proxy.objects.node.pNode.reloc"><span class="function-name">typerig.proxy.objects.node.pNode.reloc</span></a> = reloc<span class="argspec">(self, newX, newY)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#pNode">typerig.proxy.objects.node.pNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node to new coordinates</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.pNode.shift"></a>

### `shift`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.pNode.shift" href="#-typerig.proxy.objects.node.pNode.shift"><span class="function-name">typerig.proxy.objects.node.pNode.shift</span></a> = shift<span class="argspec">(self, deltaX, deltaY)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#pNode">typerig.proxy.objects.node.pNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Shift the node by given amout</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.pNode.smartReloc"></a>

### `smartReloc`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.pNode.smartReloc" href="#-typerig.proxy.objects.node.pNode.smartReloc"><span class="function-name">typerig.proxy.objects.node.pNode.smartReloc</span></a> = smartReloc<span class="argspec">(self, newX, newY)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#pNode">typerig.proxy.objects.node.pNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node and adjacent BCPs to new coordinates</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.pNode.smartShift"></a>

### `smartShift`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.pNode.smartShift" href="#-typerig.proxy.objects.node.pNode.smartShift"><span class="function-name">typerig.proxy.objects.node.pNode.smartShift</span></a> = smartShift<span class="argspec">(self, deltaX, deltaY)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#pNode">typerig.proxy.objects.node.pNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Shift the node and adjacent BCPs by given amout</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.pNodesContainer"></a>

## `pNodesContainer`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.node.pNodesContainer</span> = <a name="typerig.proxy.objects.node.pNodesContainer" href="#typerig.proxy.objects.node.pNodesContainer">class pNodesContainer</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Abstract nodes container

Constructor:
        pNodesContainer(list(flNode))

Attributes:</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pNodesContainer-__delitem__" href="#pNodesContainer-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__getitem__" href="#pNodesContainer-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__hash__" href="#pNodesContainer-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__init__" href="#pNodesContainer-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, nodeList, extend<span class="parameter-default">=&lt;class 'typerig.proxy.objects.node.pNode'&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__len__" href="#pNodesContainer-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__repr__" href="#pNodesContainer-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-__setitem__" href="#pNodesContainer-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-append" href="#pNodesContainer-append"><span class="function-name">append</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-applyTransform" href="#pNodesContainer-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-clone" href="#pNodesContainer-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-cloneTransform" href="#pNodesContainer-cloneTransform"><span class="function-name">cloneTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getBounds" href="#pNodesContainer-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getCoord" href="#pNodesContainer-getCoord"><span class="function-name">getCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-getPosition" href="#pNodesContainer-getPosition"><span class="function-name">getPosition</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-insert" href="#pNodesContainer-insert"><span class="function-name">insert</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-reverse" href="#pNodesContainer-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-shift" href="#pNodesContainer-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pNodesContainer-smartShift" href="#pNodesContainer-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

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


<a name="typerig.proxy.objects.node.eNode"></a>

## `eNode`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.node.eNode</span> = <a name="typerig.proxy.objects.node.eNode" href="#typerig.proxy.objects.node.eNode">class eNode</a>(<a href="./typerig.proxy.objects.node.html#pNode">pNode</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of the Proxy Node, adding some advanced functionality

Constructor:
        eNode(flNode)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.node.html#eNode">eNode</a></dd><dd><a href="./typerig.proxy.objects.node.html#pNode">pNode</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eNode-alignTo" href="#eNode-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align current node to a node or line given.
Arguments:
        entity (flNode, pNode, eNode or Line)
        align (tuple(Align_X (bool), Align_Y (bool))</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-asCoord" href="#eNode-asCoord"><span class="function-name">asCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the node.</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerMitre" href="#eNode-cornerMitre"><span class="function-name">cornerMitre</span></a><span class="argspec">(self, mitreSize<span class="parameter-default">=5</span>, isRadius<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Corner operations ---------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerRound" href="#eNode-cornerRound"><span class="function-name">cornerRound</span></a><span class="argspec">(self, size<span class="parameter-default">=5</span>, proportion<span class="parameter-default">=None</span>, curvature<span class="parameter-default">=None</span>, isRadius<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerTrap" href="#eNode-cornerTrap"><span class="function-name">cornerTrap</span></a><span class="argspec">(self, aperture<span class="parameter-default">=10</span>, depth<span class="parameter-default">=20</span>, trap<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given aperture.

Arguments:
        aperture (float): Width of the traps mouth (opening);
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom.

Returns:
        tuple(flNode, flNode, flNode, flNode)</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-cornerTrapInc" href="#eNode-cornerTrapInc"><span class="function-name">cornerTrapInc</span></a><span class="argspec">(self, incision<span class="parameter-default">=10</span>, depth<span class="parameter-default">=50</span>, trap<span class="parameter-default">=2</span>, smooth<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given incision into the glyph flesh.

Arguments:
        incision (float): How much to cut into glyphs flesh based from that corner inward;
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom;
        smooth (bool): Creates a smooth trap.

Returns:
        tuple(flNode, flNode, flNode, flNode) four base (ON) nodes of the trap.</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffTo" href="#eNode-diffTo"><span class="function-name">diffTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffToNext" href="#eNode-diffToNext"><span class="function-name">diffToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-diffToPrev" href="#eNode-diffToPrev"><span class="function-name">diffToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNextLine" href="#eNode-getNextLine"><span class="function-name">getNextLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrevLine" href="#eNode-getPrevLine"><span class="function-name">getPrevLine</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-interpShift" href="#eNode-interpShift"><span class="function-name">interpShift</span></a><span class="argspec">(self, shift_x, shift_y)</span></dt><dd>

<pre class="doc" markdown="0">Interpolated move aka Interpolated Nudge.

Arguments:
        shift_x, shift_y (float)</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarReloc" href="#eNode-polarReloc"><span class="function-name">polarReloc</span></a><span class="argspec">(self, angle, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarRelocFromPrev" href="#eNode-polarRelocFromPrev"><span class="function-name">polarRelocFromPrev</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarTo" href="#eNode-polarTo"><span class="function-name">polarTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarToNext" href="#eNode-polarToNext"><span class="function-name">polarToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-polarToPrev" href="#eNode-polarToPrev"><span class="function-name">polarToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shiftFromNext" href="#eNode-shiftFromNext"><span class="function-name">shiftFromNext</span></a><span class="argspec">(self, diffX, diffY)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shiftFromPrev" href="#eNode-shiftFromPrev"><span class="function-name">shiftFromPrev</span></a><span class="argspec">(self, diffX, diffY)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-slantShift" href="#eNode-slantShift"><span class="function-name">slantShift</span></a><span class="argspec">(self, shift_x, shift_y, angle)</span></dt><dd>

<pre class="doc" markdown="0">Slanted move - move a node (in inclined space) according to Y coordinate slanted at given angle.

Arguments:
        shift_x, shift_y (float)
        angle (float): Angle in degrees</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartPolarReloc" href="#eNode-smartPolarReloc"><span class="function-name">smartPolarReloc</span></a><span class="argspec">(self, angle, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.node.html#pNode">pNode</a></h4><dl class="function"><dt><a name="eNode-__init__" href="#eNode-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-__repr__" href="#eNode-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleTo" href="#eNode-angleTo"><span class="function-name">angleTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleToNext" href="#eNode-angleToNext"><span class="function-name">angleToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-angleToPrev" href="#eNode-angleToPrev"><span class="function-name">angleToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-delSmartAngle" href="#eNode-delSmartAngle"><span class="function-name">delSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceTo" href="#eNode-distanceTo"><span class="function-name">distanceTo</span></a><span class="argspec">(self, node)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceToNext" href="#eNode-distanceToNext"><span class="function-name">distanceToNext</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-distanceToPrev" href="#eNode-distanceToPrev"><span class="function-name">distanceToPrev</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getContour" href="#eNode-getContour"><span class="function-name">getContour</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getMaxY" href="#eNode-getMaxY"><span class="function-name">getMaxY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getMinY" href="#eNode-getMinY"><span class="function-name">getMinY</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNext" href="#eNode-getNext"><span class="function-name">getNext</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getNextOn" href="#eNode-getNextOn"><span class="function-name">getNextOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getOn" href="#eNode-getOn"><span class="function-name">getOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrev" href="#eNode-getPrev"><span class="function-name">getPrev</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getPrevOn" href="#eNode-getPrevOn"><span class="function-name">getPrevOn</span></a><span class="argspec">(self, naked<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSegment" href="#eNode-getSegment"><span class="function-name">getSegment</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSegmentNodes" href="#eNode-getSegmentNodes"><span class="function-name">getSegmentNodes</span></a><span class="argspec">(self, relativeTime<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSmartAngle" href="#eNode-getSmartAngle"><span class="function-name">getSmartAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Effects --------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getSmartAngleRadius" href="#eNode-getSmartAngleRadius"><span class="function-name">getSmartAngleRadius</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-getTime" href="#eNode-getTime"><span class="function-name">getTime</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertAfter" href="#eNode-insertAfter"><span class="function-name">insertAfter</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertAfterDist" href="#eNode-insertAfterDist"><span class="function-name">insertAfterDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertBefore" href="#eNode-insertBefore"><span class="function-name">insertBefore</span></a><span class="argspec">(self, time)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-insertBeforeDist" href="#eNode-insertBeforeDist"><span class="function-name">insertBeforeDist</span></a><span class="argspec">(self, distance)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-reloc" href="#eNode-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-remove" href="#eNode-remove"><span class="function-name">remove</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-setSmartAngle" href="#eNode-setSmartAngle"><span class="function-name">setSmartAngle</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-setSmartAngleRadius" href="#eNode-setSmartAngleRadius"><span class="function-name">setSmartAngleRadius</span></a><span class="argspec">(self, radius)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-shift" href="#eNode-shift"><span class="function-name">shift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartReloc" href="#eNode-smartReloc"><span class="function-name">smartReloc</span></a><span class="argspec">(self, newX, newY)</span></dt><dd>

<pre class="doc" markdown="0">Relocate the node and adjacent BCPs to new coordinates</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-smartShift" href="#eNode-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, deltaX, deltaY)</span></dt><dd>

<pre class="doc" markdown="0">Shift the node and adjacent BCPs by given amout</pre>

</dd></dl>
<dl class="function"><dt><a name="eNode-update" href="#eNode-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.node.html#pNode">pNode</a></h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.proxy.objects.node.eNode.asCoord"></a>

### `asCoord`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.asCoord" href="#-typerig.proxy.objects.node.eNode.asCoord"><span class="function-name">typerig.proxy.objects.node.eNode.asCoord</span></a> = asCoord<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns Coord object of the node.</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNode.cornerTrap"></a>

### `cornerTrap`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.cornerTrap" href="#-typerig.proxy.objects.node.eNode.cornerTrap"><span class="function-name">typerig.proxy.objects.node.eNode.cornerTrap</span></a> = cornerTrap<span class="argspec">(self, aperture<span class="parameter-default">=10</span>, depth<span class="parameter-default">=20</span>, trap<span class="parameter-default">=2</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given aperture.

Arguments:
        aperture (float): Width of the traps mouth (opening);
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom.

Returns:
        tuple(flNode, flNode, flNode, flNode)</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNode.cornerTrapInc"></a>

### `cornerTrapInc`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.cornerTrapInc" href="#-typerig.proxy.objects.node.eNode.cornerTrapInc"><span class="function-name">typerig.proxy.objects.node.eNode.cornerTrapInc</span></a> = cornerTrapInc<span class="argspec">(self, incision<span class="parameter-default">=10</span>, depth<span class="parameter-default">=50</span>, trap<span class="parameter-default">=2</span>, smooth<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Trap a corner by given incision into the glyph flesh.

Arguments:
        incision (float): How much to cut into glyphs flesh based from that corner inward;
        depth (float): Length of the traps sides;
        trap (float): Width of the traps bottom;
        smooth (bool): Creates a smooth trap.

Returns:
        tuple(flNode, flNode, flNode, flNode) four base (ON) nodes of the trap.</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNode.interpShift"></a>

### `interpShift`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.interpShift" href="#-typerig.proxy.objects.node.eNode.interpShift"><span class="function-name">typerig.proxy.objects.node.eNode.interpShift</span></a> = interpShift<span class="argspec">(self, shift_x, shift_y)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Interpolated move aka Interpolated Nudge.

Arguments:
        shift_x, shift_y (float)</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNode.slantShift"></a>

### `slantShift`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.slantShift" href="#-typerig.proxy.objects.node.eNode.slantShift"><span class="function-name">typerig.proxy.objects.node.eNode.slantShift</span></a> = slantShift<span class="argspec">(self, shift_x, shift_y, angle)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Slanted move - move a node (in inclined space) according to Y coordinate slanted at given angle.

Arguments:
        shift_x, shift_y (float)
        angle (float): Angle in degrees</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNode.alignTo"></a>

### `alignTo`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNode.alignTo" href="#-typerig.proxy.objects.node.eNode.alignTo"><span class="function-name">typerig.proxy.objects.node.eNode.alignTo</span></a> = alignTo<span class="argspec">(self, entity, align<span class="parameter-default">=(True, True)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNode">typerig.proxy.objects.node.eNode</a> method</span></dt><dd>

<pre class="doc" markdown="0">Align current node to a node or line given.
Arguments:
        entity (flNode, pNode, eNode or Line)
        align (tuple(Align_X (bool), Align_Y (bool))</pre>

</dd></dl>



<a name="typerig.proxy.objects.node.eNodesContainer"></a>

## `eNodesContainer`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.node.eNodesContainer</span> = <a name="typerig.proxy.objects.node.eNodesContainer" href="#typerig.proxy.objects.node.eNodesContainer">class eNodesContainer</a>(<a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Extended representation of Abstract nodes container

Constructor:
        eNodesContainer(list(flNode))</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.node.html#eNodesContainer">eNodesContainer</a></dd><dd><a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eNodesContainer-alignTo" href="#eNodesContainer-alignTo"><span class="function-name">alignTo</span></a><span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0">Align Abstract nodes container to.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></h4><dl class="function"><dt><a name="eNodesContainer-__delitem__" href="#eNodesContainer-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__getitem__" href="#eNodesContainer-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__hash__" href="#eNodesContainer-__hash__"><span class="function-name">__hash__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__init__" href="#eNodesContainer-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, nodeList, extend<span class="parameter-default">=&lt;class 'typerig.proxy.objects.node.pNode'&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__len__" href="#eNodesContainer-__len__"><span class="function-name">__len__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__repr__" href="#eNodesContainer-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-__setitem__" href="#eNodesContainer-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-append" href="#eNodesContainer-append"><span class="function-name">append</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-applyTransform" href="#eNodesContainer-applyTransform"><span class="function-name">applyTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-clone" href="#eNodesContainer-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-cloneTransform" href="#eNodesContainer-cloneTransform"><span class="function-name">cloneTransform</span></a><span class="argspec">(self, transform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getBounds" href="#eNodesContainer-getBounds"><span class="function-name">getBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getCoord" href="#eNodesContainer-getCoord"><span class="function-name">getCoord</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-getPosition" href="#eNodesContainer-getPosition"><span class="function-name">getPosition</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-insert" href="#eNodesContainer-insert"><span class="function-name">insert</span></a><span class="argspec">(self, index, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-reverse" href="#eNodesContainer-reverse"><span class="function-name">reverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-shift" href="#eNodesContainer-shift"><span class="function-name">shift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eNodesContainer-smartShift" href="#eNodesContainer-smartShift"><span class="function-name">smartShift</span></a><span class="argspec">(self, dx, dy)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.node.html#pNodesContainer">pNodesContainer</a></h4><dl class="descriptor"><dt>__dict__</dt>
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


<a name="typerig.proxy.objects.node.eNodesContainer.alignTo"></a>

### `alignTo`


<dl class="function"><dt><a name="-typerig.proxy.objects.node.eNodesContainer.alignTo" href="#-typerig.proxy.objects.node.eNodesContainer.alignTo"><span class="function-name">typerig.proxy.objects.node.eNodesContainer.alignTo</span></a> = alignTo<span class="argspec">(self, entity, alignMode<span class="parameter-default">=''</span>, align<span class="parameter-default">=(True, True)</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.node.html#eNodesContainer">typerig.proxy.objects.node.eNodesContainer</a> method</span></dt><dd>

<pre class="doc" markdown="0">Align Abstract nodes container to.
Arguments:
        entity ()
        alignMode (String) : L(left), R(right), C(center), T(top), B(bottom), E(vertical center) !ORDER MATTERS</pre>

</dd></dl>

