class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        used = set()
        ans = []
        def helper(curr,x):
            tpl = tuple(sorted(curr))
          #   if tpl in used:
             #    return
            used.add(tpl)
            if sum(curr) == target:
                ans.append(curr.copy())
                return
            if sum(curr)>target:
                return
            for i in range(x,len(nums)):
                curr.append(nums[i])
                helper(curr,i)
                curr.pop()
        helper([],0)
        return ans
        