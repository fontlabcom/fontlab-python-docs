

<a name="typerig.proxy.objects.font"></a>

# `typerig.proxy.objects.font`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.font (<span class="info">version 0.27.4)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Font (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>json</li><li>FL</li><li>math</li><li>PythonQt</li><li>fontTools.pens.statisticsPen</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#jFont">jFont</a></span></li><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#pDesignSpace">pDesignSpace</a></span></li><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#pFont">pFont</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#eFont">eFont</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#pFontMetrics">pFontMetrics</a></span></li><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#pMasters">pMasters</a></span></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.collection.html#treeDict">typerig.core.objects.collection.treeDict</a></span>(<span class="bases">collections.defaultdict</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.font.html#pMaster">pMaster</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="eFont" href="#eFont">class <span class="class-name">eFont</span></a>(<a href="./typerig.proxy.objects.font.html#pFont">pFont</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy Font extension, packing some useful tools.

Constructor:
        eFont() - default represents the current glyph and current font
        eFont(fgFont)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.font.html#eFont">eFont</a></dd><dd><a href="./typerig.proxy.objects.font.html#pFont">pFont</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eFont-copyZones" href="#eFont-copyZones"><span class="function-name">copyZones</span></a><span class="argspec">(self, font)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.font.html#pFont">pFont</a></h4><dl class="function"><dt><a name="eFont-__init__" href="#eFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-__repr__" href="#eFont-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGlyph" href="#eFont-addGlyph"><span class="function-name">addGlyph</span></a><span class="argspec">(self, glyph)</span></dt><dd>

<pre class="doc" markdown="0">Adds a Glyph (fgGlyph or flGlyph) to font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGlyphList" href="#eFont-addGlyphList"><span class="function-name">addGlyphList</span></a><span class="argspec">(self, glyphList)</span></dt><dd>

<pre class="doc" markdown="0">Adds a List of Glyphs [fgGlyph or flGlyph] to font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGuideline" href="#eFont-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Adds a guideline (flGuide) to font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addOTgroup" href="#eFont-addOTgroup"><span class="function-name">addOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addZone" href="#eFont-addZone"><span class="function-name">addZone</span></a><span class="argspec">(self, position, width, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">A very dirty way to add a new Zone to Font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-add_kerning_group" href="#eFont-add_kerning_group"><span class="function-name">add_kerning_group</span></a><span class="argspec">(self, key, glyphNameList, type, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-alternates" href="#eFont-alternates"><span class="function-name">alternates</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all alternate characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-axes" href="#eFont-axes"><span class="function-name">axes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Axes and MM ----------------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-clearFeatures" href="#eFont-clearFeatures"><span class="function-name">clearFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-clearGuidelines" href="#eFont-clearGuidelines"><span class="function-name">clearGuidelines</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Removes all font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-delFeature" href="#eFont-delFeature"><span class="function-name">delFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-delGuideline" href="#eFont-delGuideline"><span class="function-name">delGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Removes a guideline (flGuide) from font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-dict_to_kerning_groups" href="#eFont-dict_to_kerning_groups"><span class="function-name">dict_to_kerning_groups</span></a><span class="argspec">(self, groupDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-duplicateGlyph" href="#eFont-duplicateGlyph"><span class="function-name">duplicateGlyph</span></a><span class="argspec">(self, src_name, dst_name, dst_unicode<span class="parameter-default">=None</span>, options<span class="parameter-default">={'adv': True, 'anc': True, 'flg': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True, 'tag': True}</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a glyph and adds it to the font
Args:
        src_name, dst_name (str): Source and destination names
        dst_unicode (int): Unicode int of the new glyph
        references (bool): Keep existing element references (True) or decompose (False)
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-figures" href="#eFont-figures"><span class="function-name">figures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-findShape" href="#eFont-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, master<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Search for element (flShape) in font and return it</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fl_kerning_groups" href="#eFont-fl_kerning_groups"><span class="function-name">fl_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fl_kerning_groups_to_dict" href="#eFont-fl_kerning_groups_to_dict"><span class="function-name">fl_kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fontMetrics" href="#eFont-fontMetrics"><span class="function-name">fontMetrics</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns <a href="#pFontMetrics">pFontMetrics</a> Object with getter/setter functionality</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fontMetricsInfo" href="#eFont-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (<a href="./__builtin__.html#object">object</a>)</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeaPrefix" href="#eFont-getFeaPrefix"><span class="function-name">getFeaPrefix</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeature" href="#eFont-getFeature"><span class="function-name">getFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeatureTags" href="#eFont-getFeatureTags"><span class="function-name">getFeatureTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeatures" href="#eFont-getFeatures"><span class="function-name">getFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - OpenType and features -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphNameDict" href="#eFont-getGlyphNameDict"><span class="function-name">getGlyphNameDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphNames" href="#eFont-getGlyphNames"><span class="function-name">getGlyphNames</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Charset -----------------------------------------------
# -- Return Names</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphUnicodeDict" href="#eFont-getGlyphUnicodeDict"><span class="function-name">getGlyphUnicodeDict</span></a><span class="argspec">(self, encoding<span class="parameter-default">='utf-8'</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getItalicAngle" href="#eFont-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Font metrics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getOTgroups" href="#eFont-getOTgroups"><span class="function-name">getOTgroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getSelectedIndices" href="#eFont-getSelectedIndices"><span class="function-name">getSelectedIndices</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># Functions ---------------------------------------------------
# - Font Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getZones" href="#eFont-getZones"><span class="function-name">getZones</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns font alignment (blue) zones (list[flGuideline]). Note: HintingDataType = {'HintingPS': 0, 'HintingTT': 1}</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-glyph" href="#eFont-glyph"><span class="function-name">glyph</span></a><span class="argspec">(self, glyph, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> (pGlyph) by index (int) or name (str).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-glyphs" href="#eFont-glyphs"><span class="function-name">glyphs</span></a><span class="argspec">(self, indexList<span class="parameter-default">=[]</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of FontGate glyph objects (list[fgGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-guidelines" href="#eFont-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, hostInf<span class="parameter-default">=False</span>, fontgate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return font guidelines
Args:
        hostInf (bool): If True Return flHostInfo guidelines host objects
        fontgate (bool): If True return FontGate font guideline objects
Returns
        list[flGuideline] or list[fgGuideline]</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasFeature" href="#eFont-hasFeature"><span class="function-name">hasFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasGlyph" href="#eFont-hasGlyph"><span class="function-name">hasGlyph</span></a><span class="argspec">(self, glyphName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasMaster" href="#eFont-hasMaster"><span class="function-name">hasMaster</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hinting" href="#eFont-hinting"><span class="function-name">hinting</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns fonts hinting</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-instances" href="#eFont-instances"><span class="function-name">instances</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning" href="#eFont-kerning"><span class="function-name">kerning</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning <a href="./__builtin__.html#object">object</a> (fgKerning) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_dump" href="#eFont-kerning_dump"><span class="function-name">kerning_dump</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mark_groups<span class="parameter-default">='@'</span>, pairs_only<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Dump layer kerning to simple tuples.
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        mark_groups (String): Mark group kerning with special symbol
        pairs_only (Bool): Export pairs without value

Returns:
        pairs_only is False:    list(tuple(tuple(str(First), str(Second))), Int(Value)))
        pairs_only is True:             list(tuple(str(First), str(Second)))</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_groups" href="#eFont-kerning_groups"><span class="function-name">kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning groups <a href="./__builtin__.html#object">object</a> (fgKerningGroups) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_groups_to_dict" href="#eFont-kerning_groups_to_dict"><span class="function-name">kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, byPosition<span class="parameter-default">=False</span>, sortUnicode<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return dictionary containing kerning groups 
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        byPosition (bool): Dictionary by class kerning positions - KernLeft(1st), KernRight(2nd) or KernBothSide(Both);
        sortUnicode (bool): Sort members of kern group according to their Unicode value.

Returns:
        dict</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_to_list" href="#eFont-kerning_to_list"><span class="function-name">kerning_to_list</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-ligatures" href="#eFont-ligatures"><span class="function-name">ligatures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all ligature characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-lowercase" href="#eFont-lowercase"><span class="function-name">lowercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-masters" href="#eFont-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newGlyph" href="#eFont-newGlyph"><span class="function-name">newGlyph</span></a><span class="argspec">(self, glyph_name, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Creates new glyph and adds it to the font
