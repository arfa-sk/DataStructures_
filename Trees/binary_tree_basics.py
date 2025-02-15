class Node:
    """A Node in the Binary Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Basic Binary Tree Implementation"""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value into the tree (Level Order)"""
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def search(self, value):
        """Search for a value in the tree"""
        if not self.root:
            return False
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            if current.value == value:
                return True
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return False

    def display(self):
        """Display Tree using Level Order Traversal"""
        if not self.root:
            print("Tree is empty.")
            return
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            print(current.value, end=" ")
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)
    tree.display()
    print("Search 30:", tree.search(30))
    print("Search 100:", tree.search(100))
