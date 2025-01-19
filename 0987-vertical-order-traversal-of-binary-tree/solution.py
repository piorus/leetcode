"""
Problem: 987. Vertical Order Traversal of a Binary Tree
Difficulty: Hard
Concepts: BFS
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
================
Time complexity: O(nlogn)
Space complexity: O(n)
"""
from collections import defaultdict, deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = defaultdict(list)
        q = deque([(0, root)])
        row = 0

        while len(q) > 0:
            for _ in range(len(q)):
                col, root = q.popleft()
                result[(row, col)].append(root.val)

                if root.left:
                    q.append((col - 1, root.left))
                if root.right:
                    q.append((col + 1, root.right))
            row += 1

        answer = defaultdict(list)

        for row, col in sorted(result.keys(), key=lambda x: x[1]):
            answer[col] += sorted(result[(row, col)])

        return list(answer.values())