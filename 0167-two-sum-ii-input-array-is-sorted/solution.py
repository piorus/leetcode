"""
Problem: 167. Two Sum II - Input Array Is Sorted
Difficulty: Medium
Concepts: Two Pointers
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
================
Time complexity: O(n)
Space complexity: O(1)
"""


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            candidate = numbers[left] + numbers[right]

            if candidate == target:
                return [left + 1, right + 1]
            elif candidate < target:
                left += 1
            else:
                right -= 1