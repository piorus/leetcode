"""
Problem: 63. Unique Paths II
Difficulty: Medium
Concepts: DP
Link: https://leetcode.com/problems/unique-paths-ii/
================
Time complexity: O(n^2)
Space complexity: O(1)
"""

class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        OBSTACLE = 1
        g[0][0] = 0 if g[0][0] == OBSTACLE else 1

        for c in range(1, len(g[0])):
            if g[0][c] == OBSTACLE:
                g[0][c] = 0
            else:
                g[0][c] = g[0][c - 1]

        for r in range(1, len(g)):
            for c in range(len(g[r])):
                if g[r][c] == OBSTACLE:
                    g[r][c] = 0
                elif c == 0:
                    g[r][c] = g[r - 1][c]
                else:
                    g[r][c] = g[r - 1][c] + g[r][c - 1]

        return g[-1][-1]