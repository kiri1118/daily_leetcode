# 6/10/2024
# https://leetcode.com/problems/height-checker/description/
# 1051 - Height Checker
# Used built in sort function, can use other sorting methods
# Time: O(nlogn), Space: O(n)
from typing import List
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        res = 0
        for index in range(len(heights)):
            if heights[index] != expected[index]:
                res += 1
        return res