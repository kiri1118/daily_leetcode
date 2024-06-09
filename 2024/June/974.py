# 6/9/2024
# https://leetcode.com/problems/subarray-sums-divisible-by-k/
# 974 - Subarray Sums Divisible by K
# Similar concept to Problem 523, make use of the mod and the same concept to calculate subarray sums.
# Time: O(n), Space: O(k)
from typing import List
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sums = {0: 1}
        tmp = 0
        res = 0
        for n in nums:
            tmp = (tmp + n) % k
            res += sums.get(tmp, 0)
            sums[tmp] = sums.get(tmp, 0) + 1
        return res