class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        ans=[0 for _ in range(len(nums)+1)]
        ans[1] = nums[0]
        skipfirstans = [0 for _ in range(len(nums)+1)]
        for i in range(1,len(nums)):
            if i==len(nums)-1:
                ans[i+1] = ans[i]
                skipfirstans[i+1] = max(skipfirstans[i-1]+nums[i],skipfirstans[i])
            else:
                ans[i+1] = max(ans[i-1]+nums[i],ans[i])
                skipfirstans[i+1] = max(skipfirstans[i-1]+nums[i],skipfirstans[i])
        return max(ans[len(nums)],skipfirstans[len(nums)])