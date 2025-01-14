"""
https://leetcode.com/problems/unique-paths-iii
"""

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        OBSTACLE, FIELD, START, TARGET = -1, 0, 1, 2
        num_obstacles = 0
        start_pos = None
        result = 0

        for r, row in enumerate(grid):
            for c, cell in enumerate(row):
                if cell == OBSTACLE:
                    num_obstacles += 1
                if cell == START:
                    start_pos = (r, c)

        if not start_pos:
            return result

        def dfs(r, c, path):
            if (
                r < 0 
                or c < 0 
                or r == ROWS 
                or c == COLS
                or (r, c) in path
            ):
                return

            if grid[r][c] == TARGET and len(path) == ROWS * COLS - num_obstacles - 1:
                nonlocal result
                result += 1
            
            if grid[r][c] in [TARGET, OBSTACLE]:
                return

            path.append((r, c))
            dfs(r + 1, c, path)
            dfs(r - 1, c, path)
            dfs(r, c + 1, path)
            dfs(r, c - 1, path)
            path.pop()

        dfs(start_pos[0], start_pos[1], [])

        return result