Args:
        glyph_name (str): New glyph name
        layers (list(str) or list(flLayer)): List of layers to be added to the new glyph
        unicode_int (int): Unicode int of the new glyph
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newGlyphFromRecipe" href="#eFont-newGlyphFromRecipe"><span class="function-name">newGlyphFromRecipe</span></a><span class="argspec">(self, glyph_name, recipe, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>, rtl<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate new glyph (glyph_name) using String Recipe (recipe)
Args:
        glyph_name (str): New glyph name
        recipe (str): Glyph composition recipe using OLD Fontlab syntax (ex. A+acute=Aacute)
        layers (list(str)): List of layer names to be added
        unicode_int (int): Unicode int of the new glyph
        rtl (bool): Right to left
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newKernPair" href="#eFont-newKernPair"><span class="function-name">newKernPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newOTgroup" href="#eFont-newOTgroup"><span class="function-name">newOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-pGlyphs" href="#eFont-pGlyphs"><span class="function-name">pGlyphs</span></a><span class="argspec">(self, fgGlyphList<span class="parameter-default">=[]</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of TypeRig proxy Glyph objects glyph objects (list[pGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-remove_kerning_group" href="#eFont-remove_kerning_group"><span class="function-name">remove_kerning_group</span></a><span class="argspec">(self, key, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-rename_kerning_group" href="#eFont-rename_kerning_group"><span class="function-name">rename_kerning_group</span></a><span class="argspec">(self, oldkey, newkey, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-reset_kerning_groups" href="#eFont-reset_kerning_groups"><span class="function-name">reset_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selectGlyphs" href="#eFont-selectGlyphs"><span class="function-name">selectGlyphs</span></a><span class="argspec">(self, glyphNameList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selectedGlyphs" href="#eFont-selectedGlyphs"><span class="function-name">selectedGlyphs</span></a><span class="argspec">(self, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selected_pGlyphs" href="#eFont-selected_pGlyphs"><span class="function-name">selected_pGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setFeaPrefix" href="#eFont-setFeaPrefix"><span class="function-name">setFeaPrefix</span></a><span class="argspec">(self, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setFeature" href="#eFont-setFeature"><span class="function-name">setFeature</span></a><span class="argspec">(self, tag, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setSelectedIndices" href="#eFont-setSelectedIndices"><span class="function-name">setSelectedIndices</span></a><span class="argspec">(self, indList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setZones" href="#eFont-setZones"><span class="function-name">setZones</span></a><span class="argspec">(self, fontZones, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-symbol" href="#eFont-symbol"><span class="function-name">symbol</span></a><span class="argspec">(self, gID)</span></dt><dd>

<pre class="doc" markdown="0">Return fgSymbol by glyph index (int)</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-symbols" href="#eFont-symbols"><span class="function-name">symbols</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-unselectAll" href="#eFont-unselectAll"><span class="function-name">unselectAll</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-update" href="#eFont-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-updateObject" href="#eFont-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-uppercase" href="#eFont-uppercase"><span class="function-name">uppercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-zonesFromTuples" href="#eFont-zonesFromTuples"><span class="function-name">zonesFromTuples</span></a><span class="argspec">(self, zoneTupleList, layer<span class="parameter-default">=None</span>, forceNames<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-zonesToTuples" href="#eFont-zonesToTuples"><span class="function-name">zonesToTuples</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.font.html#pFont">pFont</a></h4><dl class="descriptor"><dt>OTfullName</dt>
</dl>
<dl class="descriptor"><dt>PSfullName</dt>
</dl>
<dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyName</dt>
</dl>
<dl class="descriptor"><dt>info</dt>
</dl>
<dl class="descriptor"><dt>italic_angle</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>path</dt>
</dl>
</dd>
<dt class="class"><h2><a name="jFont" href="#jFont">class <span class="class-name">jFont</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy VFJ Font (Fontlab JSON Font format)

Constructor:
        jFont(): Construct an empty jFont
        jFont(vfj_file_path): Load VFJ form vfj_file_path (STR)
        jFont(pFont): Load VFJ from pFont.path. VFJ Font has to be in the same path as the VFC

Methods:
        .data(): Access to VFJ font
        .load(file_path): Load VFJ font from path
        .save_as(file_path): Save VFJ font to path
        .save(): Save VFJ (overwrite)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="jFont-__init__" href="#jFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, source<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-load" href="#jFont-load"><span class="function-name">load</span></a><span class="argspec">(self, file_path)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-save" href="#jFont-save"><span class="function-name">save</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-save_as" href="#jFont-save_as"><span class="function-name">save_as</span></a><span class="argspec">(self, file_path)</span></dt><dd>

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
<dt class="class"><h2><a name="pDesignSpace" href="#pDesignSpace">class <span class="class-name">pDesignSpace</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pDesignSpace-__init__" href="#pDesignSpace-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, parent)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pDesignSpace-__repr__" href="#pDesignSpace-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

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
<dl class="descriptor"><dt>axes</dt>
</dl>
<dl class="descriptor"><dt>axes_dict</dt>
</dl>
<dl class="descriptor"><dt>axes_list</dt>
</dl>
</dd>
<dt class="class"><h2><a name="pFont" href="#pFont">class <span class="class-name">pFont</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A Proxy Font representation of Fonlab fgFont and flPackage.

Constructor:
        pFont(None) : Default represents the current glyph and current font
        pFont(fgFont) : Creates a pFont object from FontGate fgFont object
        pFont(file_path) : Loats a existing font form file_path (str) and creates a pFont object</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pFont-__init__" href="#pFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-__repr__" href="#pFont-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGlyph" href="#pFont-addGlyph"><span class="function-name">addGlyph</span></a><span class="argspec">(self, glyph)</span></dt><dd>

<pre class="doc" markdown="0">Adds a Glyph (fgGlyph or flGlyph) to font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGlyphList" href="#pFont-addGlyphList"><span class="function-name">addGlyphList</span></a><span class="argspec">(self, glyphList)</span></dt><dd>

<pre class="doc" markdown="0">Adds a List of Glyphs [fgGlyph or flGlyph] to font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGuideline" href="#pFont-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Adds a guideline (flGuide) to font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addOTgroup" href="#pFont-addOTgroup"><span class="function-name">addOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addZone" href="#pFont-addZone"><span class="function-name">addZone</span></a><span class="argspec">(self, position, width, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">A very dirty way to add a new Zone to Font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-add_kerning_group" href="#pFont-add_kerning_group"><span class="function-name">add_kerning_group</span></a><span class="argspec">(self, key, glyphNameList, type, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-alternates" href="#pFont-alternates"><span class="function-name">alternates</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all alternate characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-axes" href="#pFont-axes"><span class="function-name">axes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Axes and MM ----------------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-clearFeatures" href="#pFont-clearFeatures"><span class="function-name">clearFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-clearGuidelines" href="#pFont-clearGuidelines"><span class="function-name">clearGuidelines</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Removes all font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-delFeature" href="#pFont-delFeature"><span class="function-name">delFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-delGuideline" href="#pFont-delGuideline"><span class="function-name">delGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Removes a guideline (flGuide) from font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-dict_to_kerning_groups" href="#pFont-dict_to_kerning_groups"><span class="function-name">dict_to_kerning_groups</span></a><span class="argspec">(self, groupDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-duplicateGlyph" href="#pFont-duplicateGlyph"><span class="function-name">duplicateGlyph</span></a><span class="argspec">(self, src_name, dst_name, dst_unicode<span class="parameter-default">=None</span>, options<span class="parameter-default">={'adv': True, 'anc': True, 'flg': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True, 'tag': True}</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a glyph and adds it to the font
Args:
        src_name, dst_name (str): Source and destination names
        dst_unicode (int): Unicode int of the new glyph
        references (bool): Keep existing element references (True) or decompose (False)
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-figures" href="#pFont-figures"><span class="function-name">figures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-findShape" href="#pFont-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, master<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Search for element (flShape) in font and return it</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fl_kerning_groups" href="#pFont-fl_kerning_groups"><span class="function-name">fl_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fl_kerning_groups_to_dict" href="#pFont-fl_kerning_groups_to_dict"><span class="function-name">fl_kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fontMetrics" href="#pFont-fontMetrics"><span class="function-name">fontMetrics</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns <a href="#pFontMetrics">pFontMetrics</a> Object with getter/setter functionality</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fontMetricsInfo" href="#pFont-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (<a href="./__builtin__.html#object">object</a>)</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeaPrefix" href="#pFont-getFeaPrefix"><span class="function-name">getFeaPrefix</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeature" href="#pFont-getFeature"><span class="function-name">getFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeatureTags" href="#pFont-getFeatureTags"><span class="function-name">getFeatureTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeatures" href="#pFont-getFeatures"><span class="function-name">getFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - OpenType and features -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphNameDict" href="#pFont-getGlyphNameDict"><span class="function-name">getGlyphNameDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphNames" href="#pFont-getGlyphNames"><span class="function-name">getGlyphNames</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Charset -----------------------------------------------
# -- Return Names</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphUnicodeDict" href="#pFont-getGlyphUnicodeDict"><span class="function-name">getGlyphUnicodeDict</span></a><span class="argspec">(self, encoding<span class="parameter-default">='utf-8'</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getItalicAngle" href="#pFont-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Font metrics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getOTgroups" href="#pFont-getOTgroups"><span class="function-name">getOTgroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getSelectedIndices" href="#pFont-getSelectedIndices"><span class="function-name">getSelectedIndices</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># Functions ---------------------------------------------------
# - Font Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getZones" href="#pFont-getZones"><span class="function-name">getZones</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns font alignment (blue) zones (list[flGuideline]). Note: HintingDataType = {'HintingPS': 0, 'HintingTT': 1}</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-glyph" href="#pFont-glyph"><span class="function-name">glyph</span></a><span class="argspec">(self, glyph, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> (pGlyph) by index (int) or name (str).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-glyphs" href="#pFont-glyphs"><span class="function-name">glyphs</span></a><span class="argspec">(self, indexList<span class="parameter-default">=[]</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of FontGate glyph objects (list[fgGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-guidelines" href="#pFont-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, hostInf<span class="parameter-default">=False</span>, fontgate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return font guidelines
Args:
        hostInf (bool): If True Return flHostInfo guidelines host objects
        fontgate (bool): If True return FontGate font guideline objects
