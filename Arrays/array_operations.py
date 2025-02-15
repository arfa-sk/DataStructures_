# Array Operations: Insert, Reverse, Sort, and Search

def insert_element(arr, index, value):
    if 0 <= index <= len(arr):
        arr.insert(index, value)
    return arr

def reverse_array(arr):
    return arr[::-1]

def sort_array(arr):
    return sorted(arr)

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Element found at index {i}"
    return "Element not found!"

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return f"Element found at index {mid}"
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Element not found!"

# Example Usage
if __name__ == "__main__":
    arr = [5, 3, 8, 1, 9]
    print("Insert 7 at index 2:", insert_element(arr, 2, 7))
    print("Reverse array:", reverse_array(arr))
    print("Sorted array:", sort_array(arr))
    print("Linear Search for 8:", linear_search(arr, 8))
    print("Binary Search for 9:", binary_search(sorted(arr), 9))
