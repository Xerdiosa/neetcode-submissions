class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        q = deque(list(senate))
        delr = 0
        deld = 0
        rcount = 0
        dcount = 0
        for i in list(senate):
            if i == "R":
                rcount+=1
            else:
                dcount+=1
        while rcount>0 and dcount>0:
            curr = q.popleft()
            if curr == "R":
                if delr>0:
                    delr-=1
                    continue
                deld+=1
                dcount-=1
                q.append(curr)
            else:
                if deld>0:
                    deld-=1
                    continue
                delr+=1
                rcount-=1
                q.append(curr)
        return "Radiant" if rcount>0 else "Dire"