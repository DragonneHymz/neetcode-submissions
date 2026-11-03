class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = [-i for i in nums]
        heapq.heapify(maxHeap)
        res = 0
        for _ in range(k):
            res = -heapq.heappop(maxHeap)
        return res