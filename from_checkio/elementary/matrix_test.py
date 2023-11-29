from unittest import TestCase, main
from matrix import house

class MatrixTestCase(TestCase):
    def test_house(self):
        self.assertEqual(2, house('#000\n#000\n0000'))

    def test_house_min(self):
        self.assertEqual(1, house('0000\n00#0\n0000'))

    def test_house_null(self):
        self.assertEqual(0, house('0000\n0000\n0000'))

    def test_house_edges(self):
        self.assertEqual(12, house('#000\n0000\n000#'))

    def test_house_bad(self):
        self.assertRaises(TypeError, house, 45)


if __name__ == '__main__':
    main()
