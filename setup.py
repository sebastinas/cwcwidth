#!/usr/bin/python3

import platform
import os.path
from setuptools import setup, Extension
from Cython.Build import cythonize


def read(name):
    with open(os.path.join(os.path.dirname(__file__), name), encoding="utf-8") as f:
        return f.read()


extension_sources = ["cwcwidth/_impl.pyx"]
if platform.system() in ("Windows", "Darwin"):
    extension_sources.append("cwcwidth/wcwidth.c")
    define_macros = [
        ("USE_MK_WCWIDTH", None),
    ]
else:
    define_macros = [
        ("_XOPEN_SOURCE", "600"),
    ]


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
        [
            Extension(
                "cwcwidth._impl",
                extension_sources,
                define_macros=define_macros,
            )
        ],
        language_level=3,
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
