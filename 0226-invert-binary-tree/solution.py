"""
Problem: 226. Invert Binary Tree
Difficulty: Easy
Concepts: DFS
Link: https://leetcode.com/problems/invert-binary-tree/
================
Time complexity: O(n)
Space complexity: O(n)
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def dfs(root):
            if not root:
                return None

            dfs(root.left)
            dfs(root.right)
            root.left, root.right = root.right, root.left

        dfs(root)

        return root