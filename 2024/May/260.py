# 5/31/2024
# https://leetcode.com/problems/single-number-iii/description/
# 260 - Single Number III
# Looped through input list to add a number to the set if it's not in it and remove otherwise. If the number only appears once, it won't get removed.
# Time: O(n), Space: O(n)
# Doable with O(1) space with bit manipulation using xor
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)