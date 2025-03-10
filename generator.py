import random
from utils import Fraction

def generate_operand(r):
    if random.choice([True, False]):
        return random.randint(0, r - 1)
    else:
        num = random.randint(1, r - 1)
        den = random.randint(2, r - 1)
        return Fraction(num, den) if num < den else Fraction(den, num)

def generate_expression(r, max_ops, used_expressions):
    ops = ['+', '-', '×', '÷']
    op_count = random.randint(1, min(3, max_ops))
    expr = str(generate_operand(r))
    for _ in range(op_count):
        op = random.choice(ops)
        next_op = generate_operand(r)
        if op == '-' and eval_expr(expr) < next_op:
            continue  # Avoid negatives
        if op == '÷' and next_op == 0:
            continue  # Avoid division by zero
        new_expr = f"({expr} {op} {next_op})"
        normalized = normalize(new_expr)
        if normalized not in used_expressions:
            expr = new_expr
            used_expressions.add(normalized)
        else:
            return None
    return expr

def normalize(expr):
    # Simplified normalization (consider commutativity)
    return expr.replace(" ", "").replace("×", "*").replace("÷", "/")

def generate_exercises(n, r):
    exercises = []
    used_expressions = set()
    attempts = 0
    while len(exercises) < n and attempts < n * 10:
        expr = generate_expression(r, 3, used_expressions)
        if expr:
            exercises.append(f"{expr} =")
        attempts += 1
    return exercises