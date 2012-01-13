#!/usr/bin/env python
import os
from topicsio import __version__

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
long_description = f.read()
f.close()

sdict = {
    'name' : 'python-topicsio',
    'version' : __version__,
    'description' : 'Python client for Topics.io web service',
    'long_description' : long_description,
    'url': 'http://github.com/drano/python-topicsio',
    'download_url' : 'http://cloud.github.com/downloads/drano/python-topicsio/python-topicsio-%s.tar.gz' % __version__,
    'author' : 'Didier Rano',
    'author_email' : 'didier.rano@gmail.com',
    'maintainer' : 'Didier Rano',
    'maintainer_email' : 'didier.rano@gmail.com',
    'keywords' : ['Topics.io', 'news', 'topics'],
    'license' : 'MIT',
    'packages' : ['topicsio'],
    'test_suite' : 'tests.all_tests',
    'classifiers' : [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'],
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**sdict)
