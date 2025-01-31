class Node:
    def __init__(self, value):
        self.value = value  # Data stored in node
        self.left = None     # Left child
        self.right = None    # Right child


# Creating nodes
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)  # Left
        print(node.value, end=" ")    # Root
        inorder_traversal(node.right) # Right

print("Inorder Traversal:")
inorder_traversal(root)  # Output: 2 5 7 10 15 20

# Tree structure:
#         10
#        /  \
#       5    15
#      / \     \
#     2   7    20

