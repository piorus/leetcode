"""
Problem: 32. Longest Valid Parentheses
Difficulty: Hard
Concepts: Stack
Link: https://leetcode.com/problems/longest-valid-parentheses/
================
Time complexity: O(n) 
Space complexity: O(n)
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        stack = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)

            if s[i] == ')' and len(stack) == 0 or s[stack[-1]] == ')':
                stack.append(i)
            elif s[i] == ')' and s[stack[-1]] == '(':
                stack.pop()
            
            dp[i] = i - (stack[-1] if len(stack) else -1)

        return max(dp) if len(dp) else 0
