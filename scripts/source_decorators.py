# this_file: scripts/source_decorators.py
"""Prove the bounded identity-registration decorator shape against live bindings."""

import ast


def preserves_class(node: ast.AST, bindings: dict) -> bool:
    """Accept an active single-argument function with proven safe dependencies.

    A source dictionary and builtin hasattr must still have those bindings when
    the decorator is applied. Arbitrary calls, class mutation and other statement
    forms are intentionally unsupported rather than inferred to preserve identity.
    """
    if not isinstance(node, ast.FunctionDef) or node.decorator_list:
        return False
    parameters = [*node.args.posonlyargs, *node.args.args]
    if (
        len(parameters) != 1
        or node.args.vararg
        or node.args.kwarg
        or node.args.kwonlyargs
        or node.type_params
        or not node.body
        or not isinstance(node.body[-1], ast.Return)
    ):
        return False
    parameter = parameters[0].arg
    for value in ast.walk(node):
        if isinstance(value, ast.Return) and (
            not isinstance(value.value, ast.Name) or value.value.id != parameter
        ):
            return False
        if isinstance(value, (ast.Yield, ast.YieldFrom, ast.NamedExpr)):
            return False
        if (
            isinstance(value, ast.stmt)
            and value is not node
            and not isinstance(
                value, (ast.Expr, ast.If, ast.Assign, ast.Return, ast.Pass)
            )
        ):
            return False
        if isinstance(value, ast.Call) and (
            not isinstance(value.func, ast.Name)
            or value.func.id != "hasattr"
            or bindings.get("hasattr", "builtins.hasattr") != "builtins.hasattr"
            or "*" in bindings
            or parameter == "hasattr"
        ):
            return False
        if isinstance(value, ast.Assign):
            for target in value.targets:
                if (
                    not isinstance(target, ast.Subscript)
                    or not isinstance(target.value, ast.Name)
                    or target.value.id == parameter
                    or not isinstance(bindings.get(target.value.id), ast.Dict)
                ):
                    return False
    return True
