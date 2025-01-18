"""
Problem: 2193. Minimum Number of Moves to Make Palindrome
Difficulty: Hard
Concepts: Two Pointers, Greedy
Link: https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
================
Time complexity: O(n^2)
Space complexity: O(n)
"""

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        num_swaps = 0
        l, r = 0, len(s) - 1
        s = list(s)

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

            index = r
            while index > l and s[index] != s[l]:
                index -= 1

            if index == l:
                s[l], s[l + 1] = s[l + 1], s[l]
                num_swaps += 1
                continue

            for i in range(index, r):
                s[i], s[i + 1] = s[i + 1], s[i]
                num_swaps += 1

            l += 1
            r -= 1

        return num_swaps