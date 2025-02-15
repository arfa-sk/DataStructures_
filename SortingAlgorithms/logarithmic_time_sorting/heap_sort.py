import heapq

def heap_sort(arr):
    """Heap Sort Algorithm - O(n log n) Time Complexity"""
    heapq.heapify(arr)  # Convert list into a min-heap
    sorted_array = [heapq.heappop(arr) for _ in range(len(arr))]
    return sorted_array

# Example Usage
if __name__ == "__main__":
    arr = [3, 5, 1, 10, 2]
    print("Sorted array:", heap_sort(arr))
