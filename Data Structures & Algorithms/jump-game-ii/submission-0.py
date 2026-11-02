class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = [100000 for _ in range(len(nums))]
        ans[-1]=0
        for i in range(len(nums)-2, -1, -1):
            try:
                ans[i]=1+min(ans[i+1:min(i+nums[i]+1,len(nums))])
            except Exception:
                continue
        return ans[0]