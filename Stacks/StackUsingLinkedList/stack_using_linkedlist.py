class Node:
    """Node class for Linked List"""
    def __init__(self, value):
        self.value = value
        self.next = None

class StackLinkedList:
    """Implementation of Stack using a Linked List"""
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        """Push an element onto the stack"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        """Remove the top element of the stack"""
        if self.is_empty():
            return "Stack Underflow! Cannot pop from empty stack."
        popped_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return popped_value

    def peek(self):
        """Return the top element without removing it"""
        if self.is_empty():
            return "Stack is empty."
        return self.top.value

    def is_empty(self):
        """Check if the stack is empty"""
        return self.top is None

    def get_size(self):
        """Return the number of elements in the stack"""
        return self.size

    def display(self):
        """Display all elements of the stack"""
        current = self.top
        print("Stack (top to bottom):", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    stack = StackLinkedList()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    print("Top element:", stack.peek())
    print("Popped element:", stack.pop())
    stack.display()
