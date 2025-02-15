class StackArrayList:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        print(f"Push {x}: {self.stack}")

    def pop(self):
        if not self.is_empty():
            popped = self.stack.pop()
            print(f"Pop {popped}: {self.stack}")
            return popped
        return "Stack is empty"

    def peek(self):
        return self.stack[-1] if not self.is_empty() else "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0



stack_arr = StackArrayList()
stack_arr.push(10)
stack_arr.push(20)
stack_arr.pop()
stack_arr.push(30)

