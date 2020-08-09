

<a name="FL.Glyph"></a>

# `Glyph`


<dt class="class"><h2><span class="class-name">FL.Glyph</span> = <a name="FL.Glyph" href="#FL.Glyph">class Glyph</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Glyph - class to represent glyph
===============================================

CONSTRUCTOR:
  Glyph() - generic constructor, creates an empty glyph
  Glyph(Glyph) - copy constructor
  Glyph(masterscount) - creates a glyph with 'masterscount' number of masters
  Glyph(masterscount, [Node, ...]) - creates a glyph with 'masterscount' number of masters and assigns a list of nodes

ATTRIBUTES:
  parent (read-only) - Glyph's parent object
  nodes [Node] - list of Nodes
  customdata (string) - custom data defined for this glyph
  note (string) - note defined for this glyph
  mark (integer) - True if glyph is marked
  anchors [Anchor] - list of anchors
  hhints [Hint] - list of horizontal hints
  vhints [Hint] - list of vertical hints
  hlinks [Link] - list of horizontal links
  vlinks [Link] - list of vertical links
  components [Component] - list of componets
  replace_table [Replace] - hint replacing program, list of Replace objects
  kerning [KerningPair] - list of kerning pairs
  layers_number (integer) - number of masters
  flags (integer) - flags set for this glyph
  nodes_number (integer) - number of nodes, same as 'len(Glyph)'
  width (integer) - advance width for the first master
  height (integer) - advance height for the first master
  unicode (integer) - first Unicode index in integer form
  unicodes [integer] - list of Unicode indexes
  name (string) - glyph name
  mask (string) - mask

  STORED TRUETYPE DATA
  advance_width (integer)
  advance_height (integer)
  left_side_bearing (integer)
  top_side_bearing (integer)
  y_pels (integer)
  bounding_box (Rect)
  number_of_contours (integer)
  end_points [integer]
  points [TTPoint]
  instructions [Byte]
  hdmx[Byte]

OPERATIONS:
  len() - returns number of nodes in the glyph
  [] - can be used to access individial nodes
  slice - can be used to access portion of the glyph's nodes array
  + or concatination - can be used to append Glyph, Node or sequence of Nodes
  multiply - second operand must be Matrix, applies matrix transformation to a glyph

