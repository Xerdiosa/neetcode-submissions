class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        import heapq
        pq=[]
        for i in range(len(nums)):
            heapq.heappush(pq,(nums[i],i))
        for i in range(k):
            tomul = heapq.heappop(pq)
            nums[tomul[1]]=tomul[0]*multiplier
            heapq.heappush(pq,(nums[tomul[1]],tomul[1]))
        return nums