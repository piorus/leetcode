"""
Problem: 1768. Merge Strings Alternately
Difficulty: Easy
Concepts: Arrays
Link: https://leetcode.com/problems/merge-strings-alternately/
================
Time complexity: O(m + n)
Space complexity: O(1)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        pos1, pos2 = 0, 0

        while pos1 < len(word1) or pos2 < len(word2):
            if pos1 < len(word1):
                result += word1[pos1]
            if pos2 < len(word2):
                result += word2[pos2]

            pos1 += 1
            pos2 += 1

        return result