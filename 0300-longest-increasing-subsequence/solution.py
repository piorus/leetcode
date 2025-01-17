"""
Problem: 300. Longest Increasing Subsequence
Difficulty: Medium
Concepts: Binary search
Link: https://leetcode.com/problems/longest-increasing-subsequence/
================
Time complexity: O(n * logn)
Space complexity: O(n)
"""

from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence = []

        for num in nums:
            pos = bisect_left(sequence, num)

            if pos == len(sequence):
                sequence.append(num)
            else:
                sequence[pos] = num
        
        return len(sequence)
