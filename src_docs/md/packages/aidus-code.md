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

This page describes Aidus Code v0.2.1.

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

In FontLab, open the **Aidus Code** entry in the Scripts menu. Try:
"What are the sidebearings of the current glyph?" or "Set the right sidebearing
of all selected glyphs to 50."

## Programmatic tools

The agent's FontLab tools are also callable from Python inside FontLab, through
the [Aidus tools reference](../reference/aidus_code_tools.md):

```python
# Inside FontLab, with fontlab-aidus-code installed
from fontlab_echopy import aidus_code_tools

print(aidus_code_tools.get_current_glyph_info())
```

## Limits

- Use a disposable font for your first editing experiments: the agent can change
  and run code on the open font.
- Prompts and tool results go to your configured AI provider.

Reference: [fontlab_aidus_code](../reference/fontlab_aidus_code.md). Aidus Code is
proprietary (© Fontlab Ltd); only its API documentation is published here.
