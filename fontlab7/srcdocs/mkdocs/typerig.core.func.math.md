

<a name="typerig.core.func.math"></a>

# `math`


<h2>math</h2> <a class="official-docs" href="https://docs.python.org/library/math" target="_blank" rel="noreferrer noopener">Module Docs</a><div class="module">  <div class="docstring">

<pre class="doc" markdown="0">This module is always available.  It provides access to the
mathematical functions defined by the C standard.</pre>

</div>  <div class="functions"><h3>Functions</h3><dl class="functions"><dl class="function"><dt><a name="-acos" href="#-acos"><span class="function-name">acos</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-acos">acos</a>(x)

Return the arc cosine (measured in radians) of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-acosh" href="#-acosh"><span class="function-name">acosh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-acosh">acosh</a>(x)

Return the inverse hyperbolic cosine of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-asin" href="#-asin"><span class="function-name">asin</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-asin">asin</a>(x)

Return the arc sine (measured in radians) of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-asinh" href="#-asinh"><span class="function-name">asinh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-asinh">asinh</a>(x)

Return the inverse hyperbolic sine of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-atan" href="#-atan"><span class="function-name">atan</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-atan">atan</a>(x)

Return the arc tangent (measured in radians) of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-atan2" href="#-atan2"><span class="function-name">atan2</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-atan2">atan2</a>(y, x)

Return the arc tangent (measured in radians) of y/x.
Unlike <a href="#-atan">atan</a>(y/x), the signs of both x and y are considered.</pre>

</dd></dl>

<dl class="function"><dt><a name="-atanh" href="#-atanh"><span class="function-name">atanh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-atanh">atanh</a>(x)

Return the inverse hyperbolic tangent of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-ceil" href="#-ceil"><span class="function-name">ceil</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-ceil">ceil</a>(x)

Return the ceiling of x as a float.
This is the smallest integral value >= x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-copysign" href="#-copysign"><span class="function-name">copysign</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-copysign">copysign</a>(x, y)

Return x with the sign of y.</pre>

</dd></dl>

<dl class="function"><dt><a name="-cos" href="#-cos"><span class="function-name">cos</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-cos">cos</a>(x)

Return the cosine of x (measured in radians).</pre>

</dd></dl>

<dl class="function"><dt><a name="-cosh" href="#-cosh"><span class="function-name">cosh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-cosh">cosh</a>(x)

Return the hyperbolic cosine of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-degrees" href="#-degrees"><span class="function-name">degrees</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-degrees">degrees</a>(x)

Convert angle x from radians to degrees.</pre>

</dd></dl>

<dl class="function"><dt><a name="-erf" href="#-erf"><span class="function-name">erf</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-erf">erf</a>(x)

Error function at x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-erfc" href="#-erfc"><span class="function-name">erfc</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-erfc">erfc</a>(x)

Complementary error function at x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-exp" href="#-exp"><span class="function-name">exp</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-exp">exp</a>(x)

Return e raised to the power of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-expm1" href="#-expm1"><span class="function-name">expm1</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-expm1">expm1</a>(x)

Return <a href="#-exp">exp</a>(x)-1.
This function avoids the loss of precision involved in the direct evaluation of <a href="#-exp">exp</a>(x)-1 for small x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-fabs" href="#-fabs"><span class="function-name">fabs</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-fabs">fabs</a>(x)

Return the absolute value of the float x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-factorial" href="#-factorial"><span class="function-name">factorial</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-factorial">factorial</a>(x) -> Integral

Find x!. Raise a ValueError if x is negative or non-integral.</pre>

</dd></dl>

<dl class="function"><dt><a name="-floor" href="#-floor"><span class="function-name">floor</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-floor">floor</a>(x)

Return the floor of x as a float.
This is the largest integral value <= x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-fmod" href="#-fmod"><span class="function-name">fmod</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-fmod">fmod</a>(x, y)

Return <a href="#-fmod">fmod</a>(x, y), according to platform C.  x % y may differ.</pre>

</dd></dl>

<dl class="function"><dt><a name="-frexp" href="#-frexp"><span class="function-name">frexp</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-frexp">frexp</a>(x)

Return the mantissa and exponent of x, as pair (m, e).
m is a float and e is an int, such that x = m * 2.**e.
If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.</pre>

</dd></dl>

<dl class="function"><dt><a name="-fsum" href="#-fsum"><span class="function-name">fsum</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-fsum">fsum</a>(iterable)

