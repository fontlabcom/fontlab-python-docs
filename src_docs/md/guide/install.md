---
this_file: src_docs/md/guide/install.md
---
# Install and connect

Use the reviewed wheel or source distribution from each package's GitHub release.
Private repositories require authenticated access. Keep credentials in your
normal GitHub tooling; never put them in documentation, URLs or Python scripts.

## Install inside FontLab

Install **Instamix 1.0.9 or newer** first. Download its standalone
[install.vfpy](https://code.fontlab.com/fontlab-python-instamix/install.vfpy),
then open that file in FontLab. It bootstraps the stdlib-only installer from a
validated wheel; a pre-existing pip or venv is not required. The current generated
project installer checks migration and rollback capabilities before reusing its
provider. Do not use Instamix 1.0.8 to upgrade an old `install.vfpy` installation:
a failed replacement could remove other files recorded by that legacy installer.

In FontLab's Scripting panel, install ordinary distribution requirements with:

```python
from fontlab_instamix import install_packages

install_packages("uharfbuzz>=0.57")
```

Instamix finds or downloads uv, verifies a standalone Python matching the target,
and creates or checks the shared venv. Packages go to
`<data>/python/<major.minor>/site-packages`, which FontLab already reads. The
venv reads that same directory through its own managed `.pth`; FontLab does not
need to process that file. An incompatible existing venv is refused rather than
replaced. Installation refreshes import caches, without reloading imported modules.

For a source project with `[tool.fontlab-install]`, open its current `install.vfpy`.
For a ready `.fontlabext`, `.fontlabextz` or root manifest, use the
[Instamix extension API](../packages/instamix.md). Its records and uninstall
commands are under **Scripts > Instamix**.

Default data-folder discovery uses an explicit argument, then `FONTLAB_DATA_DIR`,
then native preferences' `dataPathDefault`, then the platform default. A custom
current application `dataPath` is a different value: pass the intended folder
explicitly when those differ. Never assume a terminal's Python version or
architecture matches the running FontLab.

## Install outside FontLab

Install external clients such as Remopy into an ordinary environment with
`uv pip install PATH_TO_WHEEL`. That environment does not make packages available
to embedded FontLab. [Instamix](../packages/instamix.md#targets-and-the-shared-environment)
explains explicit targets and the external CLI. FontLab supplies its native
bindings and existing Qt application; install neither PySide binaries nor a
second Qt application into that host.

### Temporary release inputs

App 1.2.31, Plugmix 1.1.19 and Remopy 2.0.7 have checked GitHub release artifacts,
but their PyPI uploads failed because trusted publishers were not configured.
Do not lower a dependency floor to work around a missing release. Use the checked
release-wheel download URLs with `uv pip install` in an ordinary Python
environment. The App and Plugmix versions above resolved together in a fresh
ordinary arm64 Python 3.11 environment.

That is an ordinary package-install check, not a FontLab plugin deployment test.
Use the reviewed source installer or extension pack for its Scripts and bundles.
Recheck publication status when choosing later releases; keep version floors and
artifact identity aligned. Instamix 1.0.9 or newer is still needed for legacy
project upgrades.

The captured API uses FontLab9, Python3.11 and Qt5. The source-only documentation
environment uses Python3.12 or newer. A PySide2 binary wheel is a reference input;
it is not loaded into FontLab's PythonQt runtime.

## Connect from another process

!!! warning "FontLab 9.1.9813 bridge defect"
    The native MCP bridge can crash in `BridgeConnection::updateTimeout` on this
    build ([fontlab/fl#8657](https://github.com/Fontlab/fl/issues/8657)). Remopy
    setup/tools/run and Instamix `--remote` can time out. A submitted operation's
    outcome is unknown until its receipt is checked. Do not retry automatically.
    Until a fixed bridge ships, run an owned `.vfpy` directly through FontLab's
    File > Open and have it write a result file; submission alone proves no work.

On a build with a working MCP bridge, enable FontLab's MCP server, then connect:

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
