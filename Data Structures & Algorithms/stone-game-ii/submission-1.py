class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = dict()
        s = sum(piles)
        ps = []
        ps.append(s-piles[0])
        for i in piles[1:]:
            ps.append(ps[-1]-i)
        def helper(n,M):
            if n==len(piles):
                return 0
            if (n,M) in dp:
                return dp[(n,M)]
            ans = -10000 #smaller than constraint
            for i in range(2*M):
                if n+i<len(piles):
                    ans = max(ans, sum(piles[n:n+i+1])+(ps[n+i]-helper(n+1+i,max((i+1),M))))
            dp[(n,M)] = ans
            return ans
        return helper(0,1)