Return an accurate floating point sum of values in the iterable.
Assumes IEEE-754 floating point arithmetic.</pre>

</dd></dl>

<dl class="function"><dt><a name="-gamma" href="#-gamma"><span class="function-name">gamma</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-gamma">gamma</a>(x)

Gamma function at x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-hypot" href="#-hypot"><span class="function-name">hypot</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-hypot">hypot</a>(x, y)

Return the Euclidean distance, <a href="#-sqrt">sqrt</a>(x*x + y*y).</pre>

</dd></dl>

<dl class="function"><dt><a name="-isinf" href="#-isinf"><span class="function-name">isinf</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-isinf">isinf</a>(x) -> bool

Check if float x is infinite (positive or negative).</pre>

</dd></dl>

<dl class="function"><dt><a name="-isnan" href="#-isnan"><span class="function-name">isnan</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-isnan">isnan</a>(x) -> bool

Check if float x is not a number (NaN).</pre>

</dd></dl>

<dl class="function"><dt><a name="-ldexp" href="#-ldexp"><span class="function-name">ldexp</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-ldexp">ldexp</a>(x, i)

Return x * (2**i).</pre>

</dd></dl>

<dl class="function"><dt><a name="-lgamma" href="#-lgamma"><span class="function-name">lgamma</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-lgamma">lgamma</a>(x)

Natural logarithm of absolute value of Gamma function at x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-log" href="#-log"><span class="function-name">log</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-log">log</a>(x[, base])

Return the logarithm of x to the given base.
If the base not specified, returns the natural logarithm (base e) of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-log10" href="#-log10"><span class="function-name">log10</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-log10">log10</a>(x)

Return the base 10 logarithm of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-log1p" href="#-log1p"><span class="function-name">log1p</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-log1p">log1p</a>(x)

Return the natural logarithm of 1+x (base e).
The result is computed in a way which is accurate for x near zero.</pre>

</dd></dl>

<dl class="function"><dt><a name="-modf" href="#-modf"><span class="function-name">modf</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-modf">modf</a>(x)

Return the fractional and integer parts of x.  Both results carry the sign
of x and are floats.</pre>

</dd></dl>

<dl class="function"><dt><a name="-pow" href="#-pow"><span class="function-name">pow</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-pow">pow</a>(x, y)

Return x**y (x to the power of y).</pre>

</dd></dl>

<dl class="function"><dt><a name="-radians" href="#-radians"><span class="function-name">radians</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-radians">radians</a>(x)

Convert angle x from degrees to radians.</pre>

</dd></dl>

<dl class="function"><dt><a name="-sin" href="#-sin"><span class="function-name">sin</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-sin">sin</a>(x)

Return the sine of x (measured in radians).</pre>

</dd></dl>

<dl class="function"><dt><a name="-sinh" href="#-sinh"><span class="function-name">sinh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-sinh">sinh</a>(x)

Return the hyperbolic sine of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-sqrt" href="#-sqrt"><span class="function-name">sqrt</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-sqrt">sqrt</a>(x)

Return the square root of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-tan" href="#-tan"><span class="function-name">tan</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-tan">tan</a>(x)

Return the tangent of x (measured in radians).</pre>

</dd></dl>

<dl class="function"><dt><a name="-tanh" href="#-tanh"><span class="function-name">tanh</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-tanh">tanh</a>(x)

Return the hyperbolic tangent of x.</pre>

</dd></dl>

<dl class="function"><dt><a name="-trunc" href="#-trunc"><span class="function-name">trunc</span></a><span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0"><a href="#-trunc">trunc</a>(x:Real) -> Integral

Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.</pre>

</dd></dl>
</dl></div></div>


<a name="typerig.core.func.math.acos"></a>

## `acos`


<dl class="function"><dt><a name="-typerig.core.func.math.acos" href="#-typerig.core.func.math.acos"><span class="function-name">typerig.core.func.math.acos</span></a> = acos<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">acos(x)

Return the arc cosine (measured in radians) of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.acosh"></a>

## `acosh`


<dl class="function"><dt><a name="-typerig.core.func.math.acosh" href="#-typerig.core.func.math.acosh"><span class="function-name">typerig.core.func.math.acosh</span></a> = acosh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">acosh(x)

Return the inverse hyperbolic cosine of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.asin"></a>

## `asin`


<dl class="function"><dt><a name="-typerig.core.func.math.asin" href="#-typerig.core.func.math.asin"><span class="function-name">typerig.core.func.math.asin</span></a> = asin<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">asin(x)

