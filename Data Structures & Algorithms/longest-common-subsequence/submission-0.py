class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2)>len(text1):
            text1, text2= text2, text1
        dp=dict()
        def helper(t1ss, t2ss):
            if (t1ss, t2ss) in dp:
                return dp[(t1ss, t2ss)]
            if t1ss>=len(text1) or t2ss>=len(text2):
                dp[(t1ss, t2ss)] = 0
                return dp[(t1ss, t2ss)]
            if text1[t1ss]==text2[t2ss]:
                dp[(t1ss, t2ss)] = 1+helper(t1ss+1,t2ss+1)
                return dp[(t1ss, t2ss)]
            dp[(t1ss, t2ss)]= max(helper(t1ss+1,t2ss),helper(t1ss,t2ss+1))
            return dp[(t1ss, t2ss)]
        return helper(0,0)