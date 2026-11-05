class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = dict()
        def helper(w1idx, w2idx):
            if (w1idx, w2idx) in dp:
                return dp[(w1idx, w2idx)]
            if w1idx==len(word1) and w2idx==len(word2): #no diff
                dp[(w1idx, w2idx)]=0
                return dp[(w1idx, w2idx)]
            if w1idx==len(word1) or w2idx==len(word2): #add until reach
                dp[(w1idx, w2idx)]=len(word1)-w1idx + len(word2)-w2idx
                return dp[(w1idx, w2idx)]
            if word1[w1idx]==word2[w2idx]: #no diff
                dp[(w1idx, w2idx)]=helper(w1idx+1,w2idx+1)
                return dp[(w1idx, w2idx)]
            dp[(w1idx, w2idx)] = min(
                1+helper(w1idx+1,w2idx),
                1+helper(w1idx,w2idx+1),
                1+helper(w1idx+1,w2idx+1)
            )
            return dp[(w1idx, w2idx)]
        return helper(0,0)