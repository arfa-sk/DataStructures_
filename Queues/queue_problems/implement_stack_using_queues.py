from collections import deque

class StackUsingQueues:
    """Stack Implementation Using Two Queues"""
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, value):
        """Push element onto stack"""
        self.q1.append(value)

    def pop(self):
        """Remove and return top element (Simulated Stack Behavior)"""
        if not self.q1:
            return "Stack Underflow!"
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1  # Swap queues
        return popped

    def top(self):
        """Return top element without removing it"""
        return self.q1[-1] if self.q1 else "Stack is empty."

    def is_empty(self):
        """Check if stack is empty"""
        return not self.q1

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.q1)

# Example Usage
if __name__ == "__main__":
    stack = StackUsingQueues()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.top())
    print("Popped element:", stack.pop())
    print("Stack size:", stack.size())
