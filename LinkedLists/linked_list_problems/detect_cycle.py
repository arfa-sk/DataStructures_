def has_cycle(head):
    """Detect cycle using Floyd’s Cycle Detection Algorithm"""
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
