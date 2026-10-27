class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        k = end
        def can_finish(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                total_hours += (pile + k - 1) // k 
            
            return total_hours <= h
        while start <= end:
            mid = (start+end)//2
            if can_finish(mid):
                end = mid-1
                k = mid
            else:
                start = mid+1
        return k
