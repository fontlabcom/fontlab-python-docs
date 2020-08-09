

<a name="FL.Canvas"></a>

# `Canvas`


<dt class="class"><h2><span class="class-name">FL.Canvas</span> = <a name="FL.Canvas" href="#FL.Canvas">class Canvas</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Canvas - class to represent screen paint area and operations
===============================================
This class can perform automatic coordinates transformations, so you can draw in Glyph coordinate space or, if you prefer, in screen coordinates directly
Use constants defined for FontLab module to assign attributes to Canvas object

CONSTRUCTOR:
  ++ Never create Canvas object explicitly - they must be obtained from the FontLab's window classes
  Canvas() - generic constructor, creates an empty Canvas
  Canvas(Canvas) - copy constructor

ATTRIBUTES:
  delta (Point) - horizontal shift during coordinates transformation
  scale (Point(float)) - scaling during coordinates transformation
  width (integer, read-only) - width of the canvas in pixels
  height (integer, read-only) - height of the canvas in pixels
  draw_style (integer, write-only) - sets current drawing mode (copy, XOR, invert etc.)
  pen_color (integer, write-only) - sets current pen color
  pen_style (integer, write-only) - sets current pen style (solid, dashed etc.)
  brush_color (integer, write-only) - sets current brush color
  brush_style (integer, write-only) -  sets current brush style (solid, patterned etc.)
  text_color (integer, write-only) - sets color for a text
  bk_color (integer, write-only) - sets color for a text background
  bk_mode (integer, write-only) - sets background mode for a text output (transparent or opaque)

OPERATIONS:

METHODS
  MoveTo(Point p) | (x, y) - moves current position to p or (x, y) coordinates
  LineTo(Point p) | (x, y) - draws a straight line to the position p or (x, y)
  CurveTo(Point p0, Point p1, Point p2) - draws a 3th-order Bezier curve from the current point to points p0, p1, p2
  SplineTo(Point p0, Point p1) - draws a 2th-order Bezier curve from the current point to points p0, p1
  Ellipse(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled ellipse defined by the Rect r, points p0 and p1 or set of coordinates
  Rectangle(Rect r) | (Point p0, Point p1) | (x0, y0, x1, y1) - draws a filled rectangle defined by the Rect r, points p0 and p1 or set of coordinates
  Convert(Point p) - converts coordinates from the source coordinate space to screen coordinates
  UnConvert(Point p) - converts screen coordinates to the currently defined coordinate space
  FitGlyph(Rect r, Glyph g) | (Rect r, Glyph g, WeightVector w) - recalculates parameters of coordinate conversion function to fit glyph g into rectangle r using currently selected options.
  FillGlyph(Glyph g) | (Glyph g, WeightVector w) - fills the glyph g using current coordinate transformation.
  OutlineGlyph(Glyph g) | (Glyph g, WeightVector w) - draws the glyph g outline using current coordinate transformation.
  TextOut(Point p, string s) | (x, y, string s) - draws the string s in the position p or (x, y)
  PutImage(Image i, Point p) | (Image i, Pioint p, int mode) - puts Image i at the selected point</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Canvas-Convert" href="#Canvas-Convert"><span class="function-name">Convert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-CurveTo" href="#Canvas-CurveTo"><span class="function-name">CurveTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-Ellipse" href="#Canvas-Ellipse"><span class="function-name">Ellipse</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-FillGlyph" href="#Canvas-FillGlyph"><span class="function-name">FillGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-FitGlyph" href="#Canvas-FitGlyph"><span class="function-name">FitGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-LineTo" href="#Canvas-LineTo"><span class="function-name">LineTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-MoveTo" href="#Canvas-MoveTo"><span class="function-name">MoveTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-OutlineGlyph" href="#Canvas-OutlineGlyph"><span class="function-name">OutlineGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-PutImage" href="#Canvas-PutImage"><span class="function-name">PutImage</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-Rectangle" href="#Canvas-Rectangle"><span class="function-name">Rectangle</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-SplineTo" href="#Canvas-SplineTo"><span class="function-name">SplineTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-TextOut" href="#Canvas-TextOut"><span class="function-name">TextOut</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-UnConvert" href="#Canvas-UnConvert"><span class="function-name">UnConvert</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-__delattr__" href="#Canvas-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Canvas-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-__getattribute__" href="#Canvas-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Canvas-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-__init__" href="#Canvas-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Canvas-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-__repr__" href="#Canvas-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Canvas-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Canvas-__setattr__" href="#Canvas-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Canvas-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Canvas-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
