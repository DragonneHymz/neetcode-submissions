class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        if k == len(nums):
            return [max(nums)]

        output = []
        for back in range(0, len(nums) - k + 1):
            front = back + k 
            maximum = max(nums[back:front])
            output.append(maximum)

            print("back", back)
            print("front", front)
        return output

        