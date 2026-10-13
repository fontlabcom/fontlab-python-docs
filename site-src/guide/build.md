---
this_file: site-src/guide/build.md
---
# Rebuild and contribute

The reference consumes Echopy's captured/enriched Python sources and adjacent
stubs. It renders as the actual `fontlab`, `fontgate`, `fontpr`, `PythonQt.*`
namespaces. Runtime inspection is disabled throughout normal documentation builds.

Source checkout mode uses sibling ecosystem repositories. Installed artifact
mode selects one provisioned Python package directory with
`FONTLAB_API_SOURCE_ROOT`. Private sources are provisioned using authenticated
GitHub tooling, without embedding credentials in the project.

```bash
./build.sh
./build.sh --check
./build.sh --serve
```

The first environment synchronization may fetch locked dependencies. Once the
dependency cache and source inputs exist, normal builds require neither FontLab
nor network access. Explicit native refresh is a separate source-production
operation; it captures inside FontLab before generation and enrichment.

Generated coverage records every identity and exact source hash. Class indexes
retain each member occurrence; identical captured text is linked to one full
declaration. This sharing does not assert native inheritance or object identity.

Before contributing, agree to the repository's FontLab contributor license
agreement. Change source or enrichment inputs, regenerate, verify rendered
references and cross-links, and include tests for changed behavior. Preserve
source attribution and the Qt/PySide documentation licenses.
