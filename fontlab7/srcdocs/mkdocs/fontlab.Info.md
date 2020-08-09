

<a name="fontlab.Info"></a>

# `Info`


<dt class="class"><h2><span class="class-name">fontlab.Info</span> = <a name="fontlab.Info" href="#fontlab.Info">class Info</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">Font Info data</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Info-__delattr__" href="#Info-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Info-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Info-__getattribute__" href="#Info-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Info-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Info-__init__" href="#Info-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Info-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Info-__repr__" href="#Info-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Info-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Info-__setattr__" href="#Info-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#fontlab.Info-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>ascender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>capHeight</dt>
<dd>

<pre class="doc" markdown="0">Cap height value. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>copyright</dt>
<dd>

<pre class="doc" markdown="0">Copyright statement. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>descender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>familyName</dt>
<dd>

<pre class="doc" markdown="0">Family name. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>italicAngle</dt>
<dd>

<pre class="doc" markdown="0">Italic angle. This must be an angle in counter-clockwise degrees from the vertical. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>macintoshFONDFamilyID</dt>
<dd>

<pre class="doc" markdown="0">Family ID number. Corresponds to the ffFamID in the FOND resource. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>macintoshFONDName</dt>
<dd>

<pre class="doc" markdown="0">Font name for the FOND resource. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>note</dt>
<dd>

<pre class="doc" markdown="0">Arbitrary note about the font. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeGaspRangeRecords</dt>
<dd>

<pre class="doc" markdown="0">A list of gasp Range Records. These must be sorted in ascending order based on the rangeMaxPPEM value of the record. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHeadCreated</dt>
<dd>

<pre class="doc" markdown="0">Creation date. Expressed as a string of the format "YYYY/MM/DD HH:MM:SS". "YYYY/MM/DD" is year/month/day. The month must be in the range 1-12 and the day must be in the range 1-end of month. "HH:MM:SS" is hour:minute:second. The hour must be in the range 0:23. The minute and second must each be in the range 0-59. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHeadFlags</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table flags field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHeadLowestRecPPEM</dt>
<dd>

<pre class="doc" markdown="0">Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field. This should be a non-negative integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType hhea table Ascender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaCaretOffset</dt>
<dd>

<pre class="doc" markdown="0">Caret offset value. Corresponds to the OpenType hhea table caretOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaCaretSlopeRise</dt>
<dd>

<pre class="doc" markdown="0">Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaCaretSlopeRun</dt>
<dd>

<pre class="doc" markdown="0">Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType hhea table Descender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeHheaLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType hhea table LineGap field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameCompatibleFullName</dt>
<dd>

<pre class="doc" markdown="0">Compatible full name. Corresponds to the OpenType name table name ID 18. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameDescription</dt>
<dd>

<pre class="doc" markdown="0">Description of the font. Corresponds to the OpenType name table name ID 10. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameDesigner</dt>
<dd>

<pre class="doc" markdown="0">Designer name. Corresponds to the OpenType name table name ID 9. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameDesignerURL</dt>
<dd>

<pre class="doc" markdown="0">URL for the designer. Corresponds to the OpenType name table name ID 12. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameLicense</dt>
<dd>

<pre class="doc" markdown="0">License text. Corresponds to the OpenType name table name ID 13. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameLicenseURL</dt>
<dd>

<pre class="doc" markdown="0">URL for the license. Corresponds to the OpenType name table name ID 14. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameManufacturer</dt>
<dd>

<pre class="doc" markdown="0">Manufacturer name. Corresponds to the OpenType name table name ID 8. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameManufacturerURL</dt>
<dd>

<pre class="doc" markdown="0">Manufacturer URL. Corresponds to the OpenType name table name ID 11. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNamePreferredFamilyName</dt>
<dd>

<pre class="doc" markdown="0">Preferred family name. Corresponds to the OpenType name table name ID 16. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNamePreferredSubfamilyName</dt>
<dd>

<pre class="doc" markdown="0">Preferred subfamily name. Corresponds to the OpenType name table name ID 17. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameRecords</dt>
<dd>

<pre class="doc" markdown="0">A list of name records. This name record storage area is intended for records that require platform, encoding and or language localization. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameSampleText</dt>
<dd>

<pre class="doc" markdown="0">Sample text. Corresponds to the OpenType name table name ID 19. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameUniqueID</dt>
<dd>

