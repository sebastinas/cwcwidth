import unittest
from cwcwidth import wcwidth, wcswidth


class Tests(unittest.TestCase):
    def exec_test(
        self, phrase, individual_expected_lengths, expected_length=None, n=None
    ):
        if expected_length is None:
            expected_length = sum(individual_expected_lengths)
        self.assertEqual(
            individual_expected_lengths,
            tuple(map(wcwidth, phrase if n is None else phrase[:n])),
        )
        self.assertEqual(expected_length, wcswidth(phrase, n))

    def test_hello_jp(self):
        """Width of Japanese phrase: コンニチハ, セカイ!"""
        self.exec_test("コンニチハ, セカイ!", (2, 2, 2, 2, 2, 1, 1, 2, 2, 2, 1))

    def test_wcswidth_substr(self):
        """Test wcswidth() optional 2nd parameter, ``n``."""
        self.exec_test("コンニチハ, セカイ!", (2, 2, 2, 2, 2, 1, 1), n=7)

    def test_null_width_0(self):
        """NULL (0) reports width 0."""
        self.exec_test("abc\x00def", (1, 1, 1, 0, 1, 1, 1))
        self.exec_test("abc\x00def", (1, 1, 1, 0, 1, 1, 1), n=7)

    def test_control_c0_width_negative_1(self):
        """CSI (Control sequence initiate) reports width -1."""
        self.exec_test("\x1b[0m", (-1, 1, 1, 1), expected_length=-1)

    def test_combining_width_negative_1(self):
        """Simple test combining reports total width of 4."""
        self.exec_test("--\u05bf--", (1, 1, 0, 1, 1))

    def test_combining_cafe(self):
        """Phrase cafe + COMBINING ACUTE ACCENT is café of length 4."""
        self.exec_test("cafe\u0301", (1, 1, 1, 1, 0))

    def test_combining_enclosing(self):
        """CYRILLIC CAPITAL LETTER A + COMBINING CYRILLIC HUNDRED THOUSANDS SIGN is А҈ of length 1."""
        expect_length_each = (1, 0)
        self.exec_test("\u0410\u0488", (1, 0))

    def test_combining_spacing(self):
        """Balinese kapal (ship) is ᬓᬨᬮ᭄ of length 4."""
        self.exec_test("\u1B13\u1B28\u1B2E\u1B44", (1, 1, 1, 1))
