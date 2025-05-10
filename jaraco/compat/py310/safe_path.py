"""
Applies backward compatibility to honor PYTHONSAFEPATH.
"""

import contextlib
import os
import sys


def ensure_safe_path() -> None:
    """
    Ensure that '.' isn't on sys.path.

    >>> ensure_safe_path()
    """
    with contextlib.suppress(ValueError):
        sys.path.remove('')
    with contextlib.suppress(ValueError):
        sys.path.remove(os.path.abspath(''))


if sys.version_info < (3, 11) and os.environ.get('PYTHONSAFEPATH'):  # pragma: no cover
    ensure_safe_path()
