import sys
import os
import tempfile

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import os
from checker import check_answers

class TestChecker(unittest.TestCase):

    def setUp(self):
        """创建测试用的题目和答案文件"""
        with open("test_exercises.txt", "w") as ef, open("test_answers.txt", "w") as af:
            ef.write("1/6 + 1/8 =\n2/3 × 3/5 =\n5/9 - 1/4 =\n4 ÷ 2 =\n7/3 - 2/3 =\n")
            af.write("7/24\n2/5\n11/36\n2\n1'2/3\n")  # 正确答案

    def tearDown(self):
        """清理测试文件"""
        os.remove("test_exercises.txt")
        os.remove("test_answers.txt")
        if os.path.exists("Grade.txt"):
            os.remove("Grade.txt")

    def test_correct_answers(self):
        """测试所有答案正确的情况"""
        check_answers("test_exercises.txt", "test_answers.txt")
        with open("Grade.txt", "r") as gf:
            result = gf.read()
        self.assertIn("Correct: 5 (1, 2, 3, 4, 5)", result)

    def test_wrong_answers(self):
        """测试部分错误答案"""
        with open("test_answers.txt", "w") as af:
            af.write("7/24\n2/5\n2/7\n3\n2\n")  # 第3、4、5题错误

        check_answers("test_exercises.txt", "test_answers.txt")
        with open("Grade.txt", "r") as gf:
            result = gf.read()
        self.assertIn("Correct: 2 (1, 2)", result)
        self.assertIn("Wrong: 3 (3, 4, 5)", result)

    # def test_missing_file(self):
    #     """测试文件不存在的情况"""
    #     with self.assertRaises(FileNotFoundError):
    #         check_answers("nonexistent.txt", "test_answers.txt")

if __name__ == '__main__':
    unittest.main()
