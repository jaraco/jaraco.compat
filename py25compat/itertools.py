from __future__ import absolute_import
import itertools

__all__ = ['product', 'izip_longest']

try:
	from itertools import product
except ImportError:
	# from Python 2.7 docs
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
	from itertools import izip_longest
except ImportError:
	# from Python 2.7.1 docs
	def izip_longest(*args, **kwds):
		# izip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
		fillvalue = kwds.get('fillvalue')
		def sentinel(counter = ([fillvalue]*(len(args)-1)).pop):
			yield counter()         # yields the fillvalue, or raises IndexError
		fillers = itertools.repeat(fillvalue)
		iters = [itertools.chain(it, sentinel(), fillers) for it in args]
		try:
			for tup in itertools.izip(*iters):
				yield tup
		except IndexError:
			pass
