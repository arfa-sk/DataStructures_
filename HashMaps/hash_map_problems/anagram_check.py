from collections import Counter

def is_anagram(str1, str2):
    """Check if two strings are anagrams using frequency count."""
    return Counter(str1) == Counter(str2)

# Example Usage
if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))    # False
