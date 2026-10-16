---
this_file: site-src/guide/install.md
---
# Install and connect

Use the reviewed wheel or source distribution from each package's GitHub release.
Private repositories require authenticated access. Keep credentials in your
normal GitHub tooling; never put them in documentation, URLs or Python scripts.

Install outside FontLab with `uv pip install PATH_TO_WHEEL`. For embedded use,
install into a Python directory on FontLab's interpreter path using a compatible
Python version. FontLab supplies its native bindings and existing Qt application.

The captured API uses FontLab9, Python3.11 and Qt5. The source-only documentation
environment uses Python3.12 or newer. A PySide2 binary wheel is a reference input;
it is not loaded into FontLab's PythonQt runtime.

Enable FontLab's MCP server, then connect:

```python
from fontlab_remopy import FontLab

with FontLab() as app:
    print(app.fonts())
    print(app.output())
```

`eval()` returns a JSON-native value. `run()` captures stdout/stderr and a result;
bind variables as keyword arguments rather than interpolating them into code.
The native execution deadline still applies. A timeout can leave an operation's
outcome unknown, so mutating calls are never retried automatically.

```python
with FontLab() as app:
    answer = app.eval("value + 2", value=40)
    execution = app.run("print(message)\nresult = 42", message="Hello, FontLab")
```

For asynchronous programs, use `AsyncFontLab` with `async with` and await calls.
