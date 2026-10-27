class MedianFinder:

    def __init__(self):
        # first is max heap, last is min heap
        self.first, self.last = [],[]

    def addNum(self, num: int) -> None:
        if self.last and num > self.last[0]:
            heapq.heappush(self.last, num)
        else:
            heapq.heappush(self.first, -1 * num)
        
        if len(self.first) > len(self.last) +1 :
            val = -1 * heapq.heappop(self.first)
            heapq.heappush(self.last, val)
        
        if len(self.last) > len(self.first)+1 :
            val = heapq.heappop(self.last)
            heapq.heappush(self.first, -1 * val)


    def findMedian(self) -> float:
        if len(self.first) > len(self.last):
            return -1* self.first[0]
        if len(self.last) > len(self.first):
            return self.last[0]
        
        return (-1*self.first[0] + self.last[0])/2
        
        
        