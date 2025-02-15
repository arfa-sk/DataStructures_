class Node:
    """A Node in a Doubly Linked List"""
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Doubly Linked List Implementation"""
    def __init__(self):
        self.head = None

    def insert_at_end(self, value):
        """Insert an element at the end of the list"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def insert_at_beginning(self, value):
        """Insert an element at the beginning of the list"""
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def display_forward(self):
        """Display the linked list in forward direction"""
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_beginning(0)
    dll.display_forward()
