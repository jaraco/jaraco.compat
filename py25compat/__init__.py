# this module provides forward-compatibility for Python 2.6 and later
#  features on Python 2.5

# At such a time as this library moves to Python 2.6+, these constructs
#  can easily be replaced by searching for py25compat.

import __builtin__

# next statement
try:
	next
except NameError:
	class __NotSupplied(object): pass
	def next(iterable, default=__NotSupplied):
		try:
			return iterable.next()
		except StopIteration:
			if default is __NotSupplied:
				raise
			return default

# namedtuple
try:
	from collections import namedtuple
except ImportError:
	from namedtuple_backport import namedtuple

# enumerate with start param
try:
	enumerate('abc', 1)
	enumerate = enumerate
except TypeError:
	def enumerate(seq, start=0):
		for index, item in __builtin__.enumerate(seq):
			yield index + start, item
