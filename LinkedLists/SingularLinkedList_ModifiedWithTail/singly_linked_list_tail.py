class Node:
    """A Node in a Singly Linked List with Tail Pointer"""
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedListTail:
    """Singly Linked List with a Tail Pointer"""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        """Insert an element at the end of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_beginning(self, value):
        """Insert an element at the beginning of the list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def display(self):
        """Display the linked list"""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    sll_tail = SinglyLinkedListTail()
    sll_tail.insert_at_end(5)
    sll_tail.insert_at_end(10)
    sll_tail.display()
