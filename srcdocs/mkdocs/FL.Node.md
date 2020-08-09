

<a name="FL.Node"></a>

# `Node`


<dt class="class"><h2><span class="class-name">FL.Node</span> = <a name="FL.Node" href="#FL.Node">class Node</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Node - class to represent node
===============================================
This class is Multiple Master - compatible

CONSTRUCTOR:
  Node() - generic constructor, creates an empty node
  Node(Node) - copy constructor
  Node(intteger type, Point p) - creates a Node and assigns type and coordinates of the final point

ATTRIBUTES:
  parent (read-only) - Node's parent object
         type (integer) - type of the node, values are: nMOVE, nLINE, nCURVE or nOFF
  count (integer, read-only) - number of points in the node. 3 for curves and 1 for all other types of nodes
  alignment (integer) - type of primitive connection, possible values are: nSHARP, nSMOOTH, nFIXED
  selected (integer) - True if node is selected
  point (Point) - position of the final point of the first master
  points [(Points)] - positions of all points of the first master
  x (integer) - horizontal position of the final point of the node
  y (integer) - vertical position of the final point of the node

OPERATIONS:
  len() - returns number of points in the node, same as count attribute
  [] - can be used to access individial points of the first master
  multiply - second operand must be Matrix, applies matrix transformation to a node

METHODS
  Assign - assigns new values to a Node, refer to constructor for a description of possible options
  SetAllLayers(pointindex, Point p) - assigns position of the point p to all masters of the point number 'pointindex'
  Layer(masterindex) - returns list of points for the master 'masterindex'
  Section(pointindex) - returns list of points for all layers and point number 'pointindex'
  Shift(Point p, masterindex) - shifts position of all points for the master 'masterindex'
  ExpandLayer(masterindex) - copies positions of all points in the master 'masterindex' to other masters
  Transform(Matrix m) - applies Matrix transformation to the Node (see Matrix().__doc__)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Node-Assign" href="#Node-Assign"><span class="function-name">Assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-ExpandLayer" href="#Node-ExpandLayer"><span class="function-name">ExpandLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-Layer" href="#Node-Layer"><span class="function-name">Layer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-Section" href="#Node-Section"><span class="function-name">Section</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-SetAllLayers" href="#Node-SetAllLayers"><span class="function-name">SetAllLayers</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-Shift" href="#Node-Shift"><span class="function-name">Shift</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-Transform" href="#Node-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__add__" href="#Node-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__delattr__" href="#Node-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__delitem__" href="#Node-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__delslice__" href="#Node-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__getattribute__" href="#Node-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__getitem__" href="#Node-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__getslice__" href="#Node-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__init__" href="#Node-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__init__">__init__</a>(...) initializes x; see help(<a href="#FL.Node-type">type</a>(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__len__" href="#Node-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__mul__" href="#Node-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__repr__" href="#Node-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__rmul__" href="#Node-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__setattr__" href="#Node-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__setitem__" href="#Node-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Node-__setslice__" href="#Node-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Node-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>alignment</dt>
</dl>
<dl class="descriptor"><dt>count</dt>
</dl>
<dl class="descriptor"><dt>open</dt>
</dl>
<dl class="descriptor"><dt>parent</dt>
</dl>
<dl class="descriptor"><dt>point</dt>
</dl>
<dl class="descriptor"><dt>points</dt>
</dl>
<dl class="descriptor"><dt>selected</dt>
</dl>
<dl class="descriptor"><dt>type</dt>
</dl>
<dl class="descriptor"><dt>x</dt>
</dl>
<dl class="descriptor"><dt>y</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Node-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
