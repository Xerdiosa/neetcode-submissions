class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr = prices[0]
        for i in prices[1:]:
            if curr > i:
                curr=i
            else:
                ans+=i-curr
                curr=i 
        return ans
