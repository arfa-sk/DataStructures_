def reverse_list(head):
    """Reverse a Linked List"""
    prev, current = None, head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev
