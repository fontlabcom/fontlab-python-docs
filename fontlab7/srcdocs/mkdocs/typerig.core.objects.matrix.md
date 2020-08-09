

<a name="typerig.core.objects.matrix"></a>

# `typerig.core.objects.matrix`


<h2><a href="./typerig.html">typerig</a>.<a href="./typerig.core.html">core</a>.<a href="./typerig.core.objects.html">objects</a>.matrix</h2> <div class="module">  <div class="docstring">

<pre class="doc" markdown="0"># MODULE: TypeRig / Core / Matrix (Object)
# ----------------------------------------------------------
# A slight adaptation of...
# "Basic Table, Matrix and Vector functions for Python 2+"
# (C) Raymond Hettinger, 2002
# -----------------------------------------------------------
# (C) Vassil Kateliev, 2017-2020        (http://www.kateliev.com)
# (C) Karandash Type Foundry            (http://www.karandash.eu)
#------------------------------------------------------------
# www.typerig.com</pre>

</div>  <div class="modules"><h3>Modules</h3><ul class="list"><li>math</li><li>operator</li><li>random</li></ul></div>  <div class="classes"><h3>Classes</h3><ul class="tree"><li><span class="class-name"><a href="./__builtin__.html#list">__builtin__.list</a></span>(<span class="bases">__builtin__.object</span>)</li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#Table">Table</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#Square">Square</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></span></li><li><ul class="tree"><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#LowerTri">LowerTri</a></span></li><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#UpperTri">UpperTri</a></span></li></ul></li></ul></li></ul></li><li><span class="class-name"><a href="./typerig.core.objects.matrix.html#Vec">Vec</a></span></li></ul></li></ul></li></ul><dl class="classes"><dt class="class"><h2><a name="LowerTri" href="#LowerTri">class <span class="class-name">LowerTri</span></a>(<a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#LowerTri">LowerTri</a></dd><dd><a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></dd><dd><a href="./typerig.core.objects.matrix.html#Square">Square</a></dd><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></h4><dl class="function"><dt><a name="LowerTri-det" href="#LowerTri-det"><span class="function-name">det</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-eigs" href="#LowerTri-eigs"><span class="function-name">eigs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Square">Square</a></h4><dl class="function"><dt><a name="LowerTri-__pow__" href="#LowerTri-__pow__"><span class="function-name">__pow__</span></a><span class="argspec">(self, exp)</span></dt><dd>