Returns
        list[flGuideline] or list[fgGuideline]</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasFeature" href="#pFont-hasFeature"><span class="function-name">hasFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasGlyph" href="#pFont-hasGlyph"><span class="function-name">hasGlyph</span></a><span class="argspec">(self, glyphName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasMaster" href="#pFont-hasMaster"><span class="function-name">hasMaster</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hinting" href="#pFont-hinting"><span class="function-name">hinting</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns fonts hinting</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-instances" href="#pFont-instances"><span class="function-name">instances</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning" href="#pFont-kerning"><span class="function-name">kerning</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning <a href="./__builtin__.html#object">object</a> (fgKerning) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_dump" href="#pFont-kerning_dump"><span class="function-name">kerning_dump</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mark_groups<span class="parameter-default">='@'</span>, pairs_only<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Dump layer kerning to simple tuples.
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        mark_groups (String): Mark group kerning with special symbol
        pairs_only (Bool): Export pairs without value

Returns:
        pairs_only is False:    list(tuple(tuple(str(First), str(Second))), Int(Value)))
        pairs_only is True:             list(tuple(str(First), str(Second)))</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_groups" href="#pFont-kerning_groups"><span class="function-name">kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning groups <a href="./__builtin__.html#object">object</a> (fgKerningGroups) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_groups_to_dict" href="#pFont-kerning_groups_to_dict"><span class="function-name">kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, byPosition<span class="parameter-default">=False</span>, sortUnicode<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return dictionary containing kerning groups 
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        byPosition (bool): Dictionary by class kerning positions - KernLeft(1st), KernRight(2nd) or KernBothSide(Both);
        sortUnicode (bool): Sort members of kern group according to their Unicode value.

Returns:
        dict</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_to_list" href="#pFont-kerning_to_list"><span class="function-name">kerning_to_list</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-ligatures" href="#pFont-ligatures"><span class="function-name">ligatures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all ligature characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-lowercase" href="#pFont-lowercase"><span class="function-name">lowercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-masters" href="#pFont-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newGlyph" href="#pFont-newGlyph"><span class="function-name">newGlyph</span></a><span class="argspec">(self, glyph_name, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Creates new glyph and adds it to the font
Args:
        glyph_name (str): New glyph name
        layers (list(str) or list(flLayer)): List of layers to be added to the new glyph
        unicode_int (int): Unicode int of the new glyph
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newGlyphFromRecipe" href="#pFont-newGlyphFromRecipe"><span class="function-name">newGlyphFromRecipe</span></a><span class="argspec">(self, glyph_name, recipe, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>, rtl<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate new glyph (glyph_name) using String Recipe (recipe)
Args:
        glyph_name (str): New glyph name
        recipe (str): Glyph composition recipe using OLD Fontlab syntax (ex. A+acute=Aacute)
        layers (list(str)): List of layer names to be added
        unicode_int (int): Unicode int of the new glyph
        rtl (bool): Right to left
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newKernPair" href="#pFont-newKernPair"><span class="function-name">newKernPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newOTgroup" href="#pFont-newOTgroup"><span class="function-name">newOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-pGlyphs" href="#pFont-pGlyphs"><span class="function-name">pGlyphs</span></a><span class="argspec">(self, fgGlyphList<span class="parameter-default">=[]</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of TypeRig proxy Glyph objects glyph objects (list[pGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-remove_kerning_group" href="#pFont-remove_kerning_group"><span class="function-name">remove_kerning_group</span></a><span class="argspec">(self, key, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-rename_kerning_group" href="#pFont-rename_kerning_group"><span class="function-name">rename_kerning_group</span></a><span class="argspec">(self, oldkey, newkey, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-reset_kerning_groups" href="#pFont-reset_kerning_groups"><span class="function-name">reset_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selectGlyphs" href="#pFont-selectGlyphs"><span class="function-name">selectGlyphs</span></a><span class="argspec">(self, glyphNameList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selectedGlyphs" href="#pFont-selectedGlyphs"><span class="function-name">selectedGlyphs</span></a><span class="argspec">(self, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selected_pGlyphs" href="#pFont-selected_pGlyphs"><span class="function-name">selected_pGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph <a href="./__builtin__.html#object">object</a> for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setFeaPrefix" href="#pFont-setFeaPrefix"><span class="function-name">setFeaPrefix</span></a><span class="argspec">(self, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setFeature" href="#pFont-setFeature"><span class="function-name">setFeature</span></a><span class="argspec">(self, tag, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setSelectedIndices" href="#pFont-setSelectedIndices"><span class="function-name">setSelectedIndices</span></a><span class="argspec">(self, indList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setZones" href="#pFont-setZones"><span class="function-name">setZones</span></a><span class="argspec">(self, fontZones, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-symbol" href="#pFont-symbol"><span class="function-name">symbol</span></a><span class="argspec">(self, gID)</span></dt><dd>

<pre class="doc" markdown="0">Return fgSymbol by glyph index (int)</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-symbols" href="#pFont-symbols"><span class="function-name">symbols</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-unselectAll" href="#pFont-unselectAll"><span class="function-name">unselectAll</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-update" href="#pFont-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-updateObject" href="#pFont-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-uppercase" href="#pFont-uppercase"><span class="function-name">uppercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-zonesFromTuples" href="#pFont-zonesFromTuples"><span class="function-name">zonesFromTuples</span></a><span class="argspec">(self, zoneTupleList, layer<span class="parameter-default">=None</span>, forceNames<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-zonesToTuples" href="#pFont-zonesToTuples"><span class="function-name">zonesToTuples</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>OTfullName</dt>
</dl>
<dl class="descriptor"><dt>PSfullName</dt>
</dl>
<dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyName</dt>
</dl>
<dl class="descriptor"><dt>info</dt>
</dl>
<dl class="descriptor"><dt>italic_angle</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>path</dt>
</dl>
</dd>
<dt class="class"><h2><a name="pFontMetrics" href="#pFontMetrics">class <span class="class-name">pFontMetrics</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">An Abstract Font Metrics getter/setter of a flPackage.

