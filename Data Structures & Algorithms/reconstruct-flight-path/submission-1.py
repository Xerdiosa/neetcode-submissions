class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        import heapq
        trips = dict()
        for ticket in tickets:
            trips[ticket[0]]=trips.get(ticket[0],[])
            heapq.heappush(trips[ticket[0]], ticket[1])
        ans = []
        def traverse(pos):
            nonlocal ans, trips
            while len(trips.get(pos,[]))>0:
                nxt=heapq.heappop(trips[pos])
                traverse(nxt)
            ans.append(pos)
        traverse("JFK")
        return ans[::-1]