
cwcwidth -- bindings for wc(s)wdith
===================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

To compute the number of columns needed to print a string, POSIX.1-2001 and POSIX.1-2008 define two
functions: ``wcwidth`` and ``wcswidth``. Given a character or string, they return the required
number of columns or error out with ``-1`` if they encounter a nonprintable character. These
functions are not available per default in Python, but are quite useful when the width plays a role
for formatting outputs on a terminal.

Module documentation
--------------------

The ``cwcwidth`` module provides the following two functions:

.. py:function:: cwcwidth.wcwidth(wc: str) -> int

  Return the printable length of a unicode character.

.. py:function:: cwcwidth.wcswidth(pwcs: str, n: Optional[int]=None) -> int

  Return the printable length of a unicode string. If the optional argument ``n`` is provided, only
  the first ``n`` characters of the string are considered.

Both functions behave in the same way as the functions with the same signture from the `wcwidth`_
module.

.. _wcwidth: https://pypi.org/project/wcwidth/

Example usage
-------------

::

  >>> from cwcwidth import wcwidth, wcswidth
  >>> wcwidth("a")
  1
  >>> wcswidth("コ")
  2
  >>> wcswidth("コンニチハ, セカイ!")
  19
  >>> wcswidth("コンニチハ, セカイ!", 5)
  10


Users
-----

``cwcwidth`` is currently used by the following projects:

* `curtsies`_
* `bpython`_

.. _curtsies: https://pypi.org/project/curtsies/
.. _bpython: https://pypi.org/project/bpython/
