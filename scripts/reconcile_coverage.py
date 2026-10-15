# this_file: scripts/reconcile_coverage.py
"""Reconcile documented identities with Echopy's captured identity manifest (R014).

Every captured scope, name, class member and constructor must be documented,
under its native spelling or the source spelling Echopy recorded for it. Every
other outcome either has a reason derived from the manifest or source facts, or
is reported as unexplained, which fails the build.
"""

from __future__ import annotations

from typing import Any

NATIVE = {"fontlab", "fontgate", "fontpr", "fontlabpr", "PythonQt"}


def _captured(manifest: dict[str, Any], gap) -> tuple[set[str], dict[str, str], set[str]]:
    """Collect captured identities, absent modules and class names; report errors."""
    captured, absent, classes = set(), {}, set()
    for scope, row in sorted(manifest["scopes"].items()):
        if not row["available"]:
            absent[scope] = row.get("reason", "")
        captured.add(scope)
        captured.update(scope + "." + name for name in row["names"])
        for error in row["errors"]:
            gap("capture-error", scope + "." + error["name"], error=error["error"])
        for name, cls in sorted(row["classes"].items()):
            classes.add(name)
            owner = scope + "." + name
            captured.update(owner + "." + m for m in cls["members"] + cls["constructors"])
            for error in cls["errors"]:
                gap("capture-error", owner + "." + error["name"], error=error["error"])
    return captured, absent, classes


def _declaration_reason(
    identifier: str, row: dict[str, Any], manifest: dict[str, Any]
) -> str | None:
    """Explain why one identity has several source declarations, if it can."""
    if row.get("facets"):
        return "module-and-class-facet"
    if "property" in row.get("labels", []):
        return "property-accessors"
    parent, _, name = identifier.rpartition(".")
    scopes = manifest["scopes"]
    if identifier in scopes and name in scopes.get(parent, {}).get("names", []):
        return "module-and-parent-attribute"
    if identifier.partition(".")[0] not in NATIVE and row.get("declarations"):
        return "ecosystem-source-redefinition"
    return None


def reconcile(
    manifest: dict[str, Any],
    symbols: dict[str, dict[str, Any]],
    aliases: dict[str, str],
    *,
    provenance_capture_sha256: str | None,
    shim_exports: dict[str, list[str]] | None = None,
) -> dict[str, Any]:
    """Return the reconciliation report; `unexplained` must be empty to publish."""
    unexplained: list[dict[str, Any]] = []

    def gap(problem: str, identifier: str, **detail: Any) -> None:
        unexplained.append({"problem": problem, "id": identifier, **detail})

    if (
        manifest.get("schema_version") != 1
        or manifest.get("producer") != "fontlab_echopy.tooling.identities"
    ):
        gap("manifest-format", str(manifest.get("producer")))
    if manifest["capture_sha256"] != provenance_capture_sha256:
        gap("capture-mismatch", manifest["capture_sha256"], provenance=provenance_capture_sha256)
    captured, absent, classes = _captured(manifest, gap)
    for target in manifest["merge_unmatched"]:
        gap("merge-unmatched", target)
    spellings = manifest["native_spellings"]
    sources, documented, spelled = set(), 0, 0
    for native in sorted(captured):
        source = spellings.get(native, native)
        sources.add(source)
        if source not in symbols:
            gap("missing", native, source=source)
            continue
        documented += 1
        spelled += source != native
    for native in sorted(spellings.keys() - captured):
        gap("spelling-not-captured", native)
    extensions = sorted(manifest["maintained_extensions"])
    for identifier in extensions:
        if identifier not in symbols:
            gap("missing", identifier, source="maintained extension")
    for identifier in sorted(symbols):
        if (
            identifier.partition(".")[0] in NATIVE
            and identifier not in sources
            and identifier not in extensions
        ):
            gap("not-captured", identifier)
    multiple = {}
    for identifier, row in sorted(symbols.items()):
        if row.get("occurrences", 1) > 1:
            reason = _declaration_reason(identifier, row, manifest)
            if reason:
                multiple[identifier] = reason
            else:
                gap("multiple-declarations", identifier, occurrences=row["occurrences"])
    for alias, target in sorted(aliases.items()):
        if target not in symbols:
            gap("alias-target-missing", alias, target=target)
    for shim, names in sorted((shim_exports or {}).items()):
        for name in names:
            identity = shim + "." + name
            if identity not in symbols and aliases.get(identity) not in symbols:
                gap("shim-export-unresolved", identity)
    gaps = manifest["enrichment_gaps"]
    for name in sorted(set(gaps["qt_document_failures"]) | set(gaps["unmatched_native_classes"])):
        if name not in classes:
            gap("enrichment-gap-not-captured", name)
    return {
        "schema_version": 1,
        "capture_sha256": manifest["capture_sha256"],
        "counts": {
            "captured_identities": len(captured),
            "documented": documented,
            "documented_under_native_spelling": spelled,
            "maintained_extensions": len(extensions),
            "aliases": len(aliases),
            "shim_exports": sum(len(v) for v in (shim_exports or {}).values()),
            "unexplained": len(unexplained),
        },
        "native_spellings": dict(sorted(spellings.items())),
        "explained": {
            "maintained_extension": extensions,
            "absent_optional_module": absent,
            "multiple_declarations": multiple,
            "enrichment_gaps": {
                "reason": "documented from captured source without upstream Qt prose",
                **gaps,
            },
        },
        "unexplained": unexplained,
    }


def enforce(report: dict[str, Any]) -> None:
    """Fail the build on any unexplained capture, merge or extraction gap."""
    rows = report["unexplained"]
    if rows:
        shown = "; ".join(f"{row['problem']}: {row['id']}" for row in rows[:10])
        raise ValueError(f"{len(rows)} unexplained coverage gaps (R014): {shown}")
