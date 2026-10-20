class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        import heapq
        pq = []
        q = deque()
        dct = dict()
        clock = 1

        for i in tasks:
            if i not in dct:
                dct[i]=0
            dct[i]=dct[i]+1
        for k in dct:
            heapq.heappush_max(pq,(dct[k],k))
        first = heapq.heappop_max(pq)
        if first[0]>1:
            for i in range(n):
                q.append(("skipped","tmp"))
            q.append((first[1],first[0]-1))
        # print(f"run {first[1]}")
        while len(pq)>0 or len(q)>0:
            clock+=1
            # print(len(q))
            if len(q)>0:
                popped = q.popleft()
                if popped[0] != "skipped":
                    heapq.heappush_max(pq,(popped[1],popped[0]))
            if len(pq)>0:
                nn = heapq.heappop_max(pq)
                # print(f"run {nn[1]}")
                if nn[0]>1:
                    for i in range(n-len(q)):
                        q.append(("skipped", "tmp"))
                    q.append((nn[1],nn[0]-1))
            # else:
            #     print("skip")
        return clock
            