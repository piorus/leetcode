"""
Problem: 115. Distinct Subsequences
Difficulty: Hard
Concepts: DFS with memoization
Link: https://leetcode.com/problems/distinct-subsequences/
================
Time complexity: O(n * m)
Space complexity: O(n * m)
"""
from functools import lru_cache

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0

            if s[i] == t[j]:
                return dfs(i + 1, j + 1) + dfs(i + 1, j)
            else:
                return dfs(i + 1, j)

        return dfs(0, 0)