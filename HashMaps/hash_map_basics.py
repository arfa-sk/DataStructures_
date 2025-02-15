class HashMap:
    def __init__(self, size=10):
        """Initialize the Hash Map with a fixed size."""
        self.size = size
        self.map = [None] * self.size

    def hash_function(self, key):
        """Basic Hash Function using Modulo Operation."""
        return key % self.size

    def put(self, key, value):
        """Insert key-value pair into the Hash Map."""
        index = self.hash_function(key)
        self.map[index] = value

    def get(self, key):
        """Retrieve the value associated with the key."""
        index = self.hash_function(key)
        return self.map[index] if self.map[index] is not None else "Key not found"

    def remove(self, key):
        """Remove a key-value pair from the Hash Map."""
        index = self.hash_function(key)
        self.map[index] = None

    def display(self):
        """Display the Hash Map."""
        for i, value in enumerate(self.map):
            print(f"Index {i}: {value}")

# Example Usage
if __name__ == "__main__":
    hashmap = HashMap(size=10)
    hashmap.put(5, "Apple")
    hashmap.put(15, "Banana")  # Collision occurs
    hashmap.put(25, "Cherry")  # Another collision
    hashmap.display()

    print("Get value at key 15:", hashmap.get(15))
    hashmap.remove(15)
    print("Get value at key 15 after removal:", hashmap.get(15))
