class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp=dict()
        def helper(s1idx, s2idx, s3idx):
            if (s1idx, s2idx, s3idx) in dp:
                return dp[(s1idx, s2idx, s3idx)]
            if s1idx==len(s1) and s2idx==len(s2) and s3idx==len(s3):
                return True
            if s3idx==len(s3):
                return False
            ans=False
            if s1idx<len(s1) and s1[s1idx]==s3[s3idx]:
                ans = ans or helper(s1idx+1, s2idx, s3idx+1)
            if s2idx<len(s2) and s2[s2idx]==s3[s3idx]:
                ans = ans or helper(s1idx, s2idx+1, s3idx+1)
            dp[(s1idx, s2idx, s3idx)] = ans
            return ans 
        helper(0,0,0)
        print(dp)
        return helper(0,0,0)