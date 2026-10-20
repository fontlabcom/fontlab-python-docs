# this_file: scripts/docstring_literals.py
"""Render reviewed upstream array-index prose as code, without editing sources.

Only six reviewed TypeRig docstrings are affected. Real Markdown cross-references
remain untouched; strict warnings remain enabled. Rules fail if their reviewed
literal disappears. Source identities and locked source bytes stay unchanged.
"""

from typing import Any

from griffe import Extension, Function

LITERALS = {
    "typerig.core.algo.matchmaker.dp_match": ["C[m][n]"],
    "typerig.core.algo.outline_cleanup.clean": ["masters[m][c]"],
    "typerig.core.algo.outline_cleanup_masters.assert_compatible": ["masters[m][c]"],
    "typerig.core.objects.matrix.Matrix.tr": ["Original[j][i]", "Transposed[i][j]"],
    "typerig.core.objects.matrix.Matrix.star": ["Original[j][i]", "Star[i][j]"],
    "typerig.core.objects.matrix.hilb": ["Elem[i][j]"],
}


class LiteralIndexes(Extension):
    """Use Griffe's documented static function-instance event before Markdown."""

    def on_function_instance(self, *, func: Function, **kwargs: Any) -> None:
        """Apply only the exact reviewed array expressions, idempotently."""
        if func.path not in LITERALS or func.docstring is None:
            return
        text = func.docstring.value
        for literal in LITERALS[func.path]:
            quoted = f"`{literal}`"
            if quoted in text:
                continue
            if literal not in text:
                raise ValueError(
                    f"Upstream docstring changed; review reviewed literal {func.path}: {literal}"
                )
            text = text.replace(literal, quoted)
        func.docstring.value = text
