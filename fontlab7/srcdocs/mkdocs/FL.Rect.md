

<a name="FL.Rect"></a>

# `Rect`


<dt class="class"><h2><span class="class-name">FL.Rect</span> = <a name="FL.Rect" href="#FL.Rect">class Rect</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Rect - base class to represent rectangle
===============================================
Integer or float values are accepted as coordinates

CONSTRUCTOR:
  Rect() - generic constructor, creates a Rect with zero coordinates
  Rect(Rect r) - copy constructor
  Rect(Point p) - creates rectangle with one corner at (0, 0) and another - at coordinates defined by p
  Rect(Point p0, Point p1) - creates rectangle defined by the corner points
  Rect(x0, y0, x1, y1) - creates a rectangle defined by the coordinates of the corner points

ATTRIBUTES:
  ll (Point) - position of the left/bottom corner
  ur (Point) - position of the right/top corner
  x (integer or float) - horizontal position of the left corner
  y (integer or float) - vertical position of the bottom corner
  width (integer or float) - width of the rectangle
  height (integer or float) - height of the rectangle

OPERATIONS:
  add - Point or Rect must be second operand, rectangle is expanded to include this point or rectange
  multiply - second operand must be Matrix. Matrix transformation is applied to the rectangle

METHODS
  Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor
  Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values
  Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)
  Resize(width, height) - resizes rectangle to new width and height
  Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point
  Check(Rect r) - returns True if r overlaps current rectangle
  Check(Point p) - returns True if p is insude current rectangle
  Validate() - corrents rectangle's orientation</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Rect-Assign" href="#Rect-Assign"><span class="function-name">Assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Assign">Assign</a>(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Check" href="#Rect-Check"><span class="function-name">Check</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Check">Check</a>(Rect r) - returns True if r overlaps current rectangle
<a href="#FL.Rect-Check">Check</a>(Point p) - returns True if p is insude current rectangle</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Include" href="#Rect-Include"><span class="function-name">Include</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Include">Include</a>(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Resize" href="#Rect-Resize"><span class="function-name">Resize</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Resize">Resize</a>(width, height) - resizes rectangle to new width and height</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Shift" href="#Rect-Shift"><span class="function-name">Shift</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Shift">Shift</a>(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Transform" href="#Rect-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Transform">Transform</a>(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-Validate" href="#Rect-Validate"><span class="function-name">Validate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Rect-Validate">Validate</a>() - corrents rectangle's orientation</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__add__" href="#Rect-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__delattr__" href="#Rect-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__getattribute__" href="#Rect-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__init__" href="#Rect-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__mul__" href="#Rect-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__radd__" href="#Rect-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__repr__" href="#Rect-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__rmul__" href="#Rect-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="Rect-__setattr__" href="#Rect-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Rect-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>height</dt>
</dl>
<dl class="descriptor"><dt>ll</dt>
</dl>
<dl class="descriptor"><dt>ur</dt>
</dl>
<dl class="descriptor"><dt>width</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Rect-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="FL.Rect.Assign"></a>

## `Assign`


<dl class="function"><dt><a name="-FL.Rect.Assign" href="#-FL.Rect.Assign"><span class="function-name">FL.Rect.Assign</span></a> = Assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Assign(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - assigns new values to a Rect, the same as constructor</pre>

</dd></dl>



<a name="FL.Rect.Check"></a>

## `Check`


<dl class="function"><dt><a name="-FL.Rect.Check" href="#-FL.Rect.Check"><span class="function-name">FL.Rect.Check</span></a> = Check<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Check(Rect r) - returns True if r overlaps current rectangle
Check(Point p) - returns True if p is insude current rectangle</pre>

</dd></dl>



<a name="FL.Rect.Include"></a>

## `Include`


<dl class="function"><dt><a name="-FL.Rect.Include" href="#-FL.Rect.Include"><span class="function-name">FL.Rect.Include</span></a> = Include<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Include(Rect r) | (Point p) | (x, y)  - expands rectangle to include new rectangle or point</pre>

</dd></dl>



<a name="FL.Rect.Resize"></a>

## `Resize`


<dl class="function"><dt><a name="-FL.Rect.Resize" href="#-FL.Rect.Resize"><span class="function-name">FL.Rect.Resize</span></a> = Resize<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Resize(width, height) - resizes rectangle to new width and height</pre>

</dd></dl>



<a name="FL.Rect.Shift"></a>

## `Shift`


<dl class="function"><dt><a name="-FL.Rect.Shift" href="#-FL.Rect.Shift"><span class="function-name">FL.Rect.Shift</span></a> = Shift<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Shift(Point p) | (x, y) - shifts Rect on a position defined by p or x and y values</pre>

</dd></dl>



<a name="FL.Rect.Transform"></a>

## `Transform`


<dl class="function"><dt><a name="-FL.Rect.Transform" href="#-FL.Rect.Transform"><span class="function-name">FL.Rect.Transform</span></a> = Transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Transform(Matrix m) - applies Matrix transformation to the Rect (see Matrix().__doc__)</pre>

</dd></dl>



<a name="FL.Rect.Validate"></a>

## `Validate`


<dl class="function"><dt><a name="-FL.Rect.Validate" href="#-FL.Rect.Validate"><span class="function-name">FL.Rect.Validate</span></a> = Validate<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Validate() - corrents rectangle's orientation</pre>

</dd></dl>

