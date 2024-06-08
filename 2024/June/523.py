# 6/8/2024
# https://leetcode.com/problems/continuous-subarray-sum/description/
# 523 - Continuous Subarray Sum
# Make use of the fact that subarray's sum can be calculated by subtracting prev sum from curr sum.
# By that I mean, take the array [a, b, c, d] for example, sum([c, d]) can be calculated by sum([a, b, c, d]) - sum([a, b]).
# Time: O(n), Space: O(n)
from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        hashmap = {0: -1}
        total = 0
        for i, n in enumerate(nums):
            total = (total + n) % k
            if total in hashmap: 
                if i - hashmap[total] > 1:
                    return True
            else:
                hashmap[total] = i
        return False
