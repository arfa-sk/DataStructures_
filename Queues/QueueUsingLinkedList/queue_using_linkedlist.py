class Node:
    """A Node in the Linked List"""
    def __init__(self, value):
        self.value = value
        self.next = None

class QueueLinkedList:
    """Queue Implementation Using Linked List"""
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value):
        """Add an element to the rear of the queue"""
        new_node = Node(value)
        if self.rear:
            self.rear.next = new_node
        self.rear = new_node
        if self.front is None:
            self.front = new_node
        self.size += 1

    def dequeue(self):
        """Remove an element from the front of the queue"""
        if self.is_empty():
            return "Queue Underflow! Cannot remove element."
        dequeued_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None  # Reset queue if empty
        self.size -= 1
        return dequeued_value

    def peek(self):
        """Return the front element without removing it"""
        return self.front.value if not self.is_empty() else "Queue is empty."

    def is_empty(self):
        """Check if the queue is empty"""
        return self.front is None

    def get_size(self):
        """Return the number of elements in the queue"""
        return self.size

    def display(self):
        """Display all elements of the queue"""
        current = self.front
        print("Queue (front to rear):", end=" ")
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example Usage
if __name__ == "__main__":
    queue = QueueLinkedList()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Front element:", queue.peek())
    print("Dequeued element:", queue.dequeue())
    queue.display()
