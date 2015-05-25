import types
import sys


class simplemethod(object):
	"""
	On Python 2, allow a method to bind to an instance
	(or not), just as it does on Python 3. Avoids TypeError
	when a bound method is called with a non-instance of
	the owner.
	"""
	def __new__(cls, func):
		if sys.version_info >= (3,):
			return func
		return super(simplemethod, cls).__new__(cls, func)

	def __init__(self, func):
		self.func = func

	def __get__(self, instance, owner):
		if instance is None:
			return self.func
		return types.MethodType(self.func, instance, owner)
