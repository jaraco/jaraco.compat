#!python

# some forward-compatibilty functions for those unfortunate
#  souls that can't yet run Python 2.4

# attrgetter
try:
    from operator import attrgetter
except ImportError:
    def attrgetter(attr_name):
        return lambda target: getattr(target, attr_name)

# set
try:
    set = set
    frozenset = frozenset
except NameError:
    from sets import Set as set, ImmutableSet as frozenset

# sorted
try:
    sorted = sorted
except NameError:
    # global name 'sorted' doesn't exist in Python2.3
    # this provides a poor-man's emulation of the sorted built-in method
    def sorted(l, cmp=cmp, key=None, reverse=False):
        identity = lambda x: x
        if key is None:
            key = identity
        if reverse:
            cmp_ = lambda a,b: -cmp(a,b)
        else:
            cmp_ = cmp
        sorted_list = list(l)
        sorted_list.sort(
                lambda self, other: cmp_(
                        key(self),
                        key(other)))
        return sorted_list

# reversed
try:
    reversed = reversed
except NameError:
    def reversed(sequence):
        for item in sequence[::-1]:
            yield item

# rsplit
try:
    ''.rsplit
    def rsplit(s, delim, maxsplit):
        return s.rsplit(delim, maxsplit)

except AttributeError:
    def rsplit(s, delim, maxsplit):
        """Return a list of the words of the string s, scanning s
        from the end. To all intents and purposes, the resulting
        list of words is the same as returned by split(), except
        when the optional third argument maxsplit is explicitly
        specified and nonzero. When maxsplit is nonzero, at most
        maxsplit number of splits - the rightmost ones - occur,
        and the remainder of the string is returned as the first
        element of the list (thus, the list will have at most
        maxsplit+1 elements). New in version 2.4.
        >>> rsplit('foo.bar.baz', '.', 0)
        ['foo.bar.baz']
        >>> rsplit('foo.bar.baz', '.', 1)
        ['foo.bar', 'baz']
        >>> rsplit('foo.bar.baz', '.', 2)
        ['foo', 'bar', 'baz']
        >>> rsplit('foo.bar.baz', '.', 99)
        ['foo', 'bar', 'baz']
        """
        assert maxsplit >= 0

        if maxsplit == 0: return [s]

        # the following lines perform the function, but inefficiently.
        #  This may be adequate for compatibility purposes
        items = s.split(delim)
        if maxsplit < len(items):
            items[:-maxsplit] = [delim.join(items[:-maxsplit])]
        return items

try:
    from subprocess import list2cmdline
except ImportError:
    # here's list2cmdline copied directly from python 2.5.4
    def list2cmdline(seq):
        """
        Translate a sequence of arguments into a command line
        string, using the same rules as the MS C runtime:

        1) Arguments are delimited by white space, which is either a
           space or a tab.

        2) A string surrounded by double quotation marks is
           interpreted as a single argument, regardless of white space
           contained within.  A quoted string can be embedded in an
           argument.

        3) A double quotation mark preceded by a backslash is
           interpreted as a literal double quotation mark.

        4) Backslashes are interpreted literally, unless they
           immediately precede a double quotation mark.

        5) If backslashes immediately precede a double quotation mark,
           every pair of backslashes is interpreted as a literal
           backslash.  If the number of backslashes is odd, the last
           backslash escapes the next double quotation mark as
           described in rule 3.
        """

        # See
        # http://msdn.microsoft.com/library/en-us/vccelng/htm/progs_12.asp
        result = []
        needquote = False
        for arg in seq:
            bs_buf = []

            # Add a space to separate this argument from the others
            if result:
                result.append(' ')

            needquote = (" " in arg) or ("\t" in arg) or arg == ""
            if needquote:
                result.append('"')

            for c in arg:
                if c == '\\':
                    # Don't know if we need to double yet.
                    bs_buf.append(c)
                elif c == '"':
                    # Double backspaces.
                    result.append('\\' * len(bs_buf)*2)
                    bs_buf = []
                    result.append('\\"')
                else:
                    # Normal char
                    if bs_buf:
                        result.extend(bs_buf)
                        bs_buf = []
                    result.append(c)

            # Add remaining backspaces, if any.
            if bs_buf:
                result.extend(bs_buf)

            if needquote:
                result.extend(bs_buf)
                result.append('"')

        return ''.join(result)

try:
    from hashlib import md5
    from hashlib import sha1 as sha
except ImportError:
    from md5 import md5
    from sha import sha

try:
    next = next
except NameError:
    def next(iterable):
        return iterable.next()

def dictupdate(target, *args, **kwargs):
    target.update(dict(*args, **kwargs))

import sys
if sys.version_info >= (2,4):
    from xlutils.copy import copy as xlutils_copy
else:
    # xlutils expects 'set' in builtins, so put it there
    import __builtin__
    __builtin__.set = set
    from xlutils.copy import copy as xlutils_copy
    # gotta leave set in there or the module doesn't work.
    #del __builtin__.set
    del __builtin__

try:
    from operator import itemgetter
except ImportError:
    def itemgetter(*args):
        def callback(obj):
            return [obj[item] for item in args]
        return callback

if sys.version_info >= (2,4):
    from textwrap import dedent
else:
    # Python 2.3 dedent has a bug that removes tabs, so encode them
    from textwrap import dedent as dedent_orig
    def dedent(string):
        string = string.replace('\t', '__x0009__')
        return dedent_orig(string).replace('__x0009__', '\t')

try:
    from itertools import product
except ImportError:
    # from Python 2.6 docs, a memory-inefficient but equivalent algorithm
    def product(*args, **kwds):
        # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
        # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
        pools = map(tuple, args) * kwds.get('repeat', 1)
        result = [[]]
        for pool in pools:
            result = [x+[y] for x in result for y in pool]
        for prod in result:
            yield tuple(prod)

try:
    from itertools import chain
    chain_from_iterable = chain.from_iterable
except AttributeError:
    #from Python 2.6 docs
    def chain_from_iterable(iterables):
        # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
        for it in iterables:
            for element in it:
                yield element

try:
    from collections import deque
except ImportError:
    # A partial implementation of a deque
    class deque(list):
        def popleft(self):
            return self.pop(0)

try:
    from itertools import tee
except ImportError:
    # from Python 2.6 docs
    def tee(iterable, n=2):
        it = iter(iterable)
        deques = [deque() for i in range(n)]
        def gen(mydeque):
            while True:
                if not mydeque:             # when the local deque is empty
                    newval = next(it)       # fetch a new value and
                    for d in deques:        # load it to all the deques
                        d.append(newval)
                yield mydeque.popleft()
        return tuple([gen(d) for d in deques])

try:
    any = any
except NameError:
    # from Python 2.6 docs
    def any(iterable):
        for element in iterable:
            if element:
                return True
        return False

import logging
if 'level' in logging.basicConfig.func_code.co_varnames:
	logging_basicConfig = logging.basicConfig
else:
	def logging_basicConfig(**kwargs):
		logging.basicConfig()
		if 'level' in kwargs:
			logging.root.level = kwargs.pop('level')
		if kwargs:
			pass # ignore other Py2.4 parameters for now
del logging

if sys.version_info >= (2,6):
	def ljust(s, width, fillchar=' '):
		# the Python 3.0 way of left-justifying a string
		return '{0:{2}<{1}}'.format(s, width, fillchar)
else:
	# from implementation found in CheckLibs
	def ljust(src, width, fillchar=' '):
		if len(src) >= length:
			return src
		return src+(fillchar*(length-len(src)))

del sys