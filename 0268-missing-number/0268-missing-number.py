class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        v = [-1]*(n+1)
        for i in nums:
            v[i]=1
        for i in range(len(v)):
            if v[i]== -1:
                return i
        else:
            return 0
