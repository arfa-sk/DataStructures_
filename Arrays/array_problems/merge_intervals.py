# Merge Overlapping Intervals

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]

    for i in range(1, len(intervals)):
        prev = merged[-1]
        curr = intervals[i]
        if curr[0] <= prev[1]:  # Overlapping case
            merged[-1] = [prev[0], max(prev[1], curr[1])]
        else:
            merged.append(curr)

    return merged

# Example Usage
if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Merged Intervals:", merge_intervals(intervals))
