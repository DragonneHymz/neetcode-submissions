class Solution:
    def rob(self, nums: List[int]) -> int:
        def houserobber1(nums):
            rob1,rob2 = 0,0
            # [rob1, rob2, n, n+1]
            for n in nums:
                temp = max(rob1+n, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        return max(nums[0],houserobber1(nums[1:]), houserobber1(nums[:len(nums)-1]))
        