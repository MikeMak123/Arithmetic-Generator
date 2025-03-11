import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import os
import subprocess

class TestMain(unittest.TestCase):

    def tearDown(self):
        """删除测试生成的文件"""
        files = ["Exercises.txt", "Answers.txt", "Grade.txt"]
        for file in files:
            if os.path.exists(file):
                os.remove(file)

    def test_generate_exercises(self):
        """测试生成题目"""
        subprocess.run(["python", "main.py", "-n", "5", "-r", "10"], check=True)
        self.assertTrue(os.path.exists("Exercises.txt"))
        self.assertTrue(os.path.exists("Answers.txt"))

    def test_file_content(self):
        """测试生成的题目和答案格式"""
        subprocess.run(["python", "main.py", "-n", "5", "-r", "10"], check=True)
        with open("Exercises.txt", "r") as ef, open("Answers.txt", "r") as af:
            exercises = ef.readlines()
            answers = af.readlines()
        self.assertEqual(len(exercises), 5)
        self.assertEqual(len(answers), 5)
        self.assertTrue("=" in exercises[0])

    def test_grading(self):
        """测试判卷功能"""
        # 先生成题目
        subprocess.run(["python", "main.py", "-n", "5", "-r", "10"], check=True)

        # 判卷
        subprocess.run(["python", "main.py", "-e", "Exercises.txt", "-a", "Answers.txt"], check=True)
        self.assertTrue(os.path.exists("Grade.txt"))

    # def test_invalid_arguments(self):
    #     """测试缺少参数的情况"""
    #     result = subprocess.run(["python", "main.py", "-n", "5"], capture_output=True, text=True)
    #     self.assertIn("The -r parameter is required", result.stderr)

    # def test_invalid_exercise_file(self):
    #     """测试不存在的题目文件"""
    #     result = subprocess.run(["python", "main.py", "-e", "fake.txt", "-a", "Answers.txt"], capture_output=True, text=True)
    #     self.assertIn("❌ 错误：题目或答案文件未找到！", result.stdout)

if __name__ == '__main__':
    unittest.main()
