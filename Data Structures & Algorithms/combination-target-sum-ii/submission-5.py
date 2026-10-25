class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums=candidates
        nums.sort()
        ans = []
        tmp = []
        counter = 0
        def helper(idx):
            nonlocal counter
            for i in range(idx, len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                tmp.append(nums[i])
                counter=counter+nums[i]
                if counter>target:
                    counter=counter-nums[i]
                    tmp.pop()
                    break
                if counter==target:
                    ans.append(tmp.copy())
                    counter=counter-nums[i]
                    tmp.pop()
                    break
                helper(i+1)
                counter=counter-nums[i]
                tmp.pop()
        helper(0)
        return ans