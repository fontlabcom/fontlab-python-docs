

<a name="typerig.core.fileio.flc"></a>

# `typerig.core.fileio.flc`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.fileio.html">fileio</a>.flc (<span class="info">version 0.2.4)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: Typerig / IO / Fontlab class parser (.flc)
# ------------------------------------------------------
# (C) Vassil Kateliev, 2017     (http://www.kateliev.com)
# (C) Karandash Type Foundry    (http://www.karandash.eu)
#--------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#object">__builtin__.object</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.fileio.flc.html#fontClassesFromFile">fontClassesFromFile</a></span></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="fontClassesFromFile" href="#fontClassesFromFile">class <span class="class-name">fontClassesFromFile</span></a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Loads a Fontlab class file (.flc) and parses it. 
Args:
        fileName (str) : a path to Fontlab class file
Returns:
        Object with methods:
                .fontClasses (dict -> class_name:class_contents)
                .metricClasses (dict -> class_name:class_contents)
                .kernClasses (dict -> class_name:class_contents)
                .otClasses (dict -> class_name:class_contents)
                .classPosition (Left and/or Right pair(s)); Metric (Left, Width, Right)
                .classLeader (dict -> class_name:class_leader)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fontClassesFromFile-__init__" href="#fontClassesFromFile-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, fileName)</span></dt><dd>

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


<a name="typerig.core.fileio.flc.fontClassesFromFile"></a>

## `fontClassesFromFile`


<dt class="class"><h2><span class="class-name">typerig.core.fileio.flc.fontClassesFromFile</span> = <a name="typerig.core.fileio.flc.fontClassesFromFile" href="#typerig.core.fileio.flc.fontClassesFromFile">class fontClassesFromFile</a>(<a href="./__builtin__.html#object">__builtin__.object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Loads a Fontlab class file (.flc) and parses it. 
Args:
        fileName (str) : a path to Fontlab class file
Returns:
        Object with methods:
                .fontClasses (dict -> class_name:class_contents)
                .metricClasses (dict -> class_name:class_contents)
                .kernClasses (dict -> class_name:class_contents)
                .otClasses (dict -> class_name:class_contents)
                .classPosition (Left and/or Right pair(s)); Metric (Left, Width, Right)
                .classLeader (dict -> class_name:class_leader)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="fontClassesFromFile-__init__" href="#fontClassesFromFile-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, fileName)</span></dt><dd>

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
