class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        tmp = []
        ans = []
        used = [False for _ in range(len(nums))]
        nums.sort()
        def helper(idx):
            if idx==len(nums):
                ans.append(tmp[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                tmp.append(nums[i])
                helper(idx+1)
                used[i]=False
                tmp.pop()
        helper(0)
        return ans