class Solution(object):
    def combinationSum(self, candidates, t):
        candidates.sort()
        dp = [[] for _ in range(t+1)]
        dp[0] = [[]]
        for i in range(1,t+1):
            for c in candidates:
                if c>i:
                    break
                for co in dp[i-c]:
                    if not co or c >= co[-1]:
                        dp[i].append(co + [c])
        return dp[t]   