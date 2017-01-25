"""
This module is deprecated. Use subprocess32 instead.
"""

from __future__ import absolute_import

try:
	check_output = __import__('subprocess').check_output
except AttributeError:
	check_output = __import__('subprocess32').check_output
