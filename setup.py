# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE.rst') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python Project',
    long_description=readme,
    author='Pasquale Grimaldi',
    author_email='pamaldi@gmail.com',
    url='https://github.com/pamaldi/python-sample',
    license=license,
    test_suite='tests',
    packages=find_packages(exclude=('tests', 'docs'))

)
