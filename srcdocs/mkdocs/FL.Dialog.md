

<a name="FL.Dialog"></a>

# `Dialog`


<dt class="class"><h2><span class="class-name">FL.Dialog</span> = <a name="FL.Dialog" href="#FL.Dialog">class Dialog</a>(<a href="./__builtin__.html#object">object</a>)</h2></dt><dd class="class"><dd>


<pre class="doc" markdown="0">===============================================
  Dialog - class to represent Dialog
===============================================
Note that objects of this class cannot be created explicitly, they are only generated as a result of Glyph().Audit() operation

CONSTRUCTOR:
  Dialog(DialogClass) - generic constructor

ATTRIBUTES:
  title - dialog title
  ok - text on the OK button
  cancel - text on the Cancel button
  position - position of the dialog's origin
  size - dialog size
  rectangle (combination of size and position)

OPERATIONS:

METHODS
  Center()                    - center dialog on screen
  AddControl(integer ControlType, Rect dimension, string identifier, integer ControlStyle)
                              - adds a control to the dialog, see FLdict for
                                Type- and Style-constants
  GetValue(string identifier) - get value from the specified control
  PutValue(string identifier) - put value to the specified control
  Enable(string identifier, integer value)
                              - enable (value=1) or disable (value=0) the specified control
  Show(string identifier, integer value)
                              - show (value=1) or hide (value=0) the specified control
  SetLabel(string identifier, string value)
                              - set the label of the specified control
  GetRect(string identifier)  - get dimension of the specified control as a Rect object
  Repaint(string identifier)  - redraw the specified (custom)control
  Run()                       - run the dialog
  End()|End(integer returnvalue) - end the dialog</pre>


</dd><h4 class="head-methods">Methods </h4><dl class="function"><dt><a name="Dialog-AddControl" href="#Dialog-AddControl"><span class="function-name">AddControl</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-Center" href="#Dialog-Center"><span class="function-name">Center</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-Enable" href="#Dialog-Enable"><span class="function-name">Enable</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-End" href="#Dialog-End"><span class="function-name">End</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-GetRect" href="#Dialog-GetRect"><span class="function-name">GetRect</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-GetValue" href="#Dialog-GetValue"><span class="function-name">GetValue</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-MoveTo" href="#Dialog-MoveTo"><span class="function-name">MoveTo</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-PutValue" href="#Dialog-PutValue"><span class="function-name">PutValue</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-Repaint" href="#Dialog-Repaint"><span class="function-name">Repaint</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-Run" href="#Dialog-Run"><span class="function-name">Run</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-SetLabel" href="#Dialog-SetLabel"><span class="function-name">SetLabel</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-Show" href="#Dialog-Show"><span class="function-name">Show</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"></pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-__delattr__" href="#Dialog-__delattr__"><span class="function-name">__delattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Dialog-__delattr__">__delattr__</a>('name') <==> del x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-__getattribute__" href="#Dialog-__getattribute__"><span class="function-name">__getattribute__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Dialog-__getattribute__">__getattribute__</a>('name') <==> x.name</pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-__init__" href="#Dialog-__init__"><span class="function-name">__init__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Dialog-__init__">__init__</a>(...) initializes x; see help(type(x)) for signature</pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-__repr__" href="#Dialog-__repr__"><span class="function-name">__repr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Dialog-__repr__">__repr__</a>() <==> repr(x)</pre>

</dd></dl>
<dl class="function"><dt><a name="Dialog-__setattr__" href="#Dialog-__setattr__"><span class="function-name">__setattr__</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">x.<a href="#FL.Dialog-__setattr__">__setattr__</a>('name', value) <==> x.name = value</pre>

</dd></dl>

  <h4 class="head-desc">Descriptors </h4><dl class="descriptor"><dt>cancel</dt>
</dl>
<dl class="descriptor"><dt>ok</dt>
</dl>
<dl class="descriptor"><dt>position</dt>
</dl>
<dl class="descriptor"><dt>rectangle</dt>
</dl>
<dl class="descriptor"><dt>size</dt>
</dl>
<dl class="descriptor"><dt>title</dt>
</dl>

  <h4 class="head-attrs">Attributes </h4><dl><dt><span class="other-name">__new__</span> = &lt;built-in method __new__ of type object&gt;<dd>

<pre class="doc" markdown="0">T.<a href="#FL.Dialog-__new__">__new__</a>(S, ...) -> a new object with type S, a subtype of T</pre>

</dd></dl>
</dd>
