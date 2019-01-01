from __future__ import absolute_import

import functools

# Add the automatic addition of the __wrapped__ attribute when calling
#  update_wrapper or wraps.


def update_wrapper(wrapper, wrapped, *args, **kwargs):
	res = functools.update_wrapper(wrapper, wrapped, *args, **kwargs)
	res.__wrapped__ = wrapped
	return res


def wraps(wrapped, *args, **kwargs):
	return functools.partial(update_wrapper, wrapped=wrapped, *args, **kwargs)
