from calculator import eval_expr
import random
from utils import Fraction

def generate_operand(r):
    """生成随机操作数（自然数 或 真分数）"""
    if random.choice([True, False]):
        return random.randint(0, r - 1)
    else:
        num = random.randint(1, r - 1)
        den = random.randint(2, r - 1)
        return Fraction(num, den) if num < den else Fraction(den, num)

# def generate_expression(r, max_ops, used_expressions):
#     """生成符合规则的随机算式"""
#     ops = ['+', '-', '×', '÷']
#     op_count = random.randint(1, min(3, max_ops))
#     expr = str(generate_operand(r))
    
#     for _ in range(op_count):
#         op = random.choice(ops)
#         next_op = generate_operand(r)

#         # 处理特殊情况
#         if op == '-' and eval_expr(expr) < next_op:
#             continue  # 避免负数
#         if op == '÷' and next_op == 0:
#             continue  # 避免除以 0
        
#         new_expr = f"({expr} {op} {next_op})"
#         normalized = normalize(new_expr)
        
#         if normalized not in used_expressions:
#             expr = new_expr
#             used_expressions.add(normalized)
#         else:
#             return None  # 避免重复
#     return expr

# def normalize(expr):
#     """标准化表达式，避免重复"""
#     return expr.replace(" ", "").replace("×", "*").replace("÷", "/")

# def generate_exercises(n, r):
#     """批量生成 n 道符合规则的四则运算题目"""
#     exercises = []
#     used_expressions = set()
#     attempts = 0

#     while len(exercises) < n and attempts < n * 10:
#         expr = generate_expression(r, 3, used_expressions)
#         if expr:
#             exercises.append(f"{expr} =")
#         attempts += 1

#     return exercises

def generate_expression(r, op_count, used_expressions):
    ops = ['+', '-', '*', '/']
    expr = str(random.randint(1, r))
    for i in range(op_count):
        op = random.choice(ops)
        next_op = random.randint(1, r)
        if op == '/' and next_op == 0:
            return None

        if op == '-':
            temp_expr = expr + ' - ' + str(next_op)
            try:
                result = eval(temp_expr)
                if result < 0:  #Check for negative result *before* appending
                    return None  # Reject expression if negative
                else:
                    expr = temp_expr
            except (SyntaxError, TypeError, ZeroDivisionError):
                return None # Reject on error
        else:
            expr += f' {op} {next_op}'
    return expr if expr not in used_expressions else None


# def generate_exercises(n, r):
#     """
#     Generates a specified number of unique arithmetic exercises.

#     Args:
#         n: The number of exercises to generate.
#         r: The upper limit for the numbers in the expressions.

#     Returns:
#         A list of unique arithmetic exercise strings.
#     """
#     # used_expressions = set()
#     # exercises = []
#     # while len(exercises) < n:
#     #     expr = generate_expression(r, 3, used_expressions)
#     #     if expr != "error":
#     #       try:
#     #         eval_expr(expr)
#     #         exercises.append(expr)
#     #         used_expressions.add(expr)

#     #       except:
#     #         pass
#     # return exercises
def generate_exercises(n, r):
    used_expressions = set()
    exercises = []

    for _ in range(n):
        expr = generate_expression(r, 3, used_expressions)
        while expr is None or eval(expr.replace('×', '*').replace('÷', '/')) < 0: # Check for None AND negative
            expr = generate_expression(r, 3, used_expressions)
        exercises.append(expr)
        used_expressions.add(expr)

    with open("Exercises.txt", "w") as ef, open("Answers.txt", "w") as af:
        ef.write("\n".join(exercises))
        answers = [str(eval(ex.replace('×', '*').replace('÷', '/'))) for ex in exercises]
        af.write("\n".join(answers))  # Write answers to Answers.txt

    return exercises