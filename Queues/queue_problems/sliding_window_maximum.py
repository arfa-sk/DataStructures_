from collections import deque

def sliding_window_maximum(arr, k):
    """Find Maximum in Every Window of Size K"""
    if not arr or k == 0:
        return []

    result = []
    q = deque()

    for i, num in enumerate(arr):
        while q and arr[q[-1]] <= num:
            q.pop()
        q.append(i)

        if q[0] < i - k + 1:
            q.popleft()

        if i >= k - 1:
            result.append(arr[q[0]])

    return result

# Example Usage
if __name__ == "__main__":
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Sliding Window Maximum:", sliding_window_maximum(arr, k))
