from utils import Fraction
import ast

# def eval_expr(expr):
#     """计算表达式的正确答案"""
#     expr = expr.replace('×', '*').replace('÷', '/')
#     try:
#         parts = expr.split()
#         if len(parts) == 1:
#             if '/' in parts[0]:
#                 n, d = map(int, parts[0].split('/'))
#                 return Fraction(n, d)
#             return int(parts[0])

#         left, op, right = parts[0], parts[1], parts[2]
#         left = eval_expr(left) if isinstance(left, str) else left
#         right = eval_expr(right) if isinstance(right, str) else right

#         if isinstance(left, int):
#             left = Fraction(left, 1)
#         if isinstance(right, int):
#             right = Fraction(right, 1)

#         if op == '+':
#             return left + right
#         if op == '-':
#             return left - right
#         if op == '*':
#             return left * right
#         if op == '/':
#             return left / right
#     # except Exception:
#     #     raise ValueError("Invalid expression")
#     except ZeroDivisionError:
#       raise ValueError("Division by zero")
#     except (SyntaxError, TypeError):
#       raise ValueError("Invalid expression")

# def calculate(expression):
#     """计算题目的答案"""
#     expr = expression.strip().rstrip(' =')
#     return str(eval_expr(expr))

def eval_expr(expr):
    """Evaluates an arithmetic expression string using Python's ast module."""
    expr = expr.replace("×", "*").replace("÷", "/")  # Replace symbols with standard operators
    try:
        tree = ast.parse(expr, mode='eval')
        result = eval(compile(tree, '<string>', 'eval'))
        if isinstance(result, Fraction):
            return str(result)  # Keep it as a fraction string
        elif isinstance(result, (int, float)):
            return str(result)
        else:
            return str(result)

    except (SyntaxError, NameError, TypeError):
        raise ValueError("Invalid expression")
    except ZeroDivisionError:
        raise ValueError("Division by zero")


def calculate(expr):
    """Calculates an expression string."""
    try:
        parts = expr.split("=")
        if len(parts) != 2:
            raise ValueError("Invalid format")
        
        result = eval_expr(parts[0].strip())
        return result
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError(str(e))