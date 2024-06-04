# 6/4/2024
# https://leetcode.com/problems/longest-palindrome/
# 409 - Longest Palindrome
# Simple loop over the string, O(1) because there's only 26 * 2 different characters we can get in the dict.
# Time: O(n), Space: O(1)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        res = 0
        single = 0
        for key in freq:
            res += freq[key] // 2
            single = max(single, freq[key] % 2)
        return res * 2 + single