Constructor:
        pFontMetrics() - default represents the current glyph and current font
        pFontMetrics(flPackage)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pFontMetrics-__init__" href="#pFontMetrics-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-asDict" href="#pFontMetrics-asDict"><span class="function-name">asDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Export & Import</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-fromDict" href="#pFontMetrics-fromDict"><span class="function-name">fromDict</span></a><span class="argspec">(self, metricDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getAscender" href="#pFontMetrics-getAscender"><span class="function-name">getAscender</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Getters</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getCapsHeight" href="#pFontMetrics-getCapsHeight"><span class="function-name">getCapsHeight</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getCaretOffset" href="#pFontMetrics-getCaretOffset"><span class="function-name">getCaretOffset</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getDescender" href="#pFontMetrics-getDescender"><span class="function-name">getDescender</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getItalicAngle" href="#pFontMetrics-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getLineGap" href="#pFontMetrics-getLineGap"><span class="function-name">getLineGap</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getXHeight" href="#pFontMetrics-getXHeight"><span class="function-name">getXHeight</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setAscender" href="#pFontMetrics-setAscender"><span class="function-name">setAscender</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Setters</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setCapsHeight" href="#pFontMetrics-setCapsHeight"><span class="function-name">setCapsHeight</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setCaretOffset" href="#pFontMetrics-setCaretOffset"><span class="function-name">setCaretOffset</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setDescender" href="#pFontMetrics-setDescender"><span class="function-name">setDescender</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setItalicAngle" href="#pFontMetrics-setItalicAngle"><span class="function-name">setItalicAngle</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setLineGap" href="#pFontMetrics-setLineGap"><span class="function-name">setLineGap</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setXHeight" href="#pFontMetrics-setXHeight"><span class="function-name">setXHeight</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

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
<dt class="class"><h2><a name="pMaster" href="#pMaster">class <span class="class-name">pMaster</span></a>(<a href="./typerig.core.objects.collection.html#treeDict">typerig.core.objects.collection.treeDict</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.font.html#pMaster">pMaster</a></dd><dd><a href="./typerig.core.objects.collection.html#treeDict">typerig.core.objects.collection.treeDict</a></dd><dd><a href="./collections.html#defaultdict">collections.defaultdict</a></dd><dd><a href="./__builtin__.html#dict">__builtin__.dict</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pMaster-__init__" href="#pMaster-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, *args, **kwargs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__repr__" href="#pMaster-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.collection.html#treeDict">typerig.core.objects.collection.treeDict</a></h4><dl class="function"><dt><a name="pMaster-__getattribute__" href="#pMaster-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(self, name)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__setattr__" href="#pMaster-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(self, name, value)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.collection.html#treeDict">typerig.core.objects.collection.treeDict</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="function"><dt><a name="pMaster-__copy__" href="#pMaster-__copy__"><span class="function-name">__copy__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__missing__" href="#pMaster-__missing__"><span class="function-name">__missing__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#pMaster-__missing__">__missing__</a>(key) # Called by __getitem__ for missing key; pseudo-code:
if self.<strong>default_factory</strong> is None: raise KeyError((key,))
self[key] = value = self.<a href="#pMaster-default_factory">default_factory</a>()
return value</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__reduce__" href="#pMaster-__reduce__"><span class="function-name">__reduce__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Return state information for pickling.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-copy" href="#pMaster-copy"><span class="function-name">copy</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-copy">copy</a>() -> a shallow copy of D.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./collections.html#defaultdict">collections.defaultdict</a></h4><dl class="descriptor"><dt>default_factory</dt>
<dd>

<pre class="doc" markdown="0">Factory for default value called by __missing__().</pre>

</dd>
</dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl class="function"><dt><a name="pMaster-__cmp__" href="#pMaster-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__contains__" href="#pMaster-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-__contains__">__contains__</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__delitem__" href="#pMaster-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__eq__" href="#pMaster-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__ge__" href="#pMaster-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__getitem__" href="#pMaster-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__gt__" href="#pMaster-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__iter__" href="#pMaster-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__le__" href="#pMaster-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__len__" href="#pMaster-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__lt__" href="#pMaster-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__ne__" href="#pMaster-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__setitem__" href="#pMaster-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#pMaster-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-__sizeof__" href="#pMaster-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-__sizeof__">__sizeof__</a>() -> size of D in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-clear" href="#pMaster-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-clear">clear</a>() -> None.  Remove all items from D.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-fromkeys" href="#pMaster-fromkeys"><span class="function-name">fromkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">dict.<a href="#pMaster-fromkeys">fromkeys</a>(S[,v]) -> New dict with keys from S and values equal to v.
v defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-get" href="#pMaster-get"><span class="function-name">get</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-get">get</a>(k[,d]) -> D[k] if k in D, else d.  d defaults to None.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-has_key" href="#pMaster-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-has_key">has_key</a>(k) -> True if D has a key k, else False</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-items" href="#pMaster-items"><span class="function-name">items</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-items">items</a>() -> list of D's (key, value) pairs, as 2-tuples</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-iteritems" href="#pMaster-iteritems"><span class="function-name">iteritems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-iteritems">iteritems</a>() -> an iterator over the (key, value) items of D</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-iterkeys" href="#pMaster-iterkeys"><span class="function-name">iterkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-iterkeys">iterkeys</a>() -> an iterator over the keys of D</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-itervalues" href="#pMaster-itervalues"><span class="function-name">itervalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-itervalues">itervalues</a>() -> an iterator over the values of D</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-keys" href="#pMaster-keys"><span class="function-name">keys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-keys">keys</a>() -> list of D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-pop" href="#pMaster-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-pop">pop</a>(k[,d]) -> v, remove specified key and return the corresponding value.
If key is not found, d is returned if given, otherwise KeyError is raised</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-popitem" href="#pMaster-popitem"><span class="function-name">popitem</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-popitem">popitem</a>() -> (k, v), remove and return some (key, value) pair as a
2-tuple; but raise KeyError if D is empty.</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-setdefault" href="#pMaster-setdefault"><span class="function-name">setdefault</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-setdefault">setdefault</a>(k[,d]) -> D.<a href="#pMaster-get">get</a>(k,d), also set D[k]=d if k not in D</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-update" href="#pMaster-update"><span class="function-name">update</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-update">update</a>([E, ]**F) -> None.  Update D from dict/iterable E and F.
If E present and has a .<a href="#pMaster-keys">keys</a>() method, does:     for k in E: D[k] = E[k]
If E present and lacks .<a href="#pMaster-keys">keys</a>() method, does:     for (k, v) in E: D[k] = v
In either case, this is followed by: for k in F: D[k] = F[k]</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-values" href="#pMaster-values"><span class="function-name">values</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-values">values</a>() -> list of D's values</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-viewitems" href="#pMaster-viewitems"><span class="function-name">viewitems</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-viewitems">viewitems</a>() -> a set-like <a href="./__builtin__.html#object">object</a> providing a view on D's items</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-viewkeys" href="#pMaster-viewkeys"><span class="function-name">viewkeys</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-viewkeys">viewkeys</a>() -> a set-like <a href="./__builtin__.html#object">object</a> providing a view on D's keys</pre>

</dd></dl>
<dl class="function"><dt><a name="pMaster-viewvalues" href="#pMaster-viewvalues"><span class="function-name">viewvalues</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">D.<a href="#pMaster-viewvalues">viewvalues</a>() -> an <a href="./__builtin__.html#object">object</a> providing a view on D's values</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#dict">__builtin__.dict</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#pMaster-__new__">__new__</a>(S, ...) -> a new <a href="./__builtin__.html#object">object</a> with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="pMasters" href="#pMasters">class <span class="class-name">pMasters</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pMasters-__init__" href="#pMasters-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, parent)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMasters-__repr__" href="#pMasters-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMasters-groupByWidth" href="#pMasters-groupByWidth"><span class="function-name">groupByWidth</span></a><span class="argspec">(self, double<span class="parameter-default">=0.0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMasters-locate" href="#pMasters-locate"><span class="function-name">locate</span></a><span class="argspec">(self, master_name, axes_list<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pMasters-locateAxis" href="#pMasters-locateAxis"><span class="function-name">locateAxis</span></a><span class="argspec">(self, master_name, axis_tag, width<span class="parameter-default">=False</span>)</span></dt><dd>

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
<dl class="descriptor"><dt>masters</dt>
</dl>
</dd></dl></div></div>


<a name="typerig.proxy.objects.font.pFontMetrics"></a>

## `pFontMetrics`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.font.pFontMetrics</span> = <a name="typerig.proxy.objects.font.pFontMetrics" href="#typerig.proxy.objects.font.pFontMetrics">class pFontMetrics</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">An Abstract Font Metrics getter/setter of a flPackage.

Constructor:
        pFontMetrics() - default represents the current glyph and current font
        pFontMetrics(flPackage)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pFontMetrics-__init__" href="#pFontMetrics-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-asDict" href="#pFontMetrics-asDict"><span class="function-name">asDict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Export & Import</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-fromDict" href="#pFontMetrics-fromDict"><span class="function-name">fromDict</span></a><span class="argspec">(self, metricDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getAscender" href="#pFontMetrics-getAscender"><span class="function-name">getAscender</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Getters</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getCapsHeight" href="#pFontMetrics-getCapsHeight"><span class="function-name">getCapsHeight</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getCaretOffset" href="#pFontMetrics-getCaretOffset"><span class="function-name">getCaretOffset</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getDescender" href="#pFontMetrics-getDescender"><span class="function-name">getDescender</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getItalicAngle" href="#pFontMetrics-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getLineGap" href="#pFontMetrics-getLineGap"><span class="function-name">getLineGap</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-getXHeight" href="#pFontMetrics-getXHeight"><span class="function-name">getXHeight</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setAscender" href="#pFontMetrics-setAscender"><span class="function-name">setAscender</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"># - Setters</pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setCapsHeight" href="#pFontMetrics-setCapsHeight"><span class="function-name">setCapsHeight</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setCaretOffset" href="#pFontMetrics-setCaretOffset"><span class="function-name">setCaretOffset</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setDescender" href="#pFontMetrics-setDescender"><span class="function-name">setDescender</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setItalicAngle" href="#pFontMetrics-setItalicAngle"><span class="function-name">setItalicAngle</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setLineGap" href="#pFontMetrics-setLineGap"><span class="function-name">setLineGap</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFontMetrics-setXHeight" href="#pFontMetrics-setXHeight"><span class="function-name">setXHeight</span></a><span class="argspec">(self, value, layer<span class="parameter-default">=None</span>)</span></dt><dd>

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


<a name="typerig.proxy.objects.font.pFont"></a>

## `pFont`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.font.pFont</span> = <a name="typerig.proxy.objects.font.pFont" href="#typerig.proxy.objects.font.pFont">class pFont</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">A Proxy Font representation of Fonlab fgFont and flPackage.

Constructor:
        pFont(None) : Default represents the current glyph and current font
        pFont(fgFont) : Creates a pFont object from FontGate fgFont object
        pFont(file_path) : Loats a existing font form file_path (str) and creates a pFont object</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pFont-__init__" href="#pFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-__repr__" href="#pFont-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGlyph" href="#pFont-addGlyph"><span class="function-name">addGlyph</span></a><span class="argspec">(self, glyph)</span></dt><dd>

<pre class="doc" markdown="0">Adds a Glyph (fgGlyph or flGlyph) to font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGlyphList" href="#pFont-addGlyphList"><span class="function-name">addGlyphList</span></a><span class="argspec">(self, glyphList)</span></dt><dd>

<pre class="doc" markdown="0">Adds a List of Glyphs [fgGlyph or flGlyph] to font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addGuideline" href="#pFont-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Adds a guideline (flGuide) to font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addOTgroup" href="#pFont-addOTgroup"><span class="function-name">addOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-addZone" href="#pFont-addZone"><span class="function-name">addZone</span></a><span class="argspec">(self, position, width, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">A very dirty way to add a new Zone to Font</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-add_kerning_group" href="#pFont-add_kerning_group"><span class="function-name">add_kerning_group</span></a><span class="argspec">(self, key, glyphNameList, type, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-alternates" href="#pFont-alternates"><span class="function-name">alternates</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all alternate characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-axes" href="#pFont-axes"><span class="function-name">axes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Axes and MM ----------------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-clearFeatures" href="#pFont-clearFeatures"><span class="function-name">clearFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-clearGuidelines" href="#pFont-clearGuidelines"><span class="function-name">clearGuidelines</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Removes all font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-delFeature" href="#pFont-delFeature"><span class="function-name">delFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-delGuideline" href="#pFont-delGuideline"><span class="function-name">delGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Removes a guideline (flGuide) from font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-dict_to_kerning_groups" href="#pFont-dict_to_kerning_groups"><span class="function-name">dict_to_kerning_groups</span></a><span class="argspec">(self, groupDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-duplicateGlyph" href="#pFont-duplicateGlyph"><span class="function-name">duplicateGlyph</span></a><span class="argspec">(self, src_name, dst_name, dst_unicode<span class="parameter-default">=None</span>, options<span class="parameter-default">={'adv': True, 'anc': True, 'flg': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True, 'tag': True}</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a glyph and adds it to the font
Args:
        src_name, dst_name (str): Source and destination names
        dst_unicode (int): Unicode int of the new glyph
        references (bool): Keep existing element references (True) or decompose (False)
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-figures" href="#pFont-figures"><span class="function-name">figures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-findShape" href="#pFont-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, master<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Search for element (flShape) in font and return it</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fl_kerning_groups" href="#pFont-fl_kerning_groups"><span class="function-name">fl_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fl_kerning_groups_to_dict" href="#pFont-fl_kerning_groups_to_dict"><span class="function-name">fl_kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fontMetrics" href="#pFont-fontMetrics"><span class="function-name">fontMetrics</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns pFontMetrics Object with getter/setter functionality</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-fontMetricsInfo" href="#pFont-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeaPrefix" href="#pFont-getFeaPrefix"><span class="function-name">getFeaPrefix</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeature" href="#pFont-getFeature"><span class="function-name">getFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeatureTags" href="#pFont-getFeatureTags"><span class="function-name">getFeatureTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getFeatures" href="#pFont-getFeatures"><span class="function-name">getFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - OpenType and features -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphNameDict" href="#pFont-getGlyphNameDict"><span class="function-name">getGlyphNameDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphNames" href="#pFont-getGlyphNames"><span class="function-name">getGlyphNames</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Charset -----------------------------------------------
# -- Return Names</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getGlyphUnicodeDict" href="#pFont-getGlyphUnicodeDict"><span class="function-name">getGlyphUnicodeDict</span></a><span class="argspec">(self, encoding<span class="parameter-default">='utf-8'</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getItalicAngle" href="#pFont-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Font metrics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getOTgroups" href="#pFont-getOTgroups"><span class="function-name">getOTgroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getSelectedIndices" href="#pFont-getSelectedIndices"><span class="function-name">getSelectedIndices</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># Functions ---------------------------------------------------
# - Font Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-getZones" href="#pFont-getZones"><span class="function-name">getZones</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns font alignment (blue) zones (list[flGuideline]). Note: HintingDataType = {'HintingPS': 0, 'HintingTT': 1}</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-glyph" href="#pFont-glyph"><span class="function-name">glyph</span></a><span class="argspec">(self, glyph, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object (pGlyph) by index (int) or name (str).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-glyphs" href="#pFont-glyphs"><span class="function-name">glyphs</span></a><span class="argspec">(self, indexList<span class="parameter-default">=[]</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of FontGate glyph objects (list[fgGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-guidelines" href="#pFont-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, hostInf<span class="parameter-default">=False</span>, fontgate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return font guidelines
Args:
        hostInf (bool): If True Return flHostInfo guidelines host objects
        fontgate (bool): If True return FontGate font guideline objects
Returns
        list[flGuideline] or list[fgGuideline]</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasFeature" href="#pFont-hasFeature"><span class="function-name">hasFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasGlyph" href="#pFont-hasGlyph"><span class="function-name">hasGlyph</span></a><span class="argspec">(self, glyphName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hasMaster" href="#pFont-hasMaster"><span class="function-name">hasMaster</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-hinting" href="#pFont-hinting"><span class="function-name">hinting</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns fonts hinting</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-instances" href="#pFont-instances"><span class="function-name">instances</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning" href="#pFont-kerning"><span class="function-name">kerning</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning object (fgKerning) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_dump" href="#pFont-kerning_dump"><span class="function-name">kerning_dump</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mark_groups<span class="parameter-default">='@'</span>, pairs_only<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Dump layer kerning to simple tuples.
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        mark_groups (String): Mark group kerning with special symbol
        pairs_only (Bool): Export pairs without value

Returns:
        pairs_only is False:    list(tuple(tuple(str(First), str(Second))), Int(Value)))
        pairs_only is True:             list(tuple(str(First), str(Second)))</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_groups" href="#pFont-kerning_groups"><span class="function-name">kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning groups object (fgKerningGroups) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_groups_to_dict" href="#pFont-kerning_groups_to_dict"><span class="function-name">kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, byPosition<span class="parameter-default">=False</span>, sortUnicode<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return dictionary containing kerning groups 
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        byPosition (bool): Dictionary by class kerning positions - KernLeft(1st), KernRight(2nd) or KernBothSide(Both);
        sortUnicode (bool): Sort members of kern group according to their Unicode value.

