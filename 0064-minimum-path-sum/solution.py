"""
Problem: 64. Minimum Path Sum
Difficulty: Medium
Concepts: DP
Link: https://leetcode.com/problems/minimum-path-sum/
================
Time complexity: O(mn)
Space complexity: O(1)
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for c in range(1, len(grid[0])):
            grid[0][c] = grid[0][c - 1] + grid[0][c]

        for r in range(1, len(grid)):
            for c in range(len(grid[r])):
                if c == 0:
                    grid[r][c] = grid[r - 1][c] + grid[r][c]
                else:
                    grid[r][c] = min(grid[r][c - 1], grid[r - 1][c]) + grid[r][c]

        return grid[-1][-1]