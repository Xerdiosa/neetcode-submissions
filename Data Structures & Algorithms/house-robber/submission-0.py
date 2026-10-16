class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans=[0 for _ in range(len(nums)+1)]
        ans[1] = nums[0]
        for i, v in enumerate(nums):
            ans[i+1] = max(ans[i-1]+v,ans[i])
        return ans[len(nums)]
        