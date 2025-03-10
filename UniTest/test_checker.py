import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import os
from checker import check_answers

class TestChecker(unittest.TestCase):

    def setUp(self):
        with open("test_exercises.txt", "w") as ef, open("test_answers.txt", "w") as af:
            ef.write("1 + 1 =\n2 × 2 =\n3 ÷ 2 =\n5 - 3 =\n")
            af.write("2\n4\n1/2\n2\n")

    def tearDown(self):
        os.remove("test_exercises.txt")
        os.remove("test_answers.txt")
        if os.path.exists("Grade.txt"):
            os.remove("Grade.txt")

    def test_correct_answers(self):
        check_answers("test_exercises.txt", "test_answers.txt")
        with open("Grade.txt", "r") as gf:
            result = gf.read()
        self.assertIn("Correct: 4 (1, 2, 3, 4)", result)

    def test_wrong_answers(self):
        with open("test_answers.txt", "w") as af:
            af.write("3\n4\n2/3\n0\n")  # 修改部分错误答案
        check_answers("test_exercises.txt", "test_answers.txt")
        with open("Grade.txt", "r") as gf:
            result = gf.read()
        self.assertIn("Wrong: 2", result)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            check_answers("nonexistent.txt", "test_answers.txt")

if __name__ == '__main__':
    unittest.main()
