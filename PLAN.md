---
this_file: PLAN.md
---
# Current native Python reference rebuild

Authority: parent issues/101.md R037–R044 and the user's explicit source/code
interplay requirement. The old FontLab7/Python2 reference remains a historical
source/archive until the complete new root and route preservation are verified.

Use current captured/enriched Echopy as the native API authority. Its docnames
command projects ordinary explicit aliases for fontlab/fontgate/fontpr/optional
fontlabpr/PythonQt, and its Griffe extension preserves class/namespace collisions.
No copied stubs, host imports or native inspection in normal builds.

1. Extract every source identity and exact shared body, with native public names,
   hashes and complete class/member/alias coverage. Parser/planner tests pass.
2. Generate module/class/member pages with complete per-class occurrence indexes
   and exact-body links; paginate bodies without losing declarations or guessing
   native inheritance. Preserve class/pseudo-namespace facets explicitly.
3. Build the full current reference and ecosystem guides using locked ProperDocs,
   MaterialX, fltheme26, mkdocstrings Python handler and explicit autorefs.
4. Preserve legacy routes/fragments in a versioned archive and route map.
5. Implement ./build.sh and --check/--serve/--refresh-native, source/artifact modes,
   deterministic coverage, source privacy/license checks and offline operation.
6. Complete search sharding now retains the original corpus and uses pinned,
   offline global routing plus the original consumer engine. Review the implementation
   and verify actual full rendered API/inventory, search and browser interaction,
   desktop/mobile/light/dark/keyboard, page/index/resource budgets. GitHub CI is out of scope (owner decision D3).
7. Publish only audited outputs; independently verify the deployed source
   provenance, routes, assets, search and navigation. Full goal remains active.
