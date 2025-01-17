"""
Problem: 65. Valid Number
Difficulty: Hard
Concepts: Misc
Link: https://leetcode.com/problems/valid-number/
================
Time complexity: O(1)
Space complexity: O(1)
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            blacklist = ["inf", "nan"]
            lower_s = s.lower()
            for token in blacklist:
                if token in lower_s:
                    return False

            float(s)
            return True
        except ValueError:
            return False       
