from collections import deque

def oranges_rotting(grid):
    """Find Minimum Time Required for All Oranges to Rot"""
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_oranges = 0

    # Collect initial rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))  # (row, col, time)
            elif grid[r][c] == 1:
                fresh_oranges += 1

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    minutes_passed = 0

    while queue:
        r, c, minutes_passed = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh_oranges -= 1
                queue.append((nr, nc, minutes_passed + 1))

    return minutes_passed if fresh_oranges == 0 else -1

# Example Usage
if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print("Time Required:", oranges_rotting(grid))
