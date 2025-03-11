import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
from calculator import calculate

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        """测试加法计算"""
        self.assertEqual(calculate("1/6 + 1/8 ="), "7/24")

    def test_subtraction(self):
        """测试不会出现负数的减法"""
        self.assertEqual(calculate("5/9 - 1/4 ="), "11/36")  # 5/9 - 1/4

    def test_multiplication(self):
        """测试乘法计算"""
        self.assertEqual(calculate("2/3 × 3/5 ="), "2/5")

    def test_division(self):
        """测试除法计算"""
        self.assertEqual(calculate("4 ÷ 2 ="), "2")

    def test_mixed_fraction_result(self):
        """测试带分数输出"""
        self.assertEqual(calculate("7/3 - 2/3 ="), "1'2/3")

    def test_whole_number_result(self):
        """测试整除返回整数"""
        self.assertEqual(calculate("10/4 + 1/2 ="), "3")

    def test_large_fractions(self):
        """测试大分数计算"""
        self.assertEqual(calculate("999/1000 + 1/1000 ="), "1")

    def test_zero_division(self):
        """测试除零错误"""
        with self.assertRaises(ValueError):
            calculate("1 ÷ 0 =")

    def test_invalid_expression(self):
        """测试无效输入"""
        with self.assertRaises(ValueError):
            calculate("abc + 1/2 =")

    def test_malformed_fraction(self):
        """测试错误分数格式"""
        with self.assertRaises(ValueError):
            calculate("1//2 + 1/3 =")  # 1//2 不是合法分数

if __name__ == '__main__':
    unittest.main()
