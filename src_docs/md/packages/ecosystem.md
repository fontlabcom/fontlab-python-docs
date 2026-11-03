---
this_file: src_docs/md/packages/ecosystem.md
---
# Ecosystem and package boundaries

The FontLab Python packages split by one question: where does your code run, and
what does it need to talk to? Each package owns one answer. Pick the package that
matches your answer instead of reaching across a boundary.

| Package | Role |
| --- | --- |
| [Remopy](remopy.md) | Pip-installable remote control of a running FontLab from an ordinary Python process outside it. |
| [Glyport](glyport.md) | Runs unmodified Glyphs.app scripts and plugins inside FontLab. |
| [Fontport](fontport.md) | FontParts, fontTools pens, UFO and DesignSpace interoperability. No user interface. |
| [Echopy](echopy.md) | Generates documented, pure-Python passthrough shims of `fontlab`, `fontgate`, `fontpr`, `FL` and `PythonQt`. |
| [Fontlabapp](fontlabapp.md) | The large object and UI API: menus, panels, windows, drawing overlays, dialogs. |
| [Fly](fly.md) | Nine short, lazy import aliases for the packages above. It adds no behaviour. |
| [Aidus Code](aidus-code.md) | An in-FontLab coding agent with a graphical dock. |
| [Pythonqtside](pythonqtside.md) | Runs PySide2-style code on FontLab's PythonQt. |
| Scriptmix | A collection of practical menu scripts for FontLab 9. |
| Examples | PythonQt-rich example scripts that show how to build panels and tools. |
| [Plugmix](plugmix.md) | New: native FontLab plugins, starting with toggleable reporter overlays. |

## How the packages depend on each other

Arrows point from a package to what it builds on. Dashed arrows are optional or
planned.

```mermaid
flowchart TD
    host["FontLab 9 host<br/>fontlab / fontgate / fontpr / PythonQt"]
    echopy["Echopy<br/>documented shims"]
    app["Fontlabapp<br/>objects + UI"]
    qside["Pythonqtside"]
    glyport["Glyport"]
    fontport["Fontport"]
    fly["Fly<br/>aliases"]
    aidus["Aidus Code"]
    plugmix["Plugmix"]
    scripts["Scriptmix / Examples"]
    remopy["Remopy<br/>outside FontLab"]

    echopy --> host
    app --> host
    qside --> host
    app -.-> echopy
    glyport --> app
    glyport --> echopy
    fontport --> host
    fontport -.->|Qt editors moving| app
    plugmix --> app
    aidus --> app
    aidus -.->|MCP| remopy
    scripts --> app
    fly -.-> echopy
    fly -.-> app
    fly -.-> glyport
    fly -.-> fontport
    fly -.-> qside
    remopy -.->|FontLab MCP server| host
```

Two edges are worth stating in words. Remopy never imports the host: it talks to
FontLab's native MCP server, so it runs anywhere Python runs. Fly imports nothing
until you ask for an alias, so importing it never loads a target package.

## Where does my code go?

| You want to... | Use |
| --- | --- |
| Run a script from a terminal, CI job or notebook against a running FontLab | Remopy |
| Run a Glyphs.app script or plugin without rewriting it | Glyport |
| Read or write UFO, DesignSpace or FontParts objects, or draw with fontTools pens | Fontport |
| Look up what a native FontLab class or method accepts | Echopy reference |
| Add a menu item, dock, dialog or drawing overlay | Fontlabapp |
| Reuse PySide2 code in FontLab | Pythonqtside |
| Draw an always-available read-only overlay in the Glyph window | [Plugmix](plugmix.md), or the [native hooks](../guide/native-hooks.md) directly |
| Add a custom editing tool to the toolbar | The [native hooks](../guide/native-hooks.md) (`registerPythonTool`) |
| Write a short script and share it as a menu entry | Scriptmix conventions, built on Fontlabapp |
| Ask an AI agent to inspect or edit the font | Aidus Code |

## Boundary rules

- **Outside versus inside.** Remopy is the only package meant for code outside
  FontLab. Everything else imports FontLab's own modules and needs the host.
- **Interop versus UI.** Fontport converts font data and has no user interface.
  Its Qt editors are moving to `fontlabapp.fontui` (issue 201); until that move
  is complete, they still ship with Fontport.
- **Shims versus behaviour.** Echopy documents and mirrors the native API. It does
  not add features. Behaviour that goes beyond the native API belongs in
  Fontlabapp.
- **Compatibility layers stay separate.** Glyport carries Glyphs.app behaviour;
  Pythonqtside carries PySide2 behaviour. Neither leaks into Fontlabapp.
- **Aliases are not an API.** Fly resolves names; it never wraps or extends the
  module it returns.
