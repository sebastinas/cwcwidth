# Copyright 2021 Sebastian Ramacher <sebastian@ramacher.at>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libc.stddef cimport wchar_t, size_t
from cpython.mem cimport PyMem_Free

cdef extern from "Python.h":
    wchar_t* PyUnicode_AsWideCharString(object, Py_ssize_t*) except NULL
    Py_ssize_t PyUnicode_AsWideChar(object, wchar_t*, Py_ssize_t)

cdef extern from "wcwidth_compat.h" nogil:
    int wcswidth(const wchar_t*, size_t)
    int wcwidth(wchar_t)
    size_t wcslen(const wchar_t*)


cdef int wcswidth_loop(const wchar_t* s, size_t n):
    cdef size_t idx
    cdef int v
    cdef ret = 0
    for idx in range(n):
        v = wcwidth(s[idx])
        if v == -1:
            return -1
        ret += v
    return ret


def c_wcswidth(str pwcs not None, n=None):
    """Return the printable length of a unicode character on a terminal.

    Note that this function slightly deviates from wcswidth(3) behavior when the string includes
    null characters. As strings are not null terminated, they are treated as characters of width 0
    and processing continues until the end of the string.

    See wcswidth(3) for more details.
    """

    cdef Py_ssize_t actual_length
    cdef wchar_t* s = PyUnicode_AsWideCharString(pwcs, &actual_length)
    cdef size_t cn = actual_length
    cdef int ret = 0

    if n is not None and n < cn:
        cn = <size_t>n

    if <size_t>actual_length != wcslen(s):
        # In this case pwcs contains a null character. libc's wcwidth (and other string processing
        # functions) will stop when encountering a null character, but in Python the null character
        # will just be skipped. So in this case we will emulate wcwidth's behavior and sum up all
        # the width of all characters individually
        ret = wcswidth_loop(s, cn)
    else:
        ret = wcswidth(s, cn)
    PyMem_Free(s)
    return ret


def c_wcwidth(str wc not None):
    """Return the printable length of a unicode character on a terminal.

    See wcwidth(3) for more details.
    """

    if len(wc) != 1:
        raise ValueError("Expected one unicode character")

    cdef wchar_t c
    PyUnicode_AsWideChar(wc, &c, 1)
    return wcwidth(c)
