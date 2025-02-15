def counting_sort(arr):
    """Counting Sort Algorithm - O(n) Time Complexity"""
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, freq in enumerate(count):
        sorted_arr.extend([i] * freq)

    return sorted_arr


# Example Usage
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Sorted array:", counting_sort(arr))