<pre class="doc" markdown="0">Raise a square matrix to an integer power (i.e. A**3 is the same as A.<a href="#LowerTri-mmul">mmul</a>(A.<a href="#LowerTri-mmul">mmul</a>(A))</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-hessenberg" href="#LowerTri-hessenberg"><span class="function-name">hessenberg</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-inverse" href="#LowerTri-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-lu" href="#LowerTri-lu"><span class="function-name">lu</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.<a href="#LowerTri-mmul">mmul</a>(U)==A</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="function"><dt><a name="LowerTri-__init__" href="#LowerTri-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a <a href="./__builtin__.html#list">list</a> of lists or a <a href="./__builtin__.html#list">list</a> of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-augment" href="#LowerTri-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-diag" href="#LowerTri-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-mmul" href="#LowerTri-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Matrix">Matrix</a> multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-qr" href="#LowerTri-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#LowerTri-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-rank" href="#LowerTri-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-solve" href="#LowerTri-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-star" href="#LowerTri-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#LowerTri-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-tr" href="#LowerTri-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-trace" href="#LowerTri-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="LowerTri-__abs__" href="#LowerTri-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__add__" href="#LowerTri-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__div__" href="#LowerTri-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__eq__" href="#LowerTri-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__getslice__" href="#LowerTri-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__mul__" href="#LowerTri-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__neg__" href="#LowerTri-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__radd__" href="#LowerTri-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__rdiv__" href="#LowerTri-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__rmul__" href="#LowerTri-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__rsub__" href="#LowerTri-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__str__" href="#LowerTri-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__sub__" href="#LowerTri-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-concat" href="#LowerTri-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-conjugate" href="#LowerTri-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-exists" href="#LowerTri-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-flatten" href="#LowerTri-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-forall" href="#LowerTri-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-imag" href="#LowerTri-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-map" href="#LowerTri-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-prod" href="#LowerTri-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-real" href="#LowerTri-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-sum" href="#LowerTri-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="LowerTri-__contains__" href="#LowerTri-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__delitem__" href="#LowerTri-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__delslice__" href="#LowerTri-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__ge__" href="#LowerTri-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__getattribute__" href="#LowerTri-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__getitem__" href="#LowerTri-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__gt__" href="#LowerTri-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__iadd__" href="#LowerTri-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__imul__" href="#LowerTri-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__iter__" href="#LowerTri-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__le__" href="#LowerTri-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__len__" href="#LowerTri-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__lt__" href="#LowerTri-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__ne__" href="#LowerTri-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__repr__" href="#LowerTri-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__reversed__" href="#LowerTri-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__setitem__" href="#LowerTri-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__setslice__" href="#LowerTri-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#LowerTri-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-__sizeof__" href="#LowerTri-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-append" href="#LowerTri-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-count" href="#LowerTri-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-extend" href="#LowerTri-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-index" href="#LowerTri-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-insert" href="#LowerTri-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-pop" href="#LowerTri-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-remove" href="#LowerTri-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-reverse" href="#LowerTri-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="LowerTri-sort" href="#LowerTri-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#LowerTri-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#LowerTri-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="Matrix" href="#Matrix">class <span class="class-name">Matrix</span></a>(<a href="./typerig.core.objects.matrix.html#Table">Table</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Matrix-__init__" href="#Matrix-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a <a href="./__builtin__.html#list">list</a> of lists or a <a href="./__builtin__.html#list">list</a> of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-augment" href="#Matrix-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-diag" href="#Matrix-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-mmul" href="#Matrix-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Matrix">Matrix</a> multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-qr" href="#Matrix-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#Matrix-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-rank" href="#Matrix-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-solve" href="#Matrix-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-star" href="#Matrix-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#Matrix-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-tr" href="#Matrix-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-trace" href="#Matrix-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Matrix-__abs__" href="#Matrix-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__add__" href="#Matrix-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__div__" href="#Matrix-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__eq__" href="#Matrix-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getslice__" href="#Matrix-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__mul__" href="#Matrix-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__neg__" href="#Matrix-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__radd__" href="#Matrix-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rdiv__" href="#Matrix-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rmul__" href="#Matrix-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rsub__" href="#Matrix-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__str__" href="#Matrix-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__sub__" href="#Matrix-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-concat" href="#Matrix-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-conjugate" href="#Matrix-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-exists" href="#Matrix-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-flatten" href="#Matrix-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-forall" href="#Matrix-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-imag" href="#Matrix-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-map" href="#Matrix-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-prod" href="#Matrix-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-real" href="#Matrix-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-sum" href="#Matrix-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Matrix-__contains__" href="#Matrix-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__delitem__" href="#Matrix-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__delslice__" href="#Matrix-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__ge__" href="#Matrix-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getattribute__" href="#Matrix-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getitem__" href="#Matrix-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__gt__" href="#Matrix-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__iadd__" href="#Matrix-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__imul__" href="#Matrix-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__iter__" href="#Matrix-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__le__" href="#Matrix-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__len__" href="#Matrix-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__lt__" href="#Matrix-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__ne__" href="#Matrix-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__repr__" href="#Matrix-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__reversed__" href="#Matrix-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__setitem__" href="#Matrix-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__setslice__" href="#Matrix-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Matrix-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__sizeof__" href="#Matrix-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-append" href="#Matrix-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-count" href="#Matrix-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-extend" href="#Matrix-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-index" href="#Matrix-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-insert" href="#Matrix-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-pop" href="#Matrix-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-remove" href="#Matrix-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-reverse" href="#Matrix-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-sort" href="#Matrix-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Matrix-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#Matrix-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="Square" href="#Square">class <span class="class-name">Square</span></a>(<a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Square">Square</a></dd><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Square-__pow__" href="#Square-__pow__"><span class="function-name">__pow__</span></a><span class="argspec">(self, exp)</span></dt><dd>

<pre class="doc" markdown="0">Raise a square matrix to an integer power (i.e. A**3 is the same as A.<a href="#Square-mmul">mmul</a>(A.<a href="#Square-mmul">mmul</a>(A))</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-det" href="#Square-det"><span class="function-name">det</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-eigs" href="#Square-eigs"><span class="function-name">eigs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Estimate principal eigenvalues using the QR with shifts method</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-hessenberg" href="#Square-hessenberg"><span class="function-name">hessenberg</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-inverse" href="#Square-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-lu" href="#Square-lu"><span class="function-name">lu</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.<a href="#Square-mmul">mmul</a>(U)==A</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="function"><dt><a name="Square-__init__" href="#Square-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a <a href="./__builtin__.html#list">list</a> of lists or a <a href="./__builtin__.html#list">list</a> of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-augment" href="#Square-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-diag" href="#Square-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-mmul" href="#Square-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Matrix">Matrix</a> multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-qr" href="#Square-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#Square-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-rank" href="#Square-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-solve" href="#Square-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-star" href="#Square-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#Square-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-tr" href="#Square-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-trace" href="#Square-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Square-__abs__" href="#Square-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__add__" href="#Square-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__div__" href="#Square-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__eq__" href="#Square-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getslice__" href="#Square-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__mul__" href="#Square-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__neg__" href="#Square-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__radd__" href="#Square-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rdiv__" href="#Square-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rmul__" href="#Square-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rsub__" href="#Square-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__str__" href="#Square-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__sub__" href="#Square-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-concat" href="#Square-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-conjugate" href="#Square-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-exists" href="#Square-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-flatten" href="#Square-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-forall" href="#Square-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-imag" href="#Square-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-map" href="#Square-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-prod" href="#Square-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-real" href="#Square-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-sum" href="#Square-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Square-__contains__" href="#Square-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__delitem__" href="#Square-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__delslice__" href="#Square-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__ge__" href="#Square-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getattribute__" href="#Square-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getitem__" href="#Square-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__gt__" href="#Square-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__iadd__" href="#Square-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__imul__" href="#Square-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__iter__" href="#Square-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__le__" href="#Square-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__len__" href="#Square-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__lt__" href="#Square-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__ne__" href="#Square-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__repr__" href="#Square-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__reversed__" href="#Square-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__setitem__" href="#Square-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__setslice__" href="#Square-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Square-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__sizeof__" href="#Square-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-append" href="#Square-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-count" href="#Square-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-extend" href="#Square-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-index" href="#Square-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-insert" href="#Square-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-pop" href="#Square-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-remove" href="#Square-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-reverse" href="#Square-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-sort" href="#Square-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Square-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#Square-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="Table" href="#Table">class <span class="class-name">Table</span></a>(<a href="./__builtin__.html#list">__builtin__.list</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes ------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Table-__abs__" href="#Table-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__add__" href="#Table-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__div__" href="#Table-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__eq__" href="#Table-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getslice__" href="#Table-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__init__" href="#Table-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__mul__" href="#Table-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__neg__" href="#Table-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__radd__" href="#Table-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rdiv__" href="#Table-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rmul__" href="#Table-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rsub__" href="#Table-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__str__" href="#Table-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__sub__" href="#Table-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-concat" href="#Table-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-conjugate" href="#Table-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-exists" href="#Table-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-flatten" href="#Table-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-forall" href="#Table-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-imag" href="#Table-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-map" href="#Table-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-prod" href="#Table-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-real" href="#Table-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-sum" href="#Table-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Table-__contains__" href="#Table-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__delitem__" href="#Table-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__delslice__" href="#Table-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__ge__" href="#Table-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getattribute__" href="#Table-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getitem__" href="#Table-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__gt__" href="#Table-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__iadd__" href="#Table-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__imul__" href="#Table-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__iter__" href="#Table-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__le__" href="#Table-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__len__" href="#Table-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__lt__" href="#Table-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__ne__" href="#Table-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__repr__" href="#Table-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__reversed__" href="#Table-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__setitem__" href="#Table-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__setslice__" href="#Table-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Table-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__sizeof__" href="#Table-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-append" href="#Table-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-count" href="#Table-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-extend" href="#Table-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-index" href="#Table-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-insert" href="#Table-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-pop" href="#Table-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-remove" href="#Table-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-reverse" href="#Table-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-sort" href="#Table-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Table-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#Table-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="Triangular" href="#Triangular">class <span class="class-name">Triangular</span></a>(<a href="./typerig.core.objects.matrix.html#Square">Square</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></dd><dd><a href="./typerig.core.objects.matrix.html#Square">Square</a></dd><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Triangular-det" href="#Triangular-det"><span class="function-name">det</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-eigs" href="#Triangular-eigs"><span class="function-name">eigs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Square">Square</a></h4><dl class="function"><dt><a name="Triangular-__pow__" href="#Triangular-__pow__"><span class="function-name">__pow__</span></a><span class="argspec">(self, exp)</span></dt><dd>

<pre class="doc" markdown="0">Raise a square matrix to an integer power (i.e. A**3 is the same as A.<a href="#Triangular-mmul">mmul</a>(A.<a href="#Triangular-mmul">mmul</a>(A))</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-hessenberg" href="#Triangular-hessenberg"><span class="function-name">hessenberg</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-inverse" href="#Triangular-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-lu" href="#Triangular-lu"><span class="function-name">lu</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.<a href="#Triangular-mmul">mmul</a>(U)==A</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="function"><dt><a name="Triangular-__init__" href="#Triangular-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a <a href="./__builtin__.html#list">list</a> of lists or a <a href="./__builtin__.html#list">list</a> of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-augment" href="#Triangular-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-diag" href="#Triangular-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-mmul" href="#Triangular-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Matrix">Matrix</a> multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-qr" href="#Triangular-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#Triangular-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-rank" href="#Triangular-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-solve" href="#Triangular-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-star" href="#Triangular-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#Triangular-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-tr" href="#Triangular-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-trace" href="#Triangular-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Triangular-__abs__" href="#Triangular-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__add__" href="#Triangular-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__div__" href="#Triangular-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__eq__" href="#Triangular-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__getslice__" href="#Triangular-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__mul__" href="#Triangular-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__neg__" href="#Triangular-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__radd__" href="#Triangular-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__rdiv__" href="#Triangular-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__rmul__" href="#Triangular-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__rsub__" href="#Triangular-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__str__" href="#Triangular-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__sub__" href="#Triangular-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-concat" href="#Triangular-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-conjugate" href="#Triangular-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-exists" href="#Triangular-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-flatten" href="#Triangular-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-forall" href="#Triangular-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-imag" href="#Triangular-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-map" href="#Triangular-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-prod" href="#Triangular-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-real" href="#Triangular-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-sum" href="#Triangular-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Triangular-__contains__" href="#Triangular-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__delitem__" href="#Triangular-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__delslice__" href="#Triangular-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__ge__" href="#Triangular-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__getattribute__" href="#Triangular-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__getitem__" href="#Triangular-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__gt__" href="#Triangular-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__iadd__" href="#Triangular-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__imul__" href="#Triangular-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__iter__" href="#Triangular-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__le__" href="#Triangular-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__len__" href="#Triangular-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__lt__" href="#Triangular-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__ne__" href="#Triangular-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__repr__" href="#Triangular-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__reversed__" href="#Triangular-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__setitem__" href="#Triangular-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__setslice__" href="#Triangular-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Triangular-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-__sizeof__" href="#Triangular-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-append" href="#Triangular-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-count" href="#Triangular-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-extend" href="#Triangular-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-index" href="#Triangular-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-insert" href="#Triangular-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-pop" href="#Triangular-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-remove" href="#Triangular-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-reverse" href="#Triangular-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Triangular-sort" href="#Triangular-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Triangular-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#Triangular-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="UpperTri" href="#UpperTri">class <span class="class-name">UpperTri</span></a>(<a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#UpperTri">UpperTri</a></dd><dd><a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></dd><dd><a href="./typerig.core.objects.matrix.html#Square">Square</a></dd><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Triangular">Triangular</a></h4><dl class="function"><dt><a name="UpperTri-det" href="#UpperTri-det"><span class="function-name">det</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-eigs" href="#UpperTri-eigs"><span class="function-name">eigs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Square">Square</a></h4><dl class="function"><dt><a name="UpperTri-__pow__" href="#UpperTri-__pow__"><span class="function-name">__pow__</span></a><span class="argspec">(self, exp)</span></dt><dd>

<pre class="doc" markdown="0">Raise a square matrix to an integer power (i.e. A**3 is the same as A.<a href="#UpperTri-mmul">mmul</a>(A.<a href="#UpperTri-mmul">mmul</a>(A))</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-hessenberg" href="#UpperTri-hessenberg"><span class="function-name">hessenberg</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-inverse" href="#UpperTri-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-lu" href="#UpperTri-lu"><span class="function-name">lu</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.<a href="#UpperTri-mmul">mmul</a>(U)==A</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="function"><dt><a name="UpperTri-__init__" href="#UpperTri-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a <a href="./__builtin__.html#list">list</a> of lists or a <a href="./__builtin__.html#list">list</a> of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-augment" href="#UpperTri-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-diag" href="#UpperTri-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-mmul" href="#UpperTri-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Matrix">Matrix</a> multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-qr" href="#UpperTri-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#UpperTri-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-rank" href="#UpperTri-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-solve" href="#UpperTri-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-star" href="#UpperTri-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#UpperTri-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-tr" href="#UpperTri-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-trace" href="#UpperTri-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="UpperTri-__abs__" href="#UpperTri-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__add__" href="#UpperTri-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__div__" href="#UpperTri-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__eq__" href="#UpperTri-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__getslice__" href="#UpperTri-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__mul__" href="#UpperTri-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__neg__" href="#UpperTri-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__radd__" href="#UpperTri-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__rdiv__" href="#UpperTri-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__rmul__" href="#UpperTri-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__rsub__" href="#UpperTri-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__str__" href="#UpperTri-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__sub__" href="#UpperTri-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-concat" href="#UpperTri-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-conjugate" href="#UpperTri-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-exists" href="#UpperTri-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-flatten" href="#UpperTri-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-forall" href="#UpperTri-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-imag" href="#UpperTri-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-map" href="#UpperTri-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-prod" href="#UpperTri-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-real" href="#UpperTri-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-sum" href="#UpperTri-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="UpperTri-__contains__" href="#UpperTri-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__delitem__" href="#UpperTri-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__delslice__" href="#UpperTri-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__ge__" href="#UpperTri-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__getattribute__" href="#UpperTri-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__getitem__" href="#UpperTri-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__gt__" href="#UpperTri-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__iadd__" href="#UpperTri-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__imul__" href="#UpperTri-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__iter__" href="#UpperTri-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__le__" href="#UpperTri-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__len__" href="#UpperTri-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__lt__" href="#UpperTri-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__ne__" href="#UpperTri-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__repr__" href="#UpperTri-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__reversed__" href="#UpperTri-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__setitem__" href="#UpperTri-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__setslice__" href="#UpperTri-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#UpperTri-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-__sizeof__" href="#UpperTri-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-append" href="#UpperTri-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-count" href="#UpperTri-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-extend" href="#UpperTri-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-index" href="#UpperTri-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-insert" href="#UpperTri-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-pop" href="#UpperTri-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-remove" href="#UpperTri-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-reverse" href="#UpperTri-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="UpperTri-sort" href="#UpperTri-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#UpperTri-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#UpperTri-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
<dt class="class"><h2><a name="Vec" href="#Vec">class <span class="class-name">Vec</span></a>(<a href="./typerig.core.objects.matrix.html#Table">Table</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Vec">Vec</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Vec-cross" href="#Vec-cross"><span class="function-name">cross</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0">Compute a Vector or Cross Product with another vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-dot" href="#Vec-dot"><span class="function-name">dot</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-house" href="#Vec-house"><span class="function-name">house</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0">Compute a Householder vector which zeroes all but the index element after a reflection</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-norm" href="#Vec-norm"><span class="function-name">norm</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-normalize" href="#Vec-normalize"><span class="function-name">normalize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-outer" href="#Vec-outer"><span class="function-name">outer</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-polyval" href="#Vec-polyval"><span class="function-name">polyval</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Vec">Vec</a>([6,3,4]).<a href="#Vec-polyval">polyval</a>(5) evaluates to 6*x**2 + 3*x + 4 at x=5</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-ratval" href="#Vec-ratval"><span class="function-name">ratval</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#Vec">Vec</a>([10,20,30,40,50]).<a href="#-ratfit">ratfit</a>(5) evaluates to (10*x**2 + 20*x + 30) / (40*x**2 + 50*x + 1) at x=5.</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Vec-__abs__" href="#Vec-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__add__" href="#Vec-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__div__" href="#Vec-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__eq__" href="#Vec-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getslice__" href="#Vec-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__init__" href="#Vec-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__mul__" href="#Vec-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__neg__" href="#Vec-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__radd__" href="#Vec-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rdiv__" href="#Vec-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rmul__" href="#Vec-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rsub__" href="#Vec-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__str__" href="#Vec-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__sub__" href="#Vec-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-concat" href="#Vec-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-conjugate" href="#Vec-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-exists" href="#Vec-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-flatten" href="#Vec-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-forall" href="#Vec-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-imag" href="#Vec-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-map" href="#Vec-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-prod" href="#Vec-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-real" href="#Vec-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-sum" href="#Vec-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Vec-__contains__" href="#Vec-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__delitem__" href="#Vec-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__delslice__" href="#Vec-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__ge__" href="#Vec-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getattribute__" href="#Vec-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getitem__" href="#Vec-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__gt__" href="#Vec-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__iadd__" href="#Vec-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__imul__" href="#Vec-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__iter__" href="#Vec-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__le__" href="#Vec-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__len__" href="#Vec-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__lt__" href="#Vec-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__ne__" href="#Vec-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__repr__" href="#Vec-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__reversed__" href="#Vec-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-__reversed__">__reversed__</a>() -- return a reverse iterator over the <a href="./__builtin__.html#list">list</a></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__setitem__" href="#Vec-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__setslice__" href="#Vec-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#Vec-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__sizeof__" href="#Vec-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-append" href="#Vec-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-count" href="#Vec-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-extend" href="#Vec-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-extend">extend</a>(iterable) -- extend <a href="./__builtin__.html#list">list</a> by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-index" href="#Vec-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-insert" href="#Vec-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-pop" href="#Vec-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if <a href="./__builtin__.html#list">list</a> is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-remove" href="#Vec-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-reverse" href="#Vec-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-sort" href="#Vec-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#Vec-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#Vec-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd></dl></div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-Mat" href="#-Mat"><span class="function-name">Mat</span></a><span class="argspec">(elems)</span></dt><dd>

<pre class="doc" markdown="0">Factory function to create a new matrix.</pre>

</dd></dl>

<dl class="function"><dt><a name="-eye" href="#-eye"><span class="function-name">eye</span></a><span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Identity matrix with side length m-by-m or m-by-n</pre>

</dd></dl>

<dl class="function"><dt><a name="-funToVec" href="#-funToVec"><span class="function-name">funToVec</span></a><span class="argspec">(tgtfun, low<span class="parameter-default">=-1</span>, high<span class="parameter-default">=1</span>, steps<span class="parameter-default">=40</span>, EqualSpacing<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Compute x,y points from evaluating a target function over an interval (low to high)
at evenly spaces points or with Chebyshev abscissa spacing (default)</pre>

</dd></dl>

<dl class="function"><dt><a name="-funfit" href="#-funfit"><span class="function-name">funfit</span></a><span class="argspec">((xvec, yvec), basisfuns)</span></dt><dd>

<pre class="doc" markdown="0">Solves design matrix for approximating to basis functions</pre>

</dd></dl>

<dl class="function"><dt><a name="-genmat" href="#-genmat"><span class="function-name">genmat</span></a><span class="argspec">(m, n, func)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-getconj" href="#-getconj"><span class="function-name">getconj</span></a><span class="argspec">(z)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-getimag" href="#-getimag"><span class="function-name">getimag</span></a><span class="argspec">(z)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-getreal" href="#-getreal"><span class="function-name">getreal</span></a><span class="argspec">(z)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

<dl class="function"><dt><a name="-hilb" href="#-hilb"><span class="function-name">hilb</span></a><span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Hilbert matrix with side length m-by-m or m-by-n.  Elem[i][j]=1/(i+j+1)</pre>

</dd></dl>

<dl class="function"><dt><a name="-iszero" href="#-iszero"><span class="function-name">iszero</span></a><span class="argspec">(z)</span></dt><dd>

<pre class="doc" markdown="0"># - Helpers ------------------------------</pre>

</dd></dl>

<dl class="function"><dt><a name="-polyfit" href="#-polyfit"><span class="function-name">polyfit</span></a><span class="argspec">((xvec, yvec), degree<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Solves Vandermonde design matrix for approximating polynomial coefficients</pre>

</dd></dl>

<dl class="function"><dt><a name="-rand" href="#-rand"><span class="function-name">rand</span></a><span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Random matrix with side length m-by-m or m-by-n</pre>

</dd></dl>

<dl class="function"><dt><a name="-ratfit" href="#-ratfit"><span class="function-name">ratfit</span></a><span class="argspec">((xvec, yvec), degree<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Solves design matrix for approximating rational polynomial coefficients (a*x**2 + b*x + c)/(d*x**2 + e*x + 1)</pre>

</dd></dl>

<dl class="function"><dt><a name="-zeroes" href="#-zeroes"><span class="function-name">zeroes</span></a><span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Zero matrix with side length m-by-m or m-by-n.</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.objects.matrix.Table"></a>

## `Table`


<dt class="class"><h2><span class="class-name">typerig.core.objects.matrix.Table</span> = <a name="typerig.core.objects.matrix.Table" href="#typerig.core.objects.matrix.Table">class Table</a>(<a href="./__builtin__.html#list">__builtin__.list</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"># - Classes ------------------------------</pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Table-__abs__" href="#Table-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__add__" href="#Table-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__div__" href="#Table-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__eq__" href="#Table-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getslice__" href="#Table-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__init__" href="#Table-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__mul__" href="#Table-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__neg__" href="#Table-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__radd__" href="#Table-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rdiv__" href="#Table-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rmul__" href="#Table-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__rsub__" href="#Table-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__str__" href="#Table-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__sub__" href="#Table-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-concat" href="#Table-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-conjugate" href="#Table-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-exists" href="#Table-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-flatten" href="#Table-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-forall" href="#Table-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-imag" href="#Table-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-map" href="#Table-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-prod" href="#Table-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-real" href="#Table-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Table-sum" href="#Table-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

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

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Table-__contains__" href="#Table-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__delitem__" href="#Table-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__delslice__" href="#Table-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__ge__" href="#Table-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getattribute__" href="#Table-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__getitem__" href="#Table-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__gt__" href="#Table-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__iadd__" href="#Table-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__imul__" href="#Table-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__iter__" href="#Table-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__le__" href="#Table-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__len__" href="#Table-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__lt__" href="#Table-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__ne__" href="#Table-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__repr__" href="#Table-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__reversed__" href="#Table-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-__reversed__">__reversed__</a>() -- return a reverse iterator over the list</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__setitem__" href="#Table-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__setslice__" href="#Table-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Table-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-__sizeof__" href="#Table-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-append" href="#Table-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-count" href="#Table-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-extend" href="#Table-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-extend">extend</a>(iterable) -- extend list by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-index" href="#Table-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-insert" href="#Table-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-pop" href="#Table-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-remove" href="#Table-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-reverse" href="#Table-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Table-sort" href="#Table-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Table-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.matrix.Table-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.matrix.Table.concat"></a>

### `__add__`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Table.concat" href="#-typerig.core.objects.matrix.Table.concat"><span class="function-name">typerig.core.objects.matrix.Table.concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.__add__(y) <==> x+y</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Table.dim"></a>

### `dim`


<span class="other-name">typerig.core.objects.matrix.Table.dim</span> = 1


<a name="typerig.core.objects.matrix.Table.map"></a>

### `map`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Table.map" href="#-typerig.core.objects.matrix.Table.map"><span class="function-name">typerig.core.objects.matrix.Table.map</span></a> = map<span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Table">typerig.core.objects.matrix.Table</a> method</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Vec"></a>

## `Vec`


<dt class="class"><h2><span class="class-name">typerig.core.objects.matrix.Vec</span> = <a name="typerig.core.objects.matrix.Vec" href="#typerig.core.objects.matrix.Vec">class Vec</a>(<a href="./typerig.core.objects.matrix.html#Table">Table</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Vec">Vec</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Vec-cross" href="#Vec-cross"><span class="function-name">cross</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0">Compute a Vector or Cross Product with another vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-dot" href="#Vec-dot"><span class="function-name">dot</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-house" href="#Vec-house"><span class="function-name">house</span></a><span class="argspec">(self, index)</span></dt><dd>

<pre class="doc" markdown="0">Compute a Householder vector which zeroes all but the index element after a reflection</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-norm" href="#Vec-norm"><span class="function-name">norm</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-normalize" href="#Vec-normalize"><span class="function-name">normalize</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-outer" href="#Vec-outer"><span class="function-name">outer</span></a><span class="argspec">(self, otherVec)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-polyval" href="#Vec-polyval"><span class="function-name">polyval</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Vec([6,3,4]).<a href="#typerig.core.objects.matrix.Vec-polyval">polyval</a>(5) evaluates to 6*x**2 + 3*x + 4 at x=5</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-ratval" href="#Vec-ratval"><span class="function-name">ratval</span></a><span class="argspec">(self, x)</span></dt><dd>

<pre class="doc" markdown="0">Vec([10,20,30,40,50]).ratfit(5) evaluates to (10*x**2 + 20*x + 30) / (40*x**2 + 50*x + 1) at x=5.</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Vec-__abs__" href="#Vec-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__add__" href="#Vec-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__div__" href="#Vec-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__eq__" href="#Vec-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getslice__" href="#Vec-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__init__" href="#Vec-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__mul__" href="#Vec-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__neg__" href="#Vec-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__radd__" href="#Vec-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rdiv__" href="#Vec-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rmul__" href="#Vec-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__rsub__" href="#Vec-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__str__" href="#Vec-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__sub__" href="#Vec-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-concat" href="#Vec-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-conjugate" href="#Vec-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-exists" href="#Vec-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-flatten" href="#Vec-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-forall" href="#Vec-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-imag" href="#Vec-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-map" href="#Vec-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-prod" href="#Vec-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-real" href="#Vec-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-sum" href="#Vec-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Vec-__contains__" href="#Vec-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__delitem__" href="#Vec-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__delslice__" href="#Vec-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__ge__" href="#Vec-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getattribute__" href="#Vec-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__getitem__" href="#Vec-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__gt__" href="#Vec-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__iadd__" href="#Vec-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__imul__" href="#Vec-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__iter__" href="#Vec-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__le__" href="#Vec-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__len__" href="#Vec-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__lt__" href="#Vec-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__ne__" href="#Vec-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__repr__" href="#Vec-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__reversed__" href="#Vec-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-__reversed__">__reversed__</a>() -- return a reverse iterator over the list</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__setitem__" href="#Vec-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__setslice__" href="#Vec-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Vec-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-__sizeof__" href="#Vec-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-append" href="#Vec-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-count" href="#Vec-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-extend" href="#Vec-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-extend">extend</a>(iterable) -- extend list by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-index" href="#Vec-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-insert" href="#Vec-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-pop" href="#Vec-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-remove" href="#Vec-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-reverse" href="#Vec-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Vec-sort" href="#Vec-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Vec-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.matrix.Vec-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.matrix.Vec.cross"></a>

### `cross`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Vec.cross" href="#-typerig.core.objects.matrix.Vec.cross"><span class="function-name">typerig.core.objects.matrix.Vec.cross</span></a> = cross<span class="argspec">(self, otherVec)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Vec">typerig.core.objects.matrix.Vec</a> method</span></dt><dd>

<pre class="doc" markdown="0">Compute a Vector or Cross Product with another vector</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Vec.house"></a>

### `house`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Vec.house" href="#-typerig.core.objects.matrix.Vec.house"><span class="function-name">typerig.core.objects.matrix.Vec.house</span></a> = house<span class="argspec">(self, index)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Vec">typerig.core.objects.matrix.Vec</a> method</span></dt><dd>

<pre class="doc" markdown="0">Compute a Householder vector which zeroes all but the index element after a reflection</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Vec.polyval"></a>

### `polyval`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Vec.polyval" href="#-typerig.core.objects.matrix.Vec.polyval"><span class="function-name">typerig.core.objects.matrix.Vec.polyval</span></a> = polyval<span class="argspec">(self, x)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Vec">typerig.core.objects.matrix.Vec</a> method</span></dt><dd>

<pre class="doc" markdown="0">Vec([6,3,4]).polyval(5) evaluates to 6*x**2 + 3*x + 4 at x=5</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Vec.ratval"></a>

### `ratval`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Vec.ratval" href="#-typerig.core.objects.matrix.Vec.ratval"><span class="function-name">typerig.core.objects.matrix.Vec.ratval</span></a> = ratval<span class="argspec">(self, x)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Vec">typerig.core.objects.matrix.Vec</a> method</span></dt><dd>

<pre class="doc" markdown="0">Vec([10,20,30,40,50]).ratfit(5) evaluates to (10*x**2 + 20*x + 30) / (40*x**2 + 50*x + 1) at x=5.</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix"></a>

## `Matrix`


<dt class="class"><h2><span class="class-name">typerig.core.objects.matrix.Matrix</span> = <a name="typerig.core.objects.matrix.Matrix" href="#typerig.core.objects.matrix.Matrix">class Matrix</a>(<a href="./typerig.core.objects.matrix.html#Table">Table</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Matrix-__init__" href="#Matrix-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a list of lists or a list of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-augment" href="#Matrix-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-diag" href="#Matrix-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-mmul" href="#Matrix-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">Matrix multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-qr" href="#Matrix-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#typerig.core.objects.matrix.Matrix-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-rank" href="#Matrix-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-solve" href="#Matrix-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-star" href="#Matrix-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#typerig.core.objects.matrix.Matrix-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-tr" href="#Matrix-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-trace" href="#Matrix-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Matrix-__abs__" href="#Matrix-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__add__" href="#Matrix-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__div__" href="#Matrix-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__eq__" href="#Matrix-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getslice__" href="#Matrix-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__mul__" href="#Matrix-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__neg__" href="#Matrix-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__radd__" href="#Matrix-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rdiv__" href="#Matrix-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rmul__" href="#Matrix-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__rsub__" href="#Matrix-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__str__" href="#Matrix-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__sub__" href="#Matrix-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-concat" href="#Matrix-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-conjugate" href="#Matrix-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-exists" href="#Matrix-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-flatten" href="#Matrix-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-forall" href="#Matrix-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-imag" href="#Matrix-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-map" href="#Matrix-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-prod" href="#Matrix-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-real" href="#Matrix-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-sum" href="#Matrix-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Matrix-__contains__" href="#Matrix-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__delitem__" href="#Matrix-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__delslice__" href="#Matrix-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__ge__" href="#Matrix-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getattribute__" href="#Matrix-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__getitem__" href="#Matrix-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__gt__" href="#Matrix-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__iadd__" href="#Matrix-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__imul__" href="#Matrix-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__iter__" href="#Matrix-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__le__" href="#Matrix-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__len__" href="#Matrix-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__lt__" href="#Matrix-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__ne__" href="#Matrix-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__repr__" href="#Matrix-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__reversed__" href="#Matrix-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-__reversed__">__reversed__</a>() -- return a reverse iterator over the list</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__setitem__" href="#Matrix-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__setslice__" href="#Matrix-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Matrix-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-__sizeof__" href="#Matrix-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-append" href="#Matrix-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-count" href="#Matrix-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-extend" href="#Matrix-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-extend">extend</a>(iterable) -- extend list by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-index" href="#Matrix-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-insert" href="#Matrix-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-pop" href="#Matrix-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-remove" href="#Matrix-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-reverse" href="#Matrix-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Matrix-sort" href="#Matrix-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Matrix-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.matrix.Matrix-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.matrix.Matrix.tr"></a>

### `tr`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.tr" href="#-typerig.core.objects.matrix.Matrix.tr"><span class="function-name">typerig.core.objects.matrix.Matrix.tr</span></a> = tr<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.star"></a>

### `star`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.star" href="#-typerig.core.objects.matrix.Matrix.star"><span class="function-name">typerig.core.objects.matrix.Matrix.star</span></a> = star<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].conjugate()</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.diag"></a>

### `diag`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.diag" href="#-typerig.core.objects.matrix.Matrix.diag"><span class="function-name">typerig.core.objects.matrix.Matrix.diag</span></a> = diag<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.mmul"></a>

### `mmul`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.mmul" href="#-typerig.core.objects.matrix.Matrix.mmul"><span class="function-name">typerig.core.objects.matrix.Matrix.mmul</span></a> = mmul<span class="argspec">(self, other)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Matrix multiply by another matrix or a column vector</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.augment"></a>

### `augment`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.augment" href="#-typerig.core.objects.matrix.Matrix.augment"><span class="function-name">typerig.core.objects.matrix.Matrix.augment</span></a> = augment<span class="argspec">(self, otherMat)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.qr"></a>

### `qr`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.qr" href="#-typerig.core.objects.matrix.Matrix.qr"><span class="function-name">typerig.core.objects.matrix.Matrix.qr</span></a> = qr<span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.tr()*Q==I(n), R upper triangular</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Matrix.solve"></a>

### `solve`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Matrix.solve" href="#-typerig.core.objects.matrix.Matrix.solve"><span class="function-name">typerig.core.objects.matrix.Matrix.solve</span></a> = solve<span class="argspec">(self, b)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Matrix">typerig.core.objects.matrix.Matrix</a> method</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Square"></a>

## `Square`


<dt class="class"><h2><span class="class-name">typerig.core.objects.matrix.Square</span> = <a name="typerig.core.objects.matrix.Square" href="#typerig.core.objects.matrix.Square">class Square</a>(<a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0"></pre>


</dd>  <div class="mro"><dl class="mro"><dt>Method resolution order:</dt><dd><a href="./typerig.core.objects.matrix.html#Square">Square</a></dd><dd><a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></dd><dd><a href="./typerig.core.objects.matrix.html#Table">Table</a></dd><dd><a href="./__builtin__.html#list">__builtin__.list</a></dd><dd><a href="./__builtin__.html#object">__builtin__.object</a></dd></dl></div><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Square-__pow__" href="#Square-__pow__"><span class="function-name">__pow__</span></a><span class="argspec">(self, exp)</span></dt><dd>

<pre class="doc" markdown="0">Raise a square matrix to an integer power (i.e. A**3 is the same as A.<a href="#typerig.core.objects.matrix.Square-mmul">mmul</a>(A.<a href="#typerig.core.objects.matrix.Square-mmul">mmul</a>(A))</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-det" href="#Square-det"><span class="function-name">det</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-eigs" href="#Square-eigs"><span class="function-name">eigs</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Estimate principal eigenvalues using the QR with shifts method</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-hessenberg" href="#Square-hessenberg"><span class="function-name">hessenberg</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-inverse" href="#Square-inverse"><span class="function-name">inverse</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-lu" href="#Square-lu"><span class="function-name">lu</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.<a href="#typerig.core.objects.matrix.Square-mmul">mmul</a>(U)==A</pre>

</dd></dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="function"><dt><a name="Square-__init__" href="#Square-__init__"><span class="function-name">__init__</span></a><span class="argspec">(self, elems)</span></dt><dd>

<pre class="doc" markdown="0">Form a matrix from a list of lists or a list of Vecs</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-augment" href="#Square-augment"><span class="function-name">augment</span></a><span class="argspec">(self, otherMat)</span></dt><dd>

<pre class="doc" markdown="0">Make a new matrix with the two original matrices laid side by side</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-diag" href="#Square-diag"><span class="function-name">diag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return a vector composed of elements on the matrix diagonal</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-mmul" href="#Square-mmul"><span class="function-name">mmul</span></a><span class="argspec">(self, other)</span></dt><dd>

<pre class="doc" markdown="0">Matrix multiply by another matrix or a column vector</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-qr" href="#Square-qr"><span class="function-name">qr</span></a><span class="argspec">(self, ROnly<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">QR decomposition using Householder reflections: Q*R==self, Q.<a href="#typerig.core.objects.matrix.Square-tr">tr</a>()*Q==I(n), R upper triangular</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-rank" href="#Square-rank"><span class="function-name">rank</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-solve" href="#Square-solve"><span class="function-name">solve</span></a><span class="argspec">(self, b)</span></dt><dd>

<pre class="doc" markdown="0">Divide matrix into a column vector or matrix and iterate to improve the solution</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-star" href="#Square-star"><span class="function-name">star</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Return the Hermetian adjoint so that Star[i][j] = Original[j][i].<a href="#typerig.core.objects.matrix.Square-conjugate">conjugate</a>()</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-tr" href="#Square-tr"><span class="function-name">tr</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0">Tranpose elements so that Transposed[i][j] = Original[j][i]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-trace" href="#Square-trace"><span class="function-name">trace</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Matrix">Matrix</a></h4><dl class="descriptor"><dt>cols</dt>
</dl>
<dl class="descriptor"><dt>rows</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>

  <h4 class="head-methods">Methods from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="function"><dt><a name="Square-__abs__" href="#Square-__abs__"><span class="function-name">__abs__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__add__" href="#Square-__add__"><span class="function-name">__add__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__div__" href="#Square-__div__"><span class="function-name">__div__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__eq__" href="#Square-__eq__"><span class="function-name">__eq__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getslice__" href="#Square-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(self, i, j)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__mul__" href="#Square-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__neg__" href="#Square-__neg__"><span class="function-name">__neg__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__radd__" href="#Square-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rdiv__" href="#Square-__rdiv__"><span class="function-name">__rdiv__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rmul__" href="#Square-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__rsub__" href="#Square-__rsub__"><span class="function-name">__rsub__</span></a><span class="argspec">(self, lhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__str__" href="#Square-__str__"><span class="function-name">__str__</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__sub__" href="#Square-__sub__"><span class="function-name">__sub__</span></a><span class="argspec">(self, rhs)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-concat" href="#Square-concat"><span class="function-name">concat</span></a> = __add__<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-conjugate" href="#Square-conjugate"><span class="function-name">conjugate</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-exists" href="#Square-exists"><span class="function-name">exists</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-flatten" href="#Square-flatten"><span class="function-name">flatten</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-forall" href="#Square-forall"><span class="function-name">forall</span></a><span class="argspec">(self, predicate)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-imag" href="#Square-imag"><span class="function-name">imag</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-map" href="#Square-map"><span class="function-name">map</span></a><span class="argspec">(self, op, rhs<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Apply a unary operator to every element in the matrix or a binary operator to corresponding
elements in two arrays.  If the dimensions are different, broadcast the smaller dimension over
the larger (i.e. match a scalar to every element in a vector or a vector to a matrix).</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-prod" href="#Square-prod"><span class="function-name">prod</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-real" href="#Square-real"><span class="function-name">real</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Square-sum" href="#Square-sum"><span class="function-name">sum</span></a><span class="argspec">(self)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-desc">Descriptors from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl class="descriptor"><dt>__dict__</dt>
<dd>

<pre class="doc" markdown="0">dictionary for instance variables (if defined)</pre>

</dd>
</dl>
<dl class="descriptor"><dt>__weakref__</dt>
<dd>

<pre class="doc" markdown="0">list of weak references to the object (if defined)</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes from <a href="./typerig.core.objects.matrix.html#Table">Table</a></h4><dl><dt><span class="other-name">dim</span> = 1</dt></dl>

  <h4 class="head-methods">Methods from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl class="function"><dt><a name="Square-__contains__" href="#Square-__contains__"><span class="function-name">__contains__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__contains__">__contains__</a>(y) <==> y in x</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__delitem__" href="#Square-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__delslice__" href="#Square-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__ge__" href="#Square-__ge__"><span class="function-name">__ge__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__ge__">__ge__</a>(y) <==> x>=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getattribute__" href="#Square-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__getitem__" href="#Square-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__gt__" href="#Square-__gt__"><span class="function-name">__gt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__gt__">__gt__</a>(y) <==> x>y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__iadd__" href="#Square-__iadd__"><span class="function-name">__iadd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__iadd__">__iadd__</a>(y) <==> x+=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__imul__" href="#Square-__imul__"><span class="function-name">__imul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__imul__">__imul__</a>(y) <==> x*=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__iter__" href="#Square-__iter__"><span class="function-name">__iter__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__iter__">__iter__</a>() <==> iter(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__le__" href="#Square-__le__"><span class="function-name">__le__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__le__">__le__</a>(y) <==> x<=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__len__" href="#Square-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__lt__" href="#Square-__lt__"><span class="function-name">__lt__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__lt__">__lt__</a>(y) <==> x<y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__ne__" href="#Square-__ne__"><span class="function-name">__ne__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__ne__">__ne__</a>(y) <==> x!=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__repr__" href="#Square-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__reversed__" href="#Square-__reversed__"><span class="function-name">__reversed__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-__reversed__">__reversed__</a>() -- return a reverse iterator over the list</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__setitem__" href="#Square-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__setslice__" href="#Square-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#typerig.core.objects.matrix.Square-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-__sizeof__" href="#Square-__sizeof__"><span class="function-name">__sizeof__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-__sizeof__">__sizeof__</a>() -- size of L in memory, in bytes</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-append" href="#Square-append"><span class="function-name">append</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-append">append</a>(object) -- append object to end</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-count" href="#Square-count"><span class="function-name">count</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-count">count</a>(value) -> integer -- return number of occurrences of value</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-extend" href="#Square-extend"><span class="function-name">extend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-extend">extend</a>(iterable) -- extend list by appending elements from the iterable</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-index" href="#Square-index"><span class="function-name">index</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-index">index</a>(value, [start, [stop]]) -> integer -- return first index of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-insert" href="#Square-insert"><span class="function-name">insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-insert">insert</a>(index, object) -- insert object before index</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-pop" href="#Square-pop"><span class="function-name">pop</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-pop">pop</a>([index]) -> item -- remove and return item at index (default last).
Raises IndexError if list is empty or index is out of range.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-remove" href="#Square-remove"><span class="function-name">remove</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-remove">remove</a>(value) -- remove first occurrence of value.
Raises ValueError if the value is not present.</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-reverse" href="#Square-reverse"><span class="function-name">reverse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-reverse">reverse</a>() -- reverse *IN PLACE*</pre>

</dd></dl>
<dl class="function"><dt><a name="Square-sort" href="#Square-sort"><span class="function-name">sort</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">L.<a href="#typerig.core.objects.matrix.Square-sort">sort</a>(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*;
cmp(x, y) -> -1, 0, 1</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes from <a href="./__builtin__.html#list">__builtin__.list</a></h4><dl><dt><span class="other-name">__hash__</span> = None</dt></dl>
<dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#typerig.core.objects.matrix.Square-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="typerig.core.objects.matrix.Square.lu"></a>

### `lu`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Square.lu" href="#-typerig.core.objects.matrix.Square.lu"><span class="function-name">typerig.core.objects.matrix.Square.lu</span></a> = lu<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Square">typerig.core.objects.matrix.Square</a> method</span></dt><dd>

<pre class="doc" markdown="0">Factor a square matrix into lower and upper triangular form such that L.mmul(U)==A</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Square.hessenberg"></a>

### `hessenberg`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Square.hessenberg" href="#-typerig.core.objects.matrix.Square.hessenberg"><span class="function-name">typerig.core.objects.matrix.Square.hessenberg</span></a> = hessenberg<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Square">typerig.core.objects.matrix.Square</a> method</span></dt><dd>

<pre class="doc" markdown="0">Householder reduction to Hessenberg Form (zeroes below the diagonal)
while keeping the same eigenvalues as self.</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Square.eigs"></a>

### `eigs`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Square.eigs" href="#-typerig.core.objects.matrix.Square.eigs"><span class="function-name">typerig.core.objects.matrix.Square.eigs</span></a> = eigs<span class="argspec">(self)</span><span class="note"> unbound <a href="./typerig.core.objects.matrix.html#Square">typerig.core.objects.matrix.Square</a> method</span></dt><dd>

<pre class="doc" markdown="0">Estimate principal eigenvalues using the QR with shifts method</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.Mat"></a>

## `Mat`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.Mat" href="#-typerig.core.objects.matrix.Mat"><span class="function-name">typerig.core.objects.matrix.Mat</span></a> = Mat<span class="argspec">(elems)</span></dt><dd>

<pre class="doc" markdown="0">Factory function to create a new matrix.</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.funToVec"></a>

## `funToVec`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.funToVec" href="#-typerig.core.objects.matrix.funToVec"><span class="function-name">typerig.core.objects.matrix.funToVec</span></a> = funToVec<span class="argspec">(tgtfun, low<span class="parameter-default">=-1</span>, high<span class="parameter-default">=1</span>, steps<span class="parameter-default">=40</span>, EqualSpacing<span class="parameter-default">=0</span>)</span></dt><dd>

<pre class="doc" markdown="0">Compute x,y points from evaluating a target function over an interval (low to high)
at evenly spaces points or with Chebyshev abscissa spacing (default)</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.funfit"></a>

## `funfit`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.funfit" href="#-typerig.core.objects.matrix.funfit"><span class="function-name">typerig.core.objects.matrix.funfit</span></a> = funfit<span class="argspec">((xvec, yvec), basisfuns)</span></dt><dd>

<pre class="doc" markdown="0">Solves design matrix for approximating to basis functions</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.polyfit"></a>

## `polyfit`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.polyfit" href="#-typerig.core.objects.matrix.polyfit"><span class="function-name">typerig.core.objects.matrix.polyfit</span></a> = polyfit<span class="argspec">((xvec, yvec), degree<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Solves Vandermonde design matrix for approximating polynomial coefficients</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.ratfit"></a>

## `ratfit`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.ratfit" href="#-typerig.core.objects.matrix.ratfit"><span class="function-name">typerig.core.objects.matrix.ratfit</span></a> = ratfit<span class="argspec">((xvec, yvec), degree<span class="parameter-default">=2</span>)</span></dt><dd>

<pre class="doc" markdown="0">Solves design matrix for approximating rational polynomial coefficients (a*x**2 + b*x + c)/(d*x**2 + e*x + 1)</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.zeroes"></a>

## `zeroes`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.zeroes" href="#-typerig.core.objects.matrix.zeroes"><span class="function-name">typerig.core.objects.matrix.zeroes</span></a> = zeroes<span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Zero matrix with side length m-by-m or m-by-n.</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.eye"></a>

## `eye`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.eye" href="#-typerig.core.objects.matrix.eye"><span class="function-name">typerig.core.objects.matrix.eye</span></a> = eye<span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Identity matrix with side length m-by-m or m-by-n</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.hilb"></a>

## `hilb`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.hilb" href="#-typerig.core.objects.matrix.hilb"><span class="function-name">typerig.core.objects.matrix.hilb</span></a> = hilb<span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Hilbert matrix with side length m-by-m or m-by-n.  Elem[i][j]=1/(i+j+1)</pre>

</dd></dl>



<a name="typerig.core.objects.matrix.rand"></a>

## `rand`


<dl class="function"><dt><a name="-typerig.core.objects.matrix.rand" href="#-typerig.core.objects.matrix.rand"><span class="function-name">typerig.core.objects.matrix.rand</span></a> = rand<span class="argspec">(m<span class="parameter-default">=1</span>, n<span class="parameter-default">=None</span>)</span></dt><dd>

<pre class="doc" markdown="0">Random matrix with side length m-by-m or m-by-n</pre>

</dd></dl>

