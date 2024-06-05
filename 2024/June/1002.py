# 6/5/2024
# https://leetcode.com/problems/find-common-characters/description/
# 1002 - Find Common Characters
# Loop through each word and each character, the end result desired is the minimum of occurrence of each letter in all the words
# Time: O(n * m), Space: O(1), where m is length constraint of the individual word. space is O(1) because there's only a constant amount of letters (26)
from typing import List
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = [0] * 26
        for c in words[0]:
            count[ord(c) - ord("a")] += 1
        for w in words[1:]:
            tmp = [0] * 26
            for c in w:
                tmp[ord(c) - ord("a")] += 1
            for i in range(26):
                count[i] = min(count[i], tmp[i])
        res = []
        for index in range(26):
            res.extend([chr(ord("a") +  index)] * count[index])
        return res