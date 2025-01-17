"""
Problem: 140. Word Break II
Difficulty: Hard
Concepts: DFS
Link: https://leetcode.com/problems/word-break-ii/
================
Time complexity: O(n * 2^n)
Space complexity: O(n)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        
        def dfs(start_index, path):
            if start_index == len(s):
                result.append(" ".join(path))
                return
            
            for end_index in range(start_index, len(s)):
                w = s[start_index:end_index + 1]
                if w in wordDict:
                    dfs(end_index + 1, path + [w])
        
        dfs(0, [])

        return result
