
def format(str, *args, **kwargs):
	"""
	A very cheap hack to provide a basic implementation of
	string.format under Python 2.5
	"""
	if args:
		raise NotImplementedError("args not supported yet")
	try:
		return str.format(*args, **kwargs)
	except AttributeError:
		str = str.replace('{', '%(').replace('}', ')')
		return str % kwargs
