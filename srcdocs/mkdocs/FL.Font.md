

<a name="FL.Font"></a>

# `Font`


<dt class="class"><h2><span class="class-name">FL.Font</span> = <a name="FL.Font" href="#FL.Font">class Font</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Font - base class to represent font
===============================================

CONSTRUCTOR:
  Font() - generic constructor, creates an empty Font  Font(Font) - copy constructor
  Font(string filename) - creates a Font and assigns name of the file from which it was opened

ATTRIBUTES:

  NAMES, COPYRIGHT AND IDENTIFICATION
  family_name(string) - font Family Name
  style_name
  full_name(string) - font Full Name
  font_name(string) - font Font Name
  font_style(integer) - Font Style
  menu_name(string) - font menu name
  weight
  weight_code
  width
  designer
  designer_url
  fontnames[NameRecord] - list of font name records
  copyright(string) - Copyright name field
  notice(string) - Notice field
  note(string) - Font note
  unique_id
  tt_u_id
  tt_version
  trademark
  x_u_id_num
  x_u_id
  vendor
  vendor_url
  version
  year
  version_major
  version_minor
  vp_id
  ms_charset
  ms_id
  panose[integer] - list of Panose values
  collection[collection] - list of glyph indexes in FontLab collection
  pcl_chars_set
  pcl_id

  DIMENSIONS
  upm
  ascender[integer] - list of ascenders, one for each master
  descender[integer] - list of descenders, one for each master
  cap_height[integer] - list of CapHeight records, one for each master
  x_height[integer] - list of xHeight values, one for each master
  default_width
  slant_angle
  italic_angle(float) - Italic Angle
  is_fixed_pitch
  underline_position
  underline_thickness

  ALIGNMENT
  blue_fuzz
  blue_scale
  blue_shift
  blue_values_num(integer) - number of defined blue values
  blue_values[integer[integer]] - two-dimentional array of BlueValues - master index is top-level index
  family_blues_num(integer) - number of FamilyBlues records
  family_blues[integer[integer]] - two-dimentional array of FamilyBlues - master index is top-level index
  family_other_blues_num(integer) - number of FamilyOtherBlues records
  family_other_blues[integer[integer]] - two-dimentional array of FamilyOtherBlues - master index is top-level index
  force_bold[integer] - list of Force Bold values, one for each master
  other_blues_num
  other_blues[integer[integer]] - two-dimentional array of OtherBlues - master index is top-level index
  stem_snap_h_num
  stem_snap_h
  stem_snap_v_num
  stem_snap_v

  OTHER ATTRIBUTES
  classes[string] - list of glyph classes
  ot_classes - OpenType classes data
  classes_text - glyph classes compiled in ot_classes format
  features[Feature] - list of OpenType features
  customdata(string) - font custom data field
  truetypetables[TrueTypeTable] - list of custom TrueType tables
  ttinfo(TTInfo) - loaded TrueType information (mostly hinting-related tables)
  encoding
  glyphs[Glyph] - array of glyphs
  source
  weight_vector
  measurement - position of the measurement line for the font

OPERATIONS:
  len - returns number of glyphs
  [] - accesses glyphs array

METHODS
  New() - clears the font
  Open(string filename) - opens font from VFB format
  Save(string filename) - saves font in VFB format
  Reencode()  FindGlyph(string name) | (Uni unicode) | (integer Unicode) - finds glyph and return its index or -1
  DefineAxis(string Name, string Type, string ShortName) - defines the new Multiple Master axis
  DeleteAxis(axisindex, float position) - removes the axis
  GenerateUnicode() - generates Unicode indexes for all glyphs
  GenerateNames() - generates names for all glyphs
  GenerateGlyph(string glyphname) - generates new glyph using 'glyphname' as a source of information about glyph's composition
  MakeKernFeature([WeightVector vector]) - generates 'kern' feature using font kerning and classes
  MergeFonts(Font source[, flags]) - appends all glyphs from the source font. Check mfXXXX constants for options
  SetClassFlags(int class_index, bool left, bool right) - allows to set 'left' and 'right' properties of the kerning class   SetClassFlags(int class_index, bool lsb, bool rsb, bool width) - allows to set 'lsb', 'rsb' and 'width' properties of the metrics class   GetClassLeft(int class_index) - returns the 'left' property of the class  GetClassRight(int class_index) - returns the 'right' property of the class  GetClassMetricsFlags(int class_index) - returns the tuple containing LSB, RSB and Width flags of the metrics class</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Font-DefineAxis" href="#Font-DefineAxis"><span class="function-name">DefineAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-DeleteAxis" href="#Font-DeleteAxis"><span class="function-name">DeleteAxis</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-FindGlyph" href="#Font-FindGlyph"><span class="function-name">FindGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GenerateGlyph" href="#Font-GenerateGlyph"><span class="function-name">GenerateGlyph</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GenerateNames" href="#Font-GenerateNames"><span class="function-name">GenerateNames</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GenerateUnicode" href="#Font-GenerateUnicode"><span class="function-name">GenerateUnicode</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GetClassLeft" href="#Font-GetClassLeft"><span class="function-name">GetClassLeft</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GetClassMetricsFlags" href="#Font-GetClassMetricsFlags"><span class="function-name">GetClassMetricsFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-GetClassRight" href="#Font-GetClassRight"><span class="function-name">GetClassRight</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-MakeKernFeature" href="#Font-MakeKernFeature"><span class="function-name">MakeKernFeature</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-MergeFonts" href="#Font-MergeFonts"><span class="function-name">MergeFonts</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-New" href="#Font-New"><span class="function-name">New</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-Open" href="#Font-Open"><span class="function-name">Open</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-OpenAFM" href="#Font-OpenAFM"><span class="function-name">OpenAFM</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-Save" href="#Font-Save"><span class="function-name">Save</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-SaveAFM" href="#Font-SaveAFM"><span class="function-name">SaveAFM</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-SetClassFlags" href="#Font-SetClassFlags"><span class="function-name">SetClassFlags</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__delattr__" href="#Font-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__delitem__" href="#Font-__delitem__"><span class="function-name">__delitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__delitem__">__delitem__</a>(y) <==> del x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__getattribute__" href="#Font-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__getitem__" href="#Font-__getitem__"><span class="function-name">__getitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__getitem__">__getitem__</a>(y) <==> x[y]</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__init__" href="#Font-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__len__" href="#Font-__len__"><span class="function-name">__len__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__len__">__len__</a>() <==> len(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__repr__" href="#Font-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__setattr__" href="#Font-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-__setitem__" href="#Font-__setitem__"><span class="function-name">__setitem__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Font-__setitem__">__setitem__</a>(i, y) <==> x[i]=y</pre>

</dd></dl>
<dl class="function"><dt><a name="Font-has_key" href="#Font-has_key"><span class="function-name">has_key</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Font-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
