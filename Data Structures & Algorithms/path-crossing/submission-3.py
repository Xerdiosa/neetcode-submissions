class Solution:
    def isPathCrossing(self, path: str) -> bool:
        pos = (0,0)
        past = set()
        past.add(pos)
        for i in path:
            if i=="N":
                pos = (pos[0]+1,pos[1])
            if i=="E":
                pos = (pos[0],pos[1]+1)
            if i=="S":
                pos = (pos[0]-1,pos[1])
            if i=="W":
                pos = (pos[0],pos[1]-1)
            if pos in past:
                return True
            past.add(pos)
        return False