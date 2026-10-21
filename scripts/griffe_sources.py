# this_file: scripts/griffe_sources.py
"""Load actual source in namespace directories that Griffe skips by default."""

import ast
import re
from pathlib import Path
from typing import Any

from griffe import Attribute, Extension, Module, visit


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
                        extensions=loader.extensions,
                        parent=parent,
                        modules_collection=loader.modules_collection,
                        lines_collection=loader.lines_collection,
                    )
                    parent.set_member(path.stem, model)


class TupleAssignmentExtension(Extension):
    """Declare each name of `A, B = 0, 1` as an attribute, like the inventory does.

    Griffe does not model tuple-unpacked assignments; without this the coverage
    report lists identities that mkdocstrings cannot collect.
    """

    def _add(self, node: Any, owner: Any) -> None:
        for statement in getattr(node, "body", []):
            if not (isinstance(statement, ast.Assign) and len(statement.targets) == 1):
                continue
            target = statement.targets[0]
            if not isinstance(target, (ast.Tuple, ast.List)) or not all(
                isinstance(element, ast.Name) for element in target.elts
            ):
                continue
            value = statement.value
            values = (
                value.elts
                if isinstance(value, (ast.Tuple, ast.List)) and len(value.elts) == len(target.elts)
                else [value] * len(target.elts)
            )
            for element, item in zip(target.elts, values):
                if element.id not in owner.members:
                    owner.set_member(
                        element.id,
                        Attribute(
                            element.id,
                            value=ast.unparse(item),
                            lineno=statement.lineno,
                            endlineno=statement.end_lineno,
                        ),
                    )

    def on_module_members(self, *, node: Any, mod: Any, **kwargs: Any) -> None:
        self._add(node, mod)

    def on_class_members(self, *, node: Any, cls: Any, **kwargs: Any) -> None:
        self._add(node, cls)


# Elements whose content is raw text, or that restructure a document. In a
# docstring they are always literal prose (`<title>` as a placeholder) and,
# rendered as HTML, swallow the rest of the page and its search rows.
SWALLOWING = re.compile(
    r"<(/?)(title|textarea|script|style|xmp|iframe|noembed|noframes|noscript"
    r"|plaintext|html|head|body|meta|link|base)\b",
    re.IGNORECASE,
)
CODE = re.compile(r"(^[ \t]*(?:```|~~~).*?^[ \t]*(?:```|~~~)[^\n]*$|`[^`\n]+`)", re.DOTALL | re.MULTILINE)


def escape_swallowing_tags(text: str) -> str:
    """Escape swallowing tags outside code fences and code spans."""
    parts = CODE.split(text)
    return "".join(
        part if index % 2 else SWALLOWING.sub(r"&lt;\1\2", part)
        for index, part in enumerate(parts)
    )


class SwallowingTagExtension(Extension):
    """Keep literal `<title>`-like text from becoming page-breaking HTML."""

    def on_instance(self, *, obj: Any, **kwargs: Any) -> None:
        if obj.docstring is not None:
            obj.docstring.value = escape_swallowing_tags(obj.docstring.value)
