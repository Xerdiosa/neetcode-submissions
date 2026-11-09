class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        cnt = 1
        while cnt*cnt<=n:
            squares.append(cnt*cnt)
            cnt+=1
        squares.reverse()
        dp = dict()
        dp[0]=0
        print(squares)
        def helper(tgt):
            if tgt in dp:
                return dp[tgt]
            if tgt<0:
                raise Exception(f"negative target {tgt}")
            ans = 100000 # bigger than constraint
            for s in squares:
                if tgt-s<0:
                    continue
                ans=min(ans, 1+helper(tgt-s))
            dp[tgt]=ans
            return ans
        return helper(n)