<pre class="doc" markdown="0">Unique ID string. Corresponds to the OpenType name table name ID 3. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameVersion</dt>
<dd>

<pre class="doc" markdown="0">Version string. Corresponds to the OpenType name table name ID 5. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameWWSFamilyName</dt>
<dd>

<pre class="doc" markdown="0">WWS family name. Corresponds to the OpenType name table name ID 21. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeNameWWSSubfamilyName</dt>
<dd>

<pre class="doc" markdown="0">WWS Subfamily name. Corresponds to the OpenType name table name ID 22. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2CodePageRanges</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2FamilyClass</dt>
<dd>

<pre class="doc" markdown="0">Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, must be in the range 0-14. The second number, representing the subclass, must be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table sFamilyClass field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2Panose</dt>
<dd>

<pre class="doc" markdown="0">The list must contain 10 non-negative integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table Panose field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2Selection</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table selection field. Note: Bits 0 (italic), 5 (bold) and 6 (regular) must not be set here. These bits should be taken from the generic styleMapStyle attribute. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2StrikeoutPosition</dt>
<dd>

<pre class="doc" markdown="0">Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2StrikeoutSize</dt>
<dd>

<pre class="doc" markdown="0">Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SubscriptXOffset</dt>
<dd>

<pre class="doc" markdown="0">Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SubscriptXSize</dt>
<dd>

<pre class="doc" markdown="0">Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SubscriptYOffset</dt>
<dd>

<pre class="doc" markdown="0">Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SubscriptYSize</dt>
<dd>

<pre class="doc" markdown="0">Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SuperscriptXOffset</dt>
<dd>

<pre class="doc" markdown="0">Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SuperscriptXSize</dt>
<dd>

<pre class="doc" markdown="0">Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SuperscriptYOffset</dt>
<dd>

<pre class="doc" markdown="0">Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2SuperscriptYSize</dt>
<dd>

<pre class="doc" markdown="0">Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2Type</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table fsType field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2TypoAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2TypoDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2TypoLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2UnicodeRanges</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2VendorID</dt>
<dd>

<pre class="doc" markdown="0">Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2WeightClass</dt>
<dd>

<pre class="doc" markdown="0">Weight class value. Must be a non-negative integer. Corresponds to the OpenType OS/2 table usWeightClass field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2WidthClass</dt>
<dd>

<pre class="doc" markdown="0">Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2WinAscent</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field. This should be a non-negative integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeOS2WinDescent</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType OS/2 table usWinDescent field. This should be a non-negative integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaCaretOffset</dt>
<dd>

<pre class="doc" markdown="0">Caret offset value. Corresponds to the OpenType vhea table caretOffset field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaCaretSlopeRise</dt>
<dd>

<pre class="doc" markdown="0">Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaCaretSlopeRun</dt>
<dd>

<pre class="doc" markdown="0">Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaVertTypoAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaVertTypoDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType vhea table vertTypoDescender field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>openTypeVheaVertTypoLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>panose</dt>
<dd>

<pre class="doc" markdown="0">PANOSE identification. Should be a string containing 10 space-separated numbers</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptBlueFuzz</dt>
<dd>

<pre class="doc" markdown="0">BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptBlueScale</dt>
<dd>

<pre class="doc" markdown="0">BlueScale value. This corresponds to the Type 1/CFF BlueScale field. This should be a float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptBlueShift</dt>
<dd>

<pre class="doc" markdown="0">BlueShift value. This corresponds to the Type 1/CFF BlueShift field. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptBlueValues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptDefaultCharacter</dt>
<dd>

<pre class="doc" markdown="0">The name of the glyph that should be used as the default character in PFM files. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptDefaultWidthX</dt>
<dd>

<pre class="doc" markdown="0">Default width for glyphs. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptFamilyBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptFamilyOtherBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptFontName</dt>
<dd>

<pre class="doc" markdown="0">Name to be used for the FontName field in Type 1/CFF table. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptForceBold</dt>
<dd>

<pre class="doc" markdown="0">Indicates how the Type 1/CFF ForceBold field should be set. This should be a boolean</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptFullName</dt>
<dd>

<pre class="doc" markdown="0">Name to be used for the FullName field in Type 1/CFF table. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptIsFixedPitch</dt>
<dd>

<pre class="doc" markdown="0">Indicates if the font is monospaced. An authoring tool could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field This should be a boolean</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptNominalWidthX</dt>
<dd>

