class Solution(object):
    def deleteAndEarn(self, nums):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i,j in freq.items():
            freq[i] = i*j
        mx = max(freq)
        po = [0]*(mx+1)
        for i in freq:
            po[i] = freq[i]
        dp = [0]*len(po)
        dp[0] = po[0]
        if len(po)>1:
            dp[1] = max(po[0],po[1])
        for i in range(2,len(po)):
            r = po[i] + dp[i-2]
            s = dp[i-1]
            dp[i] = max(r,s)
        return dp[-1]
