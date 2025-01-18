"""
Problem: 41. First Missing Positive
Difficulty: Hard
Concepts: Misc
Link: https://leetcode.com/problems/first-missing-positive/
================
Time complexity: O(n)
Space complexity: O(1)
"""

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        is_one_present = False
        for i in range(n):
            if nums[i] == 1:
                is_one_present = True
            if nums[i] <= 0:
                nums[i] = 1

        if not is_one_present:
            return 1

        for i in range(n):
            index = abs(nums[i]) - 1
            if index >= n:
                continue
            if nums[index] > 0:
                nums[index] *= -1

        for i in range(0, n):
            if nums[i] > 0:
                return i + 1

        return n + 1