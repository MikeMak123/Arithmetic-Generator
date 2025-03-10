
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