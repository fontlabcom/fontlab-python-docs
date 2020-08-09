

<a name="typerig.core.func.string"></a>

# `typerig.core.func.string`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.func.html">func</a>.string (<span class="info">version 0.26.2)</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / String (Functions)
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2015-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-getLowercaseCodepoint" href="#-getLowercaseCodepoint"><span class="function-name">getLowercaseCodepoint</span></a><span class="argspec">(unicodeName)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode Name (String) returns coresponding Lowercase Unicode Name! Names are in Adobe uniXXXX format</pre>

</dd></dl>

<dl class="function"><dt><a name="-getLowercaseInt" href="#-getLowercaseInt"><span class="function-name">getLowercaseInt</span></a><span class="argspec">(uniocdeInt)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode (Integer) returns coresponding Lowercase Unicode (Integer)</pre>

</dd></dl>

<dl class="function"><dt><a name="-getUppercaseCodepoint" href="#-getUppercaseCodepoint"><span class="function-name">getUppercaseCodepoint</span></a><span class="argspec">(unicodeName)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode Name (String) returns coresponding Uppercase Unicode Name! Names are in Adobe uniXXXX format</pre>

</dd></dl>

<dl class="function"><dt><a name="-getUppercaseInt" href="#-getUppercaseInt"><span class="function-name">getUppercaseInt</span></a><span class="argspec">(uniocdeInt)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Lowercase Uniocde (Integer) returns coresponding Uppercase Unicode (Integer)</pre>

</dd></dl>

