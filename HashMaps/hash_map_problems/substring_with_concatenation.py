def find_substring(s, words):
    """Find starting indices of substring formed by concatenating words."""
    from collections import Counter
    word_len = len(words[0])
    total_len = len(words) * word_len
    word_count = Counter(words)
    result = []

    for i in range(len(s) - total_len + 1):
        seen = Counter([s[j:j+word_len] for j in range(i, i+total_len, word_len)])
        if seen == word_count:
            result.append(i)

    return result

# Example Usage
if __name__ == "__main__":
    print(find_substring("barfoothefoobarman", ["foo", "bar"]))  # [0, 9]
