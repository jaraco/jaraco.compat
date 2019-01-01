try:
	from functools import lru_cache, update_wrapper, wraps
except ImportError:
	from .cache import lru_cache
	from ._functools_wraps import update_wrapper, wraps


__all__ = ['lru_cache', 'update_wrapper', 'wraps']