<pre class="doc" markdown="0">Nominal width for glyphs. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptOtherBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptStemSnapH</dt>
<dd>

<pre class="doc" markdown="0">List of horizontal stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptStemSnapV</dt>
<dd>

<pre class="doc" markdown="0">List of vertical stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field. This should be a list</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptUnderlinePosition</dt>
<dd>

<pre class="doc" markdown="0">Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptUnderlineThickness</dt>
<dd>

<pre class="doc" markdown="0">Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptUniqueID</dt>
<dd>

<pre class="doc" markdown="0">A unique ID number as defined in the Type 1/CFF specification. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptWeightName</dt>
<dd>

<pre class="doc" markdown="0">A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>postscriptWindowsCharacterSet</dt>
<dd>

<pre class="doc" markdown="0">The Windows character set. The values are defined below. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>styleMapFamilyName</dt>
<dd>

<pre class="doc" markdown="0">Family name used for bold, italic and bold italic style mapping. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>styleMapStyleName</dt>
<dd>

<pre class="doc" markdown="0">Style map style. The possible values are regular, italic, bold and bold italic. These are case sensitive. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>styleName</dt>
<dd>

<pre class="doc" markdown="0">Style name. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>trademark</dt>
<dd>

<pre class="doc" markdown="0">Trademark statement. This should be a string</pre>

</dd>
</dl>
<dl class="descriptor"><dt>unitsPerEm</dt>
<dd>

<pre class="doc" markdown="0">Units per em. This should be a non-negative integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>versionMajor</dt>
<dd>

<pre class="doc" markdown="0">Major version. This should be a integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>versionMinor</dt>
<dd>

<pre class="doc" markdown="0">Minor version. This should be a non-negative integer</pre>

</dd>
</dl>
<dl class="descriptor"><dt>xHeight</dt>
<dd>

<pre class="doc" markdown="0">x-height value. This should be a integer or float</pre>

</dd>
</dl>
<dl class="descriptor"><dt>year</dt>
<dd>

<pre class="doc" markdown="0">The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by authoring tools. However, it may occur in a font's info so authoring tools should preserve it if present. This should be a integer</pre>

</dd>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#fontlab.Info-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>


<a name="fontlab.Info.ascender"></a>

## `ascender`


<dl class="descriptor"><dt>fontlab.Info.ascender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.capHeight"></a>

## `capHeight`


<dl class="descriptor"><dt>fontlab.Info.capHeight</dt>
<dd>

<pre class="doc" markdown="0">Cap height value. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.copyright"></a>

## `copyright`


<dl class="descriptor"><dt>fontlab.Info.copyright</dt>
<dd>

<pre class="doc" markdown="0">Copyright statement. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.descender"></a>

## `descender`


<dl class="descriptor"><dt>fontlab.Info.descender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.familyName"></a>

## `familyName`


<dl class="descriptor"><dt>fontlab.Info.familyName</dt>
<dd>

<pre class="doc" markdown="0">Family name. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.italicAngle"></a>

## `italicAngle`


<dl class="descriptor"><dt>fontlab.Info.italicAngle</dt>
<dd>

<pre class="doc" markdown="0">Italic angle. This must be an angle in counter-clockwise degrees from the vertical. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.macintoshFONDFamilyID"></a>

## `macintoshFONDFamilyID`


<dl class="descriptor"><dt>fontlab.Info.macintoshFONDFamilyID</dt>
<dd>

<pre class="doc" markdown="0">Family ID number. Corresponds to the ffFamID in the FOND resource. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.macintoshFONDName"></a>

## `macintoshFONDName`


<dl class="descriptor"><dt>fontlab.Info.macintoshFONDName</dt>
<dd>

<pre class="doc" markdown="0">Font name for the FOND resource. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.note"></a>

## `note`


<dl class="descriptor"><dt>fontlab.Info.note</dt>
<dd>

<pre class="doc" markdown="0">Arbitrary note about the font. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeGaspRangeRecords"></a>

## `openTypeGaspRangeRecords`


<dl class="descriptor"><dt>fontlab.Info.openTypeGaspRangeRecords</dt>
<dd>

<pre class="doc" markdown="0">A list of gasp Range Records. These must be sorted in ascending order based on the rangeMaxPPEM value of the record. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHeadCreated"></a>

