class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        queue = deque()
        l = r = 0
        res = []
        while r < len(nums):
            
            while queue and queue[0] < l:
                queue.popleft()
                
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            queue.append(r)
            if r-l+1 >= k:
                res.append(nums[queue[0]])
                l+=1
            r+=1

        return res


                
            


                

            

        