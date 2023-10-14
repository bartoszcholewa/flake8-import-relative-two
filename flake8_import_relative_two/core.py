import ast

from flake8_import_relative_two.version import __version__


IRT1 = "IRT1 Level 3 of relative import found!"


class Visitor(ast.NodeVisitor):
    """NodeVisitor to report relative imports."""

    def __init__(self):
        """Create a Visitor with empty errors list."""
        self.errors = []

    def visit_ImportFrom(self, node):  # noqa: N802
        """Implement check for relative import level."""
        if node.level > 2:
            self.errors.append((node.lineno, node.col_offset, IRT1))

        self.generic_visit(node)


class Plugin:
    """Core plugin class for flake8-import-relative-two."""

    name = "flake8-import-relative-two"
    version = __version__

    def __init__(self, tree):
        """Create plugin instance from the provided AST."""
        self._tree = tree

    def run(self):
        """Traverse the AST and collect the errors."""
        visitor = Visitor()
        visitor.visit(self._tree)

        for line, col, msg in visitor.errors:
            yield line, col, msg, type(self)
