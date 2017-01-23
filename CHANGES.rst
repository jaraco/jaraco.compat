1.4
===

* Update project skeleton, including automated deployments. Tests
  are now run on Travis-CI with tests largely passing on Python 3.

1.3
===

* Added ``py27compat.properties`` with ``simplemethod``.

1.2
===

* Added `py24compat.functools` with `wraps` degenerate wrapper.

1.1
===

* Added `py27compat.traceback` with format_exc helper (consistently returns
  unicode results).

1.0
===

* Adding `py26compat.subprocess.check_output`.

0.9
===

* Added `py31compat.collections.lru_cache` which provides a backport of the
  Python 3.2 cache of the same name.

0.8
===

* Added `py25compat.subprocess` with `term_proc` and `kill_proc` which
  take Popen objects and terminate and kill them respectively.

0.7
===

* Added `py31compat.functools`, which provides `wraps` and `update_wrapper` that
  supply the Python 3.2 __wrapped__ attribute.
* Added `py26compat.collections`, which provides `OrderedDict` on Python 2.6
  and earlier (via the ordereddict package).

0.6
===

* Added py26compat.total_seconds
* Added py24compat.partition

0.5
===

* Added py26compat with ``cmp_to_key``.
