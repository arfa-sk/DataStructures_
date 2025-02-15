class Node:
    """A Node in the Binary Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """Binary Tree with Different Traversal Methods"""
    def __init__(self, root_value):
        self.root = Node(root_value)

    def inorder(self, node):
        """Inorder Traversal (Left, Root, Right)"""
        if node:
            self.inorder(node.left)
            print(node.value, end=" ")
            self.inorder(node.right)

    def preorder(self, node):
        """Preorder Traversal (Root, Left, Right)"""
        if node:
            print(node.value, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        """Postorder Traversal (Left, Right, Root)"""
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=" ")

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.root.left = Node(20)
    tree.root.right = Node(30)
    tree.root.left.left = Node(40)
    tree.root.left.right = Node(50)

    print("Inorder Traversal:")
    tree.inorder(tree.root)
    print("\nPreorder Traversal:")
    tree.preorder(tree.root)
    print("\nPostorder Traversal:")
    tree.postorder(tree.root)
