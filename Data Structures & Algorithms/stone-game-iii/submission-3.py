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
            for i in range(3):
                if n+i<len(stoneValue):
                    ans = max(ans, sum(stoneValue[n:n+i+1])+(ps[n+i]-helper(n+1+i)))
            dp[n] = ans
            return ans
        ans = helper(0)
        if ans*2==s:
            return "Tie"
        return "Alice" if ans>s//2 else "Bob"