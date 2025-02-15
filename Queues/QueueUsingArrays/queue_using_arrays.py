class QueueArray:
    """Queue Implementation Using Arrays"""
    def __init__(self, capacity=10):
        self.queue = []
        self.capacity = capacity

    def enqueue(self, value):
        """Add element to the rear of the queue"""
        if len(self.queue) < self.capacity:
            self.queue.append(value)
        else:
            print("Queue Overflow! Cannot add more elements.")

    def dequeue(self):
        """Remove element from the front of the queue"""
        if self.is_empty():
            return "Queue Underflow! Cannot remove element."
        return self.queue.pop(0)

    def peek(self):
        """Return the front element without removing it"""
        return self.queue[0] if not self.is_empty() else "Queue is empty."

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue"""
        return len(self.queue)

    def display(self):
        """Display all elements of the queue"""
        print("Queue (front to rear):", self.queue)

# Example Usage
if __name__ == "__main__":
    queue = QueueArray(capacity=5)
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    print("Front element:", queue.peek())
    print("Dequeued element:", queue.dequeue())
    queue.display()
