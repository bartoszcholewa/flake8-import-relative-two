import ast
from textwrap import dedent

import pytest

from flake8_import_relative_two import Plugin


def is_three_level_relative(import_source):
    """
    Indicate if a given 'from {source}' import location
    is a three-level relative import.
    """
    return import_source.startswith("...")


def format_id(id_):
    """
    Provide parametrization id formatting
    for the given id.
    """
    return f"{id_} (expect {'' if is_three_level_relative(id_) else 'no '}error)"


@pytest.mark.parametrize(
    "code",
    [
        "import sys",
        "import flake8_import_relative_two",
        "import flake8_import_relative_two.core",
        "from . import __version__",
        "from .core import Plugin",
        "from ..foo import bar",
    ]
)
def test_module_import(code):
    """Confirm no error found on module import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "code",
    [
        "from sys import argv",
        "from flake8_import_relative_two import Plugin",
        "from flake8_import_relative_two.core import Plugin",
    ],
)
def test_absolute_import(code):
    """Confirm no error found on absolute member import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize(
    "code", ["from .core import Plugin", "from . import __version__"]
)
def test_relative_import(code):
    """Confirm error *IS NOT* found on relative member import."""
    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


def test_multiple_relative_imports():
    """Confirm *NO* errors found on one-level relative member imports."""
    code = "from .core import Plugin\nfrom . import __version__"

    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


def test_correct_relative_import_linenos():
    """Confirm the multiple errors are reported on the correct lines."""
    code = dedent(
        """\
    from ...core import Plugin
    from ..core import Visitor
    from . import __version__
    from flake8_import_relative_two.core import Visitor
    from . import __version__
    from ...core import Plugin
    from ....core import Visitor
    from .....core import Plugin
    """
    )

    tree = ast.parse(code)
    assert {t[0] for t in Plugin(tree).run()} == {1, 6, 7, 8}


def test_multilevel_relative_import():
    """Confirm error is *NOT* found with a two-level relative import."""
    code = "from ..foo import bar"

    tree = ast.parse(code)
    assert len(list(Plugin(tree).run())) == 0


@pytest.mark.parametrize("impfrom", ["..mod", "...mod",], ids=format_id)
def test_func_imports(impfrom):
    """Confirm plugin works for imports in functions."""
    code = dedent(
        f"""
    def func():
        from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("..."))


@pytest.mark.parametrize("impfrom", ["..mod", "...mod"], ids=format_id)
def test_class_imports(impfrom):
    """Confirm plugin works for imports in class bodies."""
    code = dedent(
        f"""
    class Bar:
        from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("..."))


@pytest.mark.parametrize("impfrom", ["..mod", "....mod"], ids=format_id)
def test_method_imports(impfrom):
    """Confirm plugin works for imports in class methods."""
    code = dedent(
        f"""
    class Bar:
        def baz(self):
            from {impfrom} import foo
    """
    )

    tree = ast.parse(code)
    assert (len(list(Plugin(tree).run())) == 1) == (impfrom.startswith("..."))
