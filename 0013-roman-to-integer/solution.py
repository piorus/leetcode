"""
Problem: 13. Roman to Integer
Difficulty: Easy
Concepts: Misc
Link: https://leetcode.com/problems/roman-to-integer/
================
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        i = 0
        n = len(s)
        total = 0

        while i < n:
            if i + 1 < n:
                chunk = s[i: i + 2]

                if chunk in mapping:
                    total += mapping[chunk]
                    i += 2
                    continue
            total += mapping[s[i]]
            i += 1

        return total