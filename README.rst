.. image:: https://img.shields.io/pypi/v/jaraco.compat.svg
   :target: https://pypi.org/project/jaraco.compat

.. image:: https://img.shields.io/pypi/pyversions/jaraco.compat.svg

.. image:: https://github.com/jaraco/jaraco.compat/actions/workflows/main.yml/badge.svg
   :target: https://github.com/jaraco/jaraco.compat/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. image:: https://readthedocs.org/projects/jaracocompat/badge/?version=latest
   :target: https://jaracocompat.readthedocs.io/en/latest/?badge=latest

.. image:: https://img.shields.io/badge/skeleton-2024-informational
   :target: https://blog.jaraco.com/skeleton

Forward compatibility for Python packages,
allowing future constructs to be borrowed before they are available in
the standard library.

`♫ It's going to be the future soon. It won't always be this way, when the things that make me weak and strange get engineered away. ♫ <https://www.youtube.com/watch?v=l5PEz3kGbp4>`_

Usage
=====

Import functions from the appropriate compat.pyXX module in your python
code. When a package is eventually ready to upgrade beyond pyXX,
easily locate (with a grep) and replace those functions with the
canonical implementations.

Example
=======

Say you want a namedtuple (introduced in Python 2.6) in a project which
supports Python 2.5 and greater::

    from compat.py25 import namedtuple
    MyTuple = namedtuple('MyTuple', 'a b c')
    mt = MyTuple(1,2,3)

With jaraco.compat installed, this code will run on Python 2.5 and
greater. When the project is ready to move to Python 2.6, one can easily
grep for py25 and make the necessary replacements with minimal
impact on the code. In this case::

    from collections import namedtuple
    MyTuple = namedtuple('MyTuple', 'a b c')
    mt = MyTuple(1,2,3)
