"""
Problem: 26. Remove Duplicates from Sorted Array
Difficulty: Easy
Concepts: Two Pointers
Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
================
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] > nums[slow]:
                slow += 1
                nums[slow] = nums[fast]

        return slow + 1