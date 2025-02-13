"""
Problem: 221. Maximal Square
Difficulty: Medium
Concepts: DP, DFS
Link: https://leetcode.com/problems/maximal-square
================
Time complexity: O(mn)
Space complexity: O(1)
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_count = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if r == 0 and c == 0:
                    left, up, diag = 0, 0, 0
                elif r == 0 and c != 0:
                    left, up, diag = matrix[r][c - 1], 0, 0
                elif r != 0 and c == 0:
                    left, up, diag = 0, matrix[r - 1][c], 0
                else:
                    left, up, diag = matrix[r][c - 1], matrix[r - 1][c], matrix[r - 1][c - 1]

                if matrix[r][c] == '1':
                    matrix[r][c] = 1 + min(left, up, diag)
                    max_count = max(max_count, matrix[r][c])
                else:
                    matrix[r][c] = 0

        return max_count ** 2

        # 2D DP

        # dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]

        # max_count = 0

        # for r in range(1, len(matrix) + 1):
        #     for c in range(1, len(matrix[r - 1]) + 1):
        #         if matrix[r - 1][c - 1] == '1':
        #             dp[r][c] = 1 + min(dp[r][c - 1], dp[r - 1][c], dp[r - 1][c - 1])
        #             max_count = max(max_count, dp[r][c])

        # return max_count ** 2

        # DFS with memoization

        # memo = {}

        # def dfs(r, c):
        #     if r >= len(matrix) or c >= len(matrix[0]) or matrix[r][c] == '0':
        #         return 0

        #     if (r, c) in memo:
        #         return memo[(r, c)]

        #     down = dfs(r + 1, c)
        #     right = dfs(r, c + 1)
        #     diagonal = dfs(r + 1, c + 1)

        #     memo[(r, c)] = 1 + min(down, right, diagonal)

        #     return memo[(r, c)]

        # result = 0

        # for r, _ in enumerate(matrix):
        #     for c, _ in enumerate(matrix[r]):
        #         if matrix[r][c] == '1':
        #             result = max(result, dfs(r, c))

        # return result ** 2