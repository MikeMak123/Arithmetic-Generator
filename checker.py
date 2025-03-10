from calculator import calculate

def check_answers(exercise_file, answer_file):
    """判卷，输出正确与错误题号"""
    with open(exercise_file, 'r') as ef, open(answer_file, 'r') as af:
        exercises = [line.strip() for line in ef.readlines()]
        answers = [line.strip() for line in af.readlines()]
    
    correct, wrong = [], []
    
    for i, (expr, ans) in enumerate(zip(exercises, answers), 1):
        correct_ans = calculate(expr)
        if correct_ans == ans:
            correct.append(i)
        else:
            wrong.append(i)

    with open('Grade.txt', 'w') as gf:
        gf.write(f"Correct: {len(correct)} ({', '.join(map(str, correct))})\n")
        gf.write(f"Wrong: {len(wrong)} ({', '.join(map(str, wrong))})\n")


# def check_answers(exercises_file, answers_file):
#     """Checks answers against exercises and writes results to Grade.txt."""
#     try:
#         with open(exercises_file, "r") as ef, open(answers_file, "r") as af, open("Grade.txt", "w") as gf:
#             exercises = ef.readlines()
#             answers = af.readlines()
#             correct_count = 0
#             correct_indices = []
#             wrong_count = 0
#             wrong_indices = []

#             for i, (exercise, answer) in enumerate(zip(exercises, answers)):
#                 exercise_line = exercise.strip().replace("×", "*").replace("÷", "/").split("=")[0].strip()
#                 answer_line = answer.strip()
#                 try:
#                     exercise_result = eval(exercise_line)
#                     answer_value = eval(answer_line)

#                     # Use a tolerance for floating-point comparisons
#                     if abs(exercise_result - answer_value) < 1e-9:  # Tolerance of 1e-9
#                         correct_count += 1
#                         correct_indices.append(i + 1)
#                     else:
#                         wrong_count += 1
#                         wrong_indices.append(i + 1)
#                 except (ValueError, SyntaxError, TypeError, ZeroDivisionError) as e:
#                     print(f"Error evaluating exercise {i + 1}: {e}")
#                     wrong_count += 1
#                     wrong_indices.append(i + 1)

#             correct_str = f"Correct: {correct_count} ({', '.join(map(str, correct_indices))})" if correct_count > 0 else "Correct: 0 ()"
#             wrong_str = f"Wrong: {wrong_count} ({', '.join(map(str, wrong_indices))})" if wrong_count > 0 else "Wrong: 0 ()"
#             gf.write(correct_str + "\n" + wrong_str + "\n")

#     except FileNotFoundError:
#         raise FileNotFoundError("Exercises or answers file not found.")




