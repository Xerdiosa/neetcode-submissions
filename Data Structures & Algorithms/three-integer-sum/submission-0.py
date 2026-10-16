class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st = dict()
        ans = set()
        for i, v in enumerate(nums):
            if v not in st:
                st[v] = set()
            st[v].add(i)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = (nums[i]+nums[j])*-1
                if target in st:
                    check = [nums[i],nums[j],target]
                    check.sort()
                    check = tuple(check)
                    if check in ans:
                        continue
                    possibleIndexes = st[target]
                    for k in possibleIndexes:
                        if k!=i and k!=j:
                            ans.add(check)
        return list(ans)