Returns:
        dict</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-kerning_to_list" href="#pFont-kerning_to_list"><span class="function-name">kerning_to_list</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-ligatures" href="#pFont-ligatures"><span class="function-name">ligatures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all ligature characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-lowercase" href="#pFont-lowercase"><span class="function-name">lowercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-masters" href="#pFont-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newGlyph" href="#pFont-newGlyph"><span class="function-name">newGlyph</span></a><span class="argspec">(self, glyph_name, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Creates new glyph and adds it to the font
Args:
        glyph_name (str): New glyph name
        layers (list(str) or list(flLayer)): List of layers to be added to the new glyph
        unicode_int (int): Unicode int of the new glyph
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newGlyphFromRecipe" href="#pFont-newGlyphFromRecipe"><span class="function-name">newGlyphFromRecipe</span></a><span class="argspec">(self, glyph_name, recipe, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>, rtl<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate new glyph (glyph_name) using String Recipe (recipe)
Args:
        glyph_name (str): New glyph name
        recipe (str): Glyph composition recipe using OLD Fontlab syntax (ex. A+acute=Aacute)
        layers (list(str)): List of layer names to be added
        unicode_int (int): Unicode int of the new glyph
        rtl (bool): Right to left
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newKernPair" href="#pFont-newKernPair"><span class="function-name">newKernPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-newOTgroup" href="#pFont-newOTgroup"><span class="function-name">newOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-pGlyphs" href="#pFont-pGlyphs"><span class="function-name">pGlyphs</span></a><span class="argspec">(self, fgGlyphList<span class="parameter-default">=[]</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of TypeRig proxy Glyph objects glyph objects (list[pGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-remove_kerning_group" href="#pFont-remove_kerning_group"><span class="function-name">remove_kerning_group</span></a><span class="argspec">(self, key, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-rename_kerning_group" href="#pFont-rename_kerning_group"><span class="function-name">rename_kerning_group</span></a><span class="argspec">(self, oldkey, newkey, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-reset_kerning_groups" href="#pFont-reset_kerning_groups"><span class="function-name">reset_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selectGlyphs" href="#pFont-selectGlyphs"><span class="function-name">selectGlyphs</span></a><span class="argspec">(self, glyphNameList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selectedGlyphs" href="#pFont-selectedGlyphs"><span class="function-name">selectedGlyphs</span></a><span class="argspec">(self, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-selected_pGlyphs" href="#pFont-selected_pGlyphs"><span class="function-name">selected_pGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setFeaPrefix" href="#pFont-setFeaPrefix"><span class="function-name">setFeaPrefix</span></a><span class="argspec">(self, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setFeature" href="#pFont-setFeature"><span class="function-name">setFeature</span></a><span class="argspec">(self, tag, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setSelectedIndices" href="#pFont-setSelectedIndices"><span class="function-name">setSelectedIndices</span></a><span class="argspec">(self, indList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-setZones" href="#pFont-setZones"><span class="function-name">setZones</span></a><span class="argspec">(self, fontZones, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-symbol" href="#pFont-symbol"><span class="function-name">symbol</span></a><span class="argspec">(self, gID)</span></dt><dd>

<pre class="doc" markdown="0">Return fgSymbol by glyph index (int)</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-symbols" href="#pFont-symbols"><span class="function-name">symbols</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-unselectAll" href="#pFont-unselectAll"><span class="function-name">unselectAll</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-update" href="#pFont-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-updateObject" href="#pFont-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-uppercase" href="#pFont-uppercase"><span class="function-name">uppercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-zonesFromTuples" href="#pFont-zonesFromTuples"><span class="function-name">zonesFromTuples</span></a><span class="argspec">(self, zoneTupleList, layer<span class="parameter-default">=None</span>, forceNames<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pFont-zonesToTuples" href="#pFont-zonesToTuples"><span class="function-name">zonesToTuples</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>OTfullName</dt>
</dl>
<dl class="descriptor"><dt>PSfullName</dt>
</dl>
<dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyName</dt>
</dl>
<dl class="descriptor"><dt>info</dt>
</dl>
<dl class="descriptor"><dt>italic_angle</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>path</dt>
</dl>
</dd>


