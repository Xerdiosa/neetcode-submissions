class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        ans = [0 for _ in range(len(cost))]
        for i in range(2,len(cost)):
            ans[i]=min(ans[i-2]+cost[i-2], ans[i-1]+cost[i-1])
        return ans[-1]
        
            