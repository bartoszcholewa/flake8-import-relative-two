# flake8-import-relative-two
============================
*Flake8 plugin that checks for relative imports up to a maximum of level two*

**Current Development Version:**

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bartoszcholewa/flake8-import-relative-two/ci_tests.yml?branch=main&logo=github)](https://github.com/bartoszcholewa/flake8-import-relative-two/actions)
[![codecov](https://codecov.io/gh/bartoszcholewa/flake8-import-relative-two/graph/badge.svg?token=RQ7LU60OYQ)](https://codecov.io/gh/bartoszcholewa/flake8-import-relative-two)

**Most Recent Stable Release:**

[![pypi](https://img.shields.io/pypi/v/flake8-import-relative-two.svg?logo=pypi)](https://pypi.org/project/flake8-import-relative-two)
![pypi](https://img.shields.io/pypi/pyversions/flake8-import-relative-two.svg?logo=python)

**Info:**

[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/bartoszcholewa/flake8-import-relative-two/blob/stable/LICENSE.txt)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://pepy.tech/badge/flake8-import-relative-two/month)](https://pepy.tech/project/flake8-import-relative-two)

----

Plugin created for linting relative imports up to a maximum of level two.
One of private projects I work on has a rule that forbids relative imports deeper than two levels and need to be converted to absolute imports.

Plugin created based on [flake8-absolute-import](https://github.com/bskinn/flake8-absolute-import) by Brian Skinn,
with help from [youtube video](https://www.youtube.com/watch?v=ot5Z4KQPBL8&t=926s&ab_channel=anthonywritescode)


`flake8-import-relative-two` uses a direct check of the AST for each
`from ...x import y` statement to flag relative imports deeper than two levels.

Relative imports raise the ``IRT1`` error code:

```python
from foo import bar   # OK
from .foo import bar   # OK
from ..foo import bar   # OK
from ...foo import bar  # IRT1
```


Available on [PyPI](https://pypi.python.org/pypi/flake8-import-relative-two)(`pip install flake8-import-relative-two`).

`flake8` should automatically detect and load the plugin.

`flake8`>=6.0 is required.

Source on [GitHub](https://github.com/bartoszcholewa/flake8-import-relative-two)

Bug reports and feature requests are welcomed at the [Issues](https://github.com/bartoszcholewa/flake8-import-relative-two/issues) page there.

Copyright (c) Bartosz Cholewa 2023

The `lake8-import-relative-two` documentation (including docstrings and README) is licensed under a
[Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/) (CC-BY).

The `lake8-import-relative-two` codebase is released under the [MIT License](https://opensource.org/licenses/MIT). See
[LICENSE.txt](https://github.com/bartoszcholewa/flake8-import-relative-two/blob/main/LICENSE.txt) for
full license terms.