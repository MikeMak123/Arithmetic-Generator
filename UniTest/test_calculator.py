import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculate("1 + 2 ="), "3")

    def test_subtraction(self):
        self.assertEqual(calculate("5 - 3 ="), "2")

    def test_multiplication(self):
        self.assertEqual(calculate("4 × 2 ="), "8")

    def test_division(self):
        self.assertEqual(calculate("1 ÷ 2 ="), "1/2") # changed expected value

    def test_complex_expression(self):
        self.assertEqual(calculate("1 + 2 × 3 ="), "7")

    def test_parentheses(self):
        self.assertEqual(calculate("(1 + 2) × 3 ="), "9")

    def test_negative_numbers(self):
        self.assertEqual(calculate("3 - 5 ="), "-2") # changed to assertEqual instead of assertRaises

    def test_zero_division(self):
        with self.assertRaises(ValueError):
            calculate("4 ÷ 0 =")

    def test_large_numbers(self):
        self.assertEqual(calculate("1000 + 2000 ="), "3000")

    def test_fraction_simplification(self):
        self.assertEqual(calculate("2 ÷ 4 ="), "1/2") # changed expected value


if __name__ == '__main__':
    unittest.main()
