"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        import heapq
        intervals = sorted(intervals, key= lambda x: (x.start, x.end))
        ans = []
        ans.append(0)
        for interval in intervals:
            if ans[0]>interval.start:
                heapq.heappush(ans, 0)
            heapq.heappop(ans)
            heapq.heappush(ans, interval.end)
        return len(ans)
        