## `openTypeHeadCreated`


<dl class="descriptor"><dt>fontlab.Info.openTypeHeadCreated</dt>
<dd>

<pre class="doc" markdown="0">Creation date. Expressed as a string of the format "YYYY/MM/DD HH:MM:SS". "YYYY/MM/DD" is year/month/day. The month must be in the range 1-12 and the day must be in the range 1-end of month. "HH:MM:SS" is hour:minute:second. The hour must be in the range 0:23. The minute and second must each be in the range 0-59. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHeadFlags"></a>

## `openTypeHeadFlags`


<dl class="descriptor"><dt>fontlab.Info.openTypeHeadFlags</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the flags. The bit numbers are listed in the OpenType head specification. Corresponds to the OpenType head table flags field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHeadLowestRecPPEM"></a>

## `openTypeHeadLowestRecPPEM`


<dl class="descriptor"><dt>fontlab.Info.openTypeHeadLowestRecPPEM</dt>
<dd>

<pre class="doc" markdown="0">Smallest readable size in pixels. Corresponds to the OpenType head table lowestRecPPEM field. This should be a non-negative integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaAscender"></a>

## `openTypeHheaAscender`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType hhea table Ascender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaCaretOffset"></a>

## `openTypeHheaCaretOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaCaretOffset</dt>
<dd>

<pre class="doc" markdown="0">Caret offset value. Corresponds to the OpenType hhea table caretOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaCaretSlopeRise"></a>

## `openTypeHheaCaretSlopeRise`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaCaretSlopeRise</dt>
<dd>

<pre class="doc" markdown="0">Caret slope rise value. Corresponds to the OpenType hhea table caretSlopeRise field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaCaretSlopeRun"></a>

## `openTypeHheaCaretSlopeRun`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaCaretSlopeRun</dt>
<dd>

<pre class="doc" markdown="0">Caret slope run value. Corresponds to the OpenType hhea table caretSlopeRun field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaDescender"></a>

## `openTypeHheaDescender`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType hhea table Descender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeHheaLineGap"></a>

## `openTypeHheaLineGap`


<dl class="descriptor"><dt>fontlab.Info.openTypeHheaLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType hhea table LineGap field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameCompatibleFullName"></a>

## `openTypeNameCompatibleFullName`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameCompatibleFullName</dt>
<dd>

<pre class="doc" markdown="0">Compatible full name. Corresponds to the OpenType name table name ID 18. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameDescription"></a>

## `openTypeNameDescription`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameDescription</dt>
<dd>

<pre class="doc" markdown="0">Description of the font. Corresponds to the OpenType name table name ID 10. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameDesigner"></a>

## `openTypeNameDesigner`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameDesigner</dt>
<dd>

<pre class="doc" markdown="0">Designer name. Corresponds to the OpenType name table name ID 9. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameDesignerURL"></a>

## `openTypeNameDesignerURL`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameDesignerURL</dt>
<dd>

<pre class="doc" markdown="0">URL for the designer. Corresponds to the OpenType name table name ID 12. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameLicense"></a>

## `openTypeNameLicense`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameLicense</dt>
<dd>

<pre class="doc" markdown="0">License text. Corresponds to the OpenType name table name ID 13. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameLicenseURL"></a>

## `openTypeNameLicenseURL`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameLicenseURL</dt>
<dd>

<pre class="doc" markdown="0">URL for the license. Corresponds to the OpenType name table name ID 14. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameManufacturer"></a>

## `openTypeNameManufacturer`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameManufacturer</dt>
<dd>

<pre class="doc" markdown="0">Manufacturer name. Corresponds to the OpenType name table name ID 8. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameManufacturerURL"></a>

## `openTypeNameManufacturerURL`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameManufacturerURL</dt>
<dd>

<pre class="doc" markdown="0">Manufacturer URL. Corresponds to the OpenType name table name ID 11. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNamePreferredFamilyName"></a>

## `openTypeNamePreferredFamilyName`


<dl class="descriptor"><dt>fontlab.Info.openTypeNamePreferredFamilyName</dt>
<dd>

<pre class="doc" markdown="0">Preferred family name. Corresponds to the OpenType name table name ID 16. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNamePreferredSubfamilyName"></a>

## `openTypeNamePreferredSubfamilyName`


