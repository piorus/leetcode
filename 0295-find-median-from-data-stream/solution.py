"""
Problem: 295. Find Median from Data Stream
Difficulty: Hard
Concepts: Min. Heap, Max. Heap
Link: https://leetcode.com/problems/find-median-from-data-stream
================
Time complexity:
    addNum() -> O(logn)
    findMedian() -> O(1)
Space complexity:
    addNum() -> O(n)
    findMedian() -> O(n)
"""

from heapq import heappop, heappush

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) > len(self.right): 
            heappush(self.right, num)
        else:
            heappush(self.left, -num)
        
        while self.left and self.right and -self.left[0] > self.right[0]:
            left = heappop(self.left)
            right = heappop(self.right)
            heappush(self.left, -right)
            heappush(self.right, -left)


    def findMedian(self) -> float:
        if not self.left and not self.right:
            return 0.0

        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2
        elif len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return self.right[0]
