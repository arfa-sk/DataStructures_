def insertion_sort(arr):
    """Insertion Sort Algorithm - O(n²) Time Complexity"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:  # Shift elements to the right
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example Usage
if __name__ == "__main__":
    arr = [8, 4, 23, 42, 16, 15]
    print("Sorted array:", insertion_sort(arr))
