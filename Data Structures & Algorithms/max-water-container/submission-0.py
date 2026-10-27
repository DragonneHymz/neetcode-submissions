class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max = 0
        while l<r:
            water = (r-l) * min(heights[l],heights[r])
            if water>max:
                max=water
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return max