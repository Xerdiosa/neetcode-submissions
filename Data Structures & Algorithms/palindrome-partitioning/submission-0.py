class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        tmp = []
        def helper(idx,carry):
            ss=s[idx+1-carry:idx+1]
            if idx==len(s)-1:
                if ss==ss[::-1]:
                    tmp.append(ss)
                    ans.append(tmp[:])
                    tmp.pop()
                return
            if ss==ss[::-1]:
                tmp.append(ss)
                helper(idx+1,1)
                tmp.pop()
            helper(idx+1,carry+1)
        helper(0,1)
        return ans

    