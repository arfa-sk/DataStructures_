class Node:
    """A Node in a Singly Linked List"""
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    """Singly Linked List Implementation"""
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

    def insert_at_beginning(self, value):
        """Insert an element at the beginning of the list"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def delete(self, value):
        """Delete a node with the given value"""
        if not self.head:
            return "List is empty"

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next:
            current.next = current.next.next
        else:
            return "Value not found"

    def display(self):
        """Display the linked list"""
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(10)
    sll.insert_at_end(20)
    sll.insert_at_end(30)
    sll.display()
    sll.delete(20)
    sll.display()
