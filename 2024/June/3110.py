# 6/1/2024
# https://leetcode.com/problems/score-of-a-string/
# 3110 - Score of a String
# Simple loop over the string, a straight forward question that doesn't need much explanation. ord() to get the ASCII.
# Time: O(n), Space: O(1)
class Solution:
    def scoreOfString(self, s: str) -> int:
        prev = ord(s[0])
        res = 0
        for c in s:
            curr = ord(c)
            res += abs(curr - prev)
            prev = curr
        return res