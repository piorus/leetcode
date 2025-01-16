"""
https://leetcode.com/problems/word-search-ii
"""

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root

        for c in word:
            node = node.children[c]
        
        node.is_end_of_word = True

    def remove(self, word):
        node = self.root

        for c in word:
            node = node.children[c]
        
        node.is_end_of_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        NUM_ROWS, NUM_COLS = len(board), len(board[0])
        res = set()
        visited = set()
        
        def dfs(r, c, node, path):
            if (
                r < 0 or c < 0 or
                r >= NUM_ROWS or c >= NUM_COLS or
                (r, c) in visited or
                board[r][c] not in node.children
            ):
                return
            
            visited.add((r, c))
            char = board[r][c]
            node = node.children[char]
            path.append(char)
            
            if node.is_end_of_word:
                res.add("".join(path))
                trie.remove("".join(path))

            dfs(r - 1, c, node, path)
            dfs(r + 1, c, node, path)
            dfs(r, c - 1, node, path)
            dfs(r, c + 1, node, path)

            visited.remove((r, c))
            path.pop()

        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                dfs(r, c, trie.root, [])
        
        return list(res)