Return the arc sine (measured in radians) of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.asinh"></a>

## `asinh`


<dl class="function"><dt><a name="-typerig.core.func.math.asinh" href="#-typerig.core.func.math.asinh"><span class="function-name">typerig.core.func.math.asinh</span></a> = asinh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">asinh(x)

Return the inverse hyperbolic sine of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.atan"></a>

## `atan`


<dl class="function"><dt><a name="-typerig.core.func.math.atan" href="#-typerig.core.func.math.atan"><span class="function-name">typerig.core.func.math.atan</span></a> = atan<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">atan(x)

Return the arc tangent (measured in radians) of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.atan2"></a>

## `atan2`


<dl class="function"><dt><a name="-typerig.core.func.math.atan2" href="#-typerig.core.func.math.atan2"><span class="function-name">typerig.core.func.math.atan2</span></a> = atan2<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">atan2(y, x)

Return the arc tangent (measured in radians) of y/x.
Unlike atan(y/x), the signs of both x and y are considered.</pre>

</dd></dl>



<a name="typerig.core.func.math.atanh"></a>

## `atanh`


<dl class="function"><dt><a name="-typerig.core.func.math.atanh" href="#-typerig.core.func.math.atanh"><span class="function-name">typerig.core.func.math.atanh</span></a> = atanh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">atanh(x)

Return the inverse hyperbolic tangent of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.ceil"></a>

## `ceil`


<dl class="function"><dt><a name="-typerig.core.func.math.ceil" href="#-typerig.core.func.math.ceil"><span class="function-name">typerig.core.func.math.ceil</span></a> = ceil<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">ceil(x)

Return the ceiling of x as a float.
This is the smallest integral value >= x.</pre>

</dd></dl>



<a name="typerig.core.func.math.copysign"></a>

## `copysign`


<dl class="function"><dt><a name="-typerig.core.func.math.copysign" href="#-typerig.core.func.math.copysign"><span class="function-name">typerig.core.func.math.copysign</span></a> = copysign<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">copysign(x, y)

Return x with the sign of y.</pre>

</dd></dl>



<a name="typerig.core.func.math.cos"></a>

## `cos`


<dl class="function"><dt><a name="-typerig.core.func.math.cos" href="#-typerig.core.func.math.cos"><span class="function-name">typerig.core.func.math.cos</span></a> = cos<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">cos(x)

Return the cosine of x (measured in radians).</pre>

</dd></dl>



<a name="typerig.core.func.math.cosh"></a>

## `cosh`


<dl class="function"><dt><a name="-typerig.core.func.math.cosh" href="#-typerig.core.func.math.cosh"><span class="function-name">typerig.core.func.math.cosh</span></a> = cosh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">cosh(x)

Return the hyperbolic cosine of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.degrees"></a>

## `degrees`


<dl class="function"><dt><a name="-typerig.core.func.math.degrees" href="#-typerig.core.func.math.degrees"><span class="function-name">typerig.core.func.math.degrees</span></a> = degrees<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">degrees(x)

Convert angle x from radians to degrees.</pre>

</dd></dl>



<a name="typerig.core.func.math.erf"></a>

## `erf`


<dl class="function"><dt><a name="-typerig.core.func.math.erf" href="#-typerig.core.func.math.erf"><span class="function-name">typerig.core.func.math.erf</span></a> = erf<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">erf(x)

Error function at x.</pre>

</dd></dl>



<a name="typerig.core.func.math.erfc"></a>

## `erfc`


<dl class="function"><dt><a name="-typerig.core.func.math.erfc" href="#-typerig.core.func.math.erfc"><span class="function-name">typerig.core.func.math.erfc</span></a> = erfc<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">erfc(x)

Complementary error function at x.</pre>

</dd></dl>



<a name="typerig.core.func.math.exp"></a>

## `exp`


<dl class="function"><dt><a name="-typerig.core.func.math.exp" href="#-typerig.core.func.math.exp"><span class="function-name">typerig.core.func.math.exp</span></a> = exp<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">exp(x)

Return e raised to the power of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.expm1"></a>

## `expm1`


<dl class="function"><dt><a name="-typerig.core.func.math.expm1" href="#-typerig.core.func.math.expm1"><span class="function-name">typerig.core.func.math.expm1</span></a> = expm1<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">expm1(x)

Return exp(x)-1.
This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.</pre>

