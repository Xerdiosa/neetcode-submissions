class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        dct = dict()
        ans = []
        visited = set()
        for i,v in enumerate(nums):
            if target-v not in dct:
                dct[target-v] = []
            dct[target-v].append(i)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if nums[i]+nums[j]+nums[k] in dct:
                        for idx in dct[nums[i]+nums[j]+nums[k]]:
                            if idx==i or idx==j or idx==k:
                                continue
                            tmp = [nums[i],nums[j],nums[k],nums[idx]]
                            tmp.sort()
                            if tuple(tmp) in visited:
                                continue
                            ans.append(tmp[:])
                            visited.add(tuple(tmp))
        return ans
