---
this_file: src_docs/md/packages/instamix.md
---
# Instamix

Instamix installs extensions, scripts and Python packages into FontLab 9. It uses
only the Python standard library and runs inside FontLab's embedded Python 3.11 or
from an ordinary terminal. The package is `fontlab-python-instamix` (import
`fontlab_instamix`).

- **Extensions**: `.fontlabext` folders and `.fontlabextz` zips are copied into
  FontLab's data folder and linked into `Scripts`, `Encoding`, `Codepage`,
  `Actions`, `Data` and `python/3.11/site-packages`. A ledger records every path,
  so uninstall removes exactly what was installed and keeps files you changed.
- **Packages**: PyPI and `git+` packages go into FontLab's site-packages through
  [uv](https://docs.astral.sh/uv/).
- **Projects**: a repository with `[tool.fontlab-install]` in its `pyproject.toml`
  installs itself with a two-line `install.vfpy`.

## Install and use

Open `install.vfpy` from the repository in FontLab 9, then in FontLab's Python
panel:

```python
import fontlab_instamix as im
im.install("/path/to/com.example.hello.fontlabextz")
im.uninstall("com.example.hello")
```

The repository README documents the command line and the data-folder rules:
<https://github.com/fontlabcom/fontlab-python-instamix>.

## Reference

[fontlab_instamix](../reference/fontlab_instamix.md) lists the public API.
