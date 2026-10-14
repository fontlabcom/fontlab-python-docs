# this_file: scripts/source_bindings.py
"""Track class base bindings in source order, without evaluating Python code."""

import ast
from importlib.util import resolve_name


def _reference(node: ast.AST) -> str | None:
    """Accept only names and dotted attributes; calls/subscripts remain unknown."""
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        origin = _reference(node.value)
        return origin + "." + node.attr if origin else None
    return None


def _effects(node: ast.AST):
    """Collect possible writes, excluding deferred function/class bodies."""
    if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
        yield node.name
        for field, value in ast.iter_fields(node):
            if field == "body":
                continue
            for child in value if isinstance(value, list) else [value]:
                if isinstance(child, ast.AST):
                    yield from _effects(child)
        return
    if isinstance(node, ast.Import):
        yield from (item.asname or item.name.split(".")[0] for item in node.names)
    elif isinstance(node, ast.ImportFrom):
        yield from (item.asname or item.name for item in node.names)
    elif isinstance(node, ast.Name) and isinstance(node.ctx, (ast.Store, ast.Del)):
        yield node.id
    elif isinstance(node, ast.Attribute) and isinstance(node.ctx, (ast.Store, ast.Del)):
        reference = _reference(node)
        if reference:
            yield reference.partition(".")[0]
    elif (
        isinstance(node, (ast.ExceptHandler, ast.MatchAs, ast.MatchStar)) and node.name
    ):
        yield node.name
    elif isinstance(node, ast.MatchMapping) and node.rest:
        yield node.rest
    elif isinstance(node, (ast.Global, ast.Nonlocal)):
        yield from node.names
    elif isinstance(node, ast.Call) and _reference(node.func) in {
        "exec",
        "eval",
        "globals",
        "locals",
        "vars",
    }:
        yield "*"
    for child in ast.iter_child_nodes(node):
        yield from _effects(child)


