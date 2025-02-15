def bucket_sort(arr, bucket_size=5):
    """Bucket Sort Algorithm - O(n) Time Complexity"""
    if len(arr) == 0:
        return arr

    min_val, max_val = min(arr), max(arr)
    bucket_count = (max_val - min_val) // bucket_size + 1
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        buckets[(num - min_val) // bucket_size].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# Example Usage
if __name__ == "__main__":
    arr = [29, 25, 3, 49, 9, 37, 21, 43]
    print("Sorted array:", bucket_sort(arr))
