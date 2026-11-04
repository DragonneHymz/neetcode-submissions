class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        occurrence = Counter(tasks)
        maxHeap = [-i for i in occurrence.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(maxHeap)
                if c:
                    q.append([c, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
