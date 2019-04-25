from __future__ import absolute_import

import functools
from collections import namedtuple, OrderedDict

try:
	import builtins
except ImportError:
	import __builtin__ as builtins

try:
	from thread import allocate_lock as Lock
except ImportError:
	try:
		from _thread import allocate_lock as Lock
	except Exception:
		from _dummy_thread import allocate_lock as Lock

from ._functools_wraps import wraps


def _move_to_end(odict, key):
	'''
	Move an existing element to the end.

	Raises KeyError if the element does not exist.
	'''
	odict[key] = odict.pop(key)


# lru_cache implementation from Python 3.3dev [dfffb293f4b3]
_CacheInfo = namedtuple("CacheInfo", "hits misses maxsize currsize")


def lru_cache(maxsize=100, typed=False):
	"""Least-recently-used cache decorator.

	If *maxsize* is set to None, the LRU features are disabled and the cache
	can grow without bound.

	If *typed* is True, arguments of different types will be cached separately.
	For example, f(3.0) and f(3) will be treated as distinct calls with
	distinct results.

	Arguments to the cached function must be hashable.

	View the cache statistics named tuple (hits, misses, maxsize, currsize) with
	f.cache_info().	 Clear the cache and statistics with f.cache_clear().
	Access the underlying function with f.__wrapped__.

	See:  http://en.wikipedia.org/wiki/Cache_algorithms#Least_Recently_Used

	"""
	# Users should only access the lru_cache through its public API:
	#     cache_info, cache_clear, and f.__wrapped__
	# The internals of the lru_cache are encapsulated for thread safety and
	# to allow the implementation to change (including a possible C version).

	def decorating_function(user_function, **kwargs):
		tuple = kwargs.get('tuple', builtins.tuple)
		sorted = kwargs.get('sorted', builtins.sorted)
		map = kwargs.get('map', builtins.map)
		len = kwargs.get('len', builtins.len)
		type = kwargs.get('type', builtins.type)
		KeyError = kwargs.get('KeyError', builtins.KeyError)

		hits = [0]
		misses = [0]
		kwd_mark = (object(),)			# separates positional and keyword args
		lock = Lock()					# needed because OrderedDict isn't threadsafe

		if maxsize is None:
			cache = dict()				# simple cache without ordering or size limit

			@wraps(user_function)
			def wrapper(*args, **kwds):
				# nonlocal hits, misses
				key = args
				if kwds:
					sorted_items = tuple(sorted(kwds.items()))
					key += kwd_mark + sorted_items
				if typed:
					key += tuple(map(type, args))
					if kwds:
						key += tuple(type(v) for k, v in sorted_items)
				try:
					result = cache[key]
					hits[0] += 1
					return result
				except KeyError:
					pass
				result = user_function(*args, **kwds)
				cache[key] = result
				misses[0] += 1
				return result
		else:
			cache = OrderedDict()			# ordered least recent to most recent
			cache_popitem = cache.popitem
			# use the move_to_end method if available, otherwise fallback to
			#  the function.
			cache_renew = getattr(
				cache, 'move_to_end',
				functools.partial(_move_to_end, cache))

			@wraps(user_function)
			def wrapper(*args, **kwds):
				# nonlocal hits, misses
				key = args
				if kwds:
					sorted_items = tuple(sorted(kwds.items()))
					key += kwd_mark + sorted_items
				if typed:
					key += tuple(map(type, args))
					if kwds:
						key += tuple(type(v) for k, v in sorted_items)
				with lock:
					try:
						result = cache[key]
						cache_renew(key)  # record recent use of this key
						hits[0] += 1
						return result
					except KeyError:
						pass
				result = user_function(*args, **kwds)
				with lock:
					cache[key] = result		# record recent use of this key
					misses[0] += 1
					if len(cache) > maxsize:
						cache_popitem(0)  # purge least recently used cache entry
				return result

		def cache_info():
			"""Report cache statistics"""
			with lock:
				return _CacheInfo(hits[0], misses[0], maxsize, len(cache))

		def cache_clear():
			"""Clear the cache and cache statistics"""
			# nonlocal hits, misses
			with lock:
				cache.clear()
				hits[0] = misses[0] = 0

		wrapper.cache_info = cache_info
		wrapper.cache_clear = cache_clear
		return wrapper

	return decorating_function
