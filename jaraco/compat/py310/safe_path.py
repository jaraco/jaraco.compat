"""
Applies backward compatibility to honor PYTHONSAFEPATH.
"""

import os
import sys

from jaraco.context import suppress


@suppress(ValueError)
def ensure_safe_path() -> None:
    """
    Ensure that '.' isn't on sys.path.

    >>> ensure_safe_path()
    """
    sys.path.remove('')


if sys.version_info < (3, 11) and os.environ.get('PYTHONSAFEPATH'):  # pragma: no cover
    ensure_safe_path()
