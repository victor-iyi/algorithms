"""
  @author
    Victor I. Afolabi
    Artificial Intelligence & Software Engineer.
    Email: javafolabi@gmail.com
    GitHub: https://github.com/victor-iyiola

  @project
    File: setup.py
    Created on 02 April, 2018 @ 7:54 PM.

  @license
    MIT License
    Copyright (c) 2018. Victor. All rights reserved.
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

algorithms = Extension('*', sources=['algorithms/cython/**.pyx'])

setup(
    name='algorithms',
    version='1.0.0',
    ext_modules=cythonize(algorithms),
    requires=["cython"],
    url='https://github.com/victor-iyiola/algorithms',
    license='MIT',
    author='Victor I. Afolabi',
    author_email='javafolabi@gmail.com',
    description='Data structures & Algorithm (written in C, C++ & Cython).',
    long_description=open('README.md').read()
)
