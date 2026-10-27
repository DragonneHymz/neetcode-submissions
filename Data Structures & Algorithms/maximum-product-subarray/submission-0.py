class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        largest = nums[0]
        smallest = nums[0]
        for num in nums[1:]:
            temp = largest
            largest = max(num, num*largest, num*smallest)
            smallest = min(num, num*temp, num*smallest)
            res = max(res, largest)
        
        return res