def selection_sort(arr):
    """Selection Sort Algorithm - O(n²) Time Complexity"""
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
    return arr

# Example Usage
if __name__ == "__main__":
    arr = [29, 10, 14, 37, 13]
    print("Sorted array:", selection_sort(arr))
