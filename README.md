# Python bindings for wc(s)width

`cwcwidth` provides Python bindings based on [Cython](https://cython.org/) for libc's `wcwidth` and
`wcswidth` functions which compute the printable length of a unicode character/string on a terminal.

The module provides the same functions as [wcwidth](https://pypi.org/project/wcwidth/) and its
behavior is compatible.

## Dependencies

* `Cython >= 0.28` (only for building)

## Quick installation guilde

`cwcwidth` can be installed via `pip`:
```sh
pip install cwcwidth
```
or by running:
```sh
python3 setup.py install
```

## Usage

```python3
import cwcwidth
cwcwidth.wcwidth("a") # 1
cwcwidth.wcswidth("コ") # 2
cwcwidth.wcswidth("コンニチハ, セカイ!") # 19
```

## Comparison with `wcwidth`

```python3
>>> import wcwidth, cwcwidth, timeit
>>> timeit.timeit(lambda: wcwidth.wcswidth("コンニチハ, セカイ!"))
19.14463168097427
>>> timeit.timeit(lambda: cwcwidth.wcswidth("コンニチハ, セカイ!"))
0.16294104099506512
```

## License

The code is licensed under the MIT license.
