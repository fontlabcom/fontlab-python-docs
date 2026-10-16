---
this_file: site-src/packages/remopy.md
---
# Remopy

Remopy controls a running FontLab 9 from another Python process through
FontLab's native MCP server: run code, read values, open and save fonts and call
any FontLab tool. It also launches FontLab and submits scripts on macOS.

## Install

Install the `fontlab-remopy` wheel into your ordinary Python 3.11+ environment
(not into FontLab). Enable FontLab's MCP server once:

```sh
fontlab-remopy launch
fontlab-remopy --timeout 15 setup
```

## Quick start

```python
from fontlab_remopy import FontLab

with FontLab() as fl:
    print(fl.fonts())
    answer = fl.eval("value + 2", value=40)            # 42
    done = fl.run("print(message); result = {'ok': True}", message="Hello")
    print(done.value, done.stdout)
```

## Examples

Write a function locally and run it inside FontLab:

```python
with FontLab() as fl:
    @fl.python
    def metrics(name: str):
        import fontpr
        return fontpr.get_glyph_metrics(glyph_name=name)

    print(metrics("A"))        # with an open font containing A
```

Run a script file and call tools from the command line:

```sh
fontlab-remopy tools
fontlab-remopy execute example.flpy
fontlab-remopy call list_fonts
```

Use `AsyncFontLab` with `async with` and `await` in asynchronous programs.

## Limits

- Values travel as JSON; native objects cannot be returned directly.
- FontLab's fixed five-second script deadline applies. A timeout leaves the
  outcome unknown, so mutating calls are never retried automatically.
- Launch and file association are macOS only; MCP works wherever FontLab's bridge
  executable is available.

Reference: [fontlab_remopy](../reference/fontlab_remopy.md). Remopy is
proprietary (© Fontlab Ltd); only its API documentation is published here.
