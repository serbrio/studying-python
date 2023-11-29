from unittest import TestCase, main
from wild_dogs import wild_dogs

class MatrixTestCase(TestCase):
    def test_wild_dogs_1(self):
        self.assertEqual(0, wild_dogs([(10, 10), (13, 13), (21, 18)]))

    def test_wild_dogs_2(self):
        self.assertEqual(0, wild_dogs([(1, 2), (2, 4), (3, 6), (123, 4)]))

    def test_wild_dogs_3(self):
        self.assertEqual(3.63, wild_dogs([(6, -0.5), (3, -5), (1, -20)]))

    def test_wild_dogs_4(self):
        self.assertEqual(0.18, wild_dogs([(7, 122), (8, 139), (9, 156), (10, 173), (11, 190), (-100, 1)]))


if __name__ == '__main__':
    main()
