import heapq


def merge_sorted_arrays(arrays):
    """Merge multiple sorted arrays into one sorted array"""
    min_heap = []

    # Push the first element of each array into heap
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))  # (value, array_index, element_index)

    result = []

    while min_heap:
        value, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(value)

        # If there's another element in the same array, push it
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))

    return result


# Example Usage
if __name__ == "__main__":
    arrays = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    print("Merged sorted array:", merge_sorted_arrays(arrays))
