from unittest import TestCase, main
from safe_code import safe_code


class SafeCodeTestCase(TestCase):
    def test_safe_code_1(self):
        self.assertEqual(0, safe_code("-5#*-1=5#"))

    def test_safe_code_2(self):
        self.assertEqual(5, safe_code("##*##=302#"))

    def test_safe_code_3(self):
        self.assertEqual(-1, safe_code("19--45=5#"))

    def test_safe_code_4(self):
        self.assertEqual(-1, safe_code("##--11=11"))

    def test_safe_code_5(self):
        self.assertEqual(1, safe_code("#9+3=22"))

    def test_safe_code_6(self):
        self.assertEqual(2, safe_code("11*#=##"))

    def test_safe_code_7(self):
        self.assertEqual(-1, safe_code("#9+3=12"))


if __name__ == '__main__':
    main()
