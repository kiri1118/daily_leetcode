# 6/2/2024
# https://leetcode.com/problems/reverse-string/description/
# 344 - Reverse String
# Loop over the string half of the string List and swap the first and last, second and second last, and so on.
# Time: O(n), Space: O(1)
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for index in range(len(s) // 2):
            s[index], s[-index - 1] = s[-index - 1], s[index]