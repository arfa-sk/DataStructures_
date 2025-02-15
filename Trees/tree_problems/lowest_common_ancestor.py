class Node:
    """A Node in the Binary Tree"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, n1, n2):
    """Find the Lowest Common Ancestor (LCA) of two nodes"""
    if not root:
        return None
    if root.value == n1 or root.value == n2:
        return root

    left_lca = find_lca(root.left, n1, n2)
    right_lca = find_lca(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca else right_lca

# Example Usage
if __name__ == "__main__":
    root = Node(3)
    root.left = Node(5)
    root.right = Node(1)
    root.left.left = Node(6)
    root.left.right = Node(2)

    lca = find_lca(root, 6, 2)
    print("Lowest Common Ancestor:", lca.value)
