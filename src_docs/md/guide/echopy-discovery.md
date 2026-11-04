---
this_file: src_docs/md/guide/echopy-discovery.md
---

# Find API scopes before measuring declaration coverage

A report can declare every name it captured while missing an entire namespace.
Echopy now restores the useful discovery behavior of the retained introspection
tools: it combines advertised and stored names, discovers loaded PythonQt
children and tries qualified imports when a child is absent from the root.
It preserves ordinary inspection failures instead of silently counting them as
successful absence.

These five independent experiments use owned Python objects and the actual
maintained tooling. Run each block in a fresh namespace. They require the
discovery repair from Echopy's `issue-123-capture-discovery-20261102` feature;
older versions omit some of these scopes. No FontLab, Qt, native framework,
font, preference or user document is accessed. Temporary generated declarations
in the last experiment belong only to its disposable owned directory.

The experiments verify source behavior, not the deployed FontLab API. Existing
native-capture, generated-reference, source-lock, site and publication holds
remain in force. A successful example does not authorize refreshing those inputs.
For live attribute delegation, see [native values and aliases](echopy-values.md).

## Retain names hidden by a custom directory listing

`dir()` is useful discovery evidence, but a custom implementation can omit public
dictionary names. The collector unions both sources, removes duplicates and
dunder names, and sorts the result. It records names and types rather than values.

<!-- example: echopy-discovery-hidden-names -->
```python
from types import ModuleType
from fontlab_echopy.tooling.capture import namespace

class Partial(ModuleType):
    def __dir__(self):
        return ["advertised", "advertised", "__doc__"]

owned = Partial("owned_example")
owned.advertised, owned.stored = 1, 2
scope = namespace(owned, owned.__name__)
assert scope["names"] == ["advertised", "stored"]
assert scope["errors"] == []
assert all("value" not in item for item in scope["attributes"])
```

## Discover a loaded child without replacing the root's object

PythonQt can expose pseudo-namespaces as root attributes, separately registered
modules, or importable children. Resolution prefers the root object, then the
registered immediate child, then a qualified import. A registry name such as
`PythonQt.A.B` identifies candidate `A`; it does not invent a flattened `A.B`.
Registry keys are snapshotted before imports can modify them.

This experiment temporarily installs only owned module entries and restores them
on leaving the context. Empty seeds keep the experiment entirely within those
owned objects; they do not model every actual PythonQt namespace.

<!-- example: echopy-discovery-registry -->
```python
import sys
from types import ModuleType
from unittest.mock import patch
from fontlab_echopy.tooling import capture as tool

root = ModuleType("PythonQt")
registered = ModuleType("PythonQt.QtOwnedGuide")
registered.from_registry = 1
with patch.dict(sys.modules, {"PythonQt": root, registered.__name__: registered}):
    with patch.object(tool, "QT_SEEDS", ()):
        first = tool.capture(["PythonQt"])["modules"]["PythonQt"]
        assert first["subpackages"]["QtOwnedGuide"]["namespace"]["names"] == ["from_registry"]
        authoritative = ModuleType("PythonQt.QtOwnedGuide")
        authoritative.from_root = 1
        root.QtOwnedGuide = authoritative
        second = tool.capture(["PythonQt"])["modules"]["PythonQt"]
        assert second["subpackages"]["QtOwnedGuide"]["namespace"]["names"] == ["from_root"]
```

## Distinguish an absent optional child from a broken dependency

An import reporting that the requested child does not exist is an optional
absence. A missing dependency inside that child is an inspection failure.
The latter keeps its child name and exception type in the report; it must not
become a successful empty namespace. Exception messages and local paths are not
copied into the error record. The following import hook is an owned experiment,
not a substitute implementation of discovery.

<!-- example: echopy-discovery-dependency -->
```python
from types import ModuleType
from unittest.mock import patch
from fontlab_echopy.tooling import capture as tool

def missing_dependency(name):
    raise ModuleNotFoundError("owned failure", name="owned_dependency")

root = ModuleType("PythonQt")
with patch.object(tool, "resolve", return_value=root):
    with patch.object(tool, "QT_SEEDS", ("QtOwnedGuide",)):
        with patch("importlib.import_module", side_effect=missing_dependency):
            item = tool.capture(["PythonQt"])["modules"]["PythonQt"]
assert item["subpackages"] == {}
assert item["namespace"]["errors"] == [{"name": "QtOwnedGuide", "error": "ModuleNotFoundError"}]
```

## Treat a deadline as cancellation

Ordinary discovery errors preserve other usable scopes. Timeouts, keyboard
interrupts and process-exit signals propagate. In particular, swallowing a host
trace deadline can disable its execution guard. A failed root getter is recorded
once and is not retried by child discovery.

<!-- example: echopy-discovery-deadline -->
```python
from fontlab_echopy.tooling.capture import namespace

class Deadline:
    def __dir__(self):
        raise TimeoutError("owned deadline")

try:
    namespace(Deadline(), "owned_deadline")
except TimeoutError as error:
    assert str(error) == "owned deadline"
else:
    raise AssertionError("A deadline must not become partial API success")
```

## Verify the discovered scope reaches declarations

Discovery is only the first stage. This final experiment sends a registered
owned namespace through actual capture, generation and merge, then parses its
sidecar. It never instantiates its API class or calls its operation. Its zero
missing-name count is meaningful only for this explicit owned scope.

<!-- example: echopy-discovery-pipeline -->
```python
import ast
import sys
from pathlib import Path
from tempfile import TemporaryDirectory
from types import ModuleType
from unittest.mock import patch
from fontlab_echopy.tooling import capture as tool
from fontlab_echopy.tooling.generate import generate
from fontlab_echopy.tooling.merge import merge

class Owned:
    def operation(self, amount=3):
        raise AssertionError("Documenting an API must not invoke it")

root, child = ModuleType("PythonQt"), ModuleType("PythonQt.QtOwnedGuide")
child.Owned = Owned
with patch.dict(sys.modules, {"PythonQt": root, child.__name__: child}):
    with patch.object(tool, "QT_SEEDS", ()):
        data = tool.capture(["PythonQt"])
with TemporaryDirectory() as folder:
    raw, merged = Path(folder) / "raw", Path(folder) / "merged"
    report = generate(data, raw)
    merge(raw, merged, [])
    assert report["modules"][child.__name__]["missing_names"] == []
    tree = ast.parse((merged / "PythonQt/QtOwnedGuide.pyi").read_text())
cls = next(node for node in tree.body if isinstance(node, ast.ClassDef))
operation = next(node for node in cls.body if isinstance(node, ast.FunctionDef) and node.name == "operation")
assert ast.literal_eval(operation.args.defaults[0]) == 3
```

Actual completeness still requires an approved capture from the intended FontLab
build, reconciliation against the real bindings and native behavior checks.
Neither a retained capture nor these experiments supply the missing historical
complete code-shadow archive or Aidus inventory. Preserve those provenance gaps
and the legacy recovery source until migration and retirement gates pass.
