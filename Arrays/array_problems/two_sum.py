# Two Sum Problem: Find two numbers in an array that add up to a given target.

def two_sum(arr, target):
    hash_map = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hash_map:
            return [hash_map[diff], i]
        hash_map[num] = i
    return []

# Example Usage
if __name__ == "__main__":
    arr = [2, 7, 11, 15]
    target = 9
    print("Indices of two numbers adding to target:", two_sum(arr, target))
