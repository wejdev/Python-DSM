from collections import deque

EMPTY, FRESH, ROTTEN = 0, 1, 2

def rotting_oranges(grid):
    def spread_rot(r, c, minutes):
        nonlocal fresh, changed
        if 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == FRESH:
            grid[r][c] = ROTTEN
            fresh -= 1
            changed = True
            rot_times[r][c] = min(rot_times[r][c], minutes)

    ROWS, COLS = len(grid), len(grid[0])
    fresh = sum(val == FRESH for row in grid for val in row)
    rot_times = [[float('inf')] * COLS for _ in range(ROWS)]

    minutes = 0
    while True:
        changed = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN and rot_times[r][c] == minutes:
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        spread_rot(r + dr, c + dc, minutes + 1)
        if not changed: break
        minutes += 1

    return minutes if fresh == 0 else -1

def rotting_oranges_queue(grid):
    ROWS, COLS = len(grid), len(grid[0])
    fresh = 0
    queue = deque()

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == ROTTEN:
                queue.append((r, c))
            elif val == FRESH:
                fresh += 1

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    minutes = 0

    while queue and fresh > 0:
        minutes += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and grid[nx][ny] == FRESH:
                    grid[nx][ny] = ROTTEN
                    queue.append((nx, ny))
                    fresh -= 1

    return minutes if fresh == 0 else -1

"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten,
because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0,
the answer is just 0.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.
"""
