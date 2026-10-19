class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.topk=[]
        self.k=k
        for i in nums:
            heapq.heappush(self.topk, i)
            if len(self.topk)>k:
                heapq.heappop(self.topk)

    def add(self, val: int) -> int:
        heapq.heappush(self.topk, val)
        if len(self.topk)>self.k:
            heapq.heappop(self.topk)
        return self.topk[0]
