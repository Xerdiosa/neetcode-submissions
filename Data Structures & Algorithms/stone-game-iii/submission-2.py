class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = dict()
        s = sum(stoneValue)
        ps = []
        ps.append(s-stoneValue[0])
        for i in stoneValue[1:]:
            ps.append(ps[-1]-i)
        def helper(n):
            if n==len(stoneValue):
                return 0
            if n in dp:
                return dp[n]
            ans = -10000 #smaller than constraint
            ans = max(ans, stoneValue[n]+(ps[n]-helper(n+1)))
            if n+1<len(stoneValue):
                ans = max(ans, stoneValue[n]+stoneValue[n+1]+(ps[n+1]-helper(n+2)))
            if n+2<len(stoneValue):
                ans = max(ans, stoneValue[n]+stoneValue[n+1]+stoneValue[n+2]+(ps[n+2]-helper(n+3)))
            dp[n] = ans
            return ans
        ans = helper(0)
        if ans*2==s:
            return "Tie"
        return "Alice" if ans>s//2 else "Bob"