"""
Problem: 68. Text Justification
Difficulty: Hard
Concepts: Misc
Link: https://leetcode.com/problems/text-justification/
================
Time complexity: O(n)
Space complexity: O(n)
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i = 0
        lines = []

        while i < len(words):
            parts = []
            parts_length = 0
            while i < len(words) and parts_length + len(words[i]) + len(parts) - 1 < maxWidth:
                parts.append(words[i])
                parts_length += len(words[i])
                i += 1
            lines.append((parts_length, parts))

        answer = []

        for row, v in enumerate(lines):
            parts_length, parts = v
            is_last_line = row == len(lines) - 1
            remaining_spacing = maxWidth - parts_length

            if is_last_line:
                spacing_per_word = remaining_spacing - len(parts) + 1
                remaining_spacing -= (len(parts) - 1)
                parts = [" ".join(parts)]
            else:
                spacing_per_word = remaining_spacing // len(parts)

            end = len(parts) if is_last_line else len(parts) - 1

            for k in range(0, end):
                parts[k] += " " * spacing_per_word
                remaining_spacing -= spacing_per_word

            is_one_part = len(parts) == 1
            start = 0
            end = len(parts) - 1 if not is_one_part else len(parts)

            while remaining_spacing > 0:
                for k in range(start, end):
                    parts[k] += " "
                    remaining_spacing -= 1
                    if remaining_spacing == 0:
                        break
            answer.append("".join(parts))

        return answer