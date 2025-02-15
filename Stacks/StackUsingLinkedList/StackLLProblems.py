class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data

    def is_empty(self):
        return self.num_elements == 0

    def size(self):
        return self.num_elements

    def print_stack(self):
        current = self.head
        while current:
            print(current.data, end=" --> ")
            current = current.next
        print("NULL")

    def insert_at_bottom(self, item):
        """ Insert an item at the bottom of the stack using recursion """
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def reverse_stack(self):
        """ Reverse the stack using recursion """
        if self.is_empty():
            return  # Base case: Stop when stack is empty
        temp = self.pop()
        self.reverse_stack()
        self.insert_at_bottom(temp)


# ------------------------------
# TESTING THE STACK OPERATIONS
# ------------------------------
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)

print("\nOriginal Stack:")
s.print_stack()  # Output: 50 --> 40 --> 30 --> 20 --> 10 --> NULL

print("\nPeek:", s.peek())  # Output: 50
print("Pop:", s.pop())  # Output: 50
s.print_stack()  # Output: 40 --> 30 --> 20 --> 10 --> NULL
print("Is the stack empty?", s.is_empty())  # Output: False
print("Size of Stack:", s.size())  # Output: 4

# Reverse the stack
print("\nReversing Stack...")
s.reverse_stack()

print("\nReversed Stack:")
s.print_stack()  # Output: 10 --> 20 --> 30 --> 40 --> NULL


# -------------------------------------
# PROBLEM 1: CHECKING BALANCED PARENTHESES
# -------------------------------------
def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":
            stack.push(char)
        elif char in ")}]":
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False
    return stack.is_empty()


print("\nBalanced Parentheses Check:")
print(is_balanced("{[()]}"))  # Output: True
print(is_balanced("{[(])}"))  # Output: False


# -------------------------------------
# PROBLEM 2: MIN STACK
# -------------------------------------
class MinStack:
    def __init__(self):
        self.stack = Stack()
        self.min_stack = Stack()  # Extra stack to track min values

    def push(self, x):
        self.stack.push(x)
        if self.min_stack.is_empty() or x <= self.min_stack.peek():
            self.min_stack.push(x)

    def pop(self):
        if not self.stack.is_empty():
            if self.stack.peek() == self.min_stack.peek():
                self.min_stack.pop()
            return self.stack.pop()

    def get_min(self):
        return self.min_stack.peek()


# Testing Min Stack
min_s = MinStack()
min_s.push(3)
min_s.push(5)
print("\nMin Stack:")
print("Min:", min_s.get_min())  # Output: 3
min_s.push(2)
min_s.push(1)
print("Min:", min_s.get_min())  # Output: 1
min_s.pop()
print("Min:", min_s.get_min())  # Output: 2


# -------------------------------------
# PROBLEM 3: SORT A STACK USING RECURSION
# -------------------------------------
def sorted_insert(stack, element):
    """ Helper function to insert an element in sorted order """
    if stack.is_empty() or element > stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.push(temp)


def sort_stack(stack):
    """ Function to sort stack using recursion """
    if not stack.is_empty():
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)


# Testing Sorting
s = Stack()
s.push(3)
s.push(1)
s.push(4)
s.push(2)

print("\nOriginal Stack Before Sorting:")
s.print_stack()  # Output: 2 --> 4 --> 1 --> 3 --> NULL

sort_stack(s)

print("\nSorted Stack:")
s.print_stack()  # Output: 1 --> 2 --> 3 --> 4 --> NULL


def evaluate_rpn_linkedlist(expression):
    stack = Stack()
    operators = {'+', '-', '*', '/'}

    for token in expression:
        if token not in operators:  # If it's a number, push to stack
            stack.push(int(token))
        else:  # It's an operator, pop two numbers and apply operation
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.push(a + b)
            elif token == '-':
                stack.push(a - b)
            elif token == '*':
                stack.push(a * b)
            elif token == '/':
                stack.push(int(a / b))  # Integer division for consistency

    return stack.pop()  # Final result


# Example Usage

print("Result:", evaluate_rpn_linkedlist(["2", "5", "+", "4", "*"]))  # Output: 16
