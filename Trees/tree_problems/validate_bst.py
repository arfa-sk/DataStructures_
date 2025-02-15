class Node:
    """A Node in the Binary Tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """
    Validate if a binary tree is a Binary Search Tree (BST).
    The function ensures that all left subtree values are < root, and right subtree values are > root.
    """
    if not root:
        return True  # An empty tree is a valid BST

    if not (min_val < root.value < max_val):
        return False  # Violates BST properties

    # Recursively validate left and right subtrees
    return (is_valid_bst(root.left, min_val, root.value) and
            is_valid_bst(root.right, root.value, max_val))


# Example Usage
if __name__ == "__main__":
    # Constructing a valid BST
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.left = Node(12)
    root.right.right = Node(20)

    print("Is valid BST?", is_valid_bst(root))  # Output: True

    # Constructing an invalid BST
    root_invalid = Node(10)
    root_invalid.left = Node(5)
    root_invalid.right = Node(15)
    root_invalid.right.left = Node(8)  # Incorrect position (should be > 10)

    print("Is valid BST?", is_valid_bst(root_invalid))  # Output: False
