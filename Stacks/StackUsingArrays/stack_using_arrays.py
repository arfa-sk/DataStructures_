class StackArray:
    """Implementation of Stack using an Array"""
    def __init__(self, capacity=10):
        self.stack = []
        self.capacity = capacity

    def push(self, value):
        """Push an element onto the stack"""
        if len(self.stack) < self.capacity:
            self.stack.append(value)
        else:
            print("Stack Overflow! Cannot push more elements.")

    def pop(self):
        """Remove the top element of the stack"""
        if self.is_empty():
            return "Stack Underflow! Cannot pop from empty stack."
        return self.stack.pop()

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            return "Stack is empty."
        return self.stack[-1]

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.stack)

    def display(self):
        """Display all elements of the stack"""
        print("Stack (top to bottom):", self.stack[::-1])

# Example Usage
if __name__ == "__main__":
    stack = StackArray(capacity=5)
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    stack.display()
