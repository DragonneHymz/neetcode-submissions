import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]
        heapq.heapify(maxheap)
        while len(maxheap) > 1:
            temp = -heapq.heappop(maxheap)
            temp2 = -heapq.heappop(maxheap)
            total = temp - temp2
            if total != 0:
                heapq.heappush(maxheap, -total)
        
        return -maxheap[0] if maxheap else 0
                

