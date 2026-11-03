class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = dict()
        def helper(sidx, tidx):
            if (sidx,tidx) in dp:
                return dp[(sidx,tidx)]
            if tidx==len(t):
                dp[(sidx,tidx)]=1
                return dp[(sidx,tidx)]
            if sidx==len(s):
                dp[(sidx,tidx)]=0
                return dp[(sidx,tidx)]
            tmp = 0
            if s[sidx]==t[tidx]:
                tmp+=helper(sidx+1,tidx+1)
            tmp += helper(sidx+1,tidx)
            dp[(sidx,tidx)]=tmp
            return tmp
        return helper(0,0)