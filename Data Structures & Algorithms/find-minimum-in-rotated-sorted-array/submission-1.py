class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1
        if nums[start] <= nums[end]:
            return nums[start]
        while start < end:
            mid = (start + end) //2
            if nums[mid] > nums[end]:
                start = mid +1
            else:
                end = mid
        return nums[start]