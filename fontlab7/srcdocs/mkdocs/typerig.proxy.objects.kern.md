

<a name="typerig.proxy.objects.kern"></a>

# `typerig.proxy.objects.kern`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.objects.html">objects</a>.kern (<span class="info">version 0.26.3)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Kern (Objects)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2018-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>PythonQt</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.objects.kern.html#pKerning">pKerning</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="pKerning" href="#pKerning">class <span class="class-name">pKerning</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to fgKerning object

Constructor:
        pKerning(fgKerning)

Attributes:
        .fg (fgKerning): Original Fontgate Kerning object 
        .groups (fgKerningGroups): Fontgate Group kerning object</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pKerning-__init__" href="#pKerning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, fgKerningObject, externalGroupData<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-__repr__" href="#pKerning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-addGroup" href="#pKerning-addGroup"><span class="function-name">addGroup</span></a><span class="argspec">(self, key, glyphNameList, type)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-asDict" href="#pKerning-asDict"><span class="function-name">asDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-asList" href="#pKerning-asList"><span class="function-name">asList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-clear" href="#pKerning-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basic functions -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getKerningForLeaders" href="#pKerning-getKerningForLeaders"><span class="function-name">getKerningForLeaders</span></a><span class="argspec">(self, transformLeft<span class="parameter-default">=None</span>, transformRight<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Now in FL6 we do not have leaders, but this returns the first glyph name in the group</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPair" href="#pKerning-getPair"><span class="function-name">getPair</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPairGroups" href="#pKerning-getPairGroups"><span class="function-name">getPairGroups</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPairObject" href="#pKerning-getPairObject"><span class="function-name">getPairObject</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groups" href="#pKerning-groups"><span class="function-name">groups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsAsDict" href="#pKerning-groupsAsDict"><span class="function-name">groupsAsDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsBiDict" href="#pKerning-groupsBiDict"><span class="function-name">groupsBiDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsFromDict" href="#pKerning-groupsFromDict"><span class="function-name">groupsFromDict</span></a><span class="argspec">(self, groupDict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-newPair" href="#pKerning-newPair"><span class="function-name">newPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-removeGroup" href="#pKerning-removeGroup"><span class="function-name">removeGroup</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-renameGroup" href="#pKerning-renameGroup"><span class="function-name">renameGroup</span></a><span class="argspec">(self, oldkey, newkey)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-resetGroups" href="#pKerning-resetGroups"><span class="function-name">resetGroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setExternalGroupData" href="#pKerning-setExternalGroupData"><span class="function-name">setExternalGroupData</span></a><span class="argspec">(self, externalGroupData)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setPair" href="#pKerning-setPair"><span class="function-name">setPair</span></a><span class="argspec">(self, pairTuple, modeTuple<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setPairs" href="#pKerning-setPairs"><span class="function-name">setPairs</span></a><span class="argspec">(self, pairTupleList, extend<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-storeExternalGroupData" href="#pKerning-storeExternalGroupData"><span class="function-name">storeExternalGroupData</span></a><span class="argspec">(self)</span></dt><dd>

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


<a name="typerig.proxy.objects.kern.pKerning"></a>

## `pKerning`


<dt class="class"><h2><span class="class-name">typerig.proxy.objects.kern.pKerning</span> = <a name="typerig.proxy.objects.kern.pKerning" href="#typerig.proxy.objects.kern.pKerning">class pKerning</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to fgKerning object

Constructor:
        pKerning(fgKerning)

