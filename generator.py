from calculator import eval_expr, calculate
import random
from utils import Fraction

def generate_fraction(r):
    """生成一个真分数（numerator < denominator），确保格式正确"""
    numerator = random.randint(1, r - 1)
    denominator = random.randint(2, r)
    while numerator >= denominator:  # 确保是 "真分数"
        numerator = random.randint(1, r - 1)
        denominator = random.randint(2, r)
    return Fraction(numerator, denominator)

def generate_expression(r, max_ops, used_expressions):
    """生成符合规则的真分数四则运算表达式"""
    ops = ['+', '-', '×', '÷']
    op_count = random.randint(1, min(3, max_ops))
    
    expr = generate_fraction(r)
    expr_str = str(expr)

    for _ in range(op_count):
        op = random.choice(ops)
        next_op = generate_fraction(r)

        # 确保减法不会出现负数
        if op == '-' and expr.numerator * next_op.denominator < next_op.numerator * expr.denominator:
            continue  

        # 确保除法不会除 0
        if op == '÷' and next_op.numerator == 0:
            continue  

        expr_str = f"{expr_str} {op} {next_op}"

    if expr_str in used_expressions:
        return None  # 避免重复
    used_expressions.add(expr_str)
    return expr_str

def generate_exercises(n, r):
    """生成 n 道真分数四则运算题目"""
    exercises = []
    used_expressions = set()
    attempts = 0

    while len(exercises) < n and attempts < n * 10:
        expr = generate_expression(r, 3, used_expressions)
        if expr:
            exercises.append(f"{expr} =")
        attempts += 1
        
    # with open("Exercises.txt", "w") as ef, open("Answers.txt", "w") as af:
    #     ef.write("\n".join(exercises))
    #     answers = [str(eval(ex.replace('×', '*').replace('÷', '/'))) for ex in exercises]
    #     af.write("\n".join(answers))  # Write answers to Answers.txt
    

    return exercises

# def generate_expression(r, op_count, used_expressions):
#     ops = ['+', '-', '*', '/']
#     expr = str(generate_operand(r))
#     for i in range(op_count):
#         op = random.choice(ops)
#         next_op = generate_operand(r)
#         if op == '/' and next_op == 0:
#             return None

#         if op == '-':
#             temp_expr = expr + ' - ' + str(next_op)
#             try:
#                 result = eval(temp_expr)
#                 if result < 0:  #Check for negative result *before* appending
#                     return None  # Reject expression if negative
#                 else:
#                     expr = temp_expr
#             except (SyntaxError, TypeError, ZeroDivisionError):
#                 return None # Reject on error
#         else:
#             expr += f' {op} {next_op}'
#     return expr if expr not in used_expressions else None


# def generate_exercises(n, r):
#     used_expressions = set()
#     exercises = []

#     for _ in range(n):
#         expr = generate_expression(r, 3, used_expressions)
#         while expr is None or eval(expr.replace('×', '*').replace('÷', '/')) < 0: # Check for None AND negative
#             expr = generate_expression(r, 3, used_expressions)
#         exercises.append(expr)
#         used_expressions.add(expr)

#     with open("Exercises.txt", "w") as ef, open("Answers.txt", "w") as af:
#         ef.write("\n".join(exercises))
#         answers = [str(eval(ex.replace('×', '*').replace('÷', '/'))) for ex in exercises]
#         af.write("\n".join(answers))  # Write answers to Answers.txt

#     return exercises

