---
this_file: src_docs/md/packages/instamix.md
---
# Instamix

Instamix installs Python distributions, source projects and ready extensions into
FontLab's user data folder. Its bootstrap uses only Python's standard library;
small selection and message helpers import FontLab's PythonQt lazily. It does
not provide another application window or a second Qt runtime.

## Start with the standalone installer

Download the standalone
[install.vfpy](https://code.fontlab.com/fontlab-python-instamix/install.vfpy)
and open it in FontLab. Use **1.0.9 or newer** before upgrading legacy installations: 1.0.8
could remove other legacy-owned files when replacement failed. Current generated
project stubs check for the corrected rollback capability before deployment;
they replace an older provider through the validated wheel bootstrap or stop if
replacement fails. See [Install and connect](../guide/install.md).

## Python entry points

These root functions are lazy exports. Importing Instamix does not import native
FontLab modules:

```python
from pathlib import Path
import fontlab_instamix as im

im.install_packages("fonttools>=4")
records = im.install(Path("tools.fontlabextz"))
print(im.installed())
kept_paths = im.uninstall("com.example.tools")
```

`install_packages(*specs, data=None)` accepts distribution requirements, including
`git+` URLs. It refreshes import caches; it does not infer a distribution from an
import name or reload an imported binary module. `install(path, data=None)`
accepts an extension folder, its root `manifest.fontlabextj`, or an archive.
`installed(data=None)` returns installation records; `uninstall(id, data=None)`
returns paths kept because the deployed files changed.

`install_project(start, data=None)` reads the nearest `pyproject.toml` at or above
a source path. Its `[tool.fontlab-install]` table names packages, Scripts,
bundles and requirements. Generate its shared entry point with:

```sh
uvx --from "fontlab-python-instamix>=1.0.9" fontlab-instamix stub path/to/project
```

The command refuses an existing `install.vfpy` unless `--force` is explicit.
`data_dir(explicit=None)` resolves the data folder; the explicit argument wins,
then `FONTLAB_DATA_DIR`, native `dataPathDefault`, and the platform default.
When the app's custom `dataPath` differs, pass that chosen path explicitly.

## Targets and the shared environment

Inside FontLab, target discovery uses the embedded Python major/minor version
and process architecture. Outside it, defaults mean FontLab 9's Python 3.11 on
the current OS and architecture, not a remotely discovered host. `python_version()`
reports the actual running Python; it is not the standalone installation default.

Target helpers belong to the `env` submodule, not the root lazy exports:

```python
from pathlib import Path
from fontlab_instamix import env, packages

chosen = env.Target("3.11", "darwin", "arm64")
data = env.data_dir(Path("scratch/FontLab 9"))
print(env.site_packages(data, version=chosen.version))
# Explicit provider operation; this does not contact a running FontLab:
packages.install(data, ["fonttools>=4"], target=chosen)
```

Use `"win32"` and `"x86_64"` for a Windows x64 target. uv selects a matching
standalone interpreter, kept separate from FontLab's executable. The verified
`<data>/.venv` reads the canonical `<data>/python/<version>/site-packages`
directory through its own managed `.pth`; packages install into that canonical
directory. uv is kept under `<data>/python/uv`. An incompatible venv or unrelated
managed-path file is refused without replacement.

The external CLI has `env`, `pkg`, `ext`, `bootstrap`, `wrap`, `pack`, `stub`,
`uv` and `venv` commands. Put global options before the subcommand:

```sh
fontlab-instamix --data-dir "scratch/FontLab 9" env
fontlab-instamix --data-dir "scratch/FontLab 9" pkg install fonttools
```

Optional Remopy enables `--remote`, where the host supplies target facts and a
shared-filesystem nonce proves access. uv work runs externally. A timeout is not
host cancellation; no automatic replay is safe. The 9.1.9813 bridge defect and
its direct-script alternative are described in [Install and connect](../guide/install.md#connect-from-another-process).

## Extension folders and archives

A canonical `com.example.tools.fontlabext` folder contains a root manifest:

```json
{
  "id": "com.example.tools",
  "name": "Example Tools",
  "version": "1.0.0",
  "python": {"requires": ["fonttools>=4"]},
  "install": [{"from": "scripts", "to": "Scripts/{}"}]
}
```

Its `scripts` directory supplies the payload. The manifest id must match the
folder name without `.fontlabext`. A `.fontlabextz` ZIP contains one or more whole
extension folders, not just their contents; the download's basename has no
identity meaning. Extensions are retained under `Extensions/Library`, then
linked or copied into normal deployment locations. Production scripts use those
normal locations, not Library paths.

Targets include `Scripts`, `Actions`, `Codepage`, `Encoding`, `Data` and
`site-packages`. `Scripts/.` means that target's root; `{}` expands to the
extension id, and `{name}` reads `vars.name`. Absolute paths, parent escapes,
unknown targets/variables and ambiguous archive identities are refused. Optional
archive installer hooks require explicit `run_hooks=True`; remote hook execution
is refused. Install records still track each extension separately.

Wrap a single script without executing it, or pack several complete extensions:

```sh
fontlab-instamix wrap width_report.py --out dist --id com.example.width-report --name "Width Report" --version 1.0.0 --zip
fontlab-instamix pack com.example.first.fontlabext com.example.second.fontlabext --out tools.fontlabextz
```

For draft plugins, add explicit `--kind`, `--plugin-id`, `--name`, `--entry` and
`--min-app-version`. Canonical suffixes are `.fontlabreporter`, `.fontlabfilter`,
`.fontlabtool`, `.fontlabpalette` and `.fontlabgeneral`; use App 1.2.31 or newer.
Wrapping validates metadata without importing the draft or proving native behavior.

Inside a script, `from fontlab_instamix.gui import install_selected` followed by
`install_selected()` selects multiple archives/manifests. `folder=True` selects
one extension directory. These are optional PythonQt helpers, not a standalone GUI.

## Upgrades, removal and failures

Current project upgrades restore affected legacy-owned files, links, modes and
receipts if replacement fails. An owner-edited or unowned conflict is a reason
to stop and inspect the named path, not to delete it. If restoration fails, the
exception names a retained recovery folder; keep that folder and its mapping.
The transaction covers the project's deployed files and ownership records;
separately installed dependencies and completed independent installs can remain.

An error can carry `installed_records` for work completed before a later failure.
A multi-extension archive must not be treated as all-or-nothing without checking
that result. Uninstall preserves changed deployed files and leaves separately
installed shared Python dependencies. Keep filesystem/native tests, ordinary
wheel installation and actual FontLab/Windows acceptance separate.
