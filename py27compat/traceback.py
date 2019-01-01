from __future__ import absolute_import

import sys
import traceback

# On Python 2.7, format_exc always returns a UTF-8-encoded bytestring; make it
#  return a unicode string as it does on Python 3.
# I determined this finding experimentally. If you find that's not the case,
#  provide a counter example. Thanks.


def _format_exc_2x(*args, **kwargs):
	return traceback.format_exc(*args, **kwargs).decode('utf-8')


format_exc = (
	_format_exc_2x
	if sys.version_info < (3,) else
	traceback.format_exc
)
