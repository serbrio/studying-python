from unittest import TestCase, main
from stones import stones


class StonesTestCase(TestCase):
    def test_stones_1(self):
        self.assertEqual(2, stones(17, [1, 3, 4]))

    def test_stones_2(self):
        self.assertEqual(1, stones(17, [1, 3, 4, 6, 9]))

    def test_stones_3(self):
        self.assertEqual(2, stones(99, [1]))


if __name__ == '__main__':
    main()
