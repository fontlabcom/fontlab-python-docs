---
this_file: src_docs/md/guide/source-checkpoint.md
---

# Source checkpoint: App .98

This documentation checkpoint pins the reviewed App .98 source and its paired
Examples and Scriptmix menus. It describes source interfaces; each tool retains
its separate native workflow and font-preservation acceptance requirements.

| Producer | Source revision |
| --- | --- |
| fontlab-echopy | `c555c9f19fcd896c1871c8fadd4b490e4fd132dc` |
| fontlab-fontlabapp | `8669c2c14f5881c49dc05a35f869cc78e5070c8a` |
| fontlab-remopy | `824d690be9aa1f73c427ae474ed9b90f3bb6273d` |
| fontlab-grablab | `2473ee1ae707cf14ff77649b85880109ed992deb` |
| pythonqtside | `2777e85cd84c7ba3d242e461a2c4143fb00ffb42` |
| fontlab-fly | `6cf9dc1503f3d11d42c72918effe6c50597345ff` |
| TypeRig | `7b8dad952ae3cd698e46a4cbc1dc3e709d870888` |
| fontlab-glyport | `2c46c729f6780ad07fb1254296426189a0e4bb84` |
| fontlab-aidus-code | `32523d418abb6122136b317411b127251b7f8bee` |
| fontlab-fontport | `7a6e400ebb1d95bcf01528fb0a4036922e468bad` |
| fontlab-python-examples | `1f54a9a72c24cf6ed76b5fcee76a0d557b92a252` |
| fontlab-python-scriptmix | `9ab9d36a0ccecfb15bdaee93b700acaeb72e3390` |

The paired collections contain 37 Examples menus and 107 Scriptmix menus.
The App package contains 251 runtime/resource files. The source lock retains
all previous 743 inputs and adds 22 documented App modules. Native FontLab
and PythonQt declarations and their capture identity manifest are unchanged.

## Newly documented workflows

| Workflow | Public source interface |
| --- | --- |
| Two component dependency graph profiles | [`components.graph.model.show` and `show_official`](../reference/fontlabapp/components/graph/model.md) |
| Two metrics and revision worksheets | [`proof.numeric.launcher.show` and `show_detailed`](../reference/fontlabapp/proof/numeric/launcher.md) |
| Same-kerning-groups proof | [`kerning.group_proof.model.run`](../reference/fontlabapp/kerning/group_proof/model.md) |
| Close But No Cigar report | [`contours.near_miss.model.show`](../reference/fontlabapp/contours/near_miss/model.md) |
| Two local spacing-offset slider profiles | [`metrics.offset.model.show` and `show_stacked`](../reference/fontlabapp/metrics/offset/model.md) |

These entries preserve the distinct original profiles and complete controls.
Local graph movement, numeric estimates and spacing-offset previews do not edit
the font. The kerning proof creates a new tab. The near-miss report uses each
selected occurrence’s first layer and its associated master. Read the individual
API descriptions for source fences, explicit refusals and current limitations.

The .98 source/artifact checkpoint passes both ordinary archive consumer graphs
and every applicable original-baseline module coverage gate. Those checks do not
establish complete native font, history, saved-file or editor workflow acceptance.
The inherited .90 spinbox controls have separate bounded native evidence.

This is an explicit .98 checkpoint. Later Text Holder .100 development is not
part of its source lock. The earlier .80 checkpoint remains historical.
Local documentation builds and browser checks do not establish site publication.
