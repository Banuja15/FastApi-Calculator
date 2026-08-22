import ast


def evaluate(node):

    # Number
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid value")

    # Binary operations: + - * /
    if isinstance(node, ast.BinOp):

        left = evaluate(node.left)
        right = evaluate(node.right)

        if isinstance(node.op, ast.Add):
            return left + right

        elif isinstance(node.op, ast.Sub):
            return left - right

        elif isinstance(node.op, ast.Mult):
            return left * right

        elif isinstance(node.op, ast.Div):

            if right == 0:
                raise ZeroDivisionError

            return left / right

    # Negative / positive numbers
    if isinstance(node, ast.UnaryOp):

        operand = evaluate(node.operand)

        if isinstance(node.op, ast.USub):
            return -operand

        elif isinstance(node.op, ast.UAdd):
            return operand

    raise ValueError("Invalid expression")


def calculate(expression: str):

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree.body)