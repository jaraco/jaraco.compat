"""
>>> r_fix('foo.bar').removesuffix('.bar')
'foo'
>>> r_fix('foo.bar').removeprefix('foo.')
'bar'
>>> cached_print = cache(print)
>>> cached_print('foo')
foo
>>> cached_print('foo')
"""

import functools
import sys
import types
from typing import Protocol, cast


class _RFixed(Protocol):
    def removesuffix(self, suffix: str) -> str: ...
    def removeprefix(self, prefix: str) -> str: ...


def _fixer(orig: str) -> _RFixed:  # pragma: no cover
    """
    Return an object that implements removesuffix and removeprefix on orig.
    """

    def removesuffix(suffix: str) -> str:
        # suffix='' should not call orig[:-0].
        if suffix and orig.endswith(suffix):
            return orig[: -len(suffix)]
        else:
            return orig[:]

    def removeprefix(prefix: str) -> str:
        if orig.startswith(prefix):
            return orig[len(prefix) :]
        else:
            return orig[:]

    return cast(
        _RFixed,
        types.SimpleNamespace(removesuffix=removesuffix, removeprefix=removeprefix),
    )


def passthrough(orig: str) -> str:
    return orig


r_fix = _fixer if sys.version_info < (3, 9) else passthrough

cache = (
    functools.cache  # type: ignore[attr-defined, unused-ignore]
    if sys.version_info >= (3, 9)
    else functools.lru_cache(maxsize=None)
)
