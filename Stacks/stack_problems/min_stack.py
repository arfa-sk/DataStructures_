class MinStack:
    """Stack with O(1) Min Retrieval"""
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Keeps track of minimums

    def push(self, value):
        """Push element onto stack"""
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        """Remove top element and update min stack"""
        if self.stack:
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()
        return "Stack Underflow"

    def top(self):
        """Get top element without removing it"""
        return self.stack[-1] if self.stack else "Stack is empty"

    def get_min(self):
        """Retrieve minimum value in O(1)"""
        return self.min_stack[-1] if self.min_stack else "No elements"

    def display(self):
        """Display stack elements"""
        print("Stack:", self.stack)
        print("Min Stack:", self.min_stack)

# Example Usage
if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(5)
    min_stack.push(2)
    min_stack.push(10)
    min_stack.push(1)
    min_stack.display()
    print("Minimum:", min_stack.get_min())  # Should return 1
    min_stack.pop()
    min_stack.display()
    print("Minimum after pop:", min_stack.get_min())  # Should return 2
