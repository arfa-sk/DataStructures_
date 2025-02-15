from functools import cmp_to_key


def compare(a, b):
    """Custom comparator to arrange numbers for forming the largest number"""
    return (b + a) > (a + b)  # Ensure correct lexicographical order


def largest_number(arr):
    """Rearrange numbers to form the largest possible number"""
    str_arr = list(map(str, arr))  # Convert numbers to strings
    sorted_arr = sorted(str_arr, key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))

    result = ''.join(sorted_arr)
    return result if result[0] != '0' else '0'  # Handle edge case: "000" -> "0"


# Example Usage
if __name__ == "__main__":
    arr = [3, 30, 34, 5, 9]
    print("Largest Number:", largest_number(arr))
