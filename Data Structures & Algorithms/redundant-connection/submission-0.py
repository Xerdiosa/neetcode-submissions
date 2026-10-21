class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        ds = dict()
        for i in range(1, len(edges)+1):
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
            if find(edge[0])==find(edge[1]):
                return edge #already connected?
            merge(edge[0], edge[1])