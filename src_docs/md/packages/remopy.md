---
this_file: src_docs/md/packages/remopy.md
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

`setup` submits a macro that sets FontLab's `mcp.enabled` preference and verifies
it. From inside FontLab, call `fontlab_remopy.enable_mcp()` to do the same
preference update directly.

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

Call any other FontLab tool by name with `fl.tool(name, **arguments)`. Remopy
checks the argument names against the tool's input schema and raises `ValueError`
for an unknown name before anything is sent. This matters because FontLab's MCP
server silently drops unknown arguments: `set_kerning_pair(master="Bold")` would
write to the current master. The kerning tools take `master_name`:

```python
with FontLab() as fl:
    fl.tool("list_kerning_pairs", master_name="Bold")
```

Only names are checked, not types, and tools missing from the catalogue or with
open schemas are not checked.

## Limits

- Values travel as JSON; native objects cannot be returned directly.
- FontLab's fixed five-second script deadline applies. A timeout leaves the
  outcome unknown, so mutating calls are never retried automatically.
- Launch and file association are macOS only; MCP works wherever FontLab's bridge
  executable is available.

Reference: [fontlab_remopy](../reference/fontlab_remopy.md). Remopy is
proprietary (© Fontlab Ltd); only its API documentation is published here.