<a name="typerig.proxy.objects.font.pFont.selected_pGlyphs"></a>

### `selected_pGlyphs`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.selected_pGlyphs" href="#-typerig.proxy.objects.font.pFont.selected_pGlyphs"><span class="function-name">typerig.proxy.objects.font.pFont.selected_pGlyphs</span></a> = selected_pGlyphs<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.selectedGlyphs"></a>

### `selectedGlyphs`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.selectedGlyphs" href="#-typerig.proxy.objects.font.pFont.selectedGlyphs"><span class="function-name">typerig.proxy.objects.font.pFont.selectedGlyphs</span></a> = selectedGlyphs<span class="argspec">(self, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.glyph"></a>

### `glyph`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.glyph" href="#-typerig.proxy.objects.font.pFont.glyph"><span class="function-name">typerig.proxy.objects.font.pFont.glyph</span></a> = glyph<span class="argspec">(self, glyph, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object (pGlyph) by index (int) or name (str).</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.symbol"></a>

### `symbol`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.symbol" href="#-typerig.proxy.objects.font.pFont.symbol"><span class="function-name">typerig.proxy.objects.font.pFont.symbol</span></a> = symbol<span class="argspec">(self, gID)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return fgSymbol by glyph index (int)</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.glyphs"></a>

### `glyphs`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.glyphs" href="#-typerig.proxy.objects.font.pFont.glyphs"><span class="function-name">typerig.proxy.objects.font.pFont.glyphs</span></a> = glyphs<span class="argspec">(self, indexList<span class="parameter-default">=[]</span>, extend<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return list of FontGate glyph objects (list[fgGlyph]).</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.pGlyphs"></a>

### `pGlyphs`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.pGlyphs" href="#-typerig.proxy.objects.font.pFont.pGlyphs"><span class="function-name">typerig.proxy.objects.font.pFont.pGlyphs</span></a> = pGlyphs<span class="argspec">(self, fgGlyphList<span class="parameter-default">=[]</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return list of TypeRig proxy Glyph objects glyph objects (list[pGlyph]).</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.findShape"></a>

### `findShape`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.findShape" href="#-typerig.proxy.objects.font.pFont.findShape"><span class="function-name">typerig.proxy.objects.font.pFont.findShape</span></a> = findShape<span class="argspec">(self, shapeName, master<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Search for element (flShape) in font and return it</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.fontMetricsInfo"></a>

### `fontMetricsInfo`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.fontMetricsInfo" href="#-typerig.proxy.objects.font.pFont.fontMetricsInfo"><span class="function-name">typerig.proxy.objects.font.pFont.fontMetricsInfo</span></a> = fontMetricsInfo<span class="argspec">(self, layer)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.fontMetrics"></a>

### `fontMetrics`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.fontMetrics" href="#-typerig.proxy.objects.font.pFont.fontMetrics"><span class="function-name">typerig.proxy.objects.font.pFont.fontMetrics</span></a> = fontMetrics<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns pFontMetrics Object with getter/setter functionality</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.updateObject"></a>

### `updateObject`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.updateObject" href="#-typerig.proxy.objects.font.pFont.updateObject"><span class="function-name">typerig.proxy.objects.font.pFont.updateObject</span></a> = updateObject<span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.guidelines"></a>

### `guidelines`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.guidelines" href="#-typerig.proxy.objects.font.pFont.guidelines"><span class="function-name">typerig.proxy.objects.font.pFont.guidelines</span></a> = guidelines<span class="argspec">(self, hostInf<span class="parameter-default">=False</span>, fontgate<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return font guidelines
Args:
        hostInf (bool): If True Return flHostInfo guidelines host objects
        fontgate (bool): If True return FontGate font guideline objects
Returns
        list[flGuideline] or list[fgGuideline]</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.addGuideline"></a>

### `addGuideline`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.addGuideline" href="#-typerig.proxy.objects.font.pFont.addGuideline"><span class="function-name">typerig.proxy.objects.font.pFont.addGuideline</span></a> = addGuideline<span class="argspec">(self, flGuide)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a guideline (flGuide) to font guidelines</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.delGuideline"></a>

### `delGuideline`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.delGuideline" href="#-typerig.proxy.objects.font.pFont.delGuideline"><span class="function-name">typerig.proxy.objects.font.pFont.delGuideline</span></a> = delGuideline<span class="argspec">(self, flGuide)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Removes a guideline (flGuide) from font guidelines</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.clearGuidelines"></a>

### `clearGuidelines`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.clearGuidelines" href="#-typerig.proxy.objects.font.pFont.clearGuidelines"><span class="function-name">typerig.proxy.objects.font.pFont.clearGuidelines</span></a> = clearGuidelines<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Removes all font guidelines</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.getZones"></a>

### `getZones`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.getZones" href="#-typerig.proxy.objects.font.pFont.getZones"><span class="function-name">typerig.proxy.objects.font.pFont.getZones</span></a> = getZones<span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns font alignment (blue) zones (list[flGuideline]). Note: HintingDataType = {'HintingPS': 0, 'HintingTT': 1}</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.addZone"></a>

### `addZone`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.addZone" href="#-typerig.proxy.objects.font.pFont.addZone"><span class="function-name">typerig.proxy.objects.font.pFont.addZone</span></a> = addZone<span class="argspec">(self, position, width, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">A very dirty way to add a new Zone to Font</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.hinting"></a>

### `hinting`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.hinting" href="#-typerig.proxy.objects.font.pFont.hinting"><span class="function-name">typerig.proxy.objects.font.pFont.hinting</span></a> = hinting<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns fonts hinting</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.uppercase"></a>

### `uppercase`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.uppercase" href="#-typerig.proxy.objects.font.pFont.uppercase"><span class="function-name">typerig.proxy.objects.font.pFont.uppercase</span></a> = uppercase<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.lowercase"></a>

### `lowercase`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.lowercase" href="#-typerig.proxy.objects.font.pFont.lowercase"><span class="function-name">typerig.proxy.objects.font.pFont.lowercase</span></a> = lowercase<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.figures"></a>

### `figures`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.figures" href="#-typerig.proxy.objects.font.pFont.figures"><span class="function-name">typerig.proxy.objects.font.pFont.figures</span></a> = figures<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.symbols"></a>

### `symbols`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.symbols" href="#-typerig.proxy.objects.font.pFont.symbols"><span class="function-name">typerig.proxy.objects.font.pFont.symbols</span></a> = symbols<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.ligatures"></a>

### `ligatures`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.ligatures" href="#-typerig.proxy.objects.font.pFont.ligatures"><span class="function-name">typerig.proxy.objects.font.pFont.ligatures</span></a> = ligatures<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all ligature characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.alternates"></a>

### `alternates`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.alternates" href="#-typerig.proxy.objects.font.pFont.alternates"><span class="function-name">typerig.proxy.objects.font.pFont.alternates</span></a> = alternates<span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Returns all alternate characters (list[fgGlyph])</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.addGlyph"></a>

### `addGlyph`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.addGlyph" href="#-typerig.proxy.objects.font.pFont.addGlyph"><span class="function-name">typerig.proxy.objects.font.pFont.addGlyph</span></a> = addGlyph<span class="argspec">(self, glyph)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a Glyph (fgGlyph or flGlyph) to font</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.addGlyphList"></a>

### `addGlyphList`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.addGlyphList" href="#-typerig.proxy.objects.font.pFont.addGlyphList"><span class="function-name">typerig.proxy.objects.font.pFont.addGlyphList</span></a> = addGlyphList<span class="argspec">(self, glyphList)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a List of Glyphs [fgGlyph or flGlyph] to font</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.newGlyph"></a>

### `newGlyph`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.newGlyph" href="#-typerig.proxy.objects.font.pFont.newGlyph"><span class="function-name">typerig.proxy.objects.font.pFont.newGlyph</span></a> = newGlyph<span class="argspec">(self, glyph_name, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Creates new glyph and adds it to the font
Args:
        glyph_name (str): New glyph name
        layers (list(str) or list(flLayer)): List of layers to be added to the new glyph
        unicode_int (int): Unicode int of the new glyph
Returns:
        pGlyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.newGlyphFromRecipe"></a>

### `newGlyphFromRecipe`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.newGlyphFromRecipe" href="#-typerig.proxy.objects.font.pFont.newGlyphFromRecipe"><span class="function-name">typerig.proxy.objects.font.pFont.newGlyphFromRecipe</span></a> = newGlyphFromRecipe<span class="argspec">(self, glyph_name, recipe, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>, rtl<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Generate new glyph (glyph_name) using String Recipe (recipe)
Args:
        glyph_name (str): New glyph name
        recipe (str): Glyph composition recipe using OLD Fontlab syntax (ex. A+acute=Aacute)
        layers (list(str)): List of layer names to be added
        unicode_int (int): Unicode int of the new glyph
        rtl (bool): Right to left
Returns:
        pGlyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.duplicateGlyph"></a>

