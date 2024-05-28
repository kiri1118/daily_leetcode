# 5/27/2024
# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/
# 1608 - Special Array With X Elements Greater Than or Equal X
# Binary Search
# Time: O(nlogn), Space: O(1)
# Alternatively without binary search, sort nums List.
from typing import List
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        l, r = 0, max(nums)
        while l <= r:
            m = (l + r) // 2
            c = self.check(nums, m) 
            if c == m:
                return m
            elif c < m:
                r = m - 1
            else:
                l = m + 1
        return -1
            
    def check(self, num, m):
        count = 0
        for n in num:
            if n >= m:
                count += 1
        return count