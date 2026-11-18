class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        st = set()
        tmp = []
        ans = []
        used = [False for _ in range(len(nums))]
        def helper(idx):
            if idx==len(nums):
                t = tuple(tmp)
                if t not in st:
                    st.add(t)
                    ans.append(tmp[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                tmp.append(nums[i])
                helper(idx+1)
                used[i]=False
                tmp.pop()
        helper(0)
        return ans