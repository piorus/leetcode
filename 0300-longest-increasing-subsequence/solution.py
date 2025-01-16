"""
https://leetcode.com/problems/longest-increasing-subsequence
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
