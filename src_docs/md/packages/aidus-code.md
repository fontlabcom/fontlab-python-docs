---
this_file: src_docs/md/packages/aidus-code.md
---
# Aidus Agentus

Aidus Agentus adds an AI chat dock to FontLab 9. Ask about the current glyph,
inspect fonts and metrics, change spacing, or have the agent write and run FontLab
Python. Responses stream into the dock. It was previously called Aidus Code;
this guide keeps its existing URL.

The current distribution is `fontlab-aidus-agentus`, imported as
`fontlab_aidus_agentus`. Its host package and PythonQt dock are in
`src/fontlab_aidus_agentus` and `src/fontlab_aidus_agentus/plugin`;
the separate brain is in `src/fontlab_aidus_agentus/core`. The reference locks
all 23 Python modules, including the brain and prompts package. Source bodies,
prompt values and private source provenance are not public reference content.

The plugin runs in FontLab's Python 3.11. The AI brain runs in a separate
Python 3.13+ process, so no AI libraries go into FontLab. The configured provider
receives your prompts and the tool results the agent uses. These source-derived
instructions do not establish native or installed acceptance for the current build.

## Install

Use an actual downloaded Aidus Agentus wheel and a compatible Remopy wheel.
Install the lightweight host separately from the brain:

```sh
uv pip install --python 3.11 --target ~/.local/share/fontlab-aidus/host PATH_TO_AIDUS_WHEEL
uv venv --python 3.13 ~/.local/share/fontlab-aidus/brain
uv pip install --python ~/.local/share/fontlab-aidus/brain/bin/python \
  'PATH_TO_AIDUS_WHEEL[brain]' PATH_TO_REMOPY_WHEEL
```

Make the host folder importable in FontLab's Python console:

```python
import os
import site
site.addsitedir(os.path.expanduser("~/.local/share/fontlab-aidus/host"))
```

Install and check the Scripts-menu entries from a terminal:

```sh
PYTHONPATH=~/.local/share/fontlab-aidus/host python3 -m fontlab_aidus_agentus.install install
PYTHONPATH=~/.local/share/fontlab-aidus/host python3 -m fontlab_aidus_agentus.install check
```

The installer records its owned files and refuses to overwrite edited or
unowned scripts or symlinks. The menu link alone does not install the package
or make the host folder importable. Configure the brain interpreter and provider
key sources using **Open Configuration**; keep provider libraries in the brain.

## Quick start

Run **Start Aidus Agentus** from the **Aidus Agentus** Scripts-menu folder.
The dock has connection status, **Reconnect** and **Clear**, a transcript and
one-line input. Startup is queued on FontLab's event loop. The separate brain
may take longer to connect. Reconnect starts a fresh session and never replays
an edit. After changing configuration, shut down and start again.

For an offline identity check, outside FontLab:

```python
from importlib.metadata import version
import fontlab_aidus_agentus

assert fontlab_aidus_agentus.__version__ == version("fontlab-aidus-agentus")
print(fontlab_aidus_agentus.__version__)
print(fontlab_aidus_agentus.__file__)
```

The internal executor diagnostic remains available without invoking a font tool:

```python
from fontlab_aidus_agentus.plugin.executor import FontLabExecutor

result = FontLabExecutor().run("list_tools")
tools = {tool["name"]: tool for tool in result["tools"]}
assert tools["get_current_glyph_info"]["requires_glyph"] is True
assert tools["set_glyph_metrics"]["optional_params"] == ["width", "lsb", "rsb"]
assert tools["run_fontlab_script"]["required_params"] == ["code"]
```

Listing a tool does not prove native read/write safety. Use disposable fonts
for initial editing experiments. The agent can run code on the open font;
a timed-out edit may have completed, so inspect the font before repeating it.
Use [Remopy](remopy.md) for external process control. Whole-font preservation,
Undo/Redo and saved/reopened behavior need their separate native checks.

## Programmatic tools

The built-in metrics tool targets the current glyph. Editing every selected
glyph needs additional script execution; the single-glyph tool is not a batch API.
The executor reads the workspace's active glyph and checks that it belongs to
the current package. Builds without that workspace record retain the older
`CurrentGlyph()` route. A stale record is refused rather than selecting another
glyph. This source behavior does not qualify every FontLab build or whole-font
preservation.

## Historical Aidus Code preservation checkpoint

The following evidence describes Aidus Code before the Agentus rename. The
installation walkthrough then targeted v0.2.1; the private preservation candidate
was `0.2.2.dev4+gb07867092.d20261101`. These results and hashes do not establish
acceptance of the current snapshot.

`get_current_glyph_info` returns current-glyph metadata, but its name does not
guarantee a side-effect-free read. On a historically affected FontLab build,
`CurrentGlyph()` could export glyph data and lose the fresh FontGate note mirror.
The public tool still calls that preflight. A later Unicode export was a second
independent route to the same loss.

The private candidate removes the inner export. It resolves the registered
package, checks package/font identities, requires a unique glyph name and checks
the record's name and ID before reading Unicode. It refuses missing or ambiguous
ownership instead of reading another glyph or restoring metadata afterwards.
It does not repair the earlier `CurrentGlyph()` call.

Fresh wheel and sdist installs each pass 18 targeted checks and retain the
preflight preservation failure. The full source suite in the brain environment
passes 808 tests with that same failure. These tests use owned doubles; the
current native build, full font state, Undo/Redo and save/reopen remain unqualified.
The native snippet in that historical checkpoint was compile-checked only; it
did not demonstrate read safety.

Tested private archive SHA256 values:

| Archive | SHA256 |
| --- | --- |
| Wheel | `f9745105a1aca6a738ce62b6ecb5b041eb5d783bf14aca1d6104853476a8d0ad` |
| sdist | `64a431624d767e5ada8045dc4603e405a7bc116e4bda601abddaa1e3797338e1` |

Version text alone does not distinguish uncommitted builds. Keep exact archive
hashes with test evidence. The old source retirement was qualified separately.
These archive hashes remain historical evidence and do not identify the modern
Agentus snapshot.

## Limits

- Prompts and tool results go to your configured AI provider.
- Current provider authentication, dock lifecycle and native behavior remain separate checks.

Reference: [fontlab_aidus_agentus](../reference/fontlab_aidus_agentus.md).
Aidus Agentus is proprietary (© Fontlab Ltd); only API documentation is published here.
