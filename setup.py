# -*- coding: UTF-8 -*-

"""
Setup script for jaraco.compat package

Copyright © 2010 Jason R. Coombs
"""

from setuptools import setup, find_packages

name = 'jaraco.compat'

setup(
	name = name,
	use_hg_version = dict(increment='0.1'),
	description = 'Modules providing forward compatibility across some Python 2.x versions',
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
	],
	dependency_links = [
	],
	setup_requires=[
		'hgtools>=0.6.4',
	],
)
