# 6/7/2024
# https://leetcode.com/problems/replace-words/description/
# 648 - Replace Words
# Pretty standard trie question, make a trie of the words in dictionary first, then traverse through sentence to see which ones to replace. 
# can be greedy when deciding on what to replace the words in sentence with since it wants the shortest root.
# Time: O(dw + sw), Space: O(dw + sw), where d is length of dictionary, s is length of sentence, w is length of the words in dictionary/sentence
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        bank = {}
        for w in dictionary:
            curr = bank
            for c in w:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr["end"] = True
        res = []
        for w in sentence.split():
            added = False
            curr = bank
            tmp = ""
            for c in w:
                if curr.get("end", False):
                    res.append(tmp)
                    added = True
                    break
                if c not in curr:
                    break
                tmp += c
                curr = curr[c]
            if not added:
                res.append(w)
        return " ".join(res)