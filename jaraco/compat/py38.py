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


def _fixer(orig: str):  # pragma: no cover
    """
    Return an object that implements removesuffix and removeprefix on orig.
    """

    def removesuffix(suffix):
        # suffix='' should not call orig[:-0].
        if suffix and orig.endswith(suffix):
            return orig[: -len(suffix)]
        else:
            return orig[:]

    def removeprefix(prefix):
        if orig.startswith(prefix):
            return orig[len(prefix) :]
        else:
            return orig[:]

    return types.SimpleNamespace(removesuffix=removesuffix, removeprefix=removeprefix)


r_fix = _fixer if sys.version_info < (3, 9) else lambda x: x

cache = (
    functools.cache  # type: ignore[attr-defined]
    if sys.version_info >= (3, 9)
    else functools.lru_cache(maxsize=None)
)
