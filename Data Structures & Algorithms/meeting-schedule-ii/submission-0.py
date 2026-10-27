"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for meeting in intervals:
            time.append([meeting.start, 1])
            time.append([meeting.end, -1])
        time.sort(key = lambda i:(i[0], i[1]))
        res = count = 0
        for t in time:
            count += t[1]
            res = max(count, res)
        return res