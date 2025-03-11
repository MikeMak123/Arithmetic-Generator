import ast
import operator
from fractions import Fraction


# def eval_expr(expr):
#     """Evaluates an arithmetic expression string using Python's ast module."""
#     expr = expr.replace("×", "*").replace("÷", "/")  # Replace symbols with standard operators
#     try:
#         tree = ast.parse(expr, mode='eval')
#         result = eval(compile(tree, '<string>', 'eval'))
#         if isinstance(result, Fraction):
#             return str(result)  # Keep it as a fraction string
#         elif isinstance(result, (int, float)):
#             return str(result)
#         else:
#             return str(result)

#     except (SyntaxError, NameError, TypeError):
#         raise ValueError("Invalid expression")
#     except ZeroDivisionError:
#         raise ValueError("Division by zero")


# def calculate(expr):
#     """Calculates an expression string."""
#     try:
#         parts = expr.split("=")
#         if len(parts) != 2:
#             raise ValueError("Invalid format")
        
#         result = eval_expr(parts[0].strip())
#         return result
#     except (ValueError, ZeroDivisionError) as e:
#         raise ValueError(str(e))


# 定义允许的数学运算
allowed_operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}

def eval_expr(expr):
    """解析并计算四则运算表达式，确保结果为真分数格式"""
    expr = expr.replace("×", "*").replace("÷", "/")  # 统一运算符
    tree = ast.parse(expr, mode='eval')  # 解析表达式

    def eval_node(node):
        if isinstance(node, ast.BinOp):  # 处理二元运算符
            left = eval_node(node.left)
            right = eval_node(node.right)
            if isinstance(left, int):
                left = Fraction(left, 1)
            if isinstance(right, int):
                right = Fraction(right, 1)
             # 确保减法不会出现负数
            if isinstance(node.op, ast.Sub) and left < right:
                left, right = right, left  # 交换顺序，确保 left ≥ right
                
            return allowed_operators[type(node.op)](left, right)
        elif isinstance(node, ast.Num):  # 处理数字（整数）
            return Fraction(node.n)
        else:
            raise ValueError("Unsupported expression")

    try:
        result = eval_node(tree.body)
        return str(format_fraction(result))  # 统一格式化输出
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except Exception:
        raise ValueError("Invalid expression")

def format_fraction(frac):
    """格式化分数为标准输出，如 1'2/3"""
    if frac.denominator == 1:
        return str(frac.numerator)  # 整数直接返回
    elif abs(frac.numerator) > frac.denominator:
        whole = frac.numerator // frac.denominator
        remainder = abs(frac.numerator % frac.denominator)
        return f"{whole}'{remainder}/{frac.denominator}" if remainder else str(whole)
    return f"{frac.numerator}/{frac.denominator}"  # 真分数格式

def calculate(expr):
    """计算并返回分数格式结果"""
    try:
        parts = expr.split("=")
        if len(parts) != 2:
            raise ValueError("Invalid format")
        
        result = eval_expr(parts[0].strip())
        return result
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError(str(e))