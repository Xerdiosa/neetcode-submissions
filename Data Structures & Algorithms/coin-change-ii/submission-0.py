class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = dict()
        def helper(s,cu):
            if (s,cu) in dp:
                return dp[(s,cu)]
            if s==amount:
                dp[(s,cu)]=1
                return dp[(s,cu)]
            if s>amount:
                dp[(s,cu)]=0
                return dp[(s,cu)]
            tmp = 0
            for i in range(cu,len(coins)):
                tmp+=helper(s+coins[i],i)
            dp[(s,cu)]=tmp
            return dp[(s,cu)]
        return helper(0,0)