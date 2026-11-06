#!/usr/bin/env python3
# this_file: tools/migrate_app_paths.py
"""Rewrite authored API paths using the configured App alias oracle (stdlib only).

Run from any directory; --check reports pending edits without writing files.
FONTLAB_API_SOURCE_ROOT selects a package root; otherwise use the sibling App.
The migration regression fixtures deliberately retain their legacy inputs.
"""

import argparse
import importlib.util
import os
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
AREAS = ('scripts', 'tests', 'src_docs')
LEGACY_FIXTURES = {
    'tests/test_migrate_app_paths.py',
    'WORK.md',
    'src_docs/md/licenses/fontlabapp-notice.txt',  # Historical source attribution.
}
EXPLICIT = {
    "fontlab_fontport.ui": "fontlabapp.fontui",
    "fontlab_fontport.feature_blocks": "fontlabapp.fontui.feature_blocks",
    "fly.fp.ui": "fly.ap.fontui",
    "fly.fp.feature_blocks": "fly.ap.fontui.feature_blocks",
    "fontlab_remopy.control": "fontlab_remopy.client",
    "fontlab_remopy.controls": "fontlab_remopy.actions",
    "fontlab_remopy.functions": "fontlab_remopy.remote",
    "fontlab_remopy.execution": "fontlab_remopy.results",
    "fontlab_remopy.native": "fontlab_remopy.host",
    "fontlab_remopy.mcp_bridge": "fontlab_remopy.mcp.relay",
}


def load_mapping() -> dict[str, str]:
    """Load only _legacy.py, without importing native App or Qt."""
    artifact_root = os.environ.get("FONTLAB_API_SOURCE_ROOT")
    source = (Path(artifact_root).expanduser().resolve() if artifact_root
              else ROOT.parent / "fontlab-fontlabapp/src")
    path = source / "fontlabapp/_legacy.py"
    spec = importlib.util.spec_from_file_location("_migration_legacy", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    mapping = dict(module.ALIASES)
    mapping.update({old.replace("fontlabapp", "fly.ap", 1):
                    new.replace("fontlabapp", "fly.ap", 1)
                    for old, new in module.ALIASES.items()})
    mapping |= EXPLICIT
    # Reference URLs use the same module paths with slash separators.
    mapping.update({old.replace(".", "/"): new.replace(".", "/")
                    for old, new in tuple(mapping.items())})
    return mapping


def rewrite(text: str, mapping: dict[str, str]) -> str:
    """Keep canonical packages stable; replace complete dotted prefixes once."""
    protected = {value for value in mapping.values()}
    for value in tuple(protected):
        separator = "/" if "/" in value else "."
        parts = value.split(separator)
        protected.update(separator.join(parts[:i]) for i in range(1, len(parts)))
    replacements = {name: name for name in protected if name not in mapping} | mapping
    pattern = re.compile(r"(?<![\w.])(?:" + "|".join(
        re.escape(name) for name in sorted(replacements, key=lambda s: (-len(s), s))
    ) + r")(?!\w)")

    def from_import(match: re.Match) -> str:
        indent, parent, names = match.groups()
        imports = []
        for item in names.split(","):
            name, *alias = item.strip().split(" as ")
            old = parent + "." + name
            if old in mapping:
                imports.append(f"{indent}import {mapping[old]} as {alias[0] if alias else name}")
            else:
                imports.append(f"{indent}from {parent} import {item.strip()}")
        return "\n".join(imports)

    # Preserve local bindings for imports that formerly relied on root __getattr__.
    parents = "fontlabapp|fly\\.ap|fontlab_fontport|fly\\.fp|fontlab_remopy"
    text = re.sub(r"^( *)(?:from) (" + parents + r") import (\w+(?: as \w+)?(?:, *\w+(?: as \w+)?)*)$",
                  from_import, text, flags=re.MULTILINE)
    text = pattern.sub(lambda match: replacements[match.group()], text)
    # api_module records contain App-relative paths rather than full import names.
    return re.sub(
        r'''(["']api_module["'](?:\s*:\s*|\]\s*==\s*))(["'])(\w+)\2''',
        lambda match: match[1] + match[2] + mapping.get(
            "fontlabapp." + match[3], "fontlabapp." + match[3]
        ).removeprefix("fontlabapp.") + match[2], text,
    )


def migrate(root: Path, mapping: dict[str, str], check: bool = False) -> list[str]:
    """Rewrite authored text; skip archives, caches and legacy test fixtures."""
    paths = list(root.glob("*.md"))
    for area in AREAS:
        paths.extend((root / area).rglob("*"))
    changed = []
    for path in sorted(paths):
        relative = path.relative_to(root)
        if (not path.is_file() or path.is_symlink()
                or any(part.startswith(".") or part == "_reference" for part in relative.parts)
                or relative.as_posix() in LEGACY_FIXTURES
                or path.suffix not in {".py", ".md", ".rst", ".txt", ".json", ".toml", ".yaml", ".yml", ".html"}):
            continue
        original = path.read_text(encoding="utf-8")
        updated = rewrite(original, mapping)
        if original != updated:
            changed.append(relative.as_posix())
            if not check:
                path.write_text(updated, encoding="utf-8")
    return changed


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    changed = migrate(ROOT, load_mapping(), args.check)
    print("\n".join(changed) if changed else "No pending API path changes")
    raise SystemExit(bool(changed) if args.check else 0)
