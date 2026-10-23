class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["." for _ in range(n)] for _ in range(n)]
        used = set()
        """
        set have 4 types:
        horizontal -> h
        vertical   -> v
        diagonal positive -> dp
        diagonal negative -> dn
        """
        ans = []
        def backtrack(x):
            if x==n:
                ans.append(["".join(i) for i in board])
                return
            for y in range(0,n):
                if ("h",x) not in used and ("v",y) not in used and ("dp",x+y) not in used and ("dv",x-y) not in used:  
                    board[x][y]="Q"
                    used.add(("h",x))
                    used.add(("v",y))
                    used.add(("dp",x+y))
                    used.add(("dv",x-y))
                    backtrack(x+1)
                    board[x][y]="."
                    used.remove(("h",x))
                    used.remove(("v",y))
                    used.remove(("dp",x+y))
                    used.remove(("dv",x-y))
        backtrack(0)
        return len(ans)