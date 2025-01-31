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
            print(current.data, end="-->")
            current = current.next
        print("NULL")


s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.print_stack()

print("Peek:", s.peek())
print("Pop:", s.pop())
s.print_stack()
print("Is the stack empty", s.is_empty())
print("Size of Stack", s.size())

