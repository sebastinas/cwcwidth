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

import locale
import unittest
from cwcwidth import wcwidth, wcswidth

supports_utf8 = "UTF-8" in locale.getlocale()


class Tests(unittest.TestCase):
    def _exec_test(
        self, phrase, individual_expected_lengths, expected_length=None, n=None
    ):
        if expected_length is None:
            expected_length = sum(individual_expected_lengths)
        self.assertEqual(
            individual_expected_lengths,
            tuple(map(wcwidth, phrase if n is None else phrase[:n])),
        )
        self.assertEqual(expected_length, wcswidth(phrase, n))

    def test_exceptions(self):
        """wcwidth raises ValueError for strings of length != 1."""
        with self.assertRaises(ValueError):
            wcwidth("")
        with self.assertRaises(ValueError):
            wcwidth("abc")

    def test_empty_string(self):
        """Width of an empty string is 0."""
        self._exec_test("", tuple())

    def test_hello_world(self):
        """Width of English phrase: Hello World!"""
        self._exec_test("Hello World!", (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1))

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_hello_jp(self):
        """Width of Japanese phrase: コンニチハ, セカイ!"""
        self._exec_test("コンニチハ, セカイ!", (2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1))

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_wcswidth_substr(self):
        """Test wcswidth() optional 2nd parameter."""
        self._exec_test("コンニチハ, セカイ!", (2, 2, 2, 2, 2, 1, 1), n=7)

    def test_null_width_0(self):
        """NULL (0) reports width 0."""
        self._exec_test("abc\x00def", (1, 1, 1, 0, 1, 1, 1))
        self._exec_test("abc\x00def", (1, 1, 1, 0, 1, 1, 1), n=7)

    def test_control_c0_width_negative_1(self):
        """CSI (Control sequence initiate) reports width -1."""
        self._exec_test("\x1b[0m", (-1, 1, 1, 1), expected_length=-1)

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_combining_width_negative_1(self):
        """Simple test combining reports total width of 4."""
        self._exec_test("--\u05bf--", (1, 1, 0, 1, 1))

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_combining_cafe(self):
        """Phrase cafe + COMBINING ACUTE ACCENT is café of length 4."""
        self._exec_test("cafe\u0301", (1, 1, 1, 1, 0))

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_combining_enclosing(self):
        """CYRILLIC CAPITAL LETTER A + COMBINING CYRILLIC HUNDRED THOUSANDS SIGN is А҈ of length 1."""
        self._exec_test("\u0410\u0488", (1, 0))

    @unittest.skipUnless(supports_utf8, "locale does not support UTF-8")
    def test_combining_spacing(self):
        """Balinese kapal (ship) is ᬓᬨᬮ᭄ of length 4."""
        self._exec_test("\u1B13\u1B28\u1B2E\u1B44", (1, 1, 1, 1))

    def test_carriage_return(self):
        """Control character reports width -1."""
        self._exec_test("\r", (-1,))
