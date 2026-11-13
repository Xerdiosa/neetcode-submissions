class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        import heapq
        waiting = []
        avail = []
        ans = []
        for i, task in enumerate(tasks):
            heapq.heappush(waiting, (task[0], task[1], i))
        clock = 0
        while len(waiting)>0 or len(avail)>0:
            if len(avail)==0: #nothing to process, sleep until next task ready
                task = heapq.heappop(waiting)
                clock = task[0]
                heapq.heappush(avail, (task[1], task[2]))
            while len(waiting)>0 and waiting[0][0]<=clock: #push all ready task
                task = heapq.heappop(waiting)
                heapq.heappush(avail, (task[1], task[2]))
            task = heapq.heappop(avail)
            clock+=task[0]
            ans.append(task[1])
            while len(waiting)>0 and waiting[0][0]<=clock: #push all ready task
                task = heapq.heappop(waiting)
                heapq.heappush(avail, (task[1], task[2]))
        return ans
