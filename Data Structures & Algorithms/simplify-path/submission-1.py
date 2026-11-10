class Solution:
    def simplifyPath(self, path: str) -> str:
        import re
        path = re.sub(r'/+', '/', path).strip("/")
        paths = path.split("/")
        ans = []
        for p in paths:
            if p==".." and len(ans)>0:
                ans.pop()
            elif p!=".." and p!=".":
                ans.append(p)
        return "/"+"/".join(ans)