# 6/6/2024
# https://leetcode.com/problems/hand-of-straights/description/
# 846 - Hand of Straights
# Can sort hand first, so that we start looking at the smallest card in hand, that way the "consecutive combination" for that card can only be going up.
# At any point when there's no consecutive cards to form the group, return False, since we've already checked for any cards less than the current one.
# Time: O(nlogn), Space: O(n)
from typing import List
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        count = {}
        for i in hand:
            count[i] = count.get(i, 0) + 1
        hand.sort()
        for i in hand:
            if count[i]:
                for add in range(groupSize):
                    if count.get(i + add, 0) <= 0:
                        return False
                    count[i + add] -= 1
        return True