<dl class="descriptor"><dt>fontlab.Info.openTypeNamePreferredSubfamilyName</dt>
<dd>

<pre class="doc" markdown="0">Preferred subfamily name. Corresponds to the OpenType name table name ID 17. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameRecords"></a>

## `openTypeNameRecords`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameRecords</dt>
<dd>

<pre class="doc" markdown="0">A list of name records. This name record storage area is intended for records that require platform, encoding and or language localization. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameSampleText"></a>

## `openTypeNameSampleText`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameSampleText</dt>
<dd>

<pre class="doc" markdown="0">Sample text. Corresponds to the OpenType name table name ID 19. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameUniqueID"></a>

## `openTypeNameUniqueID`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameUniqueID</dt>
<dd>

<pre class="doc" markdown="0">Unique ID string. Corresponds to the OpenType name table name ID 3. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameVersion"></a>

## `openTypeNameVersion`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameVersion</dt>
<dd>

<pre class="doc" markdown="0">Version string. Corresponds to the OpenType name table name ID 5. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameWWSFamilyName"></a>

## `openTypeNameWWSFamilyName`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameWWSFamilyName</dt>
<dd>

<pre class="doc" markdown="0">WWS family name. Corresponds to the OpenType name table name ID 21. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeNameWWSSubfamilyName"></a>

## `openTypeNameWWSSubfamilyName`


<dl class="descriptor"><dt>fontlab.Info.openTypeNameWWSSubfamilyName</dt>
<dd>

<pre class="doc" markdown="0">WWS Subfamily name. Corresponds to the OpenType name table name ID 22. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2CodePageRanges"></a>

## `openTypeOS2CodePageRanges`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2CodePageRanges</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers that are supported code page ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulCodePageRange1 and ulCodePageRange2 fields. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2FamilyClass"></a>

## `openTypeOS2FamilyClass`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2FamilyClass</dt>
<dd>

<pre class="doc" markdown="0">Two integers representing the IBM font class and font subclass of the font. The first number, representing the class ID, must be in the range 0-14. The second number, representing the subclass, must be in the range 0-15. The numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table sFamilyClass field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2Panose"></a>

## `openTypeOS2Panose`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2Panose</dt>
<dd>

<pre class="doc" markdown="0">The list must contain 10 non-negative integers that represent the setting for each category in the Panose specification. The integers correspond with the option numbers in each of the Panose categories. This corresponds to the OpenType OS/2 table Panose field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2Selection"></a>

## `openTypeOS2Selection`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2Selection</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the bits that should be set in fsSelection. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table selection field. Note: Bits 0 (italic), 5 (bold) and 6 (regular) must not be set here. These bits should be taken from the generic styleMapStyle attribute. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2StrikeoutPosition"></a>

## `openTypeOS2StrikeoutPosition`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2StrikeoutPosition</dt>
<dd>

<pre class="doc" markdown="0">Strikeout position. Corresponds to the OpenType OS/2 table yStrikeoutPosition field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2StrikeoutSize"></a>

## `openTypeOS2StrikeoutSize`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2StrikeoutSize</dt>
<dd>

<pre class="doc" markdown="0">Strikeout size. Corresponds to the OpenType OS/2 table yStrikeoutSize field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SubscriptXOffset"></a>

## `openTypeOS2SubscriptXOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SubscriptXOffset</dt>
<dd>

<pre class="doc" markdown="0">Subscript x offset. Corresponds to the OpenType OS/2 table ySubscriptXOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SubscriptXSize"></a>

## `openTypeOS2SubscriptXSize`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SubscriptXSize</dt>
<dd>

<pre class="doc" markdown="0">Subscript horizontal font size. Corresponds to the OpenType OS/2 table ySubscriptXSize field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SubscriptYOffset"></a>

## `openTypeOS2SubscriptYOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SubscriptYOffset</dt>
<dd>

<pre class="doc" markdown="0">Subscript y offset. Corresponds to the OpenType OS/2 table ySubscriptYOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SubscriptYSize"></a>

## `openTypeOS2SubscriptYSize`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SubscriptYSize</dt>
<dd>

<pre class="doc" markdown="0">Subscript vertical font size. Corresponds to the OpenType OS/2 table ySubscriptYSize field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SuperscriptXOffset"></a>

## `openTypeOS2SuperscriptXOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SuperscriptXOffset</dt>
<dd>

