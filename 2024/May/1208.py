# 5/28/2024
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
# 1208 - Get Equal Substrings Within Budget
# Sliding Window
# Time: O(n), Space: O(1)
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = end = 0
        res = 0
        while end < len(s):
            maxCost -= self.abs_diff(s, t, end)
            end += 1
            while maxCost < 0 and start <= end:
                maxCost += self.abs_diff(s, t, start)
                start += 1
            if start > end:
                start = end
            res = max(res, end - start)
        return res
    def abs_diff(self, s, t, index):
        return abs(ord(s[index]) - ord(t[index]))
