class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        tmp = []
        def helper(nn,kk):
            nonlocal ans, tmp
            if kk == k:
                ans.append(tmp[:])
            for i in range(nn+1, n+1):
                tmp.append(i)
                helper(i, kk+1)
                tmp.pop()
        helper(0,0)
        return ans