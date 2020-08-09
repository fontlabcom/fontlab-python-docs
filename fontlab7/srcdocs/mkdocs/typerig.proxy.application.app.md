

<a name="typerig.proxy.application.app"></a>

# `typerig.proxy.application.app`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.proxy.html">proxy</a>.<a href="./typerig.proxy.application.html">application</a>.app (<span class="info">version 0.76.0)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / Proxy / Application
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2019-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>fontgate</li><li>fontlab</li><li>PythonQt</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.proxy.application.app.html#pItems">pItems</a></span></li><li><span class="class-name"><a href="./typerig.proxy.application.app.html#pTextBlock">pTextBlock</a></span></li><li><span class="class-name"><a href="./typerig.proxy.application.app.html#pWorkspace">pWorkspace</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="pItems" href="#pItems">class <span class="class-name">pItems</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flItems object

Constructor:
        pItems()

Attributes:
        .fl (flItems): Current workspace</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pItems-__init__" href="#pItems-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pItems-outputGlyphNames" href="#pItems-outputGlyphNames"><span class="function-name">outputGlyphNames</span></a><span class="argspec">(self, glyphNamesList, layerList<span class="parameter-default">=[]</span>, cursor_location<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Output text string using glyph names and layers specified</pre>

</dd></dl>
<dl class="function"><dt><a name="pItems-outputString" href="#pItems-outputString"><span class="function-name">outputString</span></a><span class="argspec">(self, string, cursor_location<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Output text to the application</pre>

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
<dt class="class"><h2><a name="pTextBlock" href="#pTextBlock">class <span class="class-name">pTextBlock</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flTextBlock object

Constructor:
        pTextBlock(flTextBlock)

Attributes:
        .fl (flTextBlock): flTextBlock Parent</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pTextBlock-__init__" href="#pTextBlock-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, textBlock)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-__repr__" href="#pTextBlock-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-clone" href="#pTextBlock-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getFontSize" href="#pTextBlock-getFontSize"><span class="function-name">getFontSize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getFrameSize" href="#pTextBlock-getFrameSize"><span class="function-name">getFrameSize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getGlyphBounds" href="#pTextBlock-getGlyphBounds"><span class="function-name">getGlyphBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getString" href="#pTextBlock-getString"><span class="function-name">getString</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getTransform" href="#pTextBlock-getTransform"><span class="function-name">getTransform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getWrapState" href="#pTextBlock-getWrapState"><span class="function-name">getWrapState</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-height" href="#pTextBlock-height"><span class="function-name">height</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-reloc" href="#pTextBlock-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-resetTransform" href="#pTextBlock-resetTransform"><span class="function-name">resetTransform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFontSize" href="#pTextBlock-setFontSize"><span class="function-name">setFontSize</span></a><span class="argspec">(self, fontSize)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFrameSize" href="#pTextBlock-setFrameSize"><span class="function-name">setFrameSize</span></a><span class="argspec">(self, width, height)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFrameWidth" href="#pTextBlock-setFrameWidth"><span class="function-name">setFrameWidth</span></a><span class="argspec">(self, width)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setPageSize" href="#pTextBlock-setPageSize"><span class="function-name">setPageSize</span></a><span class="argspec">(self, sizeName, fixedHeight<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setTextWrap" href="#pTextBlock-setTextWrap"><span class="function-name">setTextWrap</span></a><span class="argspec">(self, width)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setTransform" href="#pTextBlock-setTransform"><span class="function-name">setTransform</span></a><span class="argspec">(self, newTransform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setWrapState" href="#pTextBlock-setWrapState"><span class="function-name">setWrapState</span></a><span class="argspec">(self, wrapText<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-update" href="#pTextBlock-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-width" href="#pTextBlock-width"><span class="function-name">width</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-x" href="#pTextBlock-x"><span class="function-name">x</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-y" href="#pTextBlock-y"><span class="function-name">y</span></a><span class="argspec">(self)</span></dt><dd>

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
<dt class="class"><h2><a name="pWorkspace" href="#pWorkspace">class <span class="class-name">pWorkspace</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flWorkspace object

Constructor:
        pWorkspace()

Attributes:
        .fl (flWorkspace): Current workspace
        .main (QWidget): Main QWidget's window</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pWorkspace-__init__" href="#pWorkspace-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-createFrame" href="#pWorkspace-createFrame"><span class="function-name">createFrame</span></a><span class="argspec">(self, string, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveGlyph" href="#pWorkspace-getActiveGlyph"><span class="function-name">getActiveGlyph</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveGlyphInfo" href="#pWorkspace-getActiveGlyphInfo"><span class="function-name">getActiveGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveIndex" href="#pWorkspace-getActiveIndex"><span class="function-name">getActiveIndex</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveKernPair" href="#pWorkspace-getActiveKernPair"><span class="function-name">getActiveKernPair</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveLine" href="#pWorkspace-getActiveLine"><span class="function-name">getActiveLine</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getCanvas" href="#pWorkspace-getCanvas"><span class="function-name">getCanvas</span></a><span class="argspec">(self, atCursor<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getCanvasList" href="#pWorkspace-getCanvasList"><span class="function-name">getCanvasList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getNextGlyphInfo" href="#pWorkspace-getNextGlyphInfo"><span class="function-name">getNextGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getPrevGlyphInfo" href="#pWorkspace-getPrevGlyphInfo"><span class="function-name">getPrevGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getSelectedNodes" href="#pWorkspace-getSelectedNodes"><span class="function-name">getSelectedNodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getTextBlockGlyphs" href="#pWorkspace-getTextBlockGlyphs"><span class="function-name">getTextBlockGlyphs</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getTextBlockList" href="#pWorkspace-getTextBlockList"><span class="function-name">getTextBlockList</span></a><span class="argspec">(self, atCursor<span class="parameter-default">=False</span>)</span></dt><dd>

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
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-openFont" href="#-openFont"><span class="function-name">openFont</span></a><span class="argspec">(file_path)</span></dt><dd>

<pre class="doc" markdown="0">Loads Font file from path (str) and returns opened fgFont <a href="./__builtin__.html#object">object</a></pre>

</dd></dl>
</dl></div></div>


<a name="typerig.proxy.application.app.openFont"></a>

## `openFont`


<dl class="function"><dt><a name="-typerig.proxy.application.app.openFont" href="#-typerig.proxy.application.app.openFont"><span class="function-name">typerig.proxy.application.app.openFont</span></a> = openFont<span class="argspec">(file_path)</span></dt><dd>

<pre class="doc" markdown="0">Loads Font file from path (str) and returns opened fgFont object</pre>

</dd></dl>



<a name="typerig.proxy.application.app.pItems"></a>

## `pItems`


<dt class="class"><h2><span class="class-name">typerig.proxy.application.app.pItems</span> = <a name="typerig.proxy.application.app.pItems" href="#typerig.proxy.application.app.pItems">class pItems</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flItems object

Constructor:
        pItems()

Attributes:
        .fl (flItems): Current workspace</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pItems-__init__" href="#pItems-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pItems-outputGlyphNames" href="#pItems-outputGlyphNames"><span class="function-name">outputGlyphNames</span></a><span class="argspec">(self, glyphNamesList, layerList<span class="parameter-default">=[]</span>, cursor_location<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Output text string using glyph names and layers specified</pre>

</dd></dl>
<dl class="function"><dt><a name="pItems-outputString" href="#pItems-outputString"><span class="function-name">outputString</span></a><span class="argspec">(self, string, cursor_location<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Output text to the application</pre>

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


<a name="typerig.proxy.application.app.pItems.outputString"></a>

### `outputString`


<dl class="function"><dt><a name="-typerig.proxy.application.app.pItems.outputString" href="#-typerig.proxy.application.app.pItems.outputString"><span class="function-name">typerig.proxy.application.app.pItems.outputString</span></a> = outputString<span class="argspec">(self, string, cursor_location<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.application.app.html#pItems">typerig.proxy.application.app.pItems</a> method</span></dt><dd>

<pre class="doc" markdown="0">Output text to the application</pre>

</dd></dl>



<a name="typerig.proxy.application.app.pItems.outputGlyphNames"></a>

### `outputGlyphNames`


<dl class="function"><dt><a name="-typerig.proxy.application.app.pItems.outputGlyphNames" href="#-typerig.proxy.application.app.pItems.outputGlyphNames"><span class="function-name">typerig.proxy.application.app.pItems.outputGlyphNames</span></a> = outputGlyphNames<span class="argspec">(self, glyphNamesList, layerList<span class="parameter-default">=[]</span>, cursor_location<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.proxy.application.app.html#pItems">typerig.proxy.application.app.pItems</a> method</span></dt><dd>

<pre class="doc" markdown="0">Output text string using glyph names and layers specified</pre>

</dd></dl>



<a name="typerig.proxy.application.app.pWorkspace"></a>

## `pWorkspace`


<dt class="class"><h2><span class="class-name">typerig.proxy.application.app.pWorkspace</span> = <a name="typerig.proxy.application.app.pWorkspace" href="#typerig.proxy.application.app.pWorkspace">class pWorkspace</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flWorkspace object

Constructor:
        pWorkspace()

Attributes:
        .fl (flWorkspace): Current workspace
        .main (QWidget): Main QWidget's window</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pWorkspace-__init__" href="#pWorkspace-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-createFrame" href="#pWorkspace-createFrame"><span class="function-name">createFrame</span></a><span class="argspec">(self, string, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveGlyph" href="#pWorkspace-getActiveGlyph"><span class="function-name">getActiveGlyph</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveGlyphInfo" href="#pWorkspace-getActiveGlyphInfo"><span class="function-name">getActiveGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveIndex" href="#pWorkspace-getActiveIndex"><span class="function-name">getActiveIndex</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveKernPair" href="#pWorkspace-getActiveKernPair"><span class="function-name">getActiveKernPair</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getActiveLine" href="#pWorkspace-getActiveLine"><span class="function-name">getActiveLine</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getCanvas" href="#pWorkspace-getCanvas"><span class="function-name">getCanvas</span></a><span class="argspec">(self, atCursor<span class="parameter-default">=False</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getCanvasList" href="#pWorkspace-getCanvasList"><span class="function-name">getCanvasList</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getNextGlyphInfo" href="#pWorkspace-getNextGlyphInfo"><span class="function-name">getNextGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getPrevGlyphInfo" href="#pWorkspace-getPrevGlyphInfo"><span class="function-name">getPrevGlyphInfo</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getSelectedNodes" href="#pWorkspace-getSelectedNodes"><span class="function-name">getSelectedNodes</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getTextBlockGlyphs" href="#pWorkspace-getTextBlockGlyphs"><span class="function-name">getTextBlockGlyphs</span></a><span class="argspec">(self, tbi<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pWorkspace-getTextBlockList" href="#pWorkspace-getTextBlockList"><span class="function-name">getTextBlockList</span></a><span class="argspec">(self, atCursor<span class="parameter-default">=False</span>)</span></dt><dd>

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


<a name="typerig.proxy.application.app.pTextBlock"></a>

## `pTextBlock`


<dt class="class"><h2><span class="class-name">typerig.proxy.application.app.pTextBlock</span> = <a name="typerig.proxy.application.app.pTextBlock" href="#typerig.proxy.application.app.pTextBlock">class pTextBlock</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Proxy to flTextBlock object

Constructor:
        pTextBlock(flTextBlock)

Attributes:
        .fl (flTextBlock): flTextBlock Parent</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="pTextBlock-__init__" href="#pTextBlock-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, textBlock)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-__repr__" href="#pTextBlock-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-clone" href="#pTextBlock-clone"><span class="function-name">clone</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getFontSize" href="#pTextBlock-getFontSize"><span class="function-name">getFontSize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getFrameSize" href="#pTextBlock-getFrameSize"><span class="function-name">getFrameSize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getGlyphBounds" href="#pTextBlock-getGlyphBounds"><span class="function-name">getGlyphBounds</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getString" href="#pTextBlock-getString"><span class="function-name">getString</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getTransform" href="#pTextBlock-getTransform"><span class="function-name">getTransform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-getWrapState" href="#pTextBlock-getWrapState"><span class="function-name">getWrapState</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-height" href="#pTextBlock-height"><span class="function-name">height</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-reloc" href="#pTextBlock-reloc"><span class="function-name">reloc</span></a><span class="argspec">(self, x, y)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-resetTransform" href="#pTextBlock-resetTransform"><span class="function-name">resetTransform</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFontSize" href="#pTextBlock-setFontSize"><span class="function-name">setFontSize</span></a><span class="argspec">(self, fontSize)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFrameSize" href="#pTextBlock-setFrameSize"><span class="function-name">setFrameSize</span></a><span class="argspec">(self, width, height)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setFrameWidth" href="#pTextBlock-setFrameWidth"><span class="function-name">setFrameWidth</span></a><span class="argspec">(self, width)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setPageSize" href="#pTextBlock-setPageSize"><span class="function-name">setPageSize</span></a><span class="argspec">(self, sizeName, fixedHeight<span class="parameter-default">=(True, True)</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setTextWrap" href="#pTextBlock-setTextWrap"><span class="function-name">setTextWrap</span></a><span class="argspec">(self, width)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setTransform" href="#pTextBlock-setTransform"><span class="function-name">setTransform</span></a><span class="argspec">(self, newTransform)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-setWrapState" href="#pTextBlock-setWrapState"><span class="function-name">setWrapState</span></a><span class="argspec">(self, wrapText<span class="parameter-default">=True</span>)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-update" href="#pTextBlock-update"><span class="function-name">update</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-width" href="#pTextBlock-width"><span class="function-name">width</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-x" href="#pTextBlock-x"><span class="function-name">x</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="pTextBlock-y" href="#pTextBlock-y"><span class="function-name">y</span></a><span class="argspec">(self)</span></dt><dd>

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
