# Python bindings for wc(s)width

`cwcwidth` provides Python bindings for `wcwidth` and `wcswidth` functions defined in POSIX.1-2001
and POSIX.1-2008 based on [Cython](https://cython.org/). These functions compute the printable
length of a unicode character/string on a terminal. The module provides the same `wcwidth()` and
`wcswidth()` functions as [wcwidth](https://pypi.org/project/wcwidth/) and its behavior is comparable.

On systems not conforming to POSIX.1-2001 and POSIX.1-2008, Markus Kuhn's
[implementation](https://www.cl.cam.ac.uk/~mgk25/ucs/wcwidth.c) is used to provide the
functionality.

## Dependencies

* `Cython >= 3.1` (optional, only for building). If Cython is not available, the C files are not
  regenerated from their source.

## Quick installation guide

`cwcwidth` can be installed via `pip`:
```sh
pip install cwcwidth
```
or by running:
```sh
python3 setup.py install
```

In case the extension should be built with the limited Python API, set the environment variable
`USE_LIMITED_API` to any value.

## Usage

```python3
>>> import cwcwidth
>>> cwcwidth.wcwidth("a")
1
>>> cwcwidth.wcswidth("コ")
2
>>> cwcwidth.wcswidth("コンニチハ, セカイ!")
19
>>> cwcwidth.wcswidth("コンニチハ, セカイ!", 5)
10
```

## Comparison with `wcwidth`

`cwcwidth` is about 2x faster than [wcwidth](https://wcwidth.readthedocs.io/en/latest/intro.html)
for CJK,

```python3
>>> import wcwidth, cwcwidth, timeit
>>> timeit.timeit(lambda: wcwidth.wcswidth("コンニチハ, セカイ!"))
0.14529069198761135
>>> timeit.timeit(lambda: cwcwidth.wcswidth("コンニチハ, セカイ!"))
0.0692138300219085
```

`wcwidth` ships a compiled extension for the stable ABI (`cp310-abi3`) with
[libwcwidth](https://wcwidth.readthedocs.io/en/latest/libwcwidth.html), and provides *grapheme
support*, required for complex languages and emojis, while `cwcwidth` is without grapheme support,
calculating the sum of single-codepoint inspections as zero, narrow, or wide, and so `uwcwidth` is
unable to measure emojis, flags, or complex languages.

## License

The code is licensed under the MIT license.

