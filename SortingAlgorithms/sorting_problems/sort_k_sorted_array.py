import heapq

def sort_k_sorted_array(arr, k):
    """Sort a k-sorted array using Min Heap"""
    heap = []
    result = []

    # Add first k+1 elements to the heap
    for num in arr[:k+1]:
        heapq.heappush(heap, num)

    # Process the remaining elements
    for i in range(k+1, len(arr)):
        result.append(heapq.heappop(heap))  # Extract min
        heapq.heappush(heap, arr[i])  # Push next element

    # Extract remaining elements from heap
    while heap:
        result.append(heapq.heappop(heap))

    return result

# Example Usage
if __name__ == "__main__":
    arr = [6, 5, 3, 2, 8, 10, 9]
    k = 3
    print("Sorted array:", sort_k_sorted_array(arr, k))
