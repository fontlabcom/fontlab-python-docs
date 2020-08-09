

<a name="FL.Matrix"></a>

# `Matrix`


<dt class="class"><h2><span class="class-name">FL.Matrix</span> = <a name="FL.Matrix" href="#FL.Matrix">class Matrix</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Matrix - class to represent planar transformations
===============================================
Matrix is used to perform following transformations:
  x1 = x * a + y * b + e
  y1 = x * c + y * d + f

CONSTRUCTOR:
  Matrix() - generic constructor, creates a Matrix that makes no change to coordinates
  Matrix(Matrix) - copy constructor
  Matrix([a, b, c, d, e, f]) - creates a Matrix and assigns coordinates from the list of float numbers
  Matrix(a, b, c, d, e, f) - creates a Matrix and assigns coordinates from float numbers

ATTRIBUTES:
  a, b, c, d, e, f (float) - Matrix parameters

OPERATIONS:
  add - Matrix must be second operand, all parameters are added
  subtract - Matrix must be second operand, all parameters are subtracted
  multiply (with Matrix) - matrixes are multiplied
  multiply (with float number) - all parameters are scaled by the operand

METHODS
  Assign - assigns new values to a Matrix, uses the same syntax as in constructors
  Add(Matrix m) - adds values of the Matrix m to current matrix
  Sub(Matrix m) - subtracts values of the Matrix m from current matrix
  Mul(float s) - mutiplies Matrix's parameters to s value
  Transform(Matrix m) - applies Matrix m transformation to the current Matrix</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Matrix-Add" href="#Matrix-Add"><span class="function-name">Add</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Matrix-Add">Add</a>(Matrix m) - adds values of the Matrix m to current matrix</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-Assign" href="#Matrix-Assign"><span class="function-name">Assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Assign - assigns new values to a Matrix, uses the same syntax as in constructors</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-Mul" href="#Matrix-Mul"><span class="function-name">Mul</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Matrix-Mul">Mul</a>(float s) - mutiplies Matrix's parameters to s value</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-Sub" href="#Matrix-Sub"><span class="function-name">Sub</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Matrix-Sub">Sub</a>(Matrix m) - subtracts values of the Matrix m from current matrix</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-Transform" href="#Matrix-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#FL.Matrix-Transform">Transform</a>(Matrix m) - applies Matrix m transformation to the current Matrix</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__add__" href="#Matrix-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__delattr__" href="#Matrix-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getattribute__" href="#Matrix-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__init__" href="#Matrix-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__mul__" href="#Matrix-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__radd__" href="#Matrix-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__repr__" href="#Matrix-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rmul__" href="#Matrix-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rsub__" href="#Matrix-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__rsub__">__rsub__</a>(y) <==> y-x</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__setattr__" href="#Matrix-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__sub__" href="#Matrix-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Matrix-__sub__">__sub__</a>(y) <==> x-y</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>a</dt>
</dl>
<dl class="descriptor"><dt>b</dt>
</dl>
<dl class="descriptor"><dt>c</dt>
</dl>
<dl class="descriptor"><dt>d</dt>
</dl>
<dl class="descriptor"><dt>e</dt>
</dl>
<dl class="descriptor"><dt>f</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Matrix-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="FL.Matrix.Add"></a>

## `Add`


<dl class="function"><dt><a name="-FL.Matrix.Add" href="#-FL.Matrix.Add"><span class="function-name">FL.Matrix.Add</span></a> = Add<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Add(Matrix m) - adds values of the Matrix m to current matrix</pre>

</dd></dl>



<a name="FL.Matrix.Assign"></a>

## `Assign`


<dl class="function"><dt><a name="-FL.Matrix.Assign" href="#-FL.Matrix.Assign"><span class="function-name">FL.Matrix.Assign</span></a> = Assign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Assign - assigns new values to a Matrix, uses the same syntax as in constructors</pre>

</dd></dl>



<a name="FL.Matrix.Mul"></a>

## `Mul`


<dl class="function"><dt><a name="-FL.Matrix.Mul" href="#-FL.Matrix.Mul"><span class="function-name">FL.Matrix.Mul</span></a> = Mul<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Mul(float s) - mutiplies Matrix's parameters to s value</pre>

</dd></dl>



<a name="FL.Matrix.Sub"></a>

## `Sub`


<dl class="function"><dt><a name="-FL.Matrix.Sub" href="#-FL.Matrix.Sub"><span class="function-name">FL.Matrix.Sub</span></a> = Sub<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Sub(Matrix m) - subtracts values of the Matrix m from current matrix</pre>

</dd></dl>



<a name="FL.Matrix.Transform"></a>

## `Transform`


<dl class="function"><dt><a name="-FL.Matrix.Transform" href="#-FL.Matrix.Transform"><span class="function-name">FL.Matrix.Transform</span></a> = Transform<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">Transform(Matrix m) - applies Matrix m transformation to the current Matrix</pre>

</dd></dl>

