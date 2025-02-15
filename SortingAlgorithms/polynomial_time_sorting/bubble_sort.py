def bubble_sort(arr):
    """Bubble Sort Algorithm - O(n²) Time Complexity"""
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  # Optimization to stop if already sorted

    return arr

# Example Usage
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    print("Sorted array:", bubble_sort(arr))
