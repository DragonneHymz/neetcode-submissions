class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = nums[i]
            if target-x in nums[i+1:]:
                return [i, nums[i+1:].index(target-x)+i+1]