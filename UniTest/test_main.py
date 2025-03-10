import sys
import os

# 识别项目根目录下的模块
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import unittest
import sys
import os
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    def tearDown(self):
        for f in ['Exercises.txt', 'Answers.txt', 'Grade.txt']:
            if os.path.exists(f):
                os.remove(f)

    def test_generate_exercises(self):
        sys.argv = ['main.py', '-n', '5', '-r', '10']
        main()
        self.assertTrue(os.path.exists('Exercises.txt'))
        self.assertTrue(os.path.exists('Answers.txt'))
        with open('Exercises.txt', 'r') as ef:
            self.assertEqual(len(ef.readlines()), 5)

    def test_missing_n(self):
        sys.argv = ['main.py', '-r', '10']
        with self.assertRaises(SystemExit):
            main()

    def test_missing_r(self):
        sys.argv = ['main.py', '-n', '5']
        with self.assertRaises(SystemExit):
            main()

    def test_invalid_n(self):
        sys.argv = ['main.py', '-n', '-1', '-r', '10']
        with self.assertRaises(SystemExit):
            main()

    def test_invalid_r(self):
        sys.argv = ['main.py', '-n', '5', '-r', '0']
        with self.assertRaises(SystemExit):
            main()

    def test_grading(self):
        with open('Exercises.txt', 'w') as ef:
            ef.write("1 + 2 =\n")
        with open('Answers.txt', 'w') as af:
            af.write("3\n")
        sys.argv = ['main.py', '-e', 'Exercises.txt', '-a', 'Answers.txt']
        main()
        self.assertTrue(os.path.exists('Grade.txt'))
        with open('Grade.txt', 'r') as gf:
            self.assertIn("Correct: 1", gf.read())

    def test_missing_e(self):
        sys.argv = ['main.py', '-a', 'Answers.txt']
        with self.assertRaises(SystemExit):
            main()

    def test_missing_a(self):
        sys.argv = ['main.py', '-e', 'Exercises.txt']
        with self.assertRaises(SystemExit):
            main()

    def test_nonexistent_exercise_file(self):
        sys.argv = ['main.py', '-e', 'Nonexistent.txt', '-a', 'Answers.txt']
        with self.assertRaises(SystemExit):
            main()

    def test_large_n(self):
        sys.argv = ['main.py', '-n', '100', '-r', '10']
        main()
        with open('Exercises.txt', 'r') as ef:
            self.assertEqual(len(ef.readlines()), 100)

if __name__ == '__main__':
    unittest.main()