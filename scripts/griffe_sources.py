# this_file: scripts/griffe_sources.py
"""Load actual source in namespace directories that Griffe skips by default."""

from pathlib import Path
from typing import Any

from griffe import Extension, Module, visit


class SourceNamespaceExtension(Extension):
    """Preserve importable namespace subpackages without editing runtime code."""

    def on_package(self, *, pkg: Any, loader: Any, **kwargs: Any) -> None:
        if isinstance(pkg.filepath, list) or Path(pkg.filepath).name not in {
            "__init__.py",
            "__init__.pyi",
        }:
            return
        root = Path(pkg.filepath).parent
        for path in sorted(root.rglob("*.py")):
            relative = path.relative_to(root)
            if (
                any(part in {"tests", "__pycache__"} for part in relative.parts)
                or path.name == "__init__.py"
            ):
                continue
            parent = pkg
            for position, part in enumerate(relative.parts[:-1]):
                member = parent.members.get(part)
                if member is None:
                    directory = root.joinpath(*relative.parts[: position + 1])
                    member = Module(
                        part,
                        filepath=[directory],
                        parent=parent,
                        modules_collection=loader.modules_collection,
                    )
                    parent.set_member(part, member)
                if not member.is_module:
                    break
                parent = member
            else:
                if path.stem not in parent.members:
                    model = visit(
                        path.stem,
                        filepath=path,
                        code=path.read_text(encoding="utf-8-sig"),
                        parent=parent,
                        modules_collection=loader.modules_collection,
                        lines_collection=loader.lines_collection,
                    )
                    parent.set_member(path.stem, model)
