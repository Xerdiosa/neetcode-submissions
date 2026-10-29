class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ds = dict()
        for i in range(n):
            ds[i]=i
        def find(n):
            og = [n]
            while ds[n]!=n:
                n=ds[n]
                og.append(n)
            for o in og:
                ds[o]=n
            return n
        def union(a,b):
            if not check(a,b):
                ds[find(a)]=find(b)
        def check(a,b):
            return find(a)==find(b)
        if len(edges)==0:
            return True
        union(edges[0][0], edges[0][1])
        for edge in edges[1:]:
            firstMatch=check(edge[0],edges[0][0])
            secondMatch=check(edge[1],edges[0][0])
            if firstMatch and secondMatch:
                # print("fail1")
                return False
            union(edge[0],edge[1])
        same = set()
        for i in range(n):
            print(f"find({i}):{find(i)}")
            same.add(find(i))
        return len(same)==1
        