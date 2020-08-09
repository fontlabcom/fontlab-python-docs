

<a name="typerig.core.func.collection"></a>

# `typerig.core.func.collection`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.func.html">func</a>.collection (<span class="info">version 0.26.1)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Collection (Functions)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-combineReccuringItems" href="#-combineReccuringItems"><span class="function-name">combineReccuringItems</span></a><span class="argspec">(listItems)</span></dt><dd>

<pre class="doc" markdown="0">Combines recurring items in [listItems] and returns a list containing sets of grouped items</pre>

</dd></dl>

<dl class="function"><dt><a name="-enumerateWithStart" href="#-enumerateWithStart"><span class="function-name">enumerateWithStart</span></a><span class="argspec">(sequence, start<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Performs [enumerate] of a [sequence] with added [start] functionality (available in Python 2.6)</pre>

</dd></dl>

<dl class="function"><dt><a name="-groupConsecutives" href="#-groupConsecutives"><span class="function-name">groupConsecutives</span></a><span class="argspec">(listItems, step<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Build a list of lists containig consecutive numbers from [listItems] (number list) within [step]</pre>

</dd></dl>

<dl class="function"><dt><a name="-mergeDicts" href="#-mergeDicts"><span class="function-name">mergeDicts</span></a><span class="argspec">(d1, d2, merge<span class="parameter-default">=&lt;function &lt;lambda&gt;&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0">Merges two dictionaries [d1, d2], combining values on duplicate keys as defined by the optional [merge] function.
--------
Example: merge(d1, d2, lambda x,y: x+y) -> {'a': 2, 'c': 6, 'b': 4}</pre>

</dd></dl>

<dl class="function"><dt><a name="-unpack" href="#-unpack"><span class="function-name">unpack</span></a><span class="argspec">(listItems)</span></dt><dd>

<pre class="doc" markdown="0">Unpacks all items form [listItems] containing other lists, sets and etc.</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.func.collection.mergeDicts"></a>

## `mergeDicts`


<dl class="function"><dt><a name="-typerig.core.func.collection.mergeDicts" href="#-typerig.core.func.collection.mergeDicts"><span class="function-name">typerig.core.func.collection.mergeDicts</span></a> = mergeDicts<span class="argspec">(d1, d2, merge<span class="parameter-default">=&lt;function &lt;lambda&gt;&gt;</span>)</span></dt><dd>

<pre class="doc" markdown="0">Merges two dictionaries [d1, d2], combining values on duplicate keys as defined by the optional [merge] function.
--------
Example: merge(d1, d2, lambda x,y: x+y) -> {'a': 2, 'c': 6, 'b': 4}</pre>

</dd></dl>



<a name="typerig.core.func.collection.unpack"></a>

## `unpack`


<dl class="function"><dt><a name="-typerig.core.func.collection.unpack" href="#-typerig.core.func.collection.unpack"><span class="function-name">typerig.core.func.collection.unpack</span></a> = unpack<span class="argspec">(listItems)</span></dt><dd>

<pre class="doc" markdown="0">Unpacks all items form [listItems] containing other lists, sets and etc.</pre>

</dd></dl>



<a name="typerig.core.func.collection.enumerateWithStart"></a>

## `enumerateWithStart`


<dl class="function"><dt><a name="-typerig.core.func.collection.enumerateWithStart" href="#-typerig.core.func.collection.enumerateWithStart"><span class="function-name">typerig.core.func.collection.enumerateWithStart</span></a> = enumerateWithStart<span class="argspec">(sequence, start<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Performs [enumerate] of a [sequence] with added [start] functionality (available in Python 2.6)</pre>

</dd></dl>



<a name="typerig.core.func.collection.combineReccuringItems"></a>

## `combineReccuringItems`


<dl class="function"><dt><a name="-typerig.core.func.collection.combineReccuringItems" href="#-typerig.core.func.collection.combineReccuringItems"><span class="function-name">typerig.core.func.collection.combineReccuringItems</span></a> = combineReccuringItems<span class="argspec">(listItems)</span></dt><dd>

<pre class="doc" markdown="0">Combines recurring items in [listItems] and returns a list containing sets of grouped items</pre>

</dd></dl>



<a name="typerig.core.func.collection.groupConsecutives"></a>

## `groupConsecutives`


<dl class="function"><dt><a name="-typerig.core.func.collection.groupConsecutives" href="#-typerig.core.func.collection.groupConsecutives"><span class="function-name">typerig.core.func.collection.groupConsecutives</span></a> = groupConsecutives<span class="argspec">(listItems, step<span class="parameter-default">=1</span>)</span></dt><dd>

<pre class="doc" markdown="0">Build a list of lists containig consecutive numbers from [listItems] (number list) within [step]</pre>

</dd></dl>

