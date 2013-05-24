try:
	from functools import wraps
except ImportError:
	def wraps(func):
		"Just return the function unwrapped"
		return lambda x: x
