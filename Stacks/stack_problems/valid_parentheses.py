def is_valid_parentheses(s):
    """Check if the given string contains valid parentheses"""
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


# Example Usage
if __name__ == "__main__":
    print(is_valid_parentheses("()[]{}"))  # True
    print(is_valid_parentheses("(]"))  # False
    print(is_valid_parentheses("{[]}"))  # True
