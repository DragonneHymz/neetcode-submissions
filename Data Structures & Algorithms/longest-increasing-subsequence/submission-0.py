class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #define table
        dp = [1]*len(nums)

        #iterate through all possible states
        for i in range(len(nums)):
            #check table for previous states
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)