Attributes:
        .fg (fgKerning): Original Fontgate Kerning object 
        .groups (fgKerningGroups): Fontgate Group kerning object</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pKerning-__init__" href="#pKerning-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, fgKerningObject, externalGroupData<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-__repr__" href="#pKerning-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-addGroup" href="#pKerning-addGroup"><span class="function-name">addGroup</span></a><span class="argspec">(self, key, glyphNameList, type)</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-asDict" href="#pKerning-asDict"><span class="function-name">asDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-asList" href="#pKerning-asList"><span class="function-name">asList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-clear" href="#pKerning-clear"><span class="function-name">clear</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"># - Basic functions -------------------------------------</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getKerningForLeaders" href="#pKerning-getKerningForLeaders"><span class="function-name">getKerningForLeaders</span></a><span class="argspec">(self, transformLeft<span class="parameter-default">=None</span>, transformRight<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Now in FL6 we do not have leaders, but this returns the first glyph name in the group</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPair" href="#pKerning-getPair"><span class="function-name">getPair</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPairGroups" href="#pKerning-getPairGroups"><span class="function-name">getPairGroups</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-getPairObject" href="#pKerning-getPairObject"><span class="function-name">getPairObject</span></a><span class="argspec">(self, pairTuple)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groups" href="#pKerning-groups"><span class="function-name">groups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsAsDict" href="#pKerning-groupsAsDict"><span class="function-name">groupsAsDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsBiDict" href="#pKerning-groupsBiDict"><span class="function-name">groupsBiDict</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-groupsFromDict" href="#pKerning-groupsFromDict"><span class="function-name">groupsFromDict</span></a><span class="argspec">(self, groupDict)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-newPair" href="#pKerning-newPair"><span class="function-name">newPair</span></a><span class="argspec">(self, glyphLeft, glyphRight, modeLeft, modeRight)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-removeGroup" href="#pKerning-removeGroup"><span class="function-name">removeGroup</span></a><span class="argspec">(self, key)</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-renameGroup" href="#pKerning-renameGroup"><span class="function-name">renameGroup</span></a><span class="argspec">(self, oldkey, newkey)</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-resetGroups" href="#pKerning-resetGroups"><span class="function-name">resetGroups</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setExternalGroupData" href="#pKerning-setExternalGroupData"><span class="function-name">setExternalGroupData</span></a><span class="argspec">(self, externalGroupData)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setPair" href="#pKerning-setPair"><span class="function-name">setPair</span></a><span class="argspec">(self, pairTuple, modeTuple<span class="parameter-default">=(0, 0)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-setPairs" href="#pKerning-setPairs"><span class="function-name">setPairs</span></a><span class="argspec">(self, pairTupleList, extend<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pKerning-storeExternalGroupData" href="#pKerning-storeExternalGroupData"><span class="function-name">storeExternalGroupData</span></a><span class="argspec">(self)</span></dt><dd>

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


<a name="typerig.proxy.objects.kern.pKerning.removeGroup"></a>

### `removeGroup`


<dl class="function"><dt><a name="-typerig.proxy.objects.kern.pKerning.removeGroup" href="#-typerig.proxy.objects.kern.pKerning.removeGroup"><span class="function-name">typerig.proxy.objects.kern.pKerning.removeGroup</span></a> = removeGroup<span class="argspec">(self, key)</span><span class="note"> unbound <a href="./typerig.proxy.objects.kern.html#pKerning">typerig.proxy.objects.kern.pKerning</a> method</span></dt><dd>

<pre class="doc" markdown="0">Remove a group from fonts kerning groups at given layer.</pre>

</dd></dl>



<a name="typerig.proxy.objects.kern.pKerning.renameGroup"></a>

### `renameGroup`


<dl class="function"><dt><a name="-typerig.proxy.objects.kern.pKerning.renameGroup" href="#-typerig.proxy.objects.kern.pKerning.renameGroup"><span class="function-name">typerig.proxy.objects.kern.pKerning.renameGroup</span></a> = renameGroup<span class="argspec">(self, oldkey, newkey)</span><span class="note"> unbound <a href="./typerig.proxy.objects.kern.html#pKerning">typerig.proxy.objects.kern.pKerning</a> method</span></dt><dd>

<pre class="doc" markdown="0">Rename a group in fonts kerning groups at given layer.</pre>

</dd></dl>



<a name="typerig.proxy.objects.kern.pKerning.addGroup"></a>

### `addGroup`


<dl class="function"><dt><a name="-typerig.proxy.objects.kern.pKerning.addGroup" href="#-typerig.proxy.objects.kern.pKerning.addGroup"><span class="function-name">typerig.proxy.objects.kern.pKerning.addGroup</span></a> = addGroup<span class="argspec">(self, key, glyphNameList, type)</span><span class="note"> unbound <a href="./typerig.proxy.objects.kern.html#pKerning">typerig.proxy.objects.kern.pKerning</a> method</span></dt><dd>

<pre class="doc" markdown="0">Adds a new group to fonts kerning groups.
Args:
        key (string): Group name
        glyphNameList (list(string)): List of glyph names
        type (string): Kern group types: L - Left group (1st), R - Right group (2nd), B - Both (1st and 2nd)
        layer (None, Int, String)

Returns:
        None</pre>

</dd></dl>



<a name="typerig.proxy.objects.kern.pKerning.getKerningForLeaders"></a>

### `getKerningForLeaders`


<dl class="function"><dt><a name="-typerig.proxy.objects.kern.pKerning.getKerningForLeaders" href="#-typerig.proxy.objects.kern.pKerning.getKerningForLeaders"><span class="function-name">typerig.proxy.objects.kern.pKerning.getKerningForLeaders</span></a> = getKerningForLeaders<span class="argspec">(self, transformLeft<span class="parameter-default">=None</span>, transformRight<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.proxy.objects.kern.html#pKerning">typerig.proxy.objects.kern.pKerning</a> method</span></dt><dd>

<pre class="doc" markdown="0">Now in FL6 we do not have leaders, but this returns the first glyph name in the group</pre>

</dd></dl>

