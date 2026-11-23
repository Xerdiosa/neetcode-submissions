class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        import math
        def canTravel(a,b):
            return math.gcd(a,b)>1
        ds = [i for i in range(len(nums))]

        def union(idx1,idx2):
            ds[find(idx1)]=find(idx2)

        def find(num):
            toCompress = []
            while ds[num]!=num:
                toCompress.append(num)
                num=ds[num]
            for i in toCompress:
                ds[i]=num
            return num

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if canTravel(nums[i],nums[j]):
                    union(i,j)
        
        king = find(0)
        for i in range(1,len(nums)):
            if find(i)!=king:
                return False
        return True
