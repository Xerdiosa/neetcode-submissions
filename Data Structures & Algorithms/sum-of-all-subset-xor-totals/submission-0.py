class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        xor = 0
        def helper(n):
            nonlocal ans,xor
            if n == len(nums):
                ans+=xor
                return
            xor = xor^nums[n]
            helper(n+1)
            xor = xor^nums[n]
            helper(n+1)
        helper(0)
        return ans