class Solution:
    def __init__(self):
        self.st=set()
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        bitmask = 2**len(nums)
        nums.sort()
        res = []
        for i in range(bitmask):
            sb, dupl = self.makesubset(nums,i)
            if not dupl:
                res.append(sb)
        return res
    def makesubset(self, nums: List[int], bitmask: int) -> List[List[int]]:
        res=[]
        i = 0
        while bitmask > 0:
            if bitmask%2==1:
                res.append(nums[i])
            i = i+1
            bitmask = bitmask//2
        used = tuple(res)
        dupl = used in self.st
        self.st.add(used)
        return res, dupl