class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds=dict()
        distinct = set()

        for i in range(n):
            ds[i]=i

        def find(point):
            og = point
            while point!=ds[point]:
                point=ds[point]
            ds[og]=point
            return point
        def merge(pointA, pointB):
            if find(pointA) != find(pointB):
                ds[find(pointB)]=find(pointA)
        for edge in edges:
            merge(edge[0], edge[1])

        ans = 0
        for i in range(n):
            if find(i) not in distinct:
                distinct.add(find(i))
                ans+=1
        return ans