</dd></dl>



<a name="typerig.core.func.math.fabs"></a>

## `fabs`


<dl class="function"><dt><a name="-typerig.core.func.math.fabs" href="#-typerig.core.func.math.fabs"><span class="function-name">typerig.core.func.math.fabs</span></a> = fabs<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fabs(x)

Return the absolute value of the float x.</pre>

</dd></dl>



<a name="typerig.core.func.math.factorial"></a>

## `factorial`


<dl class="function"><dt><a name="-typerig.core.func.math.factorial" href="#-typerig.core.func.math.factorial"><span class="function-name">typerig.core.func.math.factorial</span></a> = factorial<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">factorial(x) -> Integral

Find x!. Raise a ValueError if x is negative or non-integral.</pre>

</dd></dl>



<a name="typerig.core.func.math.floor"></a>

## `floor`


<dl class="function"><dt><a name="-typerig.core.func.math.floor" href="#-typerig.core.func.math.floor"><span class="function-name">typerig.core.func.math.floor</span></a> = floor<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">floor(x)

Return the floor of x as a float.
This is the largest integral value <= x.</pre>

</dd></dl>



<a name="typerig.core.func.math.fmod"></a>

## `fmod`


<dl class="function"><dt><a name="-typerig.core.func.math.fmod" href="#-typerig.core.func.math.fmod"><span class="function-name">typerig.core.func.math.fmod</span></a> = fmod<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fmod(x, y)

Return fmod(x, y), according to platform C.  x % y may differ.</pre>

</dd></dl>



<a name="typerig.core.func.math.frexp"></a>

## `frexp`


<dl class="function"><dt><a name="-typerig.core.func.math.frexp" href="#-typerig.core.func.math.frexp"><span class="function-name">typerig.core.func.math.frexp</span></a> = frexp<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">frexp(x)

Return the mantissa and exponent of x, as pair (m, e).
m is a float and e is an int, such that x = m * 2.**e.
If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.</pre>

</dd></dl>



<a name="typerig.core.func.math.fsum"></a>

## `fsum`


<dl class="function"><dt><a name="-typerig.core.func.math.fsum" href="#-typerig.core.func.math.fsum"><span class="function-name">typerig.core.func.math.fsum</span></a> = fsum<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">fsum(iterable)

Return an accurate floating point sum of values in the iterable.
Assumes IEEE-754 floating point arithmetic.</pre>

</dd></dl>



<a name="typerig.core.func.math.gamma"></a>

## `gamma`


<dl class="function"><dt><a name="-typerig.core.func.math.gamma" href="#-typerig.core.func.math.gamma"><span class="function-name">typerig.core.func.math.gamma</span></a> = gamma<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">gamma(x)

Gamma function at x.</pre>

</dd></dl>



<a name="typerig.core.func.math.hypot"></a>

## `hypot`


<dl class="function"><dt><a name="-typerig.core.func.math.hypot" href="#-typerig.core.func.math.hypot"><span class="function-name">typerig.core.func.math.hypot</span></a> = hypot<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">hypot(x, y)

Return the Euclidean distance, sqrt(x*x + y*y).</pre>

</dd></dl>



<a name="typerig.core.func.math.isinf"></a>

## `isinf`


<dl class="function"><dt><a name="-typerig.core.func.math.isinf" href="#-typerig.core.func.math.isinf"><span class="function-name">typerig.core.func.math.isinf</span></a> = isinf<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isinf(x) -> bool

Check if float x is infinite (positive or negative).</pre>

</dd></dl>



<a name="typerig.core.func.math.isnan"></a>

## `isnan`


<dl class="function"><dt><a name="-typerig.core.func.math.isnan" href="#-typerig.core.func.math.isnan"><span class="function-name">typerig.core.func.math.isnan</span></a> = isnan<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">isnan(x) -> bool

Check if float x is not a number (NaN).</pre>

</dd></dl>



<a name="typerig.core.func.math.ldexp"></a>

## `ldexp`


<dl class="function"><dt><a name="-typerig.core.func.math.ldexp" href="#-typerig.core.func.math.ldexp"><span class="function-name">typerig.core.func.math.ldexp</span></a> = ldexp<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">ldexp(x, i)

Return x * (2**i).</pre>

</dd></dl>



<a name="typerig.core.func.math.lgamma"></a>

## `lgamma`


