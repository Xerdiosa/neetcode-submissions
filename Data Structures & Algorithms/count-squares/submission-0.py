class CountSquares:

    def __init__(self):
        self.points=dict()
        self.v=dict()
        self.h=dict()

    def add(self, point: List[int]) -> None:
        x, y=point[0], point[1]
        p = (x,y)
        self.points[p]=self.points.get(p,0)+1
        self.v[x]=self.v.get(x,dict())
        self.v[x][y]=self.v[x].get(y,0)+1
        # self.h[y]=self.h.get(y,dict())
        # self.h[y][x]=self.h[y].get(x,0)+1

    def count(self, point: List[int]) -> int:
        x, y=point[0], point[1]
        p = (x,y)
        ans = 0
        for i in self.v.get(x,dict()):
            if i==y:
                continue
            r=abs(y-i)
            ans += self.v[x][i]*self.points.get((x-r,i),0)*self.points.get((x-r,y),0)
            ans += self.v[x][i]*self.points.get((x+r,i),0)*self.points.get((x+r,y),0)
        return ans