### `duplicateGlyph`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.duplicateGlyph" href="#-typerig.proxy.objects.font.pFont.duplicateGlyph"><span class="function-name">typerig.proxy.objects.font.pFont.duplicateGlyph</span></a> = duplicateGlyph<span class="argspec">(self, src_name, dst_name, dst_unicode<span class="parameter-default">=None</span>, options<span class="parameter-default">={'adv': True, 'anc': True, 'flg': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True, 'tag': True}</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a glyph and adds it to the font
Args:
        src_name, dst_name (str): Source and destination names
        dst_unicode (int): Unicode int of the new glyph
        references (bool): Keep existing element references (True) or decompose (False)
Returns:
        pGlyph</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.kerning"></a>

### `kerning`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.kerning" href="#-typerig.proxy.objects.font.pFont.kerning"><span class="function-name">typerig.proxy.objects.font.pFont.kerning</span></a> = kerning<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning object (fgKerning) no matter the reference.</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.kerning_dump"></a>

### `kerning_dump`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.kerning_dump" href="#-typerig.proxy.objects.font.pFont.kerning_dump"><span class="function-name">typerig.proxy.objects.font.pFont.kerning_dump</span></a> = kerning_dump<span class="argspec">(self, layer<span class="parameter-default">=None</span>, mark_groups<span class="parameter-default">='@'</span>, pairs_only<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Dump layer kerning to simple tuples.
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        mark_groups (String): Mark group kerning with special symbol
        pairs_only (Bool): Export pairs without value

Returns:
        pairs_only is False:    list(tuple(tuple(str(First), str(Second))), Int(Value)))
        pairs_only is True:             list(tuple(str(First), str(Second)))</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.kerning_groups"></a>

### `kerning_groups`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.kerning_groups" href="#-typerig.proxy.objects.font.pFont.kerning_groups"><span class="function-name">typerig.proxy.objects.font.pFont.kerning_groups</span></a> = kerning_groups<span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning groups object (fgKerningGroups) no matter the reference.</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.kerning_groups_to_dict"></a>

### `kerning_groups_to_dict`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.kerning_groups_to_dict" href="#-typerig.proxy.objects.font.pFont.kerning_groups_to_dict"><span class="function-name">typerig.proxy.objects.font.pFont.kerning_groups_to_dict</span></a> = kerning_groups_to_dict<span class="argspec">(self, layer<span class="parameter-default">=None</span>, byPosition<span class="parameter-default">=False</span>, sortUnicode<span class="parameter-default">=False</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return dictionary containing kerning groups 
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        byPosition (bool): Dictionary by class kerning positions - KernLeft(1st), KernRight(2nd) or KernBothSide(Both);
        sortUnicode (bool): Sort members of kern group according to their Unicode value.

Returns:
        dict</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.add_kerning_group"></a>

### `add_kerning_group`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.add_kerning_group" href="#-typerig.proxy.objects.font.pFont.add_kerning_group"><span class="function-name">typerig.proxy.objects.font.pFont.add_kerning_group</span></a> = add_kerning_group<span class="argspec">(self, key, glyphNameList, type, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.remove_kerning_group"></a>

### `remove_kerning_group`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.remove_kerning_group" href="#-typerig.proxy.objects.font.pFont.remove_kerning_group"><span class="function-name">typerig.proxy.objects.font.pFont.remove_kerning_group</span></a> = remove_kerning_group<span class="argspec">(self, key, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.pFont.rename_kerning_group"></a>

### `rename_kerning_group`


<dl class="function"><dt><a name="-typerig.proxy.objects.font.pFont.rename_kerning_group" href="#-typerig.proxy.objects.font.pFont.rename_kerning_group"><span class="function-name">typerig.proxy.objects.font.pFont.rename_kerning_group</span></a> = rename_kerning_group<span class="argspec">(self, oldkey, newkey, layer<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.font.html#pFont">typerig.proxy.objects.font.pFont</a> method</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>



<a name="typerig.proxy.objects.font.eFont"></a>

## `eFont`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.font.eFont</span> = <a name="typerig.proxy.objects.font.eFont" href="#typerig.proxy.objects.font.eFont">class eFont</a>(<a href="./typerig.proxy.objects.font.html#pFont">pFont</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy Font extension, packing some useful tools.

Constructor:
        eFont() - default represents the current glyph and current font
        eFont(fgFont)</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.proxy.objects.font.html#eFont">eFont</a></dd><dd><a href="./typerig.proxy.objects.font.html#pFont">pFont</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="eFont-copyZones" href="#eFont-copyZones"><span class="function-name">copyZones</span></a><span class="argspec">(self, font)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.proxy.objects.font.html#pFont">pFont</a></h4><dl class="function"><dt><a name="eFont-__init__" href="#eFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, font<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-__repr__" href="#eFont-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGlyph" href="#eFont-addGlyph"><span class="function-name">addGlyph</span></a><span class="argspec">(self, glyph)</span></dt><dd>

<pre class="doc" markdown="0">Adds a Glyph (fgGlyph or flGlyph) to font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGlyphList" href="#eFont-addGlyphList"><span class="function-name">addGlyphList</span></a><span class="argspec">(self, glyphList)</span></dt><dd>

<pre class="doc" markdown="0">Adds a List of Glyphs [fgGlyph or flGlyph] to font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addGuideline" href="#eFont-addGuideline"><span class="function-name">addGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Adds a guideline (flGuide) to font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addOTgroup" href="#eFont-addOTgroup"><span class="function-name">addOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-addZone" href="#eFont-addZone"><span class="function-name">addZone</span></a><span class="argspec">(self, position, width, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">A very dirty way to add a new Zone to Font</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-add_kerning_group" href="#eFont-add_kerning_group"><span class="function-name">add_kerning_group</span></a><span class="argspec">(self, key, glyphNameList, type, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-alternates" href="#eFont-alternates"><span class="function-name">alternates</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all alternate characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-axes" href="#eFont-axes"><span class="function-name">axes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Axes and MM ----------------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-clearFeatures" href="#eFont-clearFeatures"><span class="function-name">clearFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-clearGuidelines" href="#eFont-clearGuidelines"><span class="function-name">clearGuidelines</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Removes all font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-delFeature" href="#eFont-delFeature"><span class="function-name">delFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-delGuideline" href="#eFont-delGuideline"><span class="function-name">delGuideline</span></a><span class="argspec">(self, flGuide)</span></dt><dd>

<pre class="doc" markdown="0">Removes a guideline (flGuide) from font guidelines</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-dict_to_kerning_groups" href="#eFont-dict_to_kerning_groups"><span class="function-name">dict_to_kerning_groups</span></a><span class="argspec">(self, groupDict, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-duplicateGlyph" href="#eFont-duplicateGlyph"><span class="function-name">duplicateGlyph</span></a><span class="argspec">(self, src_name, dst_name, dst_unicode<span class="parameter-default">=None</span>, options<span class="parameter-default">={'adv': True, 'anc': True, 'flg': True, 'gui': True, 'lnk': True, 'lsb': True, 'out': True, 'ref': True, 'rsb': True, 'tag': True}</span>)</span></dt><dd>

<pre class="doc" markdown="0">Duplicates a glyph and adds it to the font
Args:
        src_name, dst_name (str): Source and destination names
        dst_unicode (int): Unicode int of the new glyph
        references (bool): Keep existing element references (True) or decompose (False)
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-figures" href="#eFont-figures"><span class="function-name">figures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-findShape" href="#eFont-findShape"><span class="function-name">findShape</span></a><span class="argspec">(self, shapeName, master<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Search for element (flShape) in font and return it</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fl_kerning_groups" href="#eFont-fl_kerning_groups"><span class="function-name">fl_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fl_kerning_groups_to_dict" href="#eFont-fl_kerning_groups_to_dict"><span class="function-name">fl_kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fontMetrics" href="#eFont-fontMetrics"><span class="function-name">fontMetrics</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns pFontMetrics Object with getter/setter functionality</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-fontMetricsInfo" href="#eFont-fontMetricsInfo"><span class="function-name">fontMetricsInfo</span></a><span class="argspec">(self, layer)</span></dt><dd>

<pre class="doc" markdown="0">Returns Font(layer) metrics no matter the reference.
Args:
        layer (int or str): Layer index or name. If None returns ActiveLayer
Returns:
        FontMetrics (object)</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeaPrefix" href="#eFont-getFeaPrefix"><span class="function-name">getFeaPrefix</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeature" href="#eFont-getFeature"><span class="function-name">getFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeatureTags" href="#eFont-getFeatureTags"><span class="function-name">getFeatureTags</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getFeatures" href="#eFont-getFeatures"><span class="function-name">getFeatures</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - OpenType and features -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphNameDict" href="#eFont-getGlyphNameDict"><span class="function-name">getGlyphNameDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphNames" href="#eFont-getGlyphNames"><span class="function-name">getGlyphNames</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Charset -----------------------------------------------
# -- Return Names</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getGlyphUnicodeDict" href="#eFont-getGlyphUnicodeDict"><span class="function-name">getGlyphUnicodeDict</span></a><span class="argspec">(self, encoding<span class="parameter-default">='utf-8'</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getItalicAngle" href="#eFont-getItalicAngle"><span class="function-name">getItalicAngle</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Font metrics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getOTgroups" href="#eFont-getOTgroups"><span class="function-name">getOTgroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getSelectedIndices" href="#eFont-getSelectedIndices"><span class="function-name">getSelectedIndices</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># Functions ---------------------------------------------------
# - Font Basics -----------------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-getZones" href="#eFont-getZones"><span class="function-name">getZones</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns font alignment (blue) zones (list[flGuideline]). Note: HintingDataType = {'HintingPS': 0, 'HintingTT': 1}</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-glyph" href="#eFont-glyph"><span class="function-name">glyph</span></a><span class="argspec">(self, glyph, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object (pGlyph) by index (int) or name (str).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-glyphs" href="#eFont-glyphs"><span class="function-name">glyphs</span></a><span class="argspec">(self, indexList<span class="parameter-default">=[]</span>, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of FontGate glyph objects (list[fgGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-guidelines" href="#eFont-guidelines"><span class="function-name">guidelines</span></a><span class="argspec">(self, hostInf<span class="parameter-default">=False</span>, fontgate<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return font guidelines
Args:
        hostInf (bool): If True Return flHostInfo guidelines host objects
        fontgate (bool): If True return FontGate font guideline objects
Returns
        list[flGuideline] or list[fgGuideline]</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasFeature" href="#eFont-hasFeature"><span class="function-name">hasFeature</span></a><span class="argspec">(self, tag)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasGlyph" href="#eFont-hasGlyph"><span class="function-name">hasGlyph</span></a><span class="argspec">(self, glyphName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hasMaster" href="#eFont-hasMaster"><span class="function-name">hasMaster</span></a><span class="argspec">(self, layerName)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-hinting" href="#eFont-hinting"><span class="function-name">hinting</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Returns fonts hinting</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-instances" href="#eFont-instances"><span class="function-name">instances</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning" href="#eFont-kerning"><span class="function-name">kerning</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning object (fgKerning) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_dump" href="#eFont-kerning_dump"><span class="function-name">kerning_dump</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, mark_groups<span class="parameter-default">='@'</span>, pairs_only<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Dump layer kerning to simple tuples.
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        mark_groups (String): Mark group kerning with special symbol
        pairs_only (Bool): Export pairs without value

Returns:
        pairs_only is False:    list(tuple(tuple(str(First), str(Second))), Int(Value)))
        pairs_only is True:             list(tuple(str(First), str(Second)))</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_groups" href="#eFont-kerning_groups"><span class="function-name">kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return the fonts kerning groups object (fgKerningGroups) no matter the reference.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_groups_to_dict" href="#eFont-kerning_groups_to_dict"><span class="function-name">kerning_groups_to_dict</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, byPosition<span class="parameter-default">=False</span>, sortUnicode<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return dictionary containing kerning groups 
