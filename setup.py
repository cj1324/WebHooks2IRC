#!/usr/bin/env python
# coding: UTF-8

import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read_file(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, *paths)) as f:
        return f.read()


# copy form: https://github.com/pypa/virtualenv/blob/develop/setup.py
def get_version():
    version_file = read_file('src', 'webhooks2irc', '__init__.py')
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='WebHooks2IRC',
    version=get_version(),
    url='https://github.com/cj1324/WebHooks2IRC',
    description='GitLab Web Hooks to IRC',
    long_description=read_file('README.md'),
    author='HanChen',
    author_email='chen1324@gmail.com',
    license='BSD-2-Clause',
    packages=['webhooks2irc'],
    package_dir={'webhooks2irc': 'src/webhooks2irc'},
    install_requires=[
        'bottle',
        'irc'
    ],
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved ::  BSD 2-clause "Simplified" License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ]
)
