# supplies OrderedDict via the ordereddict package for Python 2.5+
from __future__ import absolute_import

try:
	from collections import OrderedDict
except ImportError:
	from ordereddict import OrderedDict


__all__ = ['OrderedDict']
