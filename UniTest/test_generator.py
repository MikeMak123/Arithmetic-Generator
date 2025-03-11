import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from generator import generate_exercises

class TestGenerator(unittest.TestCase):

    def test_generate_single_expression(self):
        """测试生成单个题目"""
        exercises = generate_exercises(1, 10)
        self.assertEqual(len(exercises), 1)
        self.assertTrue("=" in exercises[0])  # 确保表达式格式正确

    def test_generate_multiple_expressions(self):
        """测试批量生成题目"""
        exercises = generate_exercises(10, 10)
        self.assertEqual(len(exercises), 10)

    def test_no_negative_subtraction(self):
        """测试不会生成负数结果的减法"""
        exercises = generate_exercises(50, 10)
        for expr in exercises:
            if "-" in expr:
                parts = expr.split(" - ")
                left, right = parts[0], parts[1].replace(" =", "")
                self.assertGreaterEqual(eval(left), eval(right))

    def test_no_duplicate_expressions(self):
        """测试生成的题目不会重复"""
        exercises = generate_exercises(100, 10)
        self.assertEqual(len(set(exercises)), 100)

    def test_correct_fraction_format(self):
        """测试题目中的分数格式"""
        exercises = generate_exercises(10, 10)
        for expr in exercises:
            parts = expr.split(" ")
            for part in parts:
                if "/" in part and part != "=":
                    num, den = part.split("/")
                    self.assertTrue(num.isdigit() and den.isdigit())  # 确保分子和分母是数字

    def test_large_number_range(self):
        """测试较大范围内生成的分数"""
        exercises = generate_exercises(5, 100)
        self.assertEqual(len(exercises), 5)

    def test_small_number_range(self):
        """测试较小范围内生成的分数"""
        exercises = generate_exercises(5, 5)
        self.assertEqual(len(exercises), 5)

    def test_no_empty_expressions(self):
        """测试不会生成空表达式"""
        exercises = generate_exercises(10, 10)
        for expr in exercises:
            self.assertNotEqual(expr.strip(), "")

    def test_zero_questions(self):
        """测试 0 题目的情况"""
        exercises = generate_exercises(0, 10)
        self.assertEqual(len(exercises), 0)

    def test_massive_generation(self):
        """测试 10000 题目生成"""
        exercises = generate_exercises(10000, 50)
        self.assertEqual(len(exercises), 10000)

if __name__ == '__main__':
    unittest.main()
