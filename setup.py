#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

settings = dict()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet',
    'Topic :: Utilities',
]

with open('README.rst') as file_readme:
    readme = file_readme.read()

with open('HISTORY.rst') as file_history:
    history = file_history.read()

with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()

settings.update(
    name='tenacity',
    version='1.3.4-dev',
    description='Tenacity',
    long_description=readme + '\n\n' + history,
    author='Julien Danjou',
    license='Apache 2.0',
    url='https://github.com/jd/tenacity',
    classifiers=CLASSIFIERS,
    keywords="decorator decorators retry retrying "
    "tenacity exception exponential backoff",
    py_modules=['tenacity'],
    test_suite="test_tenacity",
    install_requires=requirements,
)


setup(**settings)