Args:
        layer (None, Int, String): Extract kerning data for layer specified;
        byPosition (bool): Dictionary by class kerning positions - KernLeft(1st), KernRight(2nd) or KernBothSide(Both);
        sortUnicode (bool): Sort members of kern group according to their Unicode value.

Returns:
        dict</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-kerning_to_list" href="#eFont-kerning_to_list"><span class="function-name">kerning_to_list</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-ligatures" href="#eFont-ligatures"><span class="function-name">ligatures</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all ligature characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-lowercase" href="#eFont-lowercase"><span class="function-name">lowercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-masters" href="#eFont-masters"><span class="function-name">masters</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newGlyph" href="#eFont-newGlyph"><span class="function-name">newGlyph</span></a><span class="argspec">(self, glyph_name, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Creates new glyph and adds it to the font
Args:
        glyph_name (str): New glyph name
        layers (list(str) or list(flLayer)): List of layers to be added to the new glyph
        unicode_int (int): Unicode int of the new glyph
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newGlyphFromRecipe" href="#eFont-newGlyphFromRecipe"><span class="function-name">newGlyphFromRecipe</span></a><span class="argspec">(self, glyph_name, recipe, layers<span class="parameter-default">=[]</span>, unicode_int<span class="parameter-default">=None</span>, rtl<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate new glyph (glyph_name) using String Recipe (recipe)
Args:
        glyph_name (str): New glyph name
        recipe (str): Glyph composition recipe using OLD Fontlab syntax (ex. A+acute=Aacute)
        layers (list(str)): List of layer names to be added
        unicode_int (int): Unicode int of the new glyph
        rtl (bool): Right to left
Returns:
        pGlyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newKernPair" href="#eFont-newKernPair"><span class="function-name">newKernPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-newOTgroup" href="#eFont-newOTgroup"><span class="function-name">newOTgroup</span></a><span class="argspec">(self, groupName, glyphList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-pGlyphs" href="#eFont-pGlyphs"><span class="function-name">pGlyphs</span></a><span class="argspec">(self, fgGlyphList<span class="parameter-default">=[]</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return list of TypeRig proxy Glyph objects glyph objects (list[pGlyph]).</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-remove_kerning_group" href="#eFont-remove_kerning_group"><span class="function-name">remove_kerning_group</span></a><span class="argspec">(self, key, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-rename_kerning_group" href="#eFont-rename_kerning_group"><span class="function-name">rename_kerning_group</span></a><span class="argspec">(self, oldkey, newkey, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-reset_kerning_groups" href="#eFont-reset_kerning_groups"><span class="function-name">reset_kerning_groups</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selectGlyphs" href="#eFont-selectGlyphs"><span class="function-name">selectGlyphs</span></a><span class="argspec">(self, glyphNameList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selectedGlyphs" href="#eFont-selectedGlyphs"><span class="function-name">selectedGlyphs</span></a><span class="argspec">(self, extend<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-selected_pGlyphs" href="#eFont-selected_pGlyphs"><span class="function-name">selected_pGlyphs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return TypeRig proxy glyph object for each selected glyph</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setFeaPrefix" href="#eFont-setFeaPrefix"><span class="function-name">setFeaPrefix</span></a><span class="argspec">(self, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setFeature" href="#eFont-setFeature"><span class="function-name">setFeature</span></a><span class="argspec">(self, tag, feaString)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setSelectedIndices" href="#eFont-setSelectedIndices"><span class="function-name">setSelectedIndices</span></a><span class="argspec">(self, indList)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-setZones" href="#eFont-setZones"><span class="function-name">setZones</span></a><span class="argspec">(self, fontZones, layer<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-symbol" href="#eFont-symbol"><span class="function-name">symbol</span></a><span class="argspec">(self, gID)</span></dt><dd>

<pre class="doc" markdown="0">Return fgSymbol by glyph index (int)</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-symbols" href="#eFont-symbols"><span class="function-name">symbols</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-unselectAll" href="#eFont-unselectAll"><span class="function-name">unselectAll</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-update" href="#eFont-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-updateObject" href="#eFont-updateObject"><span class="function-name">updateObject</span></a><span class="argspec">(self, flObject, undoMessage<span class="parameter-default">='TypeRig'</span>, verbose<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0">Updates a flObject sends notification to the editor as well as undo/history item.
Args:
        flObject (flGlyph, flLayer, flShape, flNode, flContour): Object to be update and set undo state
        undoMessage (string): Message to be added in undo/history list.</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-uppercase" href="#eFont-uppercase"><span class="function-name">uppercase</span></a><span class="argspec">(self, namesOnly<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0">Returns all uppercase characters (list[fgGlyph])</pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-zonesFromTuples" href="#eFont-zonesFromTuples"><span class="function-name">zonesFromTuples</span></a><span class="argspec">(self, zoneTupleList, layer<span class="parameter-default">=None</span>, forceNames<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="eFont-zonesToTuples" href="#eFont-zonesToTuples"><span class="function-name">zonesToTuples</span></a><span class="argspec">(self, layer<span class="parameter-default">=None</span>, HintingDataType<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.proxy.objects.font.html#pFont">pFont</a></h4><dl class="descriptor"><dt>OTfullName</dt>
</dl>
<dl class="descriptor"><dt>PSfullName</dt>
</dl>
<dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyName</dt>
</dl>
<dl class="descriptor"><dt>info</dt>
</dl>
<dl class="descriptor"><dt>italic_angle</dt>
</dl>
<dl class="descriptor"><dt>name</dt>
</dl>
<dl class="descriptor"><dt>path</dt>
</dl>
</dd>


<a name="typerig.proxy.objects.font.jFont"></a>

## `jFont`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.font.jFont</span> = <a name="typerig.proxy.objects.font.jFont" href="#typerig.proxy.objects.font.jFont">class jFont</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy VFJ Font (Fontlab JSON Font format)

Constructor:
        jFont(): Construct an empty jFont
        jFont(vfj_file_path): Load VFJ form vfj_file_path (STR)
        jFont(pFont): Load VFJ from pFont.path. VFJ Font has to be in the same path as the VFC

Methods:
        .data(): Access to VFJ font
        .load(file_path): Load VFJ font from path
        .save_as(file_path): Save VFJ font to path
        .save(): Save VFJ (overwrite)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="jFont-__init__" href="#jFont-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, source<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-load" href="#jFont-load"><span class="function-name">load</span></a><span class="argspec">(self, file_path)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-save" href="#jFont-save"><span class="function-name">save</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="jFont-save_as" href="#jFont-save_as"><span class="function-name">save_as</span></a><span class="argspec">(self, file_path)</span></dt><dd>

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
