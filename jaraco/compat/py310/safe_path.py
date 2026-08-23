"""
Applies backward compatibility to honor PYTHONSAFEPATH.
"""

import contextlib
import os
import sys
from collections.abc import Mapping


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


#: Interpreter options ensuring a child interpreter honors a safe path.
#: Prior to 3.11, PYTHONSAFEPATH is ignored, so isolated mode, which also
#: excludes the current directory from sys.path, supplies the behavior.
args = ['-I'] * (sys.version_info < (3, 11))


def environ(base: Mapping[str, str] = os.environ) -> dict[str, str]:
    """
    Return base (os.environ by default) with a safe path enabled.

    >>> environ({'FOO': 'bar'})
    {'FOO': 'bar', 'PYTHONSAFEPATH': '1'}
    """
    return dict(base, PYTHONSAFEPATH='1')


def command(*params: str) -> list[str]:
    """
    Build a command invoking this interpreter with a safe path.

    Pass the command with ``env=environ()`` for the setting to apply.

    >>> import subprocess
    >>> cmd = command('-c', 'import sys; print("" in sys.path)')
    >>> proc = subprocess.run(cmd, env=environ(), text=True, capture_output=True)
    >>> proc.stdout.strip()
    'False'
    """
    return [sys.executable, *args, *params]
