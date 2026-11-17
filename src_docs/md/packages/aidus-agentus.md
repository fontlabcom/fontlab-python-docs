---
this_file: src_docs/md/packages/aidus-agentus.md
---
# Aidus Agentus

Aidus Agentus adds an AI chat dock to FontLab 9. Ask about the current glyph,
inspect fonts and metrics, change spacing, or have the agent write and run FontLab
Python. Responses stream into the dock. The AI provider you configure receives your
prompts and the tool results the agent uses, so try editing on a disposable font
first.

The package is `fontlab-aidus-agentus` (import `fontlab_aidus_agentus`). It
replaces the earlier Aidus Code package.

## How it is built

- The FontLab plugin runs in FontLab's Python 3.11 and PythonQt. It owns the dock
  (`fontlab_aidus_agentus.plugin`).
- The AI "brain" (`fontlab_aidus_agentus.core`) runs in a separate Python 3.13+
  process on AgentPool, so no AI libraries go into FontLab.
- `Scripts/Aidus Agentus/` holds the menu scripts that open the dock.

## Install

From a checkout, open `install.vfpy` in FontLab 9 (File > Open, double-click it or
drop it onto FontLab), then restart FontLab. The repository README has the
configuration guide and the brain environment setup:
<https://github.com/fontlabcom/fontlab-aidus-agentus>.

This page documents source behavior. It does not claim an installed or native
acceptance result for any FontLab build.

## Reference

[fontlab_aidus_agentus](../reference/fontlab_aidus_agentus.md) lists the public
API, rendered from docstrings and signatures only.
