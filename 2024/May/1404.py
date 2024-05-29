# 5/29/2024
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/description/
# 1404 - Number of Steps to Reduce a Number in Binary Representation to One
# Simple loop through the str representation of the binary number with greedy method.
# Time: O(n), Space: O(1)
class Solution:
    def numSteps(self, s: str) -> int:
        if s == "1":
            return 0
        carryover = 0
        pointer = len(s) - 1
        steps = 0
        while pointer >= 0:
            curr = 0
            if pointer == 0 and s[pointer] == "1" and not carryover:
                return steps
            if pointer >= 0:
                curr += int(s[pointer])
                pointer -= 1
            if curr + carryover == 1:
                steps += 2
                carryover = 1
            else:
                steps += 1
        return steps