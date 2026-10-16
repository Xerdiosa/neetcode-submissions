class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bitmask = 2**len(nums)
        res = []
        for i in range(bitmask):
            res.append(self.makesubset(nums,i))
        return res
    def makesubset(self, nums: List[int], bitmask: int) -> List[List[int]]:
        res=[]
        i = 0
        while bitmask > 0:
            if bitmask%2==1:
                res.append(nums[i])
            i = i+1
            bitmask = bitmask//2
        return res