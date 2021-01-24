#!/usr/bin/python3

import platform
import os.path
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize

    have_cython = True
except ImportError:
    have_cython = False


def read(name):
    with open(os.path.join(os.path.dirname(__file__), name), encoding="utf-8") as f:
        return f.read()


extension_sources = ["cwcwidth/_impl.pyx" if have_cython else "cwcwidth/_impl.c"]
if platform.system() in ("Windows", "Darwin"):
    extension_sources.append("cwcwidth/wcwidth.c")
    define_macros = [
        ("USE_MK_WCWIDTH", None),
    ]
else:
    define_macros = [
        ("_XOPEN_SOURCE", "600"),
    ]

ext_modules = [
    Extension(
        "cwcwidth._impl",
        extension_sources,
        define_macros=define_macros,
    )
]

if have_cython:
    ext_modules = cythonize(ext_modules, language_level=3)
    setup_requires = ["Cython >= 0.28"]
else:
    setup_requires = []


setup(
    name="cwcwidth",
    version="0.1.1",
    description="Python bindings for wc(s)width",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Sebastian Ramacher",
    author_email="sebastian@ramacher.at",
    url="https://github.com/sebastinas/cwcwidth",
    license="Expat",
    ext_modules=ext_modules,
    packages=["cwcwidth"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">= 3.6",
    setup_requires=setup_requires,
)
