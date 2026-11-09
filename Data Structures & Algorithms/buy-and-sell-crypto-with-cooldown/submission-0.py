class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()
        def helper(day, held):
            if (day,held) in dp:
                return dp[(day, held)]
            if day>=len(prices):
                return 0
            if held is None:
                dp[(day, held)]=max(helper(day+1, prices[day]), helper(day+1, None))
                return dp[(day,held)]
            if held<=prices[day]:
                dp[(day, held)]= max(helper(day+1,held), prices[day]-held+ helper(day+2, None))
                return dp[(day, held)]
            dp[(day, held)]=helper(day+1, held)
            return dp[(day, held)]
        return helper(0, None)