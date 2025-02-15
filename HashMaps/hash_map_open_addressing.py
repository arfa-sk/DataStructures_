class HashMapOpenAddressing:
    def __init__(self, size=10):
        """Initialize Hash Map with Open Addressing."""
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key, i):
        """Hash Function using Linear Probing."""
        return (key + i) % self.size

    def put(self, key, value):
        """Insert Key-Value Pair using Linear Probing."""
        for i in range(self.size):
            index = self.hash_function(key, i)
            if self.table[index] is None or self.table[index][0] == key:
                self.table[index] = (key, value)
                return
        print("Hash Table Full!")

    def get(self, key):
        """Retrieve Value with Linear Probing."""
        for i in range(self.size):
            index = self.hash_function(key, i)
            if self.table[index] and self.table[index][0] == key:
                return self.table[index][1]
        return "Key not found"

    def remove(self, key):
        """Delete Key-Value Pair using Linear Probing."""
        for i in range(self.size):
            index = self.hash_function(key, i)
            if self.table[index] and self.table[index][0] == key:
                self.table[index] = None
                return
        print("Key not found")

    def display(self):
        """Display the Hash Table."""
        for i, item in enumerate(self.table):
            print(f"Index {i}: {item if item else 'Empty'}")

# Example Usage
if __name__ == "__main__":
    hashmap = HashMapOpenAddressing(size=7)
    hashmap.put(5, "Apple")
    hashmap.put(12, "Banana")  # Collision resolved using Linear Probing
    hashmap.put(19, "Cherry")  # Another collision resolved
    hashmap.display()
    print("Get value at key 12:", hashmap.get(12))
    hashmap.remove(12)
    hashmap.display()
