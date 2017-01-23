jaraco.compat
=============

``jaraco.compat`` provides forward compatibility for Python packages,
allowing future constructs to be borrowed before they're available in
the standard library.

Usage
-----

Import functions from the appropriate pyXXcompat module in your python
code. When you're eventually ready to upgrade beyond pyXX, you can
easily locate (with a grep) and replace those functions with the
canonical implementations.

Example
-------

Say you want a namedtuple (introduced in Python 2.6) in a project which
supports Python 2.5 and greater::

    from py25compat import namedtuple
    MyTuple = namedtuple('MyTuple', 'a b c')
    mt = MyTuple(1,2,3)

With jaraco.compat installed, this code will run on Python 2.5 and
greater. When the project is ready to move to Python 2.6, one can easily
grep for py25compat and make the necessary replacements with minimal
impact on the code. In this case::

    from collections import namedtuple
    MyTuple = namedtuple('MyTuple', 'a b c')
    mt = MyTuple(1,2,3)

Changes
-------

1.3
~~~

* Added ``py27compat.properties`` with ``simplemethod``.

1.2
~~~

* Added `py24compat.functools` with `wraps` degenerate wrapper.

1.1
~~~

* Added `py27compat.traceback` with format_exc helper (consistently returns
  unicode results).

1.0
~~~

* Adding `py26compat.subprocess.check_output`.

0.9
~~~

* Added `py31compat.collections.lru_cache` which provides a backport of the
  Python 3.2 cache of the same name.

0.8
~~~

* Added `py25compat.subprocess` with `term_proc` and `kill_proc` which
  take Popen objects and terminate and kill them respectively.

0.7
~~~

* Added `py31compat.functools`, which provides `wraps` and `update_wrapper` that
  supply the Python 3.2 __wrapped__ attribute.
* Added `py26compat.collections`, which provides `OrderedDict` on Python 2.6
  and earlier (via the ordereddict package).

0.6
~~~

* Added py26compat.total_seconds
* Added py24compat.partition

0.5
~~~

* Added py26compat with ``cmp_to_key``.