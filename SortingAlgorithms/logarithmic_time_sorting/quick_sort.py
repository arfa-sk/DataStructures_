def quick_sort(arr):
    """Quick Sort Algorithm - O(n log n) Time Complexity"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example Usage
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Sorted array:", quick_sort(arr))
