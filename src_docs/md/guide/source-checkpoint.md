---
this_file: src_docs/md/guide/source-checkpoint.md
---

# Source checkpoint

Each build of this site reads the sibling source checkouts of every documented
package and records a SHA-256 hash of each input file in `api-sources.lock.json`.
The published `build-info.json` repeats those hashes together with the hash of
every generated page and the native capture identity. A build fails when a
source file changes without an explicit lock update, so the lock, not a list of
commits on this page, identifies the documented source.

The native `fontlab`, `fontgate`, `fontpr`, `FL` and PythonQt pages come from
the declarations in fontlab-echopy and its capture identity manifest. Native
modules absent from the captured FontLab build are listed in that manifest and
have no pages.

## Workflows added in App .98

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

Source checks do not establish native font, history, saved-file or editor
workflow acceptance. Local documentation builds and browser checks do not
establish site publication.
