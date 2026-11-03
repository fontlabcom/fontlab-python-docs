---
this_file: src_docs/md/packages/aidus-code.md
---
# Aidus Code

Aidus Code adds an AI chat dock to FontLab 9. Ask about the current glyph,
inspect fonts and metrics, change spacing, or have the agent write and run FontLab
Python. Responses stream into the dock.

The FontLab plugin runs in FontLab's Python 3.11. The AI "brain" runs in a
separate Python 3.13+ process, so no AI libraries go into FontLab. The AI provider
you configure receives your prompts and the tool results the agent uses.

The installation walkthrough describes Aidus Code v0.2.1. The read-preservation
notes below describe the private `0.2.2.dev4+gb07867092.d20261101` candidate;
they do not announce a release or establish compatibility with every FontLab build.

## Install

1. Install the host package into a dedicated folder (Python 3.11):

    ```sh
    uv pip install --python 3.11 --target ~/.local/share/fontlab-aidus/host PATH_TO_AIDUS_WHEEL
    ```

2. Create the brain environment (Python 3.13+) with the `brain` extra and Remopy:

    ```sh
    uv venv --python 3.13 ~/.local/share/fontlab-aidus/brain
    uv pip install --python ~/.local/share/fontlab-aidus/brain/bin/python \
      'PATH_TO_AIDUS_WHEEL[brain]' PATH_TO_REMOPY_WHEEL
    ```

3. Install the Scripts-menu entries and check the setup:

    ```sh
    PYTHONPATH=~/.local/share/fontlab-aidus/host python3 -m fontlab_aidus_code.install install
    PYTHONPATH=~/.local/share/fontlab-aidus/host python3 -m fontlab_aidus_code.install check
    ```

    The installer records the files it owns. Reinstalling or uninstalling keeps
    your own files. An install stops before changing anything when a script it
    would replace was modified, is not its own or is a symlink.

4. Configure the brain Python path and your AI provider keys as described in the
   package's configuration guide.

## Quick start

In FontLab, open the **Aidus Code** entry in the Scripts menu. Use owned fixture
fonts when trying requests that inspect or edit glyphs; the current read path
has the preservation limitation below. The built-in metrics tool targets the
current glyph. A request to edit every selected glyph requires additional script
execution and is not evidence that the single-glyph tool supports batch edits.

## Identify an installed candidate offline

This prints package identity without opening the dock or starting the brain:

```python
# Outside FontLab
from importlib.metadata import version
import fontlab_aidus_code

assert fontlab_aidus_code.__version__ == version("fontlab-aidus-code")
print(fontlab_aidus_code.__version__)
print(fontlab_aidus_code.__file__)
```

For maintainer diagnostics, the plugin executor can list its built-in tool
metadata without calling a font operation. This is an internal diagnostic
interface, not a replacement for the native tool API:

```python
# Outside FontLab; installed plugin diagnostic only
from aidus_code_plugin.executor import FontLabExecutor

result = FontLabExecutor().run("list_tools")
tools = {tool["name"]: tool for tool in result["tools"]}
assert tools["get_current_glyph_info"]["requires_glyph"] is True
assert tools["set_glyph_metrics"]["optional_params"] == ["width", "lsb", "rsb"]
assert tools["run_fontlab_script"]["required_params"] == ["code"]
print(sorted(tools))
```

A listed tool is not a successful native operation. Neither example contacts an
AI provider, creates a font or proves native read/write safety.

## Programmatic tools

The agent's FontLab tools are registered by the plugin's executor and are
not a public Python import. Reach them through the agent, or through
[Remopy](remopy.md) from outside FontLab.

## Glyph-info preservation boundary

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
The native snippet above is compile-checked only. Do not use it on owner fonts
to demonstrate read safety.

Tested private archive SHA256 values:

| Archive | SHA256 |
| --- | --- |
| Wheel | `f9745105a1aca6a738ce62b6ecb5b041eb5d783bf14aca1d6104853476a8d0ad` |
| sdist | `64a431624d767e5ada8045dc4603e405a7bc116e4bda601abddaa1e3797338e1` |

Version text alone does not distinguish uncommitted builds. Keep exact archive
hashes with test evidence. The obsolete `aidus-code` source remains protected
until migration and retirement requirements are satisfied.

## Limits

- Use a disposable font for your first editing experiments: the agent can change
  and run code on the open font.
- Prompts and tool results go to your configured AI provider.

Reference: [fontlab_aidus_code](../reference/fontlab_aidus_code.md). Aidus Code is
proprietary (© Fontlab Ltd); only its API documentation is published here.
