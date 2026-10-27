class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        def recurse(i, current, target):
            if target < 0:
                return 
            if target == 0:
                res.append(current.copy())
                return
            for index in range(i,len(nums)):
                if nums[index] > target:
                    break
                current.append(nums[index])
                recurse(index, current, target-nums[index])
                current.pop()
        
        recurse(0, [], target)
        return res