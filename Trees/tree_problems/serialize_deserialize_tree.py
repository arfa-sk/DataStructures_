import json


class Node:
    """A Node in the Binary Tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def serialize(root):
    """Convert tree into a string"""
    if not root:
        return None
    return json.dumps(root, default=lambda obj: obj.__dict__)


def deserialize(data):
    """Convert string back into a tree"""
    if not data:
        return None
    return json.loads(data)


# Example Usage
if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    serialized = serialize(root)
    print("Serialized Tree:", serialized)

    deserialized = deserialize(serialized)
    print("Deserialized Tree Root:", deserialized["value"])