<pre class="doc" markdown="0">Superscript x offset. Corresponds to the OpenType OS/2 table ySuperscriptXOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SuperscriptXSize"></a>

## `openTypeOS2SuperscriptXSize`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SuperscriptXSize</dt>
<dd>

<pre class="doc" markdown="0">Superscript horizontal font size. Corresponds to the OpenType OS/2 table ySuperscriptXSize field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SuperscriptYOffset"></a>

## `openTypeOS2SuperscriptYOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SuperscriptYOffset</dt>
<dd>

<pre class="doc" markdown="0">Superscript y offset. Corresponds to the OpenType OS/2 table ySuperscriptYOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2SuperscriptYSize"></a>

## `openTypeOS2SuperscriptYSize`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2SuperscriptYSize</dt>
<dd>

<pre class="doc" markdown="0">Superscript vertical font size. Corresponds to the OpenType OS/2 table ySuperscriptYSize field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2Type"></a>

## `openTypeOS2Type`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2Type</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers indicating the embedding type. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table fsType field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2TypoAscender"></a>

## `openTypeOS2TypoAscender`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2TypoAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType OS/2 table sTypoAscender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2TypoDescender"></a>

## `openTypeOS2TypoDescender`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2TypoDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType OS/2 table sTypoDescender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2TypoLineGap"></a>

## `openTypeOS2TypoLineGap`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2TypoLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType OS/2 table sTypoLineGap field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2UnicodeRanges"></a>

## `openTypeOS2UnicodeRanges`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2UnicodeRanges</dt>
<dd>

<pre class="doc" markdown="0">A list of bit numbers that are supported Unicode ranges in the font. The bit numbers are listed in the OpenType OS/2 specification. Corresponds to the OpenType OS/2 table ulUnicodeRange1, ulUnicodeRange2, ulUnicodeRange3 and ulUnicodeRange4 fields. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2VendorID"></a>

## `openTypeOS2VendorID`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2VendorID</dt>
<dd>

<pre class="doc" markdown="0">Four character identifier for the creator of the font. Corresponds to the OpenType OS/2 table achVendID field. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2WeightClass"></a>

## `openTypeOS2WeightClass`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2WeightClass</dt>
<dd>

<pre class="doc" markdown="0">Weight class value. Must be a non-negative integer. Corresponds to the OpenType OS/2 table usWeightClass field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2WidthClass"></a>

## `openTypeOS2WidthClass`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2WidthClass</dt>
<dd>

<pre class="doc" markdown="0">Width class value. Must be in the range 1-9. Corresponds to the OpenType OS/2 table usWidthClass field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2WinAscent"></a>

## `openTypeOS2WinAscent`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2WinAscent</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType OS/2 table usWinAscent field. This should be a non-negative integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeOS2WinDescent"></a>

## `openTypeOS2WinDescent`


<dl class="descriptor"><dt>fontlab.Info.openTypeOS2WinDescent</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType OS/2 table usWinDescent field. This should be a non-negative integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaCaretOffset"></a>

## `openTypeVheaCaretOffset`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaCaretOffset</dt>
<dd>

<pre class="doc" markdown="0">Caret offset value. Corresponds to the OpenType vhea table caretOffset field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaCaretSlopeRise"></a>

## `openTypeVheaCaretSlopeRise`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaCaretSlopeRise</dt>
<dd>

<pre class="doc" markdown="0">Caret slope rise value. Corresponds to the OpenType vhea table caretSlopeRise field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaCaretSlopeRun"></a>

## `openTypeVheaCaretSlopeRun`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaCaretSlopeRun</dt>
<dd>

<pre class="doc" markdown="0">Caret slope run value. Corresponds to the OpenType vhea table caretSlopeRun field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaVertTypoAscender"></a>

## `openTypeVheaVertTypoAscender`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaVertTypoAscender</dt>
<dd>

<pre class="doc" markdown="0">Ascender value. Corresponds to the OpenType vhea table vertTypoAscender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaVertTypoDescender"></a>

## `openTypeVheaVertTypoDescender`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaVertTypoDescender</dt>
<dd>

<pre class="doc" markdown="0">Descender value. Corresponds to the OpenType vhea table vertTypoDescender field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.openTypeVheaVertTypoLineGap"></a>

## `openTypeVheaVertTypoLineGap`


<dl class="descriptor"><dt>fontlab.Info.openTypeVheaVertTypoLineGap</dt>
<dd>

