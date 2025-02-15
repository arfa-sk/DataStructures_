def merge_sorted_lists(l1, l2):
    """Merge Two Sorted Linked Lists"""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.value < l2.value:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next
