#!/usr/bin/env python3

import unittest 
from collatz_hypothesis import check_collatz_hypothesis as collatz

import random

class TestCollatzHypo(unittest.TestCase):
    def test_basic_1(self):
        data = 1
        result = collatz(data)
        self.assertEqual(result, (0, []))

    def test_basic_2(self):
        data = 2
        result = collatz(data)
        self.assertEqual(result, (1, [1]))

    def test_basic_16(self):
        data = 16
        result = collatz(data)
        self.assertEqual(result, (4, [8, 4, 2, 1]))

    def test_15(self):
        data = 15
        result = collatz(data)
        self.assertEqual(result, (17, [46,23,70,35,106,53,160,80,40,20,10,5,16,8,4,2,1]))

    def test_random(self):
        data = random.randint(1000, 10000)
        result = collatz(data)
        self.assertTrue(result[0] > 1 and len(result[1]) > 1) 


if __name__ == "__main__":
    unittest.main()
