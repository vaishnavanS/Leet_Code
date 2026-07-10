class Solution(object):
    def helper(self, nums):
        dp = [0] * len(nums)
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            r = nums[i] + dp[i - 2]
            s = dp[i - 1]
            dp[i] = max(r, s)
        return dp[-1]
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(
            self.helper(nums[:-1]),  
            self.helper(nums[1:])    
        )