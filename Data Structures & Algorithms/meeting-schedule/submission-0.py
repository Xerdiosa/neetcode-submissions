"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key=lambda i:(i.start,i.end))
        if len(intervals) == 0:
            return True
        start = intervals[0]
        for i in intervals[1:]:
            if start.end>i.start:
                return False
            start=i
        return True