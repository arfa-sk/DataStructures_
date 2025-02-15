def eval_rpn(tokens):
    """Evaluate Reverse Polish Notation (Postfix Expression)"""
    stack = []

    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # Truncate towards zero
        else:
            stack.append(int(token))

    return stack[0]


# Example Usage
if __name__ == "__main__":
    print(eval_rpn(["2", "1", "+", "3", "*"]))  # (2 + 1) * 3 = 9
    print(eval_rpn(["4", "13", "5", "/", "+"]))  # 4 + (13 / 5) = 6