<dl class="function"><dt><a name="-kpxGen" href="#-kpxGen"><span class="function-name">kpxGen</span></a><span class="argspec">(inputA, inputB, suffix<span class="parameter-default">=('', '')</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate AMF style KPX paris for kerning</pre>

</dd></dl>

<dl class="function"><dt><a name="-lst2str" href="#-lst2str"><span class="function-name">lst2str</span></a><span class="argspec">(listItems, separator)</span></dt><dd>

<pre class="doc" markdown="0">Converts [listItems] to 'String' using 'String separator'
Example: <a href="#-lst2str">lst2str</a>([List], ',')</pre>

</dd></dl>

<dl class="function"><dt><a name="-lstcln" href="#-lstcln"><span class="function-name">lstcln</span></a><span class="argspec">(listItems, discard)</span></dt><dd>

<pre class="doc" markdown="0">Cleans a [listItems] by removing [discard]
Example: <a href="#-lstcln">lstcln</a>([List], '/space')</pre>

</dd></dl>

<dl class="function"><dt><a name="-str2lst" href="#-str2lst"><span class="function-name">str2lst</span></a><span class="argspec">(stringItems, separator)</span></dt><dd>

<pre class="doc" markdown="0">Converts 'stringItems' to [List] using 'String separator'
Example: <a href="#-str2lst">str2lst</a>(String, ',')</pre>

</dd></dl>

<dl class="function"><dt><a name="-strNormSpace" href="#-strNormSpace"><span class="function-name">strNormSpace</span></a><span class="argspec">(string)</span></dt><dd>

<pre class="doc" markdown="0">Removes all mutiple /space characters from [string]</pre>

</dd></dl>

<dl class="function"><dt><a name="-strRepDict" href="#-strRepDict"><span class="function-name">strRepDict</span></a><span class="argspec">(stringItems, replacementDicionary, method<span class="parameter-default">='replace'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Replaces every instance of [stringItems] according to [replacementDicionary] using 'replace' ('r') or 'consecutive' replacement ('c') [method]s
Example: <a href="#-strRepDict">strRepDict</a>('12', {'1':'/one', '2':'/two'}, 'r')</pre>

</dd></dl>

<dl class="function"><dt><a name="-stringGen" href="#-stringGen"><span class="function-name">stringGen</span></a><span class="argspec">(inputA, inputB, filler<span class="parameter-default">=('HH', 'HH')</span>, genPattern<span class="parameter-default">='FL A B A FR'</span>, suffix<span class="parameter-default">=('', '')</span>, sep<span class="parameter-default">='/'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate test text string for metrics, kerning and pairs/phrases
Args:
        inputA, inputB (list/string) : Input lists to be paired
        filler (tuple(str)) : Filler string 
        genPattern (string): A SPACE separated ordering pattern, where FL, FR is Filler Left/Right and A, B are input strings
        suffix (tuple(str)) : Suffixes to be added to inputs A and B
        sep (str) : Glyph Separator to be used. '/' default for Fontlab

Returns:
        list(str)</pre>

</dd></dl>

<dl class="function"><dt><a name="-stringGenPairs" href="#-stringGenPairs"><span class="function-name">stringGenPairs</span></a><span class="argspec">(pairs_input, filler<span class="parameter-default">=('HH', 'HH')</span>, genPattern<span class="parameter-default">='FL A B A FR'</span>, suffix<span class="parameter-default">=('', '')</span>, sep<span class="parameter-default">='/'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate test text string for metrics, kerning and pairs/phrases
Args:
        pairs_input (list(tuple)): Input list contaiing pairs
        filler (tuple(str)) : Filler string 
        genPattern (string): A SPACE separated ordering pattern, where FL, FR is Filler Left/Right and A, B are input strings
        suffix (tuple(str)) : Suffixes to be added to inputs A and B
        sep (str) : Glyph Separator to be used. '/' default for Fontlab

Returns:
        list(str)</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.func.string.getLowercaseInt"></a>

## `getLowercaseInt`


<dl class="function"><dt><a name="-typerig.core.func.string.getLowercaseInt" href="#-typerig.core.func.string.getLowercaseInt"><span class="function-name">typerig.core.func.string.getLowercaseInt</span></a> = getLowercaseInt<span class="argspec">(uniocdeInt)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode (Integer) returns coresponding Lowercase Unicode (Integer)</pre>

</dd></dl>



<a name="typerig.core.func.string.getUppercaseInt"></a>

## `getUppercaseInt`


<dl class="function"><dt><a name="-typerig.core.func.string.getUppercaseInt" href="#-typerig.core.func.string.getUppercaseInt"><span class="function-name">typerig.core.func.string.getUppercaseInt</span></a> = getUppercaseInt<span class="argspec">(uniocdeInt)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Lowercase Uniocde (Integer) returns coresponding Uppercase Unicode (Integer)</pre>

</dd></dl>



<a name="typerig.core.func.string.getLowercaseCodepoint"></a>

## `getLowercaseCodepoint`


<dl class="function"><dt><a name="-typerig.core.func.string.getLowercaseCodepoint" href="#-typerig.core.func.string.getLowercaseCodepoint"><span class="function-name">typerig.core.func.string.getLowercaseCodepoint</span></a> = getLowercaseCodepoint<span class="argspec">(unicodeName)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode Name (String) returns coresponding Lowercase Unicode Name! Names are in Adobe uniXXXX format</pre>

</dd></dl>



<a name="typerig.core.func.string.getUppercaseCodepoint"></a>

## `getUppercaseCodepoint`


<dl class="function"><dt><a name="-typerig.core.func.string.getUppercaseCodepoint" href="#-typerig.core.func.string.getUppercaseCodepoint"><span class="function-name">typerig.core.func.string.getUppercaseCodepoint</span></a> = getUppercaseCodepoint<span class="argspec">(unicodeName)</span></dt><dd>

<pre class="doc" markdown="0">Based on given Uppercase Unicode Name (String) returns coresponding Uppercase Unicode Name! Names are in Adobe uniXXXX format</pre>

</dd></dl>



<a name="typerig.core.func.string.kpxGen"></a>

## `kpxGen`


<dl class="function"><dt><a name="-typerig.core.func.string.kpxGen" href="#-typerig.core.func.string.kpxGen"><span class="function-name">typerig.core.func.string.kpxGen</span></a> = kpxGen<span class="argspec">(inputA, inputB, suffix<span class="parameter-default">=('', '')</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate AMF style KPX paris for kerning</pre>

</dd></dl>



<a name="typerig.core.func.string.stringGen"></a>

## `stringGen`


<dl class="function"><dt><a name="-typerig.core.func.string.stringGen" href="#-typerig.core.func.string.stringGen"><span class="function-name">typerig.core.func.string.stringGen</span></a> = stringGen<span class="argspec">(inputA, inputB, filler<span class="parameter-default">=('HH', 'HH')</span>, genPattern<span class="parameter-default">='FL A B A FR'</span>, suffix<span class="parameter-default">=('', '')</span>, sep<span class="parameter-default">='/'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate test text string for metrics, kerning and pairs/phrases
Args:
        inputA, inputB (list/string) : Input lists to be paired
        filler (tuple(str)) : Filler string 
        genPattern (string): A SPACE separated ordering pattern, where FL, FR is Filler Left/Right and A, B are input strings
        suffix (tuple(str)) : Suffixes to be added to inputs A and B
        sep (str) : Glyph Separator to be used. '/' default for Fontlab

Returns:
        list(str)</pre>

</dd></dl>



<a name="typerig.core.func.string.stringGenPairs"></a>

## `stringGenPairs`


<dl class="function"><dt><a name="-typerig.core.func.string.stringGenPairs" href="#-typerig.core.func.string.stringGenPairs"><span class="function-name">typerig.core.func.string.stringGenPairs</span></a> = stringGenPairs<span class="argspec">(pairs_input, filler<span class="parameter-default">=('HH', 'HH')</span>, genPattern<span class="parameter-default">='FL A B A FR'</span>, suffix<span class="parameter-default">=('', '')</span>, sep<span class="parameter-default">='/'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Generate test text string for metrics, kerning and pairs/phrases
Args:
        pairs_input (list(tuple)): Input list contaiing pairs
        filler (tuple(str)) : Filler string 
        genPattern (string): A SPACE separated ordering pattern, where FL, FR is Filler Left/Right and A, B are input strings
        suffix (tuple(str)) : Suffixes to be added to inputs A and B
        sep (str) : Glyph Separator to be used. '/' default for Fontlab

Returns:
        list(str)</pre>

</dd></dl>



<a name="typerig.core.func.string.strNormSpace"></a>

## `strNormSpace`


<dl class="function"><dt><a name="-typerig.core.func.string.strNormSpace" href="#-typerig.core.func.string.strNormSpace"><span class="function-name">typerig.core.func.string.strNormSpace</span></a> = strNormSpace<span class="argspec">(string)</span></dt><dd>

<pre class="doc" markdown="0">Removes all mutiple /space characters from [string]</pre>

</dd></dl>



<a name="typerig.core.func.string.lst2str"></a>

## `lst2str`


<dl class="function"><dt><a name="-typerig.core.func.string.lst2str" href="#-typerig.core.func.string.lst2str"><span class="function-name">typerig.core.func.string.lst2str</span></a> = lst2str<span class="argspec">(listItems, separator)</span></dt><dd>

<pre class="doc" markdown="0">Converts [listItems] to 'String' using 'String separator'
Example: lst2str([List], ',')</pre>

</dd></dl>



<a name="typerig.core.func.string.str2lst"></a>

## `str2lst`


<dl class="function"><dt><a name="-typerig.core.func.string.str2lst" href="#-typerig.core.func.string.str2lst"><span class="function-name">typerig.core.func.string.str2lst</span></a> = str2lst<span class="argspec">(stringItems, separator)</span></dt><dd>

<pre class="doc" markdown="0">Converts 'stringItems' to [List] using 'String separator'
Example: str2lst(String, ',')</pre>

</dd></dl>



<a name="typerig.core.func.string.lstcln"></a>

## `lstcln`


<dl class="function"><dt><a name="-typerig.core.func.string.lstcln" href="#-typerig.core.func.string.lstcln"><span class="function-name">typerig.core.func.string.lstcln</span></a> = lstcln<span class="argspec">(listItems, discard)</span></dt><dd>

<pre class="doc" markdown="0">Cleans a [listItems] by removing [discard]
Example: lstcln([List], '/space')</pre>

</dd></dl>



<a name="typerig.core.func.string.strRepDict"></a>

## `strRepDict`


<dl class="function"><dt><a name="-typerig.core.func.string.strRepDict" href="#-typerig.core.func.string.strRepDict"><span class="function-name">typerig.core.func.string.strRepDict</span></a> = strRepDict<span class="argspec">(stringItems, replacementDicionary, method<span class="parameter-default">='replace'</span>)</span></dt><dd>

<pre class="doc" markdown="0">Replaces every instance of [stringItems] according to [replacementDicionary] using 'replace' ('r') or 'consecutive' replacement ('c') [method]s
Example: strRepDict('12', {'1':'/one', '2':'/two'}, 'r')</pre>

</dd></dl>

