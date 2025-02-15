class Node:
    """A Node in the Linked List for Chaining."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapChaining:
    def __init__(self, size=10):
        """Initialize HashMap with Linked List Buckets."""
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        """Simple Hash Function using Modulo."""
        return key % self.size

    def put(self, key, value):
        """Insert Key-Value Pair, handling Collisions with Chaining."""
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            current = self.table[index]
            while current.next:
                if current.key == key:
                    current.value = value  # Update existing key
                    return
                current = current.next
            current.next = Node(key, value)

    def get(self, key):
        """Retrieve Value using the Key."""
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return "Key not found"

    def remove(self, key):
        """Delete a Key-Value Pair."""
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

    def display(self):
        """Display the Hash Map with Chaining."""
        for i, node in enumerate(self.table):
            chain = []
            while node:
                chain.append(f"({node.key}: {node.value})")
                node = node.next
            print(f"Bucket {i}: {' -> '.join(chain) if chain else 'Empty'}")

# Example Usage
if __name__ == "__main__":
    hashmap = HashMapChaining(size=5)
    hashmap.put(1, "One")
    hashmap.put(6, "Six")  # Collision at index 1
    hashmap.put(11, "Eleven")  # Collision at index 1
    hashmap.display()
    print("Get value at key 6:", hashmap.get(6))
    hashmap.remove(6)
    hashmap.display()
