#!/usr/bin/python3

import os.path
import sys
from setuptools import setup, Extension
from Cython.Build import cythonize


def read(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


setup(
    name="cwcwidth",
    version="0.1",
    description="Python bindings for wc(s)width",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Sebastian Ramacher",
    author_email="sebastian@ramacher.at",
    url="https://github.com/sebastinas/cwcwidth",
    license="Expat",
    ext_modules=cythonize(
        [Extension("cwcwidth._impl", ["cwcwidth/_impl.pyx"],)], language_level=3,
    ),
    packages=["cwcwidth"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">= 3.6",
    setup_requires=["cython >= 0.28"],
)
