"""
Problem: 144. Binary Tree Preorder Traversal
Difficulty: Easy
Concepts: DFS
Link: https://leetcode.com/problems/binary-tree-preorder-traversal
================
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def dfs(root: Optional[TreeNode]):
            if not root:
                return

            result.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return result