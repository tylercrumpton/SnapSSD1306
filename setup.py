#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

import fonthelper


with open('requirements.txt', 'r') as f:
    install_requires = [x for x in list(f) if x[0] != '-']

with open('test-requirements.txt', 'r') as f:
    test_requires = [x for x in list(f) if x[0:2] != '-r']

setup(
    name=fonthelper.__name__,
    description=fonthelper.__doc__,
    maintainer='Tyler Crumpton',
    maintainer_email='tyler.crumpton@gmail.com',
    url='http://www.tylercrumpton.com',
    packages=['fonthelper'],
    install_requires=install_requires,
    tests_require=test_requires,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Natural Language :: English',
    ],
)
