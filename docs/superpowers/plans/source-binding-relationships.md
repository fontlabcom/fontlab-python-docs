---
this_file: docs/superpowers/plans/source-binding-relationships.md
---
# Source binding and relationship correctness

Authority: issues/101.md R040, root PLAN.md source-binding publication gate,
and the source-only documentation contract. This parent relationship task carries
residual N1 from the concluded single final fix wave of source-reference-fidelity.
That historical review cap remains exhausted; its original reports/rulings remain
intact. This task supplies broader declaration-time binding correctness required
for current and future source inputs, not another dispatch of that final fix wave.

## Global Constraints

- Parse source without importing/executing documented packages or native modules.
- Preserve every source identity, body target, original URL and supported alias;
  incorrect relationships/aliases must be corrected with explicit diff evidence.
- Resolve bases from bindings visible at the class declaration, including lexical
  class-body scope and source order. Unknown/dynamic bindings stay unresolved.
- Never invent inheritance from a future declaration, overwritten import or
  equal name text. Existing C3/local override behavior remains required.
- Preserve source locks, accepted build baselines and all historical evidence.
- Feature branch only; preserve other edits. No native mutations, push or deploy.
- this_file records on new files; all shell commands rtk proxy; no worker subagents.
- Full ecosystem, complete examples, documentation search sharding and release
  gates remain separate required work; this task cannot establish full completion.

## Task 1: Implement source-proven declaration-time base binding

Own scripts/static_inheritance.py and the smallest necessary source-binding helper,
focused tests/test_source_bindings.py plus scoped project progress documentation.
Inspect scripts/api_inventory.py and export_aliases.py record/symbol semantics
before choosing implementation; use Griffe/current AST capabilities where suitable
without running source. Consult official Python 3.12 name-binding/class-definition
reference and installed Griffe 2.3.2 source/docs before framework-specific calls.

Tests first: import then local Base, local Base then import, import after Child,
forward local Base, unknown assignment replacing Base, deleted Base, local nested
class overriding module import, class-body import preceding a nested Child,
alias assignment from a known class, dotted imported-module base and unresolved
conditional/dynamic binding. Verify exact canonical base, inherited members,
public inherited aliases and rendered base/member links. Guard fixtures against
runtime import. Existing ordinary imported inheritance, diamonds, overrides,
unresolved bases and real TypeRig Void(Point) must retain truthful behavior.
Unknown statement effects must not fall back to a stale/future known declaration.
Report explicitly unsupported cases as unresolved, not source-proven.

Root baseline receipt ../verification/issue-101-ecosystem/evidence/
docs-source-binding-baseline.json proves four current failures across five cases.
The existing module-wide import map precedes all local candidates, ignores source
order and includes future symbols. Fix the binding model, rather than reversing
candidate priority (which would break local-then-import).

Run focused RED/GREEN tests, covering inventory/alias/render regressions and scoped
lint/diff checks. Read-only full current corpus comparison must enumerate changed
relationships/aliases and prove no loss of source identities or body targets.
Write full task report with commands/results/commit/limitations; commit owned
changes. Root owns full rebuild/browser/check after reviewed implementation.

## Task 2: Root current-corpus acceptance

After task review, rebuild strict complete docs from committed reviewed code,
verify accepted-manifest check, source locks, exact changed relationship/alias
report and all source identities/body targets. Run covering rendered inheritance
and alias-search cases on actual browser output. Preserve before/after metrics
and prior failed evidence. Publication remains pending search sharding, full site
acceptance, licensing/privacy, CI and complete ecosystem release gates.
