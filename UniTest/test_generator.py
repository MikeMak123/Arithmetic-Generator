import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


import unittest
from generator import generate_exercises

class TestGenerator(unittest.TestCase):

    def test_generate_single_expression(self):
        exercises = generate_exercises(1, 10)
        self.assertEqual(len(exercises), 1)
    
    def test_generate_multiple_expressions(self):
        exercises = generate_exercises(10, 10)
        self.assertEqual(len(exercises), 10)

    def test_operator_limits(self):
        exercises = generate_exercises(100, 10)
        for expr in exercises:
            self.assertLessEqual(expr.count('+') + expr.count('-') + expr.count('×') + expr.count('÷'), 3)

    def test_no_negatives(self):
        exercises = generate_exercises(50, 10)
        for expr in exercises:
            expr = expr.replace('×', '*').replace('÷', '/')
            self.assertTrue(eval(expr) >= 0)

    def test_no_division_by_zero(self):
        exercises = generate_exercises(50, 10)
        for expr in exercises:
          
            self.assertNotIn('÷ 0', expr)
            self.assertNotIn('/ 0', expr)
    def test_uniqueness(self):
        exercises = generate_exercises(100, 10)
        self.assertEqual(len(set(exercises)), 100)

    def test_large_number_range(self):
        exercises = generate_exercises(5, 1000)
        self.assertEqual(len(exercises), 5)

    def test_minimal_number_range(self):
        exercises = generate_exercises(5, 2)
        self.assertEqual(len(exercises), 5)

    def test_empty_case(self):
        exercises = generate_exercises(0, 10)
        self.assertEqual(len(exercises), 0)

    def test_massive_generation(self):
        exercises = generate_exercises(10000, 100)
        self.assertEqual(len(exercises), 10000)


if __name__ == '__main__':
    unittest.main()
