class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        used = [False for _ in range(len(nums))]
        def helper():
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                tmp.append(nums[i])
                if len(tmp)==len(nums):
                    ans.append(tmp.copy())
                else:
                    helper()
                used[i]=False
                tmp.pop()
        helper()
        return ans
            