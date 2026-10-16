class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = -1
        highest_diff = 0
        for i in prices:
            if lowest == -1:
                lowest = i
                continue
            if i-lowest > highest_diff:
                highest_diff  = i-lowest
            if i < lowest:
                lowest = i
        return highest_diff
        