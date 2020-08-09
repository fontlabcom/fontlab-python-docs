

<a name="fontlab.flPackage"></a>

# `flPackage`


<dt class="class"><h2><span class="class-name">fontlab.flPackage</span> = <a name="fontlab.flPackage" href="#fontlab.flPackage">class flPackage</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">flPackage representation

Constructors:
  flPackage()
  flPackage(flObject)
  flPackage(fgFont)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="flPackage-__delattr__" href="#flPackage-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__eq__" href="#flPackage-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__ge__" href="#flPackage-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__getattribute__" href="#flPackage-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__gt__" href="#flPackage-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__init__" href="#flPackage-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__init__">__init__</a>(...) initializes x; see help(<a href="#fontlab.flPackage-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__le__" href="#flPackage-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__lt__" href="#flPackage-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__ne__" href="#flPackage-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__repr__" href="#flPackage-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-__setattr__" href="#flPackage-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.flPackage-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-activateGlyph" href="#flPackage-activateGlyph"><span class="function-name">activateGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-activateGlyph">activateGlyph</a>(flGlyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-addAxis" href="#flPackage-addAxis"><span class="function-name">addAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-addAxis">addAxis</a>(flAxis variable)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-addGlyph" href="#flPackage-addGlyph"><span class="function-name">addGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-addGlyph">addGlyph</a>(fgGlyph / flGlyph )</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-addInstance" href="#flPackage-addInstance"><span class="function-name">addInstance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-addInstance">addInstance</a>(const flInstance &instance)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-addMaster" href="#flPackage-addMaster"><span class="function-name">addMaster</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-addMaster">addMaster</a>(string master_name, bool create_glyphs, flPackage source, string source_layer_name, bool copy_metrics, bool create_missing_glyphs[, flLocation location])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-assignData" href="#flPackage-assignData"><span class="function-name">assignData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-assignData">assignData</a>(const flPackage &package)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-autohintGlyphs" href="#flPackage-autohintGlyphs"><span class="function-name">autohintGlyphs</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-autohintGlyphs">autohintGlyphs</a>(QList<flGlyph> glyphs, bool make_hints)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-buildShapeDataNames" href="#flPackage-buildShapeDataNames"><span class="function-name">buildShapeDataNames</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QSet<string> <a href="#fontlab.flPackage-buildShapeDataNames">buildShapeDataNames</a>(objId exclude[, string layer_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-can_interpolate" href="#flPackage-can_interpolate"><span class="function-name">can_interpolate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-can_interpolate">can_interpolate</a>([string master_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-changed" href="#flPackage-changed"><span class="function-name">changed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-changed">changed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-checkAxisName" href="#flPackage-checkAxisName"><span class="function-name">checkAxisName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-checkAxisName">checkAxisName</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-checkInitHistoryState" href="#flPackage-checkInitHistoryState"><span class="function-name">checkInitHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-checkInitHistoryState">checkInitHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-checkVariableName" href="#flPackage-checkVariableName"><span class="function-name">checkVariableName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-checkVariableName">checkVariableName</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearAboveHistory" href="#flPackage-clearAboveHistory"><span class="function-name">clearAboveHistory</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearAboveHistory">clearAboveHistory</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearActiveGlyphs" href="#flPackage-clearActiveGlyphs"><span class="function-name">clearActiveGlyphs</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearActiveGlyphs">clearActiveGlyphs</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearFlag" href="#flPackage-clearFlag"><span class="function-name">clearFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearFlag">clearFlag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearFlags" href="#flPackage-clearFlags"><span class="function-name">clearFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearFlags">clearFlags</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearInstances" href="#flPackage-clearInstances"><span class="function-name">clearInstances</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearInstances">clearInstances</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clearMasters" href="#flPackage-clearMasters"><span class="function-name">clearMasters</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-clearMasters">clearMasters</a>(bool release)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-clone" href="#flPackage-clone"><span class="function-name">clone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-close" href="#flPackage-close"><span class="function-name">close</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-close">close</a>(save=False) - Close the font</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-collectNames" href="#flPackage-collectNames"><span class="function-name">collectNames</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-collectNames">collectNames</a>(StorageInfo * storage)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-collectShapes" href="#flPackage-collectShapes"><span class="function-name">collectShapes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<flShape>/Nothing <a href="#fontlab.flPackage-collectShapes">collectShapes</a>(flShape, string layer_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-completeData" href="#flPackage-completeData"><span class="function-name">completeData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-completeData">completeData</a>([bool fg_data = false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-convertZonesToGuidelines" href="#flPackage-convertZonesToGuidelines"><span class="function-name">convertZonesToGuidelines</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-convertZonesToGuidelines">convertZonesToGuidelines</a>(flZones zonesT, flZones zonesB)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-createHistoryState" href="#flPackage-createHistoryState"><span class="function-name">createHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-createHistoryState">createHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-currentHistoryState" href="#flPackage-currentHistoryState"><span class="function-name">currentHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-deleteGlyph" href="#flPackage-deleteGlyph"><span class="function-name">deleteGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-deleteGlyph">deleteGlyph</a>(fgGlyph / flGlyph )</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-deleteGroups" href="#flPackage-deleteGroups"><span class="function-name">deleteGroups</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-deleteGroups">deleteGroups</a>(QSet<uint> ids, bool deleteDependentContent)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-ensureProteusData" href="#flPackage-ensureProteusData"><span class="function-name">ensureProteusData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-ensureProteusData">ensureProteusData</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-family_zones" href="#flPackage-family_zones"><span class="function-name">family_zones</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flZone)& <a href="#fontlab.flPackage-family_zones">family_zones</a>(bool top)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-featuresContainer" href="#flPackage-featuresContainer"><span class="function-name">featuresContainer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flPackage-featuresContainer">featuresContainer</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findAxis" href="#flPackage-findAxis"><span class="function-name">findAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flAxis/Nothing <a href="#fontlab.flPackage-findAxis">findAxis</a>(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findAxisShort" href="#flPackage-findAxisShort"><span class="function-name">findAxisShort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flAxis/Nothing <a href="#fontlab.flPackage-findAxisShort">findAxisShort</a>(string short_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findFgId" href="#flPackage-findFgId"><span class="function-name">findFgId</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flPackage-findFgId">findFgId</a>(uint id)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findGroup" href="#flPackage-findGroup"><span class="function-name">findGroup</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fg::GlyphGroup* <a href="#fontlab.flPackage-findGroup">findGroup</a>(int _id)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findName" href="#flPackage-findName"><span class="function-name">findName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flPackage-findName">findName</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findNameId" href="#flPackage-findNameId"><span class="function-name">findNameId</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flPackage-findNameId">findNameId</a>(uint fg_id)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findNewName" href="#flPackage-findNewName"><span class="function-name">findNewName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-findNewName">findNewName</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findShapeRoot" href="#flPackage-findShapeRoot"><span class="function-name">findShapeRoot</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flPackage-findShapeRoot">findShapeRoot</a>(flShapeData shape_data)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findStem" href="#flPackage-findStem"><span class="function-name">findStem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flPackage-findStem">findStem</a>(string n, bool b, bool loose)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findUnicode" href="#flPackage-findUnicode"><span class="function-name">findUnicode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph <a href="#fontlab.flPackage-findUnicode">findUnicode</a>(uint uni)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-findZone" href="#flPackage-findZone"><span class="function-name">findZone</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flPackage-findZone">findZone</a>(string n, bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-flag" href="#flPackage-flag"><span class="function-name">flag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-flag">flag</a>(uint f)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-generateGlyph" href="#flPackage-generateGlyph"><span class="function-name">generateGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">( QList<GlyphComponent>, double width )/Nothing <a href="#fontlab.flPackage-generateGlyph">generateGlyph</a>(string recipe, string layer_name, FontMetrics metrics, bool rtl)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getAccentsInfo" href="#flPackage-getAccentsInfo"><span class="function-name">getAccentsInfo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(AccentInfo)/Nothing <a href="#fontlab.flPackage-getAccentsInfo">getAccentsInfo</a>(flLayer, flPinPoint)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getAllGroups" href="#flPackage-getAllGroups"><span class="function-name">getAllGroups</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( (bool kernGroup, string groupName, int id, int mark, list(string glyphName) )/Nothing <a href="#fontlab.flPackage-getAllGroups">getAllGroups</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getAxisName" href="#flPackage-getAxisName"><span class="function-name">getAxisName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-getAxisName">getAxisName</a>(string short_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getAxisShortName" href="#flPackage-getAxisShortName"><span class="function-name">getAxisShortName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-getAxisShortName">getAxisShortName</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getLayerName" href="#flPackage-getLayerName"><span class="function-name">getLayerName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-getLayerName">getLayerName</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getMarkOffset" href="#flPackage-getMarkOffset"><span class="function-name">getMarkOffset</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing <a href="#fontlab.flPackage-getMarkOffset">getMarkOffset</a>(flGlyph g1, flGlyph g2)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getProperties" href="#flPackage-getProperties"><span class="function-name">getProperties</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getProperty" href="#flPackage-getProperty"><span class="function-name">getProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-getProperty">getProperty</a>('key') - get object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getPropertyFloat" href="#flPackage-getPropertyFloat"><span class="function-name">getPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-getPropertyFloat">getPropertyFloat</a>('key') - get float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getPropertyInt" href="#flPackage-getPropertyInt"><span class="function-name">getPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-getPropertyInt">getPropertyInt</a>('key') - get int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-getShapes" href="#flPackage-getShapes"><span class="function-name">getShapes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<int>/Nothing <a href="#fontlab.flPackage-getShapes">getShapes</a>(string filter[, string layer_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasAxis" href="#flPackage-hasAxis"><span class="function-name">hasAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasAxis">hasAxis</a>(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasAxisShort" href="#flPackage-hasAxisShort"><span class="function-name">hasAxisShort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasAxisShort">hasAxisShort</a>(string short_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasGuides" href="#flPackage-hasGuides"><span class="function-name">hasGuides</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasGuides">hasGuides</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasHistoryState" href="#flPackage-hasHistoryState"><span class="function-name">hasHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-hasHistoryState">hasHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasMaster" href="#flPackage-hasMaster"><span class="function-name">hasMaster</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasMaster">hasMaster</a>(string name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasName" href="#flPackage-hasName"><span class="function-name">hasName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasName">hasName</a>(string name[, bool relaxed=false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasPackageHistoryStorages" href="#flPackage-hasPackageHistoryStorages"><span class="function-name">hasPackageHistoryStorages</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasPackageHistoryStorages">hasPackageHistoryStorages</a>(uint to_history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasZones" href="#flPackage-hasZones"><span class="function-name">hasZones</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasZones">hasZones</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-historyStack" href="#flPackage-historyStack"><span class="function-name">historyStack</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flPackage-historyStack">historyStack</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-historyStates" href="#flPackage-historyStates"><span class="function-name">historyStates</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-historyStates">historyStates</a>(bool accepted_state)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-independedAll" href="#flPackage-independedAll"><span class="function-name">independedAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-independedAll">independedAll</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-initItr" href="#flPackage-initItr"><span class="function-name">initItr</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-initItr">initItr</a>(fgTTInterpreter itr)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-initItrGlyph" href="#flPackage-initItrGlyph"><span class="function-name">initItrGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-initItrGlyph">initItrGlyph</a>(fgTTInterpreter itr, flGlyph glyph)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-initialHistoryState" href="#flPackage-initialHistoryState"><span class="function-name">initialHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-isComponent" href="#flPackage-isComponent"><span class="function-name">isComponent</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flGlyph, QTransform) <a href="#fontlab.flPackage-isComponent">isComponent</a>(flShapeData[, string layer_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-isEqual" href="#flPackage-isEqual"><span class="function-name">isEqual</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-isEqual">isEqual</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-kerning" href="#flPackage-kerning"><span class="function-name">kerning</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgKerning <a href="#fontlab.flPackage-kerning">kerning</a>([string master_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-kerningContainer" href="#flPackage-kerningContainer"><span class="function-name">kerningContainer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flPackage-kerningContainer">kerningContainer</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-location" href="#flPackage-location"><span class="function-name">location</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLocation& <a href="#fontlab.flPackage-location">location</a>([string master_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-makeShapeDataName" href="#flPackage-makeShapeDataName"><span class="function-name">makeShapeDataName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-makeShapeDataName">makeShapeDataName</a>(string name, objId _id, string layer_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-mastersContainer" href="#flPackage-mastersContainer"><span class="function-name">mastersContainer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flPackage-mastersContainer">mastersContainer</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-optimizeShapeTransformations" href="#flPackage-optimizeShapeTransformations"><span class="function-name">optimizeShapeTransformations</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-optimizeShapeTransformations">optimizeShapeTransformations</a>(QList<flObject> changes)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-optimizeStemData" href="#flPackage-optimizeStemData"><span class="function-name">optimizeStemData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flStems stemsH, flStems stemsV) <a href="#fontlab.flPackage-optimizeStemData">optimizeStemData</a>(flStems stemsH, flStems stemsV)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-prepareAxes" href="#flPackage-prepareAxes"><span class="function-name">prepareAxes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<flAxis>/Nothing <a href="#fontlab.flPackage-prepareAxes">prepareAxes</a>(QList<flPackage> packages, QList<flGlyph> glyphs)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-prepareFontGateData" href="#flPackage-prepareFontGateData"><span class="function-name">prepareFontGateData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-prepareFontGateData">prepareFontGateData</a>(bool prepare_tth)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-preparePropertiesData" href="#flPackage-preparePropertiesData"><span class="function-name">preparePropertiesData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-preparePropertiesData">preparePropertiesData</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-projectPackageName" href="#flPackage-projectPackageName"><span class="function-name">projectPackageName</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-projectPackageName">projectPackageName</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-referencesCount" href="#flPackage-referencesCount"><span class="function-name">referencesCount</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flPackage-referencesCount">referencesCount</a>(uint shapeDataId)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-release" href="#flPackage-release"><span class="function-name">release</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-release">release</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-remove" href="#flPackage-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-remove">remove</a>([flObject])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-removeChild" href="#flPackage-removeChild"><span class="function-name">removeChild</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-removeChild">removeChild</a>(flObject)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-removeMaster" href="#flPackage-removeMaster"><span class="function-name">removeMaster</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-removeMaster">removeMaster</a>(string name, bool remove_glyph_masters)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-removeProperty" href="#flPackage-removeProperty"><span class="function-name">removeProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-removeProperty">removeProperty</a>('key')</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-renameGlyph" href="#flPackage-renameGlyph"><span class="function-name">renameGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-renameGlyph">renameGlyph</a>(fgGlyph glyph, string name, bool rename)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-renameMaster" href="#flPackage-renameMaster"><span class="function-name">renameMaster</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-renameMaster">renameMaster</a>(string old_name, string new_name)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-replaceGlyph" href="#flPackage-replaceGlyph"><span class="function-name">replaceGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-replaceGlyph">replaceGlyph</a>(fgGlyph target, fgGlyph newGlyph, bool rename)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-replaceShapeWithReference" href="#flPackage-replaceShapeWithReference"><span class="function-name">replaceShapeWithReference</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShape/Nothing <a href="#fontlab.flPackage-replaceShapeWithReference">replaceShapeWithReference</a>(flShape shape, bool process[, string layer_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-resetPackage" href="#flPackage-resetPackage"><span class="function-name">resetPackage</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-resetPackage">resetPackage</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-resetStemData" href="#flPackage-resetStemData"><span class="function-name">resetStemData</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flStems stemsH, flStems stemsV) <a href="#fontlab.flPackage-resetStemData">resetStemData</a>(flStems stemsH, flStems stemsV)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-restoreHistoryState" href="#flPackage-restoreHistoryState"><span class="function-name">restoreHistoryState</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-restoreHistoryState">restoreHistoryState</a>(uint history_ix)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setAxis" href="#flPackage-setAxis"><span class="function-name">setAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setAxis">setAxis</a>(const flAxis &p)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setFlag" href="#flPackage-setFlag"><span class="function-name">setFlag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setFlag">setFlag</a>(uint f [, bool value])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setLocation" href="#flPackage-setLocation"><span class="function-name">setLocation</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setLocation">setLocation</a>(flLocation location[, string master_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setMaster" href="#flPackage-setMaster"><span class="function-name">setMaster</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setMaster">setMaster</a>(string name[, bool notify = false])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setProperty" href="#flPackage-setProperty"><span class="function-name">setProperty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setProperty">setProperty</a>('key', value) - set object property by 'key' or number</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setPropertyFloat" href="#flPackage-setPropertyFloat"><span class="function-name">setPropertyFloat</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setPropertyFloat">setPropertyFloat</a>('key', value) - set float object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setPropertyInt" href="#flPackage-setPropertyInt"><span class="function-name">setPropertyInt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setPropertyInt">setPropertyInt</a>('key', value) - set int object property by 'key'</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-setUpm" href="#flPackage-setUpm"><span class="function-name">setUpm</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-setUpm">setUpm</a>(int upm, bool scale)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_ascender_locked" href="#flPackage-set_ascender_locked"><span class="function-name">set_ascender_locked</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_ascender_locked">set_ascender_locked</a>(bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_capsHeight_locked" href="#flPackage-set_capsHeight_locked"><span class="function-name">set_capsHeight_locked</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_capsHeight_locked">set_capsHeight_locked</a>(bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_descender_locked" href="#flPackage-set_descender_locked"><span class="function-name">set_descender_locked</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_descender_locked">set_descender_locked</a>(bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_interpolate" href="#flPackage-set_interpolate"><span class="function-name">set_interpolate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_interpolate">set_interpolate</a>(bool b[, string master_name])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_measurement_locked" href="#flPackage-set_measurement_locked"><span class="function-name">set_measurement_locked</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_measurement_locked">set_measurement_locked</a>(bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-set_xHeight_locked" href="#flPackage-set_xHeight_locked"><span class="function-name">set_xHeight_locked</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-set_xHeight_locked">set_xHeight_locked</a>(bool b)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-stems" href="#flPackage-stems"><span class="function-name">stems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flStem)& <a href="#fontlab.flPackage-stems">stems</a>(HintingDataType, bool top)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-store_font_info" href="#flPackage-store_font_info"><span class="function-name">store_font_info</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-store_font_info">store_font_info</a>(fg::Package *package)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-store_hinting_data" href="#flPackage-store_hinting_data"><span class="function-name">store_hinting_data</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-store_hinting_data">store_hinting_data</a>(fgPackage package)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-styleCode" href="#flPackage-styleCode"><span class="function-name">styleCode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">unsigned char <a href="#fontlab.flPackage-styleCode">styleCode</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-tag" href="#flPackage-tag"><span class="function-name">tag</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-tag">tag</a>([string])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-title_name" href="#flPackage-title_name"><span class="function-name">title_name</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string <a href="#fontlab.flPackage-title_name">title_name</a>([bool force_full = true])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-tthRenameStems" href="#flPackage-tthRenameStems"><span class="function-name">tthRenameStems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-tthRenameStems">tthRenameStems</a>(QMap<QString, QString> map_h, QMap<QString, QString> map_v)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-tthRenameZones" href="#flPackage-tthRenameZones"><span class="function-name">tthRenameZones</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-tthRenameZones">tthRenameZones</a>(QMap<QString, QString> map_top, QMap<QString, QString> map_bottom)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-update" href="#flPackage-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-update">update</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-updateAxesMap" href="#flPackage-updateAxesMap"><span class="function-name">updateAxesMap</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-updateAxesMap">updateAxesMap</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-updateFontMetrics" href="#flPackage-updateFontMetrics"><span class="function-name">updateFontMetrics</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-updateFontMetrics">updateFontMetrics</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-updateShapeReferenceCount" href="#flPackage-updateShapeReferenceCount"><span class="function-name">updateShapeReferenceCount</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-updateShapeReferenceCount">updateShapeReferenceCount</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-updateZonesFromGuidelines" href="#flPackage-updateZonesFromGuidelines"><span class="function-name">updateZonesFromGuidelines</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#fontlab.flPackage-updateZonesFromGuidelines">updateZonesFromGuidelines</a>([flZones zonesT, flZones zonesB])</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-zones" href="#flPackage-zones"><span class="function-name">zones</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flZone)& <a href="#fontlab.flPackage-zones">zones</a>(HintingDataType, bool top)</pre>

</dd></dl>

  <h4 class="head-static-methods">Static methods </h4><dl class="function"><dt><a name="flPackage-cloneObject" href="#flPackage-cloneObject"><span class="function-name">cloneObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject <a href="#fontlab.flPackage-cloneObject">cloneObject</a>(const flObject&);</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-createObject" href="#flPackage-createObject"><span class="function-name">createObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing <a href="#fontlab.flPackage-createObject">createObject</a>(int);</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-hasInstaceFor" href="#flPackage-hasInstaceFor"><span class="function-name">hasInstaceFor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-hasInstaceFor">hasInstaceFor</a>(fgFont)</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-haveObject" href="#flPackage-haveObject"><span class="function-name">haveObject</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.flPackage-haveObject">haveObject</a>(uint);</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-instanceType" href="#flPackage-instanceType"><span class="function-name">instanceType</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int <a href="#fontlab.flPackage-instanceType">instanceType</a>();</pre>

</dd></dl>
<dl class="function"><dt><a name="flPackage-readFromFile" href="#flPackage-readFromFile"><span class="function-name">readFromFile</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flPackage/Nothing <a href="#fontlab.flPackage-readFromFile">readFromFile</a>(string[, StorageInfo*=0])</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>allGuidelines</dt>
<dd>

<pre class="doc" markdown="0">QList<flObject></pre>

</dd>
</dl>
<dl class="descriptor"><dt>ascender_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>axes</dt>
<dd>

<pre class="doc" markdown="0">QList<flAxis></pre>

</dd>
</dl>
<dl class="descriptor"><dt>bold</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>capsHeight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>caretOffset_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>cornerTension_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>counterAnchors</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>counterGuides</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>currentSearch</dt>
<dd>

<pre class="doc" markdown="0">QByteArray</pre>

</dd>
</dl>
<dl class="descriptor"><dt>curveTension</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>curveTension_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>defaultMaster</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>descender_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>elidedName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>family_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>family_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ffn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fgId</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fgPackage</dt>
<dd>

<pre class="doc" markdown="0">fgFont</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fileName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>fontLayerOrder</dt>
<dd>

<pre class="doc" markdown="0">A list of layer names indicating order of the layers in the font</pre>

</dd>
</dl>
<dl class="descriptor"><dt>glyphsCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>guidelines</dt>
<dd>

<pre class="doc" markdown="0">flObjectsList<flGuideLine></pre>

</dd>
</dl>
<dl class="descriptor"><dt>guidelinesHost</dt>
<dd>

<pre class="doc" markdown="0">GuidelinesHostIntf*</pre>

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
<dl class="descriptor"><dt>hasWeightAxis</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hasWidthAxis</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>hinting</dt>
<dd>

<pre class="doc" markdown="0">flHintingParameters</pre>

</dd>
</dl>
<dl class="descriptor"><dt>id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>
<dl class="descriptor"><dt>info</dt>
<dd>

<pre class="doc" markdown="0">FontInfo</pre>

</dd>
</dl>
<dl class="descriptor"><dt>inktrapLen_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>instanceAttributes</dt>
<dd>

<pre class="doc" markdown="0">flLayerAttributes</pre>

</dd>
</dl>
<dl class="descriptor"><dt>instances</dt>
<dd>

<pre class="doc" markdown="0">QList<flInstance></pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolationCheckGeometry</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolationExtrapolate</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolationFlags</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolationMutatorMath</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>interpolationSortContours</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isKey</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>isMaster</dt>
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
<dl class="descriptor"><dt>italic</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>italicAngle_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>keepShapeData</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>lineGap_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>mask</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>master</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>masters</dt>
<dd>

<pre class="doc" markdown="0">QList<string></pre>

</dd>
</dl>
<dl class="descriptor"><dt>mastersCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>measurement_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>monospaced</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>
<dl class="descriptor"><dt>name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>
<dl class="descriptor"><dt>note</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>other</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>panose</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>path</dt>
<dd>

<pre class="doc" markdown="0">The path to the source font file</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ps_stemsH</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ps_stemsV</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ps_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>ps_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>psn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>
<dl class="descriptor"><dt>safeBottom_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>safeTop_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>sampleString</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>sgn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>slantTransform</dt>
<dd>

<pre class="doc" markdown="0">QTransform</pre>

</dd>
</dl>
<dl class="descriptor"><dt>slope</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>smartCornerParameters</dt>
<dd>

<pre class="doc" markdown="0">SmartCornerParameters</pre>

</dd>
</dl>
<dl class="descriptor"><dt>stateObject</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tfn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tsn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tt_stemsH</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tt_stemsV</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tt_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>tt_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>
<dl class="descriptor"><dt>underlinePosition_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>underlineThickness_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>upm</dt>
<dd>

<pre class="doc" markdown="0">float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>variables</dt>
<dd>

<pre class="doc" markdown="0">list(flPropertyDouble)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>variationPackages</dt>
<dd>

<pre class="doc" markdown="0">QList<flPackage></pre>

</dd>
</dl>
<dl class="descriptor"><dt>versionMajor</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>versionMinor</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>
<dl class="descriptor"><dt>weight</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>weight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>width</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>width_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>
<dl class="descriptor"><dt>xHeight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.flPackage-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
<dl><dt><span class="other-name">flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}</dt></dl>
</dd>


<a name="fontlab.flPackage.activateGlyph"></a>

## `activateGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.activateGlyph" href="#-fontlab.flPackage.activateGlyph"><span class="function-name">fontlab.flPackage.activateGlyph</span></a> = activateGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">activateGlyph(flGlyph)</pre>

</dd></dl>



<a name="fontlab.flPackage.addAxis"></a>

## `addAxis`


<dl class="function"><dt><a name="-fontlab.flPackage.addAxis" href="#-fontlab.flPackage.addAxis"><span class="function-name">fontlab.flPackage.addAxis</span></a> = addAxis<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string addAxis(flAxis variable)</pre>

</dd></dl>



<a name="fontlab.flPackage.addGlyph"></a>

## `addGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.addGlyph" href="#-fontlab.flPackage.addGlyph"><span class="function-name">fontlab.flPackage.addGlyph</span></a> = addGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">addGlyph(fgGlyph / flGlyph )</pre>

</dd></dl>



<a name="fontlab.flPackage.addInstance"></a>

## `addInstance`


<dl class="function"><dt><a name="-fontlab.flPackage.addInstance" href="#-fontlab.flPackage.addInstance"><span class="function-name">fontlab.flPackage.addInstance</span></a> = addInstance<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">addInstance(const flInstance &instance)</pre>

</dd></dl>



<a name="fontlab.flPackage.addMaster"></a>

## `addMaster`


<dl class="function"><dt><a name="-fontlab.flPackage.addMaster" href="#-fontlab.flPackage.addMaster"><span class="function-name">fontlab.flPackage.addMaster</span></a> = addMaster<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string addMaster(string master_name, bool create_glyphs, flPackage source, string source_layer_name, bool copy_metrics, bool create_missing_glyphs[, flLocation location])</pre>

</dd></dl>



<a name="fontlab.flPackage.allGuidelines"></a>

## `allGuidelines`


<dl class="descriptor"><dt>fontlab.flPackage.allGuidelines</dt>
<dd>

<pre class="doc" markdown="0">QList<flObject></pre>

</dd>
</dl>



<a name="fontlab.flPackage.ascender_value"></a>

## `ascender_value`


<dl class="descriptor"><dt>fontlab.flPackage.ascender_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.assignData"></a>

## `assignData`


<dl class="function"><dt><a name="-fontlab.flPackage.assignData" href="#-fontlab.flPackage.assignData"><span class="function-name">fontlab.flPackage.assignData</span></a> = assignData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">assignData(const flPackage &package)</pre>

</dd></dl>



<a name="fontlab.flPackage.autohintGlyphs"></a>

## `autohintGlyphs`


<dl class="function"><dt><a name="-fontlab.flPackage.autohintGlyphs" href="#-fontlab.flPackage.autohintGlyphs"><span class="function-name">fontlab.flPackage.autohintGlyphs</span></a> = autohintGlyphs<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">autohintGlyphs(QList<flGlyph> glyphs, bool make_hints)</pre>

</dd></dl>



<a name="fontlab.flPackage.axes"></a>

## `axes`


<dl class="descriptor"><dt>fontlab.flPackage.axes</dt>
<dd>

<pre class="doc" markdown="0">QList<flAxis></pre>

</dd>
</dl>



<a name="fontlab.flPackage.bold"></a>

## `bold`


<dl class="descriptor"><dt>fontlab.flPackage.bold</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.buildShapeDataNames"></a>

## `buildShapeDataNames`


<dl class="function"><dt><a name="-fontlab.flPackage.buildShapeDataNames" href="#-fontlab.flPackage.buildShapeDataNames"><span class="function-name">fontlab.flPackage.buildShapeDataNames</span></a> = buildShapeDataNames<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QSet<string> buildShapeDataNames(objId exclude[, string layer_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.can_interpolate"></a>

## `can_interpolate`


<dl class="function"><dt><a name="-fontlab.flPackage.can_interpolate" href="#-fontlab.flPackage.can_interpolate"><span class="function-name">fontlab.flPackage.can_interpolate</span></a> = can_interpolate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool can_interpolate([string master_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.capsHeight_value"></a>

## `capsHeight_value`


<dl class="descriptor"><dt>fontlab.flPackage.capsHeight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.caretOffset_value"></a>

## `caretOffset_value`


<dl class="descriptor"><dt>fontlab.flPackage.caretOffset_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.changed"></a>

## `changed`


<dl class="function"><dt><a name="-fontlab.flPackage.changed" href="#-fontlab.flPackage.changed"><span class="function-name">fontlab.flPackage.changed</span></a> = changed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">changed()</pre>

</dd></dl>



<a name="fontlab.flPackage.checkAxisName"></a>

## `checkAxisName`


<dl class="function"><dt><a name="-fontlab.flPackage.checkAxisName" href="#-fontlab.flPackage.checkAxisName"><span class="function-name">fontlab.flPackage.checkAxisName</span></a> = checkAxisName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string checkAxisName(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.checkInitHistoryState"></a>

## `checkInitHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.checkInitHistoryState" href="#-fontlab.flPackage.checkInitHistoryState"><span class="function-name">fontlab.flPackage.checkInitHistoryState</span></a> = checkInitHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">checkInitHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.checkVariableName"></a>

## `checkVariableName`


<dl class="function"><dt><a name="-fontlab.flPackage.checkVariableName" href="#-fontlab.flPackage.checkVariableName"><span class="function-name">fontlab.flPackage.checkVariableName</span></a> = checkVariableName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string checkVariableName(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.clearAboveHistory"></a>

## `clearAboveHistory`


<dl class="function"><dt><a name="-fontlab.flPackage.clearAboveHistory" href="#-fontlab.flPackage.clearAboveHistory"><span class="function-name">fontlab.flPackage.clearAboveHistory</span></a> = clearAboveHistory<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearAboveHistory(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.clearActiveGlyphs"></a>

## `clearActiveGlyphs`


<dl class="function"><dt><a name="-fontlab.flPackage.clearActiveGlyphs" href="#-fontlab.flPackage.clearActiveGlyphs"><span class="function-name">fontlab.flPackage.clearActiveGlyphs</span></a> = clearActiveGlyphs<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearActiveGlyphs()</pre>

</dd></dl>



<a name="fontlab.flPackage.clearFlag"></a>

## `clearFlag`


<dl class="function"><dt><a name="-fontlab.flPackage.clearFlag" href="#-fontlab.flPackage.clearFlag"><span class="function-name">fontlab.flPackage.clearFlag</span></a> = clearFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlag(uint f)</pre>

</dd></dl>



<a name="fontlab.flPackage.clearFlags"></a>

## `clearFlags`


<dl class="function"><dt><a name="-fontlab.flPackage.clearFlags" href="#-fontlab.flPackage.clearFlags"><span class="function-name">fontlab.flPackage.clearFlags</span></a> = clearFlags<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearFlags()</pre>

</dd></dl>



<a name="fontlab.flPackage.clearInstances"></a>

## `clearInstances`


<dl class="function"><dt><a name="-fontlab.flPackage.clearInstances" href="#-fontlab.flPackage.clearInstances"><span class="function-name">fontlab.flPackage.clearInstances</span></a> = clearInstances<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearInstances()</pre>

</dd></dl>



<a name="fontlab.flPackage.clearMasters"></a>

## `clearMasters`


<dl class="function"><dt><a name="-fontlab.flPackage.clearMasters" href="#-fontlab.flPackage.clearMasters"><span class="function-name">fontlab.flPackage.clearMasters</span></a> = clearMasters<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">clearMasters(bool release)</pre>

</dd></dl>



<a name="fontlab.flPackage.clone"></a>

## `clone`


<dl class="function"><dt><a name="-fontlab.flPackage.clone" href="#-fontlab.flPackage.clone"><span class="function-name">fontlab.flPackage.clone</span></a> = clone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Clone the object</pre>

</dd></dl>



<a name="fontlab.flPackage.cloneObject"></a>

## `cloneObject`


<dl class="function"><dt><a name="-fontlab.flPackage.cloneObject" href="#-fontlab.flPackage.cloneObject"><span class="function-name">fontlab.flPackage.cloneObject</span></a> = cloneObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject cloneObject(const flObject&);</pre>

</dd></dl>



<a name="fontlab.flPackage.close"></a>

## `close`


<dl class="function"><dt><a name="-fontlab.flPackage.close" href="#-fontlab.flPackage.close"><span class="function-name">fontlab.flPackage.close</span></a> = close<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">close(save=False) - Close the font</pre>

</dd></dl>



<a name="fontlab.flPackage.collectNames"></a>

## `collectNames`


<dl class="function"><dt><a name="-fontlab.flPackage.collectNames" href="#-fontlab.flPackage.collectNames"><span class="function-name">fontlab.flPackage.collectNames</span></a> = collectNames<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">collectNames(StorageInfo * storage)</pre>

</dd></dl>



<a name="fontlab.flPackage.collectShapes"></a>

## `collectShapes`


<dl class="function"><dt><a name="-fontlab.flPackage.collectShapes" href="#-fontlab.flPackage.collectShapes"><span class="function-name">fontlab.flPackage.collectShapes</span></a> = collectShapes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<flShape>/Nothing collectShapes(flShape, string layer_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.completeData"></a>

## `completeData`


<dl class="function"><dt><a name="-fontlab.flPackage.completeData" href="#-fontlab.flPackage.completeData"><span class="function-name">fontlab.flPackage.completeData</span></a> = completeData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">completeData([bool fg_data = false])</pre>

</dd></dl>



<a name="fontlab.flPackage.convertZonesToGuidelines"></a>

## `convertZonesToGuidelines`


<dl class="function"><dt><a name="-fontlab.flPackage.convertZonesToGuidelines" href="#-fontlab.flPackage.convertZonesToGuidelines"><span class="function-name">fontlab.flPackage.convertZonesToGuidelines</span></a> = convertZonesToGuidelines<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">convertZonesToGuidelines(flZones zonesT, flZones zonesB)</pre>

</dd></dl>



<a name="fontlab.flPackage.cornerTension_value"></a>

## `cornerTension_value`


<dl class="descriptor"><dt>fontlab.flPackage.cornerTension_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.counterAnchors"></a>

## `counterAnchors`


<dl class="descriptor"><dt>fontlab.flPackage.counterAnchors</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.counterGuides"></a>

## `counterGuides`


<dl class="descriptor"><dt>fontlab.flPackage.counterGuides</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.createHistoryState"></a>

## `createHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.createHistoryState" href="#-fontlab.flPackage.createHistoryState"><span class="function-name">fontlab.flPackage.createHistoryState</span></a> = createHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">createHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.createObject"></a>

## `createObject`


<dl class="function"><dt><a name="-fontlab.flPackage.createObject" href="#-fontlab.flPackage.createObject"><span class="function-name">fontlab.flPackage.createObject</span></a> = createObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject/Nothing createObject(int);</pre>

</dd></dl>



<a name="fontlab.flPackage.currentHistoryState"></a>

## `currentHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.currentHistoryState" href="#-fontlab.flPackage.currentHistoryState"><span class="function-name">fontlab.flPackage.currentHistoryState</span></a> = currentHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">currentHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flPackage.currentSearch"></a>

## `currentSearch`


<dl class="descriptor"><dt>fontlab.flPackage.currentSearch</dt>
<dd>

<pre class="doc" markdown="0">QByteArray</pre>

</dd>
</dl>



<a name="fontlab.flPackage.curveTension"></a>

## `curveTension`


<dl class="descriptor"><dt>fontlab.flPackage.curveTension</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.curveTension_value"></a>

## `curveTension_value`


<dl class="descriptor"><dt>fontlab.flPackage.curveTension_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.defaultMaster"></a>

## `defaultMaster`


<dl class="descriptor"><dt>fontlab.flPackage.defaultMaster</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.deleteGlyph"></a>

## `deleteGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.deleteGlyph" href="#-fontlab.flPackage.deleteGlyph"><span class="function-name">fontlab.flPackage.deleteGlyph</span></a> = deleteGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool deleteGlyph(fgGlyph / flGlyph )</pre>

</dd></dl>



<a name="fontlab.flPackage.deleteGroups"></a>

## `deleteGroups`


<dl class="function"><dt><a name="-fontlab.flPackage.deleteGroups" href="#-fontlab.flPackage.deleteGroups"><span class="function-name">fontlab.flPackage.deleteGroups</span></a> = deleteGroups<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">deleteGroups(QSet<uint> ids, bool deleteDependentContent)</pre>

</dd></dl>



<a name="fontlab.flPackage.descender_value"></a>

## `descender_value`


<dl class="descriptor"><dt>fontlab.flPackage.descender_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.elidedName"></a>

## `elidedName`


<dl class="descriptor"><dt>fontlab.flPackage.elidedName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.ensureProteusData"></a>

## `ensureProteusData`


<dl class="function"><dt><a name="-fontlab.flPackage.ensureProteusData" href="#-fontlab.flPackage.ensureProteusData"><span class="function-name">fontlab.flPackage.ensureProteusData</span></a> = ensureProteusData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">ensureProteusData()</pre>

</dd></dl>



<a name="fontlab.flPackage.family_zones"></a>

## `family_zones`


<dl class="function"><dt><a name="-fontlab.flPackage.family_zones" href="#-fontlab.flPackage.family_zones"><span class="function-name">fontlab.flPackage.family_zones</span></a> = family_zones<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flZone)& family_zones(bool top)</pre>

</dd></dl>



<a name="fontlab.flPackage.family_zonesB"></a>

## `family_zonesB`


<dl class="descriptor"><dt>fontlab.flPackage.family_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.family_zonesT"></a>

## `family_zonesT`


<dl class="descriptor"><dt>fontlab.flPackage.family_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.featuresContainer"></a>

## `featuresContainer`


<dl class="function"><dt><a name="-fontlab.flPackage.featuresContainer" href="#-fontlab.flPackage.featuresContainer"><span class="function-name">fontlab.flPackage.featuresContainer</span></a> = featuresContainer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject featuresContainer()</pre>

</dd></dl>



<a name="fontlab.flPackage.ffn"></a>

## `ffn`


<dl class="descriptor"><dt>fontlab.flPackage.ffn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.fgId"></a>

## `fgId`


<dl class="descriptor"><dt>fontlab.flPackage.fgId</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.fgPackage"></a>

## `fgPackage`


<dl class="descriptor"><dt>fontlab.flPackage.fgPackage</dt>
<dd>

<pre class="doc" markdown="0">fgFont</pre>

</dd>
</dl>



<a name="fontlab.flPackage.fileName"></a>

## `fileName`


<dl class="descriptor"><dt>fontlab.flPackage.fileName</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.findAxis"></a>

## `findAxis`


<dl class="function"><dt><a name="-fontlab.flPackage.findAxis" href="#-fontlab.flPackage.findAxis"><span class="function-name">fontlab.flPackage.findAxis</span></a> = findAxis<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flAxis/Nothing findAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>



<a name="fontlab.flPackage.findAxisShort"></a>

## `findAxisShort`


<dl class="function"><dt><a name="-fontlab.flPackage.findAxisShort" href="#-fontlab.flPackage.findAxisShort"><span class="function-name">fontlab.flPackage.findAxisShort</span></a> = findAxisShort<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flAxis/Nothing findAxisShort(string short_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.findFgId"></a>

## `findFgId`


<dl class="function"><dt><a name="-fontlab.flPackage.findFgId" href="#-fontlab.flPackage.findFgId"><span class="function-name">fontlab.flPackage.findFgId</span></a> = findFgId<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph findFgId(uint id)</pre>

</dd></dl>



<a name="fontlab.flPackage.findGroup"></a>

## `findGroup`


<dl class="function"><dt><a name="-fontlab.flPackage.findGroup" href="#-fontlab.flPackage.findGroup"><span class="function-name">fontlab.flPackage.findGroup</span></a> = findGroup<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fg::GlyphGroup* findGroup(int _id)</pre>

</dd></dl>



<a name="fontlab.flPackage.findName"></a>

## `findName`


<dl class="function"><dt><a name="-fontlab.flPackage.findName" href="#-fontlab.flPackage.findName"><span class="function-name">fontlab.flPackage.findName</span></a> = findName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph findName(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.findNameId"></a>

## `findNameId`


<dl class="function"><dt><a name="-fontlab.flPackage.findNameId" href="#-fontlab.flPackage.findNameId"><span class="function-name">fontlab.flPackage.findNameId</span></a> = findNameId<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph findNameId(uint fg_id)</pre>

</dd></dl>



<a name="fontlab.flPackage.findNewName"></a>

## `findNewName`


<dl class="function"><dt><a name="-fontlab.flPackage.findNewName" href="#-fontlab.flPackage.findNewName"><span class="function-name">fontlab.flPackage.findNewName</span></a> = findNewName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string findNewName(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.findShapeRoot"></a>

## `findShapeRoot`


<dl class="function"><dt><a name="-fontlab.flPackage.findShapeRoot" href="#-fontlab.flPackage.findShapeRoot"><span class="function-name">fontlab.flPackage.findShapeRoot</span></a> = findShapeRoot<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph findShapeRoot(flShapeData shape_data)</pre>

</dd></dl>



<a name="fontlab.flPackage.findStem"></a>

## `findStem`


<dl class="function"><dt><a name="-fontlab.flPackage.findStem" href="#-fontlab.flPackage.findStem"><span class="function-name">fontlab.flPackage.findStem</span></a> = findStem<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int findStem(string n, bool b, bool loose)</pre>

</dd></dl>



<a name="fontlab.flPackage.findUnicode"></a>

## `findUnicode`


<dl class="function"><dt><a name="-fontlab.flPackage.findUnicode" href="#-fontlab.flPackage.findUnicode"><span class="function-name">fontlab.flPackage.findUnicode</span></a> = findUnicode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flGlyph findUnicode(uint uni)</pre>

</dd></dl>



<a name="fontlab.flPackage.findZone"></a>

## `findZone`


<dl class="function"><dt><a name="-fontlab.flPackage.findZone" href="#-fontlab.flPackage.findZone"><span class="function-name">fontlab.flPackage.findZone</span></a> = findZone<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int findZone(string n, bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.flag"></a>

## `flag`


<dl class="function"><dt><a name="-fontlab.flPackage.flag" href="#-fontlab.flPackage.flag"><span class="function-name">fontlab.flPackage.flag</span></a> = flag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flag(uint f)</pre>

</dd></dl>



<a name="fontlab.flPackage.flObjectFlags"></a>

## `flObjectFlags`


<span class="other-name">fontlab.flPackage.flObjectFlags</span> = {'ofAnchored': 64, 'ofChanged': 2, 'ofHistory': 128, 'ofIgnore': 8, 'ofIgnoreChanges': 4, 'ofPassive': 16, 'ofReleased': 1, 'ofSlowUpdate': 32}


<a name="fontlab.flPackage.fontLayerOrder"></a>

## `fontLayerOrder`


<dl class="descriptor"><dt>fontlab.flPackage.fontLayerOrder</dt>
<dd>

<pre class="doc" markdown="0">A list of layer names indicating order of the layers in the font</pre>

</dd>
</dl>



<a name="fontlab.flPackage.generateGlyph"></a>

## `generateGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.generateGlyph" href="#-fontlab.flPackage.generateGlyph"><span class="function-name">fontlab.flPackage.generateGlyph</span></a> = generateGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">( QList<GlyphComponent>, double width )/Nothing generateGlyph(string recipe, string layer_name, FontMetrics metrics, bool rtl)</pre>

</dd></dl>



<a name="fontlab.flPackage.getAccentsInfo"></a>

## `getAccentsInfo`


<dl class="function"><dt><a name="-fontlab.flPackage.getAccentsInfo" href="#-fontlab.flPackage.getAccentsInfo"><span class="function-name">fontlab.flPackage.getAccentsInfo</span></a> = getAccentsInfo<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(AccentInfo)/Nothing getAccentsInfo(flLayer, flPinPoint)</pre>

</dd></dl>



<a name="fontlab.flPackage.getAllGroups"></a>

## `getAllGroups`


<dl class="function"><dt><a name="-fontlab.flPackage.getAllGroups" href="#-fontlab.flPackage.getAllGroups"><span class="function-name">fontlab.flPackage.getAllGroups</span></a> = getAllGroups<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list( (bool kernGroup, string groupName, int id, int mark, list(string glyphName) )/Nothing getAllGroups()</pre>

</dd></dl>



<a name="fontlab.flPackage.getAxisName"></a>

## `getAxisName`


<dl class="function"><dt><a name="-fontlab.flPackage.getAxisName" href="#-fontlab.flPackage.getAxisName"><span class="function-name">fontlab.flPackage.getAxisName</span></a> = getAxisName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getAxisName(string short_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.getAxisShortName"></a>

## `getAxisShortName`


<dl class="function"><dt><a name="-fontlab.flPackage.getAxisShortName" href="#-fontlab.flPackage.getAxisShortName"><span class="function-name">fontlab.flPackage.getAxisShortName</span></a> = getAxisShortName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getAxisShortName(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.getLayerName"></a>

## `getLayerName`


<dl class="function"><dt><a name="-fontlab.flPackage.getLayerName" href="#-fontlab.flPackage.getLayerName"><span class="function-name">fontlab.flPackage.getLayerName</span></a> = getLayerName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string getLayerName()</pre>

</dd></dl>



<a name="fontlab.flPackage.getMarkOffset"></a>

## `getMarkOffset`


<dl class="function"><dt><a name="-fontlab.flPackage.getMarkOffset" href="#-fontlab.flPackage.getMarkOffset"><span class="function-name">fontlab.flPackage.getMarkOffset</span></a> = getMarkOffset<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QPointF/Nothing getMarkOffset(flGlyph g1, flGlyph g2)</pre>

</dd></dl>



<a name="fontlab.flPackage.getProperties"></a>

## `getProperties`


<dl class="function"><dt><a name="-fontlab.flPackage.getProperties" href="#-fontlab.flPackage.getProperties"><span class="function-name">fontlab.flPackage.getProperties</span></a> = getProperties<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Get object's properties list</pre>

</dd></dl>



<a name="fontlab.flPackage.getProperty"></a>

## `getProperty`


<dl class="function"><dt><a name="-fontlab.flPackage.getProperty" href="#-fontlab.flPackage.getProperty"><span class="function-name">fontlab.flPackage.getProperty</span></a> = getProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getProperty('key') - get object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flPackage.getPropertyFloat"></a>

## `getPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flPackage.getPropertyFloat" href="#-fontlab.flPackage.getPropertyFloat"><span class="function-name">fontlab.flPackage.getPropertyFloat</span></a> = getPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyFloat('key') - get float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flPackage.getPropertyInt"></a>

## `getPropertyInt`


<dl class="function"><dt><a name="-fontlab.flPackage.getPropertyInt" href="#-fontlab.flPackage.getPropertyInt"><span class="function-name">fontlab.flPackage.getPropertyInt</span></a> = getPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">getPropertyInt('key') - get int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flPackage.getShapes"></a>

## `getShapes`


<dl class="function"><dt><a name="-fontlab.flPackage.getShapes" href="#-fontlab.flPackage.getShapes"><span class="function-name">fontlab.flPackage.getShapes</span></a> = getShapes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<int>/Nothing getShapes(string filter[, string layer_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.glyphsCount"></a>

## `glyphsCount`


<dl class="descriptor"><dt>fontlab.flPackage.glyphsCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.guidelines"></a>

## `guidelines`


<dl class="descriptor"><dt>fontlab.flPackage.guidelines</dt>
<dd>

<pre class="doc" markdown="0">flObjectsList<flGuideLine></pre>

</dd>
</dl>



<a name="fontlab.flPackage.guidelinesHost"></a>

## `guidelinesHost`


<dl class="descriptor"><dt>fontlab.flPackage.guidelinesHost</dt>
<dd>

<pre class="doc" markdown="0">GuidelinesHostIntf*</pre>

</dd>
</dl>



<a name="fontlab.flPackage.hasAxis"></a>

## `hasAxis`


<dl class="function"><dt><a name="-fontlab.flPackage.hasAxis" href="#-fontlab.flPackage.hasAxis"><span class="function-name">fontlab.flPackage.hasAxis</span></a> = hasAxis<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasAxis(string name[, Qt::CaseSensitivity cs = Qt::CaseSensitive])</pre>

</dd></dl>



<a name="fontlab.flPackage.hasAxisShort"></a>

## `hasAxisShort`


<dl class="function"><dt><a name="-fontlab.flPackage.hasAxisShort" href="#-fontlab.flPackage.hasAxisShort"><span class="function-name">fontlab.flPackage.hasAxisShort</span></a> = hasAxisShort<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasAxisShort(string short_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.hasChanges"></a>

## `hasChanges`


<dl class="descriptor"><dt>fontlab.flPackage.hasChanges</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.hasGuides"></a>

## `hasGuides`


<dl class="function"><dt><a name="-fontlab.flPackage.hasGuides" href="#-fontlab.flPackage.hasGuides"><span class="function-name">fontlab.flPackage.hasGuides</span></a> = hasGuides<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasGuides()</pre>

</dd></dl>



<a name="fontlab.flPackage.hasHistoryState"></a>

## `hasHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.hasHistoryState" href="#-fontlab.flPackage.hasHistoryState"><span class="function-name">fontlab.flPackage.hasHistoryState</span></a> = hasHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hasHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.hasHistoryStates"></a>

## `hasHistoryStates`


<dl class="descriptor"><dt>fontlab.flPackage.hasHistoryStates</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.hasInstaceFor"></a>

## `hasInstaceFor`


<dl class="function"><dt><a name="-fontlab.flPackage.hasInstaceFor" href="#-fontlab.flPackage.hasInstaceFor"><span class="function-name">fontlab.flPackage.hasInstaceFor</span></a> = hasInstaceFor<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasInstaceFor(fgFont)</pre>

</dd></dl>



<a name="fontlab.flPackage.hasMaster"></a>

## `hasMaster`


<dl class="function"><dt><a name="-fontlab.flPackage.hasMaster" href="#-fontlab.flPackage.hasMaster"><span class="function-name">fontlab.flPackage.hasMaster</span></a> = hasMaster<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasMaster(string name)</pre>

</dd></dl>



<a name="fontlab.flPackage.hasName"></a>

## `hasName`


<dl class="function"><dt><a name="-fontlab.flPackage.hasName" href="#-fontlab.flPackage.hasName"><span class="function-name">fontlab.flPackage.hasName</span></a> = hasName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasName(string name[, bool relaxed=false])</pre>

</dd></dl>



<a name="fontlab.flPackage.hasPackageHistoryStorages"></a>

## `hasPackageHistoryStorages`


<dl class="function"><dt><a name="-fontlab.flPackage.hasPackageHistoryStorages" href="#-fontlab.flPackage.hasPackageHistoryStorages"><span class="function-name">fontlab.flPackage.hasPackageHistoryStorages</span></a> = hasPackageHistoryStorages<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasPackageHistoryStorages(uint to_history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.hasWeightAxis"></a>

## `hasWeightAxis`


<dl class="descriptor"><dt>fontlab.flPackage.hasWeightAxis</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.hasWidthAxis"></a>

## `hasWidthAxis`


<dl class="descriptor"><dt>fontlab.flPackage.hasWidthAxis</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.hasZones"></a>

## `hasZones`


<dl class="function"><dt><a name="-fontlab.flPackage.hasZones" href="#-fontlab.flPackage.hasZones"><span class="function-name">fontlab.flPackage.hasZones</span></a> = hasZones<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool hasZones()</pre>

</dd></dl>



<a name="fontlab.flPackage.haveObject"></a>

## `haveObject`


<dl class="function"><dt><a name="-fontlab.flPackage.haveObject" href="#-fontlab.flPackage.haveObject"><span class="function-name">fontlab.flPackage.haveObject</span></a> = haveObject<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool haveObject(uint);</pre>

</dd></dl>



<a name="fontlab.flPackage.hinting"></a>

## `hinting`


<dl class="descriptor"><dt>fontlab.flPackage.hinting</dt>
<dd>

<pre class="doc" markdown="0">flHintingParameters</pre>

</dd>
</dl>



<a name="fontlab.flPackage.historyStack"></a>

## `historyStack`


<dl class="function"><dt><a name="-fontlab.flPackage.historyStack" href="#-fontlab.flPackage.historyStack"><span class="function-name">fontlab.flPackage.historyStack</span></a> = historyStack<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject historyStack()</pre>

</dd></dl>



<a name="fontlab.flPackage.historyStates"></a>

## `historyStates`


<dl class="function"><dt><a name="-fontlab.flPackage.historyStates" href="#-fontlab.flPackage.historyStates"><span class="function-name">fontlab.flPackage.historyStates</span></a> = historyStates<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">historyStates(bool accepted_state)</pre>

</dd></dl>



<a name="fontlab.flPackage.id"></a>

## `id`


<dl class="descriptor"><dt>fontlab.flPackage.id</dt>
<dd>

<pre class="doc" markdown="0">object id</pre>

</dd>
</dl>



<a name="fontlab.flPackage.independedAll"></a>

## `independedAll`


<dl class="function"><dt><a name="-fontlab.flPackage.independedAll" href="#-fontlab.flPackage.independedAll"><span class="function-name">fontlab.flPackage.independedAll</span></a> = independedAll<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">independedAll()</pre>

</dd></dl>



<a name="fontlab.flPackage.info"></a>

## `info`


<dl class="descriptor"><dt>fontlab.flPackage.info</dt>
<dd>

<pre class="doc" markdown="0">FontInfo</pre>

</dd>
</dl>



<a name="fontlab.flPackage.initialHistoryState"></a>

## `initialHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.initialHistoryState" href="#-fontlab.flPackage.initialHistoryState"><span class="function-name">fontlab.flPackage.initialHistoryState</span></a> = initialHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initialHistoryIx()</pre>

</dd></dl>



<a name="fontlab.flPackage.initItr"></a>

## `initItr`


<dl class="function"><dt><a name="-fontlab.flPackage.initItr" href="#-fontlab.flPackage.initItr"><span class="function-name">fontlab.flPackage.initItr</span></a> = initItr<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initItr(fgTTInterpreter itr)</pre>

</dd></dl>



<a name="fontlab.flPackage.initItrGlyph"></a>

## `initItrGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.initItrGlyph" href="#-fontlab.flPackage.initItrGlyph"><span class="function-name">fontlab.flPackage.initItrGlyph</span></a> = initItrGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">initItrGlyph(fgTTInterpreter itr, flGlyph glyph)</pre>

</dd></dl>



<a name="fontlab.flPackage.inktrapLen_value"></a>

## `inktrapLen_value`


<dl class="descriptor"><dt>fontlab.flPackage.inktrapLen_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.instanceAttributes"></a>

## `instanceAttributes`


<dl class="descriptor"><dt>fontlab.flPackage.instanceAttributes</dt>
<dd>

<pre class="doc" markdown="0">flLayerAttributes</pre>

</dd>
</dl>



<a name="fontlab.flPackage.instances"></a>

## `instances`


<dl class="descriptor"><dt>fontlab.flPackage.instances</dt>
<dd>

<pre class="doc" markdown="0">QList<flInstance></pre>

</dd>
</dl>



<a name="fontlab.flPackage.instanceType"></a>

## `instanceType`


<dl class="function"><dt><a name="-fontlab.flPackage.instanceType" href="#-fontlab.flPackage.instanceType"><span class="function-name">fontlab.flPackage.instanceType</span></a> = instanceType<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int instanceType();</pre>

</dd></dl>



<a name="fontlab.flPackage.interpolationCheckGeometry"></a>

## `interpolationCheckGeometry`


<dl class="descriptor"><dt>fontlab.flPackage.interpolationCheckGeometry</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.interpolationExtrapolate"></a>

## `interpolationExtrapolate`


<dl class="descriptor"><dt>fontlab.flPackage.interpolationExtrapolate</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.interpolationFlags"></a>

## `interpolationFlags`


<dl class="descriptor"><dt>fontlab.flPackage.interpolationFlags</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.interpolationMutatorMath"></a>

## `interpolationMutatorMath`


<dl class="descriptor"><dt>fontlab.flPackage.interpolationMutatorMath</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.interpolationSortContours"></a>

## `interpolationSortContours`


<dl class="descriptor"><dt>fontlab.flPackage.interpolationSortContours</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isChanged"></a>

## `isChanged`


<dl class="descriptor"><dt>fontlab.flPackage.isChanged</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isComponent"></a>

## `isComponent`


<dl class="function"><dt><a name="-fontlab.flPackage.isComponent" href="#-fontlab.flPackage.isComponent"><span class="function-name">fontlab.flPackage.isComponent</span></a> = isComponent<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flGlyph, QTransform) isComponent(flShapeData[, string layer_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.isEqual"></a>

## `isEqual`


<dl class="function"><dt><a name="-fontlab.flPackage.isEqual" href="#-fontlab.flPackage.isEqual"><span class="function-name">fontlab.flPackage.isEqual</span></a> = isEqual<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isEqual(flObject)</pre>

</dd></dl>



<a name="fontlab.flPackage.isKey"></a>

## `isKey`


<dl class="descriptor"><dt>fontlab.flPackage.isKey</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isMaster"></a>

## `isMaster`


<dl class="descriptor"><dt>fontlab.flPackage.isMaster</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isNull"></a>

## `isNull`


<dl class="descriptor"><dt>fontlab.flPackage.isNull</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isPresent"></a>

## `isPresent`


<dl class="descriptor"><dt>fontlab.flPackage.isPresent</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isReleased"></a>

## `isReleased`


<dl class="descriptor"><dt>fontlab.flPackage.isReleased</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.isValid"></a>

## `isValid`


<dl class="descriptor"><dt>fontlab.flPackage.isValid</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.italic"></a>

## `italic`


<dl class="descriptor"><dt>fontlab.flPackage.italic</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.italicAngle_value"></a>

## `italicAngle_value`


<dl class="descriptor"><dt>fontlab.flPackage.italicAngle_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.keepShapeData"></a>

## `keepShapeData`


<dl class="descriptor"><dt>fontlab.flPackage.keepShapeData</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.kerning"></a>

## `kerning`


<dl class="function"><dt><a name="-fontlab.flPackage.kerning" href="#-fontlab.flPackage.kerning"><span class="function-name">fontlab.flPackage.kerning</span></a> = kerning<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fgKerning kerning([string master_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.kerningContainer"></a>

## `kerningContainer`


<dl class="function"><dt><a name="-fontlab.flPackage.kerningContainer" href="#-fontlab.flPackage.kerningContainer"><span class="function-name">fontlab.flPackage.kerningContainer</span></a> = kerningContainer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject kerningContainer()</pre>

</dd></dl>



<a name="fontlab.flPackage.lineGap_value"></a>

## `lineGap_value`


<dl class="descriptor"><dt>fontlab.flPackage.lineGap_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.location"></a>

## `location`


<dl class="function"><dt><a name="-fontlab.flPackage.location" href="#-fontlab.flPackage.location"><span class="function-name">fontlab.flPackage.location</span></a> = location<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flLocation& location([string master_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.makeShapeDataName"></a>

## `makeShapeDataName`


<dl class="function"><dt><a name="-fontlab.flPackage.makeShapeDataName" href="#-fontlab.flPackage.makeShapeDataName"><span class="function-name">fontlab.flPackage.makeShapeDataName</span></a> = makeShapeDataName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string makeShapeDataName(string name, objId _id, string layer_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.mask"></a>

## `mask`


<dl class="descriptor"><dt>fontlab.flPackage.mask</dt>
<dd>

<pre class="doc" markdown="0">flLayer</pre>

</dd>
</dl>



<a name="fontlab.flPackage.master"></a>

## `master`


<dl class="descriptor"><dt>fontlab.flPackage.master</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.masters"></a>

## `masters`


<dl class="descriptor"><dt>fontlab.flPackage.masters</dt>
<dd>

<pre class="doc" markdown="0">QList<string></pre>

</dd>
</dl>



<a name="fontlab.flPackage.mastersContainer"></a>

## `mastersContainer`


<dl class="function"><dt><a name="-fontlab.flPackage.mastersContainer" href="#-fontlab.flPackage.mastersContainer"><span class="function-name">fontlab.flPackage.mastersContainer</span></a> = mastersContainer<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flObject mastersContainer()</pre>

</dd></dl>



<a name="fontlab.flPackage.mastersCount"></a>

## `mastersCount`


<dl class="descriptor"><dt>fontlab.flPackage.mastersCount</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.measurement_value"></a>

## `measurement_value`


<dl class="descriptor"><dt>fontlab.flPackage.measurement_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.monospaced"></a>

## `monospaced`


<dl class="descriptor"><dt>fontlab.flPackage.monospaced</dt>
<dd>

<pre class="doc" markdown="0">bool</pre>

</dd>
</dl>



<a name="fontlab.flPackage.name"></a>

## `name`


<dl class="descriptor"><dt>fontlab.flPackage.name</dt>
<dd>

<pre class="doc" markdown="0">object name</pre>

</dd>
</dl>



<a name="fontlab.flPackage.note"></a>

## `note`


<dl class="descriptor"><dt>fontlab.flPackage.note</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.optimizeShapeTransformations"></a>

## `optimizeShapeTransformations`


<dl class="function"><dt><a name="-fontlab.flPackage.optimizeShapeTransformations" href="#-fontlab.flPackage.optimizeShapeTransformations"><span class="function-name">fontlab.flPackage.optimizeShapeTransformations</span></a> = optimizeShapeTransformations<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool optimizeShapeTransformations(QList<flObject> changes)</pre>

</dd></dl>



<a name="fontlab.flPackage.optimizeStemData"></a>

## `optimizeStemData`


<dl class="function"><dt><a name="-fontlab.flPackage.optimizeStemData" href="#-fontlab.flPackage.optimizeStemData"><span class="function-name">fontlab.flPackage.optimizeStemData</span></a> = optimizeStemData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flStems stemsH, flStems stemsV) optimizeStemData(flStems stemsH, flStems stemsV)</pre>

</dd></dl>



<a name="fontlab.flPackage.other"></a>

## `other`


<dl class="descriptor"><dt>fontlab.flPackage.other</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.panose"></a>

## `panose`


<dl class="descriptor"><dt>fontlab.flPackage.panose</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.path"></a>

## `path`


<dl class="descriptor"><dt>fontlab.flPackage.path</dt>
<dd>

<pre class="doc" markdown="0">The path to the source font file</pre>

</dd>
</dl>



<a name="fontlab.flPackage.prepareAxes"></a>

## `prepareAxes`


<dl class="function"><dt><a name="-fontlab.flPackage.prepareAxes" href="#-fontlab.flPackage.prepareAxes"><span class="function-name">fontlab.flPackage.prepareAxes</span></a> = prepareAxes<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">QList<flAxis>/Nothing prepareAxes(QList<flPackage> packages, QList<flGlyph> glyphs)</pre>

</dd></dl>



<a name="fontlab.flPackage.prepareFontGateData"></a>

## `prepareFontGateData`


<dl class="function"><dt><a name="-fontlab.flPackage.prepareFontGateData" href="#-fontlab.flPackage.prepareFontGateData"><span class="function-name">fontlab.flPackage.prepareFontGateData</span></a> = prepareFontGateData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">prepareFontGateData(bool prepare_tth)</pre>

</dd></dl>



<a name="fontlab.flPackage.preparePropertiesData"></a>

## `preparePropertiesData`


<dl class="function"><dt><a name="-fontlab.flPackage.preparePropertiesData" href="#-fontlab.flPackage.preparePropertiesData"><span class="function-name">fontlab.flPackage.preparePropertiesData</span></a> = preparePropertiesData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">preparePropertiesData()</pre>

</dd></dl>



<a name="fontlab.flPackage.projectPackageName"></a>

## `projectPackageName`


<dl class="function"><dt><a name="-fontlab.flPackage.projectPackageName" href="#-fontlab.flPackage.projectPackageName"><span class="function-name">fontlab.flPackage.projectPackageName</span></a> = projectPackageName<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string projectPackageName()</pre>

</dd></dl>



<a name="fontlab.flPackage.ps_stemsH"></a>

## `ps_stemsH`


<dl class="descriptor"><dt>fontlab.flPackage.ps_stemsH</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.ps_stemsV"></a>

## `ps_stemsV`


<dl class="descriptor"><dt>fontlab.flPackage.ps_stemsV</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.ps_zonesB"></a>

## `ps_zonesB`


<dl class="descriptor"><dt>fontlab.flPackage.ps_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.ps_zonesT"></a>

## `ps_zonesT`


<dl class="descriptor"><dt>fontlab.flPackage.ps_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.psn"></a>

## `psn`


<dl class="descriptor"><dt>fontlab.flPackage.psn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.readFromFile"></a>

## `readFromFile`


<dl class="function"><dt><a name="-fontlab.flPackage.readFromFile" href="#-fontlab.flPackage.readFromFile"><span class="function-name">fontlab.flPackage.readFromFile</span></a> = readFromFile<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flPackage/Nothing readFromFile(string[, StorageInfo*=0])</pre>

</dd></dl>



<a name="fontlab.flPackage.refCnt"></a>

## `refCnt`


<dl class="descriptor"><dt>fontlab.flPackage.refCnt</dt>
<dd>

<pre class="doc" markdown="0">object references count</pre>

</dd>
</dl>



<a name="fontlab.flPackage.referencesCount"></a>

## `referencesCount`


<dl class="function"><dt><a name="-fontlab.flPackage.referencesCount" href="#-fontlab.flPackage.referencesCount"><span class="function-name">fontlab.flPackage.referencesCount</span></a> = referencesCount<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">int referencesCount(uint shapeDataId)</pre>

</dd></dl>



<a name="fontlab.flPackage.release"></a>

## `release`


<dl class="function"><dt><a name="-fontlab.flPackage.release" href="#-fontlab.flPackage.release"><span class="function-name">fontlab.flPackage.release</span></a> = release<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">release()</pre>

</dd></dl>



<a name="fontlab.flPackage.remove"></a>

## `remove`


<dl class="function"><dt><a name="-fontlab.flPackage.remove" href="#-fontlab.flPackage.remove"><span class="function-name">fontlab.flPackage.remove</span></a> = remove<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">remove([flObject])</pre>

</dd></dl>



<a name="fontlab.flPackage.removeChild"></a>

## `removeChild`


<dl class="function"><dt><a name="-fontlab.flPackage.removeChild" href="#-fontlab.flPackage.removeChild"><span class="function-name">fontlab.flPackage.removeChild</span></a> = removeChild<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeChild(flObject)</pre>

</dd></dl>



<a name="fontlab.flPackage.removeMaster"></a>

## `removeMaster`


<dl class="function"><dt><a name="-fontlab.flPackage.removeMaster" href="#-fontlab.flPackage.removeMaster"><span class="function-name">fontlab.flPackage.removeMaster</span></a> = removeMaster<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeMaster(string name, bool remove_glyph_masters)</pre>

</dd></dl>



<a name="fontlab.flPackage.removeProperty"></a>

## `removeProperty`


<dl class="function"><dt><a name="-fontlab.flPackage.removeProperty" href="#-fontlab.flPackage.removeProperty"><span class="function-name">fontlab.flPackage.removeProperty</span></a> = removeProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">removeProperty('key')</pre>

</dd></dl>



<a name="fontlab.flPackage.renameGlyph"></a>

## `renameGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.renameGlyph" href="#-fontlab.flPackage.renameGlyph"><span class="function-name">fontlab.flPackage.renameGlyph</span></a> = renameGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool renameGlyph(fgGlyph glyph, string name, bool rename)</pre>

</dd></dl>



<a name="fontlab.flPackage.renameMaster"></a>

## `renameMaster`


<dl class="function"><dt><a name="-fontlab.flPackage.renameMaster" href="#-fontlab.flPackage.renameMaster"><span class="function-name">fontlab.flPackage.renameMaster</span></a> = renameMaster<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string renameMaster(string old_name, string new_name)</pre>

</dd></dl>



<a name="fontlab.flPackage.replaceGlyph"></a>

## `replaceGlyph`


<dl class="function"><dt><a name="-fontlab.flPackage.replaceGlyph" href="#-fontlab.flPackage.replaceGlyph"><span class="function-name">fontlab.flPackage.replaceGlyph</span></a> = replaceGlyph<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool replaceGlyph(fgGlyph target, fgGlyph newGlyph, bool rename)</pre>

</dd></dl>



<a name="fontlab.flPackage.replaceShapeWithReference"></a>

## `replaceShapeWithReference`


<dl class="function"><dt><a name="-fontlab.flPackage.replaceShapeWithReference" href="#-fontlab.flPackage.replaceShapeWithReference"><span class="function-name">fontlab.flPackage.replaceShapeWithReference</span></a> = replaceShapeWithReference<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">flShape/Nothing replaceShapeWithReference(flShape shape, bool process[, string layer_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.resetPackage"></a>

## `resetPackage`


<dl class="function"><dt><a name="-fontlab.flPackage.resetPackage" href="#-fontlab.flPackage.resetPackage"><span class="function-name">fontlab.flPackage.resetPackage</span></a> = resetPackage<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">resetPackage()</pre>

</dd></dl>



<a name="fontlab.flPackage.resetStemData"></a>

## `resetStemData`


<dl class="function"><dt><a name="-fontlab.flPackage.resetStemData" href="#-fontlab.flPackage.resetStemData"><span class="function-name">fontlab.flPackage.resetStemData</span></a> = resetStemData<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">(flStems stemsH, flStems stemsV) resetStemData(flStems stemsH, flStems stemsV)</pre>

</dd></dl>



<a name="fontlab.flPackage.restoreHistoryState"></a>

## `restoreHistoryState`


<dl class="function"><dt><a name="-fontlab.flPackage.restoreHistoryState" href="#-fontlab.flPackage.restoreHistoryState"><span class="function-name">fontlab.flPackage.restoreHistoryState</span></a> = restoreHistoryState<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">restoreHistoryState(uint history_ix)</pre>

</dd></dl>



<a name="fontlab.flPackage.safeBottom_value"></a>

## `safeBottom_value`


<dl class="descriptor"><dt>fontlab.flPackage.safeBottom_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.safeTop_value"></a>

## `safeTop_value`


<dl class="descriptor"><dt>fontlab.flPackage.safeTop_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.sampleString"></a>

## `sampleString`


<dl class="descriptor"><dt>fontlab.flPackage.sampleString</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.set_ascender_locked"></a>

## `set_ascender_locked`


<dl class="function"><dt><a name="-fontlab.flPackage.set_ascender_locked" href="#-fontlab.flPackage.set_ascender_locked"><span class="function-name">fontlab.flPackage.set_ascender_locked</span></a> = set_ascender_locked<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_ascender_locked(bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.set_capsHeight_locked"></a>

## `set_capsHeight_locked`


<dl class="function"><dt><a name="-fontlab.flPackage.set_capsHeight_locked" href="#-fontlab.flPackage.set_capsHeight_locked"><span class="function-name">fontlab.flPackage.set_capsHeight_locked</span></a> = set_capsHeight_locked<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_capsHeight_locked(bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.set_descender_locked"></a>

## `set_descender_locked`


<dl class="function"><dt><a name="-fontlab.flPackage.set_descender_locked" href="#-fontlab.flPackage.set_descender_locked"><span class="function-name">fontlab.flPackage.set_descender_locked</span></a> = set_descender_locked<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_descender_locked(bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.set_interpolate"></a>

## `set_interpolate`


<dl class="function"><dt><a name="-fontlab.flPackage.set_interpolate" href="#-fontlab.flPackage.set_interpolate"><span class="function-name">fontlab.flPackage.set_interpolate</span></a> = set_interpolate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_interpolate(bool b[, string master_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.set_measurement_locked"></a>

## `set_measurement_locked`


<dl class="function"><dt><a name="-fontlab.flPackage.set_measurement_locked" href="#-fontlab.flPackage.set_measurement_locked"><span class="function-name">fontlab.flPackage.set_measurement_locked</span></a> = set_measurement_locked<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_measurement_locked(bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.set_xHeight_locked"></a>

## `set_xHeight_locked`


<dl class="function"><dt><a name="-fontlab.flPackage.set_xHeight_locked" href="#-fontlab.flPackage.set_xHeight_locked"><span class="function-name">fontlab.flPackage.set_xHeight_locked</span></a> = set_xHeight_locked<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">set_xHeight_locked(bool b)</pre>

</dd></dl>



<a name="fontlab.flPackage.setAxis"></a>

## `setAxis`


<dl class="function"><dt><a name="-fontlab.flPackage.setAxis" href="#-fontlab.flPackage.setAxis"><span class="function-name">fontlab.flPackage.setAxis</span></a> = setAxis<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setAxis(const flAxis &p)</pre>

</dd></dl>



<a name="fontlab.flPackage.setFlag"></a>

## `setFlag`


<dl class="function"><dt><a name="-fontlab.flPackage.setFlag" href="#-fontlab.flPackage.setFlag"><span class="function-name">fontlab.flPackage.setFlag</span></a> = setFlag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setFlag(uint f [, bool value])</pre>

</dd></dl>



<a name="fontlab.flPackage.setLocation"></a>

## `setLocation`


<dl class="function"><dt><a name="-fontlab.flPackage.setLocation" href="#-fontlab.flPackage.setLocation"><span class="function-name">fontlab.flPackage.setLocation</span></a> = setLocation<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setLocation(flLocation location[, string master_name])</pre>

</dd></dl>



<a name="fontlab.flPackage.setMaster"></a>

## `setMaster`


<dl class="function"><dt><a name="-fontlab.flPackage.setMaster" href="#-fontlab.flPackage.setMaster"><span class="function-name">fontlab.flPackage.setMaster</span></a> = setMaster<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setMaster(string name[, bool notify = false])</pre>

</dd></dl>



<a name="fontlab.flPackage.setProperty"></a>

## `setProperty`


<dl class="function"><dt><a name="-fontlab.flPackage.setProperty" href="#-fontlab.flPackage.setProperty"><span class="function-name">fontlab.flPackage.setProperty</span></a> = setProperty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setProperty('key', value) - set object property by 'key' or number</pre>

</dd></dl>



<a name="fontlab.flPackage.setPropertyFloat"></a>

## `setPropertyFloat`


<dl class="function"><dt><a name="-fontlab.flPackage.setPropertyFloat" href="#-fontlab.flPackage.setPropertyFloat"><span class="function-name">fontlab.flPackage.setPropertyFloat</span></a> = setPropertyFloat<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyFloat('key', value) - set float object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flPackage.setPropertyInt"></a>

## `setPropertyInt`


<dl class="function"><dt><a name="-fontlab.flPackage.setPropertyInt" href="#-fontlab.flPackage.setPropertyInt"><span class="function-name">fontlab.flPackage.setPropertyInt</span></a> = setPropertyInt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setPropertyInt('key', value) - set int object property by 'key'</pre>

</dd></dl>



<a name="fontlab.flPackage.setUpm"></a>

## `setUpm`


<dl class="function"><dt><a name="-fontlab.flPackage.setUpm" href="#-fontlab.flPackage.setUpm"><span class="function-name">fontlab.flPackage.setUpm</span></a> = setUpm<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">setUpm(int upm, bool scale)</pre>

</dd></dl>



<a name="fontlab.flPackage.sgn"></a>

## `sgn`


<dl class="descriptor"><dt>fontlab.flPackage.sgn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.slantTransform"></a>

## `slantTransform`


<dl class="descriptor"><dt>fontlab.flPackage.slantTransform</dt>
<dd>

<pre class="doc" markdown="0">QTransform</pre>

</dd>
</dl>



<a name="fontlab.flPackage.slope"></a>

## `slope`


<dl class="descriptor"><dt>fontlab.flPackage.slope</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.smartCornerParameters"></a>

## `smartCornerParameters`


<dl class="descriptor"><dt>fontlab.flPackage.smartCornerParameters</dt>
<dd>

<pre class="doc" markdown="0">SmartCornerParameters</pre>

</dd>
</dl>



<a name="fontlab.flPackage.stateObject"></a>

## `stateObject`


<dl class="descriptor"><dt>fontlab.flPackage.stateObject</dt>
<dd>

<pre class="doc" markdown="0">flObject</pre>

</dd>
</dl>



<a name="fontlab.flPackage.stems"></a>

## `stems`


<dl class="function"><dt><a name="-fontlab.flPackage.stems" href="#-fontlab.flPackage.stems"><span class="function-name">fontlab.flPackage.stems</span></a> = stems<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flStem)& stems(HintingDataType, bool top)</pre>

</dd></dl>



<a name="fontlab.flPackage.store_font_info"></a>

## `store_font_info`


<dl class="function"><dt><a name="-fontlab.flPackage.store_font_info" href="#-fontlab.flPackage.store_font_info"><span class="function-name">fontlab.flPackage.store_font_info</span></a> = store_font_info<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">store_font_info(fg::Package *package)</pre>

</dd></dl>



<a name="fontlab.flPackage.store_hinting_data"></a>

## `store_hinting_data`


<dl class="function"><dt><a name="-fontlab.flPackage.store_hinting_data" href="#-fontlab.flPackage.store_hinting_data"><span class="function-name">fontlab.flPackage.store_hinting_data</span></a> = store_hinting_data<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">store_hinting_data(fgPackage package)</pre>

</dd></dl>



<a name="fontlab.flPackage.styleCode"></a>

## `styleCode`


<dl class="function"><dt><a name="-fontlab.flPackage.styleCode" href="#-fontlab.flPackage.styleCode"><span class="function-name">fontlab.flPackage.styleCode</span></a> = styleCode<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">unsigned char styleCode()</pre>

</dd></dl>



<a name="fontlab.flPackage.tag"></a>

## `tag`


<dl class="function"><dt><a name="-fontlab.flPackage.tag" href="#-fontlab.flPackage.tag"><span class="function-name">fontlab.flPackage.tag</span></a> = tag<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tag([string])</pre>

</dd></dl>



<a name="fontlab.flPackage.tfn"></a>

## `tfn`


<dl class="descriptor"><dt>fontlab.flPackage.tfn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.title_name"></a>

## `title_name`


<dl class="function"><dt><a name="-fontlab.flPackage.title_name" href="#-fontlab.flPackage.title_name"><span class="function-name">fontlab.flPackage.title_name</span></a> = title_name<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">string title_name([bool force_full = true])</pre>

</dd></dl>



<a name="fontlab.flPackage.tsn"></a>

## `tsn`


<dl class="descriptor"><dt>fontlab.flPackage.tsn</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.tt_stemsH"></a>

## `tt_stemsH`


<dl class="descriptor"><dt>fontlab.flPackage.tt_stemsH</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.tt_stemsV"></a>

## `tt_stemsV`


<dl class="descriptor"><dt>fontlab.flPackage.tt_stemsV</dt>
<dd>

<pre class="doc" markdown="0">list(flStem)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.tt_zonesB"></a>

## `tt_zonesB`


<dl class="descriptor"><dt>fontlab.flPackage.tt_zonesB</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.tt_zonesT"></a>

## `tt_zonesT`


<dl class="descriptor"><dt>fontlab.flPackage.tt_zonesT</dt>
<dd>

<pre class="doc" markdown="0">list(flZone)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.tthRenameStems"></a>

## `tthRenameStems`


<dl class="function"><dt><a name="-fontlab.flPackage.tthRenameStems" href="#-fontlab.flPackage.tthRenameStems"><span class="function-name">fontlab.flPackage.tthRenameStems</span></a> = tthRenameStems<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool tthRenameStems(QMap<QString, QString> map_h, QMap<QString, QString> map_v)</pre>

</dd></dl>



<a name="fontlab.flPackage.tthRenameZones"></a>

## `tthRenameZones`


<dl class="function"><dt><a name="-fontlab.flPackage.tthRenameZones" href="#-fontlab.flPackage.tthRenameZones"><span class="function-name">fontlab.flPackage.tthRenameZones</span></a> = tthRenameZones<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool tthRenameZones(QMap<QString, QString> map_top, QMap<QString, QString> map_bottom)</pre>

</dd></dl>



<a name="fontlab.flPackage.type"></a>

## `type`


<dl class="descriptor"><dt>fontlab.flPackage.type</dt>
<dd>

<pre class="doc" markdown="0">object type</pre>

</dd>
</dl>



<a name="fontlab.flPackage.underlinePosition_value"></a>

## `underlinePosition_value`


<dl class="descriptor"><dt>fontlab.flPackage.underlinePosition_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.underlineThickness_value"></a>

## `underlineThickness_value`


<dl class="descriptor"><dt>fontlab.flPackage.underlineThickness_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.update"></a>

## `update`


<dl class="function"><dt><a name="-fontlab.flPackage.update" href="#-fontlab.flPackage.update"><span class="function-name">fontlab.flPackage.update</span></a> = update<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">update()</pre>

</dd></dl>



<a name="fontlab.flPackage.updateAxesMap"></a>

## `updateAxesMap`


<dl class="function"><dt><a name="-fontlab.flPackage.updateAxesMap" href="#-fontlab.flPackage.updateAxesMap"><span class="function-name">fontlab.flPackage.updateAxesMap</span></a> = updateAxesMap<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateAxesMap()</pre>

</dd></dl>



<a name="fontlab.flPackage.updateFontMetrics"></a>

## `updateFontMetrics`


<dl class="function"><dt><a name="-fontlab.flPackage.updateFontMetrics" href="#-fontlab.flPackage.updateFontMetrics"><span class="function-name">fontlab.flPackage.updateFontMetrics</span></a> = updateFontMetrics<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateFontMetrics()</pre>

</dd></dl>



<a name="fontlab.flPackage.updateShapeReferenceCount"></a>

## `updateShapeReferenceCount`


<dl class="function"><dt><a name="-fontlab.flPackage.updateShapeReferenceCount" href="#-fontlab.flPackage.updateShapeReferenceCount"><span class="function-name">fontlab.flPackage.updateShapeReferenceCount</span></a> = updateShapeReferenceCount<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateShapeReferenceCount()</pre>

</dd></dl>



<a name="fontlab.flPackage.updateZonesFromGuidelines"></a>

## `updateZonesFromGuidelines`


<dl class="function"><dt><a name="-fontlab.flPackage.updateZonesFromGuidelines" href="#-fontlab.flPackage.updateZonesFromGuidelines"><span class="function-name">fontlab.flPackage.updateZonesFromGuidelines</span></a> = updateZonesFromGuidelines<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">updateZonesFromGuidelines([flZones zonesT, flZones zonesB])</pre>

</dd></dl>



<a name="fontlab.flPackage.upm"></a>

## `upm`


<dl class="descriptor"><dt>fontlab.flPackage.upm</dt>
<dd>

<pre class="doc" markdown="0">float</pre>

</dd>
</dl>



<a name="fontlab.flPackage.variables"></a>

## `variables`


<dl class="descriptor"><dt>fontlab.flPackage.variables</dt>
<dd>

<pre class="doc" markdown="0">list(flPropertyDouble)</pre>

</dd>
</dl>



<a name="fontlab.flPackage.variationPackages"></a>

## `variationPackages`


<dl class="descriptor"><dt>fontlab.flPackage.variationPackages</dt>
<dd>

<pre class="doc" markdown="0">QList<flPackage></pre>

</dd>
</dl>



<a name="fontlab.flPackage.versionMajor"></a>

## `versionMajor`


<dl class="descriptor"><dt>fontlab.flPackage.versionMajor</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.versionMinor"></a>

## `versionMinor`


<dl class="descriptor"><dt>fontlab.flPackage.versionMinor</dt>
<dd>

<pre class="doc" markdown="0">int</pre>

</dd>
</dl>



<a name="fontlab.flPackage.weight"></a>

## `weight`


<dl class="descriptor"><dt>fontlab.flPackage.weight</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.weight_value"></a>

## `weight_value`


<dl class="descriptor"><dt>fontlab.flPackage.weight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.width"></a>

## `width`


<dl class="descriptor"><dt>fontlab.flPackage.width</dt>
<dd>

<pre class="doc" markdown="0">string</pre>

</dd>
</dl>



<a name="fontlab.flPackage.width_value"></a>

## `width_value`


<dl class="descriptor"><dt>fontlab.flPackage.width_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.xHeight_value"></a>

## `xHeight_value`


<dl class="descriptor"><dt>fontlab.flPackage.xHeight_value</dt>
<dd>

<pre class="doc" markdown="0">double</pre>

</dd>
</dl>



<a name="fontlab.flPackage.zones"></a>

## `zones`


<dl class="function"><dt><a name="-fontlab.flPackage.zones" href="#-fontlab.flPackage.zones"><span class="function-name">fontlab.flPackage.zones</span></a> = zones<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">list(flZone)& zones(HintingDataType, bool top)</pre>

</dd></dl>