METHODS
  Assign (Glyph) - copies all information from the assigned glyph
  Transform(Matrix m) - applies Matrix transformation to the Glyph (see Matrix().__doc__)
  SetLayersNumber(mastersnumber) - changes the number of masters, is applicable only to glyphs that have no parent
  Clear() - removes all nodes
  Add - refer to '+' operator
  Insert (Node | Glyph | [Node]) | (Node | Glyph | [Node], nodeindex) - inserts Node, Glyph or sequence of Nodes at the begining of glyph's nodes or at specified node index
  Present (style) - returns True if a layer or a combination of layers are present in the glyph
  Delete (index) | (index0, index1) - removes node or range of nodes
  ExpandLayer (masterindex) - expands selected master to all other masters
  Shift (Point) | (Point, masterindex) - shifts positions of all nodes at first or specified master
  Scale (Point(float) scale) | (Point(float) scale, Point center) | (Point(float) scale, Point center, masterindex) - scales the glyph
  Layer (masterindex) - returns list of Points for all nodes for the selected master
  Section (masterindex, pointindex, nodetype) - returns list of Points that conform to selected options
  MoveNode(...) - moves the node copying Edit tool behavior (see User manual for details)
  DeleteNode(nodeindex) - removes the node
  InsertNode(nodeindex) | (nodeindex, float time) | (nodeindex, float time, masterindex) - insers new node on a contour
  SELECTION OPERATIONS
  Selection() - returns list of selected nodes
  SelectAll() - selects all nodes
  UnselectAll() - deselects all nodes
  InvertSelection() - selects unselected nodes and deselects selected nodes
  isAnySelected() - returns True if at least one node is selected
  SelectedCount() - returns number of selected nodes
  SelectRect(Rect r) | (Rect r, masterindex) - selects all nodes that are inside the rectangle
  UnselectRect(Rect r) | (Rect r, masterindex) - deselects all nodes that are inside the rectangle
  DeleteSelected() - deletes all selected nodes

  METRICS AND BBOX OPERATIONS
  GetBoundingRect() | (masterindex) - returns Rect - bounding box of the glyph
  GetMetrics() | (masterindex) - returns glyph advance width and advance height in a form of Point
  SetMetrics(Point p) | (Point p, masterindex) - assigns new values to the width and height of the glyph
  GetVSB() | (masterindex) - returns glyph bottom sidebearing position
  SetVSB(value) | (value, masterindex) - assigns new values to the bottom sidebearing of the glyph

  OVERLAP OPERATIONS
  RemoveOverlap() | (masterindex) - removes overlap
  Badd(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Add operation with the glyph or list of nodes
  Bsubtract(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Subtract operation with the glyph or list of nodes
  Bintersect(Glyph g) | ([Node]) | (Glyph g, masterindex) | ([Node], masterindex) - performs bollean Insersect operation with the glyph or list of nodes

  OPERATIONS ON CONTOURS
  GetContoursNumber() - returns number of contours in the glyph
  GetContourBegin(contourindex) - returns index of the first node for a contour
  GetContourLength(contourindex) - returns number of nodes in a contour
  SelectContour(contourindex) - selects all nodes in the contour
  DeleteContour(contourindex) - removes contour
  ReverseContour(contourindex) - reverses contour's direction
  ReorderContour(contourindex, newindex) - reorders contours in the glyph
  isContourClockwise(contourindex) - returns True if direction of contour is clockwise
  SetStartNode(nodeindex) - makes the node a starting node of the contour
  FindContour(nodeindex) - returns number of contour containing the 'nodeindex'

  HINTS OPERATIONS
  RemoveHints(mode) - removes hints and links
  Autohint() | (masterindex) - automatically generates Type 1 hints

  ANCHOR OPERATIONS
  FindAnchor(string name) - finds anchor by name

  TRANSFORMATION ACTIONS
  Decompose() - pastes all components to the glyph outline
  MakeExtremeNodes() | (masterindex) - automatically detects and adds extreme nodes
  Audit() | (masterindex) - performs test of the glyph and returns list of AuditRecord objects
  Iterate(Iterator) - iterates glyph trough iterator class which must unclude following methods: 
     Start(); ClosePath(); StartPath(Node); LineTo(Node); CurveTo(Node); SplineTo(Node); Finish()
  Rotate3D
  Extrude3D(outlinewidth, shift_x, shift_y)
  Shadow(outlinewidth, shift_x, shift_y)
  College(outlinewidth, distance)
  Gradient(outlinewidth, direction, stripes_number, start_y, finish_y)
  Distance(width_x, width_y, cornermode) | (width_x, width_y, cornermode, Glyph dest)
  Interpolate([(nodeindex, Point newposition])
  Warp([Point], float force)
  Rasterize() | Rasterize(Image, [, active layer[, height]]) | Rasterize(Image, [, WeightVector[, height]]) - rasterizes glyph to the Image or to glyph's background. Returns resulting image_rect. Height is relative to font's UPM
         Blend(Glyph source, integer layer1, integer layer2, Point amount) - returns blend of the glyph and source
         JoinAll() - tries to join all open contours
         SaveEPS(string filename) | (string filename, layer) - writes layer into the EPS file named filename
         LoadEPS(string filename) - reads EPS from filename and returns Glyph object. Use Assign method to replace current glyph with the loaded outline
  R([Point], float force)</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Glyph-Add" href="#Glyph-Add"><span class="function-name">Add</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Assign" href="#Glyph-Assign"><span class="function-name">Assign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Audit" href="#Glyph-Audit"><span class="function-name">Audit</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Autohint" href="#Glyph-Autohint"><span class="function-name">Autohint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Badd" href="#Glyph-Badd"><span class="function-name">Badd</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Bintersect" href="#Glyph-Bintersect"><span class="function-name">Bintersect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Blend" href="#Glyph-Blend"><span class="function-name">Blend</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Bsubtract" href="#Glyph-Bsubtract"><span class="function-name">Bsubtract</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Clear" href="#Glyph-Clear"><span class="function-name">Clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-College" href="#Glyph-College"><span class="function-name">College</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Decompose" href="#Glyph-Decompose"><span class="function-name">Decompose</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Delete" href="#Glyph-Delete"><span class="function-name">Delete</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-DeleteContour" href="#Glyph-DeleteContour"><span class="function-name">DeleteContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-DeleteNode" href="#Glyph-DeleteNode"><span class="function-name">DeleteNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-DeleteSelected" href="#Glyph-DeleteSelected"><span class="function-name">DeleteSelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Distance" href="#Glyph-Distance"><span class="function-name">Distance</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-EditMask" href="#Glyph-EditMask"><span class="function-name">EditMask</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-ExchangeMask" href="#Glyph-ExchangeMask"><span class="function-name">ExchangeMask</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-ExpandLayer" href="#Glyph-ExpandLayer"><span class="function-name">ExpandLayer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Extrude3D" href="#Glyph-Extrude3D"><span class="function-name">Extrude3D</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-FindAnchor" href="#Glyph-FindAnchor"><span class="function-name">FindAnchor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-FindContour" href="#Glyph-FindContour"><span class="function-name">FindContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-GetBoundingRect" href="#Glyph-GetBoundingRect"><span class="function-name">GetBoundingRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-GetContourBegin" href="#Glyph-GetContourBegin"><span class="function-name">GetContourBegin</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-GetContourLength" href="#Glyph-GetContourLength"><span class="function-name">GetContourLength</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-GetContoursNumber" href="#Glyph-GetContoursNumber"><span class="function-name">GetContoursNumber</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-GetMetrics" href="#Glyph-GetMetrics"><span class="function-name">GetMetrics</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Gradient" href="#Glyph-Gradient"><span class="function-name">Gradient</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Insert" href="#Glyph-Insert"><span class="function-name">Insert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-InsertNode" href="#Glyph-InsertNode"><span class="function-name">InsertNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Interpolate" href="#Glyph-Interpolate"><span class="function-name">Interpolate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-InvertSelection" href="#Glyph-InvertSelection"><span class="function-name">InvertSelection</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Iterate" href="#Glyph-Iterate"><span class="function-name">Iterate</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-JoinAll" href="#Glyph-JoinAll"><span class="function-name">JoinAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Layer" href="#Glyph-Layer"><span class="function-name">Layer</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-LoadEPS" href="#Glyph-LoadEPS"><span class="function-name">LoadEPS</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-MakeExtremeNodes" href="#Glyph-MakeExtremeNodes"><span class="function-name">MakeExtremeNodes</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-MoveNode" href="#Glyph-MoveNode"><span class="function-name">MoveNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Present" href="#Glyph-Present"><span class="function-name">Present</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Rasterize" href="#Glyph-Rasterize"><span class="function-name">Rasterize</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-RemoveHints" href="#Glyph-RemoveHints"><span class="function-name">RemoveHints</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-RemoveOverlap" href="#Glyph-RemoveOverlap"><span class="function-name">RemoveOverlap</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-ReorderContour" href="#Glyph-ReorderContour"><span class="function-name">ReorderContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-ReverseContour" href="#Glyph-ReverseContour"><span class="function-name">ReverseContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Rotate3D" href="#Glyph-Rotate3D"><span class="function-name">Rotate3D</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SaveEPS" href="#Glyph-SaveEPS"><span class="function-name">SaveEPS</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Scale" href="#Glyph-Scale"><span class="function-name">Scale</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Section" href="#Glyph-Section"><span class="function-name">Section</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SelectAll" href="#Glyph-SelectAll"><span class="function-name">SelectAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SelectContour" href="#Glyph-SelectContour"><span class="function-name">SelectContour</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SelectRect" href="#Glyph-SelectRect"><span class="function-name">SelectRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SelectedCount" href="#Glyph-SelectedCount"><span class="function-name">SelectedCount</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Selection" href="#Glyph-Selection"><span class="function-name">Selection</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SetLayersNumber" href="#Glyph-SetLayersNumber"><span class="function-name">SetLayersNumber</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SetMetrics" href="#Glyph-SetMetrics"><span class="function-name">SetMetrics</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-SetStartNode" href="#Glyph-SetStartNode"><span class="function-name">SetStartNode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Shadow" href="#Glyph-Shadow"><span class="function-name">Shadow</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Shift" href="#Glyph-Shift"><span class="function-name">Shift</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Transform" href="#Glyph-Transform"><span class="function-name">Transform</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-UnselectAll" href="#Glyph-UnselectAll"><span class="function-name">UnselectAll</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-UnselectRect" href="#Glyph-UnselectRect"><span class="function-name">UnselectRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-Warp" href="#Glyph-Warp"><span class="function-name">Warp</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__add__" href="#Glyph-__add__"><span class="function-name">__add__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__add__">__add__</a>(y) <==> x+y</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__delattr__" href="#Glyph-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__delitem__" href="#Glyph-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__delslice__" href="#Glyph-__delslice__"><span class="function-name">__delslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__delslice__">__delslice__</a>(i, j) <==> del x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__getattribute__" href="#Glyph-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__getitem__" href="#Glyph-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__getslice__" href="#Glyph-__getslice__"><span class="function-name">__getslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__getslice__">__getslice__</a>(i, j) <==> x[i:j]

Use of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__init__" href="#Glyph-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__len__" href="#Glyph-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__mul__" href="#Glyph-__mul__"><span class="function-name">__mul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__mul__">__mul__</a>(y) <==> x*y</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__radd__" href="#Glyph-__radd__"><span class="function-name">__radd__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__radd__">__radd__</a>(y) <==> y+x</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__repr__" href="#Glyph-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__rmul__" href="#Glyph-__rmul__"><span class="function-name">__rmul__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__rmul__">__rmul__</a>(y) <==> y*x</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__setattr__" href="#Glyph-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__setitem__" href="#Glyph-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-__setslice__" href="#Glyph-__setslice__"><span class="function-name">__setslice__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Glyph-__setslice__">__setslice__</a>(i, j, y) <==> x[i:j]=y

Use  of negative indices is not supported.</pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-clear" href="#Glyph-clear"><span class="function-name">clear</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-isAnySelected" href="#Glyph-isAnySelected"><span class="function-name">isAnySelected</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Glyph-isContourClockwise" href="#Glyph-isContourClockwise"><span class="function-name">isContourClockwise</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Glyph-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
