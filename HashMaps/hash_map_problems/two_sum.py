def two_sum(nums, target):
    """Find two numbers in an array that sum to a given target."""
    hash_map = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return []

# Example Usage
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
