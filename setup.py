#!/usr/bin/python3

import platform
from setuptools import setup, Extension


extension_sources = ["cwcwidth/_impl.pyx"]
define_macros = []
if platform.system() == "Windows":
    extension_sources.append("cwcwidth/wcwidth.c")
    define_macros.append(
        ("USE_MK_WCWIDTH", None),
    )

ext_modules = [
    Extension(
        "cwcwidth._impl",
        extension_sources,
        define_macros=define_macros,
    )
]

setup(
    ext_modules=ext_modules,
    packages=["cwcwidth"],
    package_data={
        "cwcwidth": ["_impl.pyi", "py.typed"],
    },
)
