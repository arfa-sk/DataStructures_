class Stack:
    def __init__(self, initial_size=10):
        self.arr = [0 for _ in range(initial_size)]  # Fixed-size array initialized with 0
        self.next_index = 0  # Points to the next insertion position
        self.num_elements = 0  # Number of elements in stack

    def push(self, data):
        """ Add an element to the stack """
        if self.next_index == len(self.arr):  # Stack is full, double the capacity
            print("Out of space! Increasing array capacity ...")
            self._handle_stack_capacity_full()

        self.arr[self.next_index] = data
        self.next_index += 1
        self.num_elements += 1

    def pop(self):
        """ Remove and return the top element of the stack """
        if self.is_empty():
            return None
        self.next_index -= 1
        self.num_elements -= 1
        return self.arr[self.next_index]  # Return last added element

    def peek(self):
        """ Return the top element without removing it """
        if self.is_empty():
            return None
        return self.arr[self.next_index - 1]

    def is_empty(self):
        """ Check if the stack is empty """
        return self.num_elements == 0

    def size(self):
        """ Return the number of elements in stack """
        return self.num_elements

    def _handle_stack_capacity_full(self):
        """ Double the stack capacity when it's full """
        old_arr = self.arr
        self.arr = [0 for _ in range(2 * len(old_arr))]  # Double size
        for index, element in enumerate(old_arr):
            self.arr[index] = element  # Copy old elements

    def print_stack(self):
        """ Print the stack elements """
        print("Stack (top to bottom):", self.arr[:self.num_elements])


# ------------------------------
# TESTING THE STACK OPERATIONS
# ------------------------------
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print("\nOriginal Stack:")
stack.print_stack()  # Output: Stack (top to bottom): [1, 2, 3, 4, 5]

print("\nPeek:", stack.peek())  # Output: 5
print("Pop:", stack.pop())  # Output: 5
stack.print_stack()  # Output: [1, 2, 3, 4]
print("Is stack empty?", stack.is_empty())  # Output: False
print("Size of Stack:", stack.size())  # Output: 4

# Test automatic expansion
for i in range(6, 12):
    stack.push(i)

print("\nStack after expanding:")
stack.print_stack()  # Output should show expanded stack
print("Stack size:", len(stack.arr))  # Should be doubled (20)
