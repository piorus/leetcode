"""
https://leetcode.com/problems/word-break-ii
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
