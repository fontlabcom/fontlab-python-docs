---
this_file: AGENTS.md
---

<!-- workspace-handoff:2026-11-03 -->
## Workspace documentation handoff —2026-11-03

Issue 123 implementation is paused by the owner. The present request authorizes
only documentation maintenance; preserve all source, owner edits and branch state.
Authored guides and source-derived native API documentation. Observed canonical checkout: `main` at `5ec628a388fa`. No source integration is performed by this update.

Accepted feature d9c15dc adds the owned-window recovery guide after extensive generation/resource/manager/discovery/node/layer guides.

Authored source/ordinary examples were checked; generated references, source-lock, rendered site and publication remain gated.

Read workspace AGENTS/DECISIONS and local project guidance before later work.
Use direct execution unless a new request explicitly authorizes agents. Product
work stays isolated; this docs-only request does not authorize native actions,
installs, merges, pushes, releases, generated-site updates or legacy retirement.
<!-- /workspace-handoff -->

<!-- this_file: AGENTS.md -->

# fontlab-python-docs: agent guidance

<!-- shared-theme-integration:start -->
## Shared theme maintenance

Read [THEME.md](THEME.md) before changing shared chrome, MaterialX configuration
or component assets. This repository’s role is: python and pythonqt api reference.
Shared browser behavior belongs in `fontlab-www-docstheme`; FontLab global menu
source belongs in `img/docs/menu/fontlab.js`, Vexy menu source in
`i.vexy.art/docs/menu/vexy.js`. Keep per-site content, branding and native builds here.
Preserve one menu and one search control, documented ownership defaults, scoped
`.fltheme-components` styles and `du-` component prefixes. Verify final generated
HTML after overlays; a source-only change is not proof of a live deployment.
Do not commit unrelated local edits or hand-edit generated CSS as the source fix.
Work directly unless the current user explicitly requests delegation.
<!-- shared-theme-integration:end -->
