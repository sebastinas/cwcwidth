# Changelog

## 0.1.13

* Build wheels with limited API on platforms where possible. Limited API support with freethreading still needs some work in [cython](https://github.com/cython/cython/issues/7399).
* Clean up build system and require `setuptools >= 77.0.3` for building.

## 0.1.12

* Drop support for Python 3.10.
* Add support for building extensions with limited API.
* Build wheels for PyPI with limited API.

## 0.1.11

* Drop support for Python 3.9.
* Add support for Python 3.14.

## 0.1.10

* Drop support for Python 3.8.
* Add support for Python 3.13.
* Update Unicode definition to 15.1.

## 0.1.9

* Drop support for Python 3.7.
* Add support for Python 3.12.
* Avoid redefinition of `_XOPEN_SOURCE`.

## 0.1.8

* Set build-backend in pyproject.toml.

## 0.1.7

* Ensure that cython generated C source file is always included in sdist.

## 0.1.6

* Add support for Python 3.10.
* Drop support for Python 3.6.

## 0.1.5

* Fix type annotations.

## 0.1.4

* Include tests again.
* Include C file again.

## 0.1.3

* Fix memory leaks in certain error cases.
* Modernize build system and rely on setuptool's Cython support.
* Add more tests.
* Skip some tests if not run in a UTF-8 locale.
* Use libc's implementation on Mac OS.

## 0.1.2

* Also build wheels with cibuildwheel.
* Provide type information for mypy.

## 0.1.1

* If Cython is not available, do not regenerate the C source file during build.

## 0.1

* Initial release.
