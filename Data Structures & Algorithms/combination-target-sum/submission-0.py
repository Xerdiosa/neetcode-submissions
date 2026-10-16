class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        used = set()
        ans = []
        def helper(curr):
            tpl = tuple(sorted(curr))
            if tpl in used:
                return
            used.add(tpl)
            if sum(curr) == target:
                ans.append(curr.copy())
                return
            if sum(curr)>target:
                return
            for i in nums:
                curr.append(i)
                helper(curr)
                curr.pop()
        helper([])
        return ans
        