<pre class="doc" markdown="0">Line gap value. Corresponds to the OpenType vhea table vertTypoLineGap field. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.panose"></a>

## `panose`


<dl class="descriptor"><dt>fontlab.Info.panose</dt>
<dd>

<pre class="doc" markdown="0">PANOSE identification. Should be a string containing 10 space-separated numbers</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptBlueFuzz"></a>

## `postscriptBlueFuzz`


<dl class="descriptor"><dt>fontlab.Info.postscriptBlueFuzz</dt>
<dd>

<pre class="doc" markdown="0">BlueFuzz value. This corresponds to the Type 1/CFF BlueFuzz field. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptBlueScale"></a>

## `postscriptBlueScale`


<dl class="descriptor"><dt>fontlab.Info.postscriptBlueScale</dt>
<dd>

<pre class="doc" markdown="0">BlueScale value. This corresponds to the Type 1/CFF BlueScale field. This should be a float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptBlueShift"></a>

## `postscriptBlueShift`


<dl class="descriptor"><dt>fontlab.Info.postscriptBlueShift</dt>
<dd>

<pre class="doc" markdown="0">BlueShift value. This corresponds to the Type 1/CFF BlueShift field. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptBlueValues"></a>

## `postscriptBlueValues`


<dl class="descriptor"><dt>fontlab.Info.postscriptBlueValues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF BlueValues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptDefaultCharacter"></a>

## `postscriptDefaultCharacter`


<dl class="descriptor"><dt>fontlab.Info.postscriptDefaultCharacter</dt>
<dd>

<pre class="doc" markdown="0">The name of the glyph that should be used as the default character in PFM files. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptDefaultWidthX"></a>

## `postscriptDefaultWidthX`


<dl class="descriptor"><dt>fontlab.Info.postscriptDefaultWidthX</dt>
<dd>

<pre class="doc" markdown="0">Default width for glyphs. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptFamilyBlues"></a>

## `postscriptFamilyBlues`


<dl class="descriptor"><dt>fontlab.Info.postscriptFamilyBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 14 integers or floats specifying the values that should be in the Type 1/CFF FamilyBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptFamilyOtherBlues"></a>

## `postscriptFamilyOtherBlues`


<dl class="descriptor"><dt>fontlab.Info.postscriptFamilyOtherBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF FamilyOtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptFontName"></a>

## `postscriptFontName`


<dl class="descriptor"><dt>fontlab.Info.postscriptFontName</dt>
<dd>

<pre class="doc" markdown="0">Name to be used for the FontName field in Type 1/CFF table. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptForceBold"></a>

## `postscriptForceBold`


<dl class="descriptor"><dt>fontlab.Info.postscriptForceBold</dt>
<dd>

<pre class="doc" markdown="0">Indicates how the Type 1/CFF ForceBold field should be set. This should be a boolean</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptFullName"></a>

## `postscriptFullName`


<dl class="descriptor"><dt>fontlab.Info.postscriptFullName</dt>
<dd>

<pre class="doc" markdown="0">Name to be used for the FullName field in Type 1/CFF table. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptIsFixedPitch"></a>

## `postscriptIsFixedPitch`


<dl class="descriptor"><dt>fontlab.Info.postscriptIsFixedPitch</dt>
<dd>

<pre class="doc" markdown="0">Indicates if the font is monospaced. An authoring tool could calculate this automatically, but the designer may wish to override this setting. This corresponds to the Type 1/CFF isFixedPitched field This should be a boolean</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptNominalWidthX"></a>

## `postscriptNominalWidthX`


<dl class="descriptor"><dt>fontlab.Info.postscriptNominalWidthX</dt>
<dd>

<pre class="doc" markdown="0">Nominal width for glyphs. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptOtherBlues"></a>

## `postscriptOtherBlues`


<dl class="descriptor"><dt>fontlab.Info.postscriptOtherBlues</dt>
<dd>

<pre class="doc" markdown="0">A list of up to 10 integers or floats specifying the values that should be in the Type 1/CFF OtherBlues field. This list must contain an even number of integers following the rules defined in the Type 1/CFF specification. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptStemSnapH"></a>

## `postscriptStemSnapH`


<dl class="descriptor"><dt>fontlab.Info.postscriptStemSnapH</dt>
<dd>

