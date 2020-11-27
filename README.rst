.. image:: https://img.shields.io/pypi/v/jaraco.compat.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.compat.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.compat

.. image:: https://github.com/jaraco/jaraco.compat/workflows/Automated%20Tests/badge.svg
   :target: https://github.com/jaraco/jaraco.compat/actions?query=workflow%3A%22Automated+Tests%22
   :alt: Automated Tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

.. image:: https://readthedocs.org/projects/jaracocompat/badge/?version=latest
   :target: https://jaracocompat.readthedocs.io/en/latest/?badge=latest

Forward compatibility for Python packages,
allowing future constructs to be borrowed before they're available in
the standard library.

This package is generally deprecated in favor of more surgical
backports in separate packages.

Usage
=====

Import functions from the appropriate pyXXcompat module in your python
code. When you're eventually ready to upgrade beyond pyXX, you can
easily locate (with a grep) and replace those functions with the
canonical implementations.

Example
=======

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
