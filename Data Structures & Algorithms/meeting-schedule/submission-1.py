"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda i:i.start)
        lastEnd = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < lastEnd:
                return False
            else:
                lastEnd = interval.end
        return True