"""
Problem: 125. Valid Palindrome
Difficulty: Easy
Concepts: Two Pointers
Link: https://leetcode.com/problems/valid-palindrome/
================
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True