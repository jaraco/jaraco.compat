"""
Exposes 'collections.abc' as 'abc' as found in Python 3.4

>>> from py33compat.collections import abc
>>> 'Sequence' in vars(abc)
True
>>> import types
>>> from py33compat import collections
>>> isinstance(collections.abc, types.ModuleType)
True
"""

from __future__ import absolute_import

try:
	from collections import abc
except ImportError:
	import collections as abc


__all__ = ['abc']
