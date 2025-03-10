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
        self.tempdir = tempfile.TemporaryDirectory()
        self.exercises_file = os.path.join(self.tempdir.name, "test_exercises.txt")
        self.answers_file = os.path.join(self.tempdir.name, "test_answers.txt")

    def tearDown(self):
        self.tempdir.cleanup()

    def create_files(self, exercises, answers):
        with open(self.exercises_file, "w") as ef, open(self.answers_file, "w") as af:
            ef.write(exercises)
            af.write(answers)

    def test_correct_answers(self):
        exercises = "1 + 1 =\n2 * 2 =\n3 / 2 =\n5 - 3 =\n"
        answers = "2\n4\n1.5\n2\n"
        self.create_files(exercises, answers)
        check_answers(self.exercises_file, self.answers_file)
        with open("Grade.txt", "r") as gf:
            result = gf.read().strip()
        self.assertIn("Correct: 3", result)  # Check for correct count


    def test_wrong_answers(self):
        exercises = "1 + 1 =\n2 * 2 =\n3 / 2 =\n5 - 3 =\n"
        answers = "3\n4\n2\n0\n"
        self.create_files(exercises, answers)
        check_answers(self.exercises_file, self.answers_file)
        with open("Grade.txt", "r") as gf:
            result = gf.read().strip()
        self.assertIn("Wrong: 3", result)  # Check for correct count

    def test_mixed_answers(self):
        exercises = "1 + 1 =\n2 * 2 =\n3 / 2 =\n5 - 3 =\n"
        answers = "2\n4\n1.5\n0\n"
        self.create_files(exercises, answers)
        check_answers(self.exercises_file, self.answers_file)
        with open("Grade.txt", "r") as gf:
            result = gf.read().strip()
        self.assertIn("Correct: 2", result)
        self.assertIn("Wrong: 2", result)

    def test_empty_files(self):
        self.create_files("", "")
        check_answers(self.exercises_file, self.answers_file)
        with open("Grade.txt", "r") as gf:
            result = gf.read().strip()
        self.assertEqual(result, "Correct: 0 ()\nWrong: 0 ()")


    def test_invalid_expression(self):
        exercises = "1 + 1 =\n2 * 2 =\n3 / 0 =\n5 - 3 =\n"
        answers = "2\n4\n1.5\n2\n"
        self.create_files(exercises, answers)
        check_answers(self.exercises_file, self.answers_file)
        with open("Grade.txt", "r") as gf:
            result = gf.read().strip()
        self.assertIn("Wrong: 2", result)

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            check_answers("nonexistent_file.txt", self.answers_file)

if __name__ == '__main__':
    unittest.main()