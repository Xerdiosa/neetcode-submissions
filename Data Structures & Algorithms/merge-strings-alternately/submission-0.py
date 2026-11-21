class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        b = []
        w1Idx = 0
        w2Idx = 0
        while w1Idx<len(word1) or w2Idx<len(word2):
            if w1Idx<len(word1):
                b.append(word1[w1Idx])
                w1Idx+=1
            if w2Idx<len(word2):
                b.append(word2[w2Idx])
                w2Idx+=1
        return "".join(b)