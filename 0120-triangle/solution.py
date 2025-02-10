"""
Problem: 120. Triangle
Difficulty: Medium
Concepts: DP
Link: https://leetcode.com/problems/triangle/
================
Time complexity: O(n)
Space complexity: O(1)
"""

import math

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    minimal = triangle[r - 1][c]
                elif r == c:
                    minimal = triangle[r - 1][c - 1]
                else:
                    minimal = min(triangle[r - 1][c], triangle[r - 1][c - 1])

                triangle[r][c] += minimal

        return min(triangle[-1])