class Solution(object):
    def findDisappearedNumbers(self, nums):
        m = len(nums)
        dp = []
        for i in range(1,m+1):
            dp.append(i)
        r = list(set(dp).difference(nums))
        return r
        