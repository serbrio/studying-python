from unittest import TestCase, main
from treasures import treasures


class TreasuresTestCase(TestCase):
    def test_treasures_1(self):
        self.assertEqual(['golden coin: 92', 'ruby: 2'], treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 200},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 1000},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 2}}, 5))

    def test_treasures_2(self):
        self.assertEqual(['golden coin: 100', 'silver coin: 100', 'ruby: 1'], treasures({'golden coin':
                         {'price': 100, 'weight': 50, 'amount': 100},
                      'silver coin':
                         {'price': 10, 'weight': 20, 'amount': 100},
                      'ruby':
                         {'price': 1000, 'weight': 200, 'amount': 1}}, 7.5))

    def test_treasures_3(self):
        self.assertEqual(["golden coin: 100", "ruby: 4"], treasures({"golden coin":
                         {"price": 100, "weight": 10, "amount": 100},
                      "silver coin":
                         {"price": 10, "weight": 10, "amount": 100},
                      "ruby":
                         {"price": 1000, "weight": 200, "amount": 5}}, 1.8))


if __name__ == '__main__':
    main()