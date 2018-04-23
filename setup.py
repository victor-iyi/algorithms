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

from distutils.core import setup
from Cython.Build import cythonize


setup(
    name='algorithms',
    version='1.0.0',
    ext_modules=cythonize('apis/cython/algorithms.pyx', language='c++'),
    requires=["cython"],
    url='https://github.com/victor-iyiola/algorithms',
    license='MIT',
    author='Victor I. Afolabi',
    author_email='javafolabi@gmail.com',
    description=''
)
