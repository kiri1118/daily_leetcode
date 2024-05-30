# 5/30/2024
# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/
# 1442 - Count Triplets That Can Form Two Arrays of Equal XOR
# Take advantage of the fact that a == b iff a xor b is 0. If we have a subarray that xor to 0, then any way we can split the subarray into two halves will
# satisfy the triplet condition since any one half xor the other half has to be 0 to fulfill the if condition in the first place, meaning the two halves are equal.
# Time: O(n^2), Space: O(1)
from typing import List
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr) - 1):
            curr = 0
            for j in range(i, len(arr)):
                curr ^= arr[j]
                if curr == 0:
                    res += j - i
        return res