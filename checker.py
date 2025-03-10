from calculator import calculate

def check_answers(exercise_file, answer_file):
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