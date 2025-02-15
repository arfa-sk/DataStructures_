from collections import deque

class StackUsingQueues:
    def _init_(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        """ Push element into the stack """
        self.q1.append(value)

    def pop(self):
        """ Remove and return the top element """
        if not self.q1:
            return None  # Stack is empty
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped_value = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return popped_value

    def peek(self):
        """ Return top element without removing """
        if not self.q1:
            return None
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_value = self.q1.popleft()
        self.q2.append(top_value)
        self.q1, self.q2 = self.q2, self.q1
        return top_value

    def is_empty(self):
        return len(self.q1) == 0

    def insert_at_bottom(self, item):
        """ Insert an item at the bottom of the stack recursively """
        if self.is_empty():
            self.push(item)
        else:
            temp = self.pop()
            self.insert_at_bottom(item)
            self.push(temp)

    def reverse_stack(self):
        """ Reverse the stack using recursion """
        if not self.is_empty():
            temp = self.pop()
            self.reverse_stack()
            self.insert_at_bottom(temp)

    def print_stack(self):
        print("Stack (top to bottom):", list(self.q1)[::-1])

# Testing Reverse Stack
stack = StackUsingQueues()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("\nOriginal Stack:")
stack.print_stack()

print("\nReversing Stack...")
stack.reverse_stack()

print("\nReversed Stack:")
stack.print_stack()