<pre class="doc" markdown="0">List of horizontal stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapH field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptStemSnapV"></a>

## `postscriptStemSnapV`


<dl class="descriptor"><dt>fontlab.Info.postscriptStemSnapV</dt>
<dd>

<pre class="doc" markdown="0">List of vertical stems sorted in the order specified in the Type 1/CFF specification. Up to 12 integers or floats are possible. This corresponds to the Type 1/CFF StemSnapV field. This should be a list</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptUnderlinePosition"></a>

## `postscriptUnderlinePosition`


<dl class="descriptor"><dt>fontlab.Info.postscriptUnderlinePosition</dt>
<dd>

<pre class="doc" markdown="0">Underline position value. Corresponds to the Type 1/CFF/post table UnderlinePosition field. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptUnderlineThickness"></a>

## `postscriptUnderlineThickness`


<dl class="descriptor"><dt>fontlab.Info.postscriptUnderlineThickness</dt>
<dd>

<pre class="doc" markdown="0">Underline thickness value. Corresponds to the Type 1/CFF/post table UnderlineThickness field. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptUniqueID"></a>

## `postscriptUniqueID`


<dl class="descriptor"><dt>fontlab.Info.postscriptUniqueID</dt>
<dd>

<pre class="doc" markdown="0">A unique ID number as defined in the Type 1/CFF specification. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptWeightName"></a>

## `postscriptWeightName`


<dl class="descriptor"><dt>fontlab.Info.postscriptWeightName</dt>
<dd>

<pre class="doc" markdown="0">A string indicating the overall weight of the font. This corresponds to the Type 1/CFF Weight field. It should be in sync with the openTypeOS2WeightClass value. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.postscriptWindowsCharacterSet"></a>

## `postscriptWindowsCharacterSet`


<dl class="descriptor"><dt>fontlab.Info.postscriptWindowsCharacterSet</dt>
<dd>

<pre class="doc" markdown="0">The Windows character set. The values are defined below. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.styleMapFamilyName"></a>

## `styleMapFamilyName`


<dl class="descriptor"><dt>fontlab.Info.styleMapFamilyName</dt>
<dd>

<pre class="doc" markdown="0">Family name used for bold, italic and bold italic style mapping. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.styleMapStyleName"></a>

## `styleMapStyleName`


<dl class="descriptor"><dt>fontlab.Info.styleMapStyleName</dt>
<dd>

<pre class="doc" markdown="0">Style map style. The possible values are regular, italic, bold and bold italic. These are case sensitive. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.styleName"></a>

## `styleName`


<dl class="descriptor"><dt>fontlab.Info.styleName</dt>
<dd>

<pre class="doc" markdown="0">Style name. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.trademark"></a>

## `trademark`


<dl class="descriptor"><dt>fontlab.Info.trademark</dt>
<dd>

<pre class="doc" markdown="0">Trademark statement. This should be a string</pre>

</dd>
</dl>



<a name="fontlab.Info.unitsPerEm"></a>

## `unitsPerEm`


<dl class="descriptor"><dt>fontlab.Info.unitsPerEm</dt>
<dd>

<pre class="doc" markdown="0">Units per em. This should be a non-negative integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.versionMajor"></a>

## `versionMajor`


<dl class="descriptor"><dt>fontlab.Info.versionMajor</dt>
<dd>

<pre class="doc" markdown="0">Major version. This should be a integer</pre>

</dd>
</dl>



<a name="fontlab.Info.versionMinor"></a>

## `versionMinor`


<dl class="descriptor"><dt>fontlab.Info.versionMinor</dt>
<dd>

<pre class="doc" markdown="0">Minor version. This should be a non-negative integer</pre>

</dd>
</dl>



<a name="fontlab.Info.xHeight"></a>

## `xHeight`


<dl class="descriptor"><dt>fontlab.Info.xHeight</dt>
<dd>

<pre class="doc" markdown="0">x-height value. This should be a integer or float</pre>

</dd>
</dl>



<a name="fontlab.Info.year"></a>

## `year`


<dl class="descriptor"><dt>fontlab.Info.year</dt>
<dd>

<pre class="doc" markdown="0">The year the font was created. This attribute is deprecated as of version 2. It's presence should not be relied upon by authoring tools. However, it may occur in a font's info so authoring tools should preserve it if present. This should be a integer</pre>

</dd>
</dl>

