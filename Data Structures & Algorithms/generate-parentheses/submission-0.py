class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        tmp = []
        def helper(l, o, c):
            if l==n*2:
                ans.append("".join(tmp))
            if o>0:
                tmp.append("(")
                helper(l+1, o-1, c+1)
                tmp.pop()
            if c>0:
                tmp.append(")")
                helper(l+1, o, c-1)
                tmp.pop()
        helper(0, n, 0)
        return ans