def bind_bases(records: list, classes: dict, aliases: dict) -> set[str]:
    """Set canonical targets at each class declaration; return unresolved owners.

    Class headers see the surrounding class namespace. A nested class body gets
    its own namespace plus module globals, not its enclosing class's namespace.
    Conditional writes and dynamic namespace effects invalidate prior knowledge.
    Imported paths use the inventory's existing explicit export-chain resolver.
    """
    unresolved = set()
    modules = {name: record for record in records for name in (record[1], record[2])}
    namespaces, class_namespaces, pending = {}, {}, set()
    identity_decorators = set()
    for record in records:
        dictionaries = {
            target.id
            for statement in record[5].body
            if isinstance(statement, ast.Assign)
            and isinstance(statement.value, ast.Dict)
            for target in statement.targets
            if isinstance(target, ast.Name)
        }
        for node in record[5].body:
            if not isinstance(node, ast.FunctionDef) or node.decorator_list:
                continue
            parameters = [*node.args.posonlyargs, *node.args.args]
            if (
                len(parameters) != 1
                or not node.body
                or not isinstance(node.body[-1], ast.Return)
            ):
                continue
            parameter = parameters[0].arg
            returns = [
                value for value in ast.walk(node) if isinstance(value, ast.Return)
            ]
            effects = {name for statement in node.body for name in _effects(statement)}
            unsafe = any(
                isinstance(value, (ast.Yield, ast.YieldFrom))
                or isinstance(value, ast.stmt)
                and value is not node
                and not isinstance(
                    value, (ast.Expr, ast.If, ast.Assign, ast.Return, ast.Pass)
                )
                or isinstance(value, ast.NamedExpr)
                or isinstance(value, ast.Call)
                and _reference(value.func) != "hasattr"
                or isinstance(value, ast.Assign)
                and any(
                    not isinstance(target, ast.Subscript)
                    or not isinstance(target.value, ast.Name)
                    or target.value.id not in dictionaries
                    for target in value.targets
                )
                for value in ast.walk(node)
            )
            if (
                parameter not in effects
                and "*" not in effects
                and all(
                    isinstance(value.value, ast.Name) and value.value.id == parameter
                    for value in returns
                )
                and not unsafe
            ):
                identity_decorators.add(record[1] + "." + node.name)

    def member(origin, name):
        origin = aliases.get(origin, origin)
        target = origin + "." + name
        record = modules.get(origin)
        if record:
            if record[1] in pending:
                return target if target in modules else None
            namespace = bind(record)
        else:
            namespace = class_namespaces.get(origin, {})
        if name in namespace:
            return namespace[name]
        return (
            aliases.get(target, target) if target in modules or not namespace else None
        )

    def star_exports(origin):
        origin = aliases.get(origin, origin)
        record = modules.get(origin)
        if record is None or record[1] in pending:
            return None
        names = bind(record)
        exports = None
        for statement in record[5].body:
            if "__all__" not in _effects(statement):
                continue
            if not isinstance(statement, (ast.Assign, ast.AnnAssign)):
                return None
            try:
                exports = ast.literal_eval(statement.value)
            except (ValueError, TypeError):
                return None
            if not isinstance(exports, (list, tuple)) or not all(
                isinstance(name, str) for name in exports
            ):
                return None
        if "*" in names or (exports is None and "__getattr__" in names):
            return None
        public = (
            exports
            if exports is not None
            else [name for name in names if not name.startswith("_")]
        )
        return {name: names.get(name) for name in public}

    def bind(record):
        relative, module, _, source, _, tree, _ = record
        if module in namespaces:
            return namespaces[module]
        pending.add(module)
        context = module if relative.name == "__init__" else module.rpartition(".")[0]
        globals_ = {}

        def lookup(expression, names):
            first, _, suffix = expression.partition(".")
            origin = names.get(first) if first in names else globals_.get(first)
            if origin is None:
                if (
                    first == "object"
                    and not suffix
                    and first not in names
                    and first not in globals_
                ):
                    return "builtins.object"
                return None
            for name in suffix.split(".") if suffix else []:
                origin = member(origin, name)
                if origin is None:
                    return None
            return aliases.get(origin, origin)

        def invalidate(node, names):
            for name in _effects(node):
                if name == "*":
                    names.update(dict.fromkeys(globals_))
                    names.update(dict.fromkeys(names))
                    names["object"] = None
                    names["*"] = None
                else:
                    names[name] = None

        def walk(body, parent, names):
            global_names = set()
            for node in body:
                if isinstance(node, ast.ClassDef):
                    identifier = parent + "." + node.name
                    row = classes.get(identifier)
                    known = (
                        row
                        and row["source"] == source
                        and row["line"] == node.lineno
                        and sum(
                            d["kind"] == "class" for d in row.get("declarations", [])
                        )
                        <= 1
                    )
                    for expression in [
                        *node.decorator_list,
                        *node.bases,
                        *node.keywords,
                    ]:
                        invalidate(expression, names)
                    parameters = {
                        parameter.name: None for parameter in node.type_params
                    }
                    header = {**names, **parameters} if parameters else names
                    if known:
                        for base, expression in zip(row.get("bases", []), node.bases):
                            reference = _reference(expression)
                            target = lookup(reference, header) if reference else None
                            base["target"] = target if target in classes else None
                            if target not in classes and target != "builtins.object":
                                unresolved.add(identifier)
                    # Bind the class name only after its body finishes.
                    walk(node.body, identifier, parameters)
                    class_namespaces[identifier] = parameters
                    names[node.name] = (
                        identifier
                        if known
                        and all(
                            lookup(reference, names) in identity_decorators
                            if (reference := _reference(decorator))
                            else False
                            for decorator in node.decorator_list
                        )
                        else None
                    )
                elif isinstance(node, ast.Import):
                    for item in node.names:
                        names[item.asname or item.name.split(".")[0]] = (
                            item.name if item.asname else item.name.split(".")[0]
                        )
                elif isinstance(node, ast.ImportFrom):
                    origin = "." * node.level + (node.module or "")
                    origin = resolve_name(origin, context) if node.level else origin
                    for item in node.names:
                        if item.name == "*":
                            exports = star_exports(origin)
                            if exports is None:
                                invalidate(node, names)
                            else:
                                names.update(exports)
                        else:
                            names[item.asname or item.name] = member(origin, item.name)
                elif isinstance(node, (ast.Assign, ast.AnnAssign)):
                    # An annotation without a value does not bind its name.
                    if isinstance(node, ast.AnnAssign) and node.value is None:
                        continue
                    reference = _reference(node.value)
                    target = lookup(reference, names) if reference else None
                    invalidate(node, names)
                    targets = (
                        node.targets if isinstance(node, ast.Assign) else [node.target]
                    )
                    for assigned in targets:
                        if isinstance(assigned, ast.Name):
                            names[assigned.id] = target if target in classes else None
                elif isinstance(node, ast.Delete):
                    for target in node.targets:
                        if isinstance(target, ast.Name):
                            names.pop(target.id, None)
                        else:
                            invalidate(target, names)
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    invalidate(node, names)
                    names[node.name] = (
                        parent + "." + node.name if not node.decorator_list else None
                    )
                else:
                    invalidate(node, names)
                if (
                    isinstance(node, (ast.Global, ast.Nonlocal))
                    and names is not globals_
                ):
                    global_names.update(node.names)
                for name in global_names:
                    names[name] = globals_[name] = None

        walk(tree.body, module, globals_)
        pending.remove(module)
        namespaces[module] = globals_
        return globals_

    for record in records:
        bind(record)
    # Unvisited/ambiguous declaration occurrences are never resolved by text.
    for identifier, row in classes.items():
        for base in row.get("bases", []):
            if "target" not in base:
                base["target"] = None
                unresolved.add(identifier)
    return unresolved
