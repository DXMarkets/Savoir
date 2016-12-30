#!/usr/bin/env python
import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requires = ['']


setup(name='Savoir',
    version='1.0.1',
    description='A python wrapper for Multichain Json-RPC API ',
    long_description=read('README.mkdn'),
    license="BSD",
    author='Federico Cardoso',
    author_email='federico.cardoso@dxmarkets.com',
    url='https://github.com/DXMarkets/Savoir',
    keywords='multichain python blockchain',
    packages=find_packages(),
    install_requires=requires,
    )
