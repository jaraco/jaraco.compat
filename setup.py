# -*- coding: UTF-8 -*-

"""
Setup script for jaraco.compat package

Copyright © 2010-2011 Jason R. Coombs
"""
import sys
import os

from setuptools import find_packages

name = 'jaraco.compat'

py26_reqs = ['ordereddict >= 1.1'] if sys.version_info < (2,7) else []
try:
	f = open(os.path.join(os.path.dirname(__file__), 'README'))
	long_description = f.read()
finally:
	f.close()

setup_params = dict(
	name = name,
	use_hg_version = dict(increment='0.1'),
	description = 'Modules providing forward compatibility across some '
		'Python 2.x versions',
	long_description = long_description,
	author = 'Jason R. Coombs',
	author_email = 'jaraco@jaraco.com',
	url = 'http://bitbucket.org/jaraco/'+name,
	packages = find_packages(),
	license = 'MIT',
	classifiers = [
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Programming Language :: Python",
	],
	entry_points = {
	},
	install_requires=[
	] + py26_reqs,
	dependency_links = [
	],
	setup_requires=[
		'hgtools>=0.6.4',
	],
)

if __name__ == '__main__':
	from setuptools import setup
	setup(**setup_params)
