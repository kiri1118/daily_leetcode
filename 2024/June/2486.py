# 6/3/2024
# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/
# 2486 - Append Characters to String to Make Subsequence
# Loop through s with a pointer for t to keep track of which part of the subsequence is already covered, then return the difference that needs to be appended.
# Time: O(n), Space: O(1)
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        for c in s:
            if t_index >= len(t):
                return 0
            if c == t[t_index]:
                t_index += 1
        return len(t) - t_index
