

<a name="FL.Point"></a>

# `Point`


<dt class="class"><h2><span class="class-name">FL.Point</span> = <a name="FL.Point" href="#FL.Point">class Point</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Point - base class to represent point
===============================================
Integer or float values are accepted as coordinates

CONSTRUCTOR:
  Point() - generic constructor, creates a Point with zero coordinates
  Point(Point) - copy constructor
  Point(x, y) - creates a Point and assigns coordinates. x and y may be integer or float

ATTRIBUTES:
  parent (read-only) - Point's parent object
  x (integer or float) - horizontal position of the point
  y (integer or float) - vertical position of the point

OPERATIONS:
  == - compares two points, both coordinates must be equal
  add - Point must be second operand, both coordinates are added
  subtract - Point must be second operand, both coordinates are added
  multiply - second operand may be Point, float or Matrix. If second operand is Point, then result of scalar product is returned

METHODS
  Assign(Point p) | (x, y) - assigns new values to a Point
  Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values
  Add(Point p) - same as Shift(Point p)
  Sub(Point p) - subtracts p coordinates from the current Point
  Mul(float s) - mutiplies Point's position to s value
  Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Point-Add" href="#Point-Add"><span class="function-name">Add</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Add">Add</a>(Point p) - same as <a href="#FL.Point-Shift">Shift</a>(Point p)</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-Assign" href="#Point-Assign"><span class="function-name">Assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Assign">Assign</a>(Point p) | (x, y) - assigns new values to a Point</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-Mul" href="#Point-Mul"><span class="function-name">Mul</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Mul">Mul</a>(float s) - mutiplies Point's position to s value</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-Shift" href="#Point-Shift"><span class="function-name">Shift</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Shift">Shift</a>(Point p) | (x, y) - shifts Point on a position defined by p or x and y values</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-Sub" href="#Point-Sub"><span class="function-name">Sub</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Sub">Sub</a>(Point p) - subtracts p coordinates from the current Point</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-Transform" href="#Point-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Point-Transform">Transform</a>(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__add__" href="#Point-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__cmp__" href="#Point-__cmp__"><span class="function-name">__cmp__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__cmp__">__cmp__</a>(y) <==> cmp(x,y)</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__delattr__" href="#Point-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__getattribute__" href="#Point-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__init__" href="#Point-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__mul__" href="#Point-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__radd__" href="#Point-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__repr__" href="#Point-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__rmul__" href="#Point-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__rsub__" href="#Point-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__setattr__" href="#Point-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Point-__sub__" href="#Point-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Point-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Point-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="FL.Point.Add"></a>

## `Add`


<dl class="function"><dt><a name="-FL.Point.Add" href="#-FL.Point.Add"><span class="function-name">FL.Point.Add</span></a> = Add<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Add(Point p) - same as Shift(Point p)</pre>

</dd></dl>



<a name="FL.Point.Assign"></a>

## `Assign`


<dl class="function"><dt><a name="-FL.Point.Assign" href="#-FL.Point.Assign"><span class="function-name">FL.Point.Assign</span></a> = Assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Assign(Point p) | (x, y) - assigns new values to a Point</pre>

</dd></dl>



<a name="FL.Point.Mul"></a>

## `Mul`


<dl class="function"><dt><a name="-FL.Point.Mul" href="#-FL.Point.Mul"><span class="function-name">FL.Point.Mul</span></a> = Mul<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Mul(float s) - mutiplies Point's position to s value</pre>

</dd></dl>



<a name="FL.Point.Shift"></a>

## `Shift`


<dl class="function"><dt><a name="-FL.Point.Shift" href="#-FL.Point.Shift"><span class="function-name">FL.Point.Shift</span></a> = Shift<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Shift(Point p) | (x, y) - shifts Point on a position defined by p or x and y values</pre>

</dd></dl>



<a name="FL.Point.Sub"></a>

## `Sub`


<dl class="function"><dt><a name="-FL.Point.Sub" href="#-FL.Point.Sub"><span class="function-name">FL.Point.Sub</span></a> = Sub<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Sub(Point p) - subtracts p coordinates from the current Point</pre>

</dd></dl>



<a name="FL.Point.Transform"></a>

## `Transform`


<dl class="function"><dt><a name="-FL.Point.Transform" href="#-FL.Point.Transform"><span class="function-name">FL.Point.Transform</span></a> = Transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Transform(Matrix m) - applies Matrix transformation to the Point (see Matrix().__doc__)</pre>

</dd></dl>