<dl class="function"><dt><a name="-typerig.core.func.math.lgamma" href="#-typerig.core.func.math.lgamma"><span class="function-name">typerig.core.func.math.lgamma</span></a> = lgamma<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">lgamma(x)

Natural logarithm of absolute value of Gamma function at x.</pre>

</dd></dl>



<a name="typerig.core.func.math.log"></a>

## `log`


<dl class="function"><dt><a name="-typerig.core.func.math.log" href="#-typerig.core.func.math.log"><span class="function-name">typerig.core.func.math.log</span></a> = log<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">log(x[, base])

Return the logarithm of x to the given base.
If the base not specified, returns the natural logarithm (base e) of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.log10"></a>

## `log10`


<dl class="function"><dt><a name="-typerig.core.func.math.log10" href="#-typerig.core.func.math.log10"><span class="function-name">typerig.core.func.math.log10</span></a> = log10<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">log10(x)

Return the base 10 logarithm of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.log1p"></a>

## `log1p`


<dl class="function"><dt><a name="-typerig.core.func.math.log1p" href="#-typerig.core.func.math.log1p"><span class="function-name">typerig.core.func.math.log1p</span></a> = log1p<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">log1p(x)

Return the natural logarithm of 1+x (base e).
The result is computed in a way which is accurate for x near zero.</pre>

</dd></dl>



<a name="typerig.core.func.math.modf"></a>

## `modf`


<dl class="function"><dt><a name="-typerig.core.func.math.modf" href="#-typerig.core.func.math.modf"><span class="function-name">typerig.core.func.math.modf</span></a> = modf<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">modf(x)

Return the fractional and integer parts of x.  Both results carry the sign
of x and are floats.</pre>

</dd></dl>



<a name="typerig.core.func.math.pow"></a>

## `pow`


<dl class="function"><dt><a name="-typerig.core.func.math.pow" href="#-typerig.core.func.math.pow"><span class="function-name">typerig.core.func.math.pow</span></a> = pow<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">pow(x, y)

Return x**y (x to the power of y).</pre>

</dd></dl>



<a name="typerig.core.func.math.radians"></a>

## `radians`


<dl class="function"><dt><a name="-typerig.core.func.math.radians" href="#-typerig.core.func.math.radians"><span class="function-name">typerig.core.func.math.radians</span></a> = radians<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">radians(x)

Convert angle x from degrees to radians.</pre>

</dd></dl>



<a name="typerig.core.func.math.sin"></a>

## `sin`


<dl class="function"><dt><a name="-typerig.core.func.math.sin" href="#-typerig.core.func.math.sin"><span class="function-name">typerig.core.func.math.sin</span></a> = sin<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">sin(x)

Return the sine of x (measured in radians).</pre>

</dd></dl>



<a name="typerig.core.func.math.sinh"></a>

## `sinh`


<dl class="function"><dt><a name="-typerig.core.func.math.sinh" href="#-typerig.core.func.math.sinh"><span class="function-name">typerig.core.func.math.sinh</span></a> = sinh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">sinh(x)

Return the hyperbolic sine of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.sqrt"></a>

## `sqrt`


<dl class="function"><dt><a name="-typerig.core.func.math.sqrt" href="#-typerig.core.func.math.sqrt"><span class="function-name">typerig.core.func.math.sqrt</span></a> = sqrt<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">sqrt(x)

Return the square root of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.tan"></a>

## `tan`


<dl class="function"><dt><a name="-typerig.core.func.math.tan" href="#-typerig.core.func.math.tan"><span class="function-name">typerig.core.func.math.tan</span></a> = tan<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tan(x)

Return the tangent of x (measured in radians).</pre>

</dd></dl>



<a name="typerig.core.func.math.tanh"></a>

## `tanh`


<dl class="function"><dt><a name="-typerig.core.func.math.tanh" href="#-typerig.core.func.math.tanh"><span class="function-name">typerig.core.func.math.tanh</span></a> = tanh<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">tanh(x)

Return the hyperbolic tangent of x.</pre>

</dd></dl>



<a name="typerig.core.func.math.trunc"></a>

## `trunc`


<dl class="function"><dt><a name="-typerig.core.func.math.trunc" href="#-typerig.core.func.math.trunc"><span class="function-name">typerig.core.func.math.trunc</span></a> = trunc<span class="argspec">(...)</span></dt><dd>

<pre class="doc" markdown="0">trunc(x:Real) -> Integral

Truncates x to the nearest Integral toward 0. Uses the __trunc__ magic method.</pre>

</dd></dl>

