"""
Problem: 58. Length of Last Word
Difficulty: Easy
Concepts: Misc
Link: https://leetcode.com/problems/length-of-last-word/description/
================
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        startFound = False

        for i in range(len(s) - 1, -1, -1):
            if not startFound and s[i] == " ":
                continue
            elif not startFound and s[i] != " ":
                startFound = True
            elif startFound and s[i] == " ":
                break
            length += 1

        return length