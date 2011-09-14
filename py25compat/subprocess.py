"""
Python added .terminate() and .kill() to subprocess.Popen objects in
Python 2.6. If you need Python 2.5 compatibility, use term_proc and
kill_proc instead.

from py25compat.subprocess import term_proc

my_proc = Popen(...)
# do stuff...
term_proc(my_proc)
# or if you really need to kill it
kill_proc(my_proc)

"""

import sys
import os

def os_term(pid):
	import signal
	os.kill(pid, signal.SIGTERM)

def term_pid_win32(pid):
	raise NotImplementedError()

def os_kill(pid):
	import signal
	os.kill(pid, signal.SIGKILL)

def kill_pid_win32(pid):
	raise NotImplementedError()

if sys.version_info < (2,6):
	def term_proc(popen):
		"""
		Terminate a popen process
		"""
		func = globals().get('term_pid_' + sys.platform, os_term)
		func(popen.pid)
	def kill_proc(popen):
		"""
		Kill a popen process
		"""
		func = globals().get('kill_pid_' + sys.platform, os_kill)
		func(popen.pid)
else:
	def term_proc(popen):
		return popen.terminate()
	def kill_proc(popen):
		return popen.kill()
