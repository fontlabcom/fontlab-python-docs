

<a name="FL.Image"></a>

# `Image`


<dt class="class"><h2><span class="class-name">FL.Image</span> = <a name="FL.Image" href="#FL.Image">class Image</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Image - class to represent bitmap image
===============================================

CONSTRUCTOR:
  Image() - generic constructor, creates a Image with zero coordinates
  Image(Image) - copy constructor
  Image(index1, index2) - creates a Image between nodes index1 and index2

ATTRIBUTES:
  width, height (integer) [read-only] - dimensions of the image
  empty (integer) [read-only] - empty status of the image
  size (integer) [read-only] - size of the image buffer
  data (string)  - image data as string with length
  traceenabled () [read-only] - there is a possibility to trace the image with the Trace command

OPERATIONS:
  Trace (Glyph) - Traces the image with the current option and adds it to the glyph

METHODS</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Image-Clear" href="#Image-Clear"><span class="function-name">Clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-Create" href="#Image-Create"><span class="function-name">Create</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-GetPixel" href="#Image-GetPixel"><span class="function-name">GetPixel</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-HLine" href="#Image-HLine"><span class="function-name">HLine</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-ImageBlt" href="#Image-ImageBlt"><span class="function-name">ImageBlt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-Invert" href="#Image-Invert"><span class="function-name">Invert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-SetPixel" href="#Image-SetPixel"><span class="function-name">SetPixel</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-Trace" href="#Image-Trace"><span class="function-name">Trace</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Image-__delattr__" href="#Image-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Image-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Image-__getattribute__" href="#Image-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Image-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Image-__init__" href="#Image-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Image-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Image-__repr__" href="#Image-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Image-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Image-__setattr__" href="#Image-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Image-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Image-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
