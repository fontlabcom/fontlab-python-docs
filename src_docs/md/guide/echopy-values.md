---
this_file: src_docs/md/guide/echopy-values.md
---
# Echopy module values and their documentation

Echopy keeps a native module value connected to its owner. A read through the
facade sees the current object; an accepted module write or deletion reaches the
native namespace. The adjacent declaration records documentation and a type
without inventing an offline value. Maintainers need to check both routes:
correct names alone cannot reveal a hidden write or a lost attribute docstring.

This guide explains the source contract with invented, owned modules. The names
`owned_echopy_values`, `value-with-dash` and `_echopy_value` below are test inputs,
not claims that a FontLab build exposes those names. Every assignment changes an
owned `ModuleType` object. For real native import and read-only class identity
examples, start with the [Echopy package guide](../packages/echopy.md#use-the-two-import-names).
An arbitrary native module assignment can change application state; these
examples do not authorize copying invented assignments into FontLab.

## Follow a value through the pipeline

| Stage | What it supplies | What it does not establish |
| --- | --- | --- |
| Capture metadata | Names, recorded types, docs and inspection failures | Complete getter/setter behavior or safe arbitrary introspection |
| Raw generation | Source-safe annotated names, adjacent docs and alias metadata | Concrete offline values |
| Maintained JSON overlays | Targeted doc/type enrichment with explicit source attribution | New measured native semantics |
| Merged `.pyi` | Full declarations and adjacent attribute documentation | A runtime implementation |
| Tiny `.py` facade | Current native dispatch, or offline declarations | Emulation of FontLab |
| Griffe static visitor | What a documentation consumer reads from source | Native argument conversion or execution |

`from module import value` follows normal Python binding rules: the local name
refers to the object obtained at that moment. Keep reading `module.value` when
you need later module replacements. Similarly, `module.__dict__` can contain
initial binding snapshots and runtime bookkeeping. Use attribute access, aliases
and `dir()` to test delegation; do not treat the dictionary as a live native map.
Python documents module subclasses in its
[module attribute access reference](https://docs.python.org/3.11/reference/datamodel.html#customizing-module-attribute-access).

## Set up an owned experiment

Use Python 3.11 in a fresh directory that you own, with the Echopy revision being
checked and its `docs` extra already provisioned (`griffe` is required). Check
`fontlab_echopy.__file__` before proceeding so the source or installed copy is
unambiguous. No FontLab, native Qt or macOS framework is required. The source
runner and installed-prefix runner execute this exact setup anew before each
marked example; they never rewrite the setup or example body.

Save this setup followed by **one** marked example in a Python file and run that
file. Each example is independent. `TemporaryDirectory` owns the raw/merged
outputs and overlays; leaving the context removes those scratch files and the
invented module registrations, even if an assertion fails. The helper calls the
real capture/generation/merge/runtime code rather than reproducing its logic.

<!-- setup: echopy-owned-values -->
```python
import ast
from contextlib import contextmanager
import copy
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
from types import ModuleType, SimpleNamespace

from fontlab_echopy.tooling.capture import namespace as capture_namespace
from fontlab_echopy.tooling.generate import generate, source_name
from fontlab_echopy.tooling.merge import merge

OWNED_NATIVE = "owned_echopy_values"
OWNED_FACADE = "owned_echopy_values_facade"

@contextmanager
def owned_pipeline(scope, *, values=None, overlays=(), stage="merged"):
    assert OWNED_NATIVE not in sys.modules and OWNED_FACADE not in sys.modules
    data = {"modules": {OWNED_NATIVE: {"namespace": copy.deepcopy(scope)}}}
    with TemporaryDirectory(prefix="echopy-values-", dir=Path.cwd()) as temporary:
        folder = Path(temporary)
        raw, output = folder / "raw", folder / "merged"
        generate(data, raw)
        paths = []
        for index, patch in enumerate(overlays):
            path = folder / f"overlay-{index}.json"
            path.write_text(json.dumps(patch), encoding="utf-8")
            paths.append(path)
        raw_before = {p.name: p.read_bytes() for p in raw.iterdir() if p.is_file()}
        overlay_before = [p.read_bytes() for p in paths]
        result = merge(raw, output, paths)
        native = ModuleType(OWNED_NATIVE) if values is not None else None
        if native is not None:
            native.__dict__.update(values)
            sys.modules[OWNED_NATIVE] = native
        facade = ModuleType(OWNED_FACADE)
        source = (raw if stage == "raw" else output) / f"{OWNED_NATIVE}.py"
        facade.__file__ = str(source)
        sys.modules[OWNED_FACADE] = facade
        try:
            exec(compile(source.read_text(), str(source), "exec"), facade.__dict__)
            yield SimpleNamespace(native=native, facade=facade, raw=raw,
                                  output=output, overlays=paths, result=result)
            assert raw_before == {p.name: p.read_bytes() for p in raw.iterdir() if p.is_file()}
            assert overlay_before == [p.read_bytes() for p in paths]
        finally:
            sys.modules.pop(OWNED_FACADE, None)
            sys.modules.pop(OWNED_NATIVE, None)
```

The `values=None` branch deliberately omits a native module. A dictionary,
including an empty dictionary, explicitly supplies an owned native module.
This distinction prevents an unavailable native namespace from becoming a
successful dummy. The helper verifies raw and overlay byte preservation after
every normally completed example; the capture example also checks its input.

## Read the current object and forward a write

The first example keeps an earlier local reference, replaces the value through
the facade, then changes the native owner directly. Both module reads follow
the owner. The earlier local reference keeps ordinary Python snapshot semantics.

<!-- example: echopy-live-value -->
```python
initial, replacement, final = object(), object(), object()
scope = {"attributes": [{"name": "value", "type": "Any"}]}
with owned_pipeline(scope, values={"value": initial}) as case:
    facade, native = case.facade, case.native
    saved_reference = facade.value
    assert facade.value is native.value is initial
    facade.value = replacement
    assert facade.value is native.value is replacement
    native.value = final
    assert facade.value is native.value is final
    assert saved_reference is initial
```

Echopy preserves native object identity; it does not clone a value or wrap it in
a documentation object. This test proves dispatch on an owned Python module.
It says nothing about whether a particular native attribute has a writable
setter, accepts a type, or changes a document safely. Native setter errors
propagate through either spelling. Any partial native side effects require their
own preservation check.

## Keep source-safe and native spellings connected

A native name that cannot appear in Python source receives a source identifier.
For this invented name, `source_name("value-with-dash")` is `value_with_dash`.
Use `getattr`/`setattr`/`delattr` for the original spelling; the source identifier
supports ordinary attribute syntax. Both routes must reach the same object.
Deletion must remove both visible spellings, and re-creation must reconnect them.

<!-- example: echopy-sanitized-value -->
```python
native_name = "value-with-dash"
alias = source_name(native_name)
assert alias == "value_with_dash"
initial, replacement = object(), object()
scope = {"attributes": [{"name": native_name, "type": "Any"}]}
with owned_pipeline(scope, values={native_name: initial}) as case:
    facade, native = case.facade, case.native
    assert getattr(facade, native_name) is facade.value_with_dash is initial
    facade.value_with_dash = replacement
    assert getattr(native, native_name) is replacement
    assert getattr(facade, native_name) is facade.value_with_dash is replacement
    assert {native_name, alias}.issubset(dir(facade))
    delattr(facade, native_name)
    assert not hasattr(native, native_name)
    assert not hasattr(facade, native_name) and not hasattr(facade, alias)
    assert native_name not in dir(facade) and alias not in dir(facade)
    setattr(facade, alias, initial)
    assert getattr(native, native_name) is getattr(facade, native_name) is initial
```

This is module dispatch. A sanitized class-member declaration does not add a
renamed member to an original native class: returning that class unchanged
preserves its identity. Consult the native spelling with `getattr` when needed.
The package import aliases `echopy` and `fontlab_echopy` are a separate mechanism;
the [package guide](../packages/echopy.md#use-the-two-import-names) checks those.

## Reserve exact bookkeeping fields

The runtime keeps `_echopy_native`, `_echopy_name` and `_echopy_aliases` local.
Its child-facade import bookkeeping also remains special, so importing a child
facade cannot overwrite a native pseudo-namespace. These rules do not reserve
all `_echopy_` spellings. The generator separately refuses helper-name collisions
before writing output; do not broaden its refusal policy to hide valid names.

This matrix exercises accepted invented names at both raw and merged stages.
It writes by both spellings, checks exact runtime state identities, deletes and
checks `dir()` again. `_echopy_builtins` is an accepted invented value here; raw
generation selects another private import alias when that name is occupied.
None of these spellings is asserted to exist in the running FontLab.

<!-- example: echopy-prefix-values -->
```python
for stage in ("raw", "merged"):
    for native_name in ("_echopy_value", "_echopy-value",
                        "_echopy_value-with-dash", "_echopy_builtins"):
        for route in (native_name, source_name(native_name)):
            initial, replacement = object(), object()
            scope = {"attributes": [{"name": native_name, "type": "Any"}]}
            with owned_pipeline(scope, values={native_name: initial}, stage=stage) as case:
                facade, native = case.facade, case.native
                state = {key: facade.__dict__[key] for key in
                         ("_echopy_native", "_echopy_name", "_echopy_aliases")}
                setattr(facade, route, replacement)
                assert getattr(native, native_name) is replacement
                assert getattr(facade, native_name) is replacement
                assert getattr(facade, source_name(native_name)) is replacement
                assert all(facade.__dict__[key] is value for key, value in state.items())
                delattr(facade, route)
                assert not hasattr(native, native_name)
                for spelling in {native_name, source_name(native_name)}:
                    assert not hasattr(facade, spelling) and spelling not in dir(facade)
```

## Keep annotation-only values absent offline

An annotation is documentation, not a value assignment. The generated source
and merged sidecar record an `AnnAssign` without a value. Offline loading keeps
the annotation while attribute reads fail. A type or doc overlay must not
materialize a sentinel, `None` or a fabricated constant.

<!-- example: echopy-offline-absence -->
```python
native_name = "_echopy-value"
alias = source_name(native_name)
scope = {"attributes": [{"name": native_name, "type": "int", "doc": "Owned value."}]}
patch = {f"{OWNED_NATIVE}.{alias}": {"returns": "str", "doc": "Owned supplement."}}
for stage in ("raw", "merged"):
    with owned_pipeline(scope, overlays=[patch], stage=stage) as case:
        assert case.native is None
        assert alias in case.facade.__annotations__
        assert not hasattr(case.facade, alias)
        assert not hasattr(case.facade, native_name)
        stub = ast.parse((case.output / f"{OWNED_NATIVE}.pyi").read_text())
        value = next(node for node in stub.body if isinstance(node, ast.AnnAssign))
        assert value.value is None and ast.unparse(value.annotation) == "str"
```

For callable declarations, offline operations raise `NativeUnavailable`; see
[unavailable native operations](../packages/echopy.md#handle-unavailable-native-operations).
A missing annotation-only value instead has normal absent-attribute behavior.
A `dir()` entry or a declared type is not proof that an offline value exists.

## Capture descriptor documentation without invoking its getter

Here a property object is stored directly on a plain owned module. Reading that
module member returns the descriptor itself; capture can read its documentation
without invoking the property getter. The deliberately failing getter makes the
boundary testable. This is not a claim that every native module `getattr` is
side-effect free, nor permission to run a fresh capture against a live host.

<!-- example: echopy-captured-value-doc -->
```python
calls = []
def forbidden_getter(owner):
    """Owned captured descriptor documentation."""
    calls.append(owner)
    raise AssertionError("The property getter must never run")

owned = ModuleType(OWNED_NATIVE)
owned.value = property(forbidden_getter)
captured = capture_namespace(owned, OWNED_NATIVE)
before = copy.deepcopy(captured)
assert captured["attributes"][0]["doc"] == forbidden_getter.__doc__
with owned_pipeline(captured) as case:
    raw_text = (case.raw / f"{OWNED_NATIVE}.py").read_text()
    stub_text = (case.output / f"{OWNED_NATIVE}.pyi").read_text()
    assert forbidden_getter.__doc__ in raw_text and forbidden_getter.__doc__ in stub_text
    assert case.result == {"applied": 0, "unmatched": []}
assert captured == before and calls == []
```

Capture records errors explicitly. Documentation and a recorded descriptor type
do not establish whether a native property is readable, writable or callable.
A docstring that includes parentheses is not enough to turn an attribute into a
method. Preserve recorded fields and limitations rather than guessing a setter.

## Preserve docs for each value collection

The generator accepts module `attributes`, `constants` and `modules` collections.
Those are input collections; capture need not classify every object into all
three. Each collection emits an annotation followed immediately by its captured
docstring. The adjacent string belongs to the annotated value for documentation
consumers; moving it to the module header loses that association.

<!-- example: echopy-value-collections -->
```python
for collection in ("attributes", "constants", "modules"):
    captured_doc = f"Owned {collection} documentation."
    scope = {collection: [{"name": "value-with-dash", "type": "Any", "doc": captured_doc}]}
    with owned_pipeline(scope) as case:
        for path in (case.raw / f"{OWNED_NATIVE}.py", case.output / f"{OWNED_NATIVE}.pyi"):
            tree = ast.parse(path.read_text())
            index = next(i for i, node in enumerate(tree.body) if isinstance(node, ast.AnnAssign))
            annotation, documentation = tree.body[index:index + 2]
            assert annotation.target.id == "value_with_dash" and annotation.value is None
            assert isinstance(documentation, ast.Expr)
            assert documentation.value.value == captured_doc
        assert not hasattr(case.facade, "value_with_dash")
```

Unknown captured types remain `Any`. That expresses missing type information;
it does not mean every object can safely be passed to a native setter.
The Python [annotated assignment AST](https://docs.python.org/3.11/library/ast.html#ast.AnnAssign)
records the target, annotation and optional value independently.

## Target source identifiers and preserve overlay precedence

Overlay keys use the emitted source identifier: `owned_echopy_values.value_with_dash`
for native `value-with-dash`. On annotated attributes, the existing `returns`
field specifies the annotation override; it does not call a getter or describe a
method return. `doc` supplies supplemental prose and `source` gives its origin.

Overlays are combined in list order, field by field. A later field replaces the
earlier value for that field. Omitting a field in a later overlay retains the
earlier setting. The following intentionally includes one unmatched native-name
key to show the diagnostic, then verifies the correctly targeted source key.
The later doc replaces the earlier supplemental doc; the earlier `float` type
survives. Captured documentation remains first and appears once.

<!-- example: echopy-overlay-precedence -->
```python
scope = {"attributes": [{"name": "value-with-dash", "type": "int", "doc": "Captured value."}]}
first = {f"{OWNED_NATIVE}.value_with_dash":
         {"doc": "First supplement.", "returns": "float", "source": "owned-first"}}
last = {f"{OWNED_NATIVE}.value_with_dash":
        {"doc": "Final supplement.", "source": "owned-final"},
        f"{OWNED_NATIVE}.value-with-dash": {"doc": "Wrong target."}}
with owned_pipeline(scope, overlays=[first, last]) as case:
    assert case.result == {"applied": 1, "unmatched": [f"{OWNED_NATIVE}.value-with-dash"]}
    tree = ast.parse((case.output / f"{OWNED_NATIVE}.pyi").read_text())
    index = next(i for i, node in enumerate(tree.body) if isinstance(node, ast.AnnAssign))
    annotation, documentation = tree.body[index:index + 2]
    assert ast.unparse(annotation.annotation) == "float"
    assert documentation.value.value == ("Captured value.\n\nSupplemental documentation:\n"
                                         "Final supplement.\n\nSource: owned-final")
    assert "First supplement." not in documentation.value.value
```

An unmatched target must be investigated. It can mean a spelling error, an
obsolete capture target or a patch for another producer; a green identity count
does not prove the overlay was applied. Keep overlay inputs independent of
regenerated raw output. Changing generation/merge code alone does not update
already shipped captures, declarations, provenance or generated references.

## Check the actual documentation consumer

An AST string check catches emission mistakes. It does not establish which
docstring a documentation consumer associates with the member. This example
uses Griffe's actual static `visit` API against the emitted `.pyi`, then compares
the member name, annotation and combined documentation. It does not import or
execute the sidecar. Griffe documents the API in its
[agents reference](https://mkdocstrings.github.io/griffe/reference/api/agents/#griffe.visit).

<!-- example: echopy-griffe-value-doc -->
```python
from griffe import visit

scope = {"attributes": [{"name": "value-with-dash", "type": "Any", "doc": "Captured detail."}]}
patch = {f"{OWNED_NATIVE}.value_with_dash":
         {"returns": "str", "doc": "Maintained detail.", "source": "owned-guide"}}
with owned_pipeline(scope, overlays=[patch]) as case:
    stub = case.output / f"{OWNED_NATIVE}.pyi"
    documented = visit(OWNED_NATIVE, filepath=stub, code=stub.read_text())
    member = documented.members["value_with_dash"]
    assert str(member.annotation) == "str"
    assert member.docstring.value == ("Captured detail.\n\nSupplemental documentation:\n"
                                      "Maintained detail.\n\nSource: owned-guide")
    assert member.value is None
    assert not hasattr(case.facade, "value_with_dash")
```

This establishes the owned source-to-Griffe path. It does not qualify rendered
pages, navigation, type links, browser accessibility or a published site.

## Keep the native facade small and lazy

Detailed value docs belong in the sidecar. Native loading must not parse that
sidecar merely to obtain a value. This example generates an owned facade, removes
its sidecar only inside the temporary directory, and re-executes it while its
owned native module remains registered. If native binding required the sidecar,
this would fail. The descriptor-free live value still has exact identity.

<!-- example: echopy-lazy-facade -->
```python
initial = object()
scope = {"attributes": [{"name": "value", "type": "Any", "doc": "Owned sidecar detail."}]}
with owned_pipeline(scope, values={"value": initial}) as case:
    source = case.output / f"{OWNED_NATIVE}.py"
    stub = source.with_suffix(".pyi")
    facade_text = source.read_text()
    assert "Owned sidecar detail." not in facade_text
    assert "_populate(globals()," in facade_text
    stub.unlink()
    exec(compile(facade_text, str(source), "exec"), case.facade.__dict__)
    assert case.facade.value is case.native.value is initial
```

Deleting a shipped sidecar would break offline analysis and packaging. The
example removes a disposable owned output solely to check native-path laziness;
retain every packaged `.pyi` and its licence/provenance in real distributions.

## Interpret the evidence at its actual scope

A retained full identity audit covered 17 namespace scopes: 16 available and one
absent optional module. It matched 242,649 symbol identities and five root
namespace identities across declarations, alias maps and facade routes. Those
static matches do not classify every constructor or descriptor. The retained
census still has 1,600 variadic constructors, 13,035 variadic methods and 68,103
merged class attribute annotations typed `Any`. Exact historical raw capture
input was unavailable to that audit; a different local capture is not a valid
replacement. The retained upstream Qt enrichment report also has 35 failed
documents and 266 unmatched native classes. These are limitations of those
retained inputs, not newly measured current-host counts or results of this guide.

Captured docs, inferred annotations and reference signatures are evidence with
provenance. They cannot prove native semantic completeness. A successful owned
example is source-contract evidence; a fresh ordinary wheel/sdist run is
installed-artifact evidence. Consumer qualification, native FontLab workflows,
canonical promotion, generated-reference/source-lock refresh and publication
remain independent acceptance levels. Read [rebuild and contribute](build.md)
for the documented build process; obey the workspace's current approval and
resource holds before attempting a capture, native run or generated build.
