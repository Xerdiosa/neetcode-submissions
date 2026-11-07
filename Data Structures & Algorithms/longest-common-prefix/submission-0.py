class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=[]
        br = False
        for i in range(len(strs[0])):
            for s in strs[1:]:
                if i>=len(s):
                    br=True
                    break
                if strs[0][i]!=s[i]:
                    br=True
                    break
            if br:
                break
            ans.append(strs[0][i])
        return "".join(ans)
        