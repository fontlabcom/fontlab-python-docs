

<a name="fontlab.Interval"></a>

# `Interval`


<dt class="class"><h2><span class="class-name">fontlab.Interval</span> = <a name="fontlab.Interval" href="#fontlab.Interval">class Interval</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Interval representation

Constructors:</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Interval-__delattr__" href="#Interval-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__eq__" href="#Interval-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__eq__">__eq__</a>(y) <==> x==y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__ge__" href="#Interval-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__getattribute__" href="#Interval-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__gt__" href="#Interval-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__init__" href="#Interval-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__le__" href="#Interval-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__lt__" href="#Interval-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__ne__" href="#Interval-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__repr__" href="#Interval-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-__setattr__" href="#Interval-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Interval-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-isEmpty" href="#Interval-isEmpty"><span class="function-name">isEmpty</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool <a href="#fontlab.Interval-isEmpty">isEmpty</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-middle" href="#Interval-middle"><span class="function-name">middle</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.Interval-middle">middle</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-reversed" href="#Interval-reversed"><span class="function-name">reversed</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Interval <a href="#fontlab.Interval-reversed">reversed</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-setT0T1" href="#Interval-setT0T1"><span class="function-name">setT0T1</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void <a href="#fontlab.Interval-setT0T1">setT0T1</a>(double t0, double t1)</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-toAbsolute" href="#Interval-toAbsolute"><span class="function-name">toAbsolute</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.Interval-toAbsolute">toAbsolute</a>(double v)</pre>

</dd></dl>
<dl class="function"><dt><a name="Interval-toInterval" href="#Interval-toInterval"><span class="function-name">toInterval</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double <a href="#fontlab.Interval-toInterval">toInterval</a>(double absv)</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>d</dt>
<dd>

<pre class="doc" markdown="0">double d</pre>

</dd>
</dl>
<dl class="descriptor"><dt>key</dt>
<dd>

<pre class="doc" markdown="0">uint key</pre>

</dd>
</dl>
<dl class="descriptor"><dt>t0</dt>
<dd>

<pre class="doc" markdown="0">double t0</pre>

</dd>
</dl>
<dl class="descriptor"><dt>t1</dt>
<dd>

<pre class="doc" markdown="0">double t1</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.Interval-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.Interval.d"></a>

## `d`


<dl class="descriptor"><dt>fontlab.Interval.d</dt>
<dd>

<pre class="doc" markdown="0">double d</pre>

</dd>
</dl>



<a name="fontlab.Interval.isEmpty"></a>

## `isEmpty`


<dl class="function"><dt><a name="-fontlab.Interval.isEmpty" href="#-fontlab.Interval.isEmpty"><span class="function-name">fontlab.Interval.isEmpty</span></a> = isEmpty<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">bool isEmpty()</pre>

</dd></dl>



<a name="fontlab.Interval.key"></a>

## `key`


<dl class="descriptor"><dt>fontlab.Interval.key</dt>
<dd>

<pre class="doc" markdown="0">uint key</pre>

</dd>
</dl>



<a name="fontlab.Interval.middle"></a>

## `middle`


<dl class="function"><dt><a name="-fontlab.Interval.middle" href="#-fontlab.Interval.middle"><span class="function-name">fontlab.Interval.middle</span></a> = middle<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double middle()</pre>

</dd></dl>



<a name="fontlab.Interval.reversed"></a>

## `reversed`


<dl class="function"><dt><a name="-fontlab.Interval.reversed" href="#-fontlab.Interval.reversed"><span class="function-name">fontlab.Interval.reversed</span></a> = reversed<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Interval reversed()</pre>

</dd></dl>



<a name="fontlab.Interval.setT0T1"></a>

## `setT0T1`


<dl class="function"><dt><a name="-fontlab.Interval.setT0T1" href="#-fontlab.Interval.setT0T1"><span class="function-name">fontlab.Interval.setT0T1</span></a> = setT0T1<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">void setT0T1(double t0, double t1)</pre>

</dd></dl>



<a name="fontlab.Interval.t0"></a>

## `t0`


<dl class="descriptor"><dt>fontlab.Interval.t0</dt>
<dd>

<pre class="doc" markdown="0">double t0</pre>

</dd>
</dl>



<a name="fontlab.Interval.t1"></a>

## `t1`


<dl class="descriptor"><dt>fontlab.Interval.t1</dt>
<dd>

<pre class="doc" markdown="0">double t1</pre>

</dd>
</dl>



<a name="fontlab.Interval.toAbsolute"></a>

## `toAbsolute`


<dl class="function"><dt><a name="-fontlab.Interval.toAbsolute" href="#-fontlab.Interval.toAbsolute"><span class="function-name">fontlab.Interval.toAbsolute</span></a> = toAbsolute<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double toAbsolute(double v)</pre>

</dd></dl>



<a name="fontlab.Interval.toInterval"></a>

## `toInterval`


<dl class="function"><dt><a name="-fontlab.Interval.toInterval" href="#-fontlab.Interval.toInterval"><span class="function-name">fontlab.Interval.toInterval</span></a> = toInterval<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">double toInterval(double absv)</pre>

</dd></dl>

