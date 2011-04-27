from __future__ import division

try:
	from functools import cmp_to_key
except ImportError:
	# from Python 2.7 docs
	def cmp_to_key(mycmp):
		'Convert a cmp= function into a key= function'
		class K(object):
			def __init__(self, obj, *args):
				self.obj = obj
			def __lt__(self, other):
				return mycmp(self.obj, other.obj) < 0
			def __gt__(self, other):
				return mycmp(self.obj, other.obj) > 0
			def __eq__(self, other):
				return mycmp(self.obj, other.obj) == 0
			def __le__(self, other):
				return mycmp(self.obj, other.obj) <= 0
			def __ge__(self, other):
				return mycmp(self.obj, other.obj) >= 0
			def __ne__(self, other):
				return mycmp(self.obj, other.obj) != 0
		return K

def total_seconds(td):
	"""
	Python 2.7 adds a total_seconds method to timedelta objects.
	See http://docs.python.org/library/datetime.html#datetime.timedelta.total_seconds
	"""
	try:
		result = td.total_seconds()
	except AttributeError:
		result = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 10**6) / 10**6
	return result
