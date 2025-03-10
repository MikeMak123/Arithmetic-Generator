import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from utils import Fraction

class TestFraction(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(str(Fraction(1, 2) + Fraction(1, 3)), "5/6")

    def test_subtraction(self):
        self.assertEqual(str(Fraction(3, 4) - Fraction(1, 4)), "1/2")

    def test_multiplication(self):
        self.assertEqual(str(Fraction(2, 3) * Fraction(3, 4)), "1/2")

    def test_division(self):
        self.assertEqual(str(Fraction(2, 3) / Fraction(3, 4)), "8/9")

    def test_simplify(self):
        self.assertEqual(str(Fraction(4, 8)), "1/2")

    def test_whole_number(self):
        self.assertEqual(str(Fraction(6, 3)), "2")

    def test_mixed_fraction(self):
        self.assertEqual(str(Fraction(5, 2)), "2'1/2")

    def test_zero_denominator(self):
        with self.assertRaises(ValueError):
            Fraction(1, 0)

    def test_negative_fraction(self):
        with self.assertRaises(ValueError):
            Fraction(-1, 2)

    def test_large_numbers(self):
        self.assertEqual(str(Fraction(1000, 2500)), "2/5")

if __name__ == '__main__':
    unittest.main()
