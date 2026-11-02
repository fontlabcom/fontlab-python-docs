---
this_file: src_docs/md/packages/echopy.md
---
# Echopy

Echopy makes FontLab's native Python API readable by editors, type checkers and
documentation tools. Inside FontLab, it returns the original native objects.
Outside FontLab, it provides declarations; it does not emulate the font editor.

Use `echopy` for short imports or `fontlab_echopy` for explicit package names.
Matching submodules imported through either name resolve to the same module
objects. The examples below use Python 3.11.

## Install and identify your copy

Install the `fontlab-echopy` wheel into the Python environment where you need
its declarations. For host use, follow [Install into FontLab](index.md#install-into-fontlab).
FontLab supplies the native modules; installing Echopy alone does not supply them.
Do not install PySide or create a second Qt application inside FontLab.

Run this outside FontLab to identify the installed distribution:

```python
# Outside FontLab
from importlib.metadata import version
import fontlab_echopy

print(version("fontlab-echopy"))
print(fontlab_echopy.__file__)
```

The package version identifies the installed declarations. It does not identify
the running FontLab build or prove that every declaration matches that build.
Keep the package version, native build and capture provenance together when
reporting a mismatch.

For maintenance work, see [module values and their documentation](../guide/echopy-values.md):
current-value identity, source-safe aliases, exact bookkeeping fields, absent
offline values, captured attribute docs, maintained overlays and static Griffe
checks. Its executable experiments use invented owned modules.

## Use the two import names

This check runs outside FontLab and does not construct native objects:

```python
# Outside FontLab
from echopy import fontlab as short_name
from fontlab_echopy import fontlab as long_name

assert short_name is long_name
print(short_name.__name__)
```

Inside FontLab, check native identity before relying on argument conversion or
`isinstance`. This snippet reads class objects only; it does not edit a font:

```python
# Inside FontLab; native execution required
import fontlab
from echopy import fontlab as fl

assert fl.flNode is fontlab.flNode
assert fl.flLayer is fontlab.flLayer
```

Echopy does not wrap each node or layer in a Python replacement class. Native
constructors, methods, errors and return values retain the host's behavior.
A declaration does not repair a host defect or add an unsupported overload.

## Read the full declarations offline

Small `.py` facades keep runtime imports inexpensive. Their adjacent `.pyi`
files hold the detailed declarations and docstrings. Inspecting an offline
placeholder with `inspect.signature` can show a generic signature; read the
sidecar when you need the recorded declaration.

Locate the FontLab sidecar without importing the native module:

```python
# Outside FontLab
from pathlib import Path
import fontlab_echopy

package = Path(fontlab_echopy.__file__).parent
sidecar = package / "fontlab.pyi"
assert sidecar.is_file()
print(sidecar.name)
```

Use Python's parser to extract one class and its documentation without executing
its declaration. This example prints the recorded `flNode` class:

```python
# Outside FontLab
import ast
from pathlib import Path
import fontlab_echopy

sidecar = Path(fontlab_echopy.__file__).parent / "fontlab.pyi"
source = sidecar.read_text(encoding="utf-8")
tree = ast.parse(source)
node = next(item for item in tree.body
            if isinstance(item, ast.ClassDef) and item.name == "flNode")
print(ast.get_docstring(node) or "No captured class documentation")
print(ast.get_source_segment(source, node))
```

The same approach applies to `fontgate.pyi` and `fontpr.pyi`. PythonQt declarations
use their package subdirectories. Read these files as text; do not execute them
to create native objects outside the host.

## Read a recorded call signature

Read the declaration and its docstring together. A Python signature can express
argument order and defaults, but it cannot prove native overload selection or
implicit conversions.

| Declaration text | How to read it |
| --- | --- |
| `value, /` | The recorded parameter is positional-only. |
| `*, label` | The recorded parameter is keyword-only. |
| `count=3` | The declaration records a literal default. |
| `value=...` | The actual default may be omitted; consult the captured documentation rather than passing `...` as a substitute. |
| `*args, **kwargs` | The declaration is variadic. It may be a fallback for missing or ambiguous metadata; it does not mean every argument is accepted. |
| `Any` | The declaration does not constrain that type; it is not proof of native compatibility. |
| `@staticmethod` or `@classmethod` | The declaration records that binding kind. Its absence does not prove that an unknown native descriptor is an instance method. |

Print the recorded constructor signature and documentation from the installed
sidecar. This reads text only, so an unsupported constructor is never called:

```python
# Outside FontLab
import ast
from pathlib import Path
import fontlab_echopy

path = Path(fontlab_echopy.__file__).parent / "fontlab.pyi"
tree = ast.parse(path.read_text(encoding="utf-8"))
cls = next(node for node in tree.body
           if isinstance(node, ast.ClassDef) and node.name == "flNode")
constructor = next(node for node in cls.body
                   if isinstance(node, ast.FunctionDef) and node.name == "__init__")
for decorator in constructor.decorator_list:
    print("@" + ast.unparse(decorator))
print(f"def {constructor.name}({ast.unparse(constructor.args)})")
print(ast.get_docstring(constructor) or "No recorded constructor documentation")
```

A single captured constructor can supply a specific signature. When several
constructor records are present, the generator keeps a variadic declaration and
retains their signatures and documentation together. Missing constructor records
keep the generic fallback. These rules apply when generating new output;
installing a newer generator does not refresh an older capture or sidecar.

Python's [AST reference](https://docs.python.org/3.11/library/ast.html#ast.arguments)
describes the argument fields used here. Parsing and printing the declaration
does not evaluate its annotations or default expressions.

## Handle unavailable native operations

Offline imports support documentation and analysis. An attempted native operation
raises `NativeUnavailable` instead of returning a dummy object. This example
expects that refusal in a normal Python process without FontLab's native modules:

```python
# Outside FontLab
from echopy import fontlab as fl
from fontlab_echopy import NativeUnavailable

try:
    fl.flNode()
except NativeUnavailable:
    print("Run native operations inside FontLab")
else:
    raise AssertionError("This example requires an environment without FontLab")
```

Catch this exception at an application's boundary if host access is optional.
Do not catch every exception and present a failed native operation as success.
Inside FontLab, other exceptions can indicate invalid arguments or a host defect.

## Check capture provenance

Read the packaged provenance to see which capture and enrichment records produced
the declarations. The following prints its available top-level sections without
assuming that every release uses an identical metadata schema:

```python
# Outside FontLab
import json
from pathlib import Path
import fontlab_echopy

path = Path(fontlab_echopy.__file__).parent / "_provenance.json"
provenance = json.loads(path.read_text(encoding="utf-8"))
print(sorted(provenance))
```

A capture hash identifies input bytes, not complete behavioral coverage. Unknown
signatures remain explicit as `*args, **kwargs`. PySide2-derived signatures are
reference enrichment and may differ from FontLab's PythonQt bindings. Prefer a
measured call on the actual host when an overload or property is uncertain.

## Understand runtime shims

The `GlyphsApp`, `vanilla` and related shim declarations describe compatibility
modules supplied by other packages. They do not install Glyphs.app or turn an
offline process into a running Glyphs-compatible session. Glyport owns the
runtime providers used by adapted scripts.

Producer-derived shim freshness and native API fidelity are separate checks:

| Check | What it establishes |
| --- | --- |
| Regenerate shims against pinned producer files | Declarations match those producer inputs |
| Compare the generated files and provenance | The generated output is reproducible |
| Run offline tests | The tested Python behavior works outside FontLab |
| Run installed artifacts in FontLab | The exercised behavior works on that host build |

`fontlabapp_shim` has a separate App capture/generation route. Regenerating the
Glyport and Aidus shims does not refresh that capture or FontLab's native modules.

## Use PythonQt inside FontLab

FontLab's PythonQt exposes widgets through `QtGui`, not a `QtWidgets` namespace.
This native-only identity check does not create or show a widget:

```python
# Inside FontLab; native execution required
from PythonQt import QtGui as native_gui
from echopy.PythonQt import QtGui

assert QtGui.QWidget is native_gui.QWidget
```

Use the existing application and event loop. Do not construct `QApplication`,
start an application-wide `exec()`, or load another Qt runtime. For practical
panels, use the shared application helpers and retain their handles until close.
Do not probe every property on arbitrary native instances: some getters require
initialized native state and can crash the host. Class declarations and recorded
metadata are safer starting points for discovery.

## Check the metadata pipeline with an owned fixture

Maintainers can test capture, generation and merge without FontLab. This example
was checked with the private, uncommitted Echopy artifact
`0.2.4.dev6+ga4f2fbf48.d20261101` containing the constructor-binding and decorator-resolution repairs.
Earlier artifacts share this version but fail constructor binding or captured-name
shadowing checks; use archive hashes to identify the tested snapshot.
These fixtures are ordinary Python classes, not models of FontLab or PythonQt
and not evidence of a published release.

```python
# Outside FontLab; owned fixture, no native calls
import ast
import builtins
import inspect
from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
from fontlab_echopy.tooling.capture import namespace
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge

class Fixture:
    def __init__(receiver, value=3, /, *, label="a,b"):
        raise AssertionError("Metadata inspection must not construct instances")

    def ordinary(receiver, value=3, /, *, label="a,b"):
        raise AssertionError("Metadata inspection must not call this method")

    @staticmethod
    def measure(value=3, /, *, label="a,b"):
        raise AssertionError("Metadata inspection must not call this method")

    @classmethod
    def create(owner, value=3):
        raise AssertionError("Metadata inspection must not call this method")

    # Captured names can match Python builtins. These are ordinary methods.
    def staticmethod(receiver):
        raise AssertionError("Metadata inspection must not call this method")

    def classmethod(receiver):
        raise AssertionError("Metadata inspection must not call this method")

class StaticInit:
    @staticmethod
    def __init__(value=3, /, *, label="a,b"):
        raise AssertionError("Metadata inspection must not call constructors")

class ClassInit:
    @classmethod
    def __init__(owner, value=3, /, *, label="a,b"):
        raise AssertionError("Metadata inspection must not call constructors")

captured = namespace(
    SimpleNamespace(Fixture=Fixture, StaticInit=StaticInit, ClassInit=ClassInit),
    "owned_fixture",
)
classes = {item["name"]: item for item in captured["classes"]}
records = {item["name"]: item for item in classes["Fixture"]["methods"]}
assert records["measure"]["binding"] == "staticmethod"
assert records["create"]["binding"] == "classmethod"
assert records["create"]["signature"].startswith("(owner,")
assert records["ordinary"].get("binding") == "instancemethod"
assert classes["Fixture"]["constructors"][0]["binding"] == "instancemethod"
for name, kind in (("StaticInit", "staticmethod"), ("ClassInit", "classmethod")):
    assert classes[name]["constructors"][0].get("binding") == kind, name
assert classes["ClassInit"]["constructors"][0]["signature"].startswith("(owner,")

with TemporaryDirectory(prefix="echopy-fixture-") as folder:
    raw, merged = Path(folder) / "raw", Path(folder) / "merged"
    generate({"modules": {"owned_fixture": {"namespace": captured}}}, raw)
    merge(raw, merged, [])
    tree = ast.parse((merged / "owned_fixture.pyi").read_text(encoding="utf-8"))
    builtin_prefix = next(
        (alias.asname + "." for node in tree.body if isinstance(node, ast.Import)
         for alias in node.names if alias.name == "builtins"), ""
    )
    emitted = {node.name: node for node in tree.body if isinstance(node, ast.ClassDef)}
    cls = emitted["Fixture"]
    methods = {node.name: node for node in cls.body if isinstance(node, ast.FunctionDef)}
    for name, kind in (("measure", "staticmethod"), ("create", "classmethod")):
        assert [ast.unparse(node) for node in methods[name].decorator_list] == [builtin_prefix + kind]
        print(name, ast.unparse(methods[name].args))
    assert [arg.arg for arg in methods["measure"].args.posonlyargs] == ["value"]
    assert ast.literal_eval(methods["measure"].args.kw_defaults[0]) == "a,b"
    for name in ("ordinary", "__init__"):
        args = methods[name].args
        assert [arg.arg for arg in args.posonlyargs] == ["receiver", "value"]
        assert not args.args  # No invented self before the recorded receiver.
        assert ast.literal_eval(args.kw_defaults[0]) == "a,b"
        print(name, ast.unparse(args))
    for name, kind, arguments in (
        ("StaticInit", "staticmethod", ["value"]),
        ("ClassInit", "classmethod", ["owner", "value"]),
    ):
        constructor = next(node for node in emitted[name].body
                           if isinstance(node, ast.FunctionDef) and node.name == "__init__")
        assert [ast.unparse(node) for node in constructor.decorator_list] == [builtin_prefix + kind]
        assert [arg.arg for arg in constructor.args.posonlyargs] == arguments
        assert not constructor.args.args
        assert ast.literal_eval(constructor.args.kw_defaults[0]) == "a,b"
        assert ast.unparse(constructor.returns) == "None"

    # Execute only these owned declarations, never native captures or methods.
    for path in (raw / "owned_fixture.py", merged / "owned_fixture.pyi"):
        values = {"__name__": "echopy_doc_owned_declarations"}
        exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), values)
        for member, kind in (("measure", builtins.staticmethod),
                             ("create", builtins.classmethod)):
            assert type(inspect.getattr_static(values["Fixture"], member)) is kind
        for member in ("staticmethod", "classmethod"):
            assert inspect.isfunction(inspect.getattr_static(values["Fixture"], member))
```

The temporary files are deleted when the block finishes. Only owned generated declarations execute;
no fixture method runs and no instance is constructed. Captured builtin names
remain ordinary methods, while generated decorators retain builtin identity.
Known Python static/class descriptors preserve their binding. Known ordinary
methods and constructors preserve their recorded receiver, even when it is not
named `self`; inserting another receiver would change the callable's arguments.
This identification uses Python function descriptors, not parameter-name guesses.
Unclassified native descriptors keep the existing fallback.

Tested private archive SHA256 values:

| Archive | SHA256 |
| --- | --- |
| Wheel | `6f82d7856a52e7befb50c43e08b9786d86300303fff409dcf3bdb7a05f92e5ac` |
| sdist | `fe8ae224794fae742dfd193775febc2dd8f21d7dcf840af4edfad4e2c4f24bdb` |

A passing fixture demonstrates the metadata pipeline only. It does not establish
that every native wrapper exposes enough information to classify its methods.

For a real mismatch report, include the installed Echopy version, actual FontLab
build, relevant capture/provenance hashes, the exact declaration and the observed
call or error from an owned native fixture. Do not replace an uncertain declaration
with a guessed signature merely to silence a type checker.

## Reject ambiguous declaration names before writing

Native spellings can contain characters that Python identifiers cannot use.
For example, `A-B` and `A_B` both map to `A_B`. Emitting both would replace one
class declaration and could make a name-only coverage check look complete.
The generator rejects such collisions before writing any scope or removing stale
output. Its error identifies the owner, original spellings and shared identifier.

This example uses synthetic metadata and a disposable directory. It demonstrates
that the existing file remains byte-for-byte unchanged when generation refuses
the collision. It does not load a native module or execute generated code.

```python
# Outside FontLab; owned capture and output directory
from pathlib import Path
from tempfile import TemporaryDirectory
from fontlab_echopy.tooling.generate import generate

capture = {"modules": {"owned_collision": {"namespace": {
    "classes": [{"name": "A-B"}, {"name": "A_B"}],
}}}}
with TemporaryDirectory(prefix="echopy-collision-") as directory:
    output = Path(directory)
    previous = output / "owned_collision.py"
    previous.write_bytes(b"# Previous owned output\n")
    before = {path.name: path.read_bytes() for path in output.iterdir()}
    try:
        generate(capture, output)
    except ValueError as error:
        assert "Source name collision in owned_collision" in str(error)
        assert "'A-B'" in str(error) and "'A_B'" in str(error)
    else:
        raise AssertionError("The conflicting declarations must be refused")
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before
    for name in ("_bind", "_echopy_unavailable"):
        helper_capture = {"modules": {"owned_helper": {"namespace": {
            "functions": [{"name": name}],
        }}}}
        try:
            generate(helper_capture, output)
        except ValueError as error:
            assert "Reserved source name in owned_helper" in str(error)
            assert repr(name) in str(error)
        else:
            raise AssertionError("Captured helpers must not replace facade machinery")
        assert {path.name: path.read_bytes() for path in output.iterdir()} == before
```

Retain the capture and report the conflicting names. Do not delete a captured
member to make coverage pass. This preflight checks both declared members and
captured name inventories, across all scopes before writing. It is not a general
transaction for filesystem errors. Top-level names mapping to `Any`, `globals`,
`_bind`, `_unavailable`, `_echopy_native`, `_echopy_name`, `_echopy_aliases` or
`_echopy_unavailable` are refused because they replace facade helpers or state.
The rule also applies to normalized spellings such as `-bind` becoming `_bind`.
Same-named class members remain allowed. Other built-in shadowing and duplicate
records with an identical native spelling remain separate checks. The low-level
`module_source` renderer does not perform this whole-capture preflight.

The example requires the private helper-name preflight artifact. The earlier
deletion-repair artifact has the same version string but does not reject the
helper capture. Neither is a published release. Tested archive SHA256 values:

| Archive | SHA256 |
| --- | --- |
| Wheel | `2a18dcdcc5aeff7879a24614f27c14ec8cb44109af5db741bef132980d8416c5` |
| sdist | `fc0a00dd9d196bcaddbf47b3405a895b84db4667efacdf6303bf97d77b5e9df6` |

## Read and update a native name through its source alias

A native name such as `value-name` cannot appear after a dot in Python source.
New declarations expose it as `value_name`. The alias refers to the original
native attribute: later native changes remain visible, and writes or deletion
through the alias affect the original spelling. This applies to top-level
classes, functions, attributes, constants and modules. It does not wrap native
objects or rename members on native classes.

The following fixture generates and merges an annotated value, then loads the
small facade twice: first without a provider, then with an owned module double.
The offline annotation has no value. Ordinary native attributes also disappear
from facade lookup and `dir()` when deleted, and reappear when rebound.
The double demonstrates routing only; it
is not FontLab or a test of font mutations.

```python
# Outside FontLab; owned metadata, modules and temporary files only
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge

provider_name = "echopy_doc_owned_alias_provider"
facade_name = "echopy_doc_owned_alias_facade"
assert provider_name not in sys.modules and facade_name not in sys.modules
capture = {"modules": {provider_name: {"namespace": {
    "names": ["value-name", "ordinary"],
    "attributes": [{"name": name, "type": "int"}
                   for name in ("value-name", "ordinary")],
}}}}
with TemporaryDirectory(prefix="echopy-alias-") as directory:
    raw, merged = Path(directory) / "raw", Path(directory) / "merged"
    report = generate(capture, raw)
    assert report["modules"][provider_name]["missing_names"] == []
    merge(raw, merged, [])
    path = merged / (provider_name + ".py")
    try:
        offline = ModuleType(facade_name)
        offline.__file__ = str(path)
        sys.modules[facade_name] = offline
        exec(compile(path.read_text(), str(path), "exec"), offline.__dict__)
        assert "value_name" in offline.__annotations__
        assert not hasattr(offline, "value_name")  # No invented None value.

        provider = ModuleType(provider_name)
        provider.ordinary = 5
        setattr(provider, "value-name", 7)
        sys.modules[provider_name] = provider
        live = ModuleType(facade_name)
        live.__file__ = str(path)
        sys.modules[facade_name] = live
        exec(compile(path.read_text(), str(path), "exec"), live.__dict__)
        assert live.ordinary == 5
        del provider.ordinary
        assert not hasattr(live, "ordinary")  # No stale copied value.
        assert "ordinary" not in dir(live)
        provider.ordinary = 6
        assert live.ordinary == 6
        assert "ordinary" in dir(live)
        assert live.value_name == 7
        setattr(provider, "value-name", 9)
        assert live.value_name == 9
        live.value_name = 11
        assert getattr(provider, "value-name") == 11
        assert not hasattr(provider, "value_name")
        del live.value_name
        assert not hasattr(provider, "value-name")
        assert not hasattr(live, "value_name")
    finally:
        sys.modules.pop(facade_name, None)
        sys.modules.pop(provider_name, None)
```

The `exec` calls load only the generated owned fixture. Temporary files and
module registrations are removed even if an assertion fails. The double does not establish how
a real FontLab attribute setter affects document state. Annotation-only values remain unreadable offline,
while declared functions and constructors raise `NativeUnavailable` when called.

This example requires the private alias and ordinary-deletion repairs. The
earlier alias-only build shares the version `0.2.4.dev6+ga4f2fbf48.d20261101`
but fails the ordinary-deletion assertion. Tested archives are identified by
SHA256, not version text alone:

| Archive | SHA256 |
| --- | --- |
| Wheel | `d77ba8a507702b53382a3c9c31211ef34ec29ba809b1d1d368d878e2eb072699` |
| sdist | `1d9f9e6f203aedc513d287838705461bafa94a60fe482c61c108f313cf18b27a` |

These checks do not qualify actual native bindings, a regenerated reference site
or a published release. Existing class aliases in merged facades remain supported;
new nonidentifier declarations require reviewed generation from the capture.

## Source-derived compound metadata

The earlier GlyphsApp sidecar re-exported Glyport's `GSApplication` and
`GSGlyphInfo` classes. The current profile-aware producer declares the selected
application type and re-exports `GSGlyphInfo` and `GSGlyphsInfo`; use the generated
declarations from the existing producer CLI. The [compound guide](../guide/glyport-compounds.md) shows
nine owned checks for their raw/shared/copy/nested/positional behavior. These
are provider semantics, separate from Echopy's native FontLab declarations.

After the compound producer changes, the existing CLI regenerates all 13 source
targets. Only the GlyphsApp catalogue's producer fingerprint/capture digest
changes; its exported entries and all facade/sidecar bytes stay unchanged.
The refreshed source passes 385 tests, including 15 actual-export controls; the
older ordinary producer fails 13 of those while two single-record controls pass.
Fresh matching Echopy artifacts and the complete ordinary installed tuple remain
pending. A current source fingerprint does not prove native FontLab behavior,
proprietary data completeness or every Glyphs version.

## Selected-record descriptions

The [description guide](../guide/glyport-descriptions.md) exercises the actual
re-exported class and `desc` property through owned sessions. The description
successor adds 14 export checks: they fail against the earlier compound producer
while its 15 compound controls still pass. At that checkpoint, all 399 Echopy source tests passed.
Regeneration changes only the GlyphsApp producer fingerprint/capture digest;
exported entries, facade/sidecar bytes and protected native/legacy data stay exact.

The H producer implements the selected parent/document/shared manager and exact
Glyphs2/3/4 application contracts. The [manager guide](../guide/glyport-managers.md)
adds actual-export controls for those routes and the bounded custom file/index/
finalizer/discovery capability. The connected local-manager successor documents
actual constructor/reload/parser/sidebar dispatch with explicit invented providers;
source controls preserve queue, error and summary boundaries. Complete lawful
default/private resources, native initialization/reload, matching companion ordinary consumers, the full original HTML workflow
and native FontLab/Glyphs behavior retain separate qualification. The 399-test
description result above identifies its earlier source checkpoint.

## Verification boundaries

The offline examples can run in an ordinary Echopy installation. The two native
identity snippets require FontLab; compiling them is not native verification.
Neither example tests font edits, Undo/Redo, saving or reopening documents.

`fontlabpr` was absent in the recorded FontLab 9.0.9780 baseline. Treat that as a
build-specific observation, not a promise about every later release. Confirm
availability in the actual target host before designing a dependency on it.

Reference: [fontlab_echopy](../reference/fontlab_echopy.md), [fontlab](../reference/fontlab.md),
[fontgate](../reference/fontgate.md), [fontpr](../reference/fontpr.md),
[PythonQt](../reference/PythonQt.md), and [Glyport](glyport.md).
