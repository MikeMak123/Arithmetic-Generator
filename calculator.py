from utils import Fraction

def eval_expr(expr):
    # Replace operators and evaluate safely
    expr = expr.replace('×', '*').replace('÷', '/')
    try:
        # For simplicity, assume integers or fractions
        parts = expr.split()
        if len(parts) == 1:
            if '/' in parts[0]:
                n, d = map(int, parts[0].split('/'))
                return Fraction(n, d)
            return int(parts[0])
        # Handle binary operations (simplified)
        left, op, right = parts[0], parts[1], parts[2]
        left = eval_expr(left) if isinstance(left, str) else left
        right = eval_expr(right) if isinstance(right, str) else right
        if isinstance(left, int):
            left = Fraction(left, 1)
        if isinstance(right, int):
            right = Fraction(right, 1)
        if op == '+':
            return left + right
        if op == '-':
            return left - right
        if op == '*':
            return left * right
        if op == '/':
            return left / right
    except Exception:
        raise ValueError("Invalid expression")

def calculate(expression):
    expr = expression.strip().rstrip(' =')
    result = eval_expr